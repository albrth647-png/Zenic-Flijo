"""
HAT-ORBITAL Specialist — Monitor Agent.

Specialist del dominio Operate. Coordina MetricsScraperWorker.
"""

from __future__ import annotations

from typing import Any

from src.agents.base import AgentCapability, AgentConfig, BaseAgent
from src.hat.agents.card_publisher import CardPublisherMixin
from src.hat.agents.cards import AgentCard
from src.hat.agents.workers.metrics_scraper import MetricsScraperWorker
from src.utils.logger import setup_logging

logger = setup_logging(__name__)


class MonitorAgentSpecialist(BaseAgent, CardPublisherMixin):
    """Specialist que monitorea métricas de servicios."""

    def __init__(self, config: AgentConfig) -> None:
        super().__init__(config)
        if not config.capabilities:
            config.capabilities = [AgentCapability.DATA_ANALYSIS, AgentCapability.REASONING]
        worker_config = AgentConfig(name=f"{self.name}_metrics_scraper", max_iterations=3)
        self._metrics_scraper = MetricsScraperWorker(worker_config)

    def get_card(self) -> AgentCard:
        return AgentCard(
            agent_id="monitor_agent",
            agent_name="Monitor Agent",
            domain="operate",
            tier="specialist",
            capabilities=["monitoring", "health_check", "metrics_analysis"],
            cost_per_call=0.01,
            avg_latency_ms=200,
            orbital_keywords=["monitor", "métricas", "metricas", "status", "salud",
                              "rendimiento", "performance", "cpu", "memoria"],
            orbital_amplitude=1.5,
            orbital_velocity=0.05,
        )

    def think(self, observation: Any) -> Any:
        if not isinstance(observation, dict):
            return None
        service = observation.get("service") or observation.get("query")
        if not isinstance(service, str) or not service.strip():
            return None
        return {"service": service, "valid": True}

    def act(self, decision: Any) -> Any:
        if not isinstance(decision, dict) or not decision.get("valid"):
            return {"metrics": {}, "specialist": self.name, "status": "failed"}
        worker_result = self._metrics_scraper.run({"service": decision["service"]})
        if not isinstance(worker_result, dict):
            return {"metrics": {}, "specialist": self.name, "status": "failed"}
        return {
            "metrics": worker_result.get("metrics", {}),
            "specialist": self.name,
            "status": worker_result.get("status", "completed"),
        }
