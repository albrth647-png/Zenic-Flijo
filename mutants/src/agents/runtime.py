"""Agent Runtime — Lifecycle manager for agent instances.

Spawns, monitors, and terminates agents. Manages execution pools,
health checks, and resource limits. Integrates with the orbital context
for agent state synchronization.
"""

from __future__ import annotations

import threading
import time
from collections import defaultdict
from dataclasses import dataclass
from typing import Any

from src.agents.base import AgentConfig, AgentState, BaseAgent
from src.utils.logger import get_logger

logger = get_logger("agent.runtime")


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class RuntimeStats:
    """Aggregate statistics for the agent runtime."""

    total_spawned: int = 0
    total_terminated: int = 0
    total_errors: int = 0
    active_count: int = 0
    peak_active: int = 0
    total_iterations: int = 0
mutants_xǁAgentRuntimeǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁAgentRuntimeǁget_instance__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAgentRuntimeǁreset_instance__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAgentRuntimeǁspawn__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAgentRuntimeǁterminate_agent__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAgentRuntimeǁpause_agent__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAgentRuntimeǁresume_agent__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAgentRuntimeǁget_agent__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAgentRuntimeǁlist_agents__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAgentRuntimeǁget_agent_status__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAgentRuntimeǁroute_message__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAgentRuntimeǁbroadcast__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAgentRuntimeǁstart_heartbeat__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAgentRuntimeǁstop_heartbeat__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAgentRuntimeǁ_heartbeat_loop__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAgentRuntimeǁ_check_agents_health__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAgentRuntimeǁregister_hook__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAgentRuntimeǁ_fire_hook__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAgentRuntimeǁget_stats__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAgentRuntimeǁ_agents_by_state__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAgentRuntimeǁshutdown__mutmut: MutantDict = {}  # type: ignore


