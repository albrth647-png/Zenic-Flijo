"""
HAT-ORBITAL Supervisor — Research Domain.

Primer dominio concreto de HAT. Coordina specialists de research:
- WebResearcherSpecialist (F0: solo este)

En F0 solo registra 1 specialist (WebResearcher). El DomainSupervisor base
detecta que hay <2 y usa el fallback directo (anti-bug B-05) en vez de
invocar MultiAgentOrchestrator HIERARCHICAL.

En F2/F3 se añadirán DocAnalyst y DataAnalyst para completar los 3 specialists
y activar la orquestación HIERARCHICAL completa.

Implementado en F0-D5.
"""

from __future__ import annotations

from src.agents.base import AgentConfig, BaseAgent
from src.hat.agents.specialists.web_researcher import WebResearcherSpecialist
from src.hat.ledger.repository import LedgerRepository
from src.hat.supervisors.base import DomainSupervisor


class ResearchSupervisor(DomainSupervisor):
    """Supervisor del dominio Research.

    Coordina specialists de research (Web Researcher, Doc Analyst, Data Analyst).
    En F0 solo tiene WebResearcher — usa el fallback directo del base.
    """

    domain = "research"

    def __init__(
        self,
        ledger: LedgerRepository | None = None,
    ) -> None:
        """Inicializa ResearchSupervisor. Pasa None como orchestrator al base
        para que use el singleton MultiAgentOrchestrator."""
        super().__init__(ledger=ledger, orchestrator=None)

    def _load_specialists(self) -> list[type[BaseAgent]]:
        """Retorna las clases de specialists del dominio Research.

        En F0: solo WebResearcherSpecialist. En F2+ se añadirán más.
        """
        return [WebResearcherSpecialist]

    def _build_configs(self) -> list[AgentConfig]:
        """Retorna las configs para cada specialist."""
        return [
            AgentConfig(
                name="web_researcher",
                description="Web Researcher specialist — expands queries for web search",
                max_iterations=3,
                timeout_seconds=30.0,
            ),
        ]
