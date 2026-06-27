"""Base Agent — Abstract foundation for all Zenic-Flijo agents.

Provides lifecycle management, state transitions, capability declarations,
orbital integration, and structured communication between agents.
"""

from __future__ import annotations

import threading
import time
import uuid
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from typing import Any

from src.utils.logger import get_logger

logger = get_logger("agent.base")


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class AgentState(Enum):
    """Agent lifecycle states following a strict state machine."""

    IDLE = "idle"
    THINKING = "thinking"
    EXECUTING = "executing"
    WAITING = "waiting"
    PAUSED = "paused"
    ERROR = "error"
    TERMINATED = "terminated"


class AgentCapability(Enum):
    """Capabilities an agent can declare."""

    REASONING = "reasoning"
    TOOL_USE = "tool_use"
    CODE_GENERATION = "code_generation"
    DATA_ANALYSIS = "data_analysis"
    WORKFLOW_ORCHESTRATION = "workflow_orchestration"
    NLU_PROCESSING = "nlu_processing"
    FILE_OPERATIONS = "file_operations"
    API_CALLS = "api_calls"
    MEMORY_ACCESS = "memory_access"
    MULTI_AGENT_COORDINATION = "multi_agent_coordination"


# Valid state transitions
VALID_TRANSITIONS: dict[AgentState, set[AgentState]] = {
    AgentState.IDLE: {AgentState.THINKING, AgentState.TERMINATED},
    AgentState.THINKING: {AgentState.EXECUTING, AgentState.WAITING, AgentState.ERROR, AgentState.IDLE},
    AgentState.EXECUTING: {AgentState.THINKING, AgentState.WAITING, AgentState.ERROR, AgentState.IDLE},
    AgentState.WAITING: {AgentState.THINKING, AgentState.PAUSED, AgentState.ERROR, AgentState.IDLE},
    AgentState.PAUSED: {AgentState.THINKING, AgentState.TERMINATED},
    AgentState.ERROR: {AgentState.IDLE, AgentState.TERMINATED},
    AgentState.TERMINATED: set(),
}


@dataclass
class AgentMessage:
    """Structured message for inter-agent communication."""

    sender_id: str
    recipient_id: str
    content: Any
    message_type: str = "inform"
    correlation_id: str = ""
    timestamp: float = field(default_factory=time.time)
    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.correlation_id:
            self.correlation_id = str(uuid.uuid4())


@dataclass
class AgentConfig:
    """Configuration for an agent instance."""

    agent_id: str = ""
    name: str = ""
    description: str = ""
    capabilities: list[AgentCapability] = field(default_factory=list)
    max_iterations: int = 10
    timeout_seconds: float = 300.0
    memory_enabled: bool = True
    orbital_enabled: bool = True
    tools_enabled: bool = True
    custom_config: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.agent_id:
            self.agent_id = f"agent-{uuid.uuid4().hex[:8]}"
        if not self.name:
            self.name = self.agent_id
mutants_xǁBaseAgentǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁBaseAgentǁtransition_to__mutmut: MutantDict = {}  # type: ignore
mutants_xǁBaseAgentǁforce_state__mutmut: MutantDict = {}  # type: ignore
mutants_xǁBaseAgentǁrun__mutmut: MutantDict = {}  # type: ignore
mutants_xǁBaseAgentǁpause__mutmut: MutantDict = {}  # type: ignore
mutants_xǁBaseAgentǁresume__mutmut: MutantDict = {}  # type: ignore
mutants_xǁBaseAgentǁterminate__mutmut: MutantDict = {}  # type: ignore
mutants_xǁBaseAgentǁsend_message__mutmut: MutantDict = {}  # type: ignore
mutants_xǁBaseAgentǁreceive_message__mutmut: MutantDict = {}  # type: ignore
mutants_xǁBaseAgentǁget_pending_messages__mutmut: MutantDict = {}  # type: ignore
mutants_xǁBaseAgentǁset_context__mutmut: MutantDict = {}  # type: ignore
mutants_xǁBaseAgentǁget_context__mutmut: MutantDict = {}  # type: ignore
mutants_xǁBaseAgentǁ_should_stop__mutmut: MutantDict = {}  # type: ignore
mutants_xǁBaseAgentǁget_status__mutmut: MutantDict = {}  # type: ignore