class AgentRuntime:
    """Centralized runtime for managing agent lifecycles.

    Responsibilities:
    - Spawn and register agent instances
    - Monitor agent health (heartbeat checks)
    - Enforce resource limits (max concurrent agents, timeouts)
    - Provide agent discovery and lookup
    - Thread-safe agent registry with lifecycle hooks

    Usage:
        runtime = AgentRuntime.get_instance()
        agent = runtime.spawn(MyAgent, config)
        status = runtime.get_agent_status(agent.agent_id)
        runtime.terminate_agent(agent.agent_id)
    """

    _instance: AgentRuntime | None = None
    _lock = threading.Lock()

    @_mutmut_mutated(mutants_xǁAgentRuntimeǁ__init____mutmut)
    def __init__(self, max_agents: int = 50, heartbeat_interval: float = 30.0) -> None:
        self._agents: dict[str, BaseAgent] = {}
        self._agent_lock = threading.Lock()
        self._max_agents = max_agents
        self._heartbeat_interval = heartbeat_interval
        self._stats = RuntimeStats()
        self._hooks: dict[str, list] = defaultdict(list)
        self._running = False
        self._heartbeat_thread: threading.Thread | None = None

    def xǁAgentRuntimeǁ__init____mutmut_orig(self, max_agents: int = 50, heartbeat_interval: float = 30.0) -> None:
        self._agents: dict[str, BaseAgent] = {}
        self._agent_lock = threading.Lock()
        self._max_agents = max_agents
        self._heartbeat_interval = heartbeat_interval
        self._stats = RuntimeStats()
        self._hooks: dict[str, list] = defaultdict(list)
        self._running = False
        self._heartbeat_thread: threading.Thread | None = None

    def xǁAgentRuntimeǁ__init____mutmut_1(self, max_agents: int = 51, heartbeat_interval: float = 30.0) -> None:
        self._agents: dict[str, BaseAgent] = {}
        self._agent_lock = threading.Lock()
        self._max_agents = max_agents
        self._heartbeat_interval = heartbeat_interval
        self._stats = RuntimeStats()
        self._hooks: dict[str, list] = defaultdict(list)
        self._running = False
        self._heartbeat_thread: threading.Thread | None = None

    def xǁAgentRuntimeǁ__init____mutmut_2(self, max_agents: int = 50, heartbeat_interval: float = 31.0) -> None:
        self._agents: dict[str, BaseAgent] = {}
        self._agent_lock = threading.Lock()
        self._max_agents = max_agents
        self._heartbeat_interval = heartbeat_interval
        self._stats = RuntimeStats()
        self._hooks: dict[str, list] = defaultdict(list)
        self._running = False
        self._heartbeat_thread: threading.Thread | None = None

    def xǁAgentRuntimeǁ__init____mutmut_3(self, max_agents: int = 50, heartbeat_interval: float = 30.0) -> None:
        self._agents: dict[str, BaseAgent] = None
        self._agent_lock = threading.Lock()
        self._max_agents = max_agents
        self._heartbeat_interval = heartbeat_interval
        self._stats = RuntimeStats()
        self._hooks: dict[str, list] = defaultdict(list)
        self._running = False
        self._heartbeat_thread: threading.Thread | None = None

    def xǁAgentRuntimeǁ__init____mutmut_4(self, max_agents: int = 50, heartbeat_interval: float = 30.0) -> None:
        self._agents: dict[str, BaseAgent] = {}
        self._agent_lock = None
        self._max_agents = max_agents
        self._heartbeat_interval = heartbeat_interval
        self._stats = RuntimeStats()
        self._hooks: dict[str, list] = defaultdict(list)
        self._running = False
        self._heartbeat_thread: threading.Thread | None = None

    def xǁAgentRuntimeǁ__init____mutmut_5(self, max_agents: int = 50, heartbeat_interval: float = 30.0) -> None:
        self._agents: dict[str, BaseAgent] = {}
        self._agent_lock = threading.Lock()
        self._max_agents = None
        self._heartbeat_interval = heartbeat_interval
        self._stats = RuntimeStats()
        self._hooks: dict[str, list] = defaultdict(list)
        self._running = False
        self._heartbeat_thread: threading.Thread | None = None

    def xǁAgentRuntimeǁ__init____mutmut_6(self, max_agents: int = 50, heartbeat_interval: float = 30.0) -> None:
        self._agents: dict[str, BaseAgent] = {}
        self._agent_lock = threading.Lock()
        self._max_agents = max_agents
        self._heartbeat_interval = None
        self._stats = RuntimeStats()
        self._hooks: dict[str, list] = defaultdict(list)
        self._running = False
        self._heartbeat_thread: threading.Thread | None = None

    def xǁAgentRuntimeǁ__init____mutmut_7(self, max_agents: int = 50, heartbeat_interval: float = 30.0) -> None:
        self._agents: dict[str, BaseAgent] = {}
        self._agent_lock = threading.Lock()
        self._max_agents = max_agents
        self._heartbeat_interval = heartbeat_interval
        self._stats = None
        self._hooks: dict[str, list] = defaultdict(list)
        self._running = False
        self._heartbeat_thread: threading.Thread | None = None

    def xǁAgentRuntimeǁ__init____mutmut_8(self, max_agents: int = 50, heartbeat_interval: float = 30.0) -> None:
        self._agents: dict[str, BaseAgent] = {}
        self._agent_lock = threading.Lock()
        self._max_agents = max_agents
        self._heartbeat_interval = heartbeat_interval
        self._stats = RuntimeStats()
        self._hooks: dict[str, list] = None
        self._running = False
        self._heartbeat_thread: threading.Thread | None = None

    def xǁAgentRuntimeǁ__init____mutmut_9(self, max_agents: int = 50, heartbeat_interval: float = 30.0) -> None:
        self._agents: dict[str, BaseAgent] = {}
        self._agent_lock = threading.Lock()
        self._max_agents = max_agents
        self._heartbeat_interval = heartbeat_interval
        self._stats = RuntimeStats()
        self._hooks: dict[str, list] = defaultdict(None)
        self._running = False
        self._heartbeat_thread: threading.Thread | None = None

    def xǁAgentRuntimeǁ__init____mutmut_10(self, max_agents: int = 50, heartbeat_interval: float = 30.0) -> None:
        self._agents: dict[str, BaseAgent] = {}
        self._agent_lock = threading.Lock()
        self._max_agents = max_agents
        self._heartbeat_interval = heartbeat_interval
        self._stats = RuntimeStats()
        self._hooks: dict[str, list] = defaultdict(list)
        self._running = None
        self._heartbeat_thread: threading.Thread | None = None

    def xǁAgentRuntimeǁ__init____mutmut_11(self, max_agents: int = 50, heartbeat_interval: float = 30.0) -> None:
        self._agents: dict[str, BaseAgent] = {}
        self._agent_lock = threading.Lock()
        self._max_agents = max_agents
        self._heartbeat_interval = heartbeat_interval
        self._stats = RuntimeStats()
        self._hooks: dict[str, list] = defaultdict(list)
        self._running = True
        self._heartbeat_thread: threading.Thread | None = None

    def xǁAgentRuntimeǁ__init____mutmut_12(self, max_agents: int = 50, heartbeat_interval: float = 30.0) -> None:
        self._agents: dict[str, BaseAgent] = {}
        self._agent_lock = threading.Lock()
        self._max_agents = max_agents
        self._heartbeat_interval = heartbeat_interval
        self._stats = RuntimeStats()
        self._hooks: dict[str, list] = defaultdict(list)
        self._running = False
        self._heartbeat_thread: threading.Thread | None = ""

    @classmethod
    @_mutmut_mutated(mutants_xǁAgentRuntimeǁget_instance__mutmut, is_classmethod = True)
    def get_instance(cls, **kwargs: Any) -> AgentRuntime:
        """Get or create the singleton AgentRuntime."""
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = cls(**kwargs)
        return cls._instance

    @classmethod
    def xǁAgentRuntimeǁget_instance__mutmut_orig(cls, **kwargs: Any) -> AgentRuntime:
        """Get or create the singleton AgentRuntime."""
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = cls(**kwargs)
        return cls._instance

    @classmethod
    def xǁAgentRuntimeǁget_instance__mutmut_1(cls, **kwargs: Any) -> AgentRuntime:
        """Get or create the singleton AgentRuntime."""
        if cls._instance is not None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = cls(**kwargs)
        return cls._instance

    @classmethod
    def xǁAgentRuntimeǁget_instance__mutmut_2(cls, **kwargs: Any) -> AgentRuntime:
        """Get or create the singleton AgentRuntime."""
        if cls._instance is None:
            with cls._lock:
                if cls._instance is not None:
                    cls._instance = cls(**kwargs)
        return cls._instance

    @classmethod
    def xǁAgentRuntimeǁget_instance__mutmut_3(cls, **kwargs: Any) -> AgentRuntime:
        """Get or create the singleton AgentRuntime."""
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = None
        return cls._instance

    @classmethod
    @_mutmut_mutated(mutants_xǁAgentRuntimeǁreset_instance__mutmut, is_classmethod = True)
    def reset_instance(cls) -> None:
        """Reset the singleton (for testing)."""
        with cls._lock:
            if cls._instance is not None:
                cls._instance.shutdown()
            cls._instance = None

    @classmethod
    def xǁAgentRuntimeǁreset_instance__mutmut_orig(cls) -> None:
        """Reset the singleton (for testing)."""
        with cls._lock:
            if cls._instance is not None:
                cls._instance.shutdown()
            cls._instance = None

    @classmethod
    def xǁAgentRuntimeǁreset_instance__mutmut_1(cls) -> None:
        """Reset the singleton (for testing)."""
        with cls._lock:
            if cls._instance is None:
                cls._instance.shutdown()
            cls._instance = None

    @classmethod
    def xǁAgentRuntimeǁreset_instance__mutmut_2(cls) -> None:
        """Reset the singleton (for testing)."""
        with cls._lock:
            if cls._instance is not None:
                cls._instance.shutdown()
            cls._instance = ""

    # ── Lifecycle ───────────────────────────────────────────

    @_mutmut_mutated(mutants_xǁAgentRuntimeǁspawn__mutmut)
    def spawn(
        self,
        agent_class: type[BaseAgent],
        config: AgentConfig | None = None,
        parent_id: str | None = None,
    ) -> BaseAgent:
        """Spawn a new agent instance and register it in the runtime.

        Args:
            agent_class: The concrete BaseAgent subclass to instantiate.
            config: Agent configuration. If None, a default is created.
            parent_id: Optional parent agent ID for hierarchy.

        Returns:
            The newly created agent instance.

        Raises:
            RuntimeError: If max agent limit is reached.
        """
        with self._agent_lock:
            if len(self._agents) >= self._max_agents:
                msg = f"Max agent limit reached ({self._max_agents})"
                raise RuntimeError(msg)

            if config is None:
                config = AgentConfig()

            agent = agent_class(config)
            agent._parent_id = parent_id

            # Register parent-child relationship
            if parent_id and parent_id in self._agents:
                self._agents[parent_id]._child_ids.append(agent.agent_id)

            self._agents[agent.agent_id] = agent
            self._stats.total_spawned += 1
            self._stats.active_count = len(self._agents)
            self._stats.peak_active = max(self._stats.peak_active, self._stats.active_count)

            self._fire_hook("on_spawn", agent)
            logger.info("Agent spawned: %s (%s)", agent.name, agent.agent_id)
            return agent

    # ── Lifecycle ───────────────────────────────────────────

    def xǁAgentRuntimeǁspawn__mutmut_orig(
        self,
        agent_class: type[BaseAgent],
        config: AgentConfig | None = None,
        parent_id: str | None = None,
    ) -> BaseAgent:
        """Spawn a new agent instance and register it in the runtime.

        Args:
            agent_class: The concrete BaseAgent subclass to instantiate.
            config: Agent configuration. If None, a default is created.
            parent_id: Optional parent agent ID for hierarchy.

        Returns:
            The newly created agent instance.

        Raises:
            RuntimeError: If max agent limit is reached.
        """
        with self._agent_lock:
            if len(self._agents) >= self._max_agents:
                msg = f"Max agent limit reached ({self._max_agents})"
                raise RuntimeError(msg)

            if config is None:
                config = AgentConfig()

            agent = agent_class(config)
            agent._parent_id = parent_id

            # Register parent-child relationship
            if parent_id and parent_id in self._agents:
                self._agents[parent_id]._child_ids.append(agent.agent_id)

            self._agents[agent.agent_id] = agent
            self._stats.total_spawned += 1
            self._stats.active_count = len(self._agents)
            self._stats.peak_active = max(self._stats.peak_active, self._stats.active_count)

            self._fire_hook("on_spawn", agent)
            logger.info("Agent spawned: %s (%s)", agent.name, agent.agent_id)
            return agent

    # ── Lifecycle ───────────────────────────────────────────

    def xǁAgentRuntimeǁspawn__mutmut_1(
        self,
        agent_class: type[BaseAgent],
        config: AgentConfig | None = None,
        parent_id: str | None = None,
    ) -> BaseAgent:
        """Spawn a new agent instance and register it in the runtime.

        Args:
            agent_class: The concrete BaseAgent subclass to instantiate.
            config: Agent configuration. If None, a default is created.
            parent_id: Optional parent agent ID for hierarchy.

        Returns:
            The newly created agent instance.

        Raises:
            RuntimeError: If max agent limit is reached.
        """
        with self._agent_lock:
            if len(self._agents) > self._max_agents:
                msg = f"Max agent limit reached ({self._max_agents})"
                raise RuntimeError(msg)

            if config is None:
                config = AgentConfig()

            agent = agent_class(config)
            agent._parent_id = parent_id

            # Register parent-child relationship
            if parent_id and parent_id in self._agents:
                self._agents[parent_id]._child_ids.append(agent.agent_id)

            self._agents[agent.agent_id] = agent
            self._stats.total_spawned += 1
            self._stats.active_count = len(self._agents)
            self._stats.peak_active = max(self._stats.peak_active, self._stats.active_count)

            self._fire_hook("on_spawn", agent)
            logger.info("Agent spawned: %s (%s)", agent.name, agent.agent_id)
            return agent

    # ── Lifecycle ───────────────────────────────────────────

    def xǁAgentRuntimeǁspawn__mutmut_2(
        self,
        agent_class: type[BaseAgent],
        config: AgentConfig | None = None,
        parent_id: str | None = None,
    ) -> BaseAgent:
        """Spawn a new agent instance and register it in the runtime.

        Args:
            agent_class: The concrete BaseAgent subclass to instantiate.
            config: Agent configuration. If None, a default is created.
            parent_id: Optional parent agent ID for hierarchy.

        Returns:
            The newly created agent instance.

        Raises:
            RuntimeError: If max agent limit is reached.
        """
        with self._agent_lock:
            if len(self._agents) >= self._max_agents:
                msg = None
                raise RuntimeError(msg)

            if config is None:
                config = AgentConfig()

            agent = agent_class(config)
            agent._parent_id = parent_id

            # Register parent-child relationship
            if parent_id and parent_id in self._agents:
                self._agents[parent_id]._child_ids.append(agent.agent_id)

            self._agents[agent.agent_id] = agent
            self._stats.total_spawned += 1
            self._stats.active_count = len(self._agents)
            self._stats.peak_active = max(self._stats.peak_active, self._stats.active_count)

            self._fire_hook("on_spawn", agent)
            logger.info("Agent spawned: %s (%s)", agent.name, agent.agent_id)
            return agent

    # ── Lifecycle ───────────────────────────────────────────

    def xǁAgentRuntimeǁspawn__mutmut_3(
        self,
        agent_class: type[BaseAgent],
        config: AgentConfig | None = None,
        parent_id: str | None = None,
    ) -> BaseAgent:
        """Spawn a new agent instance and register it in the runtime.

        Args:
            agent_class: The concrete BaseAgent subclass to instantiate.
            config: Agent configuration. If None, a default is created.
            parent_id: Optional parent agent ID for hierarchy.

        Returns:
            The newly created agent instance.

        Raises:
            RuntimeError: If max agent limit is reached.
        """
        with self._agent_lock:
            if len(self._agents) >= self._max_agents:
                msg = f"Max agent limit reached ({self._max_agents})"
                raise RuntimeError(None)

            if config is None:
                config = AgentConfig()

            agent = agent_class(config)
            agent._parent_id = parent_id

            # Register parent-child relationship
            if parent_id and parent_id in self._agents:
                self._agents[parent_id]._child_ids.append(agent.agent_id)

            self._agents[agent.agent_id] = agent
            self._stats.total_spawned += 1
            self._stats.active_count = len(self._agents)
            self._stats.peak_active = max(self._stats.peak_active, self._stats.active_count)

            self._fire_hook("on_spawn", agent)
            logger.info("Agent spawned: %s (%s)", agent.name, agent.agent_id)
            return agent

    # ── Lifecycle ───────────────────────────────────────────

    def xǁAgentRuntimeǁspawn__mutmut_4(
        self,
        agent_class: type[BaseAgent],
        config: AgentConfig | None = None,
        parent_id: str | None = None,
    ) -> BaseAgent:
        """Spawn a new agent instance and register it in the runtime.

        Args:
            agent_class: The concrete BaseAgent subclass to instantiate.
            config: Agent configuration. If None, a default is created.
            parent_id: Optional parent agent ID for hierarchy.

        Returns:
            The newly created agent instance.

        Raises:
            RuntimeError: If max agent limit is reached.
        """
        with self._agent_lock:
            if len(self._agents) >= self._max_agents:
                msg = f"Max agent limit reached ({self._max_agents})"
                raise RuntimeError(msg)

            if config is not None:
                config = AgentConfig()

            agent = agent_class(config)
            agent._parent_id = parent_id

            # Register parent-child relationship
            if parent_id and parent_id in self._agents:
                self._agents[parent_id]._child_ids.append(agent.agent_id)

            self._agents[agent.agent_id] = agent
            self._stats.total_spawned += 1
            self._stats.active_count = len(self._agents)
            self._stats.peak_active = max(self._stats.peak_active, self._stats.active_count)

            self._fire_hook("on_spawn", agent)
            logger.info("Agent spawned: %s (%s)", agent.name, agent.agent_id)
            return agent

    # ── Lifecycle ───────────────────────────────────────────

    def xǁAgentRuntimeǁspawn__mutmut_5(
        self,
        agent_class: type[BaseAgent],
        config: AgentConfig | None = None,
        parent_id: str | None = None,
    ) -> BaseAgent:
        """Spawn a new agent instance and register it in the runtime.

        Args:
            agent_class: The concrete BaseAgent subclass to instantiate.
            config: Agent configuration. If None, a default is created.
            parent_id: Optional parent agent ID for hierarchy.

        Returns:
            The newly created agent instance.

        Raises:
            RuntimeError: If max agent limit is reached.
        """
        with self._agent_lock:
            if len(self._agents) >= self._max_agents:
                msg = f"Max agent limit reached ({self._max_agents})"
                raise RuntimeError(msg)

            if config is None:
                config = None

            agent = agent_class(config)
            agent._parent_id = parent_id

            # Register parent-child relationship
            if parent_id and parent_id in self._agents:
                self._agents[parent_id]._child_ids.append(agent.agent_id)

            self._agents[agent.agent_id] = agent
            self._stats.total_spawned += 1
            self._stats.active_count = len(self._agents)
            self._stats.peak_active = max(self._stats.peak_active, self._stats.active_count)

            self._fire_hook("on_spawn", agent)
            logger.info("Agent spawned: %s (%s)", agent.name, agent.agent_id)
            return agent

    # ── Lifecycle ───────────────────────────────────────────

    def xǁAgentRuntimeǁspawn__mutmut_6(
        self,
        agent_class: type[BaseAgent],
        config: AgentConfig | None = None,
        parent_id: str | None = None,
    ) -> BaseAgent:
        """Spawn a new agent instance and register it in the runtime.

        Args:
            agent_class: The concrete BaseAgent subclass to instantiate.
            config: Agent configuration. If None, a default is created.
            parent_id: Optional parent agent ID for hierarchy.

        Returns:
            The newly created agent instance.

        Raises:
            RuntimeError: If max agent limit is reached.
        """
        with self._agent_lock:
            if len(self._agents) >= self._max_agents:
                msg = f"Max agent limit reached ({self._max_agents})"
                raise RuntimeError(msg)

            if config is None:
                config = AgentConfig()

            agent = None
            agent._parent_id = parent_id

            # Register parent-child relationship
            if parent_id and parent_id in self._agents:
                self._agents[parent_id]._child_ids.append(agent.agent_id)

            self._agents[agent.agent_id] = agent
            self._stats.total_spawned += 1
            self._stats.active_count = len(self._agents)
            self._stats.peak_active = max(self._stats.peak_active, self._stats.active_count)

            self._fire_hook("on_spawn", agent)
            logger.info("Agent spawned: %s (%s)", agent.name, agent.agent_id)
            return agent

    # ── Lifecycle ───────────────────────────────────────────

    def xǁAgentRuntimeǁspawn__mutmut_7(
        self,
        agent_class: type[BaseAgent],
        config: AgentConfig | None = None,
        parent_id: str | None = None,
    ) -> BaseAgent:
        """Spawn a new agent instance and register it in the runtime.

        Args:
            agent_class: The concrete BaseAgent subclass to instantiate.
            config: Agent configuration. If None, a default is created.
            parent_id: Optional parent agent ID for hierarchy.

        Returns:
            The newly created agent instance.

        Raises:
            RuntimeError: If max agent limit is reached.
        """
        with self._agent_lock:
            if len(self._agents) >= self._max_agents:
                msg = f"Max agent limit reached ({self._max_agents})"
                raise RuntimeError(msg)

            if config is None:
                config = AgentConfig()

            agent = agent_class(None)
            agent._parent_id = parent_id

            # Register parent-child relationship
            if parent_id and parent_id in self._agents:
                self._agents[parent_id]._child_ids.append(agent.agent_id)

            self._agents[agent.agent_id] = agent
            self._stats.total_spawned += 1
            self._stats.active_count = len(self._agents)
            self._stats.peak_active = max(self._stats.peak_active, self._stats.active_count)

            self._fire_hook("on_spawn", agent)
            logger.info("Agent spawned: %s (%s)", agent.name, agent.agent_id)
            return agent

    # ── Lifecycle ───────────────────────────────────────────

    def xǁAgentRuntimeǁspawn__mutmut_8(
        self,
        agent_class: type[BaseAgent],
        config: AgentConfig | None = None,
        parent_id: str | None = None,
    ) -> BaseAgent:
        """Spawn a new agent instance and register it in the runtime.

        Args:
            agent_class: The concrete BaseAgent subclass to instantiate.
            config: Agent configuration. If None, a default is created.
            parent_id: Optional parent agent ID for hierarchy.

        Returns:
            The newly created agent instance.

        Raises:
            RuntimeError: If max agent limit is reached.
        """
        with self._agent_lock:
            if len(self._agents) >= self._max_agents:
                msg = f"Max agent limit reached ({self._max_agents})"
                raise RuntimeError(msg)

            if config is None:
                config = AgentConfig()

            agent = agent_class(config)
            agent._parent_id = None

            # Register parent-child relationship
            if parent_id and parent_id in self._agents:
                self._agents[parent_id]._child_ids.append(agent.agent_id)

            self._agents[agent.agent_id] = agent
            self._stats.total_spawned += 1
            self._stats.active_count = len(self._agents)
            self._stats.peak_active = max(self._stats.peak_active, self._stats.active_count)

            self._fire_hook("on_spawn", agent)
            logger.info("Agent spawned: %s (%s)", agent.name, agent.agent_id)
            return agent

    # ── Lifecycle ───────────────────────────────────────────

    def xǁAgentRuntimeǁspawn__mutmut_9(
        self,
        agent_class: type[BaseAgent],
        config: AgentConfig | None = None,
        parent_id: str | None = None,
    ) -> BaseAgent:
        """Spawn a new agent instance and register it in the runtime.

        Args:
            agent_class: The concrete BaseAgent subclass to instantiate.
            config: Agent configuration. If None, a default is created.
            parent_id: Optional parent agent ID for hierarchy.

        Returns:
            The newly created agent instance.

        Raises:
            RuntimeError: If max agent limit is reached.
        """
        with self._agent_lock:
            if len(self._agents) >= self._max_agents:
                msg = f"Max agent limit reached ({self._max_agents})"
                raise RuntimeError(msg)

            if config is None:
                config = AgentConfig()

            agent = agent_class(config)
            agent._parent_id = parent_id

            # Register parent-child relationship
            if parent_id or parent_id in self._agents:
                self._agents[parent_id]._child_ids.append(agent.agent_id)

            self._agents[agent.agent_id] = agent
            self._stats.total_spawned += 1
            self._stats.active_count = len(self._agents)
            self._stats.peak_active = max(self._stats.peak_active, self._stats.active_count)

            self._fire_hook("on_spawn", agent)
            logger.info("Agent spawned: %s (%s)", agent.name, agent.agent_id)
            return agent

    # ── Lifecycle ───────────────────────────────────────────

    def xǁAgentRuntimeǁspawn__mutmut_10(
        self,
        agent_class: type[BaseAgent],
        config: AgentConfig | None = None,
        parent_id: str | None = None,
    ) -> BaseAgent:
        """Spawn a new agent instance and register it in the runtime.

        Args:
            agent_class: The concrete BaseAgent subclass to instantiate.
            config: Agent configuration. If None, a default is created.
            parent_id: Optional parent agent ID for hierarchy.

        Returns:
            The newly created agent instance.

        Raises:
            RuntimeError: If max agent limit is reached.
        """
        with self._agent_lock:
            if len(self._agents) >= self._max_agents:
                msg = f"Max agent limit reached ({self._max_agents})"
                raise RuntimeError(msg)

            if config is None:
                config = AgentConfig()

            agent = agent_class(config)
            agent._parent_id = parent_id

            # Register parent-child relationship
            if parent_id and parent_id not in self._agents:
                self._agents[parent_id]._child_ids.append(agent.agent_id)

            self._agents[agent.agent_id] = agent
            self._stats.total_spawned += 1
            self._stats.active_count = len(self._agents)
            self._stats.peak_active = max(self._stats.peak_active, self._stats.active_count)

            self._fire_hook("on_spawn", agent)
            logger.info("Agent spawned: %s (%s)", agent.name, agent.agent_id)
            return agent

    # ── Lifecycle ───────────────────────────────────────────

    def xǁAgentRuntimeǁspawn__mutmut_11(
        self,
        agent_class: type[BaseAgent],
        config: AgentConfig | None = None,
        parent_id: str | None = None,
    ) -> BaseAgent:
        """Spawn a new agent instance and register it in the runtime.

        Args:
            agent_class: The concrete BaseAgent subclass to instantiate.
            config: Agent configuration. If None, a default is created.
            parent_id: Optional parent agent ID for hierarchy.

        Returns:
            The newly created agent instance.

        Raises:
            RuntimeError: If max agent limit is reached.
        """
        with self._agent_lock:
            if len(self._agents) >= self._max_agents:
                msg = f"Max agent limit reached ({self._max_agents})"
                raise RuntimeError(msg)

            if config is None:
                config = AgentConfig()

            agent = agent_class(config)
            agent._parent_id = parent_id

            # Register parent-child relationship
            if parent_id and parent_id in self._agents:
                self._agents[parent_id]._child_ids.append(None)

            self._agents[agent.agent_id] = agent
            self._stats.total_spawned += 1
            self._stats.active_count = len(self._agents)
            self._stats.peak_active = max(self._stats.peak_active, self._stats.active_count)

            self._fire_hook("on_spawn", agent)
            logger.info("Agent spawned: %s (%s)", agent.name, agent.agent_id)
            return agent

    # ── Lifecycle ───────────────────────────────────────────

    def xǁAgentRuntimeǁspawn__mutmut_12(
        self,
        agent_class: type[BaseAgent],
        config: AgentConfig | None = None,
        parent_id: str | None = None,
    ) -> BaseAgent:
        """Spawn a new agent instance and register it in the runtime.

        Args:
            agent_class: The concrete BaseAgent subclass to instantiate.
            config: Agent configuration. If None, a default is created.
            parent_id: Optional parent agent ID for hierarchy.

        Returns:
            The newly created agent instance.

        Raises:
            RuntimeError: If max agent limit is reached.
        """
        with self._agent_lock:
            if len(self._agents) >= self._max_agents:
                msg = f"Max agent limit reached ({self._max_agents})"
                raise RuntimeError(msg)

            if config is None:
                config = AgentConfig()

            agent = agent_class(config)
            agent._parent_id = parent_id

            # Register parent-child relationship
            if parent_id and parent_id in self._agents:
                self._agents[parent_id]._child_ids.append(agent.agent_id)

            self._agents[agent.agent_id] = None
            self._stats.total_spawned += 1
            self._stats.active_count = len(self._agents)
            self._stats.peak_active = max(self._stats.peak_active, self._stats.active_count)

            self._fire_hook("on_spawn", agent)
            logger.info("Agent spawned: %s (%s)", agent.name, agent.agent_id)
            return agent

    # ── Lifecycle ───────────────────────────────────────────

    def xǁAgentRuntimeǁspawn__mutmut_13(
        self,
        agent_class: type[BaseAgent],
        config: AgentConfig | None = None,
        parent_id: str | None = None,
    ) -> BaseAgent:
        """Spawn a new agent instance and register it in the runtime.

        Args:
            agent_class: The concrete BaseAgent subclass to instantiate.
            config: Agent configuration. If None, a default is created.
            parent_id: Optional parent agent ID for hierarchy.

        Returns:
            The newly created agent instance.

        Raises:
            RuntimeError: If max agent limit is reached.
        """
        with self._agent_lock:
            if len(self._agents) >= self._max_agents:
                msg = f"Max agent limit reached ({self._max_agents})"
                raise RuntimeError(msg)

            if config is None:
                config = AgentConfig()

            agent = agent_class(config)
            agent._parent_id = parent_id

            # Register parent-child relationship
            if parent_id and parent_id in self._agents:
                self._agents[parent_id]._child_ids.append(agent.agent_id)

            self._agents[agent.agent_id] = agent
            self._stats.total_spawned = 1
            self._stats.active_count = len(self._agents)
            self._stats.peak_active = max(self._stats.peak_active, self._stats.active_count)

            self._fire_hook("on_spawn", agent)
            logger.info("Agent spawned: %s (%s)", agent.name, agent.agent_id)
            return agent

    # ── Lifecycle ───────────────────────────────────────────

    def xǁAgentRuntimeǁspawn__mutmut_14(
        self,
        agent_class: type[BaseAgent],
        config: AgentConfig | None = None,
        parent_id: str | None = None,
    ) -> BaseAgent:
        """Spawn a new agent instance and register it in the runtime.

        Args:
            agent_class: The concrete BaseAgent subclass to instantiate.
            config: Agent configuration. If None, a default is created.
            parent_id: Optional parent agent ID for hierarchy.

        Returns:
            The newly created agent instance.

        Raises:
            RuntimeError: If max agent limit is reached.
        """
        with self._agent_lock:
            if len(self._agents) >= self._max_agents:
                msg = f"Max agent limit reached ({self._max_agents})"
                raise RuntimeError(msg)

            if config is None:
                config = AgentConfig()

            agent = agent_class(config)
            agent._parent_id = parent_id

            # Register parent-child relationship
            if parent_id and parent_id in self._agents:
                self._agents[parent_id]._child_ids.append(agent.agent_id)

            self._agents[agent.agent_id] = agent
            self._stats.total_spawned -= 1
            self._stats.active_count = len(self._agents)
            self._stats.peak_active = max(self._stats.peak_active, self._stats.active_count)

            self._fire_hook("on_spawn", agent)
            logger.info("Agent spawned: %s (%s)", agent.name, agent.agent_id)
            return agent

    # ── Lifecycle ───────────────────────────────────────────

    def xǁAgentRuntimeǁspawn__mutmut_15(
        self,
        agent_class: type[BaseAgent],
        config: AgentConfig | None = None,
        parent_id: str | None = None,
    ) -> BaseAgent:
        """Spawn a new agent instance and register it in the runtime.

        Args:
            agent_class: The concrete BaseAgent subclass to instantiate.
            config: Agent configuration. If None, a default is created.
            parent_id: Optional parent agent ID for hierarchy.

        Returns:
            The newly created agent instance.

        Raises:
            RuntimeError: If max agent limit is reached.
        """
        with self._agent_lock:
            if len(self._agents) >= self._max_agents:
                msg = f"Max agent limit reached ({self._max_agents})"
                raise RuntimeError(msg)

            if config is None:
                config = AgentConfig()

            agent = agent_class(config)
            agent._parent_id = parent_id

            # Register parent-child relationship
            if parent_id and parent_id in self._agents:
                self._agents[parent_id]._child_ids.append(agent.agent_id)

            self._agents[agent.agent_id] = agent
            self._stats.total_spawned += 2
            self._stats.active_count = len(self._agents)
            self._stats.peak_active = max(self._stats.peak_active, self._stats.active_count)

            self._fire_hook("on_spawn", agent)
            logger.info("Agent spawned: %s (%s)", agent.name, agent.agent_id)
            return agent

    # ── Lifecycle ───────────────────────────────────────────

    def xǁAgentRuntimeǁspawn__mutmut_16(
        self,
        agent_class: type[BaseAgent],
        config: AgentConfig | None = None,
        parent_id: str | None = None,
    ) -> BaseAgent:
        """Spawn a new agent instance and register it in the runtime.

        Args:
            agent_class: The concrete BaseAgent subclass to instantiate.
            config: Agent configuration. If None, a default is created.
            parent_id: Optional parent agent ID for hierarchy.

        Returns:
            The newly created agent instance.

        Raises:
            RuntimeError: If max agent limit is reached.
        """
        with self._agent_lock:
            if len(self._agents) >= self._max_agents:
                msg = f"Max agent limit reached ({self._max_agents})"
                raise RuntimeError(msg)

            if config is None:
                config = AgentConfig()

            agent = agent_class(config)
            agent._parent_id = parent_id

            # Register parent-child relationship
            if parent_id and parent_id in self._agents:
                self._agents[parent_id]._child_ids.append(agent.agent_id)

            self._agents[agent.agent_id] = agent
            self._stats.total_spawned += 1
            self._stats.active_count = None
            self._stats.peak_active = max(self._stats.peak_active, self._stats.active_count)

            self._fire_hook("on_spawn", agent)
            logger.info("Agent spawned: %s (%s)", agent.name, agent.agent_id)
            return agent

    # ── Lifecycle ───────────────────────────────────────────

    def xǁAgentRuntimeǁspawn__mutmut_17(
        self,
        agent_class: type[BaseAgent],
        config: AgentConfig | None = None,
        parent_id: str | None = None,
    ) -> BaseAgent:
        """Spawn a new agent instance and register it in the runtime.

        Args:
            agent_class: The concrete BaseAgent subclass to instantiate.
            config: Agent configuration. If None, a default is created.
            parent_id: Optional parent agent ID for hierarchy.

        Returns:
            The newly created agent instance.

        Raises:
            RuntimeError: If max agent limit is reached.
        """
        with self._agent_lock:
            if len(self._agents) >= self._max_agents:
                msg = f"Max agent limit reached ({self._max_agents})"
                raise RuntimeError(msg)

            if config is None:
                config = AgentConfig()

            agent = agent_class(config)
            agent._parent_id = parent_id

            # Register parent-child relationship
            if parent_id and parent_id in self._agents:
                self._agents[parent_id]._child_ids.append(agent.agent_id)

            self._agents[agent.agent_id] = agent
            self._stats.total_spawned += 1
            self._stats.active_count = len(self._agents)
            self._stats.peak_active = None

            self._fire_hook("on_spawn", agent)
            logger.info("Agent spawned: %s (%s)", agent.name, agent.agent_id)
            return agent

    # ── Lifecycle ───────────────────────────────────────────

    def xǁAgentRuntimeǁspawn__mutmut_18(
        self,
        agent_class: type[BaseAgent],
        config: AgentConfig | None = None,
        parent_id: str | None = None,
    ) -> BaseAgent:
        """Spawn a new agent instance and register it in the runtime.

        Args:
            agent_class: The concrete BaseAgent subclass to instantiate.
            config: Agent configuration. If None, a default is created.
            parent_id: Optional parent agent ID for hierarchy.

        Returns:
            The newly created agent instance.

        Raises:
            RuntimeError: If max agent limit is reached.
        """
        with self._agent_lock:
            if len(self._agents) >= self._max_agents:
                msg = f"Max agent limit reached ({self._max_agents})"
                raise RuntimeError(msg)

            if config is None:
                config = AgentConfig()

            agent = agent_class(config)
            agent._parent_id = parent_id

            # Register parent-child relationship
            if parent_id and parent_id in self._agents:
                self._agents[parent_id]._child_ids.append(agent.agent_id)

            self._agents[agent.agent_id] = agent
            self._stats.total_spawned += 1
            self._stats.active_count = len(self._agents)
            self._stats.peak_active = max(None, self._stats.active_count)

            self._fire_hook("on_spawn", agent)
            logger.info("Agent spawned: %s (%s)", agent.name, agent.agent_id)
            return agent

    # ── Lifecycle ───────────────────────────────────────────

    def xǁAgentRuntimeǁspawn__mutmut_19(
        self,
        agent_class: type[BaseAgent],
        config: AgentConfig | None = None,
        parent_id: str | None = None,
    ) -> BaseAgent:
        """Spawn a new agent instance and register it in the runtime.

        Args:
            agent_class: The concrete BaseAgent subclass to instantiate.
            config: Agent configuration. If None, a default is created.
            parent_id: Optional parent agent ID for hierarchy.

        Returns:
            The newly created agent instance.

        Raises:
            RuntimeError: If max agent limit is reached.
        """
        with self._agent_lock:
            if len(self._agents) >= self._max_agents:
                msg = f"Max agent limit reached ({self._max_agents})"
                raise RuntimeError(msg)

            if config is None:
                config = AgentConfig()

            agent = agent_class(config)
            agent._parent_id = parent_id

            # Register parent-child relationship
            if parent_id and parent_id in self._agents:
                self._agents[parent_id]._child_ids.append(agent.agent_id)

            self._agents[agent.agent_id] = agent
            self._stats.total_spawned += 1
            self._stats.active_count = len(self._agents)
            self._stats.peak_active = max(self._stats.peak_active, None)

            self._fire_hook("on_spawn", agent)
            logger.info("Agent spawned: %s (%s)", agent.name, agent.agent_id)
            return agent

    # ── Lifecycle ───────────────────────────────────────────

    def xǁAgentRuntimeǁspawn__mutmut_20(
        self,
        agent_class: type[BaseAgent],
        config: AgentConfig | None = None,
        parent_id: str | None = None,
    ) -> BaseAgent:
        """Spawn a new agent instance and register it in the runtime.

        Args:
            agent_class: The concrete BaseAgent subclass to instantiate.
            config: Agent configuration. If None, a default is created.
            parent_id: Optional parent agent ID for hierarchy.

        Returns:
            The newly created agent instance.

        Raises:
            RuntimeError: If max agent limit is reached.
        """
        with self._agent_lock:
            if len(self._agents) >= self._max_agents:
                msg = f"Max agent limit reached ({self._max_agents})"
                raise RuntimeError(msg)

            if config is None:
                config = AgentConfig()

            agent = agent_class(config)
            agent._parent_id = parent_id

            # Register parent-child relationship
            if parent_id and parent_id in self._agents:
                self._agents[parent_id]._child_ids.append(agent.agent_id)

            self._agents[agent.agent_id] = agent
            self._stats.total_spawned += 1
            self._stats.active_count = len(self._agents)
            self._stats.peak_active = max(self._stats.active_count)

            self._fire_hook("on_spawn", agent)
            logger.info("Agent spawned: %s (%s)", agent.name, agent.agent_id)
            return agent

    # ── Lifecycle ───────────────────────────────────────────

    def xǁAgentRuntimeǁspawn__mutmut_21(
        self,
        agent_class: type[BaseAgent],
        config: AgentConfig | None = None,
        parent_id: str | None = None,
    ) -> BaseAgent:
        """Spawn a new agent instance and register it in the runtime.

        Args:
            agent_class: The concrete BaseAgent subclass to instantiate.
            config: Agent configuration. If None, a default is created.
            parent_id: Optional parent agent ID for hierarchy.

        Returns:
            The newly created agent instance.

        Raises:
            RuntimeError: If max agent limit is reached.
        """
        with self._agent_lock:
            if len(self._agents) >= self._max_agents:
                msg = f"Max agent limit reached ({self._max_agents})"
                raise RuntimeError(msg)

            if config is None:
                config = AgentConfig()

            agent = agent_class(config)
            agent._parent_id = parent_id

            # Register parent-child relationship
            if parent_id and parent_id in self._agents:
                self._agents[parent_id]._child_ids.append(agent.agent_id)

            self._agents[agent.agent_id] = agent
            self._stats.total_spawned += 1
            self._stats.active_count = len(self._agents)
            self._stats.peak_active = max(self._stats.peak_active, )

            self._fire_hook("on_spawn", agent)
            logger.info("Agent spawned: %s (%s)", agent.name, agent.agent_id)
            return agent

    # ── Lifecycle ───────────────────────────────────────────

    def xǁAgentRuntimeǁspawn__mutmut_22(
        self,
        agent_class: type[BaseAgent],
        config: AgentConfig | None = None,
        parent_id: str | None = None,
    ) -> BaseAgent:
        """Spawn a new agent instance and register it in the runtime.

        Args:
            agent_class: The concrete BaseAgent subclass to instantiate.
            config: Agent configuration. If None, a default is created.
            parent_id: Optional parent agent ID for hierarchy.

        Returns:
            The newly created agent instance.

        Raises:
            RuntimeError: If max agent limit is reached.
        """
        with self._agent_lock:
            if len(self._agents) >= self._max_agents:
                msg = f"Max agent limit reached ({self._max_agents})"
                raise RuntimeError(msg)

            if config is None:
                config = AgentConfig()

            agent = agent_class(config)
            agent._parent_id = parent_id

            # Register parent-child relationship
            if parent_id and parent_id in self._agents:
                self._agents[parent_id]._child_ids.append(agent.agent_id)

            self._agents[agent.agent_id] = agent
            self._stats.total_spawned += 1
            self._stats.active_count = len(self._agents)
            self._stats.peak_active = max(self._stats.peak_active, self._stats.active_count)

            self._fire_hook(None, agent)
            logger.info("Agent spawned: %s (%s)", agent.name, agent.agent_id)
            return agent

    # ── Lifecycle ───────────────────────────────────────────

    def xǁAgentRuntimeǁspawn__mutmut_23(
        self,
        agent_class: type[BaseAgent],
        config: AgentConfig | None = None,
        parent_id: str | None = None,
    ) -> BaseAgent:
        """Spawn a new agent instance and register it in the runtime.

        Args:
            agent_class: The concrete BaseAgent subclass to instantiate.
            config: Agent configuration. If None, a default is created.
            parent_id: Optional parent agent ID for hierarchy.

        Returns:
            The newly created agent instance.

        Raises:
            RuntimeError: If max agent limit is reached.
        """
        with self._agent_lock:
            if len(self._agents) >= self._max_agents:
                msg = f"Max agent limit reached ({self._max_agents})"
                raise RuntimeError(msg)

            if config is None:
                config = AgentConfig()

            agent = agent_class(config)
            agent._parent_id = parent_id

            # Register parent-child relationship
            if parent_id and parent_id in self._agents:
                self._agents[parent_id]._child_ids.append(agent.agent_id)

            self._agents[agent.agent_id] = agent
            self._stats.total_spawned += 1
            self._stats.active_count = len(self._agents)
            self._stats.peak_active = max(self._stats.peak_active, self._stats.active_count)

            self._fire_hook("on_spawn", None)
            logger.info("Agent spawned: %s (%s)", agent.name, agent.agent_id)
            return agent

    # ── Lifecycle ───────────────────────────────────────────

    def xǁAgentRuntimeǁspawn__mutmut_24(
        self,
        agent_class: type[BaseAgent],
        config: AgentConfig | None = None,
        parent_id: str | None = None,
    ) -> BaseAgent:
        """Spawn a new agent instance and register it in the runtime.

        Args:
            agent_class: The concrete BaseAgent subclass to instantiate.
            config: Agent configuration. If None, a default is created.
            parent_id: Optional parent agent ID for hierarchy.

        Returns:
            The newly created agent instance.

        Raises:
            RuntimeError: If max agent limit is reached.
        """
        with self._agent_lock:
            if len(self._agents) >= self._max_agents:
                msg = f"Max agent limit reached ({self._max_agents})"
                raise RuntimeError(msg)

            if config is None:
                config = AgentConfig()

            agent = agent_class(config)
            agent._parent_id = parent_id

            # Register parent-child relationship
            if parent_id and parent_id in self._agents:
                self._agents[parent_id]._child_ids.append(agent.agent_id)

            self._agents[agent.agent_id] = agent
            self._stats.total_spawned += 1
            self._stats.active_count = len(self._agents)
            self._stats.peak_active = max(self._stats.peak_active, self._stats.active_count)

            self._fire_hook(agent)
            logger.info("Agent spawned: %s (%s)", agent.name, agent.agent_id)
            return agent

    # ── Lifecycle ───────────────────────────────────────────

    def xǁAgentRuntimeǁspawn__mutmut_25(
        self,
        agent_class: type[BaseAgent],
        config: AgentConfig | None = None,
        parent_id: str | None = None,
    ) -> BaseAgent:
        """Spawn a new agent instance and register it in the runtime.

        Args:
            agent_class: The concrete BaseAgent subclass to instantiate.
            config: Agent configuration. If None, a default is created.
            parent_id: Optional parent agent ID for hierarchy.

        Returns:
            The newly created agent instance.

        Raises:
            RuntimeError: If max agent limit is reached.
        """
        with self._agent_lock:
            if len(self._agents) >= self._max_agents:
                msg = f"Max agent limit reached ({self._max_agents})"
                raise RuntimeError(msg)

            if config is None:
                config = AgentConfig()

            agent = agent_class(config)
            agent._parent_id = parent_id

            # Register parent-child relationship
            if parent_id and parent_id in self._agents:
                self._agents[parent_id]._child_ids.append(agent.agent_id)

            self._agents[agent.agent_id] = agent
            self._stats.total_spawned += 1
            self._stats.active_count = len(self._agents)
            self._stats.peak_active = max(self._stats.peak_active, self._stats.active_count)

            self._fire_hook("on_spawn", )
            logger.info("Agent spawned: %s (%s)", agent.name, agent.agent_id)
            return agent

    # ── Lifecycle ───────────────────────────────────────────

    def xǁAgentRuntimeǁspawn__mutmut_26(
        self,
        agent_class: type[BaseAgent],
        config: AgentConfig | None = None,
        parent_id: str | None = None,
    ) -> BaseAgent:
        """Spawn a new agent instance and register it in the runtime.

        Args:
            agent_class: The concrete BaseAgent subclass to instantiate.
            config: Agent configuration. If None, a default is created.
            parent_id: Optional parent agent ID for hierarchy.

        Returns:
            The newly created agent instance.

        Raises:
            RuntimeError: If max agent limit is reached.
        """
        with self._agent_lock:
            if len(self._agents) >= self._max_agents:
                msg = f"Max agent limit reached ({self._max_agents})"
                raise RuntimeError(msg)

            if config is None:
                config = AgentConfig()

            agent = agent_class(config)
            agent._parent_id = parent_id

            # Register parent-child relationship
            if parent_id and parent_id in self._agents:
                self._agents[parent_id]._child_ids.append(agent.agent_id)

            self._agents[agent.agent_id] = agent
            self._stats.total_spawned += 1
            self._stats.active_count = len(self._agents)
            self._stats.peak_active = max(self._stats.peak_active, self._stats.active_count)

            self._fire_hook("XXon_spawnXX", agent)
            logger.info("Agent spawned: %s (%s)", agent.name, agent.agent_id)
            return agent

    # ── Lifecycle ───────────────────────────────────────────

    def xǁAgentRuntimeǁspawn__mutmut_27(
        self,
        agent_class: type[BaseAgent],
        config: AgentConfig | None = None,
        parent_id: str | None = None,
    ) -> BaseAgent:
        """Spawn a new agent instance and register it in the runtime.

        Args:
            agent_class: The concrete BaseAgent subclass to instantiate.
            config: Agent configuration. If None, a default is created.
            parent_id: Optional parent agent ID for hierarchy.

        Returns:
            The newly created agent instance.

        Raises:
            RuntimeError: If max agent limit is reached.
        """
        with self._agent_lock:
            if len(self._agents) >= self._max_agents:
                msg = f"Max agent limit reached ({self._max_agents})"
                raise RuntimeError(msg)

            if config is None:
                config = AgentConfig()

            agent = agent_class(config)
            agent._parent_id = parent_id

            # Register parent-child relationship
            if parent_id and parent_id in self._agents:
                self._agents[parent_id]._child_ids.append(agent.agent_id)

            self._agents[agent.agent_id] = agent
            self._stats.total_spawned += 1
            self._stats.active_count = len(self._agents)
            self._stats.peak_active = max(self._stats.peak_active, self._stats.active_count)

            self._fire_hook("ON_SPAWN", agent)
            logger.info("Agent spawned: %s (%s)", agent.name, agent.agent_id)
            return agent

    # ── Lifecycle ───────────────────────────────────────────

    def xǁAgentRuntimeǁspawn__mutmut_28(
        self,
        agent_class: type[BaseAgent],
        config: AgentConfig | None = None,
        parent_id: str | None = None,
    ) -> BaseAgent:
        """Spawn a new agent instance and register it in the runtime.

        Args:
            agent_class: The concrete BaseAgent subclass to instantiate.
            config: Agent configuration. If None, a default is created.
            parent_id: Optional parent agent ID for hierarchy.

        Returns:
            The newly created agent instance.

        Raises:
            RuntimeError: If max agent limit is reached.
        """
        with self._agent_lock:
            if len(self._agents) >= self._max_agents:
                msg = f"Max agent limit reached ({self._max_agents})"
                raise RuntimeError(msg)

            if config is None:
                config = AgentConfig()

            agent = agent_class(config)
            agent._parent_id = parent_id

            # Register parent-child relationship
            if parent_id and parent_id in self._agents:
                self._agents[parent_id]._child_ids.append(agent.agent_id)

            self._agents[agent.agent_id] = agent
            self._stats.total_spawned += 1
            self._stats.active_count = len(self._agents)
            self._stats.peak_active = max(self._stats.peak_active, self._stats.active_count)

            self._fire_hook("on_spawn", agent)
            logger.info(None, agent.name, agent.agent_id)
            return agent

    # ── Lifecycle ───────────────────────────────────────────

    def xǁAgentRuntimeǁspawn__mutmut_29(
        self,
        agent_class: type[BaseAgent],
        config: AgentConfig | None = None,
        parent_id: str | None = None,
    ) -> BaseAgent:
        """Spawn a new agent instance and register it in the runtime.

        Args:
            agent_class: The concrete BaseAgent subclass to instantiate.
            config: Agent configuration. If None, a default is created.
            parent_id: Optional parent agent ID for hierarchy.

        Returns:
            The newly created agent instance.

        Raises:
            RuntimeError: If max agent limit is reached.
        """
        with self._agent_lock:
            if len(self._agents) >= self._max_agents:
                msg = f"Max agent limit reached ({self._max_agents})"
                raise RuntimeError(msg)

            if config is None:
                config = AgentConfig()

            agent = agent_class(config)
            agent._parent_id = parent_id

            # Register parent-child relationship
            if parent_id and parent_id in self._agents:
                self._agents[parent_id]._child_ids.append(agent.agent_id)

            self._agents[agent.agent_id] = agent
            self._stats.total_spawned += 1
            self._stats.active_count = len(self._agents)
            self._stats.peak_active = max(self._stats.peak_active, self._stats.active_count)

            self._fire_hook("on_spawn", agent)
            logger.info("Agent spawned: %s (%s)", None, agent.agent_id)
            return agent

    # ── Lifecycle ───────────────────────────────────────────

    def xǁAgentRuntimeǁspawn__mutmut_30(
        self,
        agent_class: type[BaseAgent],
        config: AgentConfig | None = None,
        parent_id: str | None = None,
    ) -> BaseAgent:
        """Spawn a new agent instance and register it in the runtime.

        Args:
            agent_class: The concrete BaseAgent subclass to instantiate.
            config: Agent configuration. If None, a default is created.
            parent_id: Optional parent agent ID for hierarchy.

        Returns:
            The newly created agent instance.

        Raises:
            RuntimeError: If max agent limit is reached.
        """
        with self._agent_lock:
            if len(self._agents) >= self._max_agents:
                msg = f"Max agent limit reached ({self._max_agents})"
                raise RuntimeError(msg)

            if config is None:
                config = AgentConfig()

            agent = agent_class(config)
            agent._parent_id = parent_id

            # Register parent-child relationship
            if parent_id and parent_id in self._agents:
                self._agents[parent_id]._child_ids.append(agent.agent_id)

            self._agents[agent.agent_id] = agent
            self._stats.total_spawned += 1
            self._stats.active_count = len(self._agents)
            self._stats.peak_active = max(self._stats.peak_active, self._stats.active_count)

            self._fire_hook("on_spawn", agent)
            logger.info("Agent spawned: %s (%s)", agent.name, None)
            return agent

    # ── Lifecycle ───────────────────────────────────────────

    def xǁAgentRuntimeǁspawn__mutmut_31(
        self,
        agent_class: type[BaseAgent],
        config: AgentConfig | None = None,
        parent_id: str | None = None,
    ) -> BaseAgent:
        """Spawn a new agent instance and register it in the runtime.

        Args:
            agent_class: The concrete BaseAgent subclass to instantiate.
            config: Agent configuration. If None, a default is created.
            parent_id: Optional parent agent ID for hierarchy.

        Returns:
            The newly created agent instance.

        Raises:
            RuntimeError: If max agent limit is reached.
        """
        with self._agent_lock:
            if len(self._agents) >= self._max_agents:
                msg = f"Max agent limit reached ({self._max_agents})"
                raise RuntimeError(msg)

            if config is None:
                config = AgentConfig()

            agent = agent_class(config)
            agent._parent_id = parent_id

            # Register parent-child relationship
            if parent_id and parent_id in self._agents:
                self._agents[parent_id]._child_ids.append(agent.agent_id)

            self._agents[agent.agent_id] = agent
            self._stats.total_spawned += 1
            self._stats.active_count = len(self._agents)
            self._stats.peak_active = max(self._stats.peak_active, self._stats.active_count)

            self._fire_hook("on_spawn", agent)
            logger.info(agent.name, agent.agent_id)
            return agent

    # ── Lifecycle ───────────────────────────────────────────

    def xǁAgentRuntimeǁspawn__mutmut_32(
        self,
        agent_class: type[BaseAgent],
        config: AgentConfig | None = None,
        parent_id: str | None = None,
    ) -> BaseAgent:
        """Spawn a new agent instance and register it in the runtime.

        Args:
            agent_class: The concrete BaseAgent subclass to instantiate.
            config: Agent configuration. If None, a default is created.
            parent_id: Optional parent agent ID for hierarchy.

        Returns:
            The newly created agent instance.

        Raises:
            RuntimeError: If max agent limit is reached.
        """
        with self._agent_lock:
            if len(self._agents) >= self._max_agents:
                msg = f"Max agent limit reached ({self._max_agents})"
                raise RuntimeError(msg)

            if config is None:
                config = AgentConfig()

            agent = agent_class(config)
            agent._parent_id = parent_id

            # Register parent-child relationship
            if parent_id and parent_id in self._agents:
                self._agents[parent_id]._child_ids.append(agent.agent_id)

            self._agents[agent.agent_id] = agent
            self._stats.total_spawned += 1
            self._stats.active_count = len(self._agents)
            self._stats.peak_active = max(self._stats.peak_active, self._stats.active_count)

            self._fire_hook("on_spawn", agent)
            logger.info("Agent spawned: %s (%s)", agent.agent_id)
            return agent

    # ── Lifecycle ───────────────────────────────────────────

    def xǁAgentRuntimeǁspawn__mutmut_33(
        self,
        agent_class: type[BaseAgent],
        config: AgentConfig | None = None,
        parent_id: str | None = None,
    ) -> BaseAgent:
        """Spawn a new agent instance and register it in the runtime.

        Args:
            agent_class: The concrete BaseAgent subclass to instantiate.
            config: Agent configuration. If None, a default is created.
            parent_id: Optional parent agent ID for hierarchy.

        Returns:
            The newly created agent instance.

        Raises:
            RuntimeError: If max agent limit is reached.
        """
        with self._agent_lock:
            if len(self._agents) >= self._max_agents:
                msg = f"Max agent limit reached ({self._max_agents})"
                raise RuntimeError(msg)

            if config is None:
                config = AgentConfig()

            agent = agent_class(config)
            agent._parent_id = parent_id

            # Register parent-child relationship
            if parent_id and parent_id in self._agents:
                self._agents[parent_id]._child_ids.append(agent.agent_id)

            self._agents[agent.agent_id] = agent
            self._stats.total_spawned += 1
            self._stats.active_count = len(self._agents)
            self._stats.peak_active = max(self._stats.peak_active, self._stats.active_count)

            self._fire_hook("on_spawn", agent)
            logger.info("Agent spawned: %s (%s)", agent.name, )
            return agent

    # ── Lifecycle ───────────────────────────────────────────

    def xǁAgentRuntimeǁspawn__mutmut_34(
        self,
        agent_class: type[BaseAgent],
        config: AgentConfig | None = None,
        parent_id: str | None = None,
    ) -> BaseAgent:
        """Spawn a new agent instance and register it in the runtime.

        Args:
            agent_class: The concrete BaseAgent subclass to instantiate.
            config: Agent configuration. If None, a default is created.
            parent_id: Optional parent agent ID for hierarchy.

        Returns:
            The newly created agent instance.

        Raises:
            RuntimeError: If max agent limit is reached.
        """
        with self._agent_lock:
            if len(self._agents) >= self._max_agents:
                msg = f"Max agent limit reached ({self._max_agents})"
                raise RuntimeError(msg)

            if config is None:
                config = AgentConfig()

            agent = agent_class(config)
            agent._parent_id = parent_id

            # Register parent-child relationship
            if parent_id and parent_id in self._agents:
                self._agents[parent_id]._child_ids.append(agent.agent_id)

            self._agents[agent.agent_id] = agent
            self._stats.total_spawned += 1
            self._stats.active_count = len(self._agents)
            self._stats.peak_active = max(self._stats.peak_active, self._stats.active_count)

            self._fire_hook("on_spawn", agent)
            logger.info("XXAgent spawned: %s (%s)XX", agent.name, agent.agent_id)
            return agent

    # ── Lifecycle ───────────────────────────────────────────

    def xǁAgentRuntimeǁspawn__mutmut_35(
        self,
        agent_class: type[BaseAgent],
        config: AgentConfig | None = None,
        parent_id: str | None = None,
    ) -> BaseAgent:
        """Spawn a new agent instance and register it in the runtime.

        Args:
            agent_class: The concrete BaseAgent subclass to instantiate.
            config: Agent configuration. If None, a default is created.
            parent_id: Optional parent agent ID for hierarchy.

        Returns:
            The newly created agent instance.

        Raises:
            RuntimeError: If max agent limit is reached.
        """
        with self._agent_lock:
            if len(self._agents) >= self._max_agents:
                msg = f"Max agent limit reached ({self._max_agents})"
                raise RuntimeError(msg)

            if config is None:
                config = AgentConfig()

            agent = agent_class(config)
            agent._parent_id = parent_id

            # Register parent-child relationship
            if parent_id and parent_id in self._agents:
                self._agents[parent_id]._child_ids.append(agent.agent_id)

            self._agents[agent.agent_id] = agent
            self._stats.total_spawned += 1
            self._stats.active_count = len(self._agents)
            self._stats.peak_active = max(self._stats.peak_active, self._stats.active_count)

            self._fire_hook("on_spawn", agent)
            logger.info("agent spawned: %s (%s)", agent.name, agent.agent_id)
            return agent

    # ── Lifecycle ───────────────────────────────────────────

    def xǁAgentRuntimeǁspawn__mutmut_36(
        self,
        agent_class: type[BaseAgent],
        config: AgentConfig | None = None,
        parent_id: str | None = None,
    ) -> BaseAgent:
        """Spawn a new agent instance and register it in the runtime.

        Args:
            agent_class: The concrete BaseAgent subclass to instantiate.
            config: Agent configuration. If None, a default is created.
            parent_id: Optional parent agent ID for hierarchy.

        Returns:
            The newly created agent instance.

        Raises:
            RuntimeError: If max agent limit is reached.
        """
        with self._agent_lock:
            if len(self._agents) >= self._max_agents:
                msg = f"Max agent limit reached ({self._max_agents})"
                raise RuntimeError(msg)

            if config is None:
                config = AgentConfig()

            agent = agent_class(config)
            agent._parent_id = parent_id

            # Register parent-child relationship
            if parent_id and parent_id in self._agents:
                self._agents[parent_id]._child_ids.append(agent.agent_id)

            self._agents[agent.agent_id] = agent
            self._stats.total_spawned += 1
            self._stats.active_count = len(self._agents)
            self._stats.peak_active = max(self._stats.peak_active, self._stats.active_count)

            self._fire_hook("on_spawn", agent)
            logger.info("AGENT SPAWNED: %S (%S)", agent.name, agent.agent_id)
            return agent

    @_mutmut_mutated(mutants_xǁAgentRuntimeǁterminate_agent__mutmut)
    def terminate_agent(self, agent_id: str, force: bool = False) -> bool:
        """Terminate an agent by ID.

        Args:
            agent_id: The agent to terminate.
            force: If True, force-terminate even if agent is in an active state.

        Returns:
            True if termination was successful.
        """
        with self._agent_lock:
            agent = self._agents.get(agent_id)
            if agent is None:
                return False

            if force:
                agent.force_state(AgentState.TERMINATED)
            else:
                if not agent.terminate():
                    logger.warning("Cannot terminate agent %s in state %s", agent_id, agent.state)
                    return False

            # Terminate all children first
            for child_id in list(agent._child_ids):
                self.terminate_agent(child_id, force=True)

            self._fire_hook("on_terminate", agent)
            del self._agents[agent_id]
            self._stats.total_terminated += 1
            self._stats.active_count = len(self._agents)
            logger.info("Agent terminated: %s", agent_id)
            return True

    def xǁAgentRuntimeǁterminate_agent__mutmut_orig(self, agent_id: str, force: bool = False) -> bool:
        """Terminate an agent by ID.

        Args:
            agent_id: The agent to terminate.
            force: If True, force-terminate even if agent is in an active state.

        Returns:
            True if termination was successful.
        """
        with self._agent_lock:
            agent = self._agents.get(agent_id)
            if agent is None:
                return False

            if force:
                agent.force_state(AgentState.TERMINATED)
            else:
                if not agent.terminate():
                    logger.warning("Cannot terminate agent %s in state %s", agent_id, agent.state)
                    return False

            # Terminate all children first
            for child_id in list(agent._child_ids):
                self.terminate_agent(child_id, force=True)

            self._fire_hook("on_terminate", agent)
            del self._agents[agent_id]
            self._stats.total_terminated += 1
            self._stats.active_count = len(self._agents)
            logger.info("Agent terminated: %s", agent_id)
            return True

    def xǁAgentRuntimeǁterminate_agent__mutmut_1(self, agent_id: str, force: bool = True) -> bool:
        """Terminate an agent by ID.

        Args:
            agent_id: The agent to terminate.
            force: If True, force-terminate even if agent is in an active state.

        Returns:
            True if termination was successful.
        """
        with self._agent_lock:
            agent = self._agents.get(agent_id)
            if agent is None:
                return False

            if force:
                agent.force_state(AgentState.TERMINATED)
            else:
                if not agent.terminate():
                    logger.warning("Cannot terminate agent %s in state %s", agent_id, agent.state)
                    return False

            # Terminate all children first
            for child_id in list(agent._child_ids):
                self.terminate_agent(child_id, force=True)

            self._fire_hook("on_terminate", agent)
            del self._agents[agent_id]
            self._stats.total_terminated += 1
            self._stats.active_count = len(self._agents)
            logger.info("Agent terminated: %s", agent_id)
            return True

    def xǁAgentRuntimeǁterminate_agent__mutmut_2(self, agent_id: str, force: bool = False) -> bool:
        """Terminate an agent by ID.

        Args:
            agent_id: The agent to terminate.
            force: If True, force-terminate even if agent is in an active state.

        Returns:
            True if termination was successful.
        """
        with self._agent_lock:
            agent = None
            if agent is None:
                return False

            if force:
                agent.force_state(AgentState.TERMINATED)
            else:
                if not agent.terminate():
                    logger.warning("Cannot terminate agent %s in state %s", agent_id, agent.state)
                    return False

            # Terminate all children first
            for child_id in list(agent._child_ids):
                self.terminate_agent(child_id, force=True)

            self._fire_hook("on_terminate", agent)
            del self._agents[agent_id]
            self._stats.total_terminated += 1
            self._stats.active_count = len(self._agents)
            logger.info("Agent terminated: %s", agent_id)
            return True

    def xǁAgentRuntimeǁterminate_agent__mutmut_3(self, agent_id: str, force: bool = False) -> bool:
        """Terminate an agent by ID.

        Args:
            agent_id: The agent to terminate.
            force: If True, force-terminate even if agent is in an active state.

        Returns:
            True if termination was successful.
        """
        with self._agent_lock:
            agent = self._agents.get(None)
            if agent is None:
                return False

            if force:
                agent.force_state(AgentState.TERMINATED)
            else:
                if not agent.terminate():
                    logger.warning("Cannot terminate agent %s in state %s", agent_id, agent.state)
                    return False

            # Terminate all children first
            for child_id in list(agent._child_ids):
                self.terminate_agent(child_id, force=True)

            self._fire_hook("on_terminate", agent)
            del self._agents[agent_id]
            self._stats.total_terminated += 1
            self._stats.active_count = len(self._agents)
            logger.info("Agent terminated: %s", agent_id)
            return True

    def xǁAgentRuntimeǁterminate_agent__mutmut_4(self, agent_id: str, force: bool = False) -> bool:
        """Terminate an agent by ID.

        Args:
            agent_id: The agent to terminate.
            force: If True, force-terminate even if agent is in an active state.

        Returns:
            True if termination was successful.
        """
        with self._agent_lock:
            agent = self._agents.get(agent_id)
            if agent is not None:
                return False

            if force:
                agent.force_state(AgentState.TERMINATED)
            else:
                if not agent.terminate():
                    logger.warning("Cannot terminate agent %s in state %s", agent_id, agent.state)
                    return False

            # Terminate all children first
            for child_id in list(agent._child_ids):
                self.terminate_agent(child_id, force=True)

            self._fire_hook("on_terminate", agent)
            del self._agents[agent_id]
            self._stats.total_terminated += 1
            self._stats.active_count = len(self._agents)
            logger.info("Agent terminated: %s", agent_id)
            return True

    def xǁAgentRuntimeǁterminate_agent__mutmut_5(self, agent_id: str, force: bool = False) -> bool:
        """Terminate an agent by ID.

        Args:
            agent_id: The agent to terminate.
            force: If True, force-terminate even if agent is in an active state.

        Returns:
            True if termination was successful.
        """
        with self._agent_lock:
            agent = self._agents.get(agent_id)
            if agent is None:
                return True

            if force:
                agent.force_state(AgentState.TERMINATED)
            else:
                if not agent.terminate():
                    logger.warning("Cannot terminate agent %s in state %s", agent_id, agent.state)
                    return False

            # Terminate all children first
            for child_id in list(agent._child_ids):
                self.terminate_agent(child_id, force=True)

            self._fire_hook("on_terminate", agent)
            del self._agents[agent_id]
            self._stats.total_terminated += 1
            self._stats.active_count = len(self._agents)
            logger.info("Agent terminated: %s", agent_id)
            return True

    def xǁAgentRuntimeǁterminate_agent__mutmut_6(self, agent_id: str, force: bool = False) -> bool:
        """Terminate an agent by ID.

        Args:
            agent_id: The agent to terminate.
            force: If True, force-terminate even if agent is in an active state.

        Returns:
            True if termination was successful.
        """
        with self._agent_lock:
            agent = self._agents.get(agent_id)
            if agent is None:
                return False

            if force:
                agent.force_state(None)
            else:
                if not agent.terminate():
                    logger.warning("Cannot terminate agent %s in state %s", agent_id, agent.state)
                    return False

            # Terminate all children first
            for child_id in list(agent._child_ids):
                self.terminate_agent(child_id, force=True)

            self._fire_hook("on_terminate", agent)
            del self._agents[agent_id]
            self._stats.total_terminated += 1
            self._stats.active_count = len(self._agents)
            logger.info("Agent terminated: %s", agent_id)
            return True

    def xǁAgentRuntimeǁterminate_agent__mutmut_7(self, agent_id: str, force: bool = False) -> bool:
        """Terminate an agent by ID.

        Args:
            agent_id: The agent to terminate.
            force: If True, force-terminate even if agent is in an active state.

        Returns:
            True if termination was successful.
        """
        with self._agent_lock:
            agent = self._agents.get(agent_id)
            if agent is None:
                return False

            if force:
                agent.force_state(AgentState.TERMINATED)
            else:
                if agent.terminate():
                    logger.warning("Cannot terminate agent %s in state %s", agent_id, agent.state)
                    return False

            # Terminate all children first
            for child_id in list(agent._child_ids):
                self.terminate_agent(child_id, force=True)

            self._fire_hook("on_terminate", agent)
            del self._agents[agent_id]
            self._stats.total_terminated += 1
            self._stats.active_count = len(self._agents)
            logger.info("Agent terminated: %s", agent_id)
            return True

    def xǁAgentRuntimeǁterminate_agent__mutmut_8(self, agent_id: str, force: bool = False) -> bool:
        """Terminate an agent by ID.

        Args:
            agent_id: The agent to terminate.
            force: If True, force-terminate even if agent is in an active state.

        Returns:
            True if termination was successful.
        """
        with self._agent_lock:
            agent = self._agents.get(agent_id)
            if agent is None:
                return False

            if force:
                agent.force_state(AgentState.TERMINATED)
            else:
                if not agent.terminate():
                    logger.warning(None, agent_id, agent.state)
                    return False

            # Terminate all children first
            for child_id in list(agent._child_ids):
                self.terminate_agent(child_id, force=True)

            self._fire_hook("on_terminate", agent)
            del self._agents[agent_id]
            self._stats.total_terminated += 1
            self._stats.active_count = len(self._agents)
            logger.info("Agent terminated: %s", agent_id)
            return True

    def xǁAgentRuntimeǁterminate_agent__mutmut_9(self, agent_id: str, force: bool = False) -> bool:
        """Terminate an agent by ID.

        Args:
            agent_id: The agent to terminate.
            force: If True, force-terminate even if agent is in an active state.

        Returns:
            True if termination was successful.
        """
        with self._agent_lock:
            agent = self._agents.get(agent_id)
            if agent is None:
                return False

            if force:
                agent.force_state(AgentState.TERMINATED)
            else:
                if not agent.terminate():
                    logger.warning("Cannot terminate agent %s in state %s", None, agent.state)
                    return False

            # Terminate all children first
            for child_id in list(agent._child_ids):
                self.terminate_agent(child_id, force=True)

            self._fire_hook("on_terminate", agent)
            del self._agents[agent_id]
            self._stats.total_terminated += 1
            self._stats.active_count = len(self._agents)
            logger.info("Agent terminated: %s", agent_id)
            return True

    def xǁAgentRuntimeǁterminate_agent__mutmut_10(self, agent_id: str, force: bool = False) -> bool:
        """Terminate an agent by ID.

        Args:
            agent_id: The agent to terminate.
            force: If True, force-terminate even if agent is in an active state.

        Returns:
            True if termination was successful.
        """
        with self._agent_lock:
            agent = self._agents.get(agent_id)
            if agent is None:
                return False

            if force:
                agent.force_state(AgentState.TERMINATED)
            else:
                if not agent.terminate():
                    logger.warning("Cannot terminate agent %s in state %s", agent_id, None)
                    return False

            # Terminate all children first
            for child_id in list(agent._child_ids):
                self.terminate_agent(child_id, force=True)

            self._fire_hook("on_terminate", agent)
            del self._agents[agent_id]
            self._stats.total_terminated += 1
            self._stats.active_count = len(self._agents)
            logger.info("Agent terminated: %s", agent_id)
            return True

    def xǁAgentRuntimeǁterminate_agent__mutmut_11(self, agent_id: str, force: bool = False) -> bool:
        """Terminate an agent by ID.

        Args:
            agent_id: The agent to terminate.
            force: If True, force-terminate even if agent is in an active state.

        Returns:
            True if termination was successful.
        """
        with self._agent_lock:
            agent = self._agents.get(agent_id)
            if agent is None:
                return False

            if force:
                agent.force_state(AgentState.TERMINATED)
            else:
                if not agent.terminate():
                    logger.warning(agent_id, agent.state)
                    return False

            # Terminate all children first
            for child_id in list(agent._child_ids):
                self.terminate_agent(child_id, force=True)

            self._fire_hook("on_terminate", agent)
            del self._agents[agent_id]
            self._stats.total_terminated += 1
            self._stats.active_count = len(self._agents)
            logger.info("Agent terminated: %s", agent_id)
            return True

    def xǁAgentRuntimeǁterminate_agent__mutmut_12(self, agent_id: str, force: bool = False) -> bool:
        """Terminate an agent by ID.

        Args:
            agent_id: The agent to terminate.
            force: If True, force-terminate even if agent is in an active state.

        Returns:
            True if termination was successful.
        """
        with self._agent_lock:
            agent = self._agents.get(agent_id)
            if agent is None:
                return False

            if force:
                agent.force_state(AgentState.TERMINATED)
            else:
                if not agent.terminate():
                    logger.warning("Cannot terminate agent %s in state %s", agent.state)
                    return False

            # Terminate all children first
            for child_id in list(agent._child_ids):
                self.terminate_agent(child_id, force=True)

            self._fire_hook("on_terminate", agent)
            del self._agents[agent_id]
            self._stats.total_terminated += 1
            self._stats.active_count = len(self._agents)
            logger.info("Agent terminated: %s", agent_id)
            return True

    def xǁAgentRuntimeǁterminate_agent__mutmut_13(self, agent_id: str, force: bool = False) -> bool:
        """Terminate an agent by ID.

        Args:
            agent_id: The agent to terminate.
            force: If True, force-terminate even if agent is in an active state.

        Returns:
            True if termination was successful.
        """
        with self._agent_lock:
            agent = self._agents.get(agent_id)
            if agent is None:
                return False

            if force:
                agent.force_state(AgentState.TERMINATED)
            else:
                if not agent.terminate():
                    logger.warning("Cannot terminate agent %s in state %s", agent_id, )
                    return False

            # Terminate all children first
            for child_id in list(agent._child_ids):
                self.terminate_agent(child_id, force=True)

            self._fire_hook("on_terminate", agent)
            del self._agents[agent_id]
            self._stats.total_terminated += 1
            self._stats.active_count = len(self._agents)
            logger.info("Agent terminated: %s", agent_id)
            return True

    def xǁAgentRuntimeǁterminate_agent__mutmut_14(self, agent_id: str, force: bool = False) -> bool:
        """Terminate an agent by ID.

        Args:
            agent_id: The agent to terminate.
            force: If True, force-terminate even if agent is in an active state.

        Returns:
            True if termination was successful.
        """
        with self._agent_lock:
            agent = self._agents.get(agent_id)
            if agent is None:
                return False

            if force:
                agent.force_state(AgentState.TERMINATED)
            else:
                if not agent.terminate():
                    logger.warning("XXCannot terminate agent %s in state %sXX", agent_id, agent.state)
                    return False

            # Terminate all children first
            for child_id in list(agent._child_ids):
                self.terminate_agent(child_id, force=True)

            self._fire_hook("on_terminate", agent)
            del self._agents[agent_id]
            self._stats.total_terminated += 1
            self._stats.active_count = len(self._agents)
            logger.info("Agent terminated: %s", agent_id)
            return True

    def xǁAgentRuntimeǁterminate_agent__mutmut_15(self, agent_id: str, force: bool = False) -> bool:
        """Terminate an agent by ID.

        Args:
            agent_id: The agent to terminate.
            force: If True, force-terminate even if agent is in an active state.

        Returns:
            True if termination was successful.
        """
        with self._agent_lock:
            agent = self._agents.get(agent_id)
            if agent is None:
                return False

            if force:
                agent.force_state(AgentState.TERMINATED)
            else:
                if not agent.terminate():
                    logger.warning("cannot terminate agent %s in state %s", agent_id, agent.state)
                    return False

            # Terminate all children first
            for child_id in list(agent._child_ids):
                self.terminate_agent(child_id, force=True)

            self._fire_hook("on_terminate", agent)
            del self._agents[agent_id]
            self._stats.total_terminated += 1
            self._stats.active_count = len(self._agents)
            logger.info("Agent terminated: %s", agent_id)
            return True

    def xǁAgentRuntimeǁterminate_agent__mutmut_16(self, agent_id: str, force: bool = False) -> bool:
        """Terminate an agent by ID.

        Args:
            agent_id: The agent to terminate.
            force: If True, force-terminate even if agent is in an active state.

        Returns:
            True if termination was successful.
        """
        with self._agent_lock:
            agent = self._agents.get(agent_id)
            if agent is None:
                return False

            if force:
                agent.force_state(AgentState.TERMINATED)
            else:
                if not agent.terminate():
                    logger.warning("CANNOT TERMINATE AGENT %S IN STATE %S", agent_id, agent.state)
                    return False

            # Terminate all children first
            for child_id in list(agent._child_ids):
                self.terminate_agent(child_id, force=True)

            self._fire_hook("on_terminate", agent)
            del self._agents[agent_id]
            self._stats.total_terminated += 1
            self._stats.active_count = len(self._agents)
            logger.info("Agent terminated: %s", agent_id)
            return True

    def xǁAgentRuntimeǁterminate_agent__mutmut_17(self, agent_id: str, force: bool = False) -> bool:
        """Terminate an agent by ID.

        Args:
            agent_id: The agent to terminate.
            force: If True, force-terminate even if agent is in an active state.

        Returns:
            True if termination was successful.
        """
        with self._agent_lock:
            agent = self._agents.get(agent_id)
            if agent is None:
                return False

            if force:
                agent.force_state(AgentState.TERMINATED)
            else:
                if not agent.terminate():
                    logger.warning("Cannot terminate agent %s in state %s", agent_id, agent.state)
                    return True

            # Terminate all children first
            for child_id in list(agent._child_ids):
                self.terminate_agent(child_id, force=True)

            self._fire_hook("on_terminate", agent)
            del self._agents[agent_id]
            self._stats.total_terminated += 1
            self._stats.active_count = len(self._agents)
            logger.info("Agent terminated: %s", agent_id)
            return True

    def xǁAgentRuntimeǁterminate_agent__mutmut_18(self, agent_id: str, force: bool = False) -> bool:
        """Terminate an agent by ID.

        Args:
            agent_id: The agent to terminate.
            force: If True, force-terminate even if agent is in an active state.

        Returns:
            True if termination was successful.
        """
        with self._agent_lock:
            agent = self._agents.get(agent_id)
            if agent is None:
                return False

            if force:
                agent.force_state(AgentState.TERMINATED)
            else:
                if not agent.terminate():
                    logger.warning("Cannot terminate agent %s in state %s", agent_id, agent.state)
                    return False

            # Terminate all children first
            for child_id in list(None):
                self.terminate_agent(child_id, force=True)

            self._fire_hook("on_terminate", agent)
            del self._agents[agent_id]
            self._stats.total_terminated += 1
            self._stats.active_count = len(self._agents)
            logger.info("Agent terminated: %s", agent_id)
            return True

    def xǁAgentRuntimeǁterminate_agent__mutmut_19(self, agent_id: str, force: bool = False) -> bool:
        """Terminate an agent by ID.

        Args:
            agent_id: The agent to terminate.
            force: If True, force-terminate even if agent is in an active state.

        Returns:
            True if termination was successful.
        """
        with self._agent_lock:
            agent = self._agents.get(agent_id)
            if agent is None:
                return False

            if force:
                agent.force_state(AgentState.TERMINATED)
            else:
                if not agent.terminate():
                    logger.warning("Cannot terminate agent %s in state %s", agent_id, agent.state)
                    return False

            # Terminate all children first
            for child_id in list(agent._child_ids):
                self.terminate_agent(None, force=True)

            self._fire_hook("on_terminate", agent)
            del self._agents[agent_id]
            self._stats.total_terminated += 1
            self._stats.active_count = len(self._agents)
            logger.info("Agent terminated: %s", agent_id)
            return True

    def xǁAgentRuntimeǁterminate_agent__mutmut_20(self, agent_id: str, force: bool = False) -> bool:
        """Terminate an agent by ID.

        Args:
            agent_id: The agent to terminate.
            force: If True, force-terminate even if agent is in an active state.

        Returns:
            True if termination was successful.
        """
        with self._agent_lock:
            agent = self._agents.get(agent_id)
            if agent is None:
                return False

            if force:
                agent.force_state(AgentState.TERMINATED)
            else:
                if not agent.terminate():
                    logger.warning("Cannot terminate agent %s in state %s", agent_id, agent.state)
                    return False

            # Terminate all children first
            for child_id in list(agent._child_ids):
                self.terminate_agent(child_id, force=None)

            self._fire_hook("on_terminate", agent)
            del self._agents[agent_id]
            self._stats.total_terminated += 1
            self._stats.active_count = len(self._agents)
            logger.info("Agent terminated: %s", agent_id)
            return True

    def xǁAgentRuntimeǁterminate_agent__mutmut_21(self, agent_id: str, force: bool = False) -> bool:
        """Terminate an agent by ID.

        Args:
            agent_id: The agent to terminate.
            force: If True, force-terminate even if agent is in an active state.

        Returns:
            True if termination was successful.
        """
        with self._agent_lock:
            agent = self._agents.get(agent_id)
            if agent is None:
                return False

            if force:
                agent.force_state(AgentState.TERMINATED)
            else:
                if not agent.terminate():
                    logger.warning("Cannot terminate agent %s in state %s", agent_id, agent.state)
                    return False

            # Terminate all children first
            for child_id in list(agent._child_ids):
                self.terminate_agent(force=True)

            self._fire_hook("on_terminate", agent)
            del self._agents[agent_id]
            self._stats.total_terminated += 1
            self._stats.active_count = len(self._agents)
            logger.info("Agent terminated: %s", agent_id)
            return True

    def xǁAgentRuntimeǁterminate_agent__mutmut_22(self, agent_id: str, force: bool = False) -> bool:
        """Terminate an agent by ID.

        Args:
            agent_id: The agent to terminate.
            force: If True, force-terminate even if agent is in an active state.

        Returns:
            True if termination was successful.
        """
        with self._agent_lock:
            agent = self._agents.get(agent_id)
            if agent is None:
                return False

            if force:
                agent.force_state(AgentState.TERMINATED)
            else:
                if not agent.terminate():
                    logger.warning("Cannot terminate agent %s in state %s", agent_id, agent.state)
                    return False

            # Terminate all children first
            for child_id in list(agent._child_ids):
                self.terminate_agent(child_id, )

            self._fire_hook("on_terminate", agent)
            del self._agents[agent_id]
            self._stats.total_terminated += 1
            self._stats.active_count = len(self._agents)
            logger.info("Agent terminated: %s", agent_id)
            return True

    def xǁAgentRuntimeǁterminate_agent__mutmut_23(self, agent_id: str, force: bool = False) -> bool:
        """Terminate an agent by ID.

        Args:
            agent_id: The agent to terminate.
            force: If True, force-terminate even if agent is in an active state.

        Returns:
            True if termination was successful.
        """
        with self._agent_lock:
            agent = self._agents.get(agent_id)
            if agent is None:
                return False

            if force:
                agent.force_state(AgentState.TERMINATED)
            else:
                if not agent.terminate():
                    logger.warning("Cannot terminate agent %s in state %s", agent_id, agent.state)
                    return False

            # Terminate all children first
            for child_id in list(agent._child_ids):
                self.terminate_agent(child_id, force=False)

            self._fire_hook("on_terminate", agent)
            del self._agents[agent_id]
            self._stats.total_terminated += 1
            self._stats.active_count = len(self._agents)
            logger.info("Agent terminated: %s", agent_id)
            return True

    def xǁAgentRuntimeǁterminate_agent__mutmut_24(self, agent_id: str, force: bool = False) -> bool:
        """Terminate an agent by ID.

        Args:
            agent_id: The agent to terminate.
            force: If True, force-terminate even if agent is in an active state.

        Returns:
            True if termination was successful.
        """
        with self._agent_lock:
            agent = self._agents.get(agent_id)
            if agent is None:
                return False

            if force:
                agent.force_state(AgentState.TERMINATED)
            else:
                if not agent.terminate():
                    logger.warning("Cannot terminate agent %s in state %s", agent_id, agent.state)
                    return False

            # Terminate all children first
            for child_id in list(agent._child_ids):
                self.terminate_agent(child_id, force=True)

            self._fire_hook(None, agent)
            del self._agents[agent_id]
            self._stats.total_terminated += 1
            self._stats.active_count = len(self._agents)
            logger.info("Agent terminated: %s", agent_id)
            return True

    def xǁAgentRuntimeǁterminate_agent__mutmut_25(self, agent_id: str, force: bool = False) -> bool:
        """Terminate an agent by ID.

        Args:
            agent_id: The agent to terminate.
            force: If True, force-terminate even if agent is in an active state.

        Returns:
            True if termination was successful.
        """
        with self._agent_lock:
            agent = self._agents.get(agent_id)
            if agent is None:
                return False

            if force:
                agent.force_state(AgentState.TERMINATED)
            else:
                if not agent.terminate():
                    logger.warning("Cannot terminate agent %s in state %s", agent_id, agent.state)
                    return False

            # Terminate all children first
            for child_id in list(agent._child_ids):
                self.terminate_agent(child_id, force=True)

            self._fire_hook("on_terminate", None)
            del self._agents[agent_id]
            self._stats.total_terminated += 1
            self._stats.active_count = len(self._agents)
            logger.info("Agent terminated: %s", agent_id)
            return True

    def xǁAgentRuntimeǁterminate_agent__mutmut_26(self, agent_id: str, force: bool = False) -> bool:
        """Terminate an agent by ID.

        Args:
            agent_id: The agent to terminate.
            force: If True, force-terminate even if agent is in an active state.

        Returns:
            True if termination was successful.
        """
        with self._agent_lock:
            agent = self._agents.get(agent_id)
            if agent is None:
                return False

            if force:
                agent.force_state(AgentState.TERMINATED)
            else:
                if not agent.terminate():
                    logger.warning("Cannot terminate agent %s in state %s", agent_id, agent.state)
                    return False

            # Terminate all children first
            for child_id in list(agent._child_ids):
                self.terminate_agent(child_id, force=True)

            self._fire_hook(agent)
            del self._agents[agent_id]
            self._stats.total_terminated += 1
            self._stats.active_count = len(self._agents)
            logger.info("Agent terminated: %s", agent_id)
            return True

    def xǁAgentRuntimeǁterminate_agent__mutmut_27(self, agent_id: str, force: bool = False) -> bool:
        """Terminate an agent by ID.

        Args:
            agent_id: The agent to terminate.
            force: If True, force-terminate even if agent is in an active state.

        Returns:
            True if termination was successful.
        """
        with self._agent_lock:
            agent = self._agents.get(agent_id)
            if agent is None:
                return False

            if force:
                agent.force_state(AgentState.TERMINATED)
            else:
                if not agent.terminate():
                    logger.warning("Cannot terminate agent %s in state %s", agent_id, agent.state)
                    return False

            # Terminate all children first
            for child_id in list(agent._child_ids):
                self.terminate_agent(child_id, force=True)

            self._fire_hook("on_terminate", )
            del self._agents[agent_id]
            self._stats.total_terminated += 1
            self._stats.active_count = len(self._agents)
            logger.info("Agent terminated: %s", agent_id)
            return True

    def xǁAgentRuntimeǁterminate_agent__mutmut_28(self, agent_id: str, force: bool = False) -> bool:
        """Terminate an agent by ID.

        Args:
            agent_id: The agent to terminate.
            force: If True, force-terminate even if agent is in an active state.

        Returns:
            True if termination was successful.
        """
        with self._agent_lock:
            agent = self._agents.get(agent_id)
            if agent is None:
                return False

            if force:
                agent.force_state(AgentState.TERMINATED)
            else:
                if not agent.terminate():
                    logger.warning("Cannot terminate agent %s in state %s", agent_id, agent.state)
                    return False

            # Terminate all children first
            for child_id in list(agent._child_ids):
                self.terminate_agent(child_id, force=True)

            self._fire_hook("XXon_terminateXX", agent)
            del self._agents[agent_id]
            self._stats.total_terminated += 1
            self._stats.active_count = len(self._agents)
            logger.info("Agent terminated: %s", agent_id)
            return True

    def xǁAgentRuntimeǁterminate_agent__mutmut_29(self, agent_id: str, force: bool = False) -> bool:
        """Terminate an agent by ID.

        Args:
            agent_id: The agent to terminate.
            force: If True, force-terminate even if agent is in an active state.

        Returns:
            True if termination was successful.
        """
        with self._agent_lock:
            agent = self._agents.get(agent_id)
            if agent is None:
                return False

            if force:
                agent.force_state(AgentState.TERMINATED)
            else:
                if not agent.terminate():
                    logger.warning("Cannot terminate agent %s in state %s", agent_id, agent.state)
                    return False

            # Terminate all children first
            for child_id in list(agent._child_ids):
                self.terminate_agent(child_id, force=True)

            self._fire_hook("ON_TERMINATE", agent)
            del self._agents[agent_id]
            self._stats.total_terminated += 1
            self._stats.active_count = len(self._agents)
            logger.info("Agent terminated: %s", agent_id)
            return True

    def xǁAgentRuntimeǁterminate_agent__mutmut_30(self, agent_id: str, force: bool = False) -> bool:
        """Terminate an agent by ID.

        Args:
            agent_id: The agent to terminate.
            force: If True, force-terminate even if agent is in an active state.

        Returns:
            True if termination was successful.
        """
        with self._agent_lock:
            agent = self._agents.get(agent_id)
            if agent is None:
                return False

            if force:
                agent.force_state(AgentState.TERMINATED)
            else:
                if not agent.terminate():
                    logger.warning("Cannot terminate agent %s in state %s", agent_id, agent.state)
                    return False

            # Terminate all children first
            for child_id in list(agent._child_ids):
                self.terminate_agent(child_id, force=True)

            self._fire_hook("on_terminate", agent)
            del self._agents[agent_id]
            self._stats.total_terminated = 1
            self._stats.active_count = len(self._agents)
            logger.info("Agent terminated: %s", agent_id)
            return True

    def xǁAgentRuntimeǁterminate_agent__mutmut_31(self, agent_id: str, force: bool = False) -> bool:
        """Terminate an agent by ID.

        Args:
            agent_id: The agent to terminate.
            force: If True, force-terminate even if agent is in an active state.

        Returns:
            True if termination was successful.
        """
        with self._agent_lock:
            agent = self._agents.get(agent_id)
            if agent is None:
                return False

            if force:
                agent.force_state(AgentState.TERMINATED)
            else:
                if not agent.terminate():
                    logger.warning("Cannot terminate agent %s in state %s", agent_id, agent.state)
                    return False

            # Terminate all children first
            for child_id in list(agent._child_ids):
                self.terminate_agent(child_id, force=True)

            self._fire_hook("on_terminate", agent)
            del self._agents[agent_id]
            self._stats.total_terminated -= 1
            self._stats.active_count = len(self._agents)
            logger.info("Agent terminated: %s", agent_id)
            return True

    def xǁAgentRuntimeǁterminate_agent__mutmut_32(self, agent_id: str, force: bool = False) -> bool:
        """Terminate an agent by ID.

        Args:
            agent_id: The agent to terminate.
            force: If True, force-terminate even if agent is in an active state.

        Returns:
            True if termination was successful.
        """
        with self._agent_lock:
            agent = self._agents.get(agent_id)
            if agent is None:
                return False

            if force:
                agent.force_state(AgentState.TERMINATED)
            else:
                if not agent.terminate():
                    logger.warning("Cannot terminate agent %s in state %s", agent_id, agent.state)
                    return False

            # Terminate all children first
            for child_id in list(agent._child_ids):
                self.terminate_agent(child_id, force=True)

            self._fire_hook("on_terminate", agent)
            del self._agents[agent_id]
            self._stats.total_terminated += 2
            self._stats.active_count = len(self._agents)
            logger.info("Agent terminated: %s", agent_id)
            return True

    def xǁAgentRuntimeǁterminate_agent__mutmut_33(self, agent_id: str, force: bool = False) -> bool:
        """Terminate an agent by ID.

        Args:
            agent_id: The agent to terminate.
            force: If True, force-terminate even if agent is in an active state.

        Returns:
            True if termination was successful.
        """
        with self._agent_lock:
            agent = self._agents.get(agent_id)
            if agent is None:
                return False

            if force:
                agent.force_state(AgentState.TERMINATED)
            else:
                if not agent.terminate():
                    logger.warning("Cannot terminate agent %s in state %s", agent_id, agent.state)
                    return False

            # Terminate all children first
            for child_id in list(agent._child_ids):
                self.terminate_agent(child_id, force=True)

            self._fire_hook("on_terminate", agent)
            del self._agents[agent_id]
            self._stats.total_terminated += 1
            self._stats.active_count = None
            logger.info("Agent terminated: %s", agent_id)
            return True

    def xǁAgentRuntimeǁterminate_agent__mutmut_34(self, agent_id: str, force: bool = False) -> bool:
        """Terminate an agent by ID.

        Args:
            agent_id: The agent to terminate.
            force: If True, force-terminate even if agent is in an active state.

        Returns:
            True if termination was successful.
        """
        with self._agent_lock:
            agent = self._agents.get(agent_id)
            if agent is None:
                return False

            if force:
                agent.force_state(AgentState.TERMINATED)
            else:
                if not agent.terminate():
                    logger.warning("Cannot terminate agent %s in state %s", agent_id, agent.state)
                    return False

            # Terminate all children first
            for child_id in list(agent._child_ids):
                self.terminate_agent(child_id, force=True)

            self._fire_hook("on_terminate", agent)
            del self._agents[agent_id]
            self._stats.total_terminated += 1
            self._stats.active_count = len(self._agents)
            logger.info(None, agent_id)
            return True

    def xǁAgentRuntimeǁterminate_agent__mutmut_35(self, agent_id: str, force: bool = False) -> bool:
        """Terminate an agent by ID.

        Args:
            agent_id: The agent to terminate.
            force: If True, force-terminate even if agent is in an active state.

        Returns:
            True if termination was successful.
        """
        with self._agent_lock:
            agent = self._agents.get(agent_id)
            if agent is None:
                return False

            if force:
                agent.force_state(AgentState.TERMINATED)
            else:
                if not agent.terminate():
                    logger.warning("Cannot terminate agent %s in state %s", agent_id, agent.state)
                    return False

            # Terminate all children first
            for child_id in list(agent._child_ids):
                self.terminate_agent(child_id, force=True)

            self._fire_hook("on_terminate", agent)
            del self._agents[agent_id]
            self._stats.total_terminated += 1
            self._stats.active_count = len(self._agents)
            logger.info("Agent terminated: %s", None)
            return True

    def xǁAgentRuntimeǁterminate_agent__mutmut_36(self, agent_id: str, force: bool = False) -> bool:
        """Terminate an agent by ID.

        Args:
            agent_id: The agent to terminate.
            force: If True, force-terminate even if agent is in an active state.

        Returns:
            True if termination was successful.
        """
        with self._agent_lock:
            agent = self._agents.get(agent_id)
            if agent is None:
                return False

            if force:
                agent.force_state(AgentState.TERMINATED)
            else:
                if not agent.terminate():
                    logger.warning("Cannot terminate agent %s in state %s", agent_id, agent.state)
                    return False

            # Terminate all children first
            for child_id in list(agent._child_ids):
                self.terminate_agent(child_id, force=True)

            self._fire_hook("on_terminate", agent)
            del self._agents[agent_id]
            self._stats.total_terminated += 1
            self._stats.active_count = len(self._agents)
            logger.info(agent_id)
            return True

    def xǁAgentRuntimeǁterminate_agent__mutmut_37(self, agent_id: str, force: bool = False) -> bool:
        """Terminate an agent by ID.

        Args:
            agent_id: The agent to terminate.
            force: If True, force-terminate even if agent is in an active state.

        Returns:
            True if termination was successful.
        """
        with self._agent_lock:
            agent = self._agents.get(agent_id)
            if agent is None:
                return False

            if force:
                agent.force_state(AgentState.TERMINATED)
            else:
                if not agent.terminate():
                    logger.warning("Cannot terminate agent %s in state %s", agent_id, agent.state)
                    return False

            # Terminate all children first
            for child_id in list(agent._child_ids):
                self.terminate_agent(child_id, force=True)

            self._fire_hook("on_terminate", agent)
            del self._agents[agent_id]
            self._stats.total_terminated += 1
            self._stats.active_count = len(self._agents)
            logger.info("Agent terminated: %s", )
            return True

    def xǁAgentRuntimeǁterminate_agent__mutmut_38(self, agent_id: str, force: bool = False) -> bool:
        """Terminate an agent by ID.

        Args:
            agent_id: The agent to terminate.
            force: If True, force-terminate even if agent is in an active state.

        Returns:
            True if termination was successful.
        """
        with self._agent_lock:
            agent = self._agents.get(agent_id)
            if agent is None:
                return False

            if force:
                agent.force_state(AgentState.TERMINATED)
            else:
                if not agent.terminate():
                    logger.warning("Cannot terminate agent %s in state %s", agent_id, agent.state)
                    return False

            # Terminate all children first
            for child_id in list(agent._child_ids):
                self.terminate_agent(child_id, force=True)

            self._fire_hook("on_terminate", agent)
            del self._agents[agent_id]
            self._stats.total_terminated += 1
            self._stats.active_count = len(self._agents)
            logger.info("XXAgent terminated: %sXX", agent_id)
            return True

    def xǁAgentRuntimeǁterminate_agent__mutmut_39(self, agent_id: str, force: bool = False) -> bool:
        """Terminate an agent by ID.

        Args:
            agent_id: The agent to terminate.
            force: If True, force-terminate even if agent is in an active state.

        Returns:
            True if termination was successful.
        """
        with self._agent_lock:
            agent = self._agents.get(agent_id)
            if agent is None:
                return False

            if force:
                agent.force_state(AgentState.TERMINATED)
            else:
                if not agent.terminate():
                    logger.warning("Cannot terminate agent %s in state %s", agent_id, agent.state)
                    return False

            # Terminate all children first
            for child_id in list(agent._child_ids):
                self.terminate_agent(child_id, force=True)

            self._fire_hook("on_terminate", agent)
            del self._agents[agent_id]
            self._stats.total_terminated += 1
            self._stats.active_count = len(self._agents)
            logger.info("agent terminated: %s", agent_id)
            return True

    def xǁAgentRuntimeǁterminate_agent__mutmut_40(self, agent_id: str, force: bool = False) -> bool:
        """Terminate an agent by ID.

        Args:
            agent_id: The agent to terminate.
            force: If True, force-terminate even if agent is in an active state.

        Returns:
            True if termination was successful.
        """
        with self._agent_lock:
            agent = self._agents.get(agent_id)
            if agent is None:
                return False

            if force:
                agent.force_state(AgentState.TERMINATED)
            else:
                if not agent.terminate():
                    logger.warning("Cannot terminate agent %s in state %s", agent_id, agent.state)
                    return False

            # Terminate all children first
            for child_id in list(agent._child_ids):
                self.terminate_agent(child_id, force=True)

            self._fire_hook("on_terminate", agent)
            del self._agents[agent_id]
            self._stats.total_terminated += 1
            self._stats.active_count = len(self._agents)
            logger.info("AGENT TERMINATED: %S", agent_id)
            return True

    def xǁAgentRuntimeǁterminate_agent__mutmut_41(self, agent_id: str, force: bool = False) -> bool:
        """Terminate an agent by ID.

        Args:
            agent_id: The agent to terminate.
            force: If True, force-terminate even if agent is in an active state.

        Returns:
            True if termination was successful.
        """
        with self._agent_lock:
            agent = self._agents.get(agent_id)
            if agent is None:
                return False

            if force:
                agent.force_state(AgentState.TERMINATED)
            else:
                if not agent.terminate():
                    logger.warning("Cannot terminate agent %s in state %s", agent_id, agent.state)
                    return False

            # Terminate all children first
            for child_id in list(agent._child_ids):
                self.terminate_agent(child_id, force=True)

            self._fire_hook("on_terminate", agent)
            del self._agents[agent_id]
            self._stats.total_terminated += 1
            self._stats.active_count = len(self._agents)
            logger.info("Agent terminated: %s", agent_id)
            return False

    @_mutmut_mutated(mutants_xǁAgentRuntimeǁpause_agent__mutmut)
    def pause_agent(self, agent_id: str) -> bool:
        """Pause an active agent."""
        agent = self._agents.get(agent_id)
        if agent and agent.pause():
            self._fire_hook("on_pause", agent)
            return True
        return False

    def xǁAgentRuntimeǁpause_agent__mutmut_orig(self, agent_id: str) -> bool:
        """Pause an active agent."""
        agent = self._agents.get(agent_id)
        if agent and agent.pause():
            self._fire_hook("on_pause", agent)
            return True
        return False

    def xǁAgentRuntimeǁpause_agent__mutmut_1(self, agent_id: str) -> bool:
        """Pause an active agent."""
        agent = None
        if agent and agent.pause():
            self._fire_hook("on_pause", agent)
            return True
        return False

    def xǁAgentRuntimeǁpause_agent__mutmut_2(self, agent_id: str) -> bool:
        """Pause an active agent."""
        agent = self._agents.get(None)
        if agent and agent.pause():
            self._fire_hook("on_pause", agent)
            return True
        return False

    def xǁAgentRuntimeǁpause_agent__mutmut_3(self, agent_id: str) -> bool:
        """Pause an active agent."""
        agent = self._agents.get(agent_id)
        if agent or agent.pause():
            self._fire_hook("on_pause", agent)
            return True
        return False

    def xǁAgentRuntimeǁpause_agent__mutmut_4(self, agent_id: str) -> bool:
        """Pause an active agent."""
        agent = self._agents.get(agent_id)
        if agent and agent.pause():
            self._fire_hook(None, agent)
            return True
        return False

    def xǁAgentRuntimeǁpause_agent__mutmut_5(self, agent_id: str) -> bool:
        """Pause an active agent."""
        agent = self._agents.get(agent_id)
        if agent and agent.pause():
            self._fire_hook("on_pause", None)
            return True
        return False

    def xǁAgentRuntimeǁpause_agent__mutmut_6(self, agent_id: str) -> bool:
        """Pause an active agent."""
        agent = self._agents.get(agent_id)
        if agent and agent.pause():
            self._fire_hook(agent)
            return True
        return False

    def xǁAgentRuntimeǁpause_agent__mutmut_7(self, agent_id: str) -> bool:
        """Pause an active agent."""
        agent = self._agents.get(agent_id)
        if agent and agent.pause():
            self._fire_hook("on_pause", )
            return True
        return False

    def xǁAgentRuntimeǁpause_agent__mutmut_8(self, agent_id: str) -> bool:
        """Pause an active agent."""
        agent = self._agents.get(agent_id)
        if agent and agent.pause():
            self._fire_hook("XXon_pauseXX", agent)
            return True
        return False

    def xǁAgentRuntimeǁpause_agent__mutmut_9(self, agent_id: str) -> bool:
        """Pause an active agent."""
        agent = self._agents.get(agent_id)
        if agent and agent.pause():
            self._fire_hook("ON_PAUSE", agent)
            return True
        return False

    def xǁAgentRuntimeǁpause_agent__mutmut_10(self, agent_id: str) -> bool:
        """Pause an active agent."""
        agent = self._agents.get(agent_id)
        if agent and agent.pause():
            self._fire_hook("on_pause", agent)
            return False
        return False

    def xǁAgentRuntimeǁpause_agent__mutmut_11(self, agent_id: str) -> bool:
        """Pause an active agent."""
        agent = self._agents.get(agent_id)
        if agent and agent.pause():
            self._fire_hook("on_pause", agent)
            return True
        return True

    @_mutmut_mutated(mutants_xǁAgentRuntimeǁresume_agent__mutmut)
    def resume_agent(self, agent_id: str) -> bool:
        """Resume a paused agent."""
        agent = self._agents.get(agent_id)
        if agent and agent.resume():
            self._fire_hook("on_resume", agent)
            return True
        return False

    def xǁAgentRuntimeǁresume_agent__mutmut_orig(self, agent_id: str) -> bool:
        """Resume a paused agent."""
        agent = self._agents.get(agent_id)
        if agent and agent.resume():
            self._fire_hook("on_resume", agent)
            return True
        return False

    def xǁAgentRuntimeǁresume_agent__mutmut_1(self, agent_id: str) -> bool:
        """Resume a paused agent."""
        agent = None
        if agent and agent.resume():
            self._fire_hook("on_resume", agent)
            return True
        return False

    def xǁAgentRuntimeǁresume_agent__mutmut_2(self, agent_id: str) -> bool:
        """Resume a paused agent."""
        agent = self._agents.get(None)
        if agent and agent.resume():
            self._fire_hook("on_resume", agent)
            return True
        return False

    def xǁAgentRuntimeǁresume_agent__mutmut_3(self, agent_id: str) -> bool:
        """Resume a paused agent."""
        agent = self._agents.get(agent_id)
        if agent or agent.resume():
            self._fire_hook("on_resume", agent)
            return True
        return False

    def xǁAgentRuntimeǁresume_agent__mutmut_4(self, agent_id: str) -> bool:
        """Resume a paused agent."""
        agent = self._agents.get(agent_id)
        if agent and agent.resume():
            self._fire_hook(None, agent)
            return True
        return False

    def xǁAgentRuntimeǁresume_agent__mutmut_5(self, agent_id: str) -> bool:
        """Resume a paused agent."""
        agent = self._agents.get(agent_id)
        if agent and agent.resume():
            self._fire_hook("on_resume", None)
            return True
        return False

    def xǁAgentRuntimeǁresume_agent__mutmut_6(self, agent_id: str) -> bool:
        """Resume a paused agent."""
        agent = self._agents.get(agent_id)
        if agent and agent.resume():
            self._fire_hook(agent)
            return True
        return False

    def xǁAgentRuntimeǁresume_agent__mutmut_7(self, agent_id: str) -> bool:
        """Resume a paused agent."""
        agent = self._agents.get(agent_id)
        if agent and agent.resume():
            self._fire_hook("on_resume", )
            return True
        return False

    def xǁAgentRuntimeǁresume_agent__mutmut_8(self, agent_id: str) -> bool:
        """Resume a paused agent."""
        agent = self._agents.get(agent_id)
        if agent and agent.resume():
            self._fire_hook("XXon_resumeXX", agent)
            return True
        return False

    def xǁAgentRuntimeǁresume_agent__mutmut_9(self, agent_id: str) -> bool:
        """Resume a paused agent."""
        agent = self._agents.get(agent_id)
        if agent and agent.resume():
            self._fire_hook("ON_RESUME", agent)
            return True
        return False

    def xǁAgentRuntimeǁresume_agent__mutmut_10(self, agent_id: str) -> bool:
        """Resume a paused agent."""
        agent = self._agents.get(agent_id)
        if agent and agent.resume():
            self._fire_hook("on_resume", agent)
            return False
        return False

    def xǁAgentRuntimeǁresume_agent__mutmut_11(self, agent_id: str) -> bool:
        """Resume a paused agent."""
        agent = self._agents.get(agent_id)
        if agent and agent.resume():
            self._fire_hook("on_resume", agent)
            return True
        return True

    # ── Lookup ──────────────────────────────────────────────

    @_mutmut_mutated(mutants_xǁAgentRuntimeǁget_agent__mutmut)
    def get_agent(self, agent_id: str) -> BaseAgent | None:
        """Get an agent by ID."""
        return self._agents.get(agent_id)

    # ── Lookup ──────────────────────────────────────────────

    def xǁAgentRuntimeǁget_agent__mutmut_orig(self, agent_id: str) -> BaseAgent | None:
        """Get an agent by ID."""
        return self._agents.get(agent_id)

    # ── Lookup ──────────────────────────────────────────────

    def xǁAgentRuntimeǁget_agent__mutmut_1(self, agent_id: str) -> BaseAgent | None:
        """Get an agent by ID."""
        return self._agents.get(None)

    @_mutmut_mutated(mutants_xǁAgentRuntimeǁlist_agents__mutmut)
    def list_agents(
        self,
        state: AgentState | None = None,
        capability: str | None = None,
    ) -> list[BaseAgent]:
        """List agents, optionally filtered by state or capability.

        Args:
            state: Filter by agent state.
            capability: Filter by capability name.

        Returns:
            List of matching agents.
        """
        agents = list(self._agents.values())
        if state is not None:
            agents = [a for a in agents if a.state == state]
        if capability is not None:
            agents = [a for a in agents if any(c.value == capability for c in a.capabilities)]
        return agents

    def xǁAgentRuntimeǁlist_agents__mutmut_orig(
        self,
        state: AgentState | None = None,
        capability: str | None = None,
    ) -> list[BaseAgent]:
        """List agents, optionally filtered by state or capability.

        Args:
            state: Filter by agent state.
            capability: Filter by capability name.

        Returns:
            List of matching agents.
        """
        agents = list(self._agents.values())
        if state is not None:
            agents = [a for a in agents if a.state == state]
        if capability is not None:
            agents = [a for a in agents if any(c.value == capability for c in a.capabilities)]
        return agents

    def xǁAgentRuntimeǁlist_agents__mutmut_1(
        self,
        state: AgentState | None = None,
        capability: str | None = None,
    ) -> list[BaseAgent]:
        """List agents, optionally filtered by state or capability.

        Args:
            state: Filter by agent state.
            capability: Filter by capability name.

        Returns:
            List of matching agents.
        """
        agents = None
        if state is not None:
            agents = [a for a in agents if a.state == state]
        if capability is not None:
            agents = [a for a in agents if any(c.value == capability for c in a.capabilities)]
        return agents

    def xǁAgentRuntimeǁlist_agents__mutmut_2(
        self,
        state: AgentState | None = None,
        capability: str | None = None,
    ) -> list[BaseAgent]:
        """List agents, optionally filtered by state or capability.

        Args:
            state: Filter by agent state.
            capability: Filter by capability name.

        Returns:
            List of matching agents.
        """
        agents = list(None)
        if state is not None:
            agents = [a for a in agents if a.state == state]
        if capability is not None:
            agents = [a for a in agents if any(c.value == capability for c in a.capabilities)]
        return agents

    def xǁAgentRuntimeǁlist_agents__mutmut_3(
        self,
        state: AgentState | None = None,
        capability: str | None = None,
    ) -> list[BaseAgent]:
        """List agents, optionally filtered by state or capability.

        Args:
            state: Filter by agent state.
            capability: Filter by capability name.

        Returns:
            List of matching agents.
        """
        agents = list(self._agents.values())
        if state is None:
            agents = [a for a in agents if a.state == state]
        if capability is not None:
            agents = [a for a in agents if any(c.value == capability for c in a.capabilities)]
        return agents

    def xǁAgentRuntimeǁlist_agents__mutmut_4(
        self,
        state: AgentState | None = None,
        capability: str | None = None,
    ) -> list[BaseAgent]:
        """List agents, optionally filtered by state or capability.

        Args:
            state: Filter by agent state.
            capability: Filter by capability name.

        Returns:
            List of matching agents.
        """
        agents = list(self._agents.values())
        if state is not None:
            agents = None
        if capability is not None:
            agents = [a for a in agents if any(c.value == capability for c in a.capabilities)]
        return agents

    def xǁAgentRuntimeǁlist_agents__mutmut_5(
        self,
        state: AgentState | None = None,
        capability: str | None = None,
    ) -> list[BaseAgent]:
        """List agents, optionally filtered by state or capability.

        Args:
            state: Filter by agent state.
            capability: Filter by capability name.

        Returns:
            List of matching agents.
        """
        agents = list(self._agents.values())
        if state is not None:
            agents = [a for a in agents if a.state != state]
        if capability is not None:
            agents = [a for a in agents if any(c.value == capability for c in a.capabilities)]
        return agents

    def xǁAgentRuntimeǁlist_agents__mutmut_6(
        self,
        state: AgentState | None = None,
        capability: str | None = None,
    ) -> list[BaseAgent]:
        """List agents, optionally filtered by state or capability.

        Args:
            state: Filter by agent state.
            capability: Filter by capability name.

        Returns:
            List of matching agents.
        """
        agents = list(self._agents.values())
        if state is not None:
            agents = [a for a in agents if a.state == state]
        if capability is None:
            agents = [a for a in agents if any(c.value == capability for c in a.capabilities)]
        return agents

    def xǁAgentRuntimeǁlist_agents__mutmut_7(
        self,
        state: AgentState | None = None,
        capability: str | None = None,
    ) -> list[BaseAgent]:
        """List agents, optionally filtered by state or capability.

        Args:
            state: Filter by agent state.
            capability: Filter by capability name.

        Returns:
            List of matching agents.
        """
        agents = list(self._agents.values())
        if state is not None:
            agents = [a for a in agents if a.state == state]
        if capability is not None:
            agents = None
        return agents

    def xǁAgentRuntimeǁlist_agents__mutmut_8(
        self,
        state: AgentState | None = None,
        capability: str | None = None,
    ) -> list[BaseAgent]:
        """List agents, optionally filtered by state or capability.

        Args:
            state: Filter by agent state.
            capability: Filter by capability name.

        Returns:
            List of matching agents.
        """
        agents = list(self._agents.values())
        if state is not None:
            agents = [a for a in agents if a.state == state]
        if capability is not None:
            agents = [a for a in agents if any(None)]
        return agents

    def xǁAgentRuntimeǁlist_agents__mutmut_9(
        self,
        state: AgentState | None = None,
        capability: str | None = None,
    ) -> list[BaseAgent]:
        """List agents, optionally filtered by state or capability.

        Args:
            state: Filter by agent state.
            capability: Filter by capability name.

        Returns:
            List of matching agents.
        """
        agents = list(self._agents.values())
        if state is not None:
            agents = [a for a in agents if a.state == state]
        if capability is not None:
            agents = [a for a in agents if any(c.value != capability for c in a.capabilities)]
        return agents

    @_mutmut_mutated(mutants_xǁAgentRuntimeǁget_agent_status__mutmut)
    def get_agent_status(self, agent_id: str) -> dict[str, Any] | None:
        """Get detailed status for an agent."""
        agent = self._agents.get(agent_id)
        if agent is None:
            return None
        return agent.get_status()

    def xǁAgentRuntimeǁget_agent_status__mutmut_orig(self, agent_id: str) -> dict[str, Any] | None:
        """Get detailed status for an agent."""
        agent = self._agents.get(agent_id)
        if agent is None:
            return None
        return agent.get_status()

    def xǁAgentRuntimeǁget_agent_status__mutmut_1(self, agent_id: str) -> dict[str, Any] | None:
        """Get detailed status for an agent."""
        agent = None
        if agent is None:
            return None
        return agent.get_status()

    def xǁAgentRuntimeǁget_agent_status__mutmut_2(self, agent_id: str) -> dict[str, Any] | None:
        """Get detailed status for an agent."""
        agent = self._agents.get(None)
        if agent is None:
            return None
        return agent.get_status()

    def xǁAgentRuntimeǁget_agent_status__mutmut_3(self, agent_id: str) -> dict[str, Any] | None:
        """Get detailed status for an agent."""
        agent = self._agents.get(agent_id)
        if agent is not None:
            return None
        return agent.get_status()

    # ── Messaging ───────────────────────────────────────────

    @_mutmut_mutated(mutants_xǁAgentRuntimeǁroute_message__mutmut)
    def route_message(self, message: Any) -> bool:
        """Route a message to the target agent.

        Args:
            message: An AgentMessage with a recipient_id field.

        Returns:
            True if the message was delivered successfully.
        """
        recipient_id = getattr(message, "recipient_id", None)
        if recipient_id is None:
            logger.warning("Message has no recipient_id")
            return False

        agent = self._agents.get(recipient_id)
        if agent is None:
            logger.warning("Recipient agent not found: %s", recipient_id)
            return False

        agent.receive_message(message)
        return True

    # ── Messaging ───────────────────────────────────────────

    def xǁAgentRuntimeǁroute_message__mutmut_orig(self, message: Any) -> bool:
        """Route a message to the target agent.

        Args:
            message: An AgentMessage with a recipient_id field.

        Returns:
            True if the message was delivered successfully.
        """
        recipient_id = getattr(message, "recipient_id", None)
        if recipient_id is None:
            logger.warning("Message has no recipient_id")
            return False

        agent = self._agents.get(recipient_id)
        if agent is None:
            logger.warning("Recipient agent not found: %s", recipient_id)
            return False

        agent.receive_message(message)
        return True

    # ── Messaging ───────────────────────────────────────────

    def xǁAgentRuntimeǁroute_message__mutmut_1(self, message: Any) -> bool:
        """Route a message to the target agent.

        Args:
            message: An AgentMessage with a recipient_id field.

        Returns:
            True if the message was delivered successfully.
        """
        recipient_id = None
        if recipient_id is None:
            logger.warning("Message has no recipient_id")
            return False

        agent = self._agents.get(recipient_id)
        if agent is None:
            logger.warning("Recipient agent not found: %s", recipient_id)
            return False

        agent.receive_message(message)
        return True

    # ── Messaging ───────────────────────────────────────────

    def xǁAgentRuntimeǁroute_message__mutmut_2(self, message: Any) -> bool:
        """Route a message to the target agent.

        Args:
            message: An AgentMessage with a recipient_id field.

        Returns:
            True if the message was delivered successfully.
        """
        recipient_id = getattr(None, "recipient_id", None)
        if recipient_id is None:
            logger.warning("Message has no recipient_id")
            return False

        agent = self._agents.get(recipient_id)
        if agent is None:
            logger.warning("Recipient agent not found: %s", recipient_id)
            return False

        agent.receive_message(message)
        return True

    # ── Messaging ───────────────────────────────────────────

    def xǁAgentRuntimeǁroute_message__mutmut_3(self, message: Any) -> bool:
        """Route a message to the target agent.

        Args:
            message: An AgentMessage with a recipient_id field.

        Returns:
            True if the message was delivered successfully.
        """
        recipient_id = getattr(message, None, None)
        if recipient_id is None:
            logger.warning("Message has no recipient_id")
            return False

        agent = self._agents.get(recipient_id)
        if agent is None:
            logger.warning("Recipient agent not found: %s", recipient_id)
            return False

        agent.receive_message(message)
        return True

    # ── Messaging ───────────────────────────────────────────

    def xǁAgentRuntimeǁroute_message__mutmut_4(self, message: Any) -> bool:
        """Route a message to the target agent.

        Args:
            message: An AgentMessage with a recipient_id field.

        Returns:
            True if the message was delivered successfully.
        """
        recipient_id = getattr("recipient_id", None)
        if recipient_id is None:
            logger.warning("Message has no recipient_id")
            return False

        agent = self._agents.get(recipient_id)
        if agent is None:
            logger.warning("Recipient agent not found: %s", recipient_id)
            return False

        agent.receive_message(message)
        return True

    # ── Messaging ───────────────────────────────────────────

    def xǁAgentRuntimeǁroute_message__mutmut_5(self, message: Any) -> bool:
        """Route a message to the target agent.

        Args:
            message: An AgentMessage with a recipient_id field.

        Returns:
            True if the message was delivered successfully.
        """
        recipient_id = getattr(message, None)
        if recipient_id is None:
            logger.warning("Message has no recipient_id")
            return False

        agent = self._agents.get(recipient_id)
        if agent is None:
            logger.warning("Recipient agent not found: %s", recipient_id)
            return False

        agent.receive_message(message)
        return True

    # ── Messaging ───────────────────────────────────────────

    def xǁAgentRuntimeǁroute_message__mutmut_6(self, message: Any) -> bool:
        """Route a message to the target agent.

        Args:
            message: An AgentMessage with a recipient_id field.

        Returns:
            True if the message was delivered successfully.
        """
        recipient_id = getattr(message, "recipient_id", )
        if recipient_id is None:
            logger.warning("Message has no recipient_id")
            return False

        agent = self._agents.get(recipient_id)
        if agent is None:
            logger.warning("Recipient agent not found: %s", recipient_id)
            return False

        agent.receive_message(message)
        return True

    # ── Messaging ───────────────────────────────────────────

    def xǁAgentRuntimeǁroute_message__mutmut_7(self, message: Any) -> bool:
        """Route a message to the target agent.

        Args:
            message: An AgentMessage with a recipient_id field.

        Returns:
            True if the message was delivered successfully.
        """
        recipient_id = getattr(message, "XXrecipient_idXX", None)
        if recipient_id is None:
            logger.warning("Message has no recipient_id")
            return False

        agent = self._agents.get(recipient_id)
        if agent is None:
            logger.warning("Recipient agent not found: %s", recipient_id)
            return False

        agent.receive_message(message)
        return True

    # ── Messaging ───────────────────────────────────────────

    def xǁAgentRuntimeǁroute_message__mutmut_8(self, message: Any) -> bool:
        """Route a message to the target agent.

        Args:
            message: An AgentMessage with a recipient_id field.

        Returns:
            True if the message was delivered successfully.
        """
        recipient_id = getattr(message, "RECIPIENT_ID", None)
        if recipient_id is None:
            logger.warning("Message has no recipient_id")
            return False

        agent = self._agents.get(recipient_id)
        if agent is None:
            logger.warning("Recipient agent not found: %s", recipient_id)
            return False

        agent.receive_message(message)
        return True

    # ── Messaging ───────────────────────────────────────────

    def xǁAgentRuntimeǁroute_message__mutmut_9(self, message: Any) -> bool:
        """Route a message to the target agent.

        Args:
            message: An AgentMessage with a recipient_id field.

        Returns:
            True if the message was delivered successfully.
        """
        recipient_id = getattr(message, "recipient_id", None)
        if recipient_id is not None:
            logger.warning("Message has no recipient_id")
            return False

        agent = self._agents.get(recipient_id)
        if agent is None:
            logger.warning("Recipient agent not found: %s", recipient_id)
            return False

        agent.receive_message(message)
        return True

    # ── Messaging ───────────────────────────────────────────

    def xǁAgentRuntimeǁroute_message__mutmut_10(self, message: Any) -> bool:
        """Route a message to the target agent.

        Args:
            message: An AgentMessage with a recipient_id field.

        Returns:
            True if the message was delivered successfully.
        """
        recipient_id = getattr(message, "recipient_id", None)
        if recipient_id is None:
            logger.warning(None)
            return False

        agent = self._agents.get(recipient_id)
        if agent is None:
            logger.warning("Recipient agent not found: %s", recipient_id)
            return False

        agent.receive_message(message)
        return True

    # ── Messaging ───────────────────────────────────────────

    def xǁAgentRuntimeǁroute_message__mutmut_11(self, message: Any) -> bool:
        """Route a message to the target agent.

        Args:
            message: An AgentMessage with a recipient_id field.

        Returns:
            True if the message was delivered successfully.
        """
        recipient_id = getattr(message, "recipient_id", None)
        if recipient_id is None:
            logger.warning("XXMessage has no recipient_idXX")
            return False

        agent = self._agents.get(recipient_id)
        if agent is None:
            logger.warning("Recipient agent not found: %s", recipient_id)
            return False

        agent.receive_message(message)
        return True

    # ── Messaging ───────────────────────────────────────────

    def xǁAgentRuntimeǁroute_message__mutmut_12(self, message: Any) -> bool:
        """Route a message to the target agent.

        Args:
            message: An AgentMessage with a recipient_id field.

        Returns:
            True if the message was delivered successfully.
        """
        recipient_id = getattr(message, "recipient_id", None)
        if recipient_id is None:
            logger.warning("message has no recipient_id")
            return False

        agent = self._agents.get(recipient_id)
        if agent is None:
            logger.warning("Recipient agent not found: %s", recipient_id)
            return False

        agent.receive_message(message)
        return True

    # ── Messaging ───────────────────────────────────────────

    def xǁAgentRuntimeǁroute_message__mutmut_13(self, message: Any) -> bool:
        """Route a message to the target agent.

        Args:
            message: An AgentMessage with a recipient_id field.

        Returns:
            True if the message was delivered successfully.
        """
        recipient_id = getattr(message, "recipient_id", None)
        if recipient_id is None:
            logger.warning("MESSAGE HAS NO RECIPIENT_ID")
            return False

        agent = self._agents.get(recipient_id)
        if agent is None:
            logger.warning("Recipient agent not found: %s", recipient_id)
            return False

        agent.receive_message(message)
        return True

    # ── Messaging ───────────────────────────────────────────

    def xǁAgentRuntimeǁroute_message__mutmut_14(self, message: Any) -> bool:
        """Route a message to the target agent.

        Args:
            message: An AgentMessage with a recipient_id field.

        Returns:
            True if the message was delivered successfully.
        """
        recipient_id = getattr(message, "recipient_id", None)
        if recipient_id is None:
            logger.warning("Message has no recipient_id")
            return True

        agent = self._agents.get(recipient_id)
        if agent is None:
            logger.warning("Recipient agent not found: %s", recipient_id)
            return False

        agent.receive_message(message)
        return True

    # ── Messaging ───────────────────────────────────────────

    def xǁAgentRuntimeǁroute_message__mutmut_15(self, message: Any) -> bool:
        """Route a message to the target agent.

        Args:
            message: An AgentMessage with a recipient_id field.

        Returns:
            True if the message was delivered successfully.
        """
        recipient_id = getattr(message, "recipient_id", None)
        if recipient_id is None:
            logger.warning("Message has no recipient_id")
            return False

        agent = None
        if agent is None:
            logger.warning("Recipient agent not found: %s", recipient_id)
            return False

        agent.receive_message(message)
        return True

    # ── Messaging ───────────────────────────────────────────

    def xǁAgentRuntimeǁroute_message__mutmut_16(self, message: Any) -> bool:
        """Route a message to the target agent.

        Args:
            message: An AgentMessage with a recipient_id field.

        Returns:
            True if the message was delivered successfully.
        """
        recipient_id = getattr(message, "recipient_id", None)
        if recipient_id is None:
            logger.warning("Message has no recipient_id")
            return False

        agent = self._agents.get(None)
        if agent is None:
            logger.warning("Recipient agent not found: %s", recipient_id)
            return False

        agent.receive_message(message)
        return True

    # ── Messaging ───────────────────────────────────────────

    def xǁAgentRuntimeǁroute_message__mutmut_17(self, message: Any) -> bool:
        """Route a message to the target agent.

        Args:
            message: An AgentMessage with a recipient_id field.

        Returns:
            True if the message was delivered successfully.
        """
        recipient_id = getattr(message, "recipient_id", None)
        if recipient_id is None:
            logger.warning("Message has no recipient_id")
            return False

        agent = self._agents.get(recipient_id)
        if agent is not None:
            logger.warning("Recipient agent not found: %s", recipient_id)
            return False

        agent.receive_message(message)
        return True

    # ── Messaging ───────────────────────────────────────────

    def xǁAgentRuntimeǁroute_message__mutmut_18(self, message: Any) -> bool:
        """Route a message to the target agent.

        Args:
            message: An AgentMessage with a recipient_id field.

        Returns:
            True if the message was delivered successfully.
        """
        recipient_id = getattr(message, "recipient_id", None)
        if recipient_id is None:
            logger.warning("Message has no recipient_id")
            return False

        agent = self._agents.get(recipient_id)
        if agent is None:
            logger.warning(None, recipient_id)
            return False

        agent.receive_message(message)
        return True

    # ── Messaging ───────────────────────────────────────────

    def xǁAgentRuntimeǁroute_message__mutmut_19(self, message: Any) -> bool:
        """Route a message to the target agent.

        Args:
            message: An AgentMessage with a recipient_id field.

        Returns:
            True if the message was delivered successfully.
        """
        recipient_id = getattr(message, "recipient_id", None)
        if recipient_id is None:
            logger.warning("Message has no recipient_id")
            return False

        agent = self._agents.get(recipient_id)
        if agent is None:
            logger.warning("Recipient agent not found: %s", None)
            return False

        agent.receive_message(message)
        return True

    # ── Messaging ───────────────────────────────────────────

    def xǁAgentRuntimeǁroute_message__mutmut_20(self, message: Any) -> bool:
        """Route a message to the target agent.

        Args:
            message: An AgentMessage with a recipient_id field.

        Returns:
            True if the message was delivered successfully.
        """
        recipient_id = getattr(message, "recipient_id", None)
        if recipient_id is None:
            logger.warning("Message has no recipient_id")
            return False

        agent = self._agents.get(recipient_id)
        if agent is None:
            logger.warning(recipient_id)
            return False

        agent.receive_message(message)
        return True

    # ── Messaging ───────────────────────────────────────────

    def xǁAgentRuntimeǁroute_message__mutmut_21(self, message: Any) -> bool:
        """Route a message to the target agent.

        Args:
            message: An AgentMessage with a recipient_id field.

        Returns:
            True if the message was delivered successfully.
        """
        recipient_id = getattr(message, "recipient_id", None)
        if recipient_id is None:
            logger.warning("Message has no recipient_id")
            return False

        agent = self._agents.get(recipient_id)
        if agent is None:
            logger.warning("Recipient agent not found: %s", )
            return False

        agent.receive_message(message)
        return True

    # ── Messaging ───────────────────────────────────────────

    def xǁAgentRuntimeǁroute_message__mutmut_22(self, message: Any) -> bool:
        """Route a message to the target agent.

        Args:
            message: An AgentMessage with a recipient_id field.

        Returns:
            True if the message was delivered successfully.
        """
        recipient_id = getattr(message, "recipient_id", None)
        if recipient_id is None:
            logger.warning("Message has no recipient_id")
            return False

        agent = self._agents.get(recipient_id)
        if agent is None:
            logger.warning("XXRecipient agent not found: %sXX", recipient_id)
            return False

        agent.receive_message(message)
        return True

    # ── Messaging ───────────────────────────────────────────

    def xǁAgentRuntimeǁroute_message__mutmut_23(self, message: Any) -> bool:
        """Route a message to the target agent.

        Args:
            message: An AgentMessage with a recipient_id field.

        Returns:
            True if the message was delivered successfully.
        """
        recipient_id = getattr(message, "recipient_id", None)
        if recipient_id is None:
            logger.warning("Message has no recipient_id")
            return False

        agent = self._agents.get(recipient_id)
        if agent is None:
            logger.warning("recipient agent not found: %s", recipient_id)
            return False

        agent.receive_message(message)
        return True

    # ── Messaging ───────────────────────────────────────────

    def xǁAgentRuntimeǁroute_message__mutmut_24(self, message: Any) -> bool:
        """Route a message to the target agent.

        Args:
            message: An AgentMessage with a recipient_id field.

        Returns:
            True if the message was delivered successfully.
        """
        recipient_id = getattr(message, "recipient_id", None)
        if recipient_id is None:
            logger.warning("Message has no recipient_id")
            return False

        agent = self._agents.get(recipient_id)
        if agent is None:
            logger.warning("RECIPIENT AGENT NOT FOUND: %S", recipient_id)
            return False

        agent.receive_message(message)
        return True

    # ── Messaging ───────────────────────────────────────────

    def xǁAgentRuntimeǁroute_message__mutmut_25(self, message: Any) -> bool:
        """Route a message to the target agent.

        Args:
            message: An AgentMessage with a recipient_id field.

        Returns:
            True if the message was delivered successfully.
        """
        recipient_id = getattr(message, "recipient_id", None)
        if recipient_id is None:
            logger.warning("Message has no recipient_id")
            return False

        agent = self._agents.get(recipient_id)
        if agent is None:
            logger.warning("Recipient agent not found: %s", recipient_id)
            return True

        agent.receive_message(message)
        return True

    # ── Messaging ───────────────────────────────────────────

    def xǁAgentRuntimeǁroute_message__mutmut_26(self, message: Any) -> bool:
        """Route a message to the target agent.

        Args:
            message: An AgentMessage with a recipient_id field.

        Returns:
            True if the message was delivered successfully.
        """
        recipient_id = getattr(message, "recipient_id", None)
        if recipient_id is None:
            logger.warning("Message has no recipient_id")
            return False

        agent = self._agents.get(recipient_id)
        if agent is None:
            logger.warning("Recipient agent not found: %s", recipient_id)
            return False

        agent.receive_message(None)
        return True

    # ── Messaging ───────────────────────────────────────────

    def xǁAgentRuntimeǁroute_message__mutmut_27(self, message: Any) -> bool:
        """Route a message to the target agent.

        Args:
            message: An AgentMessage with a recipient_id field.

        Returns:
            True if the message was delivered successfully.
        """
        recipient_id = getattr(message, "recipient_id", None)
        if recipient_id is None:
            logger.warning("Message has no recipient_id")
            return False

        agent = self._agents.get(recipient_id)
        if agent is None:
            logger.warning("Recipient agent not found: %s", recipient_id)
            return False

        agent.receive_message(message)
        return False

    @_mutmut_mutated(mutants_xǁAgentRuntimeǁbroadcast__mutmut)
    def broadcast(self, sender_id: str, content: Any, message_type: str = "broadcast") -> int:
        """Broadcast a message to all active agents except the sender.

        Returns:
            Number of agents that received the message.
        """
        delivered = 0
        for agent in self._agents.values():
            if agent.agent_id != sender_id and agent.is_active:
                msg = agent.send_message(agent.agent_id, content, message_type)
                agent.receive_message(msg)
                delivered += 1
        return delivered

    def xǁAgentRuntimeǁbroadcast__mutmut_orig(self, sender_id: str, content: Any, message_type: str = "broadcast") -> int:
        """Broadcast a message to all active agents except the sender.

        Returns:
            Number of agents that received the message.
        """
        delivered = 0
        for agent in self._agents.values():
            if agent.agent_id != sender_id and agent.is_active:
                msg = agent.send_message(agent.agent_id, content, message_type)
                agent.receive_message(msg)
                delivered += 1
        return delivered

    def xǁAgentRuntimeǁbroadcast__mutmut_1(self, sender_id: str, content: Any, message_type: str = "XXbroadcastXX") -> int:
        """Broadcast a message to all active agents except the sender.

        Returns:
            Number of agents that received the message.
        """
        delivered = 0
        for agent in self._agents.values():
            if agent.agent_id != sender_id and agent.is_active:
                msg = agent.send_message(agent.agent_id, content, message_type)
                agent.receive_message(msg)
                delivered += 1
        return delivered

    def xǁAgentRuntimeǁbroadcast__mutmut_2(self, sender_id: str, content: Any, message_type: str = "BROADCAST") -> int:
        """Broadcast a message to all active agents except the sender.

        Returns:
            Number of agents that received the message.
        """
        delivered = 0
        for agent in self._agents.values():
            if agent.agent_id != sender_id and agent.is_active:
                msg = agent.send_message(agent.agent_id, content, message_type)
                agent.receive_message(msg)
                delivered += 1
        return delivered

    def xǁAgentRuntimeǁbroadcast__mutmut_3(self, sender_id: str, content: Any, message_type: str = "broadcast") -> int:
        """Broadcast a message to all active agents except the sender.

        Returns:
            Number of agents that received the message.
        """
        delivered = None
        for agent in self._agents.values():
            if agent.agent_id != sender_id and agent.is_active:
                msg = agent.send_message(agent.agent_id, content, message_type)
                agent.receive_message(msg)
                delivered += 1
        return delivered

    def xǁAgentRuntimeǁbroadcast__mutmut_4(self, sender_id: str, content: Any, message_type: str = "broadcast") -> int:
        """Broadcast a message to all active agents except the sender.

        Returns:
            Number of agents that received the message.
        """
        delivered = 1
        for agent in self._agents.values():
            if agent.agent_id != sender_id and agent.is_active:
                msg = agent.send_message(agent.agent_id, content, message_type)
                agent.receive_message(msg)
                delivered += 1
        return delivered

    def xǁAgentRuntimeǁbroadcast__mutmut_5(self, sender_id: str, content: Any, message_type: str = "broadcast") -> int:
        """Broadcast a message to all active agents except the sender.

        Returns:
            Number of agents that received the message.
        """
        delivered = 0
        for agent in self._agents.values():
            if agent.agent_id != sender_id or agent.is_active:
                msg = agent.send_message(agent.agent_id, content, message_type)
                agent.receive_message(msg)
                delivered += 1
        return delivered

    def xǁAgentRuntimeǁbroadcast__mutmut_6(self, sender_id: str, content: Any, message_type: str = "broadcast") -> int:
        """Broadcast a message to all active agents except the sender.

        Returns:
            Number of agents that received the message.
        """
        delivered = 0
        for agent in self._agents.values():
            if agent.agent_id == sender_id and agent.is_active:
                msg = agent.send_message(agent.agent_id, content, message_type)
                agent.receive_message(msg)
                delivered += 1
        return delivered

    def xǁAgentRuntimeǁbroadcast__mutmut_7(self, sender_id: str, content: Any, message_type: str = "broadcast") -> int:
        """Broadcast a message to all active agents except the sender.

        Returns:
            Number of agents that received the message.
        """
        delivered = 0
        for agent in self._agents.values():
            if agent.agent_id != sender_id and agent.is_active:
                msg = None
                agent.receive_message(msg)
                delivered += 1
        return delivered

    def xǁAgentRuntimeǁbroadcast__mutmut_8(self, sender_id: str, content: Any, message_type: str = "broadcast") -> int:
        """Broadcast a message to all active agents except the sender.

        Returns:
            Number of agents that received the message.
        """
        delivered = 0
        for agent in self._agents.values():
            if agent.agent_id != sender_id and agent.is_active:
                msg = agent.send_message(None, content, message_type)
                agent.receive_message(msg)
                delivered += 1
        return delivered

    def xǁAgentRuntimeǁbroadcast__mutmut_9(self, sender_id: str, content: Any, message_type: str = "broadcast") -> int:
        """Broadcast a message to all active agents except the sender.

        Returns:
            Number of agents that received the message.
        """
        delivered = 0
        for agent in self._agents.values():
            if agent.agent_id != sender_id and agent.is_active:
                msg = agent.send_message(agent.agent_id, None, message_type)
                agent.receive_message(msg)
                delivered += 1
        return delivered

    def xǁAgentRuntimeǁbroadcast__mutmut_10(self, sender_id: str, content: Any, message_type: str = "broadcast") -> int:
        """Broadcast a message to all active agents except the sender.

        Returns:
            Number of agents that received the message.
        """
        delivered = 0
        for agent in self._agents.values():
            if agent.agent_id != sender_id and agent.is_active:
                msg = agent.send_message(agent.agent_id, content, None)
                agent.receive_message(msg)
                delivered += 1
        return delivered

    def xǁAgentRuntimeǁbroadcast__mutmut_11(self, sender_id: str, content: Any, message_type: str = "broadcast") -> int:
        """Broadcast a message to all active agents except the sender.

        Returns:
            Number of agents that received the message.
        """
        delivered = 0
        for agent in self._agents.values():
            if agent.agent_id != sender_id and agent.is_active:
                msg = agent.send_message(content, message_type)
                agent.receive_message(msg)
                delivered += 1
        return delivered

    def xǁAgentRuntimeǁbroadcast__mutmut_12(self, sender_id: str, content: Any, message_type: str = "broadcast") -> int:
        """Broadcast a message to all active agents except the sender.

        Returns:
            Number of agents that received the message.
        """
        delivered = 0
        for agent in self._agents.values():
            if agent.agent_id != sender_id and agent.is_active:
                msg = agent.send_message(agent.agent_id, message_type)
                agent.receive_message(msg)
                delivered += 1
        return delivered

    def xǁAgentRuntimeǁbroadcast__mutmut_13(self, sender_id: str, content: Any, message_type: str = "broadcast") -> int:
        """Broadcast a message to all active agents except the sender.

        Returns:
            Number of agents that received the message.
        """
        delivered = 0
        for agent in self._agents.values():
            if agent.agent_id != sender_id and agent.is_active:
                msg = agent.send_message(agent.agent_id, content, )
                agent.receive_message(msg)
                delivered += 1
        return delivered

    def xǁAgentRuntimeǁbroadcast__mutmut_14(self, sender_id: str, content: Any, message_type: str = "broadcast") -> int:
        """Broadcast a message to all active agents except the sender.

        Returns:
            Number of agents that received the message.
        """
        delivered = 0
        for agent in self._agents.values():
            if agent.agent_id != sender_id and agent.is_active:
                msg = agent.send_message(agent.agent_id, content, message_type)
                agent.receive_message(None)
                delivered += 1
        return delivered

    def xǁAgentRuntimeǁbroadcast__mutmut_15(self, sender_id: str, content: Any, message_type: str = "broadcast") -> int:
        """Broadcast a message to all active agents except the sender.

        Returns:
            Number of agents that received the message.
        """
        delivered = 0
        for agent in self._agents.values():
            if agent.agent_id != sender_id and agent.is_active:
                msg = agent.send_message(agent.agent_id, content, message_type)
                agent.receive_message(msg)
                delivered = 1
        return delivered

    def xǁAgentRuntimeǁbroadcast__mutmut_16(self, sender_id: str, content: Any, message_type: str = "broadcast") -> int:
        """Broadcast a message to all active agents except the sender.

        Returns:
            Number of agents that received the message.
        """
        delivered = 0
        for agent in self._agents.values():
            if agent.agent_id != sender_id and agent.is_active:
                msg = agent.send_message(agent.agent_id, content, message_type)
                agent.receive_message(msg)
                delivered -= 1
        return delivered

    def xǁAgentRuntimeǁbroadcast__mutmut_17(self, sender_id: str, content: Any, message_type: str = "broadcast") -> int:
        """Broadcast a message to all active agents except the sender.

        Returns:
            Number of agents that received the message.
        """
        delivered = 0
        for agent in self._agents.values():
            if agent.agent_id != sender_id and agent.is_active:
                msg = agent.send_message(agent.agent_id, content, message_type)
                agent.receive_message(msg)
                delivered += 2
        return delivered

    # ── Health Monitoring ───────────────────────────────────

    @_mutmut_mutated(mutants_xǁAgentRuntimeǁstart_heartbeat__mutmut)
    def start_heartbeat(self) -> None:
        """Start the background heartbeat monitor."""
        if self._running:
            return
        self._running = True
        self._heartbeat_thread = threading.Thread(
            target=self._heartbeat_loop, daemon=True, name="agent-heartbeat"
        )
        self._heartbeat_thread.start()

    # ── Health Monitoring ───────────────────────────────────

    def xǁAgentRuntimeǁstart_heartbeat__mutmut_orig(self) -> None:
        """Start the background heartbeat monitor."""
        if self._running:
            return
        self._running = True
        self._heartbeat_thread = threading.Thread(
            target=self._heartbeat_loop, daemon=True, name="agent-heartbeat"
        )
        self._heartbeat_thread.start()

    # ── Health Monitoring ───────────────────────────────────

    def xǁAgentRuntimeǁstart_heartbeat__mutmut_1(self) -> None:
        """Start the background heartbeat monitor."""
        if self._running:
            return
        self._running = None
        self._heartbeat_thread = threading.Thread(
            target=self._heartbeat_loop, daemon=True, name="agent-heartbeat"
        )
        self._heartbeat_thread.start()

    # ── Health Monitoring ───────────────────────────────────

    def xǁAgentRuntimeǁstart_heartbeat__mutmut_2(self) -> None:
        """Start the background heartbeat monitor."""
        if self._running:
            return
        self._running = False
        self._heartbeat_thread = threading.Thread(
            target=self._heartbeat_loop, daemon=True, name="agent-heartbeat"
        )
        self._heartbeat_thread.start()

    # ── Health Monitoring ───────────────────────────────────

    def xǁAgentRuntimeǁstart_heartbeat__mutmut_3(self) -> None:
        """Start the background heartbeat monitor."""
        if self._running:
            return
        self._running = True
        self._heartbeat_thread = None
        self._heartbeat_thread.start()

    # ── Health Monitoring ───────────────────────────────────

    def xǁAgentRuntimeǁstart_heartbeat__mutmut_4(self) -> None:
        """Start the background heartbeat monitor."""
        if self._running:
            return
        self._running = True
        self._heartbeat_thread = threading.Thread(
            target=None, daemon=True, name="agent-heartbeat"
        )
        self._heartbeat_thread.start()

    # ── Health Monitoring ───────────────────────────────────

    def xǁAgentRuntimeǁstart_heartbeat__mutmut_5(self) -> None:
        """Start the background heartbeat monitor."""
        if self._running:
            return
        self._running = True
        self._heartbeat_thread = threading.Thread(
            target=self._heartbeat_loop, daemon=None, name="agent-heartbeat"
        )
        self._heartbeat_thread.start()

    # ── Health Monitoring ───────────────────────────────────

    def xǁAgentRuntimeǁstart_heartbeat__mutmut_6(self) -> None:
        """Start the background heartbeat monitor."""
        if self._running:
            return
        self._running = True
        self._heartbeat_thread = threading.Thread(
            target=self._heartbeat_loop, daemon=True, name=None
        )
        self._heartbeat_thread.start()

    # ── Health Monitoring ───────────────────────────────────

    def xǁAgentRuntimeǁstart_heartbeat__mutmut_7(self) -> None:
        """Start the background heartbeat monitor."""
        if self._running:
            return
        self._running = True
        self._heartbeat_thread = threading.Thread(
            daemon=True, name="agent-heartbeat"
        )
        self._heartbeat_thread.start()

    # ── Health Monitoring ───────────────────────────────────

    def xǁAgentRuntimeǁstart_heartbeat__mutmut_8(self) -> None:
        """Start the background heartbeat monitor."""
        if self._running:
            return
        self._running = True
        self._heartbeat_thread = threading.Thread(
            target=self._heartbeat_loop, name="agent-heartbeat"
        )
        self._heartbeat_thread.start()

    # ── Health Monitoring ───────────────────────────────────

    def xǁAgentRuntimeǁstart_heartbeat__mutmut_9(self) -> None:
        """Start the background heartbeat monitor."""
        if self._running:
            return
        self._running = True
        self._heartbeat_thread = threading.Thread(
            target=self._heartbeat_loop, daemon=True, )
        self._heartbeat_thread.start()

    # ── Health Monitoring ───────────────────────────────────

    def xǁAgentRuntimeǁstart_heartbeat__mutmut_10(self) -> None:
        """Start the background heartbeat monitor."""
        if self._running:
            return
        self._running = True
        self._heartbeat_thread = threading.Thread(
            target=self._heartbeat_loop, daemon=False, name="agent-heartbeat"
        )
        self._heartbeat_thread.start()

    # ── Health Monitoring ───────────────────────────────────

    def xǁAgentRuntimeǁstart_heartbeat__mutmut_11(self) -> None:
        """Start the background heartbeat monitor."""
        if self._running:
            return
        self._running = True
        self._heartbeat_thread = threading.Thread(
            target=self._heartbeat_loop, daemon=True, name="XXagent-heartbeatXX"
        )
        self._heartbeat_thread.start()

    # ── Health Monitoring ───────────────────────────────────

    def xǁAgentRuntimeǁstart_heartbeat__mutmut_12(self) -> None:
        """Start the background heartbeat monitor."""
        if self._running:
            return
        self._running = True
        self._heartbeat_thread = threading.Thread(
            target=self._heartbeat_loop, daemon=True, name="AGENT-HEARTBEAT"
        )
        self._heartbeat_thread.start()

    @_mutmut_mutated(mutants_xǁAgentRuntimeǁstop_heartbeat__mutmut)
    def stop_heartbeat(self) -> None:
        """Stop the heartbeat monitor."""
        self._running = False
        if self._heartbeat_thread:
            self._heartbeat_thread.join(timeout=5)
            self._heartbeat_thread = None

    def xǁAgentRuntimeǁstop_heartbeat__mutmut_orig(self) -> None:
        """Stop the heartbeat monitor."""
        self._running = False
        if self._heartbeat_thread:
            self._heartbeat_thread.join(timeout=5)
            self._heartbeat_thread = None

    def xǁAgentRuntimeǁstop_heartbeat__mutmut_1(self) -> None:
        """Stop the heartbeat monitor."""
        self._running = None
        if self._heartbeat_thread:
            self._heartbeat_thread.join(timeout=5)
            self._heartbeat_thread = None

    def xǁAgentRuntimeǁstop_heartbeat__mutmut_2(self) -> None:
        """Stop the heartbeat monitor."""
        self._running = True
        if self._heartbeat_thread:
            self._heartbeat_thread.join(timeout=5)
            self._heartbeat_thread = None

    def xǁAgentRuntimeǁstop_heartbeat__mutmut_3(self) -> None:
        """Stop the heartbeat monitor."""
        self._running = False
        if self._heartbeat_thread:
            self._heartbeat_thread.join(timeout=None)
            self._heartbeat_thread = None

    def xǁAgentRuntimeǁstop_heartbeat__mutmut_4(self) -> None:
        """Stop the heartbeat monitor."""
        self._running = False
        if self._heartbeat_thread:
            self._heartbeat_thread.join(timeout=6)
            self._heartbeat_thread = None

    def xǁAgentRuntimeǁstop_heartbeat__mutmut_5(self) -> None:
        """Stop the heartbeat monitor."""
        self._running = False
        if self._heartbeat_thread:
            self._heartbeat_thread.join(timeout=5)
            self._heartbeat_thread = ""

    @_mutmut_mutated(mutants_xǁAgentRuntimeǁ_heartbeat_loop__mutmut)
    def _heartbeat_loop(self) -> None:
        """Background loop checking agent health."""
        while self._running:
            try:
                self._check_agents_health()
            except Exception as exc:
                logger.error("Heartbeat error: %s", exc)
            time.sleep(self._heartbeat_interval)

    def xǁAgentRuntimeǁ_heartbeat_loop__mutmut_orig(self) -> None:
        """Background loop checking agent health."""
        while self._running:
            try:
                self._check_agents_health()
            except Exception as exc:
                logger.error("Heartbeat error: %s", exc)
            time.sleep(self._heartbeat_interval)

    def xǁAgentRuntimeǁ_heartbeat_loop__mutmut_1(self) -> None:
        """Background loop checking agent health."""
        while self._running:
            try:
                self._check_agents_health()
            except Exception as exc:
                logger.error(None, exc)
            time.sleep(self._heartbeat_interval)

    def xǁAgentRuntimeǁ_heartbeat_loop__mutmut_2(self) -> None:
        """Background loop checking agent health."""
        while self._running:
            try:
                self._check_agents_health()
            except Exception as exc:
                logger.error("Heartbeat error: %s", None)
            time.sleep(self._heartbeat_interval)

    def xǁAgentRuntimeǁ_heartbeat_loop__mutmut_3(self) -> None:
        """Background loop checking agent health."""
        while self._running:
            try:
                self._check_agents_health()
            except Exception as exc:
                logger.error(exc)
            time.sleep(self._heartbeat_interval)

    def xǁAgentRuntimeǁ_heartbeat_loop__mutmut_4(self) -> None:
        """Background loop checking agent health."""
        while self._running:
            try:
                self._check_agents_health()
            except Exception as exc:
                logger.error("Heartbeat error: %s", )
            time.sleep(self._heartbeat_interval)

    def xǁAgentRuntimeǁ_heartbeat_loop__mutmut_5(self) -> None:
        """Background loop checking agent health."""
        while self._running:
            try:
                self._check_agents_health()
            except Exception as exc:
                logger.error("XXHeartbeat error: %sXX", exc)
            time.sleep(self._heartbeat_interval)

    def xǁAgentRuntimeǁ_heartbeat_loop__mutmut_6(self) -> None:
        """Background loop checking agent health."""
        while self._running:
            try:
                self._check_agents_health()
            except Exception as exc:
                logger.error("heartbeat error: %s", exc)
            time.sleep(self._heartbeat_interval)

    def xǁAgentRuntimeǁ_heartbeat_loop__mutmut_7(self) -> None:
        """Background loop checking agent health."""
        while self._running:
            try:
                self._check_agents_health()
            except Exception as exc:
                logger.error("HEARTBEAT ERROR: %S", exc)
            time.sleep(self._heartbeat_interval)

    def xǁAgentRuntimeǁ_heartbeat_loop__mutmut_8(self) -> None:
        """Background loop checking agent health."""
        while self._running:
            try:
                self._check_agents_health()
            except Exception as exc:
                logger.error("Heartbeat error: %s", exc)
            time.sleep(None)

    @_mutmut_mutated(mutants_xǁAgentRuntimeǁ_check_agents_health__mutmut)
    def _check_agents_health(self) -> None:
        """Check health of all registered agents."""
        now = time.time()
        stale_threshold = 300.0  # 5 minutes

        for agent_id, agent in list(self._agents.items()):
            if agent.state == AgentState.ERROR:
                self._stats.total_errors += 1
                logger.warning("Agent %s in ERROR state", agent_id)

            # Check for stale agents (no activity for threshold)
            if now - agent._last_active > stale_threshold and agent.state not in {
                AgentState.PAUSED,
                AgentState.TERMINATED,
            }:
                logger.warning("Agent %s appears stale (last active %.0fs ago)", agent_id, now - agent._last_active)

    def xǁAgentRuntimeǁ_check_agents_health__mutmut_orig(self) -> None:
        """Check health of all registered agents."""
        now = time.time()
        stale_threshold = 300.0  # 5 minutes

        for agent_id, agent in list(self._agents.items()):
            if agent.state == AgentState.ERROR:
                self._stats.total_errors += 1
                logger.warning("Agent %s in ERROR state", agent_id)

            # Check for stale agents (no activity for threshold)
            if now - agent._last_active > stale_threshold and agent.state not in {
                AgentState.PAUSED,
                AgentState.TERMINATED,
            }:
                logger.warning("Agent %s appears stale (last active %.0fs ago)", agent_id, now - agent._last_active)

    def xǁAgentRuntimeǁ_check_agents_health__mutmut_1(self) -> None:
        """Check health of all registered agents."""
        now = None
        stale_threshold = 300.0  # 5 minutes

        for agent_id, agent in list(self._agents.items()):
            if agent.state == AgentState.ERROR:
                self._stats.total_errors += 1
                logger.warning("Agent %s in ERROR state", agent_id)

            # Check for stale agents (no activity for threshold)
            if now - agent._last_active > stale_threshold and agent.state not in {
                AgentState.PAUSED,
                AgentState.TERMINATED,
            }:
                logger.warning("Agent %s appears stale (last active %.0fs ago)", agent_id, now - agent._last_active)

    def xǁAgentRuntimeǁ_check_agents_health__mutmut_2(self) -> None:
        """Check health of all registered agents."""
        now = time.time()
        stale_threshold = None  # 5 minutes

        for agent_id, agent in list(self._agents.items()):
            if agent.state == AgentState.ERROR:
                self._stats.total_errors += 1
                logger.warning("Agent %s in ERROR state", agent_id)

            # Check for stale agents (no activity for threshold)
            if now - agent._last_active > stale_threshold and agent.state not in {
                AgentState.PAUSED,
                AgentState.TERMINATED,
            }:
                logger.warning("Agent %s appears stale (last active %.0fs ago)", agent_id, now - agent._last_active)

    def xǁAgentRuntimeǁ_check_agents_health__mutmut_3(self) -> None:
        """Check health of all registered agents."""
        now = time.time()
        stale_threshold = 301.0  # 5 minutes

        for agent_id, agent in list(self._agents.items()):
            if agent.state == AgentState.ERROR:
                self._stats.total_errors += 1
                logger.warning("Agent %s in ERROR state", agent_id)

            # Check for stale agents (no activity for threshold)
            if now - agent._last_active > stale_threshold and agent.state not in {
                AgentState.PAUSED,
                AgentState.TERMINATED,
            }:
                logger.warning("Agent %s appears stale (last active %.0fs ago)", agent_id, now - agent._last_active)

    def xǁAgentRuntimeǁ_check_agents_health__mutmut_4(self) -> None:
        """Check health of all registered agents."""
        now = time.time()
        stale_threshold = 300.0  # 5 minutes

        for agent_id, agent in list(None):
            if agent.state == AgentState.ERROR:
                self._stats.total_errors += 1
                logger.warning("Agent %s in ERROR state", agent_id)

            # Check for stale agents (no activity for threshold)
            if now - agent._last_active > stale_threshold and agent.state not in {
                AgentState.PAUSED,
                AgentState.TERMINATED,
            }:
                logger.warning("Agent %s appears stale (last active %.0fs ago)", agent_id, now - agent._last_active)

    def xǁAgentRuntimeǁ_check_agents_health__mutmut_5(self) -> None:
        """Check health of all registered agents."""
        now = time.time()
        stale_threshold = 300.0  # 5 minutes

        for agent_id, agent in list(self._agents.items()):
            if agent.state != AgentState.ERROR:
                self._stats.total_errors += 1
                logger.warning("Agent %s in ERROR state", agent_id)

            # Check for stale agents (no activity for threshold)
            if now - agent._last_active > stale_threshold and agent.state not in {
                AgentState.PAUSED,
                AgentState.TERMINATED,
            }:
                logger.warning("Agent %s appears stale (last active %.0fs ago)", agent_id, now - agent._last_active)

    def xǁAgentRuntimeǁ_check_agents_health__mutmut_6(self) -> None:
        """Check health of all registered agents."""
        now = time.time()
        stale_threshold = 300.0  # 5 minutes

        for agent_id, agent in list(self._agents.items()):
            if agent.state == AgentState.ERROR:
                self._stats.total_errors = 1
                logger.warning("Agent %s in ERROR state", agent_id)

            # Check for stale agents (no activity for threshold)
            if now - agent._last_active > stale_threshold and agent.state not in {
                AgentState.PAUSED,
                AgentState.TERMINATED,
            }:
                logger.warning("Agent %s appears stale (last active %.0fs ago)", agent_id, now - agent._last_active)

    def xǁAgentRuntimeǁ_check_agents_health__mutmut_7(self) -> None:
        """Check health of all registered agents."""
        now = time.time()
        stale_threshold = 300.0  # 5 minutes

        for agent_id, agent in list(self._agents.items()):
            if agent.state == AgentState.ERROR:
                self._stats.total_errors -= 1
                logger.warning("Agent %s in ERROR state", agent_id)

            # Check for stale agents (no activity for threshold)
            if now - agent._last_active > stale_threshold and agent.state not in {
                AgentState.PAUSED,
                AgentState.TERMINATED,
            }:
                logger.warning("Agent %s appears stale (last active %.0fs ago)", agent_id, now - agent._last_active)

    def xǁAgentRuntimeǁ_check_agents_health__mutmut_8(self) -> None:
        """Check health of all registered agents."""
        now = time.time()
        stale_threshold = 300.0  # 5 minutes

        for agent_id, agent in list(self._agents.items()):
            if agent.state == AgentState.ERROR:
                self._stats.total_errors += 2
                logger.warning("Agent %s in ERROR state", agent_id)

            # Check for stale agents (no activity for threshold)
            if now - agent._last_active > stale_threshold and agent.state not in {
                AgentState.PAUSED,
                AgentState.TERMINATED,
            }:
                logger.warning("Agent %s appears stale (last active %.0fs ago)", agent_id, now - agent._last_active)

    def xǁAgentRuntimeǁ_check_agents_health__mutmut_9(self) -> None:
        """Check health of all registered agents."""
        now = time.time()
        stale_threshold = 300.0  # 5 minutes

        for agent_id, agent in list(self._agents.items()):
            if agent.state == AgentState.ERROR:
                self._stats.total_errors += 1
                logger.warning(None, agent_id)

            # Check for stale agents (no activity for threshold)
            if now - agent._last_active > stale_threshold and agent.state not in {
                AgentState.PAUSED,
                AgentState.TERMINATED,
            }:
                logger.warning("Agent %s appears stale (last active %.0fs ago)", agent_id, now - agent._last_active)

    def xǁAgentRuntimeǁ_check_agents_health__mutmut_10(self) -> None:
        """Check health of all registered agents."""
        now = time.time()
        stale_threshold = 300.0  # 5 minutes

        for agent_id, agent in list(self._agents.items()):
            if agent.state == AgentState.ERROR:
                self._stats.total_errors += 1
                logger.warning("Agent %s in ERROR state", None)

            # Check for stale agents (no activity for threshold)
            if now - agent._last_active > stale_threshold and agent.state not in {
                AgentState.PAUSED,
                AgentState.TERMINATED,
            }:
                logger.warning("Agent %s appears stale (last active %.0fs ago)", agent_id, now - agent._last_active)

    def xǁAgentRuntimeǁ_check_agents_health__mutmut_11(self) -> None:
        """Check health of all registered agents."""
        now = time.time()
        stale_threshold = 300.0  # 5 minutes

        for agent_id, agent in list(self._agents.items()):
            if agent.state == AgentState.ERROR:
                self._stats.total_errors += 1
                logger.warning(agent_id)

            # Check for stale agents (no activity for threshold)
            if now - agent._last_active > stale_threshold and agent.state not in {
                AgentState.PAUSED,
                AgentState.TERMINATED,
            }:
                logger.warning("Agent %s appears stale (last active %.0fs ago)", agent_id, now - agent._last_active)

    def xǁAgentRuntimeǁ_check_agents_health__mutmut_12(self) -> None:
        """Check health of all registered agents."""
        now = time.time()
        stale_threshold = 300.0  # 5 minutes

        for agent_id, agent in list(self._agents.items()):
            if agent.state == AgentState.ERROR:
                self._stats.total_errors += 1
                logger.warning("Agent %s in ERROR state", )

            # Check for stale agents (no activity for threshold)
            if now - agent._last_active > stale_threshold and agent.state not in {
                AgentState.PAUSED,
                AgentState.TERMINATED,
            }:
                logger.warning("Agent %s appears stale (last active %.0fs ago)", agent_id, now - agent._last_active)

    def xǁAgentRuntimeǁ_check_agents_health__mutmut_13(self) -> None:
        """Check health of all registered agents."""
        now = time.time()
        stale_threshold = 300.0  # 5 minutes

        for agent_id, agent in list(self._agents.items()):
            if agent.state == AgentState.ERROR:
                self._stats.total_errors += 1
                logger.warning("XXAgent %s in ERROR stateXX", agent_id)

            # Check for stale agents (no activity for threshold)
            if now - agent._last_active > stale_threshold and agent.state not in {
                AgentState.PAUSED,
                AgentState.TERMINATED,
            }:
                logger.warning("Agent %s appears stale (last active %.0fs ago)", agent_id, now - agent._last_active)

    def xǁAgentRuntimeǁ_check_agents_health__mutmut_14(self) -> None:
        """Check health of all registered agents."""
        now = time.time()
        stale_threshold = 300.0  # 5 minutes

        for agent_id, agent in list(self._agents.items()):
            if agent.state == AgentState.ERROR:
                self._stats.total_errors += 1
                logger.warning("agent %s in error state", agent_id)

            # Check for stale agents (no activity for threshold)
            if now - agent._last_active > stale_threshold and agent.state not in {
                AgentState.PAUSED,
                AgentState.TERMINATED,
            }:
                logger.warning("Agent %s appears stale (last active %.0fs ago)", agent_id, now - agent._last_active)

    def xǁAgentRuntimeǁ_check_agents_health__mutmut_15(self) -> None:
        """Check health of all registered agents."""
        now = time.time()
        stale_threshold = 300.0  # 5 minutes

        for agent_id, agent in list(self._agents.items()):
            if agent.state == AgentState.ERROR:
                self._stats.total_errors += 1
                logger.warning("AGENT %S IN ERROR STATE", agent_id)

            # Check for stale agents (no activity for threshold)
            if now - agent._last_active > stale_threshold and agent.state not in {
                AgentState.PAUSED,
                AgentState.TERMINATED,
            }:
                logger.warning("Agent %s appears stale (last active %.0fs ago)", agent_id, now - agent._last_active)

    def xǁAgentRuntimeǁ_check_agents_health__mutmut_16(self) -> None:
        """Check health of all registered agents."""
        now = time.time()
        stale_threshold = 300.0  # 5 minutes

        for agent_id, agent in list(self._agents.items()):
            if agent.state == AgentState.ERROR:
                self._stats.total_errors += 1
                logger.warning("Agent %s in ERROR state", agent_id)

            # Check for stale agents (no activity for threshold)
            if now - agent._last_active > stale_threshold or agent.state not in {
                AgentState.PAUSED,
                AgentState.TERMINATED,
            }:
                logger.warning("Agent %s appears stale (last active %.0fs ago)", agent_id, now - agent._last_active)

    def xǁAgentRuntimeǁ_check_agents_health__mutmut_17(self) -> None:
        """Check health of all registered agents."""
        now = time.time()
        stale_threshold = 300.0  # 5 minutes

        for agent_id, agent in list(self._agents.items()):
            if agent.state == AgentState.ERROR:
                self._stats.total_errors += 1
                logger.warning("Agent %s in ERROR state", agent_id)

            # Check for stale agents (no activity for threshold)
            if now + agent._last_active > stale_threshold and agent.state not in {
                AgentState.PAUSED,
                AgentState.TERMINATED,
            }:
                logger.warning("Agent %s appears stale (last active %.0fs ago)", agent_id, now - agent._last_active)

    def xǁAgentRuntimeǁ_check_agents_health__mutmut_18(self) -> None:
        """Check health of all registered agents."""
        now = time.time()
        stale_threshold = 300.0  # 5 minutes

        for agent_id, agent in list(self._agents.items()):
            if agent.state == AgentState.ERROR:
                self._stats.total_errors += 1
                logger.warning("Agent %s in ERROR state", agent_id)

            # Check for stale agents (no activity for threshold)
            if now - agent._last_active >= stale_threshold and agent.state not in {
                AgentState.PAUSED,
                AgentState.TERMINATED,
            }:
                logger.warning("Agent %s appears stale (last active %.0fs ago)", agent_id, now - agent._last_active)

    def xǁAgentRuntimeǁ_check_agents_health__mutmut_19(self) -> None:
        """Check health of all registered agents."""
        now = time.time()
        stale_threshold = 300.0  # 5 minutes

        for agent_id, agent in list(self._agents.items()):
            if agent.state == AgentState.ERROR:
                self._stats.total_errors += 1
                logger.warning("Agent %s in ERROR state", agent_id)

            # Check for stale agents (no activity for threshold)
            if now - agent._last_active > stale_threshold and agent.state in {
                AgentState.PAUSED,
                AgentState.TERMINATED,
            }:
                logger.warning("Agent %s appears stale (last active %.0fs ago)", agent_id, now - agent._last_active)

    def xǁAgentRuntimeǁ_check_agents_health__mutmut_20(self) -> None:
        """Check health of all registered agents."""
        now = time.time()
        stale_threshold = 300.0  # 5 minutes

        for agent_id, agent in list(self._agents.items()):
            if agent.state == AgentState.ERROR:
                self._stats.total_errors += 1
                logger.warning("Agent %s in ERROR state", agent_id)

            # Check for stale agents (no activity for threshold)
            if now - agent._last_active > stale_threshold and agent.state not in {
                AgentState.PAUSED,
                AgentState.TERMINATED,
            }:
                logger.warning(None, agent_id, now - agent._last_active)

    def xǁAgentRuntimeǁ_check_agents_health__mutmut_21(self) -> None:
        """Check health of all registered agents."""
        now = time.time()
        stale_threshold = 300.0  # 5 minutes

        for agent_id, agent in list(self._agents.items()):
            if agent.state == AgentState.ERROR:
                self._stats.total_errors += 1
                logger.warning("Agent %s in ERROR state", agent_id)

            # Check for stale agents (no activity for threshold)
            if now - agent._last_active > stale_threshold and agent.state not in {
                AgentState.PAUSED,
                AgentState.TERMINATED,
            }:
                logger.warning("Agent %s appears stale (last active %.0fs ago)", None, now - agent._last_active)

    def xǁAgentRuntimeǁ_check_agents_health__mutmut_22(self) -> None:
        """Check health of all registered agents."""
        now = time.time()
        stale_threshold = 300.0  # 5 minutes

        for agent_id, agent in list(self._agents.items()):
            if agent.state == AgentState.ERROR:
                self._stats.total_errors += 1
                logger.warning("Agent %s in ERROR state", agent_id)

            # Check for stale agents (no activity for threshold)
            if now - agent._last_active > stale_threshold and agent.state not in {
                AgentState.PAUSED,
                AgentState.TERMINATED,
            }:
                logger.warning("Agent %s appears stale (last active %.0fs ago)", agent_id, None)

    def xǁAgentRuntimeǁ_check_agents_health__mutmut_23(self) -> None:
        """Check health of all registered agents."""
        now = time.time()
        stale_threshold = 300.0  # 5 minutes

        for agent_id, agent in list(self._agents.items()):
            if agent.state == AgentState.ERROR:
                self._stats.total_errors += 1
                logger.warning("Agent %s in ERROR state", agent_id)

            # Check for stale agents (no activity for threshold)
            if now - agent._last_active > stale_threshold and agent.state not in {
                AgentState.PAUSED,
                AgentState.TERMINATED,
            }:
                logger.warning(agent_id, now - agent._last_active)

    def xǁAgentRuntimeǁ_check_agents_health__mutmut_24(self) -> None:
        """Check health of all registered agents."""
        now = time.time()
        stale_threshold = 300.0  # 5 minutes

        for agent_id, agent in list(self._agents.items()):
            if agent.state == AgentState.ERROR:
                self._stats.total_errors += 1
                logger.warning("Agent %s in ERROR state", agent_id)

            # Check for stale agents (no activity for threshold)
            if now - agent._last_active > stale_threshold and agent.state not in {
                AgentState.PAUSED,
                AgentState.TERMINATED,
            }:
                logger.warning("Agent %s appears stale (last active %.0fs ago)", now - agent._last_active)

    def xǁAgentRuntimeǁ_check_agents_health__mutmut_25(self) -> None:
        """Check health of all registered agents."""
        now = time.time()
        stale_threshold = 300.0  # 5 minutes

        for agent_id, agent in list(self._agents.items()):
            if agent.state == AgentState.ERROR:
                self._stats.total_errors += 1
                logger.warning("Agent %s in ERROR state", agent_id)

            # Check for stale agents (no activity for threshold)
            if now - agent._last_active > stale_threshold and agent.state not in {
                AgentState.PAUSED,
                AgentState.TERMINATED,
            }:
                logger.warning("Agent %s appears stale (last active %.0fs ago)", agent_id, )

    def xǁAgentRuntimeǁ_check_agents_health__mutmut_26(self) -> None:
        """Check health of all registered agents."""
        now = time.time()
        stale_threshold = 300.0  # 5 minutes

        for agent_id, agent in list(self._agents.items()):
            if agent.state == AgentState.ERROR:
                self._stats.total_errors += 1
                logger.warning("Agent %s in ERROR state", agent_id)

            # Check for stale agents (no activity for threshold)
            if now - agent._last_active > stale_threshold and agent.state not in {
                AgentState.PAUSED,
                AgentState.TERMINATED,
            }:
                logger.warning("XXAgent %s appears stale (last active %.0fs ago)XX", agent_id, now - agent._last_active)

    def xǁAgentRuntimeǁ_check_agents_health__mutmut_27(self) -> None:
        """Check health of all registered agents."""
        now = time.time()
        stale_threshold = 300.0  # 5 minutes

        for agent_id, agent in list(self._agents.items()):
            if agent.state == AgentState.ERROR:
                self._stats.total_errors += 1
                logger.warning("Agent %s in ERROR state", agent_id)

            # Check for stale agents (no activity for threshold)
            if now - agent._last_active > stale_threshold and agent.state not in {
                AgentState.PAUSED,
                AgentState.TERMINATED,
            }:
                logger.warning("agent %s appears stale (last active %.0fs ago)", agent_id, now - agent._last_active)

    def xǁAgentRuntimeǁ_check_agents_health__mutmut_28(self) -> None:
        """Check health of all registered agents."""
        now = time.time()
        stale_threshold = 300.0  # 5 minutes

        for agent_id, agent in list(self._agents.items()):
            if agent.state == AgentState.ERROR:
                self._stats.total_errors += 1
                logger.warning("Agent %s in ERROR state", agent_id)

            # Check for stale agents (no activity for threshold)
            if now - agent._last_active > stale_threshold and agent.state not in {
                AgentState.PAUSED,
                AgentState.TERMINATED,
            }:
                logger.warning("AGENT %S APPEARS STALE (LAST ACTIVE %.0FS AGO)", agent_id, now - agent._last_active)

    def xǁAgentRuntimeǁ_check_agents_health__mutmut_29(self) -> None:
        """Check health of all registered agents."""
        now = time.time()
        stale_threshold = 300.0  # 5 minutes

        for agent_id, agent in list(self._agents.items()):
            if agent.state == AgentState.ERROR:
                self._stats.total_errors += 1
                logger.warning("Agent %s in ERROR state", agent_id)

            # Check for stale agents (no activity for threshold)
            if now - agent._last_active > stale_threshold and agent.state not in {
                AgentState.PAUSED,
                AgentState.TERMINATED,
            }:
                logger.warning("Agent %s appears stale (last active %.0fs ago)", agent_id, now + agent._last_active)

    # ── Hooks ───────────────────────────────────────────────

    @_mutmut_mutated(mutants_xǁAgentRuntimeǁregister_hook__mutmut)
    def register_hook(self, event: str, callback: Any) -> None:
        """Register a lifecycle hook callback.

        Events: on_spawn, on_terminate, on_pause, on_resume, on_error
        """
        self._hooks[event].append(callback)

    # ── Hooks ───────────────────────────────────────────────

    def xǁAgentRuntimeǁregister_hook__mutmut_orig(self, event: str, callback: Any) -> None:
        """Register a lifecycle hook callback.

        Events: on_spawn, on_terminate, on_pause, on_resume, on_error
        """
        self._hooks[event].append(callback)

    # ── Hooks ───────────────────────────────────────────────

    def xǁAgentRuntimeǁregister_hook__mutmut_1(self, event: str, callback: Any) -> None:
        """Register a lifecycle hook callback.

        Events: on_spawn, on_terminate, on_pause, on_resume, on_error
        """
        self._hooks[event].append(None)

    @_mutmut_mutated(mutants_xǁAgentRuntimeǁ_fire_hook__mutmut)
    def _fire_hook(self, event: str, agent: BaseAgent) -> None:
        """Fire all registered callbacks for an event."""
        for callback in self._hooks.get(event, []):
            try:
                callback(agent)
            except Exception as exc:
                logger.error("Hook %s error: %s", event, exc)

    def xǁAgentRuntimeǁ_fire_hook__mutmut_orig(self, event: str, agent: BaseAgent) -> None:
        """Fire all registered callbacks for an event."""
        for callback in self._hooks.get(event, []):
            try:
                callback(agent)
            except Exception as exc:
                logger.error("Hook %s error: %s", event, exc)

    def xǁAgentRuntimeǁ_fire_hook__mutmut_1(self, event: str, agent: BaseAgent) -> None:
        """Fire all registered callbacks for an event."""
        for callback in self._hooks.get(None, []):
            try:
                callback(agent)
            except Exception as exc:
                logger.error("Hook %s error: %s", event, exc)

    def xǁAgentRuntimeǁ_fire_hook__mutmut_2(self, event: str, agent: BaseAgent) -> None:
        """Fire all registered callbacks for an event."""
        for callback in self._hooks.get(event, None):
            try:
                callback(agent)
            except Exception as exc:
                logger.error("Hook %s error: %s", event, exc)

    def xǁAgentRuntimeǁ_fire_hook__mutmut_3(self, event: str, agent: BaseAgent) -> None:
        """Fire all registered callbacks for an event."""
        for callback in self._hooks.get([]):
            try:
                callback(agent)
            except Exception as exc:
                logger.error("Hook %s error: %s", event, exc)

    def xǁAgentRuntimeǁ_fire_hook__mutmut_4(self, event: str, agent: BaseAgent) -> None:
        """Fire all registered callbacks for an event."""
        for callback in self._hooks.get(event, ):
            try:
                callback(agent)
            except Exception as exc:
                logger.error("Hook %s error: %s", event, exc)

    def xǁAgentRuntimeǁ_fire_hook__mutmut_5(self, event: str, agent: BaseAgent) -> None:
        """Fire all registered callbacks for an event."""
        for callback in self._hooks.get(event, []):
            try:
                callback(None)
            except Exception as exc:
                logger.error("Hook %s error: %s", event, exc)

    def xǁAgentRuntimeǁ_fire_hook__mutmut_6(self, event: str, agent: BaseAgent) -> None:
        """Fire all registered callbacks for an event."""
        for callback in self._hooks.get(event, []):
            try:
                callback(agent)
            except Exception as exc:
                logger.error(None, event, exc)

    def xǁAgentRuntimeǁ_fire_hook__mutmut_7(self, event: str, agent: BaseAgent) -> None:
        """Fire all registered callbacks for an event."""
        for callback in self._hooks.get(event, []):
            try:
                callback(agent)
            except Exception as exc:
                logger.error("Hook %s error: %s", None, exc)

    def xǁAgentRuntimeǁ_fire_hook__mutmut_8(self, event: str, agent: BaseAgent) -> None:
        """Fire all registered callbacks for an event."""
        for callback in self._hooks.get(event, []):
            try:
                callback(agent)
            except Exception as exc:
                logger.error("Hook %s error: %s", event, None)

    def xǁAgentRuntimeǁ_fire_hook__mutmut_9(self, event: str, agent: BaseAgent) -> None:
        """Fire all registered callbacks for an event."""
        for callback in self._hooks.get(event, []):
            try:
                callback(agent)
            except Exception as exc:
                logger.error(event, exc)

    def xǁAgentRuntimeǁ_fire_hook__mutmut_10(self, event: str, agent: BaseAgent) -> None:
        """Fire all registered callbacks for an event."""
        for callback in self._hooks.get(event, []):
            try:
                callback(agent)
            except Exception as exc:
                logger.error("Hook %s error: %s", exc)

    def xǁAgentRuntimeǁ_fire_hook__mutmut_11(self, event: str, agent: BaseAgent) -> None:
        """Fire all registered callbacks for an event."""
        for callback in self._hooks.get(event, []):
            try:
                callback(agent)
            except Exception as exc:
                logger.error("Hook %s error: %s", event, )

    def xǁAgentRuntimeǁ_fire_hook__mutmut_12(self, event: str, agent: BaseAgent) -> None:
        """Fire all registered callbacks for an event."""
        for callback in self._hooks.get(event, []):
            try:
                callback(agent)
            except Exception as exc:
                logger.error("XXHook %s error: %sXX", event, exc)

    def xǁAgentRuntimeǁ_fire_hook__mutmut_13(self, event: str, agent: BaseAgent) -> None:
        """Fire all registered callbacks for an event."""
        for callback in self._hooks.get(event, []):
            try:
                callback(agent)
            except Exception as exc:
                logger.error("hook %s error: %s", event, exc)

    def xǁAgentRuntimeǁ_fire_hook__mutmut_14(self, event: str, agent: BaseAgent) -> None:
        """Fire all registered callbacks for an event."""
        for callback in self._hooks.get(event, []):
            try:
                callback(agent)
            except Exception as exc:
                logger.error("HOOK %S ERROR: %S", event, exc)

    # ── Stats ───────────────────────────────────────────────

    @_mutmut_mutated(mutants_xǁAgentRuntimeǁget_stats__mutmut)
    def get_stats(self) -> dict[str, Any]:
        """Get runtime statistics."""
        return {
            "total_spawned": self._stats.total_spawned,
            "total_terminated": self._stats.total_terminated,
            "total_errors": self._stats.total_errors,
            "active_count": self._stats.active_count,
            "peak_active": self._stats.peak_active,
            "total_iterations": sum(a._iteration_count for a in self._agents.values()),
            "agents_by_state": self._agents_by_state(),
        }

    # ── Stats ───────────────────────────────────────────────

    def xǁAgentRuntimeǁget_stats__mutmut_orig(self) -> dict[str, Any]:
        """Get runtime statistics."""
        return {
            "total_spawned": self._stats.total_spawned,
            "total_terminated": self._stats.total_terminated,
            "total_errors": self._stats.total_errors,
            "active_count": self._stats.active_count,
            "peak_active": self._stats.peak_active,
            "total_iterations": sum(a._iteration_count for a in self._agents.values()),
            "agents_by_state": self._agents_by_state(),
        }

    # ── Stats ───────────────────────────────────────────────

    def xǁAgentRuntimeǁget_stats__mutmut_1(self) -> dict[str, Any]:
        """Get runtime statistics."""
        return {
            "XXtotal_spawnedXX": self._stats.total_spawned,
            "total_terminated": self._stats.total_terminated,
            "total_errors": self._stats.total_errors,
            "active_count": self._stats.active_count,
            "peak_active": self._stats.peak_active,
            "total_iterations": sum(a._iteration_count for a in self._agents.values()),
            "agents_by_state": self._agents_by_state(),
        }

    # ── Stats ───────────────────────────────────────────────

    def xǁAgentRuntimeǁget_stats__mutmut_2(self) -> dict[str, Any]:
        """Get runtime statistics."""
        return {
            "TOTAL_SPAWNED": self._stats.total_spawned,
            "total_terminated": self._stats.total_terminated,
            "total_errors": self._stats.total_errors,
            "active_count": self._stats.active_count,
            "peak_active": self._stats.peak_active,
            "total_iterations": sum(a._iteration_count for a in self._agents.values()),
            "agents_by_state": self._agents_by_state(),
        }

    # ── Stats ───────────────────────────────────────────────

    def xǁAgentRuntimeǁget_stats__mutmut_3(self) -> dict[str, Any]:
        """Get runtime statistics."""
        return {
            "total_spawned": self._stats.total_spawned,
            "XXtotal_terminatedXX": self._stats.total_terminated,
            "total_errors": self._stats.total_errors,
            "active_count": self._stats.active_count,
            "peak_active": self._stats.peak_active,
            "total_iterations": sum(a._iteration_count for a in self._agents.values()),
            "agents_by_state": self._agents_by_state(),
        }

    # ── Stats ───────────────────────────────────────────────

    def xǁAgentRuntimeǁget_stats__mutmut_4(self) -> dict[str, Any]:
        """Get runtime statistics."""
        return {
            "total_spawned": self._stats.total_spawned,
            "TOTAL_TERMINATED": self._stats.total_terminated,
            "total_errors": self._stats.total_errors,
            "active_count": self._stats.active_count,
            "peak_active": self._stats.peak_active,
            "total_iterations": sum(a._iteration_count for a in self._agents.values()),
            "agents_by_state": self._agents_by_state(),
        }

    # ── Stats ───────────────────────────────────────────────

    def xǁAgentRuntimeǁget_stats__mutmut_5(self) -> dict[str, Any]:
        """Get runtime statistics."""
        return {
            "total_spawned": self._stats.total_spawned,
            "total_terminated": self._stats.total_terminated,
            "XXtotal_errorsXX": self._stats.total_errors,
            "active_count": self._stats.active_count,
            "peak_active": self._stats.peak_active,
            "total_iterations": sum(a._iteration_count for a in self._agents.values()),
            "agents_by_state": self._agents_by_state(),
        }

    # ── Stats ───────────────────────────────────────────────

    def xǁAgentRuntimeǁget_stats__mutmut_6(self) -> dict[str, Any]:
        """Get runtime statistics."""
        return {
            "total_spawned": self._stats.total_spawned,
            "total_terminated": self._stats.total_terminated,
            "TOTAL_ERRORS": self._stats.total_errors,
            "active_count": self._stats.active_count,
            "peak_active": self._stats.peak_active,
            "total_iterations": sum(a._iteration_count for a in self._agents.values()),
            "agents_by_state": self._agents_by_state(),
        }

    # ── Stats ───────────────────────────────────────────────

    def xǁAgentRuntimeǁget_stats__mutmut_7(self) -> dict[str, Any]:
        """Get runtime statistics."""
        return {
            "total_spawned": self._stats.total_spawned,
            "total_terminated": self._stats.total_terminated,
            "total_errors": self._stats.total_errors,
            "XXactive_countXX": self._stats.active_count,
            "peak_active": self._stats.peak_active,
            "total_iterations": sum(a._iteration_count for a in self._agents.values()),
            "agents_by_state": self._agents_by_state(),
        }

    # ── Stats ───────────────────────────────────────────────

    def xǁAgentRuntimeǁget_stats__mutmut_8(self) -> dict[str, Any]:
        """Get runtime statistics."""
        return {
            "total_spawned": self._stats.total_spawned,
            "total_terminated": self._stats.total_terminated,
            "total_errors": self._stats.total_errors,
            "ACTIVE_COUNT": self._stats.active_count,
            "peak_active": self._stats.peak_active,
            "total_iterations": sum(a._iteration_count for a in self._agents.values()),
            "agents_by_state": self._agents_by_state(),
        }

    # ── Stats ───────────────────────────────────────────────

    def xǁAgentRuntimeǁget_stats__mutmut_9(self) -> dict[str, Any]:
        """Get runtime statistics."""
        return {
            "total_spawned": self._stats.total_spawned,
            "total_terminated": self._stats.total_terminated,
            "total_errors": self._stats.total_errors,
            "active_count": self._stats.active_count,
            "XXpeak_activeXX": self._stats.peak_active,
            "total_iterations": sum(a._iteration_count for a in self._agents.values()),
            "agents_by_state": self._agents_by_state(),
        }

    # ── Stats ───────────────────────────────────────────────

    def xǁAgentRuntimeǁget_stats__mutmut_10(self) -> dict[str, Any]:
        """Get runtime statistics."""
        return {
            "total_spawned": self._stats.total_spawned,
            "total_terminated": self._stats.total_terminated,
            "total_errors": self._stats.total_errors,
            "active_count": self._stats.active_count,
            "PEAK_ACTIVE": self._stats.peak_active,
            "total_iterations": sum(a._iteration_count for a in self._agents.values()),
            "agents_by_state": self._agents_by_state(),
        }

    # ── Stats ───────────────────────────────────────────────

    def xǁAgentRuntimeǁget_stats__mutmut_11(self) -> dict[str, Any]:
        """Get runtime statistics."""
        return {
            "total_spawned": self._stats.total_spawned,
            "total_terminated": self._stats.total_terminated,
            "total_errors": self._stats.total_errors,
            "active_count": self._stats.active_count,
            "peak_active": self._stats.peak_active,
            "XXtotal_iterationsXX": sum(a._iteration_count for a in self._agents.values()),
            "agents_by_state": self._agents_by_state(),
        }

    # ── Stats ───────────────────────────────────────────────

    def xǁAgentRuntimeǁget_stats__mutmut_12(self) -> dict[str, Any]:
        """Get runtime statistics."""
        return {
            "total_spawned": self._stats.total_spawned,
            "total_terminated": self._stats.total_terminated,
            "total_errors": self._stats.total_errors,
            "active_count": self._stats.active_count,
            "peak_active": self._stats.peak_active,
            "TOTAL_ITERATIONS": sum(a._iteration_count for a in self._agents.values()),
            "agents_by_state": self._agents_by_state(),
        }

    # ── Stats ───────────────────────────────────────────────

    def xǁAgentRuntimeǁget_stats__mutmut_13(self) -> dict[str, Any]:
        """Get runtime statistics."""
        return {
            "total_spawned": self._stats.total_spawned,
            "total_terminated": self._stats.total_terminated,
            "total_errors": self._stats.total_errors,
            "active_count": self._stats.active_count,
            "peak_active": self._stats.peak_active,
            "total_iterations": sum(None),
            "agents_by_state": self._agents_by_state(),
        }

    # ── Stats ───────────────────────────────────────────────

    def xǁAgentRuntimeǁget_stats__mutmut_14(self) -> dict[str, Any]:
        """Get runtime statistics."""
        return {
            "total_spawned": self._stats.total_spawned,
            "total_terminated": self._stats.total_terminated,
            "total_errors": self._stats.total_errors,
            "active_count": self._stats.active_count,
            "peak_active": self._stats.peak_active,
            "total_iterations": sum(a._iteration_count for a in self._agents.values()),
            "XXagents_by_stateXX": self._agents_by_state(),
        }

    # ── Stats ───────────────────────────────────────────────

    def xǁAgentRuntimeǁget_stats__mutmut_15(self) -> dict[str, Any]:
        """Get runtime statistics."""
        return {
            "total_spawned": self._stats.total_spawned,
            "total_terminated": self._stats.total_terminated,
            "total_errors": self._stats.total_errors,
            "active_count": self._stats.active_count,
            "peak_active": self._stats.peak_active,
            "total_iterations": sum(a._iteration_count for a in self._agents.values()),
            "AGENTS_BY_STATE": self._agents_by_state(),
        }

    @_mutmut_mutated(mutants_xǁAgentRuntimeǁ_agents_by_state__mutmut)
    def _agents_by_state(self) -> dict[str, int]:
        """Count agents by current state."""
        counts: dict[str, int] = defaultdict(int)
        for agent in self._agents.values():
            counts[agent.state.value] += 1
        return dict(counts)

    def xǁAgentRuntimeǁ_agents_by_state__mutmut_orig(self) -> dict[str, int]:
        """Count agents by current state."""
        counts: dict[str, int] = defaultdict(int)
        for agent in self._agents.values():
            counts[agent.state.value] += 1
        return dict(counts)

    def xǁAgentRuntimeǁ_agents_by_state__mutmut_1(self) -> dict[str, int]:
        """Count agents by current state."""
        counts: dict[str, int] = None
        for agent in self._agents.values():
            counts[agent.state.value] += 1
        return dict(counts)

    def xǁAgentRuntimeǁ_agents_by_state__mutmut_2(self) -> dict[str, int]:
        """Count agents by current state."""
        counts: dict[str, int] = defaultdict(None)
        for agent in self._agents.values():
            counts[agent.state.value] += 1
        return dict(counts)

    def xǁAgentRuntimeǁ_agents_by_state__mutmut_3(self) -> dict[str, int]:
        """Count agents by current state."""
        counts: dict[str, int] = defaultdict(int)
        for agent in self._agents.values():
            counts[agent.state.value] = 1
        return dict(counts)

    def xǁAgentRuntimeǁ_agents_by_state__mutmut_4(self) -> dict[str, int]:
        """Count agents by current state."""
        counts: dict[str, int] = defaultdict(int)
        for agent in self._agents.values():
            counts[agent.state.value] -= 1
        return dict(counts)

    def xǁAgentRuntimeǁ_agents_by_state__mutmut_5(self) -> dict[str, int]:
        """Count agents by current state."""
        counts: dict[str, int] = defaultdict(int)
        for agent in self._agents.values():
            counts[agent.state.value] += 2
        return dict(counts)

    def xǁAgentRuntimeǁ_agents_by_state__mutmut_6(self) -> dict[str, int]:
        """Count agents by current state."""
        counts: dict[str, int] = defaultdict(int)
        for agent in self._agents.values():
            counts[agent.state.value] += 1
        return dict(None)

    @_mutmut_mutated(mutants_xǁAgentRuntimeǁshutdown__mutmut)
    def shutdown(self) -> None:
        """Gracefully shut down the runtime and terminate all agents."""
        self.stop_heartbeat()
        for agent_id in list(self._agents.keys()):
            self.terminate_agent(agent_id, force=True)
        logger.info("AgentRuntime shutdown complete")

    def xǁAgentRuntimeǁshutdown__mutmut_orig(self) -> None:
        """Gracefully shut down the runtime and terminate all agents."""
        self.stop_heartbeat()
        for agent_id in list(self._agents.keys()):
            self.terminate_agent(agent_id, force=True)
        logger.info("AgentRuntime shutdown complete")

    def xǁAgentRuntimeǁshutdown__mutmut_1(self) -> None:
        """Gracefully shut down the runtime and terminate all agents."""
        self.stop_heartbeat()
        for agent_id in list(None):
            self.terminate_agent(agent_id, force=True)
        logger.info("AgentRuntime shutdown complete")

    def xǁAgentRuntimeǁshutdown__mutmut_2(self) -> None:
        """Gracefully shut down the runtime and terminate all agents."""
        self.stop_heartbeat()
        for agent_id in list(self._agents.keys()):
            self.terminate_agent(None, force=True)
        logger.info("AgentRuntime shutdown complete")

    def xǁAgentRuntimeǁshutdown__mutmut_3(self) -> None:
        """Gracefully shut down the runtime and terminate all agents."""
        self.stop_heartbeat()
        for agent_id in list(self._agents.keys()):
            self.terminate_agent(agent_id, force=None)
        logger.info("AgentRuntime shutdown complete")

    def xǁAgentRuntimeǁshutdown__mutmut_4(self) -> None:
        """Gracefully shut down the runtime and terminate all agents."""
        self.stop_heartbeat()
        for agent_id in list(self._agents.keys()):
            self.terminate_agent(force=True)
        logger.info("AgentRuntime shutdown complete")

    def xǁAgentRuntimeǁshutdown__mutmut_5(self) -> None:
        """Gracefully shut down the runtime and terminate all agents."""
        self.stop_heartbeat()
        for agent_id in list(self._agents.keys()):
            self.terminate_agent(agent_id, )
        logger.info("AgentRuntime shutdown complete")

    def xǁAgentRuntimeǁshutdown__mutmut_6(self) -> None:
        """Gracefully shut down the runtime and terminate all agents."""
        self.stop_heartbeat()
        for agent_id in list(self._agents.keys()):
            self.terminate_agent(agent_id, force=False)
        logger.info("AgentRuntime shutdown complete")

    def xǁAgentRuntimeǁshutdown__mutmut_7(self) -> None:
        """Gracefully shut down the runtime and terminate all agents."""
        self.stop_heartbeat()
        for agent_id in list(self._agents.keys()):
            self.terminate_agent(agent_id, force=True)
        logger.info(None)

    def xǁAgentRuntimeǁshutdown__mutmut_8(self) -> None:
        """Gracefully shut down the runtime and terminate all agents."""
        self.stop_heartbeat()
        for agent_id in list(self._agents.keys()):
            self.terminate_agent(agent_id, force=True)
        logger.info("XXAgentRuntime shutdown completeXX")

    def xǁAgentRuntimeǁshutdown__mutmut_9(self) -> None:
        """Gracefully shut down the runtime and terminate all agents."""
        self.stop_heartbeat()
        for agent_id in list(self._agents.keys()):
            self.terminate_agent(agent_id, force=True)
        logger.info("agentruntime shutdown complete")

    def xǁAgentRuntimeǁshutdown__mutmut_10(self) -> None:
        """Gracefully shut down the runtime and terminate all agents."""
        self.stop_heartbeat()
        for agent_id in list(self._agents.keys()):
            self.terminate_agent(agent_id, force=True)
        logger.info("AGENTRUNTIME SHUTDOWN COMPLETE")

