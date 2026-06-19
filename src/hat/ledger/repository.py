"""
HAT-ORBITAL Ledger Repository
=============================

CRUD sobre las 7 tablas del Ledger HAT. Reusa DatabaseManager singleton
de Zenic-Flujo (no crea conexiones propias).

Tablas gestionadas:
  - hat_facts
  - hat_hypotheses
  - hat_plan
  - hat_progress
  - hat_dispatch_registry
  - hat_agent_cards
  - hat_sessions

Implementado en F0-D2 siguiendo HAT_ORBITAL_PLAN.md §3.2.
"""

from __future__ import annotations

import contextlib
import json
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import Any

from src.data.database_manager import DatabaseManager
from src.utils.logger import setup_logging

logger = setup_logging(__name__)

_SCHEMA_PATH = Path(__file__).parent / "schema.sql"


class LedgerRepository:
    """CRUD sobre las 7 tablas HAT del Ledger.

    Reusa el singleton DatabaseManager de ZF (sqlite3 + WAL + foreign_keys=ON).
    No crea conexiones propias; todos los métodos delegan a db.execute/fetchone/fetchall.
    """

    def __init__(self, db: DatabaseManager | None = None) -> None:
        self._db = db if db is not None else DatabaseManager()
        self.ensure_schema()

    # ── Schema bootstrap ─────────────────────────────────────

    def ensure_schema(self) -> None:
        """Crea las 7 tablas HAT si no existen. Idempotente."""
        sql = _SCHEMA_PATH.read_text(encoding="utf-8")
        # executescript no está en DatabaseManager, usar cursor directo
        conn = self._db.get_connection()
        conn.executescript(sql)
        conn.commit()
        logger.debug("LedgerRepository: schema verificado (7 tablas HAT)")

    # ─────────────────────────────────────────────────────────
    # CRUD: hat_facts
    # ─────────────────────────────────────────────────────────

    def upsert_fact(
        self,
        user_id: str,
        session_id: str,
        fact_key: str,
        fact_value: Any,
        confidence: float = 1.0,
        orbital_theta: float = 0.0,
        orbital_amplitude: float = 1.0,
    ) -> int:
        """Inserta o actualiza un fact. Retorna el id del registro."""
        # Fix F0-D2: SIEMPRE json.dumps para que _decode_fact (que siempre json.loads) sea simétrico.
        value_json = json.dumps(fact_value, ensure_ascii=False)
        cur = self._db.execute(
            """
            INSERT INTO hat_facts (user_id, session_id, fact_key, fact_value, confidence, orbital_theta, orbital_amplitude, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
            ON CONFLICT(user_id, session_id, fact_key) DO UPDATE SET
                fact_value = excluded.fact_value,
                confidence = excluded.confidence,
                orbital_theta = excluded.orbital_theta,
                orbital_amplitude = excluded.orbital_amplitude,
                updated_at = CURRENT_TIMESTAMP
            """,
            (user_id, session_id, fact_key, value_json, confidence, orbital_theta, orbital_amplitude),
        )
        return cur.lastrowid or 0

    def get_facts(self, user_id: str, session_id: str) -> list[dict[str, Any]]:
        """Retorna todos los facts de una sesión."""
        rows = self._db.fetchall(
            "SELECT * FROM hat_facts WHERE user_id = ? AND session_id = ? ORDER BY fact_key",
            (user_id, session_id),
        )
        return [self._decode_fact(r) for r in rows]

    def get_fact(self, user_id: str, session_id: str, fact_key: str) -> dict[str, Any] | None:
        row = self._db.fetchone(
            "SELECT * FROM hat_facts WHERE user_id = ? AND session_id = ? AND fact_key = ?",
            (user_id, session_id, fact_key),
        )
        return self._decode_fact(row) if row else None

    def delete_fact(self, user_id: str, session_id: str, fact_key: str) -> bool:
        """Elimina un fact. Retorna True si eliminó algo."""
        cur = self._db.execute(
            "DELETE FROM hat_facts WHERE user_id = ? AND session_id = ? AND fact_key = ?",
            (user_id, session_id, fact_key),
        )
        return cur.rowcount > 0

    @staticmethod
    def _decode_fact(row: dict[str, Any]) -> dict[str, Any]:
        return {
            "id": row["id"],
            "user_id": row["user_id"],
            "session_id": row["session_id"],
            "fact_key": row["fact_key"],
            "fact_value": json.loads(row["fact_value"]) if row["fact_value"] else None,
            "confidence": row["confidence"],
            "orbital_theta": row["orbital_theta"],
            "orbital_amplitude": row["orbital_amplitude"],
            "created_at": row["created_at"],
            "updated_at": row["updated_at"],
        }

    # ─────────────────────────────────────────────────────────
    # CRUD: hat_hypotheses
    # ─────────────────────────────────────────────────────────

    def upsert_hypothesis(
        self,
        user_id: str,
        session_id: str,
        hypothesis_key: str,
        hypothesis_value: Any,
        confidence: float = 0.5,
        orbital_theta: float = 0.785,  # π/4
        orbital_amplitude: float = 0.5,
    ) -> int:
        # Fix F0-D2: SIEMPRE json.dumps (simetría con _decode_hypothesis).
        value_json = json.dumps(hypothesis_value, ensure_ascii=False)
        cur = self._db.execute(
            """
            INSERT INTO hat_hypotheses (user_id, session_id, hypothesis_key, hypothesis_value, confidence, orbital_theta, orbital_amplitude)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(user_id, session_id, hypothesis_key) DO UPDATE SET
                hypothesis_value = excluded.hypothesis_value,
                confidence = excluded.confidence,
                orbital_theta = excluded.orbital_theta,
                orbital_amplitude = excluded.orbital_amplitude
            """,
            (user_id, session_id, hypothesis_key, value_json, confidence, orbital_theta, orbital_amplitude),
        )
        return cur.lastrowid or 0

    def get_hypotheses(self, user_id: str, session_id: str, only_unverified: bool = False) -> list[dict[str, Any]]:
        sql = "SELECT * FROM hat_hypotheses WHERE user_id = ? AND session_id = ?"
        params: list[Any] = [user_id, session_id]
        if only_unverified:
            sql += " AND verified = 0"
        sql += " ORDER BY hypothesis_key"
        rows = self._db.fetchall(sql, tuple(params))
        return [self._decode_hypothesis(r) for r in rows]

    def verify_hypothesis(
        self,
        user_id: str,
        session_id: str,
        hypothesis_key: str,
        promote_to_fact: bool = False,
    ) -> bool:
        """Marca una hipótesis como verificada. Opcionalmente la promueve a fact."""
        cur = self._db.execute(
            """
            UPDATE hat_hypotheses
            SET verified = 1, verified_at = CURRENT_TIMESTAMP, promoted_to_fact = ?
            WHERE user_id = ? AND session_id = ? AND hypothesis_key = ?
            """,
            (1 if promote_to_fact else 0, user_id, session_id, hypothesis_key),
        )
        if cur.rowcount == 0:
            return False
        if promote_to_fact:
            hyp = self.get_hypothesis(user_id, session_id, hypothesis_key)
            if hyp:
                # Promover: copiar a hat_facts con confidence=1.0, theta=0
                self.upsert_fact(
                    user_id, session_id, hypothesis_key,
                    hyp["hypothesis_value"],
                    confidence=1.0,
                    orbital_theta=0.0,
                    orbital_amplitude=1.0,
                )
        return True

    def get_hypothesis(self, user_id: str, session_id: str, hypothesis_key: str) -> dict[str, Any] | None:
        row = self._db.fetchone(
            "SELECT * FROM hat_hypotheses WHERE user_id = ? AND session_id = ? AND hypothesis_key = ?",
            (user_id, session_id, hypothesis_key),
        )
        return self._decode_hypothesis(row) if row else None

    @staticmethod
    def _decode_hypothesis(row: dict[str, Any]) -> dict[str, Any]:
        return {
            "id": row["id"],
            "user_id": row["user_id"],
            "session_id": row["session_id"],
            "hypothesis_key": row["hypothesis_key"],
            "hypothesis_value": json.loads(row["hypothesis_value"]) if row["hypothesis_value"] else None,
            "confidence": row["confidence"],
            "orbital_theta": row["orbital_theta"],
            "orbital_amplitude": row["orbital_amplitude"],
            "verified": bool(row["verified"]),
            "verified_at": row["verified_at"],
            "promoted_to_fact": bool(row["promoted_to_fact"]),
            "created_at": row["created_at"],
        }

    # ─────────────────────────────────────────────────────────
    # CRUD: hat_plan
    # ─────────────────────────────────────────────────────────

    def add_plan_step(
        self,
        user_id: str,
        session_id: str,
        step_index: int,
        step_description: str,
        assigned_domain: str | None = None,
        orbital_var_name: str | None = None,
        orbital_theta: float | None = None,
    ) -> int:
        cur = self._db.execute(
            """
            INSERT INTO hat_plan (user_id, session_id, step_index, step_description, assigned_domain, orbital_var_name, orbital_theta)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(user_id, session_id, step_index) DO UPDATE SET
                step_description = excluded.step_description,
                assigned_domain = excluded.assigned_domain
            """,
            (user_id, session_id, step_index, step_description, assigned_domain, orbital_var_name, orbital_theta),
        )
        return cur.lastrowid or 0

    def get_plan(self, user_id: str, session_id: str) -> list[dict[str, Any]]:
        rows = self._db.fetchall(
            "SELECT * FROM hat_plan WHERE user_id = ? AND session_id = ? ORDER BY step_index",
            (user_id, session_id),
        )
        return [dict(r) for r in rows]

    def update_step_status(
        self,
        user_id: str,
        session_id: str,
        step_index: int,
        new_status: str,
        dispatch_id: str | None = None,
    ) -> bool:
        cur = self._db.execute(
            """
            UPDATE hat_plan
            SET step_status = ?, dispatch_id = COALESCE(?, dispatch_id)
            WHERE user_id = ? AND session_id = ? AND step_index = ?
            """,
            (new_status, dispatch_id, user_id, session_id, step_index),
        )
        return cur.rowcount > 0

    # ─────────────────────────────────────────────────────────
    # CRUD: hat_progress
    # ─────────────────────────────────────────────────────────

    def record_progress(
        self,
        user_id: str,
        session_id: str,
        dispatch_id: str,
        domain: str,
        status: str,
        specialist: str | None = None,
        worker: str | None = None,
        result_summary: Any = None,
        orbital_resonance: float | None = None,
    ) -> int:
        summary_json = (
            json.dumps(result_summary, ensure_ascii=False)
            if result_summary is not None
            else None
        )
        completed_at = "CURRENT_TIMESTAMP" if status in ("completed", "failed") else None
        if completed_at:
            cur = self._db.execute(
                """
                INSERT INTO hat_progress (user_id, session_id, dispatch_id, domain, specialist, worker, status, result_summary, orbital_resonance, completed_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
                ON CONFLICT(dispatch_id) DO UPDATE SET
                    status = excluded.status,
                    specialist = COALESCE(excluded.specialist, hat_progress.specialist),
                    worker = COALESCE(excluded.worker, hat_progress.worker),
                    result_summary = excluded.result_summary,
                    orbital_resonance = excluded.orbital_resonance,
                    completed_at = CURRENT_TIMESTAMP
                """,
                (user_id, session_id, dispatch_id, domain, specialist, worker, status, summary_json, orbital_resonance),
            )
        else:
            cur = self._db.execute(
                """
                INSERT INTO hat_progress (user_id, session_id, dispatch_id, domain, specialist, worker, status, result_summary, orbital_resonance)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(dispatch_id) DO UPDATE SET
                    status = excluded.status,
                    specialist = COALESCE(excluded.specialist, hat_progress.specialist),
                    worker = COALESCE(excluded.worker, hat_progress.worker),
                    result_summary = excluded.result_summary,
                    orbital_resonance = excluded.orbital_resonance
                """,
                (user_id, session_id, dispatch_id, domain, specialist, worker, status, summary_json, orbital_resonance),
            )
        return cur.lastrowid or 0

    def get_progress(self, user_id: str, session_id: str, limit: int = 50) -> list[dict[str, Any]]:
        rows = self._db.fetchall(
            "SELECT * FROM hat_progress WHERE user_id = ? AND session_id = ? ORDER BY started_at DESC LIMIT ?",
            (user_id, session_id, limit),
        )
        result = []
        for r in rows:
            d = dict(r)
            if d.get("result_summary"):
                with contextlib.suppress(json.JSONDecodeError, TypeError):
                    d["result_summary"] = json.loads(d["result_summary"])
            result.append(d)
        return result

    # ─────────────────────────────────────────────────────────
    # CRUD: hat_dispatch_registry — anti-doble-llamada
    # ─────────────────────────────────────────────────────────

    def register_dispatch(
        self,
        intent_hash: str,
        user_id: str,
        session_id: str,
        domain: str,
        ttl_seconds: int = 5,
    ) -> tuple[int, bool]:
        """Registra un nuevo dispatch.

        Returns:
            (id, was_created) — was_created=False si ya existía (capa 2 idempotency).
        """
        ttl_expires = (datetime.now(UTC) + timedelta(seconds=ttl_seconds)).isoformat(sep=" ")
        try:
            cur = self._db.execute(
                """
                INSERT INTO hat_dispatch_registry (intent_hash, user_id, session_id, domain, status, ttl_expires_at)
                VALUES (?, ?, ?, ?, 'in_progress', ?)
                """,
                (intent_hash, user_id, session_id, domain, ttl_expires),
            )
            return cur.lastrowid or 0, True
        except Exception:
            # INSERT falla si el hash ya existe (UNIQUE constraint)
            existing = self.get_dispatch(intent_hash)
            return (existing["id"] if existing else 0), False

    def get_dispatch(self, intent_hash: str) -> dict[str, Any] | None:
        row = self._db.fetchone(
            "SELECT * FROM hat_dispatch_registry WHERE intent_hash = ?",
            (intent_hash,),
        )
        if not row:
            return None
        d = dict(row)
        if d.get("result_cache"):
            with contextlib.suppress(json.JSONDecodeError, TypeError):
                d["result_cache"] = json.loads(d["result_cache"])
        return d

    def complete_dispatch(
        self,
        intent_hash: str,
        result: Any,
        status: str = "completed",
    ) -> bool:
        """Marca un dispatch como completado/failed y cachea el resultado."""
        # Fix F0-D2: SIEMPRE json.dumps (simetría con get_dispatch que siempre json.loads).
        result_json = json.dumps(result, ensure_ascii=False)
        cur = self._db.execute(
            """
            UPDATE hat_dispatch_registry
            SET status = ?, result_cache = ?, completed_at = CURRENT_TIMESTAMP
            WHERE intent_hash = ? AND status = 'in_progress'
            """,
            (status, result_json, intent_hash),
        )
        return cur.rowcount > 0

    def increment_subscriber(self, intent_hash: str) -> int:
        """Incrementa el contador de subscribers (capa 2 — cuántos esperan el resultado)."""
        cur = self._db.execute(
            "UPDATE hat_dispatch_registry SET subscriber_count = subscriber_count + 1 WHERE intent_hash = ?",
            (intent_hash,),
        )
        if cur.rowcount == 0:
            return 0
        row = self._db.fetchone(
            "SELECT subscriber_count FROM hat_dispatch_registry WHERE intent_hash = ?",
            (intent_hash,),
        )
        return row["subscriber_count"] if row else 0

    def get_in_progress_dispatches(self, older_than_seconds: int | None = None) -> list[dict[str, Any]]:
        """Retorna dispatches in_progress (capa 2 + capa 4 TTL)."""
        sql = "SELECT * FROM hat_dispatch_registry WHERE status = 'in_progress'"
        params: list[Any] = []
        if older_than_seconds is not None:
            sql += " AND created_at < ?"
            cutoff = (datetime.now(UTC) - timedelta(seconds=older_than_seconds)).isoformat(sep=" ")
            params.append(cutoff)
        sql += " ORDER BY created_at DESC"
        rows = self._db.fetchall(sql, tuple(params))
        return [dict(r) for r in rows]

    def get_recent_dispatches_by_session(
        self, user_id: str, session_id: str, since_seconds: int = 5,
    ) -> list[dict[str, Any]]:
        """Capa 4 (TTL Freshness): despachos recientes para detectar doble-click."""
        cutoff = (datetime.now(UTC) - timedelta(seconds=since_seconds)).isoformat(sep=" ")
        rows = self._db.fetchall(
            """
            SELECT * FROM hat_dispatch_registry
            WHERE user_id = ? AND session_id = ? AND created_at >= ?
            ORDER BY created_at DESC
            """,
            (user_id, session_id, cutoff),
        )
        return [dict(r) for r in rows]

    # ─────────────────────────────────────────────────────────
    # CRUD: hat_agent_cards
    # ─────────────────────────────────────────────────────────

    def upsert_agent_card(
        self,
        agent_id: str,
        agent_name: str,
        domain: str,
        tier: str,
        capabilities: list[str],
        orbital_keywords: list[str],
        cost_per_call: float = 0.0,
        avg_latency_ms: int = 0,
        orbital_amplitude: float = 1.0,
        orbital_velocity: float = 0.1,
    ) -> int:
        cur = self._db.execute(
            """
            INSERT INTO hat_agent_cards (agent_id, agent_name, domain, tier, capabilities, cost_per_call,
                                          avg_latency_ms, orbital_keywords, orbital_amplitude, orbital_velocity, last_seen)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
            ON CONFLICT(agent_id) DO UPDATE SET
                agent_name = excluded.agent_name,
                domain = excluded.domain,
                tier = excluded.tier,
                capabilities = excluded.capabilities,
                cost_per_call = excluded.cost_per_call,
                avg_latency_ms = excluded.avg_latency_ms,
                orbital_keywords = excluded.orbital_keywords,
                orbital_amplitude = excluded.orbital_amplitude,
                orbital_velocity = excluded.orbital_velocity,
                last_seen = CURRENT_TIMESTAMP
            """,
            (
                agent_id, agent_name, domain, tier,
                json.dumps(capabilities, ensure_ascii=False),
                cost_per_call, avg_latency_ms,
                json.dumps(orbital_keywords, ensure_ascii=False),
                orbital_amplitude, orbital_velocity,
            ),
        )
        return cur.lastrowid or 0

    def get_agent_card(self, agent_id: str) -> dict[str, Any] | None:
        row = self._db.fetchone("SELECT * FROM hat_agent_cards WHERE agent_id = ?", (agent_id,))
        return self._decode_card(row) if row else None

    def get_agent_cards(self, domain: str | None = None, tier: str | None = None) -> list[dict[str, Any]]:
        sql = "SELECT * FROM hat_agent_cards"
        conditions: list[str] = []
        params: list[Any] = []
        if domain:
            conditions.append("domain = ?")
            params.append(domain)
        if tier:
            conditions.append("tier = ?")
            params.append(tier)
        if conditions:
            sql += " WHERE " + " AND ".join(conditions)
        sql += " ORDER BY domain, tier, agent_name"
        rows = self._db.fetchall(sql, tuple(params))
        return [self._decode_card(r) for r in rows]

    @staticmethod
    def _decode_card(row: dict[str, Any]) -> dict[str, Any]:
        return {
            "id": row["id"],
            "agent_id": row["agent_id"],
            "agent_name": row["agent_name"],
            "domain": row["domain"],
            "tier": row["tier"],
            "capabilities": json.loads(row["capabilities"]) if row["capabilities"] else [],
            "cost_per_call": row["cost_per_call"],
            "avg_latency_ms": row["avg_latency_ms"],
            "orbital_keywords": json.loads(row["orbital_keywords"]) if row["orbital_keywords"] else [],
            "orbital_amplitude": row["orbital_amplitude"],
            "orbital_velocity": row["orbital_velocity"],
            "last_seen": row["last_seen"],
            "created_at": row["created_at"],
        }

    # ─────────────────────────────────────────────────────────
    # CRUD: hat_sessions
    # ─────────────────────────────────────────────────────────

    def start_session(self, user_id: str, session_id: str, active_domain: str | None = None) -> int:
        cur = self._db.execute(
            """
            INSERT INTO hat_sessions (user_id, session_id, active_domain, started_at, last_activity)
            VALUES (?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
            ON CONFLICT(session_id) DO UPDATE SET
                last_activity = CURRENT_TIMESTAMP,
                active_domain = COALESCE(excluded.active_domain, hat_sessions.active_domain)
            """,
            (user_id, session_id, active_domain),
        )
        return cur.lastrowid or 0

    def touch_session(self, session_id: str, active_domain: str | None = None, ticks_delta: int = 0, tokens_delta: int = 0) -> bool:
        cur = self._db.execute(
            """
            UPDATE hat_sessions
            SET last_activity = CURRENT_TIMESTAMP,
                active_domain = COALESCE(?, active_domain),
                orbital_tick_count = orbital_tick_count + ?,
                total_tokens_consumed = total_tokens_consumed + ?
            WHERE session_id = ?
            """,
            (active_domain, ticks_delta, tokens_delta, session_id),
        )
        return cur.rowcount > 0

    def get_session(self, session_id: str) -> dict[str, Any] | None:
        row = self._db.fetchone("SELECT * FROM hat_sessions WHERE session_id = ?", (session_id,))
        return dict(row) if row else None
