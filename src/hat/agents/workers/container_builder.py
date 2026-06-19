"""
HAT-ORBITAL Worker — Container Builder.

Worker del dominio Build. Genera Dockerfile y simula build de imagen.
"""

from __future__ import annotations

from typing import Any

from src.agents.base import AgentCapability, AgentConfig, BaseAgent
from src.hat.agents.card_publisher import CardPublisherMixin
from src.hat.agents.cards import AgentCard
from src.utils.logger import setup_logging

logger = setup_logging(__name__)


class ContainerBuilderWorker(BaseAgent, CardPublisherMixin):
    """Worker que genera Dockerfile y simula build."""

    def __init__(self, config: AgentConfig) -> None:
        super().__init__(config)
        if not config.capabilities:
            config.capabilities = [AgentCapability.CODE_GENERATION]

    def get_card(self) -> AgentCard:
        return AgentCard(
            agent_id="container_builder",
            agent_name="Container Builder",
            domain="build",
            tier="worker",
            capabilities=["dockerfile_generation", "image_build"],
            cost_per_call=0.0,
            avg_latency_ms=100,
            orbital_keywords=["deploy", "docker", "container", "imagen", "build"],
            orbital_amplitude=0.8,
            orbital_velocity=0.1,
        )

    def think(self, observation: Any) -> Any:
        if not isinstance(observation, dict):
            return None
        code = observation.get("code")
        if not isinstance(code, str):
            return None
        return {"code": code, "ready": True}

    def act(self, decision: Any) -> Any:
        if not isinstance(decision, dict) or not decision.get("ready"):
            return {"dockerfile": "", "image_tag": "", "status": "failed"}
        dockerfile = 'FROM python:3.12-slim\nCOPY . /app\nWORKDIR /app\nCMD ["python", "main.py"]\n'
        return {"dockerfile": dockerfile, "image_tag": "app:latest", "status": "completed"}