mutants_xǁAgentRuntimeǁ__init____mutmut['_mutmut_orig'] = AgentRuntime.xǁAgentRuntimeǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ__init____mutmut['xǁAgentRuntimeǁ__init____mutmut_1'] = AgentRuntime.xǁAgentRuntimeǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ__init____mutmut['xǁAgentRuntimeǁ__init____mutmut_2'] = AgentRuntime.xǁAgentRuntimeǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ__init____mutmut['xǁAgentRuntimeǁ__init____mutmut_3'] = AgentRuntime.xǁAgentRuntimeǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ__init____mutmut['xǁAgentRuntimeǁ__init____mutmut_4'] = AgentRuntime.xǁAgentRuntimeǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ__init____mutmut['xǁAgentRuntimeǁ__init____mutmut_5'] = AgentRuntime.xǁAgentRuntimeǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ__init____mutmut['xǁAgentRuntimeǁ__init____mutmut_6'] = AgentRuntime.xǁAgentRuntimeǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ__init____mutmut['xǁAgentRuntimeǁ__init____mutmut_7'] = AgentRuntime.xǁAgentRuntimeǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ__init____mutmut['xǁAgentRuntimeǁ__init____mutmut_8'] = AgentRuntime.xǁAgentRuntimeǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ__init____mutmut['xǁAgentRuntimeǁ__init____mutmut_9'] = AgentRuntime.xǁAgentRuntimeǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ__init____mutmut['xǁAgentRuntimeǁ__init____mutmut_10'] = AgentRuntime.xǁAgentRuntimeǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ__init____mutmut['xǁAgentRuntimeǁ__init____mutmut_11'] = AgentRuntime.xǁAgentRuntimeǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ__init____mutmut['xǁAgentRuntimeǁ__init____mutmut_12'] = AgentRuntime.xǁAgentRuntimeǁ__init____mutmut_12 # type: ignore # mutmut generated

