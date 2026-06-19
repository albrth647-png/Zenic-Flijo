"""
HAT-ORBITAL Anti-Doble-Llamada — Capa 5: Circuit Breaker.

Verifica si el dominio destino tiene un historial de fallos reciente.
Si es así, aplica fallback graceful en vez de seguir despachando.

Coste: ~2ms (consulta a hat_progress).
"""

from __future__ import annotations

from typing import Any

from src.hat.ledger.repository import LedgerRepository

# Número de fallos consecutivos para abrir el circuito.
DEFAULT_FAILURE_THRESHOLD = 3


class CircuitBreakerLayer:
    """Capa 5: detecta dominios con historial de fallos reciente.

    Coste: ~2ms.
    Qué detecta: dominio con >= N fallos consecutivos → fallback graceful.
    """

    def __init__(
        self,
        repo: LedgerRepository | None = None,
        failure_threshold: int = DEFAULT_FAILURE_THRESHOLD,
    ) -> None:
        self._repo = repo if repo is not None else LedgerRepository()
        self._failure_threshold = failure_threshold

    def check(self, domain: str, user_id: str, session_id: str) -> dict[str, Any]:
        """Verifica si el dominio tiene fallos consecutivos recientes.

        Args:
            domain: Dominio destino del dispatch.
            user_id: ID del usuario.
            session_id: ID de la sesión.

        Returns:
            dict con:
                - duplicate: bool — True si el circuito está abierto
                - action: 'fallback' si duplicate, 'proceed' si no
                - failure_count: int — fallos consecutivos detectados
                - reason: str
        """
        progress = self._repo.get_progress(user_id, session_id, limit=20)
        domain_progress = [p for p in progress if p.get("domain") == domain]
        if not domain_progress:
            return self._build_proceed(0, "no progress for domain")

        consecutive_failures = self._count_consecutive_failures(domain_progress)
        if consecutive_failures >= self._failure_threshold:
            return {
                "duplicate": True,
                "action": "fallback",
                "failure_count": consecutive_failures,
                "reason": f"circuit_breaker: {consecutive_failures} consecutive failures for {domain}",
            }
        return self._build_proceed(consecutive_failures, f"{consecutive_failures} consecutive failures")

    @staticmethod
    def _count_consecutive_failures(progress: list[dict[str, Any]]) -> int:
        """Cuenta fallos consecutivos desde el más reciente hacia atrás.

        Args:
            progress: Lista de dispatches ordenada por started_at DESC.

        Returns:
            Número de fallos consecutivos (0 si el último fue exitoso).
        """
        count = 0
        for p in progress:
            if p.get("status") == "failed":
                count += 1
            else:
                break
        return count

    @staticmethod
    def _build_proceed(failure_count: int, reason: str) -> dict[str, Any]:
        """Construye respuesta de 'circuito cerrado, continuar'."""
        return {
            "duplicate": False,
            "action": "proceed",
            "failure_count": failure_count,
            "reason": reason,
        }
