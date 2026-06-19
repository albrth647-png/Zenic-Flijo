"""
HAT-ORBITAL Anti-Doble-Llamada — Capa 2: Idempotency Lock.

Verifica si un dispatch con el mismo intent_hash está actualmente en progreso.
Si es así, el caller debe suscribirse al resultado en vez de duplicar el trabajo.

Coste: ~3ms (1 SELECT + opcional UPDATE).
"""

from __future__ import annotations

from typing import Any

from src.hat.ledger.repository import LedgerRepository


class IdempotencyLayer:
    """Capa 2: detecta dispatches in-progress y gestiona subscribers.

    Coste: ~3ms.
    Qué detecta: hash en ejecución → suscríbete al resultado (no dupliques).
    """

    def __init__(self, repo: LedgerRepository | None = None) -> None:
        self._repo = repo if repo is not None else LedgerRepository()

    def check(self, intent_hash: str) -> dict[str, Any]:
        """Verifica si el intent_hash tiene un dispatch in-progress.

        Args:
            intent_hash: Hash sha256 del intent del usuario.

        Returns:
            dict con:
                - duplicate: bool — True si hay dispatch in-progress
                - action: 'subscribe' si duplicate, 'proceed' si no
                - subscription_id: str | None — ID para suscribirse
                - reason: str
        """
        dispatch = self._repo.get_dispatch(intent_hash)
        if dispatch is None:
            return self._build_proceed("no dispatch found")
        if dispatch["status"] == "in_progress":
            subscriber_count = self._repo.increment_subscriber(intent_hash)
            return {
                "duplicate": True,
                "action": "subscribe",
                "subscription_id": f"sub_{intent_hash[:8]}_{subscriber_count}",
                "reason": f"idempotency: dispatch in_progress, subscriber #{subscriber_count}",
            }
        return self._build_proceed(f"dispatch status is {dispatch['status']}")

    @staticmethod
    def _build_proceed(reason: str) -> dict[str, Any]:
        """Construye respuesta de 'no duplicado, continuar'."""
        return {
            "duplicate": False,
            "action": "proceed",
            "subscription_id": None,
            "reason": reason,
        }
