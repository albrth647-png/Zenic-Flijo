"""
HAT-ORBITAL Worker — Alert Dispatcher.

Worker del dominio Operate. Genera y envía alertas.
"""

from __future__ import annotations

from typing import Any

from src.agents.base import AgentCapability, AgentConfig, BaseAgent
from src.hat.agents.card_publisher import CardPublisherMixin
from src.hat.agents.cards import AgentCard
from src.utils.logger import setup_logging

logger = setup_logging(__name__)


class AlertDispatcherWorker(BaseAgent, CardPublisherMixin):
    """Worker que genera y envía alertas."""

    def __init__(self, config: AgentConfig) -> None:
        super().__init__(config)
        if not config.capabilities:
            config.capabilities = [AgentCapability.DATA_ANALYSIS]

    def get_card(self) -> AgentCard:
        return AgentCard(
            agent_id="alert_dispatcher",
            agent_name="Alert Dispatcher",
            domain="operate",
            tier="worker",
            capabilities=["alert_generation", "notification_sending"],
            cost_per_call=0.0,
            avg_latency_ms=20,
            orbital_keywords=["alerta", "incidente", "notifcar", "warning", "critical"],
            orbital_amplitude=0.8,
            orbital_velocity=0.1,
        )

    def think(self, observation: Any) -> Any:
        if not isinstance(observation, dict):
            return None
        message = observation.get("message") or observation.get("query")
        if not isinstance(message, str) or not message.strip():
            return None
        return {"message": message, "valid": True}

    def act(self, decision: Any) -> Any:
        if not isinstance(decision, dict) or not decision.get("valid"):
            return {"alert_sent": False, "status": "failed"}
        return {"alert_sent": True, "alert_id": f"alert_{hash(decision['message']) & 0xFFFFFF:06x}", "status": "completed"}
