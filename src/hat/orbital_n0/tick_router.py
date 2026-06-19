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

from src.hat.ledger.ovc_bridge import OVCLedgerBridge
from src.hat.ledger.repository import LedgerRepository
from src.hat.orbital_n0.fsm_disambiguator import CLARIFY_DOMAIN, fsm_disambiguate
from src.hat.orbital_n0.intent_hasher import compute_intent_hash
from src.hat.supervisors.build import BuildSupervisor
from src.hat.supervisors.operate import OperateSupervisor
from src.hat.supervisors.research import ResearchSupervisor
from src.orbital.context import OrbitalContext
from src.utils.logger import setup_logging

logger = setup_logging(__name__)

# Threshold para invocar FSM de desambiguación.
_DISAMBIGUATION_THRESHOLD = 0.15

# Dominios disponibles (F0: research, F2: +build, F3: +operate).
_SUPERVISORS_BY_DOMAIN: dict[str, type] = {
    "research": ResearchSupervisor,
    "build": BuildSupervisor,
    "operate": OperateSupervisor,
}


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
            supervisors: dict domain→supervisor instance. None → crea ResearchSupervisor.
        """
        self._ledger = ledger if ledger is not None else LedgerRepository()
        self._ctx = ctx if ctx is not None else OrbitalContext()  # type: ignore[no-untyped-call]
        self._bridge = bridge if bridge is not None else OVCLedgerBridge(
            repo=self._ledger, ctx=self._ctx,
        )
        if supervisors is not None:
            self._supervisors = supervisors
        else:
            self._supervisors = {
                "research": ResearchSupervisor(ledger=self._ledger),
                "build": BuildSupervisor(ledger=self._ledger),
                "operate": OperateSupervisor(ledger=self._ledger),
            }

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

        # Fix sistémico #1: establecer session_id para namespacing OVC
        self._set_current_session(session_id)

        # 1. Anti-doble-llamada cascade (5 capas)
        # Primero ruteo rápido para obtener domain, luego cascade completo.
        top3 = self._route_by_orbital(message)
        active_domain = self._get_active_domain(user_id, session_id)
        domain = self._disambiguate(top3, message, active_domain)

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

        # 3. Cargar sesión del Ledger → variables OVC
        self._bridge.load_session(user_id, session_id)

        # 4. Despachar al supervisor
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
        from src.hat.anti_duplication.cascade import AntiDuplicationCascade

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
            return f"Tu solicitud está siendo procesada. Te notificaremos cuando termine (capa: {layer})."
        if action == "discard":
            return f"Detectamos un doble-click. Ignorando la solicitud duplicada (capa: {layer})."
        if action == "confirm":
            return f"Tu solicitud parece similar a una anterior. ¿Confirmas que quieres procesarla de nuevo? (capa: {layer})"
        if action == "fallback":
            return f"El dominio solicitado tiene problemas temporales. Usando fallback (capa: {layer})."
        return f"Solicitud bloqueada por anti-doble-llamada (capa: {layer})."

    def _route_by_orbital(self, message: str) -> list[tuple[str, float]]:
        """Inyecta user_intent como variable OVC y ejecuta run_tick para ruteo.

        Crea un ciclo orbital entre el user_intent y los Agent Cards disponibles,
        ejecuta run_tick, y retorna los 3 dominios con mayor resonancia RCC.

        Uses session-namespaced variable names to avoid cross-session pollution.

        Args:
            message: Texto normalizado del usuario.

        Returns:
            Lista de tuplas (domain, resonance_strength) ordenada desc.
            Vacía si no hay Agent Cards registradas.
        """
        # Fix sistémico #1: usar prefijo de sesión para namespacing
        intent_var_name = self._get_intent_var_name()

        # Limpiar variable de ruteo anterior de esta sesión
        existing = self._ctx.ovc.get_variable(intent_var_name)
        if existing is not None:
            self._ctx.ovc.delete_variable(intent_var_name)

        # Crear variable orbital para el user_intent (namespaced)
        try:
            self._ctx.ovc.create_variable(
                name=intent_var_name,
                theta=0.0,
                amplitude=1.0,
                velocity=0.1,
                orbit_group="hat_routing",
                metadata={"type": "user_intent", "text": message},
            )
        except ValueError:
            pass  # ya existe (race condition rara)

        # Recopilar Agent Cards por dominio (filtrar por metadata, no por nombre)
        cards_by_domain = self._collect_cards_by_domain()
        if not cards_by_domain:
            return []

        # Para cada dominio, calcular resonancia con user_intent
        resonances: list[tuple[str, float]] = []
        for domain, card_vars in cards_by_domain.items():
            resonance = self._compute_domain_resonance(domain, card_vars)
            resonances.append((domain, resonance))

        # Ordenar desc y tomar top 3
        resonances.sort(key=lambda x: x[1], reverse=True)
        return resonances[:3]

    def _get_intent_var_name(self) -> str:
        """Retorna el nombre namespaced de la variable OVC de user_intent.

        Fix sistémico #1: cada sesión tiene su propia variable user_intent
        en vez de una global, evando cross-session pollution.

        Returns:
            Nombre en formato 'hat_<session_id>__user_intent_current'.
        """
        session_id = getattr(self, "_current_session_id", "default")
        safe_id = "".join(c if c.isalnum() else "_" for c in str(session_id))
        return f"hat_{safe_id}__user_intent_current"

    def _set_current_session(self, session_id: str) -> None:
        """Establece el session_id actual para namespacing de variables OVC.

        Debe llamarse al inicio de handle() antes de cualquier operación OVC.
        """
        self._current_session_id = session_id

    def _collect_cards_by_domain(self) -> dict[str, list[str]]:
        """Agrupa las variables OVC de tipo agent_card por dominio.

        Fix sistémico #2: filtra por metadata.type='agent_card' en vez de
        por prefijo de nombre, para soportar cards con cualquier naming
        (publish_card crea 'card_<id>', load_session crea 'hat_<sess>__card_<id>').

        Returns:
            Dict domain → lista de nombres de variables OVC.
        """
        result: dict[str, list[str]] = {}
        for name, var in self._ctx.ovc.get_all_variables().items():
            metadata = var.metadata or {}
            if metadata.get("type") != "agent_card":
                continue
            domain = metadata.get("domain", "unknown")
            result.setdefault(domain, []).append(name)
        return result

    def _compute_domain_resonance(self, domain: str, card_vars: list[str]) -> float:
        """Calcula la resonancia promedio de un dominio con user_intent.

        Usa TOR entre user_intent y cada card del dominio, promedia los valores.

        Args:
            domain: Nombre del dominio.
            card_vars: Nombres de variables OVC de las cards del dominio.

        Returns:
            Resonancia promedio en [0, 1].
        """
        if not card_vars:
            return 0.0
        intent_var_name = self._get_intent_var_name()
        user_intent = self._ctx.ovc.get_variable(intent_var_name)
        if user_intent is None:
            return 0.0
        total, max_possible = self._accumulate_resonance(
            card_vars, user_intent, intent_var_name,
        )
        if max_possible <= 0:
            return 0.0
        return min(total / max_possible, 1.0)

    def _accumulate_resonance(
        self, card_vars: list[str], user_intent: Any, intent_var_name: str,
    ) -> tuple[float, float]:
        """Acumula TOR entre user_intent y cada card. Retorna (total, max_possible).

        Args:
            card_vars: Nombres de variables OVC de las cards.
            user_intent: VariableOrbital del user_intent.
            intent_var_name: Nombre de la variable user_intent (namespaced).
        """
        tor = self._ctx.tor
        total = 0.0
        max_possible = 0.0
        for card_var_name in card_vars:
            card_var = self._ctx.ovc.get_variable(card_var_name)
            if card_var is None:
                continue
            max_possible += card_var.amplitude * user_intent.amplitude
            try:
                result = tor.calculate(intent_var_name, card_var_name)
                total += abs(result.tor_value)
            except Exception:
                continue
        return total, max_possible

    def _disambiguate(
        self,
        top3: list[tuple[str, float]],
        message: str,
        active_domain: str | None,
    ) -> str:
        """Aplica clear-winner check + FSM desambiguación si es necesario.

        Args:
            top3: Top-3 dominios por resonancia.
            message: Texto del usuario.
            active_domain: Dominio activo del Ledger (Fact "active_domain").

        Returns:
            Dominio ganador: 'research' | 'build' | 'operate' | 'clarify'.
            'clarify' si no hay Agent Cards o FSM no resuelve.
        """
        if not top3:
            return CLARIFY_DOMAIN
        return fsm_disambiguate(top3, message, active_domain)

    def _dispatch_to_supervisor(
        self, domain: str, subtask: dict[str, Any],
    ) -> dict[str, Any]:
        """Despacha la subtarea al supervisor del dominio ganador.

        Args:
            domain: Dominio ganador ('research', 'build', 'operate').
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
                    "buscar info sobre X",
                    "crear código que haga Y",
                    "monitorear servicio Z",
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
        if domain == "research" and isinstance(result, dict):
            queries = result.get("queries", [])
            if queries:
                joined = ", ".join(queries[:3])
                return f"Generé {len(queries)} queries para búsqueda: {joined}"
        if isinstance(result, dict):
            return str(result)
        return str(result)
