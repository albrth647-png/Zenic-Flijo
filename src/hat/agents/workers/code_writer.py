"""
HAT-ORBITAL Worker — Code Writer.

Worker del dominio Build. Genera código a partir de una descripción.
En F2 (MVP) retorna plantillas de código simples.
"""

from __future__ import annotations

from typing import Any

from src.agents.base import AgentCapability, AgentConfig, BaseAgent
from src.hat.agents.card_publisher import CardPublisherMixin
from src.hat.agents.cards import AgentCard
from src.utils.logger import setup_logging

logger = setup_logging(__name__)


class CodeWriterWorker(BaseAgent, CardPublisherMixin):
    """Worker que genera código a partir de una descripción."""

    def __init__(self, config: AgentConfig) -> None:
        super().__init__(config)
        if not config.capabilities:
            config.capabilities = [AgentCapability.CODE_GENERATION]

    def get_card(self) -> AgentCard:
        return AgentCard(
            agent_id="code_writer",
            agent_name="Code Writer",
            domain="build",
            tier="worker",
            capabilities=["code_generation", "template_rendering"],
            cost_per_call=0.0,
            avg_latency_ms=15,
            orbital_keywords=["código", "code", "función", "function", "clase", "class"],
            orbital_amplitude=0.8,
            orbital_velocity=0.1,
        )

    def think(self, observation: Any) -> Any:
        if not isinstance(observation, dict):
            return None
        desc = observation.get("description")
        if not isinstance(desc, str) or not desc.strip():
            return None
        return {"description": desc, "language": observation.get("language", "python")}

    def act(self, decision: Any) -> Any:
        if not isinstance(decision, dict):
            return {"code": "", "status": "failed", "error": "invalid decision"}
        desc = decision["description"]
        lang = decision.get("language", "python")
        code = self._generate_template(desc, lang)
        return {"code": code, "language": lang, "status": "completed"}

    @staticmethod
    def _generate_template(description: str, language: str) -> str:
        """Genera una plantilla de código simple."""
        safe_name = description.replace(" ", "_").lower()[:30]
        if language == "python":
            return f'def {safe_name}():\n    """TODO: Implement {description}."""\n    pass\n'
        return f"function {safe_name}() {{\n  // TODO: Implement {description}\n}}\n"
