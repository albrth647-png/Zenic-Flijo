"""HAT-ORBITAL Nivel 1 — Orbital Router (extraído de tick_router.py en M8).

Routing por resonancia ORBITAL: inyecta el user_intent como variable OVC,
calcula TOR entre el intent y cada Agent Card publicada, agrupa por dominio,
y retorna el top-3 dominios con mayor resonancia promedio normalizada.

Esta clase es la **capa de routing orbital pura** — no conoce supervisores,
ni FSM, ni anti-dup. Solo conoce OVC, TOR y Agent Cards.

Diseño:
- Stateless entre calls (limpia la variable user_intent al inicio de cada route()).
- Namespacing por session_id para evitar cross-session pollution (fix sistémico #1).
- Filtra cards por ``metadata.type == 'agent_card'`` (fix sistémico #2 — soporta
  cualquier naming convention: ``card_<id>`` o ``hat_<sess>__card_<id>``).

Implementado en M8 siguiendo IMPLEMENTATION_PLAN.md §M8.
"""
from __future__ import annotations

import contextlib
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from src.orbital.context import OrbitalContext


# ── Constantes ──────────────────────────────────────────────────────────
# Orbit group para variables de routing (separadas de facts/hypotheses).
ROUTING_ORBIT_GROUP: str = "hat_routing"

# Metadata type para variables de user_intent (distinto de 'fact', 'hypothesis', 'agent_card').
INTENT_VAR_TYPE: str = "user_intent"

# Cuántos dominios retornar en el top-N.
TOP_N_DOMAINS: int = 3

# Parámetros orbitales del user_intent (constantes — el intent no orbita solo,
# solo genera TOR con las cards).
INTENT_THETA: float = 0.0
INTENT_AMPLITUDE: float = 1.0
INTENT_VELOCITY: float = 0.1


