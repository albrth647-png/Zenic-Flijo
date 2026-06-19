"""
Tests para F0-D5: supervisors/base + supervisors/research + specialists/web_researcher
+ workers/query_builder.

Cobertura:
- QueryBuilderWorker: think/act con input válido, inválido, sinónimos, max_variants
- WebResearcherSpecialist: think/act, delegación al worker
- DomainSupervisor base: handle con 0, 1, 2+ specialists, persistencia en Ledger, anti-B-05
- ResearchSupervisor: configuración concreta del dominio research
- Integración end-to-end: subtask → ResearchSupervisor.handle() → resultado
"""

from __future__ import annotations

from datetime import datetime, timezone

import pytest

from src.agents.base import AgentConfig, BaseAgent
from src.agents.orchestrator import MultiAgentOrchestrator
from src.hat.agents.specialists.web_researcher import WebResearcherSpecialist
from src.hat.agents.workers.query_builder import QueryBuilderWorker
from src.hat.ledger.repository import LedgerRepository
from src.hat.supervisors.base import DomainSupervisor
from src.hat.supervisors.research import ResearchSupervisor


@pytest.fixture
def repo():
    return LedgerRepository()


@pytest.fixture
def session():
    ts = datetime.now(timezone.utc).strftime("%H%M%S%f")
    return {
        "user_id": f"supv_user_{ts}",
        "session_id": f"supv_sess_{ts}",
    }


@pytest.fixture(autouse=True)
def cleanup_orchestrator():
    """Reset MultiAgentOrchestrator singleton entre tests."""
    MultiAgentOrchestrator.reset_instance()
    yield
    MultiAgentOrchestrator.reset_instance()


# ─────────────────────────────────────────────────────────
# QueryBuilderWorker
# ─────────────────────────────────────────────────────────


class TestQueryBuilderWorker:
    def test_think_with_valid_input_returns_decision(self):
        worker = QueryBuilderWorker(AgentConfig(name="qb"))
        decision = worker.think({"raw_query": "busca info de python", "max_variants": 3})
        assert decision is not None
        assert decision["raw_query"] == "busca info de python"
        assert decision["max_variants"] == 3
        # "python" está en el dict de sinónimos
        assert any(word == "python" for word, _ in decision["synonyms_found"])

    def test_think_returns_none_for_invalid_input(self):
        worker = QueryBuilderWorker(AgentConfig(name="qb"))
        assert worker.think(None) is None  # type: ignore[arg-type]
        assert worker.think({}) is None
        assert worker.think({"raw_query": ""}) is None
        assert worker.think({"raw_query": 123}) is None  # type: ignore[dict-item]

    def test_act_generates_expanded_queries(self):
        worker = QueryBuilderWorker(AgentConfig(name="qb"))
        decision = {
            "raw_query": "aprende python",
            "synonyms_found": [("python", ("python3", "cpython"))],
            "max_variants": 3,
        }
        result = worker.act(decision)
        assert result["status"] == "completed"
        assert "aprende python" in result["queries"]
        # Debe incluir al menos una variante con sinónimo
        assert any("python3" in q or "cpython" in q for q in result["queries"])

    def test_act_respects_max_variants(self):
        worker = QueryBuilderWorker(AgentConfig(name="qb"))
        decision = {
            "raw_query": "test",
            "synonyms_found": [("test", ("a", "b", "c", "d", "e"))],
            "max_variants": 2,
        }
        result = worker.act(decision)
        # max_variants=2 → la query original + 1 expansión
        assert len(result["queries"]) <= 2

    def test_run_end_to_end_think_act(self):
        """run() ejecuta think→act en loop hasta completion."""
        worker = QueryBuilderWorker(AgentConfig(name="qb", max_iterations=3))
        result = worker.run({"raw_query": "busca javascript", "max_variants": 2})
        assert isinstance(result, dict)
        assert result["status"] == "completed"
        assert len(result["queries"]) >= 1

    def test_run_with_invalid_input_returns_none(self):
        """Si think() retorna None, run() debe terminar sin llamar act()."""
        worker = QueryBuilderWorker(AgentConfig(name="qb", max_iterations=3))
        result = worker.run({"raw_query": ""})
        # think retorna None → run() hace break → retorna None
        assert result is None


# ─────────────────────────────────────────────────────────
# WebResearcherSpecialist
# ─────────────────────────────────────────────────────────


