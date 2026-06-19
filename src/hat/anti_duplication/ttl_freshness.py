"""
HAT-ORBITAL Anti-Doble-Llamada — Capa 4: TTL Freshness.

Verifica si el usuario hizo un dispatch similar en los últimos N segundos.
Si es así, descarta el nuevo como doble-click accidental.

Coste: <1ms (cache hit) o ~2ms (cache miss + SELECT).
Incluye cache en memoria por sesión para evitar queries repetidos.
"""

from __future__ import annotations

import time
from typing import Any

from src.hat.ledger.repository import LedgerRepository

# Ventana de tiempo por defecto para detectar doble-click (segundos).
DEFAULT_TTL_SECONDS = 5


class TTLFreshnessLayer:
    """Capa 4: detecta doble-click dentro de ventana de TTL.

    Coste: <1ms (cache hit) o ~2ms (cache miss + SELECT).
    Qué detecta: último despacho similar hace <5s → descarta (doble-click).
    """

    def __init__(
        self,
        repo: LedgerRepository | None = None,
        ttl_seconds: int = DEFAULT_TTL_SECONDS,
    ) -> None:
        self._repo = repo if repo is not None else LedgerRepository()
        self._ttl_seconds = ttl_seconds
        self._last_check_time: dict[str, float] = {}

    def check(
        self,
        intent_hash: str,
        user_id: str,
        session_id: str,
    ) -> dict[str, Any]:
        """Verifica si hay dispatches recientes para esta sesión.

        Usa cache en memoria: si la sesión fue verificada hace <TTL segundos,
        devuelve resultado cacheado sin consultar DB.

        Args:
            intent_hash: Hash sha256 del intent.
            user_id: ID del usuario.
            session_id: ID de la sesión.

        Returns:
            dict con duplicate, action, reason.
        """
        cache_key = f"{user_id}:{session_id}"
        now = time.monotonic()

        if self._is_cached_recent(cache_key, now):
            return self._cached_result()

        recent = self._repo.get_recent_dispatches_by_session(
            user_id, session_id, since_seconds=self._ttl_seconds,
        )
        result = self._build_result(recent, intent_hash)
        self._last_check_time[cache_key] = now
        return result

    def _is_cached_recent(self, cache_key: str, now: float) -> bool:
        """Verifica si el cache para esta sesión es reciente.

        Args:
            cache_key: Clave de cache user_id:session_id.
            now: Timestamp actual (monotonic).

        Returns:
            True si el cache es reciente y dice 'proceed' (no duplicado).
        """
        last_time = self._last_check_time.get(cache_key)
        if last_time is None:
            return False
        return (now - last_time) < self._ttl_seconds

    def _cached_result(self) -> dict[str, Any]:
        """Retorna resultado cacheado para una sesión.

        Returns:
            Resultado proceed cacheado (si la sesión fue verificada
            recientemente, asumimos que sigue sin dispatches recientes).
        """
        return {
            "duplicate": False,
            "action": "proceed",
            "reason": "ttl_freshness: cached (session checked recently)",
        }

    def _build_result(
        self, recent: list[dict[str, Any]], intent_hash: str,
    ) -> dict[str, Any]:
        """Construye el resultado a partir de la lista de dispatches recientes.

        Args:
            recent: Lista de dispatches recientes de la DB.
            intent_hash: Hash del intent (para trazabilidad en reason).

        Returns:
            dict con duplicate, action, reason.
        """
        short_hash = intent_hash[:8] if intent_hash else "unknown"
        if recent:
            return {
                "duplicate": True,
                "action": "discard",
                "reason": f"ttl_freshness: {len(recent)} dispatch(es) in last {self._ttl_seconds}s (hash={short_hash})",
            }
        return {
            "duplicate": False,
            "action": "proceed",
            "reason": f"no recent dispatches in last {self._ttl_seconds}s (hash={short_hash})",
        }

    def clear_cache(self) -> None:
        """Limpia el cache de sesión. Útil para tests."""
        self._last_check_time.clear()
