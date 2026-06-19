"""
HAT-ORBITAL Specialist — Test Engineer.

Specialist del dominio Build. Coordina TestRunnerWorker para ejecutar tests.
"""

from __future__ import annotations

from typing import Any

from src.agents.base import AgentCapability, AgentConfig, BaseAgent
from src.hat.agents.card_publisher import CardPublisherMixin
from src.hat.agents.cards import AgentCard
from src.hat.agents.workers.test_runner import TestRunnerWorker
from src.utils.logger import setup_logging

logger = setup_logging(__name__)


class TestEngineerSpecialist(BaseAgent, CardPublisherMixin):
    """Specialist que coordina ejecución de tests."""

    def __init__(self, config: AgentConfig) -> None:
        super().__init__(config)
        if not config.capabilities:
            config.capabilities = [AgentCapability.CODE_GENERATION, AgentCapability.REASONING]
        worker_config = AgentConfig(name=f"{self.name}_test_runner", max_iterations=3)
        self._test_runner = TestRunnerWorker(worker_config)

    def get_card(self) -> AgentCard:
        return AgentCard(
            agent_id="test_engineer",
            agent_name="Test Engineer",
            domain="build",
            tier="specialist",
            capabilities=["test_generation", "test_execution", "coverage_analysis"],
            cost_per_call=0.01,
            avg_latency_ms=300,
            orbital_keywords=["test", "testing", "prueba", "pytest", "unittest", "coverage",
                              "cobertura", "verificar"],
            orbital_amplitude=1.5,
            orbital_velocity=0.05,
        )

    def think(self, observation: Any) -> Any:
        if not isinstance(observation, dict):
            return None
        code = observation.get("code") or observation.get("query")
        if not isinstance(code, str) or not code.strip():
            return None
        return {"code": code, "valid": True}

    def act(self, decision: Any) -> Any:
        if not isinstance(decision, dict) or not decision.get("valid"):
            return {"tests_passed": 0, "specialist": self.name, "status": "failed"}
        worker_result = self._test_runner.run({"code": decision["code"]})
        if not isinstance(worker_result, dict):
            return {"tests_passed": 0, "specialist": self.name, "status": "failed"}
        return {
            "tests_passed": worker_result.get("tests_passed", 0),
            "tests_failed": worker_result.get("tests_failed", 0),
            "specialist": self.name,
            "status": worker_result.get("status", "completed"),
        }