mutants_xǁAgentRuntimeǁget_instance__mutmut['_mutmut_orig'] = AgentRuntime.xǁAgentRuntimeǁget_instance__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁget_instance__mutmut['xǁAgentRuntimeǁget_instance__mutmut_1'] = AgentRuntime.xǁAgentRuntimeǁget_instance__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁget_instance__mutmut['xǁAgentRuntimeǁget_instance__mutmut_2'] = AgentRuntime.xǁAgentRuntimeǁget_instance__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁget_instance__mutmut['xǁAgentRuntimeǁget_instance__mutmut_3'] = AgentRuntime.xǁAgentRuntimeǁget_instance__mutmut_3 # type: ignore # mutmut generated

mutants_xǁAgentRuntimeǁreset_instance__mutmut['_mutmut_orig'] = AgentRuntime.xǁAgentRuntimeǁreset_instance__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁreset_instance__mutmut['xǁAgentRuntimeǁreset_instance__mutmut_1'] = AgentRuntime.xǁAgentRuntimeǁreset_instance__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁreset_instance__mutmut['xǁAgentRuntimeǁreset_instance__mutmut_2'] = AgentRuntime.xǁAgentRuntimeǁreset_instance__mutmut_2 # type: ignore # mutmut generated

mutants_xǁAgentRuntimeǁspawn__mutmut['_mutmut_orig'] = AgentRuntime.xǁAgentRuntimeǁspawn__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁspawn__mutmut['xǁAgentRuntimeǁspawn__mutmut_1'] = AgentRuntime.xǁAgentRuntimeǁspawn__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁspawn__mutmut['xǁAgentRuntimeǁspawn__mutmut_2'] = AgentRuntime.xǁAgentRuntimeǁspawn__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁspawn__mutmut['xǁAgentRuntimeǁspawn__mutmut_3'] = AgentRuntime.xǁAgentRuntimeǁspawn__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁspawn__mutmut['xǁAgentRuntimeǁspawn__mutmut_4'] = AgentRuntime.xǁAgentRuntimeǁspawn__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁspawn__mutmut['xǁAgentRuntimeǁspawn__mutmut_5'] = AgentRuntime.xǁAgentRuntimeǁspawn__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁspawn__mutmut['xǁAgentRuntimeǁspawn__mutmut_6'] = AgentRuntime.xǁAgentRuntimeǁspawn__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁspawn__mutmut['xǁAgentRuntimeǁspawn__mutmut_7'] = AgentRuntime.xǁAgentRuntimeǁspawn__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁspawn__mutmut['xǁAgentRuntimeǁspawn__mutmut_8'] = AgentRuntime.xǁAgentRuntimeǁspawn__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁspawn__mutmut['xǁAgentRuntimeǁspawn__mutmut_9'] = AgentRuntime.xǁAgentRuntimeǁspawn__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁspawn__mutmut['xǁAgentRuntimeǁspawn__mutmut_10'] = AgentRuntime.xǁAgentRuntimeǁspawn__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁspawn__mutmut['xǁAgentRuntimeǁspawn__mutmut_11'] = AgentRuntime.xǁAgentRuntimeǁspawn__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁspawn__mutmut['xǁAgentRuntimeǁspawn__mutmut_12'] = AgentRuntime.xǁAgentRuntimeǁspawn__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁspawn__mutmut['xǁAgentRuntimeǁspawn__mutmut_13'] = AgentRuntime.xǁAgentRuntimeǁspawn__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁspawn__mutmut['xǁAgentRuntimeǁspawn__mutmut_14'] = AgentRuntime.xǁAgentRuntimeǁspawn__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁspawn__mutmut['xǁAgentRuntimeǁspawn__mutmut_15'] = AgentRuntime.xǁAgentRuntimeǁspawn__mutmut_15 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁspawn__mutmut['xǁAgentRuntimeǁspawn__mutmut_16'] = AgentRuntime.xǁAgentRuntimeǁspawn__mutmut_16 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁspawn__mutmut['xǁAgentRuntimeǁspawn__mutmut_17'] = AgentRuntime.xǁAgentRuntimeǁspawn__mutmut_17 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁspawn__mutmut['xǁAgentRuntimeǁspawn__mutmut_18'] = AgentRuntime.xǁAgentRuntimeǁspawn__mutmut_18 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁspawn__mutmut['xǁAgentRuntimeǁspawn__mutmut_19'] = AgentRuntime.xǁAgentRuntimeǁspawn__mutmut_19 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁspawn__mutmut['xǁAgentRuntimeǁspawn__mutmut_20'] = AgentRuntime.xǁAgentRuntimeǁspawn__mutmut_20 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁspawn__mutmut['xǁAgentRuntimeǁspawn__mutmut_21'] = AgentRuntime.xǁAgentRuntimeǁspawn__mutmut_21 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁspawn__mutmut['xǁAgentRuntimeǁspawn__mutmut_22'] = AgentRuntime.xǁAgentRuntimeǁspawn__mutmut_22 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁspawn__mutmut['xǁAgentRuntimeǁspawn__mutmut_23'] = AgentRuntime.xǁAgentRuntimeǁspawn__mutmut_23 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁspawn__mutmut['xǁAgentRuntimeǁspawn__mutmut_24'] = AgentRuntime.xǁAgentRuntimeǁspawn__mutmut_24 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁspawn__mutmut['xǁAgentRuntimeǁspawn__mutmut_25'] = AgentRuntime.xǁAgentRuntimeǁspawn__mutmut_25 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁspawn__mutmut['xǁAgentRuntimeǁspawn__mutmut_26'] = AgentRuntime.xǁAgentRuntimeǁspawn__mutmut_26 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁspawn__mutmut['xǁAgentRuntimeǁspawn__mutmut_27'] = AgentRuntime.xǁAgentRuntimeǁspawn__mutmut_27 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁspawn__mutmut['xǁAgentRuntimeǁspawn__mutmut_28'] = AgentRuntime.xǁAgentRuntimeǁspawn__mutmut_28 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁspawn__mutmut['xǁAgentRuntimeǁspawn__mutmut_29'] = AgentRuntime.xǁAgentRuntimeǁspawn__mutmut_29 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁspawn__mutmut['xǁAgentRuntimeǁspawn__mutmut_30'] = AgentRuntime.xǁAgentRuntimeǁspawn__mutmut_30 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁspawn__mutmut['xǁAgentRuntimeǁspawn__mutmut_31'] = AgentRuntime.xǁAgentRuntimeǁspawn__mutmut_31 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁspawn__mutmut['xǁAgentRuntimeǁspawn__mutmut_32'] = AgentRuntime.xǁAgentRuntimeǁspawn__mutmut_32 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁspawn__mutmut['xǁAgentRuntimeǁspawn__mutmut_33'] = AgentRuntime.xǁAgentRuntimeǁspawn__mutmut_33 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁspawn__mutmut['xǁAgentRuntimeǁspawn__mutmut_34'] = AgentRuntime.xǁAgentRuntimeǁspawn__mutmut_34 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁspawn__mutmut['xǁAgentRuntimeǁspawn__mutmut_35'] = AgentRuntime.xǁAgentRuntimeǁspawn__mutmut_35 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁspawn__mutmut['xǁAgentRuntimeǁspawn__mutmut_36'] = AgentRuntime.xǁAgentRuntimeǁspawn__mutmut_36 # type: ignore # mutmut generated

