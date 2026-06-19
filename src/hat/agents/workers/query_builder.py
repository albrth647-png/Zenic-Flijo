"""
HAT-ORBITAL Worker — Query Builder.

Worker atómico del dominio Research. Toma una query cruda del usuario y
genera 1-3 queries expandidas (sinónimos, variantes, términos técnicos).

Es un BaseAgent simple: think() decide qué expansiones aplicar, act() las genera.
No invoca tools externas — la expansión es determinista y local.

Implementado en F0-D5, ampliado en F0-D6 con AgentCard.
"""

from __future__ import annotations

from typing import Any

from src.agents.base import AgentCapability, AgentConfig, BaseAgent
from src.hat.agents.card_publisher import CardPublisherMixin
from src.hat.agents.cards import AgentCard
from src.utils.logger import setup_logging

logger = setup_logging(__name__)

# Sinónimos básicos para expansión de queries (ES/EN). Mínimo, modificable.
_QUERY_SYNONYMS: dict[str, tuple[str, ...]] = {
    "python": ("python3", "cpython"),
    "javascript": ("js", "ecmascript"),
    "factura": ("invoice", "recibo"),
    "cliente": ("customer", "lead"),
    "error": ("bug", "exception", "fallo"),
    "rápido": ("fast", "veloz", "rápidamente"),
}


class QueryBuilderWorker(BaseAgent, CardPublisherMixin):
    """Worker que expande una query cruda en variantes para búsqueda.

    Capabilities:
        - QUERY_CONSTRUCTION: generar queries a partir de raw_input
        - QUERY_EXPANSION: añadir sinónimos y variantes
    """

    def __init__(self, config: AgentConfig) -> None:
        super().__init__(config)
        if not config.capabilities:
            config.capabilities = [AgentCapability.REASONING]

    def get_card(self) -> AgentCard:
        """Publica la AgentCard de QueryBuilder para resonancia RCC."""
        return AgentCard(
            agent_id="query_builder",
            agent_name="Query Builder",
            domain="research",
            tier="worker",
            capabilities=["query_construction", "query_expansion"],
            cost_per_call=0.0,
            avg_latency_ms=10,
            orbital_keywords=["query", "búsqueda", "buscar", "expansión"],
            orbital_amplitude=0.8,  # workers tienen menor amplitud que specialists
            orbital_velocity=0.1,
        )

    def think(self, observation: Any) -> Any:
        """Decide qué expansiones aplicar basándose en el input.

        Args:
            observation: dict con "raw_query" (str) y opcional "max_variants" (int).

        Returns:
            dict con "raw_query", "synonyms_found" (lista de tuplas), "max_variants".
            None si el input es inválido.
        """
        if not isinstance(observation, dict):
            return None
        raw_query = observation.get("raw_query")
        if not isinstance(raw_query, str) or not raw_query.strip():
            return None
        max_variants = observation.get("max_variants", 3)
        if not isinstance(max_variants, int) or max_variants < 1:
            max_variants = 3

        synonyms_found = self._find_synonyms(raw_query)
        return {
            "raw_query": raw_query,
            "synonyms_found": synonyms_found,
            "max_variants": max_variants,
        }

    def act(self, decision: Any) -> Any:
        """Genera las queries expandidas a partir de la decisión de think().

        Args:
            decision: dict retornado por think() con raw_query, synonyms_found, max_variants.

        Returns:
            dict con "queries" (lista de strings) y "status" ("completed").
        """
        if not isinstance(decision, dict):
            return {"queries": [], "status": "failed", "error": "invalid decision"}
        raw = decision["raw_query"]
        synonyms = decision["synonyms_found"]
        max_v = decision["max_variants"]

        queries = [raw]  # la query original siempre se incluye
        for word, syns in synonyms:
            for syn in syns:
                if len(queries) >= max_v:
                    break
                expanded = raw.replace(word, syn)
                if expanded != raw and expanded not in queries:
                    queries.append(expanded)

        return {"queries": queries, "status": "completed"}

    @staticmethod
    def _find_synonyms(text: str) -> list[tuple[str, tuple[str, ...]]]:
        """Encuentra sinónimos para palabras presentes en el texto.

        Args:
            text: Texto a analizar (case-insensitive).

        Returns:
            Lista de tuplas (word, synonyms) para cada palabra con sinónimos.
        """
        text_lower = text.lower()
        found: list[tuple[str, tuple[str, ...]]] = []
        for word, syns in _QUERY_SYNONYMS.items():
            if word in text_lower:
                found.append((word, syns))
        return found
