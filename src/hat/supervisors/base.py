"""
HAT-ORBITAL Nivel 1 — Domain Supervisor base abstracto.

Cada Supervisor de dominio (Research/Build/Operate) hereda de esta clase.
Aísla su dominio (no conoce a otros supervisores), mantiene contexto local,
aplica políticas locales (rate limits, fallbacks) y delega en specialists
vía MultiAgentOrchestrator con pattern=HIERARCHICAL.

Anti-bug B-05: MultiAgentOrchestrator crashea con 1 agente. Esta base aplica
un guard que evita despachar si solo hay 1 specialist (devuelve fallback graceful).

Implementado en F0-D5 siguiendo HAT_ORBITAL_PLAN.md §4.2.
"""

from __future__ import annotations

import time
from abc import ABC, abstractmethod
from typing import Any

from src.agents.base import AgentConfig, BaseAgent
from src.agents.orchestrator import (
    MultiAgentOrchestrator,
    OrchestrationPattern,
    OrchestrationPlan,
)
from src.hat.ledger.repository import LedgerRepository
from src.utils.logger import setup_logging

logger = setup_logging(__name__)


class DomainSupervisor(ABC):
    """Base para los 3 supervisores de dominio (Research/Build/Operate).

    Cada supervisor:
    - Aísla su dominio (no conoce a otros supervisores)
    - Mantiene contexto local (no sube todo al Orbital)
    - Aplica políticas locales (rate limits, fallbacks)
    - Delega en specialists vía MultiAgentOrchestrator con pattern=HIERARCHICAL

    Subclasses deben implementar:
        - domain: str ("research" | "build" | "operate")
        - _load_specialists(): list[type[BaseAgent]]
        - _build_configs(): list[AgentConfig]
    """

    domain: str = "abstract"

    def __init__(
        self,
        ledger: LedgerRepository | None = None,
        orchestrator: MultiAgentOrchestrator | None = None,
    ) -> None:
        """Inicializa el supervisor con dependencias inyectadas.

        Args:
            ledger: LedgerRepository para persistir progress. None → crea uno.
            orchestrator: MultiAgentOrchestrator. None → usa singleton.
        """
        self._ledger = ledger if ledger is not None else LedgerRepository()
        if orchestrator is not None:
            self._orchestrator = orchestrator
        else:
            self._orchestrator = MultiAgentOrchestrator.get_instance()
        self._specialist_classes = self._load_specialists()
        self._specialist_configs = self._build_configs()

    @abstractmethod
    def _load_specialists(self) -> list[type[BaseAgent]]:
        """Retorna las clases de especialistas para este dominio."""

    @abstractmethod
    def _build_configs(self) -> list[AgentConfig]:
        """Retorna las configs de cada especialista."""

    def handle(self, subtask: dict[str, Any]) -> dict[str, Any]:
        """Maneja una subtarea delegada por el Orbital N0.

        Anti-bug B-05: si solo hay 1 specialist, MultiAgentOrchestrator
        crashea con IndexError. Esta base aplica un guard que devuelve
        un fallback graceful en ese caso.

        Args:
            subtask: dict con "description", "dispatch_id", "params",
                "parent_intent", "user_id", "session_id".

        Returns:
            dict con "status", "result", "specialists_used", "duration_ms".
        """


        start = time.monotonic()
        ctx = self._extract_subtask_context(subtask)

        # Anti-bug B-05: HIERARCHICAL requiere >= 2 agentes (manager + worker).
        if len(self._specialist_classes) < 2:
            logger.warning(
                "DomainSupervisor(%s): solo %d specialist(s) — fallback directo",
                self.domain, len(self._specialist_classes),
            )
            return self._fallback_single_specialist(subtask, start, ctx)

        plan = self._build_orchestration_plan(subtask, ctx["dispatch_id"])
        try:
            result = self._orchestrator.orchestrate(plan)
        except Exception as exc:
            logger.error("DomainSupervisor(%s) orchestrate failed: %s", self.domain, exc)
            self._record_progress(ctx["user_id"], ctx["session_id"],
                                  ctx["dispatch_id"], "failed", str(exc), None)
            return self._build_failure_response(exc, start)

        self._record_progress(
            ctx["user_id"], ctx["session_id"], ctx["dispatch_id"],
            "completed" if result.success else "failed",
            result.final_result, result.total_duration_ms,
        )
        return self._build_success_response(result, start)

    @staticmethod
    def _extract_subtask_context(subtask: dict[str, Any]) -> dict[str, str]:
        """Extrae user_id, session_id, dispatch_id del subtask con defaults."""
        return {
            "user_id": subtask.get("user_id", "unknown"),
            "session_id": subtask.get("session_id", "unknown"),
            "dispatch_id": subtask.get("dispatch_id", "unknown"),
        }

    def _build_orchestration_plan(
        self, subtask: dict[str, Any], dispatch_id: str,
    ) -> OrchestrationPlan:
        """Construye el OrchestrationPlan HIERARCHICAL para MultiAgentOrchestrator."""
        return OrchestrationPlan(
            pattern=OrchestrationPattern.HIERARCHICAL,
            agent_classes=self._specialist_classes,
            agent_configs=self._specialist_configs,
            input_data=subtask.get("params", subtask),
            max_rounds=3,
            timeout_seconds=120.0,
            metadata={"domain": self.domain, "dispatch_id": dispatch_id},
        )

    @staticmethod
    def _build_failure_response(exc: Exception, start: float) -> dict[str, Any]:
        """Construye la respuesta de fallo con timing."""

        return {
            "status": "failed",
            "result": None,
            "error": str(exc),
            "specialists_used": [],
            "duration_ms": int((time.monotonic() - start) * 1000),
        }

    @staticmethod
    def _build_success_response(result: Any, start: float) -> dict[str, Any]:
        """Construye la respuesta de éxito con specialists usados y timing."""

        return {
            "status": "completed" if result.success else "failed",
            "result": result.final_result,
            "specialists_used": [
                r.get("name") for r in result.agent_results
                if r.get("status") == "success"
            ],
            "duration_ms": int((time.monotonic() - start) * 1000),
        }

    def _fallback_single_specialist(
        self,
        subtask: dict[str, Any],
        start: float,
        ctx: dict[str, str],
    ) -> dict[str, Any]:
        """Fallback cuando solo hay 1 specialist: ejecuta directamente sin orchestrator.

        Args:
            subtask: Subtarea original del Orbital N0.
            start: Timestamp de inicio (monotonic) para cálculo de duration_ms.
            ctx: Contexto extraído con user_id, session_id, dispatch_id.
        """


        if not self._specialist_classes:
            return {
                "status": "failed",
                "result": None,
                "error": "no specialists configured",
                "specialists_used": [],
                "duration_ms": int((time.monotonic() - start) * 1000),
            }

        specialist_class = self._specialist_classes[0]
        config = self._specialist_configs[0]
        try:
            agent = specialist_class(config)
            result = agent.run(subtask.get("params", subtask))
            self._record_progress(ctx["user_id"], ctx["session_id"],
                                  ctx["dispatch_id"], "completed", result, None)
            return {
                "status": "completed",
                "result": result,
                "specialists_used": [config.name],
                "duration_ms": int((time.monotonic() - start) * 1000),
            }
        except Exception as exc:
            logger.error("Fallback specialist failed: %s", exc)
            self._record_progress(ctx["user_id"], ctx["session_id"],
                                  ctx["dispatch_id"], "failed", str(exc), None)
            return self._build_failure_response(exc, start)

    def _record_progress(
        self,
        user_id: str,
        session_id: str,
        dispatch_id: str,
        status: str,
        result_summary: Any,
        orbital_resonance: float | None,
    ) -> None:
        """Persiste el resultado de un despacho en el Ledger."""
        try:
            self._ledger.record_progress(
                user_id=user_id,
                session_id=session_id,
                dispatch_id=dispatch_id,
                domain=self.domain,
                status=status,
                result_summary=result_summary if isinstance(result_summary, (dict, str)) else str(result_summary),
                orbital_resonance=orbital_resonance,
            )
        except Exception as exc:
            logger.warning("Failed to record progress: %s", exc)

    @property
    def specialist_count(self) -> int:
        """Número de specialists configurados."""
        return len(self._specialist_classes)

    @property
    def domain_name(self) -> str:
        """Nombre del dominio (research/build/operate)."""
        return self.domain
