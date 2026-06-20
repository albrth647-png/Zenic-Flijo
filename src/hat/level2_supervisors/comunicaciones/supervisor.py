"""
HAT NIVEL 2 — ComunicacionesSupervisor
=======================================

Sub-orquestador de comunicaciones. NO conoce a OperacionesSupervisor ni DatosAutoSupervisor.

Coordina specialists de comunicaciones (Nivel 3):
- NotificationSpecialist (email + WhatsApp)
- EmailSpecialist (Gmail)
- ChatSpecialist (Slack + Telegram)

Implementación completa en M8.
"""

from __future__ import annotations
from typing import Any
from src.core.logging import get_logger

logger = get_logger("hat.level2.comunicaciones")


class ComunicacionesSupervisor:
    """Sub-orquestador de comunicaciones."""

    domain = "comunicaciones"

    def __init__(self, specialists: dict[str, Any] | None = None, ledger: Any = None) -> None:
        self._specialists = specialists or {}
        self._ledger = ledger
        logger.info(
            "ComunicacionesSupervisor inicializado con %d specialists",
            len(self._specialists),
        )

    def handle(self, subtask: dict[str, Any]) -> dict[str, Any]:
        """TODO M8: implement keyword-based specialist selection."""
        if not self._specialists:
            return {
                "status": "failed",
                "error": "no specialists available in comunicaciones",
                "domain": self.domain,
            }
        name = next(iter(self._specialists))
        specialist = self._specialists[name]
        return specialist.handle(subtask)