mutants_xǁAgentRuntimeǁterminate_agent__mutmut['_mutmut_orig'] = AgentRuntime.xǁAgentRuntimeǁterminate_agent__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁterminate_agent__mutmut['xǁAgentRuntimeǁterminate_agent__mutmut_1'] = AgentRuntime.xǁAgentRuntimeǁterminate_agent__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁterminate_agent__mutmut['xǁAgentRuntimeǁterminate_agent__mutmut_2'] = AgentRuntime.xǁAgentRuntimeǁterminate_agent__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁterminate_agent__mutmut['xǁAgentRuntimeǁterminate_agent__mutmut_3'] = AgentRuntime.xǁAgentRuntimeǁterminate_agent__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁterminate_agent__mutmut['xǁAgentRuntimeǁterminate_agent__mutmut_4'] = AgentRuntime.xǁAgentRuntimeǁterminate_agent__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁterminate_agent__mutmut['xǁAgentRuntimeǁterminate_agent__mutmut_5'] = AgentRuntime.xǁAgentRuntimeǁterminate_agent__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁterminate_agent__mutmut['xǁAgentRuntimeǁterminate_agent__mutmut_6'] = AgentRuntime.xǁAgentRuntimeǁterminate_agent__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁterminate_agent__mutmut['xǁAgentRuntimeǁterminate_agent__mutmut_7'] = AgentRuntime.xǁAgentRuntimeǁterminate_agent__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁterminate_agent__mutmut['xǁAgentRuntimeǁterminate_agent__mutmut_8'] = AgentRuntime.xǁAgentRuntimeǁterminate_agent__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁterminate_agent__mutmut['xǁAgentRuntimeǁterminate_agent__mutmut_9'] = AgentRuntime.xǁAgentRuntimeǁterminate_agent__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁterminate_agent__mutmut['xǁAgentRuntimeǁterminate_agent__mutmut_10'] = AgentRuntime.xǁAgentRuntimeǁterminate_agent__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁterminate_agent__mutmut['xǁAgentRuntimeǁterminate_agent__mutmut_11'] = AgentRuntime.xǁAgentRuntimeǁterminate_agent__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁterminate_agent__mutmut['xǁAgentRuntimeǁterminate_agent__mutmut_12'] = AgentRuntime.xǁAgentRuntimeǁterminate_agent__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁterminate_agent__mutmut['xǁAgentRuntimeǁterminate_agent__mutmut_13'] = AgentRuntime.xǁAgentRuntimeǁterminate_agent__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁterminate_agent__mutmut['xǁAgentRuntimeǁterminate_agent__mutmut_14'] = AgentRuntime.xǁAgentRuntimeǁterminate_agent__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁterminate_agent__mutmut['xǁAgentRuntimeǁterminate_agent__mutmut_15'] = AgentRuntime.xǁAgentRuntimeǁterminate_agent__mutmut_15 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁterminate_agent__mutmut['xǁAgentRuntimeǁterminate_agent__mutmut_16'] = AgentRuntime.xǁAgentRuntimeǁterminate_agent__mutmut_16 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁterminate_agent__mutmut['xǁAgentRuntimeǁterminate_agent__mutmut_17'] = AgentRuntime.xǁAgentRuntimeǁterminate_agent__mutmut_17 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁterminate_agent__mutmut['xǁAgentRuntimeǁterminate_agent__mutmut_18'] = AgentRuntime.xǁAgentRuntimeǁterminate_agent__mutmut_18 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁterminate_agent__mutmut['xǁAgentRuntimeǁterminate_agent__mutmut_19'] = AgentRuntime.xǁAgentRuntimeǁterminate_agent__mutmut_19 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁterminate_agent__mutmut['xǁAgentRuntimeǁterminate_agent__mutmut_20'] = AgentRuntime.xǁAgentRuntimeǁterminate_agent__mutmut_20 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁterminate_agent__mutmut['xǁAgentRuntimeǁterminate_agent__mutmut_21'] = AgentRuntime.xǁAgentRuntimeǁterminate_agent__mutmut_21 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁterminate_agent__mutmut['xǁAgentRuntimeǁterminate_agent__mutmut_22'] = AgentRuntime.xǁAgentRuntimeǁterminate_agent__mutmut_22 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁterminate_agent__mutmut['xǁAgentRuntimeǁterminate_agent__mutmut_23'] = AgentRuntime.xǁAgentRuntimeǁterminate_agent__mutmut_23 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁterminate_agent__mutmut['xǁAgentRuntimeǁterminate_agent__mutmut_24'] = AgentRuntime.xǁAgentRuntimeǁterminate_agent__mutmut_24 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁterminate_agent__mutmut['xǁAgentRuntimeǁterminate_agent__mutmut_25'] = AgentRuntime.xǁAgentRuntimeǁterminate_agent__mutmut_25 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁterminate_agent__mutmut['xǁAgentRuntimeǁterminate_agent__mutmut_26'] = AgentRuntime.xǁAgentRuntimeǁterminate_agent__mutmut_26 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁterminate_agent__mutmut['xǁAgentRuntimeǁterminate_agent__mutmut_27'] = AgentRuntime.xǁAgentRuntimeǁterminate_agent__mutmut_27 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁterminate_agent__mutmut['xǁAgentRuntimeǁterminate_agent__mutmut_28'] = AgentRuntime.xǁAgentRuntimeǁterminate_agent__mutmut_28 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁterminate_agent__mutmut['xǁAgentRuntimeǁterminate_agent__mutmut_29'] = AgentRuntime.xǁAgentRuntimeǁterminate_agent__mutmut_29 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁterminate_agent__mutmut['xǁAgentRuntimeǁterminate_agent__mutmut_30'] = AgentRuntime.xǁAgentRuntimeǁterminate_agent__mutmut_30 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁterminate_agent__mutmut['xǁAgentRuntimeǁterminate_agent__mutmut_31'] = AgentRuntime.xǁAgentRuntimeǁterminate_agent__mutmut_31 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁterminate_agent__mutmut['xǁAgentRuntimeǁterminate_agent__mutmut_32'] = AgentRuntime.xǁAgentRuntimeǁterminate_agent__mutmut_32 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁterminate_agent__mutmut['xǁAgentRuntimeǁterminate_agent__mutmut_33'] = AgentRuntime.xǁAgentRuntimeǁterminate_agent__mutmut_33 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁterminate_agent__mutmut['xǁAgentRuntimeǁterminate_agent__mutmut_34'] = AgentRuntime.xǁAgentRuntimeǁterminate_agent__mutmut_34 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁterminate_agent__mutmut['xǁAgentRuntimeǁterminate_agent__mutmut_35'] = AgentRuntime.xǁAgentRuntimeǁterminate_agent__mutmut_35 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁterminate_agent__mutmut['xǁAgentRuntimeǁterminate_agent__mutmut_36'] = AgentRuntime.xǁAgentRuntimeǁterminate_agent__mutmut_36 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁterminate_agent__mutmut['xǁAgentRuntimeǁterminate_agent__mutmut_37'] = AgentRuntime.xǁAgentRuntimeǁterminate_agent__mutmut_37 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁterminate_agent__mutmut['xǁAgentRuntimeǁterminate_agent__mutmut_38'] = AgentRuntime.xǁAgentRuntimeǁterminate_agent__mutmut_38 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁterminate_agent__mutmut['xǁAgentRuntimeǁterminate_agent__mutmut_39'] = AgentRuntime.xǁAgentRuntimeǁterminate_agent__mutmut_39 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁterminate_agent__mutmut['xǁAgentRuntimeǁterminate_agent__mutmut_40'] = AgentRuntime.xǁAgentRuntimeǁterminate_agent__mutmut_40 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁterminate_agent__mutmut['xǁAgentRuntimeǁterminate_agent__mutmut_41'] = AgentRuntime.xǁAgentRuntimeǁterminate_agent__mutmut_41 # type: ignore # mutmut generated

