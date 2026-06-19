-- HAT-ORBITAL Ledger Schema v1.0
-- Creado en F0-D2 siguiendo HAT_ORBITAL_PLAN.md §3.2
--
-- 7 tablas que persisten variables orbitales entre sesiones:
--   - hat_facts           : hechos confirmados (θ=0 en OVC)
--   - hat_hypotheses      : creencias no verificadas (θ=π/4 en OVC)
--   - hat_plan            : próximos N pasos planificados (θ=i·2π/N en OVC)
--   - hat_progress        : historial de despachos ejecutados
--   - hat_dispatch_registry: anti-doble-llamada (hash → status, cache, ttl)
--   - hat_agent_cards     : capacidades declaradas por cada agente
--   - hat_sessions        : metadata de cada sesión de usuario

-- ============================================================
-- hat_facts
-- ============================================================
CREATE TABLE IF NOT EXISTS hat_facts (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id             TEXT NOT NULL,
    session_id          TEXT NOT NULL,
    fact_key            TEXT NOT NULL,
    fact_value          TEXT NOT NULL,        -- JSON
    confidence          REAL DEFAULT 1.0,
    orbital_theta       REAL DEFAULT 0.0,
    orbital_amplitude   REAL DEFAULT 1.0,
    created_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, session_id, fact_key)
);
CREATE INDEX IF NOT EXISTS idx_facts_user_session ON hat_facts(user_id, session_id);

-- ============================================================
-- hat_hypotheses
-- ============================================================
CREATE TABLE IF NOT EXISTS hat_hypotheses (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id             TEXT NOT NULL,
    session_id          TEXT NOT NULL,
    hypothesis_key      TEXT NOT NULL,
    hypothesis_value    TEXT NOT NULL,
    confidence          REAL DEFAULT 0.5,
    orbital_theta       REAL DEFAULT 0.785,   -- π/4 = menor confianza que Fact
    orbital_amplitude   REAL DEFAULT 0.5,
    verified            BOOLEAN DEFAULT 0,
    verified_at         TIMESTAMP,
    promoted_to_fact    BOOLEAN DEFAULT 0,
    created_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, session_id, hypothesis_key)
);
CREATE INDEX IF NOT EXISTS idx_hyp_user_session ON hat_hypotheses(user_id, session_id);

-- ============================================================
-- hat_plan
-- ============================================================
CREATE TABLE IF NOT EXISTS hat_plan (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id             TEXT NOT NULL,
    session_id          TEXT NOT NULL,
    step_index          INTEGER NOT NULL,
    step_description    TEXT NOT NULL,
    step_status         TEXT DEFAULT 'pending', -- pending|in_progress|done|skipped|failed
    assigned_domain     TEXT,                   -- research|build|operate
    dispatch_id         TEXT,
    orbital_var_name    TEXT,
    orbital_theta       REAL,
    created_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, session_id, step_index)
);
CREATE INDEX IF NOT EXISTS idx_plan_user_session ON hat_plan(user_id, session_id);

-- ============================================================
-- hat_progress
-- ============================================================
CREATE TABLE IF NOT EXISTS hat_progress (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id             TEXT NOT NULL,
    session_id          TEXT NOT NULL,
    dispatch_id         TEXT NOT NULL UNIQUE,
    domain              TEXT NOT NULL,
    specialist          TEXT,
    worker              TEXT,
    status              TEXT NOT NULL,           -- dispatched|running|completed|failed
    result_summary      TEXT,                    -- JSON con output resumido
    orbital_resonance   REAL,
    started_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_at        TIMESTAMP
);

-- ============================================================
-- hat_dispatch_registry — anti-doble-llamada
-- ============================================================
CREATE TABLE IF NOT EXISTS hat_dispatch_registry (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    intent_hash         TEXT NOT NULL UNIQUE,    -- sha256(user_id + session_id + normalized_intent + sorted(params))
    user_id             TEXT NOT NULL,
    session_id          TEXT NOT NULL,
    domain              TEXT NOT NULL,
    status              TEXT NOT NULL,           -- in_progress|completed|failed
    result_cache        TEXT,                    -- JSON del resultado si completed
    subscriber_count    INTEGER DEFAULT 0,
    created_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_at        TIMESTAMP,
    ttl_expires_at      TIMESTAMP                -- para capa 4 (TTL Freshness)
);
CREATE INDEX IF NOT EXISTS idx_dispatch_hash ON hat_dispatch_registry(intent_hash);
CREATE INDEX IF NOT EXISTS idx_dispatch_ttl ON hat_dispatch_registry(ttl_expires_at);
CREATE INDEX IF NOT EXISTS idx_dispatch_status ON hat_dispatch_registry(status);

-- ============================================================
-- hat_agent_cards
-- ============================================================
CREATE TABLE IF NOT EXISTS hat_agent_cards (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    agent_id            TEXT NOT NULL UNIQUE,
    agent_name          TEXT NOT NULL,
    domain              TEXT NOT NULL,           -- research|build|operate
    tier                TEXT NOT NULL,           -- supervisor|specialist|worker
    capabilities        TEXT NOT NULL,           -- JSON array
    cost_per_call       REAL DEFAULT 0.0,
    avg_latency_ms      INTEGER DEFAULT 0,
    orbital_keywords    TEXT NOT NULL,           -- JSON array, para resonancia RCC
    orbital_amplitude   REAL DEFAULT 1.0,
    orbital_velocity    REAL DEFAULT 0.1,
    last_seen           TIMESTAMP,
    created_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_cards_domain ON hat_agent_cards(domain, tier);

-- ============================================================
-- hat_sessions
-- ============================================================
CREATE TABLE IF NOT EXISTS hat_sessions (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id             TEXT NOT NULL,
    session_id          TEXT NOT NULL UNIQUE,
    started_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_activity       TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    active_domain       TEXT,
    orbital_tick_count  INTEGER DEFAULT 0,
    total_tokens_consumed INTEGER DEFAULT 0,
    UNIQUE(user_id, session_id)
);
CREATE INDEX IF NOT EXISTS idx_sessions_user ON hat_sessions(user_id);