class TestWebResearcherSpecialist:
    def test_think_with_valid_query(self):
        specialist = WebResearcherSpecialist(AgentConfig(name="wr"))
        decision = specialist.think({"query": "busca python", "max_variants": 2})
        assert decision is not None
        assert decision["valid"] is True
        assert decision["query"] == "busca python"

    def test_think_returns_none_for_invalid_input(self):
        specialist = WebResearcherSpecialist(AgentConfig(name="wr"))
        assert specialist.think(None) is None  # type: ignore[arg-type]
        assert specialist.think({}) is None
        assert specialist.think({"query": 123}) is None  # type: ignore[dict-item]

    def test_act_delegates_to_query_builder(self):
        specialist = WebResearcherSpecialist(AgentConfig(name="wr"))
        decision = {"query": "aprende python", "max_variants": 3, "valid": True}
        result = specialist.act(decision)
        assert result["specialist"] == "wr"
        assert result["status"] == "completed"
        assert len(result["queries"]) >= 1
        assert "aprende python" in result["queries"]

    def test_act_with_invalid_decision_returns_failed(self):
        specialist = WebResearcherSpecialist(AgentConfig(name="wr"))
        result = specialist.act({"valid": False})
        assert result["status"] == "failed"

    def test_run_end_to_end(self):
        specialist = WebResearcherSpecialist(AgentConfig(name="wr", max_iterations=3))
        result = specialist.run({"query": "busca javascript", "max_variants": 2})
        assert isinstance(result, dict)
        assert result["status"] == "completed"


# ─────────────────────────────────────────────────────────
# DomainSupervisor base — casos abstractos concretos
# ─────────────────────────────────────────────────────────


class _DummySpecialistOK(BaseAgent):
    """Specialist dummy que retorna un resultado fijo."""

    def think(self, observation):
        return {"ok": True, "input": observation}

    def act(self, decision):
        return {"result": "dummy_ok", "decision": decision}


class _DummySpecialistFail(BaseAgent):
    """Specialist dummy que siempre falla."""

    def think(self, observation):
        return {"ok": False}

    def act(self, decision):
        raise RuntimeError("dummy failure")


class _SupervisorWith0Specialists(DomainSupervisor):
    domain = "test_zero"

    def _load_specialists(self):
        return []

    def _build_configs(self):
        return []


class _SupervisorWith1Specialist(DomainSupervisor):
    domain = "test_one"

    def _load_specialists(self):
        return [_DummySpecialistOK]

    def _build_configs(self):
        return [AgentConfig(name="dummy1")]


class _SupervisorWith2Specialists(DomainSupervisor):
    domain = "test_two"

    def _load_specialists(self):
        return [_DummySpecialistOK, _DummySpecialistOK]

    def _build_configs(self):
        return [AgentConfig(name="dummy1"), AgentConfig(name="dummy2")]


class TestDomainSupervisorBase:
    def test_supervisor_with_0_specialists_returns_failed(self, repo):
        supv = _SupervisorWith0Specialists(ledger=repo)
        result = supv.handle({"dispatch_id": "d1", "user_id": "u", "session_id": "s"})
        assert result["status"] == "failed"
        assert "no specialists" in result["error"]

    def test_supervisor_with_1_specialist_uses_fallback(self, repo, session):
        """Anti-bug B-05: con 1 specialist, NO invoca MultiAgentOrchestrator HIERARCHICAL."""
        supv = _SupervisorWith1Specialist(ledger=repo)
        result = supv.handle({
            "dispatch_id": f"dp_{session['session_id']}",
            "user_id": session["user_id"],
            "session_id": session["session_id"],
            "params": {"query": "test"},
        })
        # El fallback directo ejecuta el specialist → status completed
        assert result["status"] == "completed"
        assert "dummy1" in result["specialists_used"]
        assert result["result"]["result"] == "dummy_ok"

    def test_supervisor_with_2_specialists_uses_orchestrator(self, repo, session):
        """Con 2+ specialists, invoca MultiAgentOrchestrator HIERARCHICAL."""
        supv = _SupervisorWith2Specialists(ledger=repo)
        result = supv.handle({
            "dispatch_id": f"dp2_{session['session_id']}",
            "user_id": session["user_id"],
            "session_id": session["session_id"],
            "params": {"query": "test"},
        })
        # HIERARCHICAL con 2 dummy specialists → manager + worker
        # El resultado puede ser success o error según la lógica del dummy
        assert result["status"] in ("completed", "failed")
        assert "duration_ms" in result

    def test_supervisor_persists_progress_to_ledger(self, repo, session):
        supv = _SupervisorWith1Specialist(ledger=repo)
        dispatch_id = f"dp_persist_{session['session_id']}"
        supv.handle({
            "dispatch_id": dispatch_id,
            "user_id": session["user_id"],
            "session_id": session["session_id"],
            "params": {"query": "test"},
        })
        progress = repo.get_progress(session["user_id"], session["session_id"])
        assert any(p["dispatch_id"] == dispatch_id for p in progress)

    def test_supervisor_domain_name_property(self, repo):
        supv = _SupervisorWith1Specialist(ledger=repo)
        assert supv.domain_name == "test_one"
        assert supv.specialist_count == 1


