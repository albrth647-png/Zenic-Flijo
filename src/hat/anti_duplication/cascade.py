"""
HAT-ORBITAL Anti-Doble-Llamada — Cascade Orquestador.

Ejecuta las 5 capas en cascada, ordenadas de más barata a más cara.
Si cualquier capa detecta duplicado, se cortocircuita el flujo.

Orden de capas (cheapest → most expensive):
1. Exact Match     (~1ms)  — hash idéntico ya completado → devuelve cache
2. Idempotency     (~3ms)  — hash en ejecución → suscríbete al resultado
3. TTL Freshness   (<1ms)  — despacho similar hace <5s → descarta (doble-click)
4. Semantic Dedup  (~15ms) — similitud > 0.85 → pide confirmación
5. Circuit Breaker (~2ms)  — supervisor caído → fallback graceful

Coste total peor caso: ~22-37ms. Probabilidad de doble despacho: <0.01%.
"""

from __future__ import annotations

from typing import Any

from src.hat.anti_duplication.circuit_breaker import CircuitBreakerLayer
from src.hat.anti_duplication.exact_match import ExactMatchLayer
from src.hat.anti_duplication.idempotency import IdempotencyLayer
from src.hat.anti_duplication.semantic_dedup import SemanticDedupLayer
from src.hat.anti_duplication.ttl_freshness import TTLFreshnessLayer
from src.hat.ledger.repository import LedgerRepository
from src.utils.logger import setup_logging

logger = setup_logging(__name__)


class AntiDuplicationCascade:
    """Orquesta las 5 capas anti-doble-llamada en cascada.

    Uso:
        cascade = AntiDuplicationCascade()
        result = cascade.check(
            intent_hash="abc123",
            user_id="user1",
            session_id="sess1",
            message="buscar python",
            domain="research",
        )
        if result["duplicate"]:
            # Cortocircuito: aplicar action (return_cache, subscribe, discard, etc.)
        else:
            # Proceed: ejecutar dispatch normalmente
    """

    def __init__(self, repo: LedgerRepository | None = None) -> None:
        self._repo = repo if repo is not None else LedgerRepository()
        self._exact_match = ExactMatchLayer(repo=self._repo)
        self._idempotency = IdempotencyLayer(repo=self._repo)
        self._ttl_freshness = TTLFreshnessLayer(repo=self._repo)
        self._semantic_dedup = SemanticDedupLayer(repo=self._repo)
        self._circuit_breaker = CircuitBreakerLayer(repo=self._repo)

    def clear_cache(self) -> None:
        """Limpia caches de todas las capas. Útil para tests."""
        self._exact_match.clear_cache()
        self._ttl_freshness.clear_cache()

    def check(
        self,
        intent_hash: str,
        user_id: str,
        session_id: str,
        message: str,
        domain: str,
    ) -> dict[str, Any]:
        """Ejecuta las 5 capas en orden. Cortocircuito en primer duplicado.

        Args:
            intent_hash: Hash sha256 del intent.
            user_id: ID del usuario.
            session_id: ID de la sesión.
            message: Texto original del usuario.
            domain: Dominio destino del dispatch.

        Returns:
            dict con:
                - duplicate: bool
                - action: 'return_cache' | 'subscribe' | 'discard' | 'confirm' | 'fallback' | 'proceed'
                - layer_hit: str — nombre de la capa que detectó (o 'none')
                - cached_result / subscription_id / similarity / failure_count: según action
                - reason: str
        """
        layers = self._build_layer_sequence(
            intent_hash, user_id, session_id, message, domain,
        )
        for layer_name, check_fn in layers:
            result: dict[str, Any] = check_fn()
            if result.get("duplicate"):
                result["layer_hit"] = layer_name
                logger.info(
                    "AntiDupCascade: layer %s triggered (action=%s, reason=%s)",
                    layer_name, result.get("action"), result.get("reason"),
                )
                return result
        return {
            "duplicate": False,
            "action": "proceed",
            "layer_hit": "none",
            "reason": "all layers passed",
        }

    def _build_layer_sequence(
        self,
        intent_hash: str,
        user_id: str,
        session_id: str,
        message: str,
        domain: str,
    ) -> list[tuple[str, Any]]:
        """Construye la secuencia de capas con sus check functions.

        Returns:
            Lista de tuplas (layer_name, check_function) en orden de ejecución.
        """
        return [
            ("exact_match", lambda: self._exact_match.check(intent_hash)),
            ("idempotency", lambda: self._idempotency.check(intent_hash)),
            ("ttl_freshness", lambda: self._ttl_freshness.check(
                intent_hash, user_id, session_id,
            )),
            ("semantic_dedup", lambda: self._semantic_dedup.check(
                user_id, session_id, message,
            )),
            ("circuit_breaker", lambda: self._circuit_breaker.check(
                domain, user_id, session_id,
            )),
        ]
