"""
HAT-ORBITAL Specialist — Log Analyzer.

Specialist del dominio Operate. Coordina LogFilterWorker.
"""

from __future__ import annotations

from typing import Any

from src.agents.base import AgentCapability, AgentConfig, BaseAgent
from src.hat.agents.card_publisher import CardPublisherMixin
from src.hat.agents.cards import AgentCard
from src.hat.agents.workers.log_filter import LogFilterWorker
from src.utils.logger import setup_logging

logger = setup_logging(__name__)


class LogAnalyzerSpecialist(BaseAgent, CardPublisherMixin):
    """Specialist que analiza logs de servicios."""

    def __init__(self, config: AgentConfig) -> None:
        super().__init__(config)
        if not config.capabilities:
            config.capabilities = [AgentCapability.DATA_ANALYSIS, AgentCapability.REASONING]
        worker_config = AgentConfig(name=f"{self.name}_log_filter", max_iterations=3)
        self._log_filter = LogFilterWorker(worker_config)

    def get_card(self) -> AgentCard:
        return AgentCard(
            agent_id="log_analyzer",
            agent_name="Log Analyzer",
            domain="operate",
            tier="specialist",
            capabilities=["log_analysis", "error_detection", "pattern_matching"],
            cost_per_call=0.01,
            avg_latency_ms=250,
            orbital_keywords=["logs", "error", "errores", "log", "advertencia",
                              "warning", "analizar", "traza", "trace"],
            orbital_amplitude=1.5,
            orbital_velocity=0.05,
        )

    def think(self, observation: Any) -> Any:
        if not isinstance(observation, dict):
            return None
        query = observation.get("query") or observation.get("service")
        if not isinstance(query, str) or not query.strip():
            return None
        return {"query": query, "valid": True}

    def act(self, decision: Any) -> Any:
        if not isinstance(decision, dict) or not decision.get("valid"):
            return {"logs": [], "specialist": self.name, "status": "failed"}
        worker_result = self._log_filter.run({"query": decision["query"]})
        if not isinstance(worker_result, dict):
            return {"logs": [], "specialist": self.name, "status": "failed"}
        return {
            "logs": worker_result.get("logs", []),
            "error_count": worker_result.get("count", 0),
            "specialist": self.name,
            "status": worker_result.get("status", "completed"),
        }
