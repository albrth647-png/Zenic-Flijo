"""
HAT NIVEL 2 — OperacionesSupervisor
====================================

Sub-orquestador de operaciones. NO conoce a ComunicacionesSupervisor ni DatosAutoSupervisor.

Coordina specialists de operaciones (Nivel 3):
- CrmSpecialist (gestión de clientes/leads)
- InvoiceSpecialist (facturación)
- InventorySpecialist (inventario/stock)

Routing:
- "cliente", "lead", "venta" → CrmSpecialist
- "factura", "invoice", "cobro" → InvoiceSpecialist
- "producto", "stock", "inventario" → InventorySpecialist

Implementación completa en M8.
"""

from __future__ import annotations
from typing import Any
from src.core.logging import get_logger

logger = get_logger("hat.level2.operaciones")


class OperacionesSupervisor:
    """Sub-orquestador de operaciones.

    Aislamiento: NO importa nada de level2_supervisors/comunicaciones/ ni
    level2_supervisors/datos_auto/. Solo conoce sus specialists (N3).
    """

    domain = "operaciones"

    def __init__(self, specialists: dict[str, Any] | None = None, ledger: Any = None) -> None:
        self._specialists = specialists or {}
        self._ledger = ledger
        logger.info(
            "OperacionesSupervisor inicializado con %d specialists",
            len(self._specialists),
        )

    def handle(self, subtask: dict[str, Any]) -> dict[str, Any]:
        """Punto de entrada — invocado por HATRouter (Nivel 1).

        Full implementation in M8. Placeholder for now.
        """
        # TODO M8: implement _select_specialist based on keywords
        if not self._specialists:
            return {
                "status": "failed",
                "error": "no specialists available in operaciones",
                "domain": self.domain,
            }
        # Default: first specialist
        name = next(iter(self._specialists))
        specialist = self._specialists[name]
        return specialist.handle(subtask)
