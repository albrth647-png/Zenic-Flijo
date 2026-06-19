"""
HAT-ORBITAL Specialist — Incident Responder.

Specialist del dominio Operate. Coordina AlertDispatcherWorker.
"""

from __future__ import annotations

from typing import Any

from src.agents.base import AgentCapability, AgentConfig, BaseAgent
from src.hat.agents.card_publisher import CardPublisherMixin
from src.hat.agents.cards import AgentCard
from src.hat.agents.workers.alert_dispatcher import AlertDispatcherWorker
from src.utils.logger import setup_logging

logger = setup_logging(__name__)


class IncidentResponderSpecialist(BaseAgent, CardPublisherMixin):
    """Specialist que responde a incidentes."""

    def __init__(self, config: AgentConfig) -> None:
        super().__init__(config)
        if not config.capabilities:
            config.capabilities = [AgentCapability.DATA_ANALYSIS, AgentCapability.REASONING]
        worker_config = AgentConfig(name=f"{self.name}_alert_dispatcher", max_iterations=3)
        self._alert_dispatcher = AlertDispatcherWorker(worker_config)

    def get_card(self) -> AgentCard:
        return AgentCard(
            agent_id="incident_responder",
            agent_name="Incident Responder",
            domain="operate",
            tier="specialist",
            capabilities=["incident_response", "alert_dispatch", "remediation"],
            cost_per_call=0.02,
            avg_latency_ms=300,
            orbital_keywords=["incidente", "alerta", "critical", "resolver",
                              "notifcar", "emergencia", "urgente", "falla"],
            orbital_amplitude=1.5,
            orbital_velocity=0.05,
        )

    def think(self, observation: Any) -> Any:
        if not isinstance(observation, dict):
            return None
        message = observation.get("query") or observation.get("message")
        if not isinstance(message, str) or not message.strip():
            return None
        return {"message": message, "valid": True}

    def act(self, decision: Any) -> Any:
        if not isinstance(decision, dict) or not decision.get("valid"):
            return {"alert_sent": False, "specialist": self.name, "status": "failed"}
        worker_result = self._alert_dispatcher.run({"message": decision["message"]})
        if not isinstance(worker_result, dict):
            return {"alert_sent": False, "specialist": self.name, "status": "failed"}
        return {
            "alert_sent": worker_result.get("alert_sent", False),
            "alert_id": worker_result.get("alert_id", ""),
            "specialist": self.name,
            "status": worker_result.get("status", "completed"),
        }