class BaseAgent(ABC):
    """Abstract base class for all Zenic-Flijo agents.

    Implements lifecycle management, state transitions, capability declarations,
    and orbital context integration. Concrete agents must implement `think()`
    and `act()` methods.

    Usage:
        class MyAgent(BaseAgent):
            def think(self, observation):
                # reasoning logic
                return {"decision": "proceed"}

            def act(self, decision):
                # action logic
                return {"result": "done"}
    """

    @_mutmut_mutated(mutants_xǁBaseAgentǁ__init____mutmut)
    def __init__(self, config: AgentConfig) -> None:
        self.config = config
        self._state = AgentState.IDLE
        self._state_lock = threading.Lock()
        self._message_queue: list[AgentMessage] = []
        self._message_lock = threading.Lock()
        self._execution_history: list[dict[str, Any]] = []
        self._created_at = time.time()
        self._last_active = self._created_at
        self._iteration_count = 0
        self._error_count = 0
        self._parent_id: str | None = None
        self._child_ids: list[str] = []
        self._context: dict[str, Any] = {}
        logger.info(
            "Agent initialized: id=%s name=%s capabilities=%s max_iterations=%d",
            self.agent_id,
            self.name,
            [c.value for c in self.config.capabilities],
            self.config.max_iterations,
        )

    def xǁBaseAgentǁ__init____mutmut_orig(self, config: AgentConfig) -> None:
        self.config = config
        self._state = AgentState.IDLE
        self._state_lock = threading.Lock()
        self._message_queue: list[AgentMessage] = []
        self._message_lock = threading.Lock()
        self._execution_history: list[dict[str, Any]] = []
        self._created_at = time.time()
        self._last_active = self._created_at
        self._iteration_count = 0
        self._error_count = 0
        self._parent_id: str | None = None
        self._child_ids: list[str] = []
        self._context: dict[str, Any] = {}
        logger.info(
            "Agent initialized: id=%s name=%s capabilities=%s max_iterations=%d",
            self.agent_id,
            self.name,
            [c.value for c in self.config.capabilities],
            self.config.max_iterations,
        )

    def xǁBaseAgentǁ__init____mutmut_1(self, config: AgentConfig) -> None:
        self.config = None
        self._state = AgentState.IDLE
        self._state_lock = threading.Lock()
        self._message_queue: list[AgentMessage] = []
        self._message_lock = threading.Lock()
        self._execution_history: list[dict[str, Any]] = []
        self._created_at = time.time()
        self._last_active = self._created_at
        self._iteration_count = 0
        self._error_count = 0
        self._parent_id: str | None = None
        self._child_ids: list[str] = []
        self._context: dict[str, Any] = {}
        logger.info(
            "Agent initialized: id=%s name=%s capabilities=%s max_iterations=%d",
            self.agent_id,
            self.name,
            [c.value for c in self.config.capabilities],
            self.config.max_iterations,
        )

    def xǁBaseAgentǁ__init____mutmut_2(self, config: AgentConfig) -> None:
        self.config = config
        self._state = None
        self._state_lock = threading.Lock()
        self._message_queue: list[AgentMessage] = []
        self._message_lock = threading.Lock()
        self._execution_history: list[dict[str, Any]] = []
        self._created_at = time.time()
        self._last_active = self._created_at
        self._iteration_count = 0
        self._error_count = 0
        self._parent_id: str | None = None
        self._child_ids: list[str] = []
        self._context: dict[str, Any] = {}
        logger.info(
            "Agent initialized: id=%s name=%s capabilities=%s max_iterations=%d",
            self.agent_id,
            self.name,
            [c.value for c in self.config.capabilities],
            self.config.max_iterations,
        )

    def xǁBaseAgentǁ__init____mutmut_3(self, config: AgentConfig) -> None:
        self.config = config
        self._state = AgentState.IDLE
        self._state_lock = None
        self._message_queue: list[AgentMessage] = []
        self._message_lock = threading.Lock()
        self._execution_history: list[dict[str, Any]] = []
        self._created_at = time.time()
        self._last_active = self._created_at
        self._iteration_count = 0
        self._error_count = 0
        self._parent_id: str | None = None
        self._child_ids: list[str] = []
        self._context: dict[str, Any] = {}
        logger.info(
            "Agent initialized: id=%s name=%s capabilities=%s max_iterations=%d",
            self.agent_id,
            self.name,
            [c.value for c in self.config.capabilities],
            self.config.max_iterations,
        )

    def xǁBaseAgentǁ__init____mutmut_4(self, config: AgentConfig) -> None:
        self.config = config
        self._state = AgentState.IDLE
        self._state_lock = threading.Lock()
        self._message_queue: list[AgentMessage] = None
        self._message_lock = threading.Lock()
        self._execution_history: list[dict[str, Any]] = []
        self._created_at = time.time()
        self._last_active = self._created_at
        self._iteration_count = 0
        self._error_count = 0
        self._parent_id: str | None = None
        self._child_ids: list[str] = []
        self._context: dict[str, Any] = {}
        logger.info(
            "Agent initialized: id=%s name=%s capabilities=%s max_iterations=%d",
            self.agent_id,
            self.name,
            [c.value for c in self.config.capabilities],
            self.config.max_iterations,
        )

    def xǁBaseAgentǁ__init____mutmut_5(self, config: AgentConfig) -> None:
        self.config = config
        self._state = AgentState.IDLE
        self._state_lock = threading.Lock()
        self._message_queue: list[AgentMessage] = []
        self._message_lock = None
        self._execution_history: list[dict[str, Any]] = []
        self._created_at = time.time()
        self._last_active = self._created_at
        self._iteration_count = 0
        self._error_count = 0
        self._parent_id: str | None = None
        self._child_ids: list[str] = []
        self._context: dict[str, Any] = {}
        logger.info(
            "Agent initialized: id=%s name=%s capabilities=%s max_iterations=%d",
            self.agent_id,
            self.name,
            [c.value for c in self.config.capabilities],
            self.config.max_iterations,
        )

    def xǁBaseAgentǁ__init____mutmut_6(self, config: AgentConfig) -> None:
        self.config = config
        self._state = AgentState.IDLE
        self._state_lock = threading.Lock()
        self._message_queue: list[AgentMessage] = []
        self._message_lock = threading.Lock()
        self._execution_history: list[dict[str, Any]] = None
        self._created_at = time.time()
        self._last_active = self._created_at
        self._iteration_count = 0
        self._error_count = 0
        self._parent_id: str | None = None
        self._child_ids: list[str] = []
        self._context: dict[str, Any] = {}
        logger.info(
            "Agent initialized: id=%s name=%s capabilities=%s max_iterations=%d",
            self.agent_id,
            self.name,
            [c.value for c in self.config.capabilities],
            self.config.max_iterations,
        )

    def xǁBaseAgentǁ__init____mutmut_7(self, config: AgentConfig) -> None:
        self.config = config
        self._state = AgentState.IDLE
        self._state_lock = threading.Lock()
        self._message_queue: list[AgentMessage] = []
        self._message_lock = threading.Lock()
        self._execution_history: list[dict[str, Any]] = []
        self._created_at = None
        self._last_active = self._created_at
        self._iteration_count = 0
        self._error_count = 0
        self._parent_id: str | None = None
        self._child_ids: list[str] = []
        self._context: dict[str, Any] = {}
        logger.info(
            "Agent initialized: id=%s name=%s capabilities=%s max_iterations=%d",
            self.agent_id,
            self.name,
            [c.value for c in self.config.capabilities],
            self.config.max_iterations,
        )

    def xǁBaseAgentǁ__init____mutmut_8(self, config: AgentConfig) -> None:
        self.config = config
        self._state = AgentState.IDLE
        self._state_lock = threading.Lock()
        self._message_queue: list[AgentMessage] = []
        self._message_lock = threading.Lock()
        self._execution_history: list[dict[str, Any]] = []
        self._created_at = time.time()
        self._last_active = None
        self._iteration_count = 0
        self._error_count = 0
        self._parent_id: str | None = None
        self._child_ids: list[str] = []
        self._context: dict[str, Any] = {}
        logger.info(
            "Agent initialized: id=%s name=%s capabilities=%s max_iterations=%d",
            self.agent_id,
            self.name,
            [c.value for c in self.config.capabilities],
            self.config.max_iterations,
        )

    def xǁBaseAgentǁ__init____mutmut_9(self, config: AgentConfig) -> None:
        self.config = config
        self._state = AgentState.IDLE
        self._state_lock = threading.Lock()
        self._message_queue: list[AgentMessage] = []
        self._message_lock = threading.Lock()
        self._execution_history: list[dict[str, Any]] = []
        self._created_at = time.time()
        self._last_active = self._created_at
        self._iteration_count = None
        self._error_count = 0
        self._parent_id: str | None = None
        self._child_ids: list[str] = []
        self._context: dict[str, Any] = {}
        logger.info(
            "Agent initialized: id=%s name=%s capabilities=%s max_iterations=%d",
            self.agent_id,
            self.name,
            [c.value for c in self.config.capabilities],
            self.config.max_iterations,
        )

    def xǁBaseAgentǁ__init____mutmut_10(self, config: AgentConfig) -> None:
        self.config = config
        self._state = AgentState.IDLE
        self._state_lock = threading.Lock()
        self._message_queue: list[AgentMessage] = []
        self._message_lock = threading.Lock()
        self._execution_history: list[dict[str, Any]] = []
        self._created_at = time.time()
        self._last_active = self._created_at
        self._iteration_count = 1
        self._error_count = 0
        self._parent_id: str | None = None
        self._child_ids: list[str] = []
        self._context: dict[str, Any] = {}
        logger.info(
            "Agent initialized: id=%s name=%s capabilities=%s max_iterations=%d",
            self.agent_id,
            self.name,
            [c.value for c in self.config.capabilities],
            self.config.max_iterations,
        )

    def xǁBaseAgentǁ__init____mutmut_11(self, config: AgentConfig) -> None:
        self.config = config
        self._state = AgentState.IDLE
        self._state_lock = threading.Lock()
        self._message_queue: list[AgentMessage] = []
        self._message_lock = threading.Lock()
        self._execution_history: list[dict[str, Any]] = []
        self._created_at = time.time()
        self._last_active = self._created_at
        self._iteration_count = 0
        self._error_count = None
        self._parent_id: str | None = None
        self._child_ids: list[str] = []
        self._context: dict[str, Any] = {}
        logger.info(
            "Agent initialized: id=%s name=%s capabilities=%s max_iterations=%d",
            self.agent_id,
            self.name,
            [c.value for c in self.config.capabilities],
            self.config.max_iterations,
        )

    def xǁBaseAgentǁ__init____mutmut_12(self, config: AgentConfig) -> None:
        self.config = config
        self._state = AgentState.IDLE
        self._state_lock = threading.Lock()
        self._message_queue: list[AgentMessage] = []
        self._message_lock = threading.Lock()
        self._execution_history: list[dict[str, Any]] = []
        self._created_at = time.time()
        self._last_active = self._created_at
        self._iteration_count = 0
        self._error_count = 1
        self._parent_id: str | None = None
        self._child_ids: list[str] = []
        self._context: dict[str, Any] = {}
        logger.info(
            "Agent initialized: id=%s name=%s capabilities=%s max_iterations=%d",
            self.agent_id,
            self.name,
            [c.value for c in self.config.capabilities],
            self.config.max_iterations,
        )

    def xǁBaseAgentǁ__init____mutmut_13(self, config: AgentConfig) -> None:
        self.config = config
        self._state = AgentState.IDLE
        self._state_lock = threading.Lock()
        self._message_queue: list[AgentMessage] = []
        self._message_lock = threading.Lock()
        self._execution_history: list[dict[str, Any]] = []
        self._created_at = time.time()
        self._last_active = self._created_at
        self._iteration_count = 0
        self._error_count = 0
        self._parent_id: str | None = ""
        self._child_ids: list[str] = []
        self._context: dict[str, Any] = {}
        logger.info(
            "Agent initialized: id=%s name=%s capabilities=%s max_iterations=%d",
            self.agent_id,
            self.name,
            [c.value for c in self.config.capabilities],
            self.config.max_iterations,
        )

    def xǁBaseAgentǁ__init____mutmut_14(self, config: AgentConfig) -> None:
        self.config = config
        self._state = AgentState.IDLE
        self._state_lock = threading.Lock()
        self._message_queue: list[AgentMessage] = []
        self._message_lock = threading.Lock()
        self._execution_history: list[dict[str, Any]] = []
        self._created_at = time.time()
        self._last_active = self._created_at
        self._iteration_count = 0
        self._error_count = 0
        self._parent_id: str | None = None
        self._child_ids: list[str] = None
        self._context: dict[str, Any] = {}
        logger.info(
            "Agent initialized: id=%s name=%s capabilities=%s max_iterations=%d",
            self.agent_id,
            self.name,
            [c.value for c in self.config.capabilities],
            self.config.max_iterations,
        )

    def xǁBaseAgentǁ__init____mutmut_15(self, config: AgentConfig) -> None:
        self.config = config
        self._state = AgentState.IDLE
        self._state_lock = threading.Lock()
        self._message_queue: list[AgentMessage] = []
        self._message_lock = threading.Lock()
        self._execution_history: list[dict[str, Any]] = []
        self._created_at = time.time()
        self._last_active = self._created_at
        self._iteration_count = 0
        self._error_count = 0
        self._parent_id: str | None = None
        self._child_ids: list[str] = []
        self._context: dict[str, Any] = None
        logger.info(
            "Agent initialized: id=%s name=%s capabilities=%s max_iterations=%d",
            self.agent_id,
            self.name,
            [c.value for c in self.config.capabilities],
            self.config.max_iterations,
        )

    def xǁBaseAgentǁ__init____mutmut_16(self, config: AgentConfig) -> None:
        self.config = config
        self._state = AgentState.IDLE
        self._state_lock = threading.Lock()
        self._message_queue: list[AgentMessage] = []
        self._message_lock = threading.Lock()
        self._execution_history: list[dict[str, Any]] = []
        self._created_at = time.time()
        self._last_active = self._created_at
        self._iteration_count = 0
        self._error_count = 0
        self._parent_id: str | None = None
        self._child_ids: list[str] = []
        self._context: dict[str, Any] = {}
        logger.info(
            None,
            self.agent_id,
            self.name,
            [c.value for c in self.config.capabilities],
            self.config.max_iterations,
        )

    def xǁBaseAgentǁ__init____mutmut_17(self, config: AgentConfig) -> None:
        self.config = config
        self._state = AgentState.IDLE
        self._state_lock = threading.Lock()
        self._message_queue: list[AgentMessage] = []
        self._message_lock = threading.Lock()
        self._execution_history: list[dict[str, Any]] = []
        self._created_at = time.time()
        self._last_active = self._created_at
        self._iteration_count = 0
        self._error_count = 0
        self._parent_id: str | None = None
        self._child_ids: list[str] = []
        self._context: dict[str, Any] = {}
        logger.info(
            "Agent initialized: id=%s name=%s capabilities=%s max_iterations=%d",
            None,
            self.name,
            [c.value for c in self.config.capabilities],
            self.config.max_iterations,
        )

    def xǁBaseAgentǁ__init____mutmut_18(self, config: AgentConfig) -> None:
        self.config = config
        self._state = AgentState.IDLE
        self._state_lock = threading.Lock()
        self._message_queue: list[AgentMessage] = []
        self._message_lock = threading.Lock()
        self._execution_history: list[dict[str, Any]] = []
        self._created_at = time.time()
        self._last_active = self._created_at
        self._iteration_count = 0
        self._error_count = 0
        self._parent_id: str | None = None
        self._child_ids: list[str] = []
        self._context: dict[str, Any] = {}
        logger.info(
            "Agent initialized: id=%s name=%s capabilities=%s max_iterations=%d",
            self.agent_id,
            None,
            [c.value for c in self.config.capabilities],
            self.config.max_iterations,
        )

    def xǁBaseAgentǁ__init____mutmut_19(self, config: AgentConfig) -> None:
        self.config = config
        self._state = AgentState.IDLE
        self._state_lock = threading.Lock()
        self._message_queue: list[AgentMessage] = []
        self._message_lock = threading.Lock()
        self._execution_history: list[dict[str, Any]] = []
        self._created_at = time.time()
        self._last_active = self._created_at
        self._iteration_count = 0
        self._error_count = 0
        self._parent_id: str | None = None
        self._child_ids: list[str] = []
        self._context: dict[str, Any] = {}
        logger.info(
            "Agent initialized: id=%s name=%s capabilities=%s max_iterations=%d",
            self.agent_id,
            self.name,
            None,
            self.config.max_iterations,
        )

    def xǁBaseAgentǁ__init____mutmut_20(self, config: AgentConfig) -> None:
        self.config = config
        self._state = AgentState.IDLE
        self._state_lock = threading.Lock()
        self._message_queue: list[AgentMessage] = []
        self._message_lock = threading.Lock()
        self._execution_history: list[dict[str, Any]] = []
        self._created_at = time.time()
        self._last_active = self._created_at
        self._iteration_count = 0
        self._error_count = 0
        self._parent_id: str | None = None
        self._child_ids: list[str] = []
        self._context: dict[str, Any] = {}
        logger.info(
            "Agent initialized: id=%s name=%s capabilities=%s max_iterations=%d",
            self.agent_id,
            self.name,
            [c.value for c in self.config.capabilities],
            None,
        )

    def xǁBaseAgentǁ__init____mutmut_21(self, config: AgentConfig) -> None:
        self.config = config
        self._state = AgentState.IDLE
        self._state_lock = threading.Lock()
        self._message_queue: list[AgentMessage] = []
        self._message_lock = threading.Lock()
        self._execution_history: list[dict[str, Any]] = []
        self._created_at = time.time()
        self._last_active = self._created_at
        self._iteration_count = 0
        self._error_count = 0
        self._parent_id: str | None = None
        self._child_ids: list[str] = []
        self._context: dict[str, Any] = {}
        logger.info(
            self.agent_id,
            self.name,
            [c.value for c in self.config.capabilities],
            self.config.max_iterations,
        )

    def xǁBaseAgentǁ__init____mutmut_22(self, config: AgentConfig) -> None:
        self.config = config
        self._state = AgentState.IDLE
        self._state_lock = threading.Lock()
        self._message_queue: list[AgentMessage] = []
        self._message_lock = threading.Lock()
        self._execution_history: list[dict[str, Any]] = []
        self._created_at = time.time()
        self._last_active = self._created_at
        self._iteration_count = 0
        self._error_count = 0
        self._parent_id: str | None = None
        self._child_ids: list[str] = []
        self._context: dict[str, Any] = {}
        logger.info(
            "Agent initialized: id=%s name=%s capabilities=%s max_iterations=%d",
            self.name,
            [c.value for c in self.config.capabilities],
            self.config.max_iterations,
        )

    def xǁBaseAgentǁ__init____mutmut_23(self, config: AgentConfig) -> None:
        self.config = config
        self._state = AgentState.IDLE
        self._state_lock = threading.Lock()
        self._message_queue: list[AgentMessage] = []
        self._message_lock = threading.Lock()
        self._execution_history: list[dict[str, Any]] = []
        self._created_at = time.time()
        self._last_active = self._created_at
        self._iteration_count = 0
        self._error_count = 0
        self._parent_id: str | None = None
        self._child_ids: list[str] = []
        self._context: dict[str, Any] = {}
        logger.info(
            "Agent initialized: id=%s name=%s capabilities=%s max_iterations=%d",
            self.agent_id,
            [c.value for c in self.config.capabilities],
            self.config.max_iterations,
        )

    def xǁBaseAgentǁ__init____mutmut_24(self, config: AgentConfig) -> None:
        self.config = config
        self._state = AgentState.IDLE
        self._state_lock = threading.Lock()
        self._message_queue: list[AgentMessage] = []
        self._message_lock = threading.Lock()
        self._execution_history: list[dict[str, Any]] = []
        self._created_at = time.time()
        self._last_active = self._created_at
        self._iteration_count = 0
        self._error_count = 0
        self._parent_id: str | None = None
        self._child_ids: list[str] = []
        self._context: dict[str, Any] = {}
        logger.info(
            "Agent initialized: id=%s name=%s capabilities=%s max_iterations=%d",
            self.agent_id,
            self.name,
            self.config.max_iterations,
        )

    def xǁBaseAgentǁ__init____mutmut_25(self, config: AgentConfig) -> None:
        self.config = config
        self._state = AgentState.IDLE
        self._state_lock = threading.Lock()
        self._message_queue: list[AgentMessage] = []
        self._message_lock = threading.Lock()
        self._execution_history: list[dict[str, Any]] = []
        self._created_at = time.time()
        self._last_active = self._created_at
        self._iteration_count = 0
        self._error_count = 0
        self._parent_id: str | None = None
        self._child_ids: list[str] = []
        self._context: dict[str, Any] = {}
        logger.info(
            "Agent initialized: id=%s name=%s capabilities=%s max_iterations=%d",
            self.agent_id,
            self.name,
            [c.value for c in self.config.capabilities],
            )

    def xǁBaseAgentǁ__init____mutmut_26(self, config: AgentConfig) -> None:
        self.config = config
        self._state = AgentState.IDLE
        self._state_lock = threading.Lock()
        self._message_queue: list[AgentMessage] = []
        self._message_lock = threading.Lock()
        self._execution_history: list[dict[str, Any]] = []
        self._created_at = time.time()
        self._last_active = self._created_at
        self._iteration_count = 0
        self._error_count = 0
        self._parent_id: str | None = None
        self._child_ids: list[str] = []
        self._context: dict[str, Any] = {}
        logger.info(
            "XXAgent initialized: id=%s name=%s capabilities=%s max_iterations=%dXX",
            self.agent_id,
            self.name,
            [c.value for c in self.config.capabilities],
            self.config.max_iterations,
        )

    def xǁBaseAgentǁ__init____mutmut_27(self, config: AgentConfig) -> None:
        self.config = config
        self._state = AgentState.IDLE
        self._state_lock = threading.Lock()
        self._message_queue: list[AgentMessage] = []
        self._message_lock = threading.Lock()
        self._execution_history: list[dict[str, Any]] = []
        self._created_at = time.time()
        self._last_active = self._created_at
        self._iteration_count = 0
        self._error_count = 0
        self._parent_id: str | None = None
        self._child_ids: list[str] = []
        self._context: dict[str, Any] = {}
        logger.info(
            "agent initialized: id=%s name=%s capabilities=%s max_iterations=%d",
            self.agent_id,
            self.name,
            [c.value for c in self.config.capabilities],
            self.config.max_iterations,
        )

    def xǁBaseAgentǁ__init____mutmut_28(self, config: AgentConfig) -> None:
        self.config = config
        self._state = AgentState.IDLE
        self._state_lock = threading.Lock()
        self._message_queue: list[AgentMessage] = []
        self._message_lock = threading.Lock()
        self._execution_history: list[dict[str, Any]] = []
        self._created_at = time.time()
        self._last_active = self._created_at
        self._iteration_count = 0
        self._error_count = 0
        self._parent_id: str | None = None
        self._child_ids: list[str] = []
        self._context: dict[str, Any] = {}
        logger.info(
            "AGENT INITIALIZED: ID=%S NAME=%S CAPABILITIES=%S MAX_ITERATIONS=%D",
            self.agent_id,
            self.name,
            [c.value for c in self.config.capabilities],
            self.config.max_iterations,
        )

    # ── Properties ──────────────────────────────────────────

    @property
    def agent_id(self) -> str:
        return self.config.agent_id

    @property
    def name(self) -> str:
        return self.config.name

    @property
    def state(self) -> AgentState:
        with self._state_lock:
            return self._state

    @property
    def capabilities(self) -> list[AgentCapability]:
        return self.config.capabilities

    @property
    def is_active(self) -> bool:
        return self.state not in {AgentState.TERMINATED, AgentState.ERROR}

    @property
    def uptime(self) -> float:
        return time.time() - self._created_at

    @property
    def iteration_count(self) -> int:
        return self._iteration_count

    # ── State Machine ───────────────────────────────────────

    @_mutmut_mutated(mutants_xǁBaseAgentǁtransition_to__mutmut)
    def transition_to(self, new_state: AgentState) -> bool:
        """Attempt a state transition. Returns True if successful."""
        with self._state_lock:
            old_state = self._state
            if new_state not in VALID_TRANSITIONS.get(old_state, set()):
                logger.warning(
                    "Invalid state transition: agent=%s from=%s to=%s",
                    self.agent_id,
                    old_state.value,
                    new_state.value,
                )
                return False
            self._state = new_state
            self._last_active = time.time()
            logger.debug(
                "State transition: agent=%s from=%s to=%s",
                self.agent_id,
                old_state.value,
                new_state.value,
            )
            return True

    # ── State Machine ───────────────────────────────────────

    def xǁBaseAgentǁtransition_to__mutmut_orig(self, new_state: AgentState) -> bool:
        """Attempt a state transition. Returns True if successful."""
        with self._state_lock:
            old_state = self._state
            if new_state not in VALID_TRANSITIONS.get(old_state, set()):
                logger.warning(
                    "Invalid state transition: agent=%s from=%s to=%s",
                    self.agent_id,
                    old_state.value,
                    new_state.value,
                )
                return False
            self._state = new_state
            self._last_active = time.time()
            logger.debug(
                "State transition: agent=%s from=%s to=%s",
                self.agent_id,
                old_state.value,
                new_state.value,
            )
            return True

    # ── State Machine ───────────────────────────────────────

    def xǁBaseAgentǁtransition_to__mutmut_1(self, new_state: AgentState) -> bool:
        """Attempt a state transition. Returns True if successful."""
        with self._state_lock:
            old_state = None
            if new_state not in VALID_TRANSITIONS.get(old_state, set()):
                logger.warning(
                    "Invalid state transition: agent=%s from=%s to=%s",
                    self.agent_id,
                    old_state.value,
                    new_state.value,
                )
                return False
            self._state = new_state
            self._last_active = time.time()
            logger.debug(
                "State transition: agent=%s from=%s to=%s",
                self.agent_id,
                old_state.value,
                new_state.value,
            )
            return True

    # ── State Machine ───────────────────────────────────────

    def xǁBaseAgentǁtransition_to__mutmut_2(self, new_state: AgentState) -> bool:
        """Attempt a state transition. Returns True if successful."""
        with self._state_lock:
            old_state = self._state
            if new_state in VALID_TRANSITIONS.get(old_state, set()):
                logger.warning(
                    "Invalid state transition: agent=%s from=%s to=%s",
                    self.agent_id,
                    old_state.value,
                    new_state.value,
                )
                return False
            self._state = new_state
            self._last_active = time.time()
            logger.debug(
                "State transition: agent=%s from=%s to=%s",
                self.agent_id,
                old_state.value,
                new_state.value,
            )
            return True

    # ── State Machine ───────────────────────────────────────

    def xǁBaseAgentǁtransition_to__mutmut_3(self, new_state: AgentState) -> bool:
        """Attempt a state transition. Returns True if successful."""
        with self._state_lock:
            old_state = self._state
            if new_state not in VALID_TRANSITIONS.get(None, set()):
                logger.warning(
                    "Invalid state transition: agent=%s from=%s to=%s",
                    self.agent_id,
                    old_state.value,
                    new_state.value,
                )
                return False
            self._state = new_state
            self._last_active = time.time()
            logger.debug(
                "State transition: agent=%s from=%s to=%s",
                self.agent_id,
                old_state.value,
                new_state.value,
            )
            return True

    # ── State Machine ───────────────────────────────────────

    def xǁBaseAgentǁtransition_to__mutmut_4(self, new_state: AgentState) -> bool:
        """Attempt a state transition. Returns True if successful."""
        with self._state_lock:
            old_state = self._state
            if new_state not in VALID_TRANSITIONS.get(old_state, None):
                logger.warning(
                    "Invalid state transition: agent=%s from=%s to=%s",
                    self.agent_id,
                    old_state.value,
                    new_state.value,
                )
                return False
            self._state = new_state
            self._last_active = time.time()
            logger.debug(
                "State transition: agent=%s from=%s to=%s",
                self.agent_id,
                old_state.value,
                new_state.value,
            )
            return True

    # ── State Machine ───────────────────────────────────────

    def xǁBaseAgentǁtransition_to__mutmut_5(self, new_state: AgentState) -> bool:
        """Attempt a state transition. Returns True if successful."""
        with self._state_lock:
            old_state = self._state
            if new_state not in VALID_TRANSITIONS.get(set()):
                logger.warning(
                    "Invalid state transition: agent=%s from=%s to=%s",
                    self.agent_id,
                    old_state.value,
                    new_state.value,
                )
                return False
            self._state = new_state
            self._last_active = time.time()
            logger.debug(
                "State transition: agent=%s from=%s to=%s",
                self.agent_id,
                old_state.value,
                new_state.value,
            )
            return True

    # ── State Machine ───────────────────────────────────────

    def xǁBaseAgentǁtransition_to__mutmut_6(self, new_state: AgentState) -> bool:
        """Attempt a state transition. Returns True if successful."""
        with self._state_lock:
            old_state = self._state
            if new_state not in VALID_TRANSITIONS.get(old_state, ):
                logger.warning(
                    "Invalid state transition: agent=%s from=%s to=%s",
                    self.agent_id,
                    old_state.value,
                    new_state.value,
                )
                return False
            self._state = new_state
            self._last_active = time.time()
            logger.debug(
                "State transition: agent=%s from=%s to=%s",
                self.agent_id,
                old_state.value,
                new_state.value,
            )
            return True

    # ── State Machine ───────────────────────────────────────

    def xǁBaseAgentǁtransition_to__mutmut_7(self, new_state: AgentState) -> bool:
        """Attempt a state transition. Returns True if successful."""
        with self._state_lock:
            old_state = self._state
            if new_state not in VALID_TRANSITIONS.get(old_state, set()):
                logger.warning(
                    None,
                    self.agent_id,
                    old_state.value,
                    new_state.value,
                )
                return False
            self._state = new_state
            self._last_active = time.time()
            logger.debug(
                "State transition: agent=%s from=%s to=%s",
                self.agent_id,
                old_state.value,
                new_state.value,
            )
            return True

    # ── State Machine ───────────────────────────────────────

    def xǁBaseAgentǁtransition_to__mutmut_8(self, new_state: AgentState) -> bool:
        """Attempt a state transition. Returns True if successful."""
        with self._state_lock:
            old_state = self._state
            if new_state not in VALID_TRANSITIONS.get(old_state, set()):
                logger.warning(
                    "Invalid state transition: agent=%s from=%s to=%s",
                    None,
                    old_state.value,
                    new_state.value,
                )
                return False
            self._state = new_state
            self._last_active = time.time()
            logger.debug(
                "State transition: agent=%s from=%s to=%s",
                self.agent_id,
                old_state.value,
                new_state.value,
            )
            return True

    # ── State Machine ───────────────────────────────────────

    def xǁBaseAgentǁtransition_to__mutmut_9(self, new_state: AgentState) -> bool:
        """Attempt a state transition. Returns True if successful."""
        with self._state_lock:
            old_state = self._state
            if new_state not in VALID_TRANSITIONS.get(old_state, set()):
                logger.warning(
                    "Invalid state transition: agent=%s from=%s to=%s",
                    self.agent_id,
                    None,
                    new_state.value,
                )
                return False
            self._state = new_state
            self._last_active = time.time()
            logger.debug(
                "State transition: agent=%s from=%s to=%s",
                self.agent_id,
                old_state.value,
                new_state.value,
            )
            return True

    # ── State Machine ───────────────────────────────────────

    def xǁBaseAgentǁtransition_to__mutmut_10(self, new_state: AgentState) -> bool:
        """Attempt a state transition. Returns True if successful."""
        with self._state_lock:
            old_state = self._state
            if new_state not in VALID_TRANSITIONS.get(old_state, set()):
                logger.warning(
                    "Invalid state transition: agent=%s from=%s to=%s",
                    self.agent_id,
                    old_state.value,
                    None,
                )
                return False
            self._state = new_state
            self._last_active = time.time()
            logger.debug(
                "State transition: agent=%s from=%s to=%s",
                self.agent_id,
                old_state.value,
                new_state.value,
            )
            return True

    # ── State Machine ───────────────────────────────────────

    def xǁBaseAgentǁtransition_to__mutmut_11(self, new_state: AgentState) -> bool:
        """Attempt a state transition. Returns True if successful."""
        with self._state_lock:
            old_state = self._state
            if new_state not in VALID_TRANSITIONS.get(old_state, set()):
                logger.warning(
                    self.agent_id,
                    old_state.value,
                    new_state.value,
                )
                return False
            self._state = new_state
            self._last_active = time.time()
            logger.debug(
                "State transition: agent=%s from=%s to=%s",
                self.agent_id,
                old_state.value,
                new_state.value,
            )
            return True

    # ── State Machine ───────────────────────────────────────

    def xǁBaseAgentǁtransition_to__mutmut_12(self, new_state: AgentState) -> bool:
        """Attempt a state transition. Returns True if successful."""
        with self._state_lock:
            old_state = self._state
            if new_state not in VALID_TRANSITIONS.get(old_state, set()):
                logger.warning(
                    "Invalid state transition: agent=%s from=%s to=%s",
                    old_state.value,
                    new_state.value,
                )
                return False
            self._state = new_state
            self._last_active = time.time()
            logger.debug(
                "State transition: agent=%s from=%s to=%s",
                self.agent_id,
                old_state.value,
                new_state.value,
            )
            return True

    # ── State Machine ───────────────────────────────────────

    def xǁBaseAgentǁtransition_to__mutmut_13(self, new_state: AgentState) -> bool:
        """Attempt a state transition. Returns True if successful."""
        with self._state_lock:
            old_state = self._state
            if new_state not in VALID_TRANSITIONS.get(old_state, set()):
                logger.warning(
                    "Invalid state transition: agent=%s from=%s to=%s",
                    self.agent_id,
                    new_state.value,
                )
                return False
            self._state = new_state
            self._last_active = time.time()
            logger.debug(
                "State transition: agent=%s from=%s to=%s",
                self.agent_id,
                old_state.value,
                new_state.value,
            )
            return True

    # ── State Machine ───────────────────────────────────────

    def xǁBaseAgentǁtransition_to__mutmut_14(self, new_state: AgentState) -> bool:
        """Attempt a state transition. Returns True if successful."""
        with self._state_lock:
            old_state = self._state
            if new_state not in VALID_TRANSITIONS.get(old_state, set()):
                logger.warning(
                    "Invalid state transition: agent=%s from=%s to=%s",
                    self.agent_id,
                    old_state.value,
                    )
                return False
            self._state = new_state
            self._last_active = time.time()
            logger.debug(
                "State transition: agent=%s from=%s to=%s",
                self.agent_id,
                old_state.value,
                new_state.value,
            )
            return True

    # ── State Machine ───────────────────────────────────────

    def xǁBaseAgentǁtransition_to__mutmut_15(self, new_state: AgentState) -> bool:
        """Attempt a state transition. Returns True if successful."""
        with self._state_lock:
            old_state = self._state
            if new_state not in VALID_TRANSITIONS.get(old_state, set()):
                logger.warning(
                    "XXInvalid state transition: agent=%s from=%s to=%sXX",
                    self.agent_id,
                    old_state.value,
                    new_state.value,
                )
                return False
            self._state = new_state
            self._last_active = time.time()
            logger.debug(
                "State transition: agent=%s from=%s to=%s",
                self.agent_id,
                old_state.value,
                new_state.value,
            )
            return True

    # ── State Machine ───────────────────────────────────────

    def xǁBaseAgentǁtransition_to__mutmut_16(self, new_state: AgentState) -> bool:
        """Attempt a state transition. Returns True if successful."""
        with self._state_lock:
            old_state = self._state
            if new_state not in VALID_TRANSITIONS.get(old_state, set()):
                logger.warning(
                    "invalid state transition: agent=%s from=%s to=%s",
                    self.agent_id,
                    old_state.value,
                    new_state.value,
                )
                return False
            self._state = new_state
            self._last_active = time.time()
            logger.debug(
                "State transition: agent=%s from=%s to=%s",
                self.agent_id,
                old_state.value,
                new_state.value,
            )
            return True

    # ── State Machine ───────────────────────────────────────

    def xǁBaseAgentǁtransition_to__mutmut_17(self, new_state: AgentState) -> bool:
        """Attempt a state transition. Returns True if successful."""
        with self._state_lock:
            old_state = self._state
            if new_state not in VALID_TRANSITIONS.get(old_state, set()):
                logger.warning(
                    "INVALID STATE TRANSITION: AGENT=%S FROM=%S TO=%S",
                    self.agent_id,
                    old_state.value,
                    new_state.value,
                )
                return False
            self._state = new_state
            self._last_active = time.time()
            logger.debug(
                "State transition: agent=%s from=%s to=%s",
                self.agent_id,
                old_state.value,
                new_state.value,
            )
            return True

    # ── State Machine ───────────────────────────────────────

    def xǁBaseAgentǁtransition_to__mutmut_18(self, new_state: AgentState) -> bool:
        """Attempt a state transition. Returns True if successful."""
        with self._state_lock:
            old_state = self._state
            if new_state not in VALID_TRANSITIONS.get(old_state, set()):
                logger.warning(
                    "Invalid state transition: agent=%s from=%s to=%s",
                    self.agent_id,
                    old_state.value,
                    new_state.value,
                )
                return True
            self._state = new_state
            self._last_active = time.time()
            logger.debug(
                "State transition: agent=%s from=%s to=%s",
                self.agent_id,
                old_state.value,
                new_state.value,
            )
            return True

    # ── State Machine ───────────────────────────────────────

    def xǁBaseAgentǁtransition_to__mutmut_19(self, new_state: AgentState) -> bool:
        """Attempt a state transition. Returns True if successful."""
        with self._state_lock:
            old_state = self._state
            if new_state not in VALID_TRANSITIONS.get(old_state, set()):
                logger.warning(
                    "Invalid state transition: agent=%s from=%s to=%s",
                    self.agent_id,
                    old_state.value,
                    new_state.value,
                )
                return False
            self._state = None
            self._last_active = time.time()
            logger.debug(
                "State transition: agent=%s from=%s to=%s",
                self.agent_id,
                old_state.value,
                new_state.value,
            )
            return True

    # ── State Machine ───────────────────────────────────────

    def xǁBaseAgentǁtransition_to__mutmut_20(self, new_state: AgentState) -> bool:
        """Attempt a state transition. Returns True if successful."""
        with self._state_lock:
            old_state = self._state
            if new_state not in VALID_TRANSITIONS.get(old_state, set()):
                logger.warning(
                    "Invalid state transition: agent=%s from=%s to=%s",
                    self.agent_id,
                    old_state.value,
                    new_state.value,
                )
                return False
            self._state = new_state
            self._last_active = None
            logger.debug(
                "State transition: agent=%s from=%s to=%s",
                self.agent_id,
                old_state.value,
                new_state.value,
            )
            return True

    # ── State Machine ───────────────────────────────────────

    def xǁBaseAgentǁtransition_to__mutmut_21(self, new_state: AgentState) -> bool:
        """Attempt a state transition. Returns True if successful."""
        with self._state_lock:
            old_state = self._state
            if new_state not in VALID_TRANSITIONS.get(old_state, set()):
                logger.warning(
                    "Invalid state transition: agent=%s from=%s to=%s",
                    self.agent_id,
                    old_state.value,
                    new_state.value,
                )
                return False
            self._state = new_state
            self._last_active = time.time()
            logger.debug(
                None,
                self.agent_id,
                old_state.value,
                new_state.value,
            )
            return True

    # ── State Machine ───────────────────────────────────────

    def xǁBaseAgentǁtransition_to__mutmut_22(self, new_state: AgentState) -> bool:
        """Attempt a state transition. Returns True if successful."""
        with self._state_lock:
            old_state = self._state
            if new_state not in VALID_TRANSITIONS.get(old_state, set()):
                logger.warning(
                    "Invalid state transition: agent=%s from=%s to=%s",
                    self.agent_id,
                    old_state.value,
                    new_state.value,
                )
                return False
            self._state = new_state
            self._last_active = time.time()
            logger.debug(
                "State transition: agent=%s from=%s to=%s",
                None,
                old_state.value,
                new_state.value,
            )
            return True

    # ── State Machine ───────────────────────────────────────

    def xǁBaseAgentǁtransition_to__mutmut_23(self, new_state: AgentState) -> bool:
        """Attempt a state transition. Returns True if successful."""
        with self._state_lock:
            old_state = self._state
            if new_state not in VALID_TRANSITIONS.get(old_state, set()):
                logger.warning(
                    "Invalid state transition: agent=%s from=%s to=%s",
                    self.agent_id,
                    old_state.value,
                    new_state.value,
                )
                return False
            self._state = new_state
            self._last_active = time.time()
            logger.debug(
                "State transition: agent=%s from=%s to=%s",
                self.agent_id,
                None,
                new_state.value,
            )
            return True

    # ── State Machine ───────────────────────────────────────

    def xǁBaseAgentǁtransition_to__mutmut_24(self, new_state: AgentState) -> bool:
        """Attempt a state transition. Returns True if successful."""
        with self._state_lock:
            old_state = self._state
            if new_state not in VALID_TRANSITIONS.get(old_state, set()):
                logger.warning(
                    "Invalid state transition: agent=%s from=%s to=%s",
                    self.agent_id,
                    old_state.value,
                    new_state.value,
                )
                return False
            self._state = new_state
            self._last_active = time.time()
            logger.debug(
                "State transition: agent=%s from=%s to=%s",
                self.agent_id,
                old_state.value,
                None,
            )
            return True

    # ── State Machine ───────────────────────────────────────

    def xǁBaseAgentǁtransition_to__mutmut_25(self, new_state: AgentState) -> bool:
        """Attempt a state transition. Returns True if successful."""
        with self._state_lock:
            old_state = self._state
            if new_state not in VALID_TRANSITIONS.get(old_state, set()):
                logger.warning(
                    "Invalid state transition: agent=%s from=%s to=%s",
                    self.agent_id,
                    old_state.value,
                    new_state.value,
                )
                return False
            self._state = new_state
            self._last_active = time.time()
            logger.debug(
                self.agent_id,
                old_state.value,
                new_state.value,
            )
            return True

    # ── State Machine ───────────────────────────────────────

    def xǁBaseAgentǁtransition_to__mutmut_26(self, new_state: AgentState) -> bool:
        """Attempt a state transition. Returns True if successful."""
        with self._state_lock:
            old_state = self._state
            if new_state not in VALID_TRANSITIONS.get(old_state, set()):
                logger.warning(
                    "Invalid state transition: agent=%s from=%s to=%s",
                    self.agent_id,
                    old_state.value,
                    new_state.value,
                )
                return False
            self._state = new_state
            self._last_active = time.time()
            logger.debug(
                "State transition: agent=%s from=%s to=%s",
                old_state.value,
                new_state.value,
            )
            return True

    # ── State Machine ───────────────────────────────────────

    def xǁBaseAgentǁtransition_to__mutmut_27(self, new_state: AgentState) -> bool:
        """Attempt a state transition. Returns True if successful."""
        with self._state_lock:
            old_state = self._state
            if new_state not in VALID_TRANSITIONS.get(old_state, set()):
                logger.warning(
                    "Invalid state transition: agent=%s from=%s to=%s",
                    self.agent_id,
                    old_state.value,
                    new_state.value,
                )
                return False
            self._state = new_state
            self._last_active = time.time()
            logger.debug(
                "State transition: agent=%s from=%s to=%s",
                self.agent_id,
                new_state.value,
            )
            return True

    # ── State Machine ───────────────────────────────────────

    def xǁBaseAgentǁtransition_to__mutmut_28(self, new_state: AgentState) -> bool:
        """Attempt a state transition. Returns True if successful."""
        with self._state_lock:
            old_state = self._state
            if new_state not in VALID_TRANSITIONS.get(old_state, set()):
                logger.warning(
                    "Invalid state transition: agent=%s from=%s to=%s",
                    self.agent_id,
                    old_state.value,
                    new_state.value,
                )
                return False
            self._state = new_state
            self._last_active = time.time()
            logger.debug(
                "State transition: agent=%s from=%s to=%s",
                self.agent_id,
                old_state.value,
                )
            return True

    # ── State Machine ───────────────────────────────────────

    def xǁBaseAgentǁtransition_to__mutmut_29(self, new_state: AgentState) -> bool:
        """Attempt a state transition. Returns True if successful."""
        with self._state_lock:
            old_state = self._state
            if new_state not in VALID_TRANSITIONS.get(old_state, set()):
                logger.warning(
                    "Invalid state transition: agent=%s from=%s to=%s",
                    self.agent_id,
                    old_state.value,
                    new_state.value,
                )
                return False
            self._state = new_state
            self._last_active = time.time()
            logger.debug(
                "XXState transition: agent=%s from=%s to=%sXX",
                self.agent_id,
                old_state.value,
                new_state.value,
            )
            return True

    # ── State Machine ───────────────────────────────────────

    def xǁBaseAgentǁtransition_to__mutmut_30(self, new_state: AgentState) -> bool:
        """Attempt a state transition. Returns True if successful."""
        with self._state_lock:
            old_state = self._state
            if new_state not in VALID_TRANSITIONS.get(old_state, set()):
                logger.warning(
                    "Invalid state transition: agent=%s from=%s to=%s",
                    self.agent_id,
                    old_state.value,
                    new_state.value,
                )
                return False
            self._state = new_state
            self._last_active = time.time()
            logger.debug(
                "state transition: agent=%s from=%s to=%s",
                self.agent_id,
                old_state.value,
                new_state.value,
            )
            return True

    # ── State Machine ───────────────────────────────────────

    def xǁBaseAgentǁtransition_to__mutmut_31(self, new_state: AgentState) -> bool:
        """Attempt a state transition. Returns True if successful."""
        with self._state_lock:
            old_state = self._state
            if new_state not in VALID_TRANSITIONS.get(old_state, set()):
                logger.warning(
                    "Invalid state transition: agent=%s from=%s to=%s",
                    self.agent_id,
                    old_state.value,
                    new_state.value,
                )
                return False
            self._state = new_state
            self._last_active = time.time()
            logger.debug(
                "STATE TRANSITION: AGENT=%S FROM=%S TO=%S",
                self.agent_id,
                old_state.value,
                new_state.value,
            )
            return True

    # ── State Machine ───────────────────────────────────────

    def xǁBaseAgentǁtransition_to__mutmut_32(self, new_state: AgentState) -> bool:
        """Attempt a state transition. Returns True if successful."""
        with self._state_lock:
            old_state = self._state
            if new_state not in VALID_TRANSITIONS.get(old_state, set()):
                logger.warning(
                    "Invalid state transition: agent=%s from=%s to=%s",
                    self.agent_id,
                    old_state.value,
                    new_state.value,
                )
                return False
            self._state = new_state
            self._last_active = time.time()
            logger.debug(
                "State transition: agent=%s from=%s to=%s",
                self.agent_id,
                old_state.value,
                new_state.value,
            )
            return False

    @_mutmut_mutated(mutants_xǁBaseAgentǁforce_state__mutmut)
    def force_state(self, new_state: AgentState) -> None:
        """Force a state transition regardless of rules (admin only)."""
        with self._state_lock:
            old_state = self._state
            self._state = new_state
            self._last_active = time.time()
            logger.warning(
                "Forced state transition: agent=%s from=%s to=%s",
                self.agent_id,
                old_state.value,
                new_state.value,
            )

    def xǁBaseAgentǁforce_state__mutmut_orig(self, new_state: AgentState) -> None:
        """Force a state transition regardless of rules (admin only)."""
        with self._state_lock:
            old_state = self._state
            self._state = new_state
            self._last_active = time.time()
            logger.warning(
                "Forced state transition: agent=%s from=%s to=%s",
                self.agent_id,
                old_state.value,
                new_state.value,
            )

    def xǁBaseAgentǁforce_state__mutmut_1(self, new_state: AgentState) -> None:
        """Force a state transition regardless of rules (admin only)."""
        with self._state_lock:
            old_state = None
            self._state = new_state
            self._last_active = time.time()
            logger.warning(
                "Forced state transition: agent=%s from=%s to=%s",
                self.agent_id,
                old_state.value,
                new_state.value,
            )

    def xǁBaseAgentǁforce_state__mutmut_2(self, new_state: AgentState) -> None:
        """Force a state transition regardless of rules (admin only)."""
        with self._state_lock:
            old_state = self._state
            self._state = None
            self._last_active = time.time()
            logger.warning(
                "Forced state transition: agent=%s from=%s to=%s",
                self.agent_id,
                old_state.value,
                new_state.value,
            )

    def xǁBaseAgentǁforce_state__mutmut_3(self, new_state: AgentState) -> None:
        """Force a state transition regardless of rules (admin only)."""
        with self._state_lock:
            old_state = self._state
            self._state = new_state
            self._last_active = None
            logger.warning(
                "Forced state transition: agent=%s from=%s to=%s",
                self.agent_id,
                old_state.value,
                new_state.value,
            )

    def xǁBaseAgentǁforce_state__mutmut_4(self, new_state: AgentState) -> None:
        """Force a state transition regardless of rules (admin only)."""
        with self._state_lock:
            old_state = self._state
            self._state = new_state
            self._last_active = time.time()
            logger.warning(
                None,
                self.agent_id,
                old_state.value,
                new_state.value,
            )

    def xǁBaseAgentǁforce_state__mutmut_5(self, new_state: AgentState) -> None:
        """Force a state transition regardless of rules (admin only)."""
        with self._state_lock:
            old_state = self._state
            self._state = new_state
            self._last_active = time.time()
            logger.warning(
                "Forced state transition: agent=%s from=%s to=%s",
                None,
                old_state.value,
                new_state.value,
            )

    def xǁBaseAgentǁforce_state__mutmut_6(self, new_state: AgentState) -> None:
        """Force a state transition regardless of rules (admin only)."""
        with self._state_lock:
            old_state = self._state
            self._state = new_state
            self._last_active = time.time()
            logger.warning(
                "Forced state transition: agent=%s from=%s to=%s",
                self.agent_id,
                None,
                new_state.value,
            )

    def xǁBaseAgentǁforce_state__mutmut_7(self, new_state: AgentState) -> None:
        """Force a state transition regardless of rules (admin only)."""
        with self._state_lock:
            old_state = self._state
            self._state = new_state
            self._last_active = time.time()
            logger.warning(
                "Forced state transition: agent=%s from=%s to=%s",
                self.agent_id,
                old_state.value,
                None,
            )

    def xǁBaseAgentǁforce_state__mutmut_8(self, new_state: AgentState) -> None:
        """Force a state transition regardless of rules (admin only)."""
        with self._state_lock:
            old_state = self._state
            self._state = new_state
            self._last_active = time.time()
            logger.warning(
                self.agent_id,
                old_state.value,
                new_state.value,
            )

    def xǁBaseAgentǁforce_state__mutmut_9(self, new_state: AgentState) -> None:
        """Force a state transition regardless of rules (admin only)."""
        with self._state_lock:
            old_state = self._state
            self._state = new_state
            self._last_active = time.time()
            logger.warning(
                "Forced state transition: agent=%s from=%s to=%s",
                old_state.value,
                new_state.value,
            )

    def xǁBaseAgentǁforce_state__mutmut_10(self, new_state: AgentState) -> None:
        """Force a state transition regardless of rules (admin only)."""
        with self._state_lock:
            old_state = self._state
            self._state = new_state
            self._last_active = time.time()
            logger.warning(
                "Forced state transition: agent=%s from=%s to=%s",
                self.agent_id,
                new_state.value,
            )

    def xǁBaseAgentǁforce_state__mutmut_11(self, new_state: AgentState) -> None:
        """Force a state transition regardless of rules (admin only)."""
        with self._state_lock:
            old_state = self._state
            self._state = new_state
            self._last_active = time.time()
            logger.warning(
                "Forced state transition: agent=%s from=%s to=%s",
                self.agent_id,
                old_state.value,
                )

    def xǁBaseAgentǁforce_state__mutmut_12(self, new_state: AgentState) -> None:
        """Force a state transition regardless of rules (admin only)."""
        with self._state_lock:
            old_state = self._state
            self._state = new_state
            self._last_active = time.time()
            logger.warning(
                "XXForced state transition: agent=%s from=%s to=%sXX",
                self.agent_id,
                old_state.value,
                new_state.value,
            )

    def xǁBaseAgentǁforce_state__mutmut_13(self, new_state: AgentState) -> None:
        """Force a state transition regardless of rules (admin only)."""
        with self._state_lock:
            old_state = self._state
            self._state = new_state
            self._last_active = time.time()
            logger.warning(
                "forced state transition: agent=%s from=%s to=%s",
                self.agent_id,
                old_state.value,
                new_state.value,
            )

    def xǁBaseAgentǁforce_state__mutmut_14(self, new_state: AgentState) -> None:
        """Force a state transition regardless of rules (admin only)."""
        with self._state_lock:
            old_state = self._state
            self._state = new_state
            self._last_active = time.time()
            logger.warning(
                "FORCED STATE TRANSITION: AGENT=%S FROM=%S TO=%S",
                self.agent_id,
                old_state.value,
                new_state.value,
            )

    # ── Lifecycle ───────────────────────────────────────────

    @_mutmut_mutated(mutants_xǁBaseAgentǁrun__mutmut)
    def run(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_orig(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_1(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(None)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_2(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = ""

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_3(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            None,
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_4(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            None,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_5(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            None,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_6(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_7(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_8(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_9(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "XXAgent run started: id=%s max_iterations=%dXX",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_10(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_11(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "AGENT RUN STARTED: ID=%S MAX_ITERATIONS=%D",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_12(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(None):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_13(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = None
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_14(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration - 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_15(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 2
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_16(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = None

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_17(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(None)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_18(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = None

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_19(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(None)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_20(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration != 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_21(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 1 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_22(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is not None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_23(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        None,
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_24(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        None,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_25(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        None,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_26(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_27(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_28(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_29(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "XXAgent run finished: id=%s iterations=%d decision=NoneXX",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_30(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "agent run finished: id=%s iterations=%d decision=none",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_31(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "AGENT RUN FINISHED: ID=%S ITERATIONS=%D DECISION=NONE",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_32(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration - 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_33(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 2,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_34(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(None)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_35(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    return

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_36(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(None)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_37(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = None

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_38(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(None)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_39(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = None

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_40(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() + iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_41(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append(None)

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_42(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "XXiterationXX": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_43(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "ITERATION": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_44(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration - 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_45(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 2,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_46(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "XXdecisionXX": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_47(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "DECISION": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_48(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "XXresultXX": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_49(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "RESULT": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_50(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "XXtimestampXX": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_51(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "TIMESTAMP": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_52(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    None,
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_53(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    None,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_54(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    None,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_55(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    None,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_56(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_57(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_58(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_59(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_60(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "XXAgent iteration completed: id=%s iteration=%d duration=%.3fsXX",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_61(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_62(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "AGENT ITERATION COMPLETED: ID=%S ITERATION=%D DURATION=%.3FS",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_63(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration - 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_64(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 2,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_65(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(None):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_66(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        None,
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_67(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        None,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_68(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        None,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_69(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_70(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_71(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_72(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "XXAgent run finished: id=%s iterations=%d stop signal receivedXX",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_73(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_74(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "AGENT RUN FINISHED: ID=%S ITERATIONS=%D STOP SIGNAL RECEIVED",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_75(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration - 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_76(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 2,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_77(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(None)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_78(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    return

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_79(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count = 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_80(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count -= 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_81(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 2
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_82(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append(None)
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_83(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "XXiterationXX": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_84(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "ITERATION": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_85(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration - 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_86(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 2,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_87(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "XXerrorXX": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_88(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "ERROR": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_89(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(None),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_90(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "XXtimestampXX": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_91(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "TIMESTAMP": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_92(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    None,
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_93(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    None,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_94(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    None,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_95(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    None,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_96(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_97(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_98(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_99(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_100(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "XXAgent run error: id=%s iteration=%d error=%sXX",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_101(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_102(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "AGENT RUN ERROR: ID=%S ITERATION=%D ERROR=%S",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_103(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration - 1,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_104(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 2,
                    exc,
                )
                self.transition_to(AgentState.ERROR)
                raise

        return result

    # ── Lifecycle ───────────────────────────────────────────

    def xǁBaseAgentǁrun__mutmut_105(self, input_data: Any = None) -> Any:
        """Execute the agent's think-act loop until completion or max iterations."""
        self.transition_to(AgentState.THINKING)
        result = None

        logger.info(
            "Agent run started: id=%s max_iterations=%d",
            self.agent_id,
            self.config.max_iterations,
        )

        for iteration in range(self.config.max_iterations):
            self._iteration_count = iteration + 1
            iter_start = time.time()

            try:
                # Think phase
                self.transition_to(AgentState.THINKING)
                decision = self.think(input_data if iteration == 0 else result)

                if decision is None:
                    logger.info(
                        "Agent run finished: id=%s iterations=%d decision=None",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

                # Act phase
                self.transition_to(AgentState.EXECUTING)
                result = self.act(decision)

                iter_duration = time.time() - iter_start

                # Record execution
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "decision": decision,
                    "result": result,
                    "timestamp": time.time(),
                })

                logger.debug(
                    "Agent iteration completed: id=%s iteration=%d duration=%.3fs",
                    self.agent_id,
                    iteration + 1,
                    iter_duration,
                )

                # Check if agent should stop
                if self._should_stop(result):
                    logger.info(
                        "Agent run finished: id=%s iterations=%d stop signal received",
                        self.agent_id,
                        iteration + 1,
                    )
                    self.transition_to(AgentState.IDLE)
                    break

            except Exception as exc:
                self._error_count += 1
                self._execution_history.append({
                    "iteration": iteration + 1,
                    "error": str(exc),
                    "timestamp": time.time(),
                })
                logger.error(
                    "Agent run error: id=%s iteration=%d error=%s",
                    self.agent_id,
                    iteration + 1,
                    exc,
                )
                self.transition_to(None)
                raise

        return result

    @_mutmut_mutated(mutants_xǁBaseAgentǁpause__mutmut)
    def pause(self) -> bool:
        """Pause the agent execution."""
        result = self.transition_to(AgentState.PAUSED)
        if result:
            logger.info("Agent paused: id=%s", self.agent_id)
        return result

    def xǁBaseAgentǁpause__mutmut_orig(self) -> bool:
        """Pause the agent execution."""
        result = self.transition_to(AgentState.PAUSED)
        if result:
            logger.info("Agent paused: id=%s", self.agent_id)
        return result

    def xǁBaseAgentǁpause__mutmut_1(self) -> bool:
        """Pause the agent execution."""
        result = None
        if result:
            logger.info("Agent paused: id=%s", self.agent_id)
        return result

    def xǁBaseAgentǁpause__mutmut_2(self) -> bool:
        """Pause the agent execution."""
        result = self.transition_to(None)
        if result:
            logger.info("Agent paused: id=%s", self.agent_id)
        return result

    def xǁBaseAgentǁpause__mutmut_3(self) -> bool:
        """Pause the agent execution."""
        result = self.transition_to(AgentState.PAUSED)
        if result:
            logger.info(None, self.agent_id)
        return result

    def xǁBaseAgentǁpause__mutmut_4(self) -> bool:
        """Pause the agent execution."""
        result = self.transition_to(AgentState.PAUSED)
        if result:
            logger.info("Agent paused: id=%s", None)
        return result

    def xǁBaseAgentǁpause__mutmut_5(self) -> bool:
        """Pause the agent execution."""
        result = self.transition_to(AgentState.PAUSED)
        if result:
            logger.info(self.agent_id)
        return result

    def xǁBaseAgentǁpause__mutmut_6(self) -> bool:
        """Pause the agent execution."""
        result = self.transition_to(AgentState.PAUSED)
        if result:
            logger.info("Agent paused: id=%s", )
        return result

    def xǁBaseAgentǁpause__mutmut_7(self) -> bool:
        """Pause the agent execution."""
        result = self.transition_to(AgentState.PAUSED)
        if result:
            logger.info("XXAgent paused: id=%sXX", self.agent_id)
        return result

    def xǁBaseAgentǁpause__mutmut_8(self) -> bool:
        """Pause the agent execution."""
        result = self.transition_to(AgentState.PAUSED)
        if result:
            logger.info("agent paused: id=%s", self.agent_id)
        return result

    def xǁBaseAgentǁpause__mutmut_9(self) -> bool:
        """Pause the agent execution."""
        result = self.transition_to(AgentState.PAUSED)
        if result:
            logger.info("AGENT PAUSED: ID=%S", self.agent_id)
        return result

    @_mutmut_mutated(mutants_xǁBaseAgentǁresume__mutmut)
    def resume(self) -> bool:
        """Resume a paused agent."""
        if self.state == AgentState.PAUSED:
            result = self.transition_to(AgentState.THINKING)
            if result:
                logger.info("Agent resumed: id=%s", self.agent_id)
            return result
        logger.warning(
            "Cannot resume agent not in PAUSED state: id=%s state=%s",
            self.agent_id,
            self.state.value,
        )
        return False

    def xǁBaseAgentǁresume__mutmut_orig(self) -> bool:
        """Resume a paused agent."""
        if self.state == AgentState.PAUSED:
            result = self.transition_to(AgentState.THINKING)
            if result:
                logger.info("Agent resumed: id=%s", self.agent_id)
            return result
        logger.warning(
            "Cannot resume agent not in PAUSED state: id=%s state=%s",
            self.agent_id,
            self.state.value,
        )
        return False

    def xǁBaseAgentǁresume__mutmut_1(self) -> bool:
        """Resume a paused agent."""
        if self.state != AgentState.PAUSED:
            result = self.transition_to(AgentState.THINKING)
            if result:
                logger.info("Agent resumed: id=%s", self.agent_id)
            return result
        logger.warning(
            "Cannot resume agent not in PAUSED state: id=%s state=%s",
            self.agent_id,
            self.state.value,
        )
        return False

    def xǁBaseAgentǁresume__mutmut_2(self) -> bool:
        """Resume a paused agent."""
        if self.state == AgentState.PAUSED:
            result = None
            if result:
                logger.info("Agent resumed: id=%s", self.agent_id)
            return result
        logger.warning(
            "Cannot resume agent not in PAUSED state: id=%s state=%s",
            self.agent_id,
            self.state.value,
        )
        return False

    def xǁBaseAgentǁresume__mutmut_3(self) -> bool:
        """Resume a paused agent."""
        if self.state == AgentState.PAUSED:
            result = self.transition_to(None)
            if result:
                logger.info("Agent resumed: id=%s", self.agent_id)
            return result
        logger.warning(
            "Cannot resume agent not in PAUSED state: id=%s state=%s",
            self.agent_id,
            self.state.value,
        )
        return False

    def xǁBaseAgentǁresume__mutmut_4(self) -> bool:
        """Resume a paused agent."""
        if self.state == AgentState.PAUSED:
            result = self.transition_to(AgentState.THINKING)
            if result:
                logger.info(None, self.agent_id)
            return result
        logger.warning(
            "Cannot resume agent not in PAUSED state: id=%s state=%s",
            self.agent_id,
            self.state.value,
        )
        return False

    def xǁBaseAgentǁresume__mutmut_5(self) -> bool:
        """Resume a paused agent."""
        if self.state == AgentState.PAUSED:
            result = self.transition_to(AgentState.THINKING)
            if result:
                logger.info("Agent resumed: id=%s", None)
            return result
        logger.warning(
            "Cannot resume agent not in PAUSED state: id=%s state=%s",
            self.agent_id,
            self.state.value,
        )
        return False

    def xǁBaseAgentǁresume__mutmut_6(self) -> bool:
        """Resume a paused agent."""
        if self.state == AgentState.PAUSED:
            result = self.transition_to(AgentState.THINKING)
            if result:
                logger.info(self.agent_id)
            return result
        logger.warning(
            "Cannot resume agent not in PAUSED state: id=%s state=%s",
            self.agent_id,
            self.state.value,
        )
        return False

    def xǁBaseAgentǁresume__mutmut_7(self) -> bool:
        """Resume a paused agent."""
        if self.state == AgentState.PAUSED:
            result = self.transition_to(AgentState.THINKING)
            if result:
                logger.info("Agent resumed: id=%s", )
            return result
        logger.warning(
            "Cannot resume agent not in PAUSED state: id=%s state=%s",
            self.agent_id,
            self.state.value,
        )
        return False

    def xǁBaseAgentǁresume__mutmut_8(self) -> bool:
        """Resume a paused agent."""
        if self.state == AgentState.PAUSED:
            result = self.transition_to(AgentState.THINKING)
            if result:
                logger.info("XXAgent resumed: id=%sXX", self.agent_id)
            return result
        logger.warning(
            "Cannot resume agent not in PAUSED state: id=%s state=%s",
            self.agent_id,
            self.state.value,
        )
        return False

    def xǁBaseAgentǁresume__mutmut_9(self) -> bool:
        """Resume a paused agent."""
        if self.state == AgentState.PAUSED:
            result = self.transition_to(AgentState.THINKING)
            if result:
                logger.info("agent resumed: id=%s", self.agent_id)
            return result
        logger.warning(
            "Cannot resume agent not in PAUSED state: id=%s state=%s",
            self.agent_id,
            self.state.value,
        )
        return False

    def xǁBaseAgentǁresume__mutmut_10(self) -> bool:
        """Resume a paused agent."""
        if self.state == AgentState.PAUSED:
            result = self.transition_to(AgentState.THINKING)
            if result:
                logger.info("AGENT RESUMED: ID=%S", self.agent_id)
            return result
        logger.warning(
            "Cannot resume agent not in PAUSED state: id=%s state=%s",
            self.agent_id,
            self.state.value,
        )
        return False

    def xǁBaseAgentǁresume__mutmut_11(self) -> bool:
        """Resume a paused agent."""
        if self.state == AgentState.PAUSED:
            result = self.transition_to(AgentState.THINKING)
            if result:
                logger.info("Agent resumed: id=%s", self.agent_id)
            return result
        logger.warning(
            None,
            self.agent_id,
            self.state.value,
        )
        return False

    def xǁBaseAgentǁresume__mutmut_12(self) -> bool:
        """Resume a paused agent."""
        if self.state == AgentState.PAUSED:
            result = self.transition_to(AgentState.THINKING)
            if result:
                logger.info("Agent resumed: id=%s", self.agent_id)
            return result
        logger.warning(
            "Cannot resume agent not in PAUSED state: id=%s state=%s",
            None,
            self.state.value,
        )
        return False

    def xǁBaseAgentǁresume__mutmut_13(self) -> bool:
        """Resume a paused agent."""
        if self.state == AgentState.PAUSED:
            result = self.transition_to(AgentState.THINKING)
            if result:
                logger.info("Agent resumed: id=%s", self.agent_id)
            return result
        logger.warning(
            "Cannot resume agent not in PAUSED state: id=%s state=%s",
            self.agent_id,
            None,
        )
        return False

    def xǁBaseAgentǁresume__mutmut_14(self) -> bool:
        """Resume a paused agent."""
        if self.state == AgentState.PAUSED:
            result = self.transition_to(AgentState.THINKING)
            if result:
                logger.info("Agent resumed: id=%s", self.agent_id)
            return result
        logger.warning(
            self.agent_id,
            self.state.value,
        )
        return False

    def xǁBaseAgentǁresume__mutmut_15(self) -> bool:
        """Resume a paused agent."""
        if self.state == AgentState.PAUSED:
            result = self.transition_to(AgentState.THINKING)
            if result:
                logger.info("Agent resumed: id=%s", self.agent_id)
            return result
        logger.warning(
            "Cannot resume agent not in PAUSED state: id=%s state=%s",
            self.state.value,
        )
        return False

    def xǁBaseAgentǁresume__mutmut_16(self) -> bool:
        """Resume a paused agent."""
        if self.state == AgentState.PAUSED:
            result = self.transition_to(AgentState.THINKING)
            if result:
                logger.info("Agent resumed: id=%s", self.agent_id)
            return result
        logger.warning(
            "Cannot resume agent not in PAUSED state: id=%s state=%s",
            self.agent_id,
            )
        return False

    def xǁBaseAgentǁresume__mutmut_17(self) -> bool:
        """Resume a paused agent."""
        if self.state == AgentState.PAUSED:
            result = self.transition_to(AgentState.THINKING)
            if result:
                logger.info("Agent resumed: id=%s", self.agent_id)
            return result
        logger.warning(
            "XXCannot resume agent not in PAUSED state: id=%s state=%sXX",
            self.agent_id,
            self.state.value,
        )
        return False

    def xǁBaseAgentǁresume__mutmut_18(self) -> bool:
        """Resume a paused agent."""
        if self.state == AgentState.PAUSED:
            result = self.transition_to(AgentState.THINKING)
            if result:
                logger.info("Agent resumed: id=%s", self.agent_id)
            return result
        logger.warning(
            "cannot resume agent not in paused state: id=%s state=%s",
            self.agent_id,
            self.state.value,
        )
        return False

    def xǁBaseAgentǁresume__mutmut_19(self) -> bool:
        """Resume a paused agent."""
        if self.state == AgentState.PAUSED:
            result = self.transition_to(AgentState.THINKING)
            if result:
                logger.info("Agent resumed: id=%s", self.agent_id)
            return result
        logger.warning(
            "CANNOT RESUME AGENT NOT IN PAUSED STATE: ID=%S STATE=%S",
            self.agent_id,
            self.state.value,
        )
        return False

    def xǁBaseAgentǁresume__mutmut_20(self) -> bool:
        """Resume a paused agent."""
        if self.state == AgentState.PAUSED:
            result = self.transition_to(AgentState.THINKING)
            if result:
                logger.info("Agent resumed: id=%s", self.agent_id)
            return result
        logger.warning(
            "Cannot resume agent not in PAUSED state: id=%s state=%s",
            self.agent_id,
            self.state.value,
        )
        return True

    @_mutmut_mutated(mutants_xǁBaseAgentǁterminate__mutmut)
    def terminate(self) -> bool:
        """Terminate the agent."""
        result = self.transition_to(AgentState.TERMINATED)
        if result:
            logger.info("Agent terminated: id=%s", self.agent_id)
        return result

    def xǁBaseAgentǁterminate__mutmut_orig(self) -> bool:
        """Terminate the agent."""
        result = self.transition_to(AgentState.TERMINATED)
        if result:
            logger.info("Agent terminated: id=%s", self.agent_id)
        return result

    def xǁBaseAgentǁterminate__mutmut_1(self) -> bool:
        """Terminate the agent."""
        result = None
        if result:
            logger.info("Agent terminated: id=%s", self.agent_id)
        return result

    def xǁBaseAgentǁterminate__mutmut_2(self) -> bool:
        """Terminate the agent."""
        result = self.transition_to(None)
        if result:
            logger.info("Agent terminated: id=%s", self.agent_id)
        return result

    def xǁBaseAgentǁterminate__mutmut_3(self) -> bool:
        """Terminate the agent."""
        result = self.transition_to(AgentState.TERMINATED)
        if result:
            logger.info(None, self.agent_id)
        return result

    def xǁBaseAgentǁterminate__mutmut_4(self) -> bool:
        """Terminate the agent."""
        result = self.transition_to(AgentState.TERMINATED)
        if result:
            logger.info("Agent terminated: id=%s", None)
        return result

    def xǁBaseAgentǁterminate__mutmut_5(self) -> bool:
        """Terminate the agent."""
        result = self.transition_to(AgentState.TERMINATED)
        if result:
            logger.info(self.agent_id)
        return result

    def xǁBaseAgentǁterminate__mutmut_6(self) -> bool:
        """Terminate the agent."""
        result = self.transition_to(AgentState.TERMINATED)
        if result:
            logger.info("Agent terminated: id=%s", )
        return result

    def xǁBaseAgentǁterminate__mutmut_7(self) -> bool:
        """Terminate the agent."""
        result = self.transition_to(AgentState.TERMINATED)
        if result:
            logger.info("XXAgent terminated: id=%sXX", self.agent_id)
        return result

    def xǁBaseAgentǁterminate__mutmut_8(self) -> bool:
        """Terminate the agent."""
        result = self.transition_to(AgentState.TERMINATED)
        if result:
            logger.info("agent terminated: id=%s", self.agent_id)
        return result

    def xǁBaseAgentǁterminate__mutmut_9(self) -> bool:
        """Terminate the agent."""
        result = self.transition_to(AgentState.TERMINATED)
        if result:
            logger.info("AGENT TERMINATED: ID=%S", self.agent_id)
        return result

    # ── Abstract Methods ────────────────────────────────────

    @abstractmethod
    def think(self, observation: Any) -> Any:
        """Reasoning phase — analyze input and produce a decision."""

    @abstractmethod
    def act(self, decision: Any) -> Any:
        """Action phase — execute based on the decision."""

    # ── Messaging ───────────────────────────────────────────

    @_mutmut_mutated(mutants_xǁBaseAgentǁsend_message__mutmut)
    def send_message(self, recipient_id: str, content: Any, message_type: str = "inform") -> AgentMessage:
        """Send a message to another agent."""
        msg = AgentMessage(
            sender_id=self.agent_id,
            recipient_id=recipient_id,
            content=content,
            message_type=message_type,
        )
        return msg

    # ── Messaging ───────────────────────────────────────────

    def xǁBaseAgentǁsend_message__mutmut_orig(self, recipient_id: str, content: Any, message_type: str = "inform") -> AgentMessage:
        """Send a message to another agent."""
        msg = AgentMessage(
            sender_id=self.agent_id,
            recipient_id=recipient_id,
            content=content,
            message_type=message_type,
        )
        return msg

    # ── Messaging ───────────────────────────────────────────

    def xǁBaseAgentǁsend_message__mutmut_1(self, recipient_id: str, content: Any, message_type: str = "XXinformXX") -> AgentMessage:
        """Send a message to another agent."""
        msg = AgentMessage(
            sender_id=self.agent_id,
            recipient_id=recipient_id,
            content=content,
            message_type=message_type,
        )
        return msg

    # ── Messaging ───────────────────────────────────────────

    def xǁBaseAgentǁsend_message__mutmut_2(self, recipient_id: str, content: Any, message_type: str = "INFORM") -> AgentMessage:
        """Send a message to another agent."""
        msg = AgentMessage(
            sender_id=self.agent_id,
            recipient_id=recipient_id,
            content=content,
            message_type=message_type,
        )
        return msg

    # ── Messaging ───────────────────────────────────────────

    def xǁBaseAgentǁsend_message__mutmut_3(self, recipient_id: str, content: Any, message_type: str = "inform") -> AgentMessage:
        """Send a message to another agent."""
        msg = None
        return msg

    # ── Messaging ───────────────────────────────────────────

    def xǁBaseAgentǁsend_message__mutmut_4(self, recipient_id: str, content: Any, message_type: str = "inform") -> AgentMessage:
        """Send a message to another agent."""
        msg = AgentMessage(
            sender_id=None,
            recipient_id=recipient_id,
            content=content,
            message_type=message_type,
        )
        return msg

    # ── Messaging ───────────────────────────────────────────

    def xǁBaseAgentǁsend_message__mutmut_5(self, recipient_id: str, content: Any, message_type: str = "inform") -> AgentMessage:
        """Send a message to another agent."""
        msg = AgentMessage(
            sender_id=self.agent_id,
            recipient_id=None,
            content=content,
            message_type=message_type,
        )
        return msg

    # ── Messaging ───────────────────────────────────────────

    def xǁBaseAgentǁsend_message__mutmut_6(self, recipient_id: str, content: Any, message_type: str = "inform") -> AgentMessage:
        """Send a message to another agent."""
        msg = AgentMessage(
            sender_id=self.agent_id,
            recipient_id=recipient_id,
            content=None,
            message_type=message_type,
        )
        return msg

    # ── Messaging ───────────────────────────────────────────

    def xǁBaseAgentǁsend_message__mutmut_7(self, recipient_id: str, content: Any, message_type: str = "inform") -> AgentMessage:
        """Send a message to another agent."""
        msg = AgentMessage(
            sender_id=self.agent_id,
            recipient_id=recipient_id,
            content=content,
            message_type=None,
        )
        return msg

    # ── Messaging ───────────────────────────────────────────

    def xǁBaseAgentǁsend_message__mutmut_8(self, recipient_id: str, content: Any, message_type: str = "inform") -> AgentMessage:
        """Send a message to another agent."""
        msg = AgentMessage(
            recipient_id=recipient_id,
            content=content,
            message_type=message_type,
        )
        return msg

    # ── Messaging ───────────────────────────────────────────

    def xǁBaseAgentǁsend_message__mutmut_9(self, recipient_id: str, content: Any, message_type: str = "inform") -> AgentMessage:
        """Send a message to another agent."""
        msg = AgentMessage(
            sender_id=self.agent_id,
            content=content,
            message_type=message_type,
        )
        return msg

    # ── Messaging ───────────────────────────────────────────

    def xǁBaseAgentǁsend_message__mutmut_10(self, recipient_id: str, content: Any, message_type: str = "inform") -> AgentMessage:
        """Send a message to another agent."""
        msg = AgentMessage(
            sender_id=self.agent_id,
            recipient_id=recipient_id,
            message_type=message_type,
        )
        return msg

    # ── Messaging ───────────────────────────────────────────

    def xǁBaseAgentǁsend_message__mutmut_11(self, recipient_id: str, content: Any, message_type: str = "inform") -> AgentMessage:
        """Send a message to another agent."""
        msg = AgentMessage(
            sender_id=self.agent_id,
            recipient_id=recipient_id,
            content=content,
            )
        return msg

    @_mutmut_mutated(mutants_xǁBaseAgentǁreceive_message__mutmut)
    def receive_message(self, message: AgentMessage) -> None:
        """Receive and queue a message from another agent."""
        with self._message_lock:
            self._message_queue.append(message)

    def xǁBaseAgentǁreceive_message__mutmut_orig(self, message: AgentMessage) -> None:
        """Receive and queue a message from another agent."""
        with self._message_lock:
            self._message_queue.append(message)

    def xǁBaseAgentǁreceive_message__mutmut_1(self, message: AgentMessage) -> None:
        """Receive and queue a message from another agent."""
        with self._message_lock:
            self._message_queue.append(None)

    @_mutmut_mutated(mutants_xǁBaseAgentǁget_pending_messages__mutmut)
    def get_pending_messages(self) -> list[AgentMessage]:
        """Get and clear all pending messages."""
        with self._message_lock:
            messages = list(self._message_queue)
            self._message_queue.clear()
            return messages

    def xǁBaseAgentǁget_pending_messages__mutmut_orig(self) -> list[AgentMessage]:
        """Get and clear all pending messages."""
        with self._message_lock:
            messages = list(self._message_queue)
            self._message_queue.clear()
            return messages

    def xǁBaseAgentǁget_pending_messages__mutmut_1(self) -> list[AgentMessage]:
        """Get and clear all pending messages."""
        with self._message_lock:
            messages = None
            self._message_queue.clear()
            return messages

    def xǁBaseAgentǁget_pending_messages__mutmut_2(self) -> list[AgentMessage]:
        """Get and clear all pending messages."""
        with self._message_lock:
            messages = list(None)
            self._message_queue.clear()
            return messages

    # ── Context ─────────────────────────────────────────────

    @_mutmut_mutated(mutants_xǁBaseAgentǁset_context__mutmut)
    def set_context(self, key: str, value: Any) -> None:
        """Set a context variable."""
        self._context[key] = value

    # ── Context ─────────────────────────────────────────────

    def xǁBaseAgentǁset_context__mutmut_orig(self, key: str, value: Any) -> None:
        """Set a context variable."""
        self._context[key] = value

    # ── Context ─────────────────────────────────────────────

    def xǁBaseAgentǁset_context__mutmut_1(self, key: str, value: Any) -> None:
        """Set a context variable."""
        self._context[key] = None

    @_mutmut_mutated(mutants_xǁBaseAgentǁget_context__mutmut)
    def get_context(self, key: str, default: Any = None) -> Any:
        """Get a context variable."""
        return self._context.get(key, default)

    def xǁBaseAgentǁget_context__mutmut_orig(self, key: str, default: Any = None) -> Any:
        """Get a context variable."""
        return self._context.get(key, default)

    def xǁBaseAgentǁget_context__mutmut_1(self, key: str, default: Any = None) -> Any:
        """Get a context variable."""
        return self._context.get(None, default)

    def xǁBaseAgentǁget_context__mutmut_2(self, key: str, default: Any = None) -> Any:
        """Get a context variable."""
        return self._context.get(key, None)

    def xǁBaseAgentǁget_context__mutmut_3(self, key: str, default: Any = None) -> Any:
        """Get a context variable."""
        return self._context.get(default)

    def xǁBaseAgentǁget_context__mutmut_4(self, key: str, default: Any = None) -> Any:
        """Get a context variable."""
        return self._context.get(key, )

    # ── Internal ────────────────────────────────────────────

    @_mutmut_mutated(mutants_xǁBaseAgentǁ_should_stop__mutmut)
    def _should_stop(self, result: Any) -> bool:
        """Determine if the agent should stop after an action."""
        if isinstance(result, dict):
            return result.get("_stop", False) or result.get("done", False)
        return False

    # ── Internal ────────────────────────────────────────────

    def xǁBaseAgentǁ_should_stop__mutmut_orig(self, result: Any) -> bool:
        """Determine if the agent should stop after an action."""
        if isinstance(result, dict):
            return result.get("_stop", False) or result.get("done", False)
        return False

    # ── Internal ────────────────────────────────────────────

    def xǁBaseAgentǁ_should_stop__mutmut_1(self, result: Any) -> bool:
        """Determine if the agent should stop after an action."""
        if isinstance(result, dict):
            return result.get("_stop", False) and result.get("done", False)
        return False

    # ── Internal ────────────────────────────────────────────

    def xǁBaseAgentǁ_should_stop__mutmut_2(self, result: Any) -> bool:
        """Determine if the agent should stop after an action."""
        if isinstance(result, dict):
            return result.get(None, False) or result.get("done", False)
        return False

    # ── Internal ────────────────────────────────────────────

    def xǁBaseAgentǁ_should_stop__mutmut_3(self, result: Any) -> bool:
        """Determine if the agent should stop after an action."""
        if isinstance(result, dict):
            return result.get("_stop", None) or result.get("done", False)
        return False

    # ── Internal ────────────────────────────────────────────

    def xǁBaseAgentǁ_should_stop__mutmut_4(self, result: Any) -> bool:
        """Determine if the agent should stop after an action."""
        if isinstance(result, dict):
            return result.get(False) or result.get("done", False)
        return False

    # ── Internal ────────────────────────────────────────────

    def xǁBaseAgentǁ_should_stop__mutmut_5(self, result: Any) -> bool:
        """Determine if the agent should stop after an action."""
        if isinstance(result, dict):
            return result.get("_stop", ) or result.get("done", False)
        return False

    # ── Internal ────────────────────────────────────────────

    def xǁBaseAgentǁ_should_stop__mutmut_6(self, result: Any) -> bool:
        """Determine if the agent should stop after an action."""
        if isinstance(result, dict):
            return result.get("XX_stopXX", False) or result.get("done", False)
        return False

    # ── Internal ────────────────────────────────────────────

    def xǁBaseAgentǁ_should_stop__mutmut_7(self, result: Any) -> bool:
        """Determine if the agent should stop after an action."""
        if isinstance(result, dict):
            return result.get("_STOP", False) or result.get("done", False)
        return False

    # ── Internal ────────────────────────────────────────────

    def xǁBaseAgentǁ_should_stop__mutmut_8(self, result: Any) -> bool:
        """Determine if the agent should stop after an action."""
        if isinstance(result, dict):
            return result.get("_stop", True) or result.get("done", False)
        return False

    # ── Internal ────────────────────────────────────────────

    def xǁBaseAgentǁ_should_stop__mutmut_9(self, result: Any) -> bool:
        """Determine if the agent should stop after an action."""
        if isinstance(result, dict):
            return result.get("_stop", False) or result.get(None, False)
        return False

    # ── Internal ────────────────────────────────────────────

    def xǁBaseAgentǁ_should_stop__mutmut_10(self, result: Any) -> bool:
        """Determine if the agent should stop after an action."""
        if isinstance(result, dict):
            return result.get("_stop", False) or result.get("done", None)
        return False

    # ── Internal ────────────────────────────────────────────

    def xǁBaseAgentǁ_should_stop__mutmut_11(self, result: Any) -> bool:
        """Determine if the agent should stop after an action."""
        if isinstance(result, dict):
            return result.get("_stop", False) or result.get(False)
        return False

    # ── Internal ────────────────────────────────────────────

    def xǁBaseAgentǁ_should_stop__mutmut_12(self, result: Any) -> bool:
        """Determine if the agent should stop after an action."""
        if isinstance(result, dict):
            return result.get("_stop", False) or result.get("done", )
        return False

    # ── Internal ────────────────────────────────────────────

    def xǁBaseAgentǁ_should_stop__mutmut_13(self, result: Any) -> bool:
        """Determine if the agent should stop after an action."""
        if isinstance(result, dict):
            return result.get("_stop", False) or result.get("XXdoneXX", False)
        return False

    # ── Internal ────────────────────────────────────────────

    def xǁBaseAgentǁ_should_stop__mutmut_14(self, result: Any) -> bool:
        """Determine if the agent should stop after an action."""
        if isinstance(result, dict):
            return result.get("_stop", False) or result.get("DONE", False)
        return False

    # ── Internal ────────────────────────────────────────────

    def xǁBaseAgentǁ_should_stop__mutmut_15(self, result: Any) -> bool:
        """Determine if the agent should stop after an action."""
        if isinstance(result, dict):
            return result.get("_stop", False) or result.get("done", True)
        return False

    # ── Internal ────────────────────────────────────────────

    def xǁBaseAgentǁ_should_stop__mutmut_16(self, result: Any) -> bool:
        """Determine if the agent should stop after an action."""
        if isinstance(result, dict):
            return result.get("_stop", False) or result.get("done", False)
        return True

    @_mutmut_mutated(mutants_xǁBaseAgentǁget_status__mutmut)
    def get_status(self) -> dict[str, Any]:
        """Get the current status of the agent."""
        return {
            "agent_id": self.agent_id,
            "name": self.name,
            "state": self.state.value,
            "capabilities": [c.value for c in self.capabilities],
            "iteration_count": self._iteration_count,
            "error_count": self._error_count,
            "uptime": self.uptime,
            "last_active": self._last_active,
            "pending_messages": len(self._message_queue),
            "parent_id": self._parent_id,
            "child_ids": self._child_ids,
        }

    def xǁBaseAgentǁget_status__mutmut_orig(self) -> dict[str, Any]:
        """Get the current status of the agent."""
        return {
            "agent_id": self.agent_id,
            "name": self.name,
            "state": self.state.value,
            "capabilities": [c.value for c in self.capabilities],
            "iteration_count": self._iteration_count,
            "error_count": self._error_count,
            "uptime": self.uptime,
            "last_active": self._last_active,
            "pending_messages": len(self._message_queue),
            "parent_id": self._parent_id,
            "child_ids": self._child_ids,
        }

    def xǁBaseAgentǁget_status__mutmut_1(self) -> dict[str, Any]:
        """Get the current status of the agent."""
        return {
            "XXagent_idXX": self.agent_id,
            "name": self.name,
            "state": self.state.value,
            "capabilities": [c.value for c in self.capabilities],
            "iteration_count": self._iteration_count,
            "error_count": self._error_count,
            "uptime": self.uptime,
            "last_active": self._last_active,
            "pending_messages": len(self._message_queue),
            "parent_id": self._parent_id,
            "child_ids": self._child_ids,
        }

    def xǁBaseAgentǁget_status__mutmut_2(self) -> dict[str, Any]:
        """Get the current status of the agent."""
        return {
            "AGENT_ID": self.agent_id,
            "name": self.name,
            "state": self.state.value,
            "capabilities": [c.value for c in self.capabilities],
            "iteration_count": self._iteration_count,
            "error_count": self._error_count,
            "uptime": self.uptime,
            "last_active": self._last_active,
            "pending_messages": len(self._message_queue),
            "parent_id": self._parent_id,
            "child_ids": self._child_ids,
        }

    def xǁBaseAgentǁget_status__mutmut_3(self) -> dict[str, Any]:
        """Get the current status of the agent."""
        return {
            "agent_id": self.agent_id,
            "XXnameXX": self.name,
            "state": self.state.value,
            "capabilities": [c.value for c in self.capabilities],
            "iteration_count": self._iteration_count,
            "error_count": self._error_count,
            "uptime": self.uptime,
            "last_active": self._last_active,
            "pending_messages": len(self._message_queue),
            "parent_id": self._parent_id,
            "child_ids": self._child_ids,
        }

    def xǁBaseAgentǁget_status__mutmut_4(self) -> dict[str, Any]:
        """Get the current status of the agent."""
        return {
            "agent_id": self.agent_id,
            "NAME": self.name,
            "state": self.state.value,
            "capabilities": [c.value for c in self.capabilities],
            "iteration_count": self._iteration_count,
            "error_count": self._error_count,
            "uptime": self.uptime,
            "last_active": self._last_active,
            "pending_messages": len(self._message_queue),
            "parent_id": self._parent_id,
            "child_ids": self._child_ids,
        }

    def xǁBaseAgentǁget_status__mutmut_5(self) -> dict[str, Any]:
        """Get the current status of the agent."""
        return {
            "agent_id": self.agent_id,
            "name": self.name,
            "XXstateXX": self.state.value,
            "capabilities": [c.value for c in self.capabilities],
            "iteration_count": self._iteration_count,
            "error_count": self._error_count,
            "uptime": self.uptime,
            "last_active": self._last_active,
            "pending_messages": len(self._message_queue),
            "parent_id": self._parent_id,
            "child_ids": self._child_ids,
        }

    def xǁBaseAgentǁget_status__mutmut_6(self) -> dict[str, Any]:
        """Get the current status of the agent."""
        return {
            "agent_id": self.agent_id,
            "name": self.name,
            "STATE": self.state.value,
            "capabilities": [c.value for c in self.capabilities],
            "iteration_count": self._iteration_count,
            "error_count": self._error_count,
            "uptime": self.uptime,
            "last_active": self._last_active,
            "pending_messages": len(self._message_queue),
            "parent_id": self._parent_id,
            "child_ids": self._child_ids,
        }

    def xǁBaseAgentǁget_status__mutmut_7(self) -> dict[str, Any]:
        """Get the current status of the agent."""
        return {
            "agent_id": self.agent_id,
            "name": self.name,
            "state": self.state.value,
            "XXcapabilitiesXX": [c.value for c in self.capabilities],
            "iteration_count": self._iteration_count,
            "error_count": self._error_count,
            "uptime": self.uptime,
            "last_active": self._last_active,
            "pending_messages": len(self._message_queue),
            "parent_id": self._parent_id,
            "child_ids": self._child_ids,
        }

    def xǁBaseAgentǁget_status__mutmut_8(self) -> dict[str, Any]:
        """Get the current status of the agent."""
        return {
            "agent_id": self.agent_id,
            "name": self.name,
            "state": self.state.value,
            "CAPABILITIES": [c.value for c in self.capabilities],
            "iteration_count": self._iteration_count,
            "error_count": self._error_count,
            "uptime": self.uptime,
            "last_active": self._last_active,
            "pending_messages": len(self._message_queue),
            "parent_id": self._parent_id,
            "child_ids": self._child_ids,
        }

    def xǁBaseAgentǁget_status__mutmut_9(self) -> dict[str, Any]:
        """Get the current status of the agent."""
        return {
            "agent_id": self.agent_id,
            "name": self.name,
            "state": self.state.value,
            "capabilities": [c.value for c in self.capabilities],
            "XXiteration_countXX": self._iteration_count,
            "error_count": self._error_count,
            "uptime": self.uptime,
            "last_active": self._last_active,
            "pending_messages": len(self._message_queue),
            "parent_id": self._parent_id,
            "child_ids": self._child_ids,
        }

    def xǁBaseAgentǁget_status__mutmut_10(self) -> dict[str, Any]:
        """Get the current status of the agent."""
        return {
            "agent_id": self.agent_id,
            "name": self.name,
            "state": self.state.value,
            "capabilities": [c.value for c in self.capabilities],
            "ITERATION_COUNT": self._iteration_count,
            "error_count": self._error_count,
            "uptime": self.uptime,
            "last_active": self._last_active,
            "pending_messages": len(self._message_queue),
            "parent_id": self._parent_id,
            "child_ids": self._child_ids,
        }

    def xǁBaseAgentǁget_status__mutmut_11(self) -> dict[str, Any]:
        """Get the current status of the agent."""
        return {
            "agent_id": self.agent_id,
            "name": self.name,
            "state": self.state.value,
            "capabilities": [c.value for c in self.capabilities],
            "iteration_count": self._iteration_count,
            "XXerror_countXX": self._error_count,
            "uptime": self.uptime,
            "last_active": self._last_active,
            "pending_messages": len(self._message_queue),
            "parent_id": self._parent_id,
            "child_ids": self._child_ids,
        }

    def xǁBaseAgentǁget_status__mutmut_12(self) -> dict[str, Any]:
        """Get the current status of the agent."""
        return {
            "agent_id": self.agent_id,
            "name": self.name,
            "state": self.state.value,
            "capabilities": [c.value for c in self.capabilities],
            "iteration_count": self._iteration_count,
            "ERROR_COUNT": self._error_count,
            "uptime": self.uptime,
            "last_active": self._last_active,
            "pending_messages": len(self._message_queue),
            "parent_id": self._parent_id,
            "child_ids": self._child_ids,
        }

    def xǁBaseAgentǁget_status__mutmut_13(self) -> dict[str, Any]:
        """Get the current status of the agent."""
        return {
            "agent_id": self.agent_id,
            "name": self.name,
            "state": self.state.value,
            "capabilities": [c.value for c in self.capabilities],
            "iteration_count": self._iteration_count,
            "error_count": self._error_count,
            "XXuptimeXX": self.uptime,
            "last_active": self._last_active,
            "pending_messages": len(self._message_queue),
            "parent_id": self._parent_id,
            "child_ids": self._child_ids,
        }

    def xǁBaseAgentǁget_status__mutmut_14(self) -> dict[str, Any]:
        """Get the current status of the agent."""
        return {
            "agent_id": self.agent_id,
            "name": self.name,
            "state": self.state.value,
            "capabilities": [c.value for c in self.capabilities],
            "iteration_count": self._iteration_count,
            "error_count": self._error_count,
            "UPTIME": self.uptime,
            "last_active": self._last_active,
            "pending_messages": len(self._message_queue),
            "parent_id": self._parent_id,
            "child_ids": self._child_ids,
        }

    def xǁBaseAgentǁget_status__mutmut_15(self) -> dict[str, Any]:
        """Get the current status of the agent."""
        return {
            "agent_id": self.agent_id,
            "name": self.name,
            "state": self.state.value,
            "capabilities": [c.value for c in self.capabilities],
            "iteration_count": self._iteration_count,
            "error_count": self._error_count,
            "uptime": self.uptime,
            "XXlast_activeXX": self._last_active,
            "pending_messages": len(self._message_queue),
            "parent_id": self._parent_id,
            "child_ids": self._child_ids,
        }

    def xǁBaseAgentǁget_status__mutmut_16(self) -> dict[str, Any]:
        """Get the current status of the agent."""
        return {
            "agent_id": self.agent_id,
            "name": self.name,
            "state": self.state.value,
            "capabilities": [c.value for c in self.capabilities],
            "iteration_count": self._iteration_count,
            "error_count": self._error_count,
            "uptime": self.uptime,
            "LAST_ACTIVE": self._last_active,
            "pending_messages": len(self._message_queue),
            "parent_id": self._parent_id,
            "child_ids": self._child_ids,
        }

    def xǁBaseAgentǁget_status__mutmut_17(self) -> dict[str, Any]:
        """Get the current status of the agent."""
        return {
            "agent_id": self.agent_id,
            "name": self.name,
            "state": self.state.value,
            "capabilities": [c.value for c in self.capabilities],
            "iteration_count": self._iteration_count,
            "error_count": self._error_count,
            "uptime": self.uptime,
            "last_active": self._last_active,
            "XXpending_messagesXX": len(self._message_queue),
            "parent_id": self._parent_id,
            "child_ids": self._child_ids,
        }

    def xǁBaseAgentǁget_status__mutmut_18(self) -> dict[str, Any]:
        """Get the current status of the agent."""
        return {
            "agent_id": self.agent_id,
            "name": self.name,
            "state": self.state.value,
            "capabilities": [c.value for c in self.capabilities],
            "iteration_count": self._iteration_count,
            "error_count": self._error_count,
            "uptime": self.uptime,
            "last_active": self._last_active,
            "PENDING_MESSAGES": len(self._message_queue),
            "parent_id": self._parent_id,
            "child_ids": self._child_ids,
        }

    def xǁBaseAgentǁget_status__mutmut_19(self) -> dict[str, Any]:
        """Get the current status of the agent."""
        return {
            "agent_id": self.agent_id,
            "name": self.name,
            "state": self.state.value,
            "capabilities": [c.value for c in self.capabilities],
            "iteration_count": self._iteration_count,
            "error_count": self._error_count,
            "uptime": self.uptime,
            "last_active": self._last_active,
            "pending_messages": len(self._message_queue),
            "XXparent_idXX": self._parent_id,
            "child_ids": self._child_ids,
        }

    def xǁBaseAgentǁget_status__mutmut_20(self) -> dict[str, Any]:
        """Get the current status of the agent."""
        return {
            "agent_id": self.agent_id,
            "name": self.name,
            "state": self.state.value,
            "capabilities": [c.value for c in self.capabilities],
            "iteration_count": self._iteration_count,
            "error_count": self._error_count,
            "uptime": self.uptime,
            "last_active": self._last_active,
            "pending_messages": len(self._message_queue),
            "PARENT_ID": self._parent_id,
            "child_ids": self._child_ids,
        }

    def xǁBaseAgentǁget_status__mutmut_21(self) -> dict[str, Any]:
        """Get the current status of the agent."""
        return {
            "agent_id": self.agent_id,
            "name": self.name,
            "state": self.state.value,
            "capabilities": [c.value for c in self.capabilities],
            "iteration_count": self._iteration_count,
            "error_count": self._error_count,
            "uptime": self.uptime,
            "last_active": self._last_active,
            "pending_messages": len(self._message_queue),
            "parent_id": self._parent_id,
            "XXchild_idsXX": self._child_ids,
        }

    def xǁBaseAgentǁget_status__mutmut_22(self) -> dict[str, Any]:
        """Get the current status of the agent."""
        return {
            "agent_id": self.agent_id,
            "name": self.name,
            "state": self.state.value,
            "capabilities": [c.value for c in self.capabilities],
            "iteration_count": self._iteration_count,
            "error_count": self._error_count,
            "uptime": self.uptime,
            "last_active": self._last_active,
            "pending_messages": len(self._message_queue),
            "parent_id": self._parent_id,
            "CHILD_IDS": self._child_ids,
        }

mutants_xǁBaseAgentǁ__init____mutmut['_mutmut_orig'] = BaseAgent.xǁBaseAgentǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁBaseAgentǁ__init____mutmut['xǁBaseAgentǁ__init____mutmut_1'] = BaseAgent.xǁBaseAgentǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁ__init____mutmut['xǁBaseAgentǁ__init____mutmut_2'] = BaseAgent.xǁBaseAgentǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁ__init____mutmut['xǁBaseAgentǁ__init____mutmut_3'] = BaseAgent.xǁBaseAgentǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁ__init____mutmut['xǁBaseAgentǁ__init____mutmut_4'] = BaseAgent.xǁBaseAgentǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁ__init____mutmut['xǁBaseAgentǁ__init____mutmut_5'] = BaseAgent.xǁBaseAgentǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁ__init____mutmut['xǁBaseAgentǁ__init____mutmut_6'] = BaseAgent.xǁBaseAgentǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁ__init____mutmut['xǁBaseAgentǁ__init____mutmut_7'] = BaseAgent.xǁBaseAgentǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁ__init____mutmut['xǁBaseAgentǁ__init____mutmut_8'] = BaseAgent.xǁBaseAgentǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁ__init____mutmut['xǁBaseAgentǁ__init____mutmut_9'] = BaseAgent.xǁBaseAgentǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁ__init____mutmut['xǁBaseAgentǁ__init____mutmut_10'] = BaseAgent.xǁBaseAgentǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁ__init____mutmut['xǁBaseAgentǁ__init____mutmut_11'] = BaseAgent.xǁBaseAgentǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁ__init____mutmut['xǁBaseAgentǁ__init____mutmut_12'] = BaseAgent.xǁBaseAgentǁ__init____mutmut_12 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁ__init____mutmut['xǁBaseAgentǁ__init____mutmut_13'] = BaseAgent.xǁBaseAgentǁ__init____mutmut_13 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁ__init____mutmut['xǁBaseAgentǁ__init____mutmut_14'] = BaseAgent.xǁBaseAgentǁ__init____mutmut_14 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁ__init____mutmut['xǁBaseAgentǁ__init____mutmut_15'] = BaseAgent.xǁBaseAgentǁ__init____mutmut_15 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁ__init____mutmut['xǁBaseAgentǁ__init____mutmut_16'] = BaseAgent.xǁBaseAgentǁ__init____mutmut_16 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁ__init____mutmut['xǁBaseAgentǁ__init____mutmut_17'] = BaseAgent.xǁBaseAgentǁ__init____mutmut_17 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁ__init____mutmut['xǁBaseAgentǁ__init____mutmut_18'] = BaseAgent.xǁBaseAgentǁ__init____mutmut_18 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁ__init____mutmut['xǁBaseAgentǁ__init____mutmut_19'] = BaseAgent.xǁBaseAgentǁ__init____mutmut_19 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁ__init____mutmut['xǁBaseAgentǁ__init____mutmut_20'] = BaseAgent.xǁBaseAgentǁ__init____mutmut_20 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁ__init____mutmut['xǁBaseAgentǁ__init____mutmut_21'] = BaseAgent.xǁBaseAgentǁ__init____mutmut_21 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁ__init____mutmut['xǁBaseAgentǁ__init____mutmut_22'] = BaseAgent.xǁBaseAgentǁ__init____mutmut_22 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁ__init____mutmut['xǁBaseAgentǁ__init____mutmut_23'] = BaseAgent.xǁBaseAgentǁ__init____mutmut_23 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁ__init____mutmut['xǁBaseAgentǁ__init____mutmut_24'] = BaseAgent.xǁBaseAgentǁ__init____mutmut_24 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁ__init____mutmut['xǁBaseAgentǁ__init____mutmut_25'] = BaseAgent.xǁBaseAgentǁ__init____mutmut_25 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁ__init____mutmut['xǁBaseAgentǁ__init____mutmut_26'] = BaseAgent.xǁBaseAgentǁ__init____mutmut_26 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁ__init____mutmut['xǁBaseAgentǁ__init____mutmut_27'] = BaseAgent.xǁBaseAgentǁ__init____mutmut_27 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁ__init____mutmut['xǁBaseAgentǁ__init____mutmut_28'] = BaseAgent.xǁBaseAgentǁ__init____mutmut_28 # type: ignore # mutmut generated

mutants_xǁBaseAgentǁtransition_to__mutmut['_mutmut_orig'] = BaseAgent.xǁBaseAgentǁtransition_to__mutmut_orig # type: ignore # mutmut generated
mutants_xǁBaseAgentǁtransition_to__mutmut['xǁBaseAgentǁtransition_to__mutmut_1'] = BaseAgent.xǁBaseAgentǁtransition_to__mutmut_1 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁtransition_to__mutmut['xǁBaseAgentǁtransition_to__mutmut_2'] = BaseAgent.xǁBaseAgentǁtransition_to__mutmut_2 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁtransition_to__mutmut['xǁBaseAgentǁtransition_to__mutmut_3'] = BaseAgent.xǁBaseAgentǁtransition_to__mutmut_3 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁtransition_to__mutmut['xǁBaseAgentǁtransition_to__mutmut_4'] = BaseAgent.xǁBaseAgentǁtransition_to__mutmut_4 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁtransition_to__mutmut['xǁBaseAgentǁtransition_to__mutmut_5'] = BaseAgent.xǁBaseAgentǁtransition_to__mutmut_5 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁtransition_to__mutmut['xǁBaseAgentǁtransition_to__mutmut_6'] = BaseAgent.xǁBaseAgentǁtransition_to__mutmut_6 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁtransition_to__mutmut['xǁBaseAgentǁtransition_to__mutmut_7'] = BaseAgent.xǁBaseAgentǁtransition_to__mutmut_7 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁtransition_to__mutmut['xǁBaseAgentǁtransition_to__mutmut_8'] = BaseAgent.xǁBaseAgentǁtransition_to__mutmut_8 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁtransition_to__mutmut['xǁBaseAgentǁtransition_to__mutmut_9'] = BaseAgent.xǁBaseAgentǁtransition_to__mutmut_9 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁtransition_to__mutmut['xǁBaseAgentǁtransition_to__mutmut_10'] = BaseAgent.xǁBaseAgentǁtransition_to__mutmut_10 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁtransition_to__mutmut['xǁBaseAgentǁtransition_to__mutmut_11'] = BaseAgent.xǁBaseAgentǁtransition_to__mutmut_11 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁtransition_to__mutmut['xǁBaseAgentǁtransition_to__mutmut_12'] = BaseAgent.xǁBaseAgentǁtransition_to__mutmut_12 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁtransition_to__mutmut['xǁBaseAgentǁtransition_to__mutmut_13'] = BaseAgent.xǁBaseAgentǁtransition_to__mutmut_13 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁtransition_to__mutmut['xǁBaseAgentǁtransition_to__mutmut_14'] = BaseAgent.xǁBaseAgentǁtransition_to__mutmut_14 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁtransition_to__mutmut['xǁBaseAgentǁtransition_to__mutmut_15'] = BaseAgent.xǁBaseAgentǁtransition_to__mutmut_15 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁtransition_to__mutmut['xǁBaseAgentǁtransition_to__mutmut_16'] = BaseAgent.xǁBaseAgentǁtransition_to__mutmut_16 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁtransition_to__mutmut['xǁBaseAgentǁtransition_to__mutmut_17'] = BaseAgent.xǁBaseAgentǁtransition_to__mutmut_17 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁtransition_to__mutmut['xǁBaseAgentǁtransition_to__mutmut_18'] = BaseAgent.xǁBaseAgentǁtransition_to__mutmut_18 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁtransition_to__mutmut['xǁBaseAgentǁtransition_to__mutmut_19'] = BaseAgent.xǁBaseAgentǁtransition_to__mutmut_19 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁtransition_to__mutmut['xǁBaseAgentǁtransition_to__mutmut_20'] = BaseAgent.xǁBaseAgentǁtransition_to__mutmut_20 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁtransition_to__mutmut['xǁBaseAgentǁtransition_to__mutmut_21'] = BaseAgent.xǁBaseAgentǁtransition_to__mutmut_21 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁtransition_to__mutmut['xǁBaseAgentǁtransition_to__mutmut_22'] = BaseAgent.xǁBaseAgentǁtransition_to__mutmut_22 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁtransition_to__mutmut['xǁBaseAgentǁtransition_to__mutmut_23'] = BaseAgent.xǁBaseAgentǁtransition_to__mutmut_23 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁtransition_to__mutmut['xǁBaseAgentǁtransition_to__mutmut_24'] = BaseAgent.xǁBaseAgentǁtransition_to__mutmut_24 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁtransition_to__mutmut['xǁBaseAgentǁtransition_to__mutmut_25'] = BaseAgent.xǁBaseAgentǁtransition_to__mutmut_25 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁtransition_to__mutmut['xǁBaseAgentǁtransition_to__mutmut_26'] = BaseAgent.xǁBaseAgentǁtransition_to__mutmut_26 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁtransition_to__mutmut['xǁBaseAgentǁtransition_to__mutmut_27'] = BaseAgent.xǁBaseAgentǁtransition_to__mutmut_27 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁtransition_to__mutmut['xǁBaseAgentǁtransition_to__mutmut_28'] = BaseAgent.xǁBaseAgentǁtransition_to__mutmut_28 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁtransition_to__mutmut['xǁBaseAgentǁtransition_to__mutmut_29'] = BaseAgent.xǁBaseAgentǁtransition_to__mutmut_29 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁtransition_to__mutmut['xǁBaseAgentǁtransition_to__mutmut_30'] = BaseAgent.xǁBaseAgentǁtransition_to__mutmut_30 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁtransition_to__mutmut['xǁBaseAgentǁtransition_to__mutmut_31'] = BaseAgent.xǁBaseAgentǁtransition_to__mutmut_31 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁtransition_to__mutmut['xǁBaseAgentǁtransition_to__mutmut_32'] = BaseAgent.xǁBaseAgentǁtransition_to__mutmut_32 # type: ignore # mutmut generated

mutants_xǁBaseAgentǁforce_state__mutmut['_mutmut_orig'] = BaseAgent.xǁBaseAgentǁforce_state__mutmut_orig # type: ignore # mutmut generated
mutants_xǁBaseAgentǁforce_state__mutmut['xǁBaseAgentǁforce_state__mutmut_1'] = BaseAgent.xǁBaseAgentǁforce_state__mutmut_1 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁforce_state__mutmut['xǁBaseAgentǁforce_state__mutmut_2'] = BaseAgent.xǁBaseAgentǁforce_state__mutmut_2 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁforce_state__mutmut['xǁBaseAgentǁforce_state__mutmut_3'] = BaseAgent.xǁBaseAgentǁforce_state__mutmut_3 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁforce_state__mutmut['xǁBaseAgentǁforce_state__mutmut_4'] = BaseAgent.xǁBaseAgentǁforce_state__mutmut_4 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁforce_state__mutmut['xǁBaseAgentǁforce_state__mutmut_5'] = BaseAgent.xǁBaseAgentǁforce_state__mutmut_5 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁforce_state__mutmut['xǁBaseAgentǁforce_state__mutmut_6'] = BaseAgent.xǁBaseAgentǁforce_state__mutmut_6 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁforce_state__mutmut['xǁBaseAgentǁforce_state__mutmut_7'] = BaseAgent.xǁBaseAgentǁforce_state__mutmut_7 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁforce_state__mutmut['xǁBaseAgentǁforce_state__mutmut_8'] = BaseAgent.xǁBaseAgentǁforce_state__mutmut_8 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁforce_state__mutmut['xǁBaseAgentǁforce_state__mutmut_9'] = BaseAgent.xǁBaseAgentǁforce_state__mutmut_9 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁforce_state__mutmut['xǁBaseAgentǁforce_state__mutmut_10'] = BaseAgent.xǁBaseAgentǁforce_state__mutmut_10 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁforce_state__mutmut['xǁBaseAgentǁforce_state__mutmut_11'] = BaseAgent.xǁBaseAgentǁforce_state__mutmut_11 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁforce_state__mutmut['xǁBaseAgentǁforce_state__mutmut_12'] = BaseAgent.xǁBaseAgentǁforce_state__mutmut_12 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁforce_state__mutmut['xǁBaseAgentǁforce_state__mutmut_13'] = BaseAgent.xǁBaseAgentǁforce_state__mutmut_13 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁforce_state__mutmut['xǁBaseAgentǁforce_state__mutmut_14'] = BaseAgent.xǁBaseAgentǁforce_state__mutmut_14 # type: ignore # mutmut generated

mutants_xǁBaseAgentǁrun__mutmut['_mutmut_orig'] = BaseAgent.xǁBaseAgentǁrun__mutmut_orig # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_1'] = BaseAgent.xǁBaseAgentǁrun__mutmut_1 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_2'] = BaseAgent.xǁBaseAgentǁrun__mutmut_2 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_3'] = BaseAgent.xǁBaseAgentǁrun__mutmut_3 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_4'] = BaseAgent.xǁBaseAgentǁrun__mutmut_4 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_5'] = BaseAgent.xǁBaseAgentǁrun__mutmut_5 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_6'] = BaseAgent.xǁBaseAgentǁrun__mutmut_6 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_7'] = BaseAgent.xǁBaseAgentǁrun__mutmut_7 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_8'] = BaseAgent.xǁBaseAgentǁrun__mutmut_8 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_9'] = BaseAgent.xǁBaseAgentǁrun__mutmut_9 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_10'] = BaseAgent.xǁBaseAgentǁrun__mutmut_10 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_11'] = BaseAgent.xǁBaseAgentǁrun__mutmut_11 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_12'] = BaseAgent.xǁBaseAgentǁrun__mutmut_12 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_13'] = BaseAgent.xǁBaseAgentǁrun__mutmut_13 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_14'] = BaseAgent.xǁBaseAgentǁrun__mutmut_14 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_15'] = BaseAgent.xǁBaseAgentǁrun__mutmut_15 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_16'] = BaseAgent.xǁBaseAgentǁrun__mutmut_16 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_17'] = BaseAgent.xǁBaseAgentǁrun__mutmut_17 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_18'] = BaseAgent.xǁBaseAgentǁrun__mutmut_18 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_19'] = BaseAgent.xǁBaseAgentǁrun__mutmut_19 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_20'] = BaseAgent.xǁBaseAgentǁrun__mutmut_20 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_21'] = BaseAgent.xǁBaseAgentǁrun__mutmut_21 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_22'] = BaseAgent.xǁBaseAgentǁrun__mutmut_22 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_23'] = BaseAgent.xǁBaseAgentǁrun__mutmut_23 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_24'] = BaseAgent.xǁBaseAgentǁrun__mutmut_24 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_25'] = BaseAgent.xǁBaseAgentǁrun__mutmut_25 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_26'] = BaseAgent.xǁBaseAgentǁrun__mutmut_26 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_27'] = BaseAgent.xǁBaseAgentǁrun__mutmut_27 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_28'] = BaseAgent.xǁBaseAgentǁrun__mutmut_28 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_29'] = BaseAgent.xǁBaseAgentǁrun__mutmut_29 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_30'] = BaseAgent.xǁBaseAgentǁrun__mutmut_30 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_31'] = BaseAgent.xǁBaseAgentǁrun__mutmut_31 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_32'] = BaseAgent.xǁBaseAgentǁrun__mutmut_32 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_33'] = BaseAgent.xǁBaseAgentǁrun__mutmut_33 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_34'] = BaseAgent.xǁBaseAgentǁrun__mutmut_34 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_35'] = BaseAgent.xǁBaseAgentǁrun__mutmut_35 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_36'] = BaseAgent.xǁBaseAgentǁrun__mutmut_36 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_37'] = BaseAgent.xǁBaseAgentǁrun__mutmut_37 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_38'] = BaseAgent.xǁBaseAgentǁrun__mutmut_38 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_39'] = BaseAgent.xǁBaseAgentǁrun__mutmut_39 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_40'] = BaseAgent.xǁBaseAgentǁrun__mutmut_40 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_41'] = BaseAgent.xǁBaseAgentǁrun__mutmut_41 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_42'] = BaseAgent.xǁBaseAgentǁrun__mutmut_42 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_43'] = BaseAgent.xǁBaseAgentǁrun__mutmut_43 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_44'] = BaseAgent.xǁBaseAgentǁrun__mutmut_44 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_45'] = BaseAgent.xǁBaseAgentǁrun__mutmut_45 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_46'] = BaseAgent.xǁBaseAgentǁrun__mutmut_46 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_47'] = BaseAgent.xǁBaseAgentǁrun__mutmut_47 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_48'] = BaseAgent.xǁBaseAgentǁrun__mutmut_48 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_49'] = BaseAgent.xǁBaseAgentǁrun__mutmut_49 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_50'] = BaseAgent.xǁBaseAgentǁrun__mutmut_50 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_51'] = BaseAgent.xǁBaseAgentǁrun__mutmut_51 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_52'] = BaseAgent.xǁBaseAgentǁrun__mutmut_52 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_53'] = BaseAgent.xǁBaseAgentǁrun__mutmut_53 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_54'] = BaseAgent.xǁBaseAgentǁrun__mutmut_54 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_55'] = BaseAgent.xǁBaseAgentǁrun__mutmut_55 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_56'] = BaseAgent.xǁBaseAgentǁrun__mutmut_56 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_57'] = BaseAgent.xǁBaseAgentǁrun__mutmut_57 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_58'] = BaseAgent.xǁBaseAgentǁrun__mutmut_58 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_59'] = BaseAgent.xǁBaseAgentǁrun__mutmut_59 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_60'] = BaseAgent.xǁBaseAgentǁrun__mutmut_60 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_61'] = BaseAgent.xǁBaseAgentǁrun__mutmut_61 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_62'] = BaseAgent.xǁBaseAgentǁrun__mutmut_62 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_63'] = BaseAgent.xǁBaseAgentǁrun__mutmut_63 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_64'] = BaseAgent.xǁBaseAgentǁrun__mutmut_64 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_65'] = BaseAgent.xǁBaseAgentǁrun__mutmut_65 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_66'] = BaseAgent.xǁBaseAgentǁrun__mutmut_66 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_67'] = BaseAgent.xǁBaseAgentǁrun__mutmut_67 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_68'] = BaseAgent.xǁBaseAgentǁrun__mutmut_68 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_69'] = BaseAgent.xǁBaseAgentǁrun__mutmut_69 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_70'] = BaseAgent.xǁBaseAgentǁrun__mutmut_70 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_71'] = BaseAgent.xǁBaseAgentǁrun__mutmut_71 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_72'] = BaseAgent.xǁBaseAgentǁrun__mutmut_72 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_73'] = BaseAgent.xǁBaseAgentǁrun__mutmut_73 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_74'] = BaseAgent.xǁBaseAgentǁrun__mutmut_74 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_75'] = BaseAgent.xǁBaseAgentǁrun__mutmut_75 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_76'] = BaseAgent.xǁBaseAgentǁrun__mutmut_76 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_77'] = BaseAgent.xǁBaseAgentǁrun__mutmut_77 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_78'] = BaseAgent.xǁBaseAgentǁrun__mutmut_78 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_79'] = BaseAgent.xǁBaseAgentǁrun__mutmut_79 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_80'] = BaseAgent.xǁBaseAgentǁrun__mutmut_80 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_81'] = BaseAgent.xǁBaseAgentǁrun__mutmut_81 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_82'] = BaseAgent.xǁBaseAgentǁrun__mutmut_82 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_83'] = BaseAgent.xǁBaseAgentǁrun__mutmut_83 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_84'] = BaseAgent.xǁBaseAgentǁrun__mutmut_84 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_85'] = BaseAgent.xǁBaseAgentǁrun__mutmut_85 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_86'] = BaseAgent.xǁBaseAgentǁrun__mutmut_86 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_87'] = BaseAgent.xǁBaseAgentǁrun__mutmut_87 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_88'] = BaseAgent.xǁBaseAgentǁrun__mutmut_88 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_89'] = BaseAgent.xǁBaseAgentǁrun__mutmut_89 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_90'] = BaseAgent.xǁBaseAgentǁrun__mutmut_90 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_91'] = BaseAgent.xǁBaseAgentǁrun__mutmut_91 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_92'] = BaseAgent.xǁBaseAgentǁrun__mutmut_92 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_93'] = BaseAgent.xǁBaseAgentǁrun__mutmut_93 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_94'] = BaseAgent.xǁBaseAgentǁrun__mutmut_94 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_95'] = BaseAgent.xǁBaseAgentǁrun__mutmut_95 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_96'] = BaseAgent.xǁBaseAgentǁrun__mutmut_96 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_97'] = BaseAgent.xǁBaseAgentǁrun__mutmut_97 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_98'] = BaseAgent.xǁBaseAgentǁrun__mutmut_98 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_99'] = BaseAgent.xǁBaseAgentǁrun__mutmut_99 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_100'] = BaseAgent.xǁBaseAgentǁrun__mutmut_100 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_101'] = BaseAgent.xǁBaseAgentǁrun__mutmut_101 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_102'] = BaseAgent.xǁBaseAgentǁrun__mutmut_102 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_103'] = BaseAgent.xǁBaseAgentǁrun__mutmut_103 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_104'] = BaseAgent.xǁBaseAgentǁrun__mutmut_104 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁrun__mutmut['xǁBaseAgentǁrun__mutmut_105'] = BaseAgent.xǁBaseAgentǁrun__mutmut_105 # type: ignore # mutmut generated

mutants_xǁBaseAgentǁpause__mutmut['_mutmut_orig'] = BaseAgent.xǁBaseAgentǁpause__mutmut_orig # type: ignore # mutmut generated
mutants_xǁBaseAgentǁpause__mutmut['xǁBaseAgentǁpause__mutmut_1'] = BaseAgent.xǁBaseAgentǁpause__mutmut_1 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁpause__mutmut['xǁBaseAgentǁpause__mutmut_2'] = BaseAgent.xǁBaseAgentǁpause__mutmut_2 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁpause__mutmut['xǁBaseAgentǁpause__mutmut_3'] = BaseAgent.xǁBaseAgentǁpause__mutmut_3 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁpause__mutmut['xǁBaseAgentǁpause__mutmut_4'] = BaseAgent.xǁBaseAgentǁpause__mutmut_4 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁpause__mutmut['xǁBaseAgentǁpause__mutmut_5'] = BaseAgent.xǁBaseAgentǁpause__mutmut_5 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁpause__mutmut['xǁBaseAgentǁpause__mutmut_6'] = BaseAgent.xǁBaseAgentǁpause__mutmut_6 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁpause__mutmut['xǁBaseAgentǁpause__mutmut_7'] = BaseAgent.xǁBaseAgentǁpause__mutmut_7 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁpause__mutmut['xǁBaseAgentǁpause__mutmut_8'] = BaseAgent.xǁBaseAgentǁpause__mutmut_8 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁpause__mutmut['xǁBaseAgentǁpause__mutmut_9'] = BaseAgent.xǁBaseAgentǁpause__mutmut_9 # type: ignore # mutmut generated

mutants_xǁBaseAgentǁresume__mutmut['_mutmut_orig'] = BaseAgent.xǁBaseAgentǁresume__mutmut_orig # type: ignore # mutmut generated
mutants_xǁBaseAgentǁresume__mutmut['xǁBaseAgentǁresume__mutmut_1'] = BaseAgent.xǁBaseAgentǁresume__mutmut_1 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁresume__mutmut['xǁBaseAgentǁresume__mutmut_2'] = BaseAgent.xǁBaseAgentǁresume__mutmut_2 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁresume__mutmut['xǁBaseAgentǁresume__mutmut_3'] = BaseAgent.xǁBaseAgentǁresume__mutmut_3 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁresume__mutmut['xǁBaseAgentǁresume__mutmut_4'] = BaseAgent.xǁBaseAgentǁresume__mutmut_4 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁresume__mutmut['xǁBaseAgentǁresume__mutmut_5'] = BaseAgent.xǁBaseAgentǁresume__mutmut_5 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁresume__mutmut['xǁBaseAgentǁresume__mutmut_6'] = BaseAgent.xǁBaseAgentǁresume__mutmut_6 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁresume__mutmut['xǁBaseAgentǁresume__mutmut_7'] = BaseAgent.xǁBaseAgentǁresume__mutmut_7 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁresume__mutmut['xǁBaseAgentǁresume__mutmut_8'] = BaseAgent.xǁBaseAgentǁresume__mutmut_8 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁresume__mutmut['xǁBaseAgentǁresume__mutmut_9'] = BaseAgent.xǁBaseAgentǁresume__mutmut_9 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁresume__mutmut['xǁBaseAgentǁresume__mutmut_10'] = BaseAgent.xǁBaseAgentǁresume__mutmut_10 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁresume__mutmut['xǁBaseAgentǁresume__mutmut_11'] = BaseAgent.xǁBaseAgentǁresume__mutmut_11 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁresume__mutmut['xǁBaseAgentǁresume__mutmut_12'] = BaseAgent.xǁBaseAgentǁresume__mutmut_12 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁresume__mutmut['xǁBaseAgentǁresume__mutmut_13'] = BaseAgent.xǁBaseAgentǁresume__mutmut_13 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁresume__mutmut['xǁBaseAgentǁresume__mutmut_14'] = BaseAgent.xǁBaseAgentǁresume__mutmut_14 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁresume__mutmut['xǁBaseAgentǁresume__mutmut_15'] = BaseAgent.xǁBaseAgentǁresume__mutmut_15 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁresume__mutmut['xǁBaseAgentǁresume__mutmut_16'] = BaseAgent.xǁBaseAgentǁresume__mutmut_16 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁresume__mutmut['xǁBaseAgentǁresume__mutmut_17'] = BaseAgent.xǁBaseAgentǁresume__mutmut_17 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁresume__mutmut['xǁBaseAgentǁresume__mutmut_18'] = BaseAgent.xǁBaseAgentǁresume__mutmut_18 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁresume__mutmut['xǁBaseAgentǁresume__mutmut_19'] = BaseAgent.xǁBaseAgentǁresume__mutmut_19 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁresume__mutmut['xǁBaseAgentǁresume__mutmut_20'] = BaseAgent.xǁBaseAgentǁresume__mutmut_20 # type: ignore # mutmut generated

mutants_xǁBaseAgentǁterminate__mutmut['_mutmut_orig'] = BaseAgent.xǁBaseAgentǁterminate__mutmut_orig # type: ignore # mutmut generated
mutants_xǁBaseAgentǁterminate__mutmut['xǁBaseAgentǁterminate__mutmut_1'] = BaseAgent.xǁBaseAgentǁterminate__mutmut_1 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁterminate__mutmut['xǁBaseAgentǁterminate__mutmut_2'] = BaseAgent.xǁBaseAgentǁterminate__mutmut_2 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁterminate__mutmut['xǁBaseAgentǁterminate__mutmut_3'] = BaseAgent.xǁBaseAgentǁterminate__mutmut_3 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁterminate__mutmut['xǁBaseAgentǁterminate__mutmut_4'] = BaseAgent.xǁBaseAgentǁterminate__mutmut_4 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁterminate__mutmut['xǁBaseAgentǁterminate__mutmut_5'] = BaseAgent.xǁBaseAgentǁterminate__mutmut_5 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁterminate__mutmut['xǁBaseAgentǁterminate__mutmut_6'] = BaseAgent.xǁBaseAgentǁterminate__mutmut_6 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁterminate__mutmut['xǁBaseAgentǁterminate__mutmut_7'] = BaseAgent.xǁBaseAgentǁterminate__mutmut_7 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁterminate__mutmut['xǁBaseAgentǁterminate__mutmut_8'] = BaseAgent.xǁBaseAgentǁterminate__mutmut_8 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁterminate__mutmut['xǁBaseAgentǁterminate__mutmut_9'] = BaseAgent.xǁBaseAgentǁterminate__mutmut_9 # type: ignore # mutmut generated

mutants_xǁBaseAgentǁsend_message__mutmut['_mutmut_orig'] = BaseAgent.xǁBaseAgentǁsend_message__mutmut_orig # type: ignore # mutmut generated
mutants_xǁBaseAgentǁsend_message__mutmut['xǁBaseAgentǁsend_message__mutmut_1'] = BaseAgent.xǁBaseAgentǁsend_message__mutmut_1 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁsend_message__mutmut['xǁBaseAgentǁsend_message__mutmut_2'] = BaseAgent.xǁBaseAgentǁsend_message__mutmut_2 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁsend_message__mutmut['xǁBaseAgentǁsend_message__mutmut_3'] = BaseAgent.xǁBaseAgentǁsend_message__mutmut_3 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁsend_message__mutmut['xǁBaseAgentǁsend_message__mutmut_4'] = BaseAgent.xǁBaseAgentǁsend_message__mutmut_4 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁsend_message__mutmut['xǁBaseAgentǁsend_message__mutmut_5'] = BaseAgent.xǁBaseAgentǁsend_message__mutmut_5 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁsend_message__mutmut['xǁBaseAgentǁsend_message__mutmut_6'] = BaseAgent.xǁBaseAgentǁsend_message__mutmut_6 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁsend_message__mutmut['xǁBaseAgentǁsend_message__mutmut_7'] = BaseAgent.xǁBaseAgentǁsend_message__mutmut_7 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁsend_message__mutmut['xǁBaseAgentǁsend_message__mutmut_8'] = BaseAgent.xǁBaseAgentǁsend_message__mutmut_8 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁsend_message__mutmut['xǁBaseAgentǁsend_message__mutmut_9'] = BaseAgent.xǁBaseAgentǁsend_message__mutmut_9 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁsend_message__mutmut['xǁBaseAgentǁsend_message__mutmut_10'] = BaseAgent.xǁBaseAgentǁsend_message__mutmut_10 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁsend_message__mutmut['xǁBaseAgentǁsend_message__mutmut_11'] = BaseAgent.xǁBaseAgentǁsend_message__mutmut_11 # type: ignore # mutmut generated

mutants_xǁBaseAgentǁreceive_message__mutmut['_mutmut_orig'] = BaseAgent.xǁBaseAgentǁreceive_message__mutmut_orig # type: ignore # mutmut generated
mutants_xǁBaseAgentǁreceive_message__mutmut['xǁBaseAgentǁreceive_message__mutmut_1'] = BaseAgent.xǁBaseAgentǁreceive_message__mutmut_1 # type: ignore # mutmut generated

mutants_xǁBaseAgentǁget_pending_messages__mutmut['_mutmut_orig'] = BaseAgent.xǁBaseAgentǁget_pending_messages__mutmut_orig # type: ignore # mutmut generated
mutants_xǁBaseAgentǁget_pending_messages__mutmut['xǁBaseAgentǁget_pending_messages__mutmut_1'] = BaseAgent.xǁBaseAgentǁget_pending_messages__mutmut_1 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁget_pending_messages__mutmut['xǁBaseAgentǁget_pending_messages__mutmut_2'] = BaseAgent.xǁBaseAgentǁget_pending_messages__mutmut_2 # type: ignore # mutmut generated

mutants_xǁBaseAgentǁset_context__mutmut['_mutmut_orig'] = BaseAgent.xǁBaseAgentǁset_context__mutmut_orig # type: ignore # mutmut generated
mutants_xǁBaseAgentǁset_context__mutmut['xǁBaseAgentǁset_context__mutmut_1'] = BaseAgent.xǁBaseAgentǁset_context__mutmut_1 # type: ignore # mutmut generated

mutants_xǁBaseAgentǁget_context__mutmut['_mutmut_orig'] = BaseAgent.xǁBaseAgentǁget_context__mutmut_orig # type: ignore # mutmut generated
mutants_xǁBaseAgentǁget_context__mutmut['xǁBaseAgentǁget_context__mutmut_1'] = BaseAgent.xǁBaseAgentǁget_context__mutmut_1 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁget_context__mutmut['xǁBaseAgentǁget_context__mutmut_2'] = BaseAgent.xǁBaseAgentǁget_context__mutmut_2 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁget_context__mutmut['xǁBaseAgentǁget_context__mutmut_3'] = BaseAgent.xǁBaseAgentǁget_context__mutmut_3 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁget_context__mutmut['xǁBaseAgentǁget_context__mutmut_4'] = BaseAgent.xǁBaseAgentǁget_context__mutmut_4 # type: ignore # mutmut generated

mutants_xǁBaseAgentǁ_should_stop__mutmut['_mutmut_orig'] = BaseAgent.xǁBaseAgentǁ_should_stop__mutmut_orig # type: ignore # mutmut generated
mutants_xǁBaseAgentǁ_should_stop__mutmut['xǁBaseAgentǁ_should_stop__mutmut_1'] = BaseAgent.xǁBaseAgentǁ_should_stop__mutmut_1 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁ_should_stop__mutmut['xǁBaseAgentǁ_should_stop__mutmut_2'] = BaseAgent.xǁBaseAgentǁ_should_stop__mutmut_2 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁ_should_stop__mutmut['xǁBaseAgentǁ_should_stop__mutmut_3'] = BaseAgent.xǁBaseAgentǁ_should_stop__mutmut_3 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁ_should_stop__mutmut['xǁBaseAgentǁ_should_stop__mutmut_4'] = BaseAgent.xǁBaseAgentǁ_should_stop__mutmut_4 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁ_should_stop__mutmut['xǁBaseAgentǁ_should_stop__mutmut_5'] = BaseAgent.xǁBaseAgentǁ_should_stop__mutmut_5 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁ_should_stop__mutmut['xǁBaseAgentǁ_should_stop__mutmut_6'] = BaseAgent.xǁBaseAgentǁ_should_stop__mutmut_6 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁ_should_stop__mutmut['xǁBaseAgentǁ_should_stop__mutmut_7'] = BaseAgent.xǁBaseAgentǁ_should_stop__mutmut_7 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁ_should_stop__mutmut['xǁBaseAgentǁ_should_stop__mutmut_8'] = BaseAgent.xǁBaseAgentǁ_should_stop__mutmut_8 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁ_should_stop__mutmut['xǁBaseAgentǁ_should_stop__mutmut_9'] = BaseAgent.xǁBaseAgentǁ_should_stop__mutmut_9 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁ_should_stop__mutmut['xǁBaseAgentǁ_should_stop__mutmut_10'] = BaseAgent.xǁBaseAgentǁ_should_stop__mutmut_10 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁ_should_stop__mutmut['xǁBaseAgentǁ_should_stop__mutmut_11'] = BaseAgent.xǁBaseAgentǁ_should_stop__mutmut_11 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁ_should_stop__mutmut['xǁBaseAgentǁ_should_stop__mutmut_12'] = BaseAgent.xǁBaseAgentǁ_should_stop__mutmut_12 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁ_should_stop__mutmut['xǁBaseAgentǁ_should_stop__mutmut_13'] = BaseAgent.xǁBaseAgentǁ_should_stop__mutmut_13 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁ_should_stop__mutmut['xǁBaseAgentǁ_should_stop__mutmut_14'] = BaseAgent.xǁBaseAgentǁ_should_stop__mutmut_14 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁ_should_stop__mutmut['xǁBaseAgentǁ_should_stop__mutmut_15'] = BaseAgent.xǁBaseAgentǁ_should_stop__mutmut_15 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁ_should_stop__mutmut['xǁBaseAgentǁ_should_stop__mutmut_16'] = BaseAgent.xǁBaseAgentǁ_should_stop__mutmut_16 # type: ignore # mutmut generated

mutants_xǁBaseAgentǁget_status__mutmut['_mutmut_orig'] = BaseAgent.xǁBaseAgentǁget_status__mutmut_orig # type: ignore # mutmut generated
mutants_xǁBaseAgentǁget_status__mutmut['xǁBaseAgentǁget_status__mutmut_1'] = BaseAgent.xǁBaseAgentǁget_status__mutmut_1 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁget_status__mutmut['xǁBaseAgentǁget_status__mutmut_2'] = BaseAgent.xǁBaseAgentǁget_status__mutmut_2 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁget_status__mutmut['xǁBaseAgentǁget_status__mutmut_3'] = BaseAgent.xǁBaseAgentǁget_status__mutmut_3 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁget_status__mutmut['xǁBaseAgentǁget_status__mutmut_4'] = BaseAgent.xǁBaseAgentǁget_status__mutmut_4 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁget_status__mutmut['xǁBaseAgentǁget_status__mutmut_5'] = BaseAgent.xǁBaseAgentǁget_status__mutmut_5 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁget_status__mutmut['xǁBaseAgentǁget_status__mutmut_6'] = BaseAgent.xǁBaseAgentǁget_status__mutmut_6 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁget_status__mutmut['xǁBaseAgentǁget_status__mutmut_7'] = BaseAgent.xǁBaseAgentǁget_status__mutmut_7 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁget_status__mutmut['xǁBaseAgentǁget_status__mutmut_8'] = BaseAgent.xǁBaseAgentǁget_status__mutmut_8 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁget_status__mutmut['xǁBaseAgentǁget_status__mutmut_9'] = BaseAgent.xǁBaseAgentǁget_status__mutmut_9 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁget_status__mutmut['xǁBaseAgentǁget_status__mutmut_10'] = BaseAgent.xǁBaseAgentǁget_status__mutmut_10 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁget_status__mutmut['xǁBaseAgentǁget_status__mutmut_11'] = BaseAgent.xǁBaseAgentǁget_status__mutmut_11 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁget_status__mutmut['xǁBaseAgentǁget_status__mutmut_12'] = BaseAgent.xǁBaseAgentǁget_status__mutmut_12 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁget_status__mutmut['xǁBaseAgentǁget_status__mutmut_13'] = BaseAgent.xǁBaseAgentǁget_status__mutmut_13 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁget_status__mutmut['xǁBaseAgentǁget_status__mutmut_14'] = BaseAgent.xǁBaseAgentǁget_status__mutmut_14 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁget_status__mutmut['xǁBaseAgentǁget_status__mutmut_15'] = BaseAgent.xǁBaseAgentǁget_status__mutmut_15 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁget_status__mutmut['xǁBaseAgentǁget_status__mutmut_16'] = BaseAgent.xǁBaseAgentǁget_status__mutmut_16 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁget_status__mutmut['xǁBaseAgentǁget_status__mutmut_17'] = BaseAgent.xǁBaseAgentǁget_status__mutmut_17 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁget_status__mutmut['xǁBaseAgentǁget_status__mutmut_18'] = BaseAgent.xǁBaseAgentǁget_status__mutmut_18 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁget_status__mutmut['xǁBaseAgentǁget_status__mutmut_19'] = BaseAgent.xǁBaseAgentǁget_status__mutmut_19 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁget_status__mutmut['xǁBaseAgentǁget_status__mutmut_20'] = BaseAgent.xǁBaseAgentǁget_status__mutmut_20 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁget_status__mutmut['xǁBaseAgentǁget_status__mutmut_21'] = BaseAgent.xǁBaseAgentǁget_status__mutmut_21 # type: ignore # mutmut generated
mutants_xǁBaseAgentǁget_status__mutmut['xǁBaseAgentǁget_status__mutmut_22'] = BaseAgent.xǁBaseAgentǁget_status__mutmut_22 # type: ignore # mutmut generated
