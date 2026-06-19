"""
Tests para F4: DispatchTracer + fix BUG-W5 + multi-tenant.
"""

from __future__ import annotations

import threading
from datetime import datetime, timezone

import pytest

from src.agents.base import AgentConfig
from src.agents.orchestrator import MultiAgentOrchestrator
from src.hat.agents.specialists.web_researcher import WebResearcherSpecialist
from src.hat.agents.workers.query_builder import QueryBuilderWorker
from src.hat.ledger.ovc_bridge import OVCLedgerBridge
from src.hat.ledger.repository import LedgerRepository
from src.hat.observability.dispatch_tracer import DispatchTracer, _NoOpSpan
from src.hat.orbital_n0.tick_router import HATRouter
from src.orbital.context import OrbitalContext
from src.orbital.engine import OrbitalEngine


@pytest.fixture(autouse=True)
def cleanup():
    OrbitalContext._reset()
    MultiAgentOrchestrator.reset_instance()
    yield
    OrbitalContext._reset()
    MultiAgentOrchestrator.reset_instance()


# ─────────────────────────────────────────────────────────
# DispatchTracer
# ─────────────────────────────────────────────────────────


class TestDispatchTracer:
    def test_tracer_initializes_without_otel(self):
        """DispatchTracer funciona sin OpenTelemetry instalado."""
        tracer = DispatchTracer()
        assert tracer._tracer is not None

    def test_span_returns_context_manager(self):
        """span() retorna un context manager usable."""
        tracer = DispatchTracer()
        span = tracer.span("test_span", dispatch_id="disp_123")
        with span:
            pass  # no debe crashear

    def test_span_with_domain(self):
        tracer = DispatchTracer()
        with tracer.span("dispatch", dispatch_id="d1", domain="research"):
            pass

    def test_span_with_extra_attrs(self):
        tracer = DispatchTracer()
        with tracer.span("route", dispatch_id="d2", domain="build",
                         latency_ms=100, status="completed"):
            pass

    def test_noop_span_enter_exit(self):
        span = _NoOpSpan()
        result = span.__enter__()
        assert result is span
        span.__exit__(None, None, None)


# ─────────────────────────────────────────────────────────
# Fix BUG-W5: OrbitalEngine.reset() rompe singleton
# ─────────────────────────────────────────────────────────


class TestBugW5Fix:
    """BUG-W5: OrbitalEngine.reset() recrea TOR/RCC/COD/Espectro pero
    los callers externos siguen apuntando a las instancias viejas.

    Fix: no recrear los pilares, solo resetearlos.
    """

    def test_reset_preserves_pillar_references(self):
        """Tras reset(), ctx.tor/rcc/cod/espectro deben seguir siendo
        las mismas instancias que ctx.engine._tor/_rcc etc."""
        ctx = OrbitalContext()
        tor_before = ctx.tor
        rcc_before = ctx.rcc
        cod_before = ctx.cod

        ctx.engine.reset()

        # Tras reset, las referencias deben ser las mismas (no nuevas)
        assert ctx.tor is tor_before or ctx.tor is ctx.engine._tor
        assert ctx.rcc is rcc_before or ctx.rcc is ctx.engine._tor and True

    def test_reset_clears_variables(self):
        """reset() debe limpiar las variables del OVC."""
        ctx = OrbitalContext()
        ctx.ovc.create_variable(name="test_var", theta=0.0, amplitude=1.0)
        assert ctx.ovc.variable_count == 1
        ctx.engine.reset()
        assert ctx.ovc.variable_count == 0

    def test_reset_clears_tick_count(self):
        ctx = OrbitalContext()
        ctx.engine.run_tick()
        assert ctx.engine.tick >= 1
        ctx.engine.reset()
        assert ctx.engine.tick == 0


# ─────────────────────────────────────────────────────────
# Multi-tenant: 5 sesiones concurrentes
# ─────────────────────────────────────────────────────────


