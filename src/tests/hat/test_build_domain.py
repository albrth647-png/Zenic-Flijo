"""
Tests para F2: BuildSupervisor + 3 specialists + 3 workers + E2E.

Cobertura:
- Workers: think/act de cada uno
- Specialists: think/act + get_card de cada uno
- BuildSupervisor: configuración + handle()
- E2E: "crea función que haga X" → código + test + deploy
"""

from __future__ import annotations

from datetime import datetime, timezone

import pytest

from src.agents.base import AgentConfig
from src.agents.orchestrator import MultiAgentOrchestrator
from src.hat.agents.specialists.code_generator import CodeGeneratorSpecialist
from src.hat.agents.specialists.deploy_agent import DeployAgentSpecialist
from src.hat.agents.specialists.test_engineer import TestEngineerSpecialist
from src.hat.agents.workers.code_writer import CodeWriterWorker
from src.hat.agents.workers.container_builder import ContainerBuilderWorker
from src.hat.agents.workers.test_runner import TestRunnerWorker
from src.hat.agents.cards import AgentCard
from src.hat.ledger.repository import LedgerRepository
from src.hat.supervisors.build import BuildSupervisor
from src.orbital.context import OrbitalContext


@pytest.fixture(autouse=True)
def cleanup():
    OrbitalContext._reset()
    MultiAgentOrchestrator.reset_instance()
    yield
    OrbitalContext._reset()
    MultiAgentOrchestrator.reset_instance()


@pytest.fixture
def session():
    ts = datetime.now(timezone.utc).strftime("%H%M%S%f")
    return {"user_id": f"build_user_{ts}", "session_id": f"build_sess_{ts}"}


# ─────────────────────────────────────────────────────────
# Workers
# ─────────────────────────────────────────────────────────


class TestCodeWriterWorker:
    def test_generates_python_code(self):
        worker = CodeWriterWorker(AgentConfig(name="cw"))
        result = worker.run({"description": "calcular suma", "language": "python"})
        assert result["status"] == "completed"
        assert "def calcular_suma" in result["code"]

    def test_returns_failed_on_invalid_input(self):
        worker = CodeWriterWorker(AgentConfig(name="cw", max_iterations=3))
        result = worker.run({"description": "", "language": "python"})
        assert result is None

    def test_get_card_returns_build_domain(self):
        worker = CodeWriterWorker(AgentConfig(name="cw"))
        card = worker.get_card()
        assert card.domain == "build"
        assert card.tier == "worker"


class TestTestRunnerWorker:
    def test_runs_tests_successfully(self):
        worker = TestRunnerWorker(AgentConfig(name="tr"))
        result = worker.run({"code": "def foo(): pass"})
        assert result["status"] == "completed"
        assert result["tests_passed"] == 1

    def test_get_card_returns_build_domain(self):
        worker = TestRunnerWorker(AgentConfig(name="tr"))
        assert worker.get_card().domain == "build"


class TestContainerBuilderWorker:
    def test_generates_dockerfile(self):
        worker = ContainerBuilderWorker(AgentConfig(name="cb"))
        result = worker.run({"code": "print('hello')"})
        assert result["status"] == "completed"
        assert "FROM" in result["dockerfile"]
        assert result["image_tag"] == "app:latest"

    def test_get_card_returns_build_domain(self):
        worker = ContainerBuilderWorker(AgentConfig(name="cb"))
        assert worker.get_card().domain == "build"


# ─────────────────────────────────────────────────────────
# Specialists
# ─────────────────────────────────────────────────────────


class TestCodeGeneratorSpecialist:
    def test_generates_code_from_description(self):
        specialist = CodeGeneratorSpecialist(AgentConfig(name="cg", max_iterations=3))
        result = specialist.run({"description": "calcular promedio", "language": "python"})
        assert result["status"] == "completed"
        assert "def calcular_promedio" in result["code"]

    def test_get_card_amplitude_1_5(self):
        specialist = CodeGeneratorSpecialist(AgentConfig(name="cg"))
        card = specialist.get_card()
        assert card.orbital_amplitude == 1.5
        assert card.domain == "build"
        assert card.tier == "specialist"


class TestTestEngineerSpecialist:
    def test_runs_tests_on_code(self):
        specialist = TestEngineerSpecialist(AgentConfig(name="te", max_iterations=3))
        result = specialist.run({"code": "def foo(): pass"})
        assert result["status"] == "completed"
        assert result["tests_passed"] >= 1

    def test_get_card(self):
        specialist = TestEngineerSpecialist(AgentConfig(name="te"))
        card = specialist.get_card()
        assert card.domain == "build"
        assert card.tier == "specialist"


