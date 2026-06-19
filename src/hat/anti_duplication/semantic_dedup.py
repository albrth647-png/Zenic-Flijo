"""
HAT-ORBITAL Anti-Doble-Llamada — Capa 3: Semantic Dedup.

Detecta si el nuevo intent es semánticamente similar a un dispatch reciente
usando resonancia TOR entre el intent actual y los intents históricos.

En F1-D1 usa una heurística simple basada en similitud de texto (Jaccard
sobre tokens). En F4 se reemplazará por embeddings locales (bge-small).

Coste: ~15-30ms (cálculo de similitud sobre historial).
"""

from __future__ import annotations

from typing import Any

from src.hat.ledger.repository import LedgerRepository
from src.hat.orbital_n0.intent_hasher import normalize_intent

# Umbral de similitud para considerar duplicado semántico.
DEFAULT_SEMANTIC_THRESHOLD = 0.85


class SemanticDedupLayer:
    """Capa 3: detecta duplicados semánticos vía similitud de texto.

    Coste: ~15-30ms.
    Qué detecta: similitud > 0.85 con dispatch reciente → posible duplicado.
    """

    def __init__(
        self,
        repo: LedgerRepository | None = None,
        threshold: float = DEFAULT_SEMANTIC_THRESHOLD,
    ) -> None:
        self._repo = repo if repo is not None else LedgerRepository()
        self._threshold = threshold

    def check(
        self,
        user_id: str,
        session_id: str,
        message: str,
    ) -> dict[str, Any]:
        """Verifica si el message es semánticamente similar a un dispatch reciente.

        Usa similitud de Jaccard sobre tokens normalizados como heurística
        simple. En F4 se reemplazará por embeddings.

        Args:
            user_id: ID del usuario.
            session_id: ID de la sesión.
            message: Texto del usuario a verificar.

        Returns:
            dict con:
                - duplicate: bool — True si similitud > threshold
                - action: 'confirm' si duplicate (pedir confirmación), 'proceed' si no
                - similarity: float — score de similitud [0, 1]
                - reason: str
        """
        progress = self._repo.get_progress(user_id, session_id, limit=10)
        if not progress:
            return self._build_proceed(0.0, "no dispatch history")

        normalized_msg = normalize_intent(message)
        msg_tokens = set(normalized_msg.split())

        max_similarity = 0.0
        for p in progress:
            description = str(p.get("result_summary") or "")
            if not description:
                continue
            desc_tokens = set(normalize_intent(description).split())
            similarity = self._jaccard_similarity(msg_tokens, desc_tokens)
            max_similarity = max(max_similarity, similarity)

        if max_similarity >= self._threshold:
            return {
                "duplicate": True,
                "action": "confirm",
                "similarity": round(max_similarity, 4),
                "reason": f"semantic_dedup: similarity {max_similarity:.4f} >= {self._threshold}",
            }
        return self._build_proceed(max_similarity, f"max similarity {max_similarity:.4f} < {self._threshold}")

    @staticmethod
    def _jaccard_similarity(set_a: set[str], set_b: set[str]) -> float:
        """Calcula similitud de Jaccard entre dos conjuntos de tokens.

        Args:
            set_a: Primer conjunto de tokens.
            set_b: Segundo conjunto de tokens.

        Returns:
            Similitud en [0, 1]. 0 = sin overlap, 1 = idénticos.
        """
        if not set_a and not set_b:
            return 1.0
        union = set_a | set_b
        if not union:
            return 0.0
        intersection = set_a & set_b
        return len(intersection) / len(union)

    @staticmethod
    def _build_proceed(similarity: float, reason: str) -> dict[str, Any]:
        """Construye respuesta de 'no duplicado, continuar'."""
        return {
            "duplicate": False,
            "action": "proceed",
            "similarity": round(similarity, 4),
            "reason": reason,
        }
