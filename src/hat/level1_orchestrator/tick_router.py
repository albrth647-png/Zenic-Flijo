"""
HAT-ORBITAL Nivel 0 — Tick Router.

Corazón del Nivel 0. Orquesta el flujo end-to-end HAT-ORBITAL:
1. Recibe input del usuario
2. Calcula intent_hash (anti-doble-llamada capa 1+2)
3. Carga sesión del Ledger vía OVCLedgerBridge.load_session()
4. Inyecta user_intent como variable OVC + crea ciclo routing_cycle
5. Ejecuta run_tick() → RCC detecta resonancia con Agent Cards
6. Llama fsm_disambiguate() si diferencia top1-top2 < 0.15
7. Despacha a DomainSupervisor.handle() del dominio ganador
8. Consolidación + persist_session() al Ledger
9. Síntesis de respuesta al usuario

Implementado en F0-D7 siguiendo HAT_ORBITAL_PLAN.md §2.4.
"""

from __future__ import annotations

import time
import uuid
from typing import Any

from src.core.logging import setup_logging
from src.hat.level1_orchestrator.fsm.disambiguator import CLARIFY_DOMAIN
from src.hat.level1_orchestrator.intent.hasher import compute_intent_hash
from src.hat.level1_orchestrator.ledger.ovc_bridge import OVCLedgerBridge
from src.hat.level1_orchestrator.ledger.repository import LedgerRepository
from src.hat.level1_orchestrator.routing import KeywordRouter, OrbitalRouter
from src.orbital.context import OrbitalContext

logger = setup_logging(__name__)

# Threshold para invocar FSM de desambiguación (mantenido para compatibilidad).
_DISAMBIGUATION_THRESHOLD = 0.15


def _get_supervisor_classes() -> dict[str, type]:
    """Retorna mapeo domain → supervisor class (solo fallback).

    M8 hardening: eliminados los lazy imports a Level 2 para respetar
    la arquitectura de 5 niveles (L1 no debe conocer L2 directamente).
    En producción, bootstrap_hat() inyecta supervisor INSTANCES.
    Si se instancia HATRouter() sin supervisors, retorna dict vacío.
    """
    return {}