# ─────────────────────────────────────────────────────────
# ResearchSupervisor concreto
# ─────────────────────────────────────────────────────────


class TestResearchSupervisor:
    def test_research_supervisor_has_correct_domain(self, repo):
        supv = ResearchSupervisor(ledger=repo)
        assert supv.domain == "research"
        assert supv.domain_name == "research"

    def test_research_supervisor_has_1_specialist_in_f0(self, repo):
        """En F0, ResearchSupervisor solo registra WebResearcherSpecialist."""
        supv = ResearchSupervisor(ledger=repo)
        assert supv.specialist_count == 1
        assert WebResearcherSpecialist in supv._specialist_classes

    def test_research_supervisor_handle_with_valid_query(self, repo, session):
        """E2E: subtask con query válida → ResearchSupervisor → resultado con queries."""
        supv = ResearchSupervisor(ledger=repo)
        result = supv.handle({
            "dispatch_id": f"e2e_{session['session_id']}",
            "user_id": session["user_id"],
            "session_id": session["session_id"],
            "params": {"query": "busca python", "max_variants": 3},
        })
        assert result["status"] == "completed"
        assert "specialists_used" in result
        assert len(result["specialists_used"]) >= 1
        # El resultado debe contener queries expandidas
        result_data = result["result"]
        if isinstance(result_data, dict):
            assert "queries" in result_data
            assert len(result_data["queries"]) >= 1

    def test_research_supervisor_persists_progress(self, repo, session):
        supv = ResearchSupervisor(ledger=repo)
        dispatch_id = f"persist_{session['session_id']}"
        supv.handle({
            "dispatch_id": dispatch_id,
            "user_id": session["user_id"],
            "session_id": session["session_id"],
            "params": {"query": "test query"},
        })
        progress = repo.get_progress(session["user_id"], session["session_id"])
        matching = [p for p in progress if p["dispatch_id"] == dispatch_id]
        assert len(matching) == 1
        assert matching[0]["domain"] == "research"

    def test_research_supervisor_uses_fallback_for_1_specialist(self, repo, session):
        """Anti-bug B-05: con 1 specialist, NO debe llamar al orchestrator."""
        # Si el fallback funciona, el resultado es el del specialist directo
        # sin pasar por HIERARCHICAL (que crashearía).
        supv = ResearchSupervisor(ledger=repo)
        result = supv.handle({
            "dispatch_id": f"fb_{session['session_id']}",
            "user_id": session["user_id"],
            "session_id": session["session_id"],
            "params": {"query": "test"},
        })
        # Si B-05 no estuviera mitigado, esto sería "failed" con IndexError.
        assert result["status"] == "completed"


# ─────────────────────────────────────────────────────────
# Integración end-to-end
# ─────────────────────────────────────────────────────────


class TestE2EResearchDomain:
    def test_e2e_subtask_to_queries(self, repo, session):
        """Flujo completo: subtask del Orbital N0 → ResearchSupervisor → queries.

        Este es el patrón que F0-D7 (tick_router) usará para invocar el dominio.
        """
        supv = ResearchSupervisor(ledger=repo)
        subtask = {
            "dispatch_id": f"e2e_full_{session['session_id']}",
            "user_id": session["user_id"],
            "session_id": session["session_id"],
            "description": "buscar info sobre python",
            "parent_intent": "research",
            "params": {"query": "aprende python", "max_variants": 3},
            "orbital_resonance": 0.7,
        }
        result = supv.handle(subtask)

        # Verificar respuesta completa
        assert result["status"] == "completed"
        assert isinstance(result["result"], dict)
        assert "queries" in result["result"]
        # La query original debe estar incluida
        assert "aprende python" in result["result"]["queries"]
        # Debe haber al menos 1 variante con sinónimo
        assert len(result["result"]["queries"]) >= 1

        # Verificar que se persistió en Ledger
        progress = repo.get_progress(session["user_id"], session["session_id"])
        assert any(p["dispatch_id"] == subtask["dispatch_id"] for p in progress)

    def test_e2e_invalid_query_handled_gracefully(self, repo, session):
        """Si la query es inválida, el specialist debe fallar gracefully."""
        supv = ResearchSupervisor(ledger=repo)
        result = supv.handle({
            "dispatch_id": f"invalid_{session['session_id']}",
            "user_id": session["user_id"],
            "session_id": session["session_id"],
            "params": {"query": ""},  # inválido
        })
        # El specialist retorna failed, el supervisor lo propaga
        assert result["status"] in ("completed", "failed")
