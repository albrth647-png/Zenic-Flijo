"""
HAT-ORBITAL Worker — Log Filter.

Worker del dominio Operate. Filtra logs por severidad y keyword.
"""

from __future__ import annotations

from typing import Any

from src.agents.base import AgentCapability, AgentConfig, BaseAgent
from src.hat.agents.card_publisher import CardPublisherMixin
from src.hat.agents.cards import AgentCard
from src.utils.logger import setup_logging

logger = setup_logging(__name__)

_SAMPLE_LOGS = [
    "[INFO] Service started on port 8080",
    "[WARN] High memory usage detected: 85%",
    "[ERROR] Database connection timeout after 30s",
    "[INFO] Request processed in 120ms",
    "[ERROR] Failed to parse response from upstream",
]


class LogFilterWorker(BaseAgent, CardPublisherMixin):
    """Worker que filtra logs por severidad."""

    def __init__(self, config: AgentConfig) -> None:
        super().__init__(config)
        if not config.capabilities:
            config.capabilities = [AgentCapability.DATA_ANALYSIS]

    def get_card(self) -> AgentCard:
        return AgentCard(
            agent_id="log_filter",
            agent_name="Log Filter",
            domain="operate",
            tier="worker",
            capabilities=["log_parsing", "error_detection"],
            cost_per_call=0.0,
            avg_latency_ms=30,
            orbital_keywords=["logs", "error", "errores", "log", "advertencia", "warning"],
            orbital_amplitude=0.8,
            orbital_velocity=0.1,
        )

    def think(self, observation: Any) -> Any:
        if not isinstance(observation, dict):
            return None
        query = observation.get("query") or observation.get("service")
        if not isinstance(query, str) or not query.strip():
            return None
        severity = observation.get("severity", "ERROR")
        return {"query": query, "severity": severity, "valid": True}

    def act(self, decision: Any) -> Any:
        if not isinstance(decision, dict) or not decision.get("valid"):
            return {"logs": [], "status": "failed"}
        severity = decision.get("severity", "ERROR")
        filtered = [line for line in _SAMPLE_LOGS if severity in line]
        return {"logs": filtered, "count": len(filtered), "status": "completed"}