mutants_xǁAgentRuntimeǁpause_agent__mutmut['_mutmut_orig'] = AgentRuntime.xǁAgentRuntimeǁpause_agent__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁpause_agent__mutmut['xǁAgentRuntimeǁpause_agent__mutmut_1'] = AgentRuntime.xǁAgentRuntimeǁpause_agent__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁpause_agent__mutmut['xǁAgentRuntimeǁpause_agent__mutmut_2'] = AgentRuntime.xǁAgentRuntimeǁpause_agent__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁpause_agent__mutmut['xǁAgentRuntimeǁpause_agent__mutmut_3'] = AgentRuntime.xǁAgentRuntimeǁpause_agent__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁpause_agent__mutmut['xǁAgentRuntimeǁpause_agent__mutmut_4'] = AgentRuntime.xǁAgentRuntimeǁpause_agent__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁpause_agent__mutmut['xǁAgentRuntimeǁpause_agent__mutmut_5'] = AgentRuntime.xǁAgentRuntimeǁpause_agent__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁpause_agent__mutmut['xǁAgentRuntimeǁpause_agent__mutmut_6'] = AgentRuntime.xǁAgentRuntimeǁpause_agent__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁpause_agent__mutmut['xǁAgentRuntimeǁpause_agent__mutmut_7'] = AgentRuntime.xǁAgentRuntimeǁpause_agent__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁpause_agent__mutmut['xǁAgentRuntimeǁpause_agent__mutmut_8'] = AgentRuntime.xǁAgentRuntimeǁpause_agent__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁpause_agent__mutmut['xǁAgentRuntimeǁpause_agent__mutmut_9'] = AgentRuntime.xǁAgentRuntimeǁpause_agent__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁpause_agent__mutmut['xǁAgentRuntimeǁpause_agent__mutmut_10'] = AgentRuntime.xǁAgentRuntimeǁpause_agent__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁpause_agent__mutmut['xǁAgentRuntimeǁpause_agent__mutmut_11'] = AgentRuntime.xǁAgentRuntimeǁpause_agent__mutmut_11 # type: ignore # mutmut generated

