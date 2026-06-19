"""
HAT-ORBITAL Specialist — Code Generator.

Specialist del dominio Build. Coordina CodeWriterWorker para generar código.
"""

from __future__ import annotations

from typing import Any

from src.agents.base import AgentCapability, AgentConfig, BaseAgent
from src.hat.agents.card_publisher import CardPublisherMixin
from src.hat.agents.cards import AgentCard
from src.hat.agents.workers.code_writer import CodeWriterWorker
from src.utils.logger import setup_logging

logger = setup_logging(__name__)


class CodeGeneratorSpecialist(BaseAgent, CardPublisherMixin):
    """Specialist que coordina generación de código."""

    def __init__(self, config: AgentConfig) -> None:
        super().__init__(config)
        if not config.capabilities:
            config.capabilities = [AgentCapability.CODE_GENERATION, AgentCapability.REASONING]
        worker_config = AgentConfig(name=f"{self.name}_code_writer", max_iterations=3)
        self._code_writer = CodeWriterWorker(worker_config)

    def get_card(self) -> AgentCard:
        return AgentCard(
            agent_id="code_generator",
            agent_name="Code Generator",
            domain="build",
            tier="specialist",
            capabilities=["code_generation", "code_review", "refactoring"],
            cost_per_call=0.01,
            avg_latency_ms=200,
            orbital_keywords=["código", "code", "función", "function", "crear", "generar",
                              "implementar", "clase", "class", "refactor"],
            orbital_amplitude=1.5,
            orbital_velocity=0.05,
        )

    def think(self, observation: Any) -> Any:
        if not isinstance(observation, dict):
            return None
        desc = observation.get("description") or observation.get("query")
        if not isinstance(desc, str) or not desc.strip():
            return None
        return {"description": desc, "language": observation.get("language", "python"), "valid": True}

    def act(self, decision: Any) -> Any:
        if not isinstance(decision, dict) or not decision.get("valid"):
            return {"code": "", "specialist": self.name, "status": "failed"}
        worker_input = {"description": decision["description"], "language": decision["language"]}
        worker_result = self._code_writer.run(worker_input)
        if not isinstance(worker_result, dict):
            return {"code": "", "specialist": self.name, "status": "failed"}
        return {"code": worker_result.get("code", ""), "specialist": self.name, "status": "completed"}
