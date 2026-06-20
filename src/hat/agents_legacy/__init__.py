"""HAT — Agents Legacy (migrado desde src/agents/ en M5).

Contiene el framework de agentes heredado que aún usan:
- src/api_v2/routers/agents.py (MultiAgentOrchestrator, AgentRuntime)
- src/hat/level3_specialists/base/specialist_agent.py (BaseAgent)

Estos archivos se mantienen por compatibilidad hasta que M6/M8
implementen specialists reales que no dependan de BaseAgent.

Migrado en M5 desde:
- src/agents/base.py → src/hat/agents_legacy/base.py
- src/agents/orchestrator.py → src/hat/agents_legacy/orchestrator.py
- src/agents/runtime.py → src/hat/agents_legacy/runtime.py
- src/agents/token_tracking.py → src/core/observability/token_tracking.py

Eliminados en M5 (huérfanos):
- src/agents/memory.py (fake embeddings, 0 callers)
- src/agents/tools.py (AgentToolRegistry, 0 callers)
"""
from src.hat.agents_legacy.base import (
    AgentCapability,
    AgentConfig,
    AgentMessage,
    AgentState,
    BaseAgent,
    VALID_TRANSITIONS,
)
from src.hat.agents_legacy.orchestrator import (
    OrchestrationPattern,
    OrchestrationPlan,
    OrchestrationResult,
    OrchestrationStrategy,
    MultiAgentOrchestrator,
)
from src.hat.agents_legacy.runtime import AgentRuntime, RuntimeStats

__all__ = [
    "AgentCapability", "AgentConfig", "AgentMessage", "AgentState",
    "BaseAgent", "VALID_TRANSITIONS",
    "OrchestrationPattern", "OrchestrationPlan", "OrchestrationResult",
    "OrchestrationStrategy", "MultiAgentOrchestrator",
    "AgentRuntime", "RuntimeStats",
]
