"""HAT-ORBITAL Nivel 2 — SpecialistRouter base class.

Patrón reutilizable de routing por keywords para los 3 supervisores del Nivel 2.
Cada supervisor define su mapeo ``keyword → specialist_name`` y esta clase
se encarga de hacer el match y despachar al specialist correcto.

Diseño:
- Stateless entre calls (no mantiene estado de sesión).
- Routing por keyword matching case-insensitive sobre el mensaje del subtask.
- Default al primer specialist si ningún keyword matchea (fallback graceful).
- Logging estructurado con specialist seleccionado y razón.

Implementado en M8 siguiendo IMPLEMENTATION_PLAN.md §M8.
"""
from __future__ import annotations

from typing import Any

from src.core.logging import get_logger

logger = get_logger("hat.level2.router")


class SpecialistRouter:
    """Base class para supervisores del Nivel 2 con routing por keywords.

    Subclases deben:
    1. Definir ``self._keyword_map``: dict ``keyword → specialist_name``.
    2. Definir ``self.domain``: nombre del dominio (ej: ``'operaciones'``).
    3. Llamar ``super().__init__(specialists, ledger)`` en su ``__init__``.

    El método :meth:`handle` hace el routing automáticamente:
    1. Extrae el mensaje del subtask (``description`` o ``message``).
    2. Busca keywords en el mensaje (case-insensitive).
    3. Despacha al specialist cuyo nombre aparece en el keyword_map.
    4. Si ningún keyword matchea, usa el primer specialist disponible (fallback).

    Attributes:
        _specialists: Dict ``specialist_name → specialist_instance``.
        _ledger: LedgerRepository opcional (no usado en routing, solo inyectado).
        _keyword_map: Dict ``keyword → specialist_name`` (definido por subclase).
        domain: Nombre del dominio (definido por subclase).
    """

    domain: str = "base"

    def __init__(
        self,
        specialists: dict[str, Any] | None = None,
        ledger: Any = None,
    ) -> None:
        """Inicializa el router con specialists y ledger inyectados.

        Args:
            specialists: Dict ``specialist_name → specialist_instance``.
                Si es None, se usa dict vacío (handle() retornará error).
            ledger: LedgerRepository opcional para persistencia futura.
                No se usa en el routing, pero se mantiene para compatibilidad
                con el constructor original de los supervisores.
        """
        self._specialists: dict[str, Any] = specialists or {}
        self._ledger: Any = ledger
        self._keyword_map: dict[str, str] = {}
        logger.info(
            "%s inicializado con %d specialists",
            type(self).__name__, len(self._specialists),
        )

    def handle(self, subtask: dict[str, Any]) -> dict[str, Any]:
        """Punto de entrada — invocado por HATRouter (Nivel 1).

        Flujo:
        1. Validar que hay specialists disponibles.
        2. Extraer mensaje del subtask.
        3. Seleccionar specialist via ``_select_specialist``.
        4. Despachar al specialist seleccionado.
        5. Retornar resultado estructurado.

        Args:
            subtask: Subtarea con ``description`` o ``message`` y ``params``.

        Returns:
            dict con: status, result/error, domain, specialists_used, duration_ms.
        """
        if not self._specialists:
            return self._build_no_specialists_response()

        specialist_name = self._select_specialist(subtask)
        specialist = self._specialists.get(specialist_name)

        if specialist is None:
            return self._build_specialist_not_found(specialist_name)

        logger.info(
            "%s routing: specialist=%s, domain=%s",
            type(self).__name__, specialist_name, self.domain,
        )

        result: dict[str, Any] = specialist.handle(subtask)
        return self._enrich_result(result, specialist_name)

    def _select_specialist(self, subtask: dict[str, Any]) -> str:
        """Selecciona el specialist basado en keywords del mensaje.

        Busca cada keyword del ``_keyword_map`` en el mensaje (case-insensitive).
        Si múltiples keywords matchean, retorna el primer match encontrado
        (orden de iteración del dict, que en Python 3.7+ es orden de inserción).

        Args:
            subtask: Subtarea con ``description`` o ``message``.

        Returns:
            Nombre del specialist seleccionado. Si ningún keyword matchea,
            retorna el primer specialist disponible (fallback).
        """
        message = self._extract_message(subtask)
        message_lower = message.lower() if message else ""

        for keyword, specialist_name in self._keyword_map.items():
            if keyword in message_lower:
                logger.debug(
                    "%s keyword match: %r → %s",
                    type(self).__name__, keyword, specialist_name,
                )
                return specialist_name

        # Fallback: primer specialist disponible
        return next(iter(self._specialists))

    @staticmethod
    def _extract_message(subtask: dict[str, Any]) -> str:
        """Extrae el mensaje del subtask (description o message).

        Args:
            subtask: Subtarea del HATRouter.

        Returns:
            Texto del mensaje, o string vacío si no hay.
        """
        return (
            subtask.get("description")
            or subtask.get("message")
            or subtask.get("params", {}).get("query", "")
            or ""
        )

    def _build_no_specialists_response(self) -> dict[str, Any]:
        """Construye respuesta de error cuando no hay specialists."""
        return {
            "status": "failed",
            "error": f"no specialists available in {self.domain}",
            "domain": self.domain,
            "specialists_used": [],
            "duration_ms": 0,
        }

    def _build_specialist_not_found(self, name: str) -> dict[str, Any]:
        """Construye respuesta de error cuando el specialist no existe."""
        return {
            "status": "failed",
            "error": f"specialist '{name}' not found in {self.domain}",
            "domain": self.domain,
            "specialists_used": [],
            "duration_ms": 0,
        }

    @staticmethod
    def _enrich_result(result: dict[str, Any], specialist_name: str) -> dict[str, Any]:
        """Enriquece el resultado del specialist con metadata del supervisor.

        Args:
            result: Resultado retornado por el specialist.
            specialist_name: Nombre del specialist que procesó la subtarea.

        Returns:
            Resultado enriquecido con ``specialists_used``.
        """
        if not isinstance(result, dict):
            return result
        result.setdefault("specialists_used", [specialist_name])
        return result

    def __repr__(self) -> str:
        return (
            f"<{type(self).__name__} domain={self.domain!r} "
            f"specialists={list(self._specialists.keys())}>"
        )
