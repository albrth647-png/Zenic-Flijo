"""
HAT-ORBITAL Worker — Test Runner.

Worker del dominio Build. Ejecuta tests y reporta resultados.
En F2 (MVP) simula ejecución de tests.
"""

from __future__ import annotations

from typing import Any

from src.agents.base import AgentCapability, AgentConfig, BaseAgent
from src.hat.agents.card_publisher import CardPublisherMixin
from src.hat.agents.cards import AgentCard
from src.utils.logger import setup_logging

logger = setup_logging(__name__)


class TestRunnerWorker(BaseAgent, CardPublisherMixin):
    """Worker que ejecuta tests y reporta resultados."""

    def __init__(self, config: AgentConfig) -> None:
        super().__init__(config)
        if not config.capabilities:
            config.capabilities = [AgentCapability.CODE_GENERATION]

    def get_card(self) -> AgentCard:
        return AgentCard(
            agent_id="test_runner",
            agent_name="Test Runner",
            domain="build",
            tier="worker",
            capabilities=["test_execution", "result_reporting"],
            cost_per_call=0.0,
            avg_latency_ms=50,
            orbital_keywords=["test", "testing", "pytest", "prueba", "unittest"],
            orbital_amplitude=0.8,
            orbital_velocity=0.1,
        )

    def think(self, observation: Any) -> Any:
        if not isinstance(observation, dict):
            return None
        code = observation.get("code")
        if not isinstance(code, str):
            return None
        return {"code": code, "valid": True}

    def act(self, decision: Any) -> Any:
        if not isinstance(decision, dict) or not decision.get("valid"):
            return {"tests_passed": 0, "tests_failed": 0, "status": "failed"}
        return {"tests_passed": 1, "tests_failed": 0, "status": "completed"}
