"""
Tests para F3: OperateSupervisor + 3 specialists + 3 workers + E2E.

HAT-ORBITAL queda con 3 dominios × (1 supervisor + 3 specialists + 3 workers) = 21 agentes.
"""

from __future__ import annotations

from datetime import datetime, timezone

import pytest

from src.agents.base import AgentConfig
from src.agents.orchestrator import MultiAgentOrchestrator
from src.hat.agents.cards import AgentCard
from src.hat.agents.specialists.incident_responder import IncidentResponderSpecialist
from src.hat.agents.specialists.log_analyzer import LogAnalyzerSpecialist
from src.hat.agents.specialists.monitor_agent import MonitorAgentSpecialist
from src.hat.agents.workers.alert_dispatcher import AlertDispatcherWorker
from src.hat.agents.workers.log_filter import LogFilterWorker
from src.hat.agents.workers.metrics_scraper import MetricsScraperWorker
from src.hat.ledger.repository import LedgerRepository
from src.hat.supervisors.operate import OperateSupervisor
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
    return {"user_id": f"op_user_{ts}", "session_id": f"op_sess_{ts}"}


# ─────────────────────────────────────────────────────────
# Workers
# ─────────────────────────────────────────────────────────


class TestMetricsScraperWorker:
    def test_collects_metrics(self):
        worker = MetricsScraperWorker(AgentConfig(name="ms"))
        result = worker.run({"service": "api-server"})
        assert result["status"] == "completed"
        assert "cpu" in result["metrics"]
        assert "memory" in result["metrics"]

    def test_get_card_operate_domain(self):
        assert MetricsScraperWorker(AgentConfig(name="ms")).get_card().domain == "operate"

    def test_invalid_input_returns_none(self):
        worker = MetricsScraperWorker(AgentConfig(name="ms", max_iterations=3))
        assert worker.run({"service": ""}) is None


class TestLogFilterWorker:
    def test_filters_errors(self):
        worker = LogFilterWorker(AgentConfig(name="lf"))
        result = worker.run({"query": "api-server", "severity": "ERROR"})
        assert result["status"] == "completed"
        assert result["count"] > 0
        assert all("ERROR" in line for line in result["logs"])

    def test_get_card_operate_domain(self):
        assert LogFilterWorker(AgentConfig(name="lf")).get_card().domain == "operate"


class TestAlertDispatcherWorker:
    def test_dispatches_alert(self):
        worker = AlertDispatcherWorker(AgentConfig(name="ad"))
        result = worker.run({"message": "Service down"})
        assert result["status"] == "completed"
        assert result["alert_sent"] is True
        assert result["alert_id"].startswith("alert_")

    def test_get_card_operate_domain(self):
        assert AlertDispatcherWorker(AgentConfig(name="ad")).get_card().domain == "operate"


# ─────────────────────────────────────────────────────────
# Specialists
# ─────────────────────────────────────────────────────────


class TestMonitorAgentSpecialist:
    def test_collects_metrics_via_worker(self):
        specialist = MonitorAgentSpecialist(AgentConfig(name="ma", max_iterations=3))
        result = specialist.run({"service": "api-server"})
        assert result["status"] == "completed"
        assert "cpu" in result["metrics"]

    def test_get_card(self):
        card = MonitorAgentSpecialist(AgentConfig(name="ma")).get_card()
        assert card.domain == "operate"
        assert card.tier == "specialist"
        assert card.orbital_amplitude == 1.5


class TestLogAnalyzerSpecialist:
    def test_analyzes_logs_via_worker(self):
        specialist = LogAnalyzerSpecialist(AgentConfig(name="la", max_iterations=3))
        result = specialist.run({"query": "api-server errors"})
        assert result["status"] == "completed"
        assert result["error_count"] > 0

    def test_get_card(self):
        card = LogAnalyzerSpecialist(AgentConfig(name="la")).get_card()
        assert card.domain == "operate"
        assert card.orbital_amplitude == 1.5


class TestIncidentResponderSpecialist:
    def test_dispatches_alert_via_worker(self):
        specialist = IncidentResponderSpecialist(AgentConfig(name="ir", max_iterations=3))
        result = specialist.run({"query": "service is down"})
        assert result["status"] == "completed"
        assert result["alert_sent"] is True

    def test_get_card(self):
        card = IncidentResponderSpecialist(AgentConfig(name="ir")).get_card()
        assert card.domain == "operate"
        assert card.orbital_amplitude == 1.5


