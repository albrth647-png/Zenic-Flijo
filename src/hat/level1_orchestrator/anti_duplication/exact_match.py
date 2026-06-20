"""
HAT-ORBITAL Anti-Doble-Llamada — Capa 1: Exact Match.

Verifica si un dispatch con el mismo intent_hash ya fue completado.
Si es así, retorna el resultado cacheado sin re-ejecutar.

Es la capa más barata (~1ms): solo un SELECT a hat_dispatch_registry.
Incluye cache LRU en memoria para evitar queries repetidos al mismo hash.
"""

from __future__ import annotations

from collections import OrderedDict
from typing import Any

from src.hat.level1_orchestrator.ledger.repository import LedgerRepository

# Tamaño máximo del cache LRU en memoria.
_CACHE_MAX_SIZE = 256


class ExactMatchLayer:
    """Capa 1: detecta dispatches idénticos ya completados.

    Coste: ~1ms (cache hit) o ~3ms (cache miss + SELECT).
    Qué detecta: hash idéntico ya completado → devuelve cache.
    """

    def __init__(self, repo: LedgerRepository | None = None) -> None:
        self._repo = repo if repo is not None else LedgerRepository()
        self._cache: OrderedDict[str, dict[str, Any]] = OrderedDict()

    def check(self, intent_hash: str) -> dict[str, Any]:
        """Verifica si el intent_hash ya tiene un dispatch completado.

        Usa cache LRU: si el hash ya fue consultado, devuelve resultado cacheado.

        Args:
            intent_hash: Hash sha256 del intent del usuario.

        Returns:
            dict con duplicate, action, cached_result, reason.
        """
        cached = self._get_cached(intent_hash)
        if cached is not None:
            return cached

        dispatch = self._repo.get_dispatch(intent_hash)
        if dispatch is None:
            result = self._build_proceed("no dispatch found")
        elif dispatch["status"] == "completed":
            result = {
                "duplicate": True,
                "action": "return_cache",
                "cached_result": dispatch.get("result_cache"),
                "reason": "exact match: dispatch already completed",
            }
        else:
            result = self._build_proceed(f"dispatch status is {dispatch['status']}")

        self._set_cached(intent_hash, result)
        return result

    def _get_cached(self, intent_hash: str) -> dict[str, Any] | None:
        """Obtiene resultado del cache LRU. None si no está.

        Args:
            intent_hash: Hash a buscar.

        Returns:
            Resultado cacheado o None.
        """
        if intent_hash in self._cache:
            self._cache.move_to_end(intent_hash)
            return self._cache[intent_hash]
        return None

    def _set_cached(self, intent_hash: str, result: dict[str, Any]) -> None:
        """Guarda resultado en cache LRU con tamaño máximo.

        Args:
            intent_hash: Hash del intent.
            result: Resultado a cachear.
        """
        self._cache[intent_hash] = result
        self._cache.move_to_end(intent_hash)
        while len(self._cache) > _CACHE_MAX_SIZE:
            self._cache.popitem(last=False)

    def clear_cache(self) -> None:
        """Limpia el cache LRU. Útil para tests."""
        self._cache.clear()

    @staticmethod
    def _build_proceed(reason: str) -> dict[str, Any]:
        """Construye respuesta de 'no duplicado, continuar'."""
        return {
            "duplicate": False,
            "action": "proceed",
            "cached_result": None,
            "reason": reason,
        }