mutants_xǁAgentRuntimeǁresume_agent__mutmut['_mutmut_orig'] = AgentRuntime.xǁAgentRuntimeǁresume_agent__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁresume_agent__mutmut['xǁAgentRuntimeǁresume_agent__mutmut_1'] = AgentRuntime.xǁAgentRuntimeǁresume_agent__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁresume_agent__mutmut['xǁAgentRuntimeǁresume_agent__mutmut_2'] = AgentRuntime.xǁAgentRuntimeǁresume_agent__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁresume_agent__mutmut['xǁAgentRuntimeǁresume_agent__mutmut_3'] = AgentRuntime.xǁAgentRuntimeǁresume_agent__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁresume_agent__mutmut['xǁAgentRuntimeǁresume_agent__mutmut_4'] = AgentRuntime.xǁAgentRuntimeǁresume_agent__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁresume_agent__mutmut['xǁAgentRuntimeǁresume_agent__mutmut_5'] = AgentRuntime.xǁAgentRuntimeǁresume_agent__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁresume_agent__mutmut['xǁAgentRuntimeǁresume_agent__mutmut_6'] = AgentRuntime.xǁAgentRuntimeǁresume_agent__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁresume_agent__mutmut['xǁAgentRuntimeǁresume_agent__mutmut_7'] = AgentRuntime.xǁAgentRuntimeǁresume_agent__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁresume_agent__mutmut['xǁAgentRuntimeǁresume_agent__mutmut_8'] = AgentRuntime.xǁAgentRuntimeǁresume_agent__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁresume_agent__mutmut['xǁAgentRuntimeǁresume_agent__mutmut_9'] = AgentRuntime.xǁAgentRuntimeǁresume_agent__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁresume_agent__mutmut['xǁAgentRuntimeǁresume_agent__mutmut_10'] = AgentRuntime.xǁAgentRuntimeǁresume_agent__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁresume_agent__mutmut['xǁAgentRuntimeǁresume_agent__mutmut_11'] = AgentRuntime.xǁAgentRuntimeǁresume_agent__mutmut_11 # type: ignore # mutmut generated

