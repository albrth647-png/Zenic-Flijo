"""
HAT-ORBITAL Supervisor — Operate Domain.

Tercer dominio de HAT. Coordina specialists de operate:
- MonitorAgentSpecialist
- LogAnalyzerSpecialist
- IncidentResponderSpecialist

Con 3 specialists activa orquestación HIERARCHICAL completa.
HAT-ORBITAL queda con 3 dominios × (1 supervisor + 3 specialists + 3 workers) = 21 agentes.
"""

from __future__ import annotations

from src.agents.base import AgentConfig, BaseAgent
from src.hat.agents.specialists.incident_responder import IncidentResponderSpecialist
from src.hat.agents.specialists.log_analyzer import LogAnalyzerSpecialist
from src.hat.agents.specialists.monitor_agent import MonitorAgentSpecialist
from src.hat.ledger.repository import LedgerRepository
from src.hat.supervisors.base import DomainSupervisor


class OperateSupervisor(DomainSupervisor):
    """Supervisor del dominio Operate.

    Coordina specialists de operate (Monitor, Log Analyzer, Incident Responder).
    Con 3 specialists activa orquestación HIERARCHICAL del MultiAgentOrchestrator.
    """

    domain = "operate"

    def __init__(
        self,
        ledger: LedgerRepository | None = None,
    ) -> None:
        super().__init__(ledger=ledger, orchestrator=None)

    def _load_specialists(self) -> list[type[BaseAgent]]:
        """Retorna las clases de specialists del dominio Operate."""
        return [MonitorAgentSpecialist, LogAnalyzerSpecialist, IncidentResponderSpecialist]

    def _build_configs(self) -> list[AgentConfig]:
        """Retorna las configs para cada specialist."""
        return [
            AgentConfig(
                name="monitor_agent",
                description="Monitor Agent specialist — collects and analyzes service metrics",
                max_iterations=3,
                timeout_seconds=30.0,
            ),
            AgentConfig(
                name="log_analyzer",
                description="Log Analyzer specialist — filters and analyzes service logs",
                max_iterations=3,
                timeout_seconds=30.0,
            ),
            AgentConfig(
                name="incident_responder",
                description="Incident Responder specialist — dispatches alerts for incidents",
                max_iterations=3,
                timeout_seconds=30.0,
            ),
        ]
