"""
HAT-ORBITAL Specialist — Deploy Agent.

Specialist del dominio Build. Coordina ContainerBuilderWorker para deploy.
"""

from __future__ import annotations

from typing import Any

from src.agents.base import AgentCapability, AgentConfig, BaseAgent
from src.hat.agents.card_publisher import CardPublisherMixin
from src.hat.agents.cards import AgentCard
from src.hat.agents.workers.container_builder import ContainerBuilderWorker
from src.utils.logger import setup_logging

logger = setup_logging(__name__)


class DeployAgentSpecialist(BaseAgent, CardPublisherMixin):
    """Specialist que coordina deploy de aplicaciones."""

    def __init__(self, config: AgentConfig) -> None:
        super().__init__(config)
        if not config.capabilities:
            config.capabilities = [AgentCapability.CODE_GENERATION, AgentCapability.REASONING]
        worker_config = AgentConfig(name=f"{self.name}_container_builder", max_iterations=3)
        self._container_builder = ContainerBuilderWorker(worker_config)

    def get_card(self) -> AgentCard:
        return AgentCard(
            agent_id="deploy_agent",
            agent_name="Deploy Agent",
            domain="build",
            tier="specialist",
            capabilities=["deployment", "docker", "ci_cd", "containerization"],
            cost_per_call=0.02,
            avg_latency_ms=500,
            orbital_keywords=["deploy", "docker", "container", "publicar", "desplegar",
                              "imagen", "build", "compilar", "release"],
            orbital_amplitude=1.5,
            orbital_velocity=0.05,
        )

    def think(self, observation: Any) -> Any:
        if not isinstance(observation, dict):
            return None
        code = observation.get("code") or observation.get("query")
        if not isinstance(code, str) or not code.strip():
            return None
        return {"code": code, "ready": True}

    def act(self, decision: Any) -> Any:
        if not isinstance(decision, dict) or not decision.get("ready"):
            return {"dockerfile": "", "specialist": self.name, "status": "failed"}
        worker_result = self._container_builder.run({"code": decision["code"]})
        if not isinstance(worker_result, dict):
            return {"dockerfile": "", "specialist": self.name, "status": "failed"}
        return {
            "dockerfile": worker_result.get("dockerfile", ""),
            "image_tag": worker_result.get("image_tag", ""),
            "specialist": self.name,
            "status": worker_result.get("status", "completed"),
        }
