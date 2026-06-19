"""
HAT-ORBITAL Worker — Metrics Scraper.

Worker del dominio Operate. Recopila métricas simuladas de un servicio.
"""

from __future__ import annotations

from typing import Any

from src.agents.base import AgentCapability, AgentConfig, BaseAgent
from src.hat.agents.card_publisher import CardPublisherMixin
from src.hat.agents.cards import AgentCard
from src.utils.logger import setup_logging

logger = setup_logging(__name__)


class MetricsScraperWorker(BaseAgent, CardPublisherMixin):
    """Worker que recopila métricas de un servicio."""

    def __init__(self, config: AgentConfig) -> None:
        super().__init__(config)
        if not config.capabilities:
            config.capabilities = [AgentCapability.DATA_ANALYSIS]

    def get_card(self) -> AgentCard:
        return AgentCard(
            agent_id="metrics_scraper",
            agent_name="Metrics Scraper",
            domain="operate",
            tier="worker",
            capabilities=["metrics_collection", "health_check"],
            cost_per_call=0.0,
            avg_latency_ms=50,
            orbital_keywords=["métricas", "metricas", "cpu", "memoria", "status", "salud"],
            orbital_amplitude=0.8,
            orbital_velocity=0.1,
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
            return {"metrics": {}, "status": "failed"}
        return {
            "metrics": {"cpu": 45.2, "memory": 62.8, "requests_per_sec": 150, "error_rate": 0.5},
            "service": decision["service"],
            "status": "completed",
        }
