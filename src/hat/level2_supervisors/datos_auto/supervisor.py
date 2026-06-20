"""
HAT NIVEL 2 — DatosAutoSupervisor
==================================

Sub-orquestador de datos + automatización. NO conoce a Operaciones ni Comunicaciones.

Coordina specialists (Nivel 3):
- DataSpecialist (DataKeeper + Sheets + Drive + PostgreSQL)
- ApiSpecialist (ApiConnector)
- CodeSpecialist (CodeRunner + LogicGate + Autopilot + OpenAI + Ollama)

Implementación completa en M8.
"""

from __future__ import annotations
from typing import Any
from src.core.logging import get_logger

logger = get_logger("hat.level2.datos_auto")


class DatosAutoSupervisor:
    """Sub-orquestador de datos y automatización."""

    domain = "datos_auto"

    def __init__(self, specialists: dict[str, Any] | None = None, ledger: Any = None) -> None:
        self._specialists = specialists or {}
        self._ledger = ledger
        logger.info(
            "DatosAutoSupervisor inicializado con %d specialists",
            len(self._specialists),
        )

    def handle(self, subtask: dict[str, Any]) -> dict[str, Any]:
        """TODO M8: implement keyword-based specialist selection."""
        if not self._specialists:
            return {
                "status": "failed",
                "error": "no specialists available in datos_auto",
                "domain": self.domain,
            }
        name = next(iter(self._specialists))
        specialist = self._specialists[name]
        return specialist.handle(subtask)
