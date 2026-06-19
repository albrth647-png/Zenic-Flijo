"""
HAT-ORBITAL Specialist — Web Researcher.

Specialist del dominio Research. Coordina al QueryBuilderWorker para expandir
queries y retorna los resultados agregados al supervisor.

Como specialist, NO invoca herramientas externas directamente — delega la
construcción de queries al worker y agrega resultados. En F0 (MVP) no hace
búsquedas web reales (eso requeriría skills externas); retorna las queries
expandidas como "plan de búsqueda" para que el supervisor las ejecute luego.

Implementado en F0-D5, ampliado en F0-D6 con AgentCard.
"""

from __future__ import annotations

from typing import Any

from src.agents.base import AgentCapability, AgentConfig, BaseAgent
from src.hat.agents.card_publisher import CardPublisherMixin
from src.hat.agents.cards import AgentCard
from src.hat.agents.workers.query_builder import QueryBuilderWorker
from src.utils.logger import setup_logging

logger = setup_logging(__name__)


class WebResearcherSpecialist(BaseAgent, CardPublisherMixin):
    """Specialist que coordina query building para research web.

    Capabilities:
        - REASONING: decidir si expandir o no
        - DATA_ANALYSIS: agregar resultados
    """

    def __init__(self, config: AgentConfig) -> None:
        super().__init__(config)
        if not config.capabilities:
            config.capabilities = [
                AgentCapability.REASONING,
                AgentCapability.DATA_ANALYSIS,
            ]
        # El specialist crea su propio worker internamente (jerarquía local).
        worker_config = AgentConfig(
            name=f"{self.name}_query_builder",
            description="Query Builder worker spawned by Web Researcher",
            max_iterations=3,
        )
        self._query_builder = QueryBuilderWorker(worker_config)

    def get_card(self) -> AgentCard:
        """Publica la AgentCard de WebResearcher para resonancia RCC."""
        return AgentCard(
            agent_id="web_researcher",
            agent_name="Web Researcher",
            domain="research",
            tier="specialist",
            capabilities=["web_search", "query_expansion", "result_aggregation"],
            cost_per_call=0.02,
            avg_latency_ms=250,
            orbital_keywords=["buscar", "info", "investigar", "search", "find",
                              "qué es", "que es", "documentación", "documentacion"],
            orbital_amplitude=1.5,  # specialists tienen mayor amplitud que workers
            orbital_velocity=0.05,
        )

    def think(self, observation: Any) -> Any:
        """Decide si el input es válido para research.

        Args:
            observation: dict con "query" (str) y opcional "max_variants" (int).

        Returns:
            dict con "query", "max_variants", "valid" (bool). None si invalid.
        """
        if not isinstance(observation, dict):
            return None
        query = observation.get("query")
        if not isinstance(query, str) or not query.strip():
            return None
        max_variants = observation.get("max_variants", 3)
        if not isinstance(max_variants, int) or max_variants < 1:
            max_variants = 3
        return {"query": query, "max_variants": max_variants, "valid": True}

    def act(self, decision: Any) -> Any:
        """Delega al QueryBuilderWorker y agrega resultados.

        Args:
            decision: dict retornado por think() con query, max_variants, valid.

        Returns:
            dict con "queries" (lista), "specialist" (str), "status" (str).
        """
        if not isinstance(decision, dict) or not decision.get("valid"):
            return {
                "queries": [],
                "specialist": self.name,
                "status": "failed",
                "error": "invalid decision",
            }
        # El worker recibe raw_query (no "query") — adaptar contrato.
        worker_input = {
            "raw_query": decision["query"],
            "max_variants": decision["max_variants"],
        }
        worker_result = self._query_builder.run(worker_input)
        if not isinstance(worker_result, dict):
            return {
                "queries": [],
                "specialist": self.name,
                "status": "failed",
                "error": "worker returned non-dict",
            }
        return {
            "queries": worker_result.get("queries", []),
            "specialist": self.name,
            "status": worker_result.get("status", "completed"),
        }