mutants_xǁAgentRuntimeǁget_agent__mutmut['_mutmut_orig'] = AgentRuntime.xǁAgentRuntimeǁget_agent__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁget_agent__mutmut['xǁAgentRuntimeǁget_agent__mutmut_1'] = AgentRuntime.xǁAgentRuntimeǁget_agent__mutmut_1 # type: ignore # mutmut generated

mutants_xǁAgentRuntimeǁlist_agents__mutmut['_mutmut_orig'] = AgentRuntime.xǁAgentRuntimeǁlist_agents__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁlist_agents__mutmut['xǁAgentRuntimeǁlist_agents__mutmut_1'] = AgentRuntime.xǁAgentRuntimeǁlist_agents__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁlist_agents__mutmut['xǁAgentRuntimeǁlist_agents__mutmut_2'] = AgentRuntime.xǁAgentRuntimeǁlist_agents__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁlist_agents__mutmut['xǁAgentRuntimeǁlist_agents__mutmut_3'] = AgentRuntime.xǁAgentRuntimeǁlist_agents__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁlist_agents__mutmut['xǁAgentRuntimeǁlist_agents__mutmut_4'] = AgentRuntime.xǁAgentRuntimeǁlist_agents__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁlist_agents__mutmut['xǁAgentRuntimeǁlist_agents__mutmut_5'] = AgentRuntime.xǁAgentRuntimeǁlist_agents__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁlist_agents__mutmut['xǁAgentRuntimeǁlist_agents__mutmut_6'] = AgentRuntime.xǁAgentRuntimeǁlist_agents__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁlist_agents__mutmut['xǁAgentRuntimeǁlist_agents__mutmut_7'] = AgentRuntime.xǁAgentRuntimeǁlist_agents__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁlist_agents__mutmut['xǁAgentRuntimeǁlist_agents__mutmut_8'] = AgentRuntime.xǁAgentRuntimeǁlist_agents__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁlist_agents__mutmut['xǁAgentRuntimeǁlist_agents__mutmut_9'] = AgentRuntime.xǁAgentRuntimeǁlist_agents__mutmut_9 # type: ignore # mutmut generated

mutants_xǁAgentRuntimeǁget_agent_status__mutmut['_mutmut_orig'] = AgentRuntime.xǁAgentRuntimeǁget_agent_status__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁget_agent_status__mutmut['xǁAgentRuntimeǁget_agent_status__mutmut_1'] = AgentRuntime.xǁAgentRuntimeǁget_agent_status__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁget_agent_status__mutmut['xǁAgentRuntimeǁget_agent_status__mutmut_2'] = AgentRuntime.xǁAgentRuntimeǁget_agent_status__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁget_agent_status__mutmut['xǁAgentRuntimeǁget_agent_status__mutmut_3'] = AgentRuntime.xǁAgentRuntimeǁget_agent_status__mutmut_3 # type: ignore # mutmut generated

mutants_xǁAgentRuntimeǁroute_message__mutmut['_mutmut_orig'] = AgentRuntime.xǁAgentRuntimeǁroute_message__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁroute_message__mutmut['xǁAgentRuntimeǁroute_message__mutmut_1'] = AgentRuntime.xǁAgentRuntimeǁroute_message__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁroute_message__mutmut['xǁAgentRuntimeǁroute_message__mutmut_2'] = AgentRuntime.xǁAgentRuntimeǁroute_message__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁroute_message__mutmut['xǁAgentRuntimeǁroute_message__mutmut_3'] = AgentRuntime.xǁAgentRuntimeǁroute_message__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁroute_message__mutmut['xǁAgentRuntimeǁroute_message__mutmut_4'] = AgentRuntime.xǁAgentRuntimeǁroute_message__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁroute_message__mutmut['xǁAgentRuntimeǁroute_message__mutmut_5'] = AgentRuntime.xǁAgentRuntimeǁroute_message__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁroute_message__mutmut['xǁAgentRuntimeǁroute_message__mutmut_6'] = AgentRuntime.xǁAgentRuntimeǁroute_message__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁroute_message__mutmut['xǁAgentRuntimeǁroute_message__mutmut_7'] = AgentRuntime.xǁAgentRuntimeǁroute_message__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁroute_message__mutmut['xǁAgentRuntimeǁroute_message__mutmut_8'] = AgentRuntime.xǁAgentRuntimeǁroute_message__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁroute_message__mutmut['xǁAgentRuntimeǁroute_message__mutmut_9'] = AgentRuntime.xǁAgentRuntimeǁroute_message__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁroute_message__mutmut['xǁAgentRuntimeǁroute_message__mutmut_10'] = AgentRuntime.xǁAgentRuntimeǁroute_message__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁroute_message__mutmut['xǁAgentRuntimeǁroute_message__mutmut_11'] = AgentRuntime.xǁAgentRuntimeǁroute_message__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁroute_message__mutmut['xǁAgentRuntimeǁroute_message__mutmut_12'] = AgentRuntime.xǁAgentRuntimeǁroute_message__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁroute_message__mutmut['xǁAgentRuntimeǁroute_message__mutmut_13'] = AgentRuntime.xǁAgentRuntimeǁroute_message__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁroute_message__mutmut['xǁAgentRuntimeǁroute_message__mutmut_14'] = AgentRuntime.xǁAgentRuntimeǁroute_message__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁroute_message__mutmut['xǁAgentRuntimeǁroute_message__mutmut_15'] = AgentRuntime.xǁAgentRuntimeǁroute_message__mutmut_15 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁroute_message__mutmut['xǁAgentRuntimeǁroute_message__mutmut_16'] = AgentRuntime.xǁAgentRuntimeǁroute_message__mutmut_16 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁroute_message__mutmut['xǁAgentRuntimeǁroute_message__mutmut_17'] = AgentRuntime.xǁAgentRuntimeǁroute_message__mutmut_17 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁroute_message__mutmut['xǁAgentRuntimeǁroute_message__mutmut_18'] = AgentRuntime.xǁAgentRuntimeǁroute_message__mutmut_18 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁroute_message__mutmut['xǁAgentRuntimeǁroute_message__mutmut_19'] = AgentRuntime.xǁAgentRuntimeǁroute_message__mutmut_19 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁroute_message__mutmut['xǁAgentRuntimeǁroute_message__mutmut_20'] = AgentRuntime.xǁAgentRuntimeǁroute_message__mutmut_20 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁroute_message__mutmut['xǁAgentRuntimeǁroute_message__mutmut_21'] = AgentRuntime.xǁAgentRuntimeǁroute_message__mutmut_21 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁroute_message__mutmut['xǁAgentRuntimeǁroute_message__mutmut_22'] = AgentRuntime.xǁAgentRuntimeǁroute_message__mutmut_22 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁroute_message__mutmut['xǁAgentRuntimeǁroute_message__mutmut_23'] = AgentRuntime.xǁAgentRuntimeǁroute_message__mutmut_23 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁroute_message__mutmut['xǁAgentRuntimeǁroute_message__mutmut_24'] = AgentRuntime.xǁAgentRuntimeǁroute_message__mutmut_24 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁroute_message__mutmut['xǁAgentRuntimeǁroute_message__mutmut_25'] = AgentRuntime.xǁAgentRuntimeǁroute_message__mutmut_25 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁroute_message__mutmut['xǁAgentRuntimeǁroute_message__mutmut_26'] = AgentRuntime.xǁAgentRuntimeǁroute_message__mutmut_26 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁroute_message__mutmut['xǁAgentRuntimeǁroute_message__mutmut_27'] = AgentRuntime.xǁAgentRuntimeǁroute_message__mutmut_27 # type: ignore # mutmut generated

mutants_xǁAgentRuntimeǁbroadcast__mutmut['_mutmut_orig'] = AgentRuntime.xǁAgentRuntimeǁbroadcast__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁbroadcast__mutmut['xǁAgentRuntimeǁbroadcast__mutmut_1'] = AgentRuntime.xǁAgentRuntimeǁbroadcast__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁbroadcast__mutmut['xǁAgentRuntimeǁbroadcast__mutmut_2'] = AgentRuntime.xǁAgentRuntimeǁbroadcast__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁbroadcast__mutmut['xǁAgentRuntimeǁbroadcast__mutmut_3'] = AgentRuntime.xǁAgentRuntimeǁbroadcast__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁbroadcast__mutmut['xǁAgentRuntimeǁbroadcast__mutmut_4'] = AgentRuntime.xǁAgentRuntimeǁbroadcast__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁbroadcast__mutmut['xǁAgentRuntimeǁbroadcast__mutmut_5'] = AgentRuntime.xǁAgentRuntimeǁbroadcast__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁbroadcast__mutmut['xǁAgentRuntimeǁbroadcast__mutmut_6'] = AgentRuntime.xǁAgentRuntimeǁbroadcast__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁbroadcast__mutmut['xǁAgentRuntimeǁbroadcast__mutmut_7'] = AgentRuntime.xǁAgentRuntimeǁbroadcast__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁbroadcast__mutmut['xǁAgentRuntimeǁbroadcast__mutmut_8'] = AgentRuntime.xǁAgentRuntimeǁbroadcast__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁbroadcast__mutmut['xǁAgentRuntimeǁbroadcast__mutmut_9'] = AgentRuntime.xǁAgentRuntimeǁbroadcast__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁbroadcast__mutmut['xǁAgentRuntimeǁbroadcast__mutmut_10'] = AgentRuntime.xǁAgentRuntimeǁbroadcast__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁbroadcast__mutmut['xǁAgentRuntimeǁbroadcast__mutmut_11'] = AgentRuntime.xǁAgentRuntimeǁbroadcast__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁbroadcast__mutmut['xǁAgentRuntimeǁbroadcast__mutmut_12'] = AgentRuntime.xǁAgentRuntimeǁbroadcast__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁbroadcast__mutmut['xǁAgentRuntimeǁbroadcast__mutmut_13'] = AgentRuntime.xǁAgentRuntimeǁbroadcast__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁbroadcast__mutmut['xǁAgentRuntimeǁbroadcast__mutmut_14'] = AgentRuntime.xǁAgentRuntimeǁbroadcast__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁbroadcast__mutmut['xǁAgentRuntimeǁbroadcast__mutmut_15'] = AgentRuntime.xǁAgentRuntimeǁbroadcast__mutmut_15 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁbroadcast__mutmut['xǁAgentRuntimeǁbroadcast__mutmut_16'] = AgentRuntime.xǁAgentRuntimeǁbroadcast__mutmut_16 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁbroadcast__mutmut['xǁAgentRuntimeǁbroadcast__mutmut_17'] = AgentRuntime.xǁAgentRuntimeǁbroadcast__mutmut_17 # type: ignore # mutmut generated

mutants_xǁAgentRuntimeǁstart_heartbeat__mutmut['_mutmut_orig'] = AgentRuntime.xǁAgentRuntimeǁstart_heartbeat__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁstart_heartbeat__mutmut['xǁAgentRuntimeǁstart_heartbeat__mutmut_1'] = AgentRuntime.xǁAgentRuntimeǁstart_heartbeat__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁstart_heartbeat__mutmut['xǁAgentRuntimeǁstart_heartbeat__mutmut_2'] = AgentRuntime.xǁAgentRuntimeǁstart_heartbeat__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁstart_heartbeat__mutmut['xǁAgentRuntimeǁstart_heartbeat__mutmut_3'] = AgentRuntime.xǁAgentRuntimeǁstart_heartbeat__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁstart_heartbeat__mutmut['xǁAgentRuntimeǁstart_heartbeat__mutmut_4'] = AgentRuntime.xǁAgentRuntimeǁstart_heartbeat__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁstart_heartbeat__mutmut['xǁAgentRuntimeǁstart_heartbeat__mutmut_5'] = AgentRuntime.xǁAgentRuntimeǁstart_heartbeat__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁstart_heartbeat__mutmut['xǁAgentRuntimeǁstart_heartbeat__mutmut_6'] = AgentRuntime.xǁAgentRuntimeǁstart_heartbeat__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁstart_heartbeat__mutmut['xǁAgentRuntimeǁstart_heartbeat__mutmut_7'] = AgentRuntime.xǁAgentRuntimeǁstart_heartbeat__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁstart_heartbeat__mutmut['xǁAgentRuntimeǁstart_heartbeat__mutmut_8'] = AgentRuntime.xǁAgentRuntimeǁstart_heartbeat__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁstart_heartbeat__mutmut['xǁAgentRuntimeǁstart_heartbeat__mutmut_9'] = AgentRuntime.xǁAgentRuntimeǁstart_heartbeat__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁstart_heartbeat__mutmut['xǁAgentRuntimeǁstart_heartbeat__mutmut_10'] = AgentRuntime.xǁAgentRuntimeǁstart_heartbeat__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁstart_heartbeat__mutmut['xǁAgentRuntimeǁstart_heartbeat__mutmut_11'] = AgentRuntime.xǁAgentRuntimeǁstart_heartbeat__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁstart_heartbeat__mutmut['xǁAgentRuntimeǁstart_heartbeat__mutmut_12'] = AgentRuntime.xǁAgentRuntimeǁstart_heartbeat__mutmut_12 # type: ignore # mutmut generated

mutants_xǁAgentRuntimeǁstop_heartbeat__mutmut['_mutmut_orig'] = AgentRuntime.xǁAgentRuntimeǁstop_heartbeat__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁstop_heartbeat__mutmut['xǁAgentRuntimeǁstop_heartbeat__mutmut_1'] = AgentRuntime.xǁAgentRuntimeǁstop_heartbeat__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁstop_heartbeat__mutmut['xǁAgentRuntimeǁstop_heartbeat__mutmut_2'] = AgentRuntime.xǁAgentRuntimeǁstop_heartbeat__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁstop_heartbeat__mutmut['xǁAgentRuntimeǁstop_heartbeat__mutmut_3'] = AgentRuntime.xǁAgentRuntimeǁstop_heartbeat__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁstop_heartbeat__mutmut['xǁAgentRuntimeǁstop_heartbeat__mutmut_4'] = AgentRuntime.xǁAgentRuntimeǁstop_heartbeat__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁstop_heartbeat__mutmut['xǁAgentRuntimeǁstop_heartbeat__mutmut_5'] = AgentRuntime.xǁAgentRuntimeǁstop_heartbeat__mutmut_5 # type: ignore # mutmut generated

mutants_xǁAgentRuntimeǁ_heartbeat_loop__mutmut['_mutmut_orig'] = AgentRuntime.xǁAgentRuntimeǁ_heartbeat_loop__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_heartbeat_loop__mutmut['xǁAgentRuntimeǁ_heartbeat_loop__mutmut_1'] = AgentRuntime.xǁAgentRuntimeǁ_heartbeat_loop__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_heartbeat_loop__mutmut['xǁAgentRuntimeǁ_heartbeat_loop__mutmut_2'] = AgentRuntime.xǁAgentRuntimeǁ_heartbeat_loop__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_heartbeat_loop__mutmut['xǁAgentRuntimeǁ_heartbeat_loop__mutmut_3'] = AgentRuntime.xǁAgentRuntimeǁ_heartbeat_loop__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_heartbeat_loop__mutmut['xǁAgentRuntimeǁ_heartbeat_loop__mutmut_4'] = AgentRuntime.xǁAgentRuntimeǁ_heartbeat_loop__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_heartbeat_loop__mutmut['xǁAgentRuntimeǁ_heartbeat_loop__mutmut_5'] = AgentRuntime.xǁAgentRuntimeǁ_heartbeat_loop__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_heartbeat_loop__mutmut['xǁAgentRuntimeǁ_heartbeat_loop__mutmut_6'] = AgentRuntime.xǁAgentRuntimeǁ_heartbeat_loop__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_heartbeat_loop__mutmut['xǁAgentRuntimeǁ_heartbeat_loop__mutmut_7'] = AgentRuntime.xǁAgentRuntimeǁ_heartbeat_loop__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_heartbeat_loop__mutmut['xǁAgentRuntimeǁ_heartbeat_loop__mutmut_8'] = AgentRuntime.xǁAgentRuntimeǁ_heartbeat_loop__mutmut_8 # type: ignore # mutmut generated

mutants_xǁAgentRuntimeǁ_check_agents_health__mutmut['_mutmut_orig'] = AgentRuntime.xǁAgentRuntimeǁ_check_agents_health__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_check_agents_health__mutmut['xǁAgentRuntimeǁ_check_agents_health__mutmut_1'] = AgentRuntime.xǁAgentRuntimeǁ_check_agents_health__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_check_agents_health__mutmut['xǁAgentRuntimeǁ_check_agents_health__mutmut_2'] = AgentRuntime.xǁAgentRuntimeǁ_check_agents_health__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_check_agents_health__mutmut['xǁAgentRuntimeǁ_check_agents_health__mutmut_3'] = AgentRuntime.xǁAgentRuntimeǁ_check_agents_health__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_check_agents_health__mutmut['xǁAgentRuntimeǁ_check_agents_health__mutmut_4'] = AgentRuntime.xǁAgentRuntimeǁ_check_agents_health__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_check_agents_health__mutmut['xǁAgentRuntimeǁ_check_agents_health__mutmut_5'] = AgentRuntime.xǁAgentRuntimeǁ_check_agents_health__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_check_agents_health__mutmut['xǁAgentRuntimeǁ_check_agents_health__mutmut_6'] = AgentRuntime.xǁAgentRuntimeǁ_check_agents_health__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_check_agents_health__mutmut['xǁAgentRuntimeǁ_check_agents_health__mutmut_7'] = AgentRuntime.xǁAgentRuntimeǁ_check_agents_health__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_check_agents_health__mutmut['xǁAgentRuntimeǁ_check_agents_health__mutmut_8'] = AgentRuntime.xǁAgentRuntimeǁ_check_agents_health__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_check_agents_health__mutmut['xǁAgentRuntimeǁ_check_agents_health__mutmut_9'] = AgentRuntime.xǁAgentRuntimeǁ_check_agents_health__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_check_agents_health__mutmut['xǁAgentRuntimeǁ_check_agents_health__mutmut_10'] = AgentRuntime.xǁAgentRuntimeǁ_check_agents_health__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_check_agents_health__mutmut['xǁAgentRuntimeǁ_check_agents_health__mutmut_11'] = AgentRuntime.xǁAgentRuntimeǁ_check_agents_health__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_check_agents_health__mutmut['xǁAgentRuntimeǁ_check_agents_health__mutmut_12'] = AgentRuntime.xǁAgentRuntimeǁ_check_agents_health__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_check_agents_health__mutmut['xǁAgentRuntimeǁ_check_agents_health__mutmut_13'] = AgentRuntime.xǁAgentRuntimeǁ_check_agents_health__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_check_agents_health__mutmut['xǁAgentRuntimeǁ_check_agents_health__mutmut_14'] = AgentRuntime.xǁAgentRuntimeǁ_check_agents_health__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_check_agents_health__mutmut['xǁAgentRuntimeǁ_check_agents_health__mutmut_15'] = AgentRuntime.xǁAgentRuntimeǁ_check_agents_health__mutmut_15 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_check_agents_health__mutmut['xǁAgentRuntimeǁ_check_agents_health__mutmut_16'] = AgentRuntime.xǁAgentRuntimeǁ_check_agents_health__mutmut_16 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_check_agents_health__mutmut['xǁAgentRuntimeǁ_check_agents_health__mutmut_17'] = AgentRuntime.xǁAgentRuntimeǁ_check_agents_health__mutmut_17 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_check_agents_health__mutmut['xǁAgentRuntimeǁ_check_agents_health__mutmut_18'] = AgentRuntime.xǁAgentRuntimeǁ_check_agents_health__mutmut_18 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_check_agents_health__mutmut['xǁAgentRuntimeǁ_check_agents_health__mutmut_19'] = AgentRuntime.xǁAgentRuntimeǁ_check_agents_health__mutmut_19 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_check_agents_health__mutmut['xǁAgentRuntimeǁ_check_agents_health__mutmut_20'] = AgentRuntime.xǁAgentRuntimeǁ_check_agents_health__mutmut_20 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_check_agents_health__mutmut['xǁAgentRuntimeǁ_check_agents_health__mutmut_21'] = AgentRuntime.xǁAgentRuntimeǁ_check_agents_health__mutmut_21 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_check_agents_health__mutmut['xǁAgentRuntimeǁ_check_agents_health__mutmut_22'] = AgentRuntime.xǁAgentRuntimeǁ_check_agents_health__mutmut_22 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_check_agents_health__mutmut['xǁAgentRuntimeǁ_check_agents_health__mutmut_23'] = AgentRuntime.xǁAgentRuntimeǁ_check_agents_health__mutmut_23 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_check_agents_health__mutmut['xǁAgentRuntimeǁ_check_agents_health__mutmut_24'] = AgentRuntime.xǁAgentRuntimeǁ_check_agents_health__mutmut_24 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_check_agents_health__mutmut['xǁAgentRuntimeǁ_check_agents_health__mutmut_25'] = AgentRuntime.xǁAgentRuntimeǁ_check_agents_health__mutmut_25 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_check_agents_health__mutmut['xǁAgentRuntimeǁ_check_agents_health__mutmut_26'] = AgentRuntime.xǁAgentRuntimeǁ_check_agents_health__mutmut_26 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_check_agents_health__mutmut['xǁAgentRuntimeǁ_check_agents_health__mutmut_27'] = AgentRuntime.xǁAgentRuntimeǁ_check_agents_health__mutmut_27 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_check_agents_health__mutmut['xǁAgentRuntimeǁ_check_agents_health__mutmut_28'] = AgentRuntime.xǁAgentRuntimeǁ_check_agents_health__mutmut_28 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_check_agents_health__mutmut['xǁAgentRuntimeǁ_check_agents_health__mutmut_29'] = AgentRuntime.xǁAgentRuntimeǁ_check_agents_health__mutmut_29 # type: ignore # mutmut generated

mutants_xǁAgentRuntimeǁregister_hook__mutmut['_mutmut_orig'] = AgentRuntime.xǁAgentRuntimeǁregister_hook__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁregister_hook__mutmut['xǁAgentRuntimeǁregister_hook__mutmut_1'] = AgentRuntime.xǁAgentRuntimeǁregister_hook__mutmut_1 # type: ignore # mutmut generated

mutants_xǁAgentRuntimeǁ_fire_hook__mutmut['_mutmut_orig'] = AgentRuntime.xǁAgentRuntimeǁ_fire_hook__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_fire_hook__mutmut['xǁAgentRuntimeǁ_fire_hook__mutmut_1'] = AgentRuntime.xǁAgentRuntimeǁ_fire_hook__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_fire_hook__mutmut['xǁAgentRuntimeǁ_fire_hook__mutmut_2'] = AgentRuntime.xǁAgentRuntimeǁ_fire_hook__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_fire_hook__mutmut['xǁAgentRuntimeǁ_fire_hook__mutmut_3'] = AgentRuntime.xǁAgentRuntimeǁ_fire_hook__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_fire_hook__mutmut['xǁAgentRuntimeǁ_fire_hook__mutmut_4'] = AgentRuntime.xǁAgentRuntimeǁ_fire_hook__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_fire_hook__mutmut['xǁAgentRuntimeǁ_fire_hook__mutmut_5'] = AgentRuntime.xǁAgentRuntimeǁ_fire_hook__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_fire_hook__mutmut['xǁAgentRuntimeǁ_fire_hook__mutmut_6'] = AgentRuntime.xǁAgentRuntimeǁ_fire_hook__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_fire_hook__mutmut['xǁAgentRuntimeǁ_fire_hook__mutmut_7'] = AgentRuntime.xǁAgentRuntimeǁ_fire_hook__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_fire_hook__mutmut['xǁAgentRuntimeǁ_fire_hook__mutmut_8'] = AgentRuntime.xǁAgentRuntimeǁ_fire_hook__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_fire_hook__mutmut['xǁAgentRuntimeǁ_fire_hook__mutmut_9'] = AgentRuntime.xǁAgentRuntimeǁ_fire_hook__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_fire_hook__mutmut['xǁAgentRuntimeǁ_fire_hook__mutmut_10'] = AgentRuntime.xǁAgentRuntimeǁ_fire_hook__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_fire_hook__mutmut['xǁAgentRuntimeǁ_fire_hook__mutmut_11'] = AgentRuntime.xǁAgentRuntimeǁ_fire_hook__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_fire_hook__mutmut['xǁAgentRuntimeǁ_fire_hook__mutmut_12'] = AgentRuntime.xǁAgentRuntimeǁ_fire_hook__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_fire_hook__mutmut['xǁAgentRuntimeǁ_fire_hook__mutmut_13'] = AgentRuntime.xǁAgentRuntimeǁ_fire_hook__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_fire_hook__mutmut['xǁAgentRuntimeǁ_fire_hook__mutmut_14'] = AgentRuntime.xǁAgentRuntimeǁ_fire_hook__mutmut_14 # type: ignore # mutmut generated

mutants_xǁAgentRuntimeǁget_stats__mutmut['_mutmut_orig'] = AgentRuntime.xǁAgentRuntimeǁget_stats__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁget_stats__mutmut['xǁAgentRuntimeǁget_stats__mutmut_1'] = AgentRuntime.xǁAgentRuntimeǁget_stats__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁget_stats__mutmut['xǁAgentRuntimeǁget_stats__mutmut_2'] = AgentRuntime.xǁAgentRuntimeǁget_stats__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁget_stats__mutmut['xǁAgentRuntimeǁget_stats__mutmut_3'] = AgentRuntime.xǁAgentRuntimeǁget_stats__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁget_stats__mutmut['xǁAgentRuntimeǁget_stats__mutmut_4'] = AgentRuntime.xǁAgentRuntimeǁget_stats__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁget_stats__mutmut['xǁAgentRuntimeǁget_stats__mutmut_5'] = AgentRuntime.xǁAgentRuntimeǁget_stats__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁget_stats__mutmut['xǁAgentRuntimeǁget_stats__mutmut_6'] = AgentRuntime.xǁAgentRuntimeǁget_stats__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁget_stats__mutmut['xǁAgentRuntimeǁget_stats__mutmut_7'] = AgentRuntime.xǁAgentRuntimeǁget_stats__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁget_stats__mutmut['xǁAgentRuntimeǁget_stats__mutmut_8'] = AgentRuntime.xǁAgentRuntimeǁget_stats__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁget_stats__mutmut['xǁAgentRuntimeǁget_stats__mutmut_9'] = AgentRuntime.xǁAgentRuntimeǁget_stats__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁget_stats__mutmut['xǁAgentRuntimeǁget_stats__mutmut_10'] = AgentRuntime.xǁAgentRuntimeǁget_stats__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁget_stats__mutmut['xǁAgentRuntimeǁget_stats__mutmut_11'] = AgentRuntime.xǁAgentRuntimeǁget_stats__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁget_stats__mutmut['xǁAgentRuntimeǁget_stats__mutmut_12'] = AgentRuntime.xǁAgentRuntimeǁget_stats__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁget_stats__mutmut['xǁAgentRuntimeǁget_stats__mutmut_13'] = AgentRuntime.xǁAgentRuntimeǁget_stats__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁget_stats__mutmut['xǁAgentRuntimeǁget_stats__mutmut_14'] = AgentRuntime.xǁAgentRuntimeǁget_stats__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁget_stats__mutmut['xǁAgentRuntimeǁget_stats__mutmut_15'] = AgentRuntime.xǁAgentRuntimeǁget_stats__mutmut_15 # type: ignore # mutmut generated

mutants_xǁAgentRuntimeǁ_agents_by_state__mutmut['_mutmut_orig'] = AgentRuntime.xǁAgentRuntimeǁ_agents_by_state__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_agents_by_state__mutmut['xǁAgentRuntimeǁ_agents_by_state__mutmut_1'] = AgentRuntime.xǁAgentRuntimeǁ_agents_by_state__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_agents_by_state__mutmut['xǁAgentRuntimeǁ_agents_by_state__mutmut_2'] = AgentRuntime.xǁAgentRuntimeǁ_agents_by_state__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_agents_by_state__mutmut['xǁAgentRuntimeǁ_agents_by_state__mutmut_3'] = AgentRuntime.xǁAgentRuntimeǁ_agents_by_state__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_agents_by_state__mutmut['xǁAgentRuntimeǁ_agents_by_state__mutmut_4'] = AgentRuntime.xǁAgentRuntimeǁ_agents_by_state__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_agents_by_state__mutmut['xǁAgentRuntimeǁ_agents_by_state__mutmut_5'] = AgentRuntime.xǁAgentRuntimeǁ_agents_by_state__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁ_agents_by_state__mutmut['xǁAgentRuntimeǁ_agents_by_state__mutmut_6'] = AgentRuntime.xǁAgentRuntimeǁ_agents_by_state__mutmut_6 # type: ignore # mutmut generated

mutants_xǁAgentRuntimeǁshutdown__mutmut['_mutmut_orig'] = AgentRuntime.xǁAgentRuntimeǁshutdown__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁshutdown__mutmut['xǁAgentRuntimeǁshutdown__mutmut_1'] = AgentRuntime.xǁAgentRuntimeǁshutdown__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁshutdown__mutmut['xǁAgentRuntimeǁshutdown__mutmut_2'] = AgentRuntime.xǁAgentRuntimeǁshutdown__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁshutdown__mutmut['xǁAgentRuntimeǁshutdown__mutmut_3'] = AgentRuntime.xǁAgentRuntimeǁshutdown__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁshutdown__mutmut['xǁAgentRuntimeǁshutdown__mutmut_4'] = AgentRuntime.xǁAgentRuntimeǁshutdown__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁshutdown__mutmut['xǁAgentRuntimeǁshutdown__mutmut_5'] = AgentRuntime.xǁAgentRuntimeǁshutdown__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁshutdown__mutmut['xǁAgentRuntimeǁshutdown__mutmut_6'] = AgentRuntime.xǁAgentRuntimeǁshutdown__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁshutdown__mutmut['xǁAgentRuntimeǁshutdown__mutmut_7'] = AgentRuntime.xǁAgentRuntimeǁshutdown__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁshutdown__mutmut['xǁAgentRuntimeǁshutdown__mutmut_8'] = AgentRuntime.xǁAgentRuntimeǁshutdown__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁshutdown__mutmut['xǁAgentRuntimeǁshutdown__mutmut_9'] = AgentRuntime.xǁAgentRuntimeǁshutdown__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAgentRuntimeǁshutdown__mutmut['xǁAgentRuntimeǁshutdown__mutmut_10'] = AgentRuntime.xǁAgentRuntimeǁshutdown__mutmut_10 # type: ignore # mutmut generated