class HATRouter:
    """Orquestador principal del Nivel 0 HAT-ORBITAL.

    Coordina Ledger, OrbitalContext, FSM de desambiguación y DomainSupervisors.
    Thread-unsafe: cada request debe crear su propio HATRouter o serializar accesos.
    """

    def __init__(
        self,
        ledger: LedgerRepository | None = None,
        ctx: OrbitalContext | None = None,
        bridge: OVCLedgerBridge | None = None,
        supervisors: dict[str, Any] | None = None,
    ) -> None:
        """Inicializa el router con dependencias inyectadas.

        Args:
            ledger: LedgerRepository. None → crea uno nuevo.
            ctx: OrbitalContext. None → usa singleton.
            bridge: OVCLedgerBridge. None → crea uno con ledger+ctx.
            supervisors: dict domain→supervisor instance. None → vacío {}.
        """
        self._ledger = ledger if ledger is not None else LedgerRepository()
        self._ctx = ctx if ctx is not None else OrbitalContext()  # type: ignore[no-untyped-call]
        self._bridge = bridge if bridge is not None else OVCLedgerBridge(
            repo=self._ledger, ctx=self._ctx,
        )
        # Supervisores del Nivel 2 inyectados por bootstrap.py.
        self._supervisors = supervisors if supervisors is not None else {}
        # Routers extraídos en M8 (routing orbital + keyword override).
        self._orbital_router = OrbitalRouter(ctx=self._ctx)
        self._keyword_router = KeywordRouter()
        # Session ID actual para namespacing OVC (seteado en handle()).
        self._current_session_id: str = "default"

    def handle(
        self,
        user_id: str,
        session_id: str,
        message: str,
        context: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Procesa un mensaje del usuario end-to-end y retorna la respuesta.

        Flujo:
        1. Calcular intent_hash
        2. Registrar dispatch (anti-doble capa 2)
        3. Cargar sesión del Ledger
        4. Ruteo por resonancia ORBITAL
        5. Despachar al supervisor del dominio ganador
        6. Consolidar + persistir
        7. Sintetizar respuesta

        Args:
            user_id: ID del usuario.
            session_id: ID de la sesión.
            message: Texto del usuario.
            context: Contexto adicional opcional (params, etc.).

        Returns:
            dict con: dispatch_id, domain, response, orbital_resonance,
            anti_dup_layer_hit, duration_ms, facts_updated.
        """
        start = time.monotonic()
        dispatch_id = f"disp_{uuid.uuid4().hex[:12]}"
        intent_hash = compute_intent_hash(user_id, session_id, message, context)
        params = context or {}

        # M8: establecer session_id en los routers extraídos.
        self._set_current_session(session_id)

        # FIX CRÍTICO M8: cargar sesión ANTES de ruteo orbital.
        self._bridge.load_session(user_id, session_id)

        # M8: ruteo delegado a OrbitalRouter + KeywordRouter.
        top3 = self._orbital_router.route(message)
        active_domain = self._get_active_domain(user_id, session_id)
        self._keyword_router.set_active_domain(active_domain)
        domain = self._keyword_router.disambiguate(top3, message)

        anti_dup_result = self._run_anti_dup_cascade(
            intent_hash, user_id, session_id, message, domain,
        )
        if anti_dup_result["duplicate"]:
            return self._build_anti_dup_response(
                anti_dup_result, dispatch_id, domain, start,
            )

        # 2. Registrar dispatch (anti-doble capa 2 idempotency)
        self._ledger.register_dispatch(
            intent_hash=intent_hash,
            user_id=user_id,
            session_id=session_id,
            domain=domain,
        )

        # 3. Despachar al supervisor
        subtask = {
            "dispatch_id": dispatch_id,
            "user_id": user_id,
            "session_id": session_id,
            "description": message,
            "parent_intent": message,
            "params": {**params, "query": message},
            "orbital_resonance": top3[0][1] if top3 else 0.0,
        }

        if domain == CLARIFY_DOMAIN:
            supervisor_result = self._build_clarify_response(message)
        else:
            supervisor_result = self._dispatch_to_supervisor(domain, subtask)

        # 5. Consolidar
        resonance = top3[0][1] if top3 else 0.0
        self._ledger.complete_dispatch(intent_hash, supervisor_result, status="completed")

        # 6. Persistir sesión al Ledger
        self._bridge.persist_session(user_id, session_id)

        # 7. Sintetizar respuesta
        duration_ms = int((time.monotonic() - start) * 1000)
        return self._synthesize_response(
            dispatch_id, domain, supervisor_result, resonance, duration_ms,
            "none",
        )

    def _run_anti_dup_cascade(
        self,
        intent_hash: str,
        user_id: str,
        session_id: str,
        message: str,
        domain: str,
    ) -> dict[str, Any]:
        """Ejecuta el cascade anti-doble-llamada de 5 capas.

        Args:
            intent_hash: Hash del intent.
            user_id: ID del usuario.
            session_id: ID de la sesión.
            message: Texto del usuario.
            domain: Dominio destino.

        Returns:
            Resultado del cascade con duplicate/action/layer_hit.
        """
        from src.hat.level1_orchestrator.anti_duplication.cascade import AntiDuplicationCascade

        cascade = AntiDuplicationCascade(repo=self._ledger)
        return cascade.check(
            intent_hash=intent_hash,
            user_id=user_id,
            session_id=session_id,
            message=message,
            domain=domain if domain != CLARIFY_DOMAIN else "clarify",
        )

    @staticmethod
    def _build_anti_dup_response(
        anti_dup_result: dict[str, Any],
        dispatch_id: str,
        domain: str,
        start: float,
    ) -> dict[str, Any]:
        """Construye la respuesta cuando el cascade detecta duplicado.

        Args:
            anti_dup_result: Resultado del cascade.
            dispatch_id: ID del despacho.
            domain: Dominio ganador.
            start: Timestamp de inicio.

        Returns:
            dict con respuesta anti-dup para el usuario.
        """
        action = anti_dup_result.get("action", "proceed")
        layer = anti_dup_result.get("layer_hit", "unknown")
        cached = anti_dup_result.get("cached_result")

        response_text = HATRouter._anti_dup_response_text(action, layer, cached)

        return {
            "dispatch_id": dispatch_id,
            "domain": domain,
            "response": response_text,
            "orbital_resonance": 0.0,
            "anti_dup_layer_hit": layer,
            "duration_ms": int((time.monotonic() - start) * 1000),
            "facts_updated": [],
            "status": "anti_dup_blocked",
        }

    @staticmethod
    def _anti_dup_response_text(
        action: str, layer: str, cached: Any,
    ) -> str:
        """Genera texto de respuesta para cada acción anti-dup.

        Args:
            action: Acción del cascade ('return_cache', 'subscribe', etc.).
            layer: Nombre de la capa que detectó.
            cached: Resultado cacheado si action='return_cache'.

        Returns:
            Texto legible para el usuario.
        """
        if action == "return_cache" and cached is not None:
            return f"Resultado cacheado (capa: {layer}): {cached}"
        if action == "subscribe":
            return (
                f"Tu solicitud está siendo procesada. "
                f"Te notificaremos cuando termine (capa: {layer})."
            )
        if action == "discard":
            return (
                f"Detectamos un doble-click. "
                f"Ignorando la solicitud duplicada (capa: {layer})."
            )
        if action == "confirm":
            return (
                f"Tu solicitud parece similar a una anterior. "
                f"¿Confirmas que quieres procesarla de nuevo? (capa: {layer})"
            )
        if action == "fallback":
            return (
                f"El dominio solicitado tiene problemas temporales. "
                f"Usando fallback (capa: {layer})."
            )
        return f"Solicitud bloqueada por anti-doble-llamada (capa: {layer})."

    def _set_current_session(self, session_id: str) -> None:
        """Establece el session_id en ambos routers extraídos (M8).

        Delega a ``OrbitalRouter.set_session()``. El KeywordRouter es stateless
        respecto a la sesión (no namespacing), solo se le pasa active_domain.
        """
        self._current_session_id = session_id
        self._orbital_router.set_session(session_id)

    def _route_by_orbital(self, message: str) -> list[tuple[str, float]]:
        """Delegado a ``OrbitalRouter.route()`` (M8).

        Mantenido como wrapper fino para compatibilidad con tests existentes
        que llaman ``hat_router._route_by_orbital()`` directamente.
        """
        return self._orbital_router.route(message)

    def _disambiguate(
        self,
        top3: list[tuple[str, float]],
        message: str,
        active_domain: str | None,
    ) -> str:
        """Delegado a ``KeywordRouter.disambiguate()`` (M8).

        Mantenido como wrapper fino para compatibilidad con tests existentes.
        """
        self._keyword_router.set_active_domain(active_domain)
        return self._keyword_router.disambiguate(top3, message)

    def _dispatch_to_supervisor(
        self, domain: str, subtask: dict[str, Any],
    ) -> dict[str, Any]:
        """Despacha la subtarea al supervisor del dominio ganador.

        Args:
            domain: Dominio ganador ('operaciones', 'comunicaciones', 'datos_auto').
            subtask: Subtarea a procesar.

        Returns:
            dict con status, result, specialists_used, duration_ms.
        """
        supervisor = self._supervisors.get(domain)
        if supervisor is None:
            return {
                "status": "failed",
                "result": None,
                "error": f"no supervisor for domain {domain!r}",
                "specialists_used": [],
                "duration_ms": 0,
            }
        result: dict[str, Any] = supervisor.handle(subtask)
        return result

    def _build_clarify_response(self, message: str) -> dict[str, Any]:
        """Construye respuesta cuando FSM no resuelve (dominio = 'clarify').

        Args:
            message: Texto original del usuario.

        Returns:
            dict con status='clarify', result con mensaje pidiendo aclaración.
        """
        return {
            "status": "clarify",
            "result": {
                "clarify_message": (
                    f"No estoy seguro de qué quieres hacer con: {message!r}. "
                    "¿Puedes ser más específico?"
                ),
                "suggestions": [
                    "crear lead para Juan",
                    "enviar email a cliente@example.com",
                    "ejecutar código Python",
                    "listar productos del inventario",
                ],
            },
            "specialists_used": [],
            "duration_ms": 0,
        }

    def _get_active_domain(self, user_id: str, session_id: str) -> str | None:
        """Obtiene el dominio activo del Ledger (Fact 'active_domain').

        Args:
            user_id: ID del usuario.
            session_id: ID de la sesión.

        Returns:
            Dominio activo o None si no hay Fact.
        """
        fact = self._ledger.get_fact(user_id, session_id, "active_domain")
        if fact is None:
            return None
        value = fact.get("fact_value")
        if isinstance(value, str):
            return value
        return None

    def _synthesize_response(
        self,
        dispatch_id: str,
        domain: str,
        supervisor_result: dict[str, Any],
        resonance: float,
        duration_ms: int,
        anti_dup_layer: str = "none",
    ) -> dict[str, Any]:
        """Sintetiza la respuesta final al usuario.

        Args:
            dispatch_id: ID del despacho.
            domain: Dominio ganador.
            supervisor_result: Resultado del supervisor.
            resonance: Resonancia ORBITAL final.
            duration_ms: Duración total en ms.
            anti_dup_layer: Capa anti-dup que se activó ('none' si ninguna).

        Returns:
            dict con: dispatch_id, domain, response, orbital_resonance,
            anti_dup_layer_hit, duration_ms, facts_updated.
        """
        status = supervisor_result.get("status", "unknown")
        result = supervisor_result.get("result", {})
        response_text = self._extract_response_text(status, result, domain)

        return {
            "dispatch_id": dispatch_id,
            "domain": domain,
            "response": response_text,
            "orbital_resonance": round(resonance, 4),
            "anti_dup_layer_hit": anti_dup_layer,
            "duration_ms": duration_ms,
            "facts_updated": [],
            "status": status,
        }

    @staticmethod
    def _extract_response_text(
        status: str, result: Any, domain: str,
    ) -> str:
        """Extrae texto legible para el usuario desde el resultado del supervisor.

        Args:
            status: Estado del supervisor ('completed', 'failed', 'clarify').
            result: Resultado crudo del supervisor.
            domain: Dominio ganador.

        Returns:
            Texto de respuesta para el usuario.
        """
        if status == "clarify":
            return HATRouter._extract_clarify_text(result)
        if status == "failed":
            return HATRouter._extract_failed_text(result)
        return HATRouter._extract_completed_text(result, domain)

    @staticmethod
    def _extract_clarify_text(result: Any) -> str:
        """Extrae texto para status='clarify'."""
        if isinstance(result, dict):
            msg: str = result.get("clarify_message", "Necesito más información.")
            return msg
        return "Necesito más información."

    @staticmethod
    def _extract_failed_text(result: Any) -> str:
        """Extrae texto para status='failed'."""
        error = ""
        if isinstance(result, dict):
            error = result.get("error", "")
        return f"Error procesando solicitud: {error}"

    @staticmethod
    def _extract_completed_text(result: Any, domain: str) -> str:
        """Extrae texto para status='completed'."""
        if domain == "operaciones" and isinstance(result, dict):
            if "queries" in result:
                return f"Resultado: {', '.join(result['queries'][:3])}"
            if "id" in result:
                return f"Creado con ID: {result['id']}"
            if "number" in result:
                return f"Factura {result['number']} creada"
            return str(result)
        if domain in ("comunicaciones", "datos_auto") and isinstance(result, dict):
            if "status" in result:
                return f"Estado: {result['status']}"
            return str(result)
        return str(result)