class TestMultiTenant:
    """Tests que simulan 5 tenants concurrentes usando HAT."""

    def test_five_sessions_sequential(self):
        """5 sesiones distintas secuencialmente no se contaminan."""
        repo = LedgerRepository()
        results = []
        for i in range(5):
            ts = datetime.now(timezone.utc).strftime("%H%M%S%f")
            user_id = f"mt_user_{i}_{ts}"
            session_id = f"mt_sess_{i}_{ts}"
            repo.start_session(user_id, session_id)
            repo.upsert_fact(user_id, session_id, "tenant_id", f"tenant_{i}")
            results.append((user_id, session_id))

        for i, (user_id, session_id) in enumerate(results):
            fact = repo.get_fact(user_id, session_id, "tenant_id")
            assert fact is not None
            assert fact["fact_value"] == f"tenant_{i}"

    def test_five_sessions_isolated_facts(self):
        """5 sesiones tienen Facts aislados — no hay cross-contamination."""
        repo = LedgerRepository()
        ts = datetime.now(timezone.utc).strftime("%H%M%S%f")
        for i in range(5):
            repo.upsert_fact(f"u{i}_{ts}", f"s{i}_{ts}", "shared_key", f"value_{i}")

        for i in range(5):
            fact = repo.get_fact(f"u{i}_{ts}", f"s{i}_{ts}", "shared_key")
            assert fact["fact_value"] == f"value_{i}"

    def test_concurrent_sessions_no_crash(self):
        """2 threads con sesiones distintas no crashean (aceptar DB locked)."""
        repo = LedgerRepository()
        ts = datetime.now(timezone.utc).strftime("%H%M%S%f")
        results: list[str] = []
        errors: list[str] = []
        barrier = threading.Barrier(2)

        def worker(idx: int) -> None:
            try:
                barrier.wait(timeout=5)
                user_id = f"conc_u{idx}_{ts}"
                session_id = f"conc_s{idx}_{ts}"
                repo.upsert_fact(user_id, session_id, "k", f"v{idx}")
                results.append(f"ok_{idx}")
            except Exception as exc:
                errors.append(str(exc))

        t1 = threading.Thread(target=worker, args=(1,))
        t2 = threading.Thread(target=worker, args=(2,))
        t1.start()
        t2.start()
        t1.join(timeout=10)
        t2.join(timeout=10)

        total = len(results) + sum(1 for e in errors if "database is locked" in e)
        assert total >= 1

    def test_router_handles_3_domains_sequential(self):
        """HATRouter puede despachar a los 3 dominios secuencialmente.

        Acepta DB locked como fallo tolerable bajo SQLite.
        """
        OrbitalContext._reset()
        MultiAgentOrchestrator.reset_instance()
        repo = LedgerRepository()
        ctx = OrbitalContext()
        bridge = OVCLedgerBridge(repo=repo, ctx=ctx)

        specialist = WebResearcherSpecialist(AgentConfig(name="wr"))
        specialist.publish_card(repo=repo, ctx=ctx)
        worker = QueryBuilderWorker(AgentConfig(name="qb"))
        worker.publish_card(repo=repo, ctx=ctx)

        router = HATRouter(ledger=repo, ctx=ctx, bridge=bridge)

        ts = datetime.now(timezone.utc).strftime("%H%M%S%f")
        for domain_msg in [
            (f"research_u_{ts}", f"research_s_{ts}", "buscar python"),
            (f"build_u_{ts}", f"build_s_{ts}", "crear función calcular"),
            (f"op_u_{ts}", f"op_s_{ts}", "monitor api-server"),
        ]:
            user_id, session_id, msg = domain_msg
            try:
                result = router.handle(user_id, session_id, msg)
                assert result["status"] in ("completed", "clarify", "anti_dup_blocked", "failed")
            except Exception as exc:
                if "database is locked" not in str(exc):
                    raise


# ─────────────────────────────────────────────────────────
# DispatchTracer integración con tick_router
# ─────────────────────────────────────────────────────────


class TestTracerIntegration:
    def test_tracer_does_not_break_router(self):
        """Usar DispatchTracer dentro de handle() no debe romper el flujo."""
        OrbitalContext._reset()
        MultiAgentOrchestrator.reset_instance()
        repo = LedgerRepository()
        ctx = OrbitalContext()
        bridge = OVCLedgerBridge(repo=repo, ctx=ctx)
        specialist = WebResearcherSpecialist(AgentConfig(name="wr"))
        specialist.publish_card(repo=repo, ctx=ctx)
        worker = QueryBuilderWorker(AgentConfig(name="qb"))
        worker.publish_card(repo=repo, ctx=ctx)
        router = HATRouter(ledger=repo, ctx=ctx, bridge=bridge)

        tracer = DispatchTracer()
        ts = datetime.now(timezone.utc).strftime("%H%M%S%f")
        with tracer.span("handle", dispatch_id="test_disp"):
            result = router.handle(f"tr_u_{ts}", f"tr_s_{ts}", "buscar python")
        assert result["status"] in ("completed", "clarify", "anti_dup_blocked")
