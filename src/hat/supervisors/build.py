"""
HAT-ORBITAL Supervisor — Build Domain.

Segundo dominio de HAT. Coordina specialists de build:
- CodeGeneratorSpecialist
- TestEngineerSpecialist
- DeployAgentSpecialist

Con 3 specialists activa orquestación HIERARCHICAL completa.
"""

from __future__ import annotations

from src.agents.base import AgentConfig, BaseAgent
from src.hat.agents.specialists.code_generator import CodeGeneratorSpecialist
from src.hat.agents.specialists.deploy_agent import DeployAgentSpecialist
from src.hat.agents.specialists.test_engineer import TestEngineerSpecialist
from src.hat.ledger.repository import LedgerRepository
from src.hat.supervisors.base import DomainSupervisor


class BuildSupervisor(DomainSupervisor):
    """Supervisor del dominio Build.

    Coordina specialists de build (Code Generator, Test Engineer, Deploy Agent).
    Con 3 specialists activa orquestación HIERARCHICAL del MultiAgentOrchestrator.
    """

    domain = "build"

    def __init__(
        self,
        ledger: LedgerRepository | None = None,
    ) -> None:
        super().__init__(ledger=ledger, orchestrator=None)

    def _load_specialists(self) -> list[type[BaseAgent]]:
        """Retorna las clases de specialists del dominio Build."""
        return [CodeGeneratorSpecialist, TestEngineerSpecialist, DeployAgentSpecialist]

    def _build_configs(self) -> list[AgentConfig]:
        """Retorna las configs para cada specialist."""
        return [
            AgentConfig(
                name="code_generator",
                description="Code Generator specialist — generates code from descriptions",
                max_iterations=3,
                timeout_seconds=30.0,
            ),
            AgentConfig(
                name="test_engineer",
                description="Test Engineer specialist — runs tests and reports results",
                max_iterations=3,
                timeout_seconds=30.0,
            ),
            AgentConfig(
                name="deploy_agent",
                description="Deploy Agent specialist — builds containers and deploys",
                max_iterations=3,
                timeout_seconds=30.0,
            ),
        ]