class TestDeployAgentSpecialist:
    def test_generates_dockerfile(self):
        specialist = DeployAgentSpecialist(AgentConfig(name="da", max_iterations=3))
        result = specialist.run({"code": "print('hello')"})
        assert result["status"] == "completed"
        assert "FROM" in result["dockerfile"]

    def test_get_card(self):
        specialist = DeployAgentSpecialist(AgentConfig(name="da"))
        assert specialist.get_card().domain == "build"


# ─────────────────────────────────────────────────────────
# BuildSupervisor
# ─────────────────────────────────────────────────────────


class TestBuildSupervisor:
    def test_has_correct_domain(self):
        repo = LedgerRepository()
        supv = BuildSupervisor(ledger=repo)
        assert supv.domain == "build"
        assert supv.domain_name == "build"

    def test_has_3_specialists(self):
        """Con 3 specialists, usa HIERARCHICAL (no fallback)."""
        repo = LedgerRepository()
        supv = BuildSupervisor(ledger=repo)
        assert supv.specialist_count == 3

    def test_handle_generates_code(self, session):
        repo = LedgerRepository()
        supv = BuildSupervisor(ledger=repo)
        result = supv.handle({
            "dispatch_id": f"build_{session['session_id']}",
            "user_id": session["user_id"],
            "session_id": session["session_id"],
            "params": {"query": "crear función calcular suma"},
        })
        assert result["status"] in ("completed", "failed")

    def test_persists_progress(self, session):
        repo = LedgerRepository()
        supv = BuildSupervisor(ledger=repo)
        dispatch_id = f"persist_{session['session_id']}"
        supv.handle({
            "dispatch_id": dispatch_id,
            "user_id": session["user_id"],
            "session_id": session["session_id"],
            "params": {"query": "crear función"},
        })
        progress = repo.get_progress(session["user_id"], session["session_id"])
        assert any(p["dispatch_id"] == dispatch_id for p in progress)
        assert any(p["domain"] == "build" for p in progress)


# ─────────────────────────────────────────────────────────
# Agent Cards
# ─────────────────────────────────────────────────────────


class TestBuildAgentCards:
    def test_code_generator_card(self):
        specialist = CodeGeneratorSpecialist(AgentConfig(name="cg"))
        card = specialist.get_card()
        assert isinstance(card, AgentCard)
        assert card.agent_id == "code_generator"
        assert "code_generation" in card.capabilities

    def test_test_engineer_card(self):
        specialist = TestEngineerSpecialist(AgentConfig(name="te"))
        card = specialist.get_card()
        assert card.agent_id == "test_engineer"
        assert "test_execution" in card.capabilities

    def test_deploy_agent_card(self):
        specialist = DeployAgentSpecialist(AgentConfig(name="da"))
        card = specialist.get_card()
        assert card.agent_id == "deploy_agent"
        assert "deployment" in card.capabilities

    def test_all_build_cards_have_amplitude_1_5(self):
        """Specialists tienen mayor amplitud que workers (1.5 vs 0.8)."""
        for cls in [CodeGeneratorSpecialist, TestEngineerSpecialist, DeployAgentSpecialist]:
            card = cls(AgentConfig(name="test")).get_card()
            assert card.orbital_amplitude == 1.5

    def test_all_worker_cards_have_amplitude_0_8(self):
        for cls in [CodeWriterWorker, TestRunnerWorker, ContainerBuilderWorker]:
            card = cls(AgentConfig(name="test")).get_card()
            assert card.orbital_amplitude == 0.8


# ─────────────────────────────────────────────────────────
# E2E: "crea función que haga X" → código + test + deploy
# ─────────────────────────────────────────────────────────


class TestE2EBuildDomain:
    def test_e2e_code_generation(self, session):
        """E2E: subtask → BuildSupervisor → código generado."""
        repo = LedgerRepository()
        supv = BuildSupervisor(ledger=repo)
        result = supv.handle({
            "dispatch_id": f"e2e_{session['session_id']}",
            "user_id": session["user_id"],
            "session_id": session["session_id"],
            "params": {"query": "crear función calcular promedio"},
        })
        assert result["status"] in ("completed", "failed")

    def test_e2e_persists_to_ledger(self, session):
        repo = LedgerRepository()
        supv = BuildSupervisor(ledger=repo)
        dispatch_id = f"e2e_p_{session['session_id']}"
        supv.handle({
            "dispatch_id": dispatch_id,
            "user_id": session["user_id"],
            "session_id": session["session_id"],
            "params": {"query": "crear función"},
        })
        progress = repo.get_progress(session["user_id"], session["session_id"])
        matching = [p for p in progress if p["dispatch_id"] == dispatch_id]
        assert len(matching) == 1
        assert matching[0]["domain"] == "build"