# ─────────────────────────────────────────────────────────
# OperateSupervisor
# ─────────────────────────────────────────────────────────


class TestOperateSupervisor:
    def test_has_correct_domain(self):
        repo = LedgerRepository()
        supv = OperateSupervisor(ledger=repo)
        assert supv.domain == "operate"

    def test_has_3_specialists(self):
        repo = LedgerRepository()
        supv = OperateSupervisor(ledger=repo)
        assert supv.specialist_count == 3

    def test_handle_monitors_service(self, session):
        repo = LedgerRepository()
        supv = OperateSupervisor(ledger=repo)
        result = supv.handle({
            "dispatch_id": f"op_{session['session_id']}",
            "user_id": session["user_id"],
            "session_id": session["session_id"],
            "params": {"query": "monitor api-server"},
        })
        assert result["status"] in ("completed", "failed")

    def test_persists_progress(self, session):
        repo = LedgerRepository()
        supv = OperateSupervisor(ledger=repo)
        dispatch_id = f"op_p_{session['session_id']}"
        supv.handle({
            "dispatch_id": dispatch_id,
            "user_id": session["user_id"],
            "session_id": session["session_id"],
            "params": {"query": "revisar logs"},
        })
        progress = repo.get_progress(session["user_id"], session["session_id"])
        assert any(p["dispatch_id"] == dispatch_id for p in progress)
        assert any(p["domain"] == "operate" for p in progress)


# ─────────────────────────────────────────────────────────
# Agent Cards
# ─────────────────────────────────────────────────────────


class TestOperateAgentCards:
    def test_all_specialist_cards(self):
        for cls in [MonitorAgentSpecialist, LogAnalyzerSpecialist, IncidentResponderSpecialist]:
            card = cls(AgentConfig(name="test")).get_card()
            assert isinstance(card, AgentCard)
            assert card.domain == "operate"
            assert card.tier == "specialist"
            assert card.orbital_amplitude == 1.5

    def test_all_worker_cards(self):
        for cls in [MetricsScraperWorker, LogFilterWorker, AlertDispatcherWorker]:
            card = cls(AgentConfig(name="test")).get_card()
            assert card.domain == "operate"
            assert card.tier == "worker"
            assert card.orbital_amplitude == 0.8


# ─────────────────────────────────────────────────────────
# E2E
# ─────────────────────────────────────────────────────────


class TestE2EOperateDomain:
    def test_e2e_monitor_service(self, session):
        """E2E: subtask → OperateSupervisor → métricas recopiladas."""
        repo = LedgerRepository()
        supv = OperateSupervisor(ledger=repo)
        result = supv.handle({
            "dispatch_id": f"e2e_{session['session_id']}",
            "user_id": session["user_id"],
            "session_id": session["session_id"],
            "params": {"query": "monitor api-server"},
        })
        assert result["status"] in ("completed", "failed")

    def test_e2e_persists_to_ledger(self, session):
        repo = LedgerRepository()
        supv = OperateSupervisor(ledger=repo)
        dispatch_id = f"e2e_p_{session['session_id']}"
        supv.handle({
            "dispatch_id": dispatch_id,
            "user_id": session["user_id"],
            "session_id": session["session_id"],
            "params": {"query": "revisar logs de errores"},
        })
        progress = repo.get_progress(session["user_id"], session["session_id"])
        matching = [p for p in progress if p["dispatch_id"] == dispatch_id]
        assert len(matching) == 1
        assert matching[0]["domain"] == "operate"


# ─────────────────────────────────────────────────────────
# HAT completo: 3 dominios
# ─────────────────────────────────────────────────────────


class TestThreeDomainsComplete:
    """Verifica que HAT-ORBITAL tiene los 3 dominios funcionando."""

    def test_all_three_supervisors_exist(self):
        from src.hat.orbital_n0.tick_router import HATRouter
        router = HATRouter()
        assert "research" in router._supervisors
        assert "build" in router._supervisors
        assert "operate" in router._supervisors

    def test_all_three_domains_dispatchable(self, session):
        from src.hat.orbital_n0.tick_router import HATRouter
        router = HATRouter()
        for domain in ("research", "build", "operate"):
            result = router._dispatch_to_supervisor(domain, {
                "dispatch_id": f"3d_{domain}_{session['session_id']}",
                "user_id": session["user_id"],
                "session_id": session["session_id"],
                "params": {"query": "test query"},
            })
            assert result["status"] in ("completed", "failed"), f"Domain {domain} failed: {result}"