class OrbitalRouter:
    """Router por resonancia ORBITAL — extrae lógica de tick_router.py.

    Recibe un ``OrbitalContext`` (singleton) y un ``session_id`` para
    namespacing. El método principal es :meth:`route`, que retorna el
    top-N dominios ordenados por resonancia descendente.

    Attributes:
        _ctx: OrbitalContext singleton (OVC + TOR + RCC + COD + Espectro).
        _session_id: ID de la sesión actual (para namespacing de variables).
    """

    def __init__(self, ctx: OrbitalContext, session_id: str = "default") -> None:
        """Inicializa el router con contexto orbital y sesión.

        Args:
            ctx: OrbitalContext singleton. Debe tener ``ovc`` y ``tor``.
            session_id: ID de la sesión. Se sanitiza para usar como prefijo
                de nombres de variables OVC (no alfanuméricos → '_').
        """
        self._ctx = ctx
        self._session_id = session_id

    # ── API pública ────────────────────────────────────────────────────

    def set_session(self, session_id: str) -> None:
        """Actualiza el session_id (debe llamarse al inicio de cada handle()).

        Args:
            session_id: ID de la sesión actual.
        """
        self._session_id = session_id

    def route(self, message: str) -> list[tuple[str, float]]:
        """Rutea un mensaje del usuario al top-N dominios por resonancia.

        Flujo:
        1. Limpiar variable user_intent previa de esta sesión (si existe).
        2. Crear variable OVC ``hat_<sess>__user_intent_current`` con el mensaje.
        3. Recolectar Agent Cards agrupadas por dominio.
        4. Para cada dominio, calcular resonancia promedio normalizada.
        5. Retornar top-N dominios ordenados desc.

        Args:
            message: Texto del usuario (se almacena en metadata, no se parsea).

        Returns:
            Lista de tuplas ``(domain, resonance_strength)`` ordenada desc.
            Vacía si no hay Agent Cards registradas en el OVC.
            ``resonance_strength`` está en [0.0, 1.0].
        """
        intent_var_name = self.get_intent_var_name()

        # 1. Limpiar variable de ruteo anterior de esta sesión
        self._clear_intent_variable(intent_var_name)

        # 2. Crear variable orbital para el user_intent (namespaced)
        self._create_intent_variable(intent_var_name, message)

        # 3. Recolectar Agent Cards por dominio
        cards_by_domain = self.collect_cards_by_domain()
        if not cards_by_domain:
            return []

        # 4. Para cada dominio, calcular resonancia con user_intent
        resonances: list[tuple[str, float]] = [
            (domain, self.compute_domain_resonance(domain, card_vars))
            for domain, card_vars in cards_by_domain.items()
        ]

        # 5. Ordenar desc y tomar top-N
        resonances.sort(key=lambda x: x[1], reverse=True)
        return resonances[:TOP_N_DOMAINS]

    # ── Helpers de namespacing ─────────────────────────────────────────

    def get_intent_var_name(self) -> str:
        """Retorna el nombre namespaced de la variable OVC de user_intent.

        Fix sistémico #1: cada sesión tiene su propia variable user_intent
        en vez de una global, evitando cross-session pollution.

        Returns:
            Nombre en formato ``'hat_<sanitized_session_id>__user_intent_current'``.
        """
        safe_id = self._sanitize_session_id(self._session_id)
        return f"hat_{safe_id}__user_intent_current"

    @staticmethod
    def _sanitize_session_id(session_id: str) -> str:
        """Sanitiza un session_id para usar como parte de nombre de variable OVC.

        Caracteres no alfanuméricos se reemplazan por ``_``.

        Args:
            session_id: ID crudo de la sesión.

        Returns:
            ID sanitizado (solo alfanum + _).
        """
        return "".join(c if c.isalnum() else "_" for c in str(session_id))

    # ── Helpers de variables OVC ───────────────────────────────────────

    def _clear_intent_variable(self, intent_var_name: str) -> None:
        """Elimina la variable user_intent previa de esta sesión (si existe)."""
        existing = self._ctx.ovc.get_variable(intent_var_name)
        if existing is not None:
            self._ctx.ovc.delete_variable(intent_var_name)

    def _create_intent_variable(self, intent_var_name: str, message: str) -> None:
        """Crea la variable OVC user_intent para esta sesión.

        Idempotente: si ya existe (race condition rara), se ignora el error.
        """
        with contextlib.suppress(ValueError):
            self._ctx.ovc.create_variable(
                name=intent_var_name,
                theta=INTENT_THETA,
                amplitude=INTENT_AMPLITUDE,
                velocity=INTENT_VELOCITY,
                orbit_group=ROUTING_ORBIT_GROUP,
                metadata={"type": INTENT_VAR_TYPE, "text": message},
            )

    # ── Helpers de Agent Cards ─────────────────────────────────────────

    def collect_cards_by_domain(self) -> dict[str, list[str]]:
        """Agrupa las variables OVC de tipo agent_card por dominio.

        Fix sistémico #2: filtra por ``metadata.type == 'agent_card'`` en vez
        de por prefijo de nombre, para soportar cards con cualquier naming
        (``publish_card`` crea ``card_<id>``, ``load_session`` crea
        ``hat_<sess>__card_<id>``).

        Returns:
            Dict ``domain → lista de nombres de variables OVC``.
            Si no hay cards, retorna dict vacío.
        """
        result: dict[str, list[str]] = {}
        for name, var in self._ctx.ovc.get_all_variables().items():
            metadata = var.metadata or {}
            if metadata.get("type") != "agent_card":
                continue
            domain = metadata.get("domain", "unknown")
            result.setdefault(domain, []).append(name)
        return result

    # ── Cálculo de resonancia ──────────────────────────────────────────

    def compute_domain_resonance(
        self, domain: str, card_vars: list[str],
    ) -> float:
        """Calcula la resonancia promedio normalizada de un dominio.

        Usa TOR entre user_intent y cada card del dominio. La resonancia
        final es ``total_tor / max_possible_tor``, acotada a [0, 1].

        Args:
            domain: Nombre del dominio (no se usa en el cálculo, solo para
                logging futuro — se mantiene por simetría con la API).
            card_vars: Nombres de variables OVC de las cards del dominio.

        Returns:
            Resonancia en [0.0, 1.0]. ``0.0`` si no hay cards, si no hay
            user_intent, o si ``max_possible <= 0``.
        """
        if not card_vars:
            return 0.0
        intent_var_name = self.get_intent_var_name()
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
        self,
        card_vars: list[str],
        user_intent: Any,
        intent_var_name: str,
    ) -> tuple[float, float]:
        """Acumula TOR entre user_intent y cada card. Retorna ``(total, max_possible)``.

        Args:
            card_vars: Nombres de variables OVC de las cards.
            user_intent: VariableOrbital del user_intent.
            intent_var_name: Nombre de la variable user_intent (namespaced).

        Returns:
            Tupla ``(total_abs_tor, max_possible_tor)``.
            - ``total_abs_tor``: suma de ``|TOR(intent, card)|`` para cards válidas.
            - ``max_possible_tor``: suma de ``card.amplitude * intent.amplitude``
              (upper bound teórico de TOR).
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
                # TOR puede fallar si las variables no existen o hay conflicto
                # de tipos — skip silencioso, no rompe el ruteo.
                continue
        return total, max_possible

    # ── Representación ─────────────────────────────────────────────────

    def __repr__(self) -> str:
        return (
            f"<OrbitalRouter session={self._session_id!r} "
            f"vars={self._ctx.ovc.variable_count}>"
        )
