"""Agent Tool Registry — Tool integration for agents.

Provides a registry of tools that agents can invoke during execution.
Each tool is a callable with metadata describing its inputs, outputs,
and required capabilities. Integrates with the connector SDK and
the existing Zenic-Flijo tool ecosystem.
"""

from __future__ import annotations

import threading
import time
import uuid
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any

from src.utils.logger import get_logger

logger = get_logger("agent.tools")


@dataclass
class AgentTool:
    """A tool that an agent can invoke.

    Attributes:
        tool_id: Unique tool identifier.
        name: Human-readable tool name.
        description: What the tool does.
        handler: The callable to execute.
        parameters: JSON Schema describing expected parameters.
        required_capabilities: Agent capabilities required to use this tool.
        timeout_seconds: Execution timeout.
        dangerous: Whether this tool can cause side effects.
        usage_count: Number of times the tool has been invoked.
    """

    tool_id: str = ""
    name: str = ""
    description: str = ""
    handler: Callable[..., Any] | None = None
    parameters: dict[str, Any] = field(default_factory=dict)
    required_capabilities: list[str] = field(default_factory=list)
    timeout_seconds: float = 30.0
    dangerous: bool = False
    usage_count: int = 0
    last_used: float = 0.0

    def __post_init__(self) -> None:
        if not self.tool_id:
            self.tool_id = f"tool-{uuid.uuid4().hex[:8]}"


@dataclass
class ToolInvocation:
    """Record of a tool invocation by an agent."""

    invocation_id: str = ""
    agent_id: str = ""
    tool_id: str = ""
    parameters: dict[str, Any] = field(default_factory=dict)
    result: Any = None
    error: str | None = None
    started_at: float = 0.0
    completed_at: float = 0.0
    duration_ms: float = 0.0

    def __post_init__(self) -> None:
        if not self.invocation_id:
            self.invocation_id = f"inv-{uuid.uuid4().hex[:8]}"


class AgentToolRegistry:
    """Registry of tools available to agents.

    Provides registration, discovery, and invocation of tools with
    capability-based access control and execution tracking.

    Usage:
        registry = AgentToolRegistry.get_instance()
        registry.register(AgentTool(name="web_search", handler=search_fn, ...))
        result = registry.invoke("agent-1", "web_search", {"query": "invoices"})
    """

    _instance: AgentToolRegistry | None = None
    _lock = threading.Lock()

    def __init__(self) -> None:
        self._tools: dict[str, AgentTool] = {}
        self._invocations: list[ToolInvocation] = []
        self._tool_lock = threading.Lock()
        self._max_invocation_history = 1000

    @classmethod
    def get_instance(cls) -> AgentToolRegistry:
        """Get or create the singleton registry."""
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = cls()
        return cls._instance

    @classmethod
    def reset_instance(cls) -> None:
        """Reset singleton for testing."""
        with cls._lock:
            cls._instance = None

    # ── Registration ────────────────────────────────────────

    def register(self, tool: AgentTool) -> str:
        """Register a tool in the registry.

        Returns:
            The tool_id of the registered tool.
        """
        with self._tool_lock:
            self._tools[tool.tool_id] = tool
            # Also index by name for lookup
            self._tools[tool.name] = tool
        logger.info("Tool registered: %s (%s)", tool.name, tool.tool_id)
        return tool.tool_id

    def unregister(self, tool_id_or_name: str) -> bool:
        """Unregister a tool by ID or name."""
        with self._tool_lock:
            tool = self._tools.pop(tool_id_or_name, None)
            if tool is not None:
                # Remove both ID and name entries
                self._tools.pop(tool.tool_id, None)
                self._tools.pop(tool.name, None)
                return True
            return False

    def register_builtin_tools(self) -> None:
        """Register the built-in Zenic-Flijo tools for agent use.

        These wrap the existing platform capabilities as agent-callable tools.
        """
        builtin_tools = [
            AgentTool(
                name="workflow.execute",
                description="Execute a workflow by ID with optional input data",
                handler=self._tool_workflow_execute,
                parameters={
                    "type": "object",
                    "properties": {
                        "workflow_id": {"type": "string", "description": "Workflow definition ID"},
                        "input_data": {"type": "object", "description": "Optional input data"},
                    },
                    "required": ["workflow_id"],
                },
                required_capabilities=["workflow_orchestration"],
            ),
            AgentTool(
                name="nlu.process",
                description="Process natural language input through the NLU pipeline",
                handler=self._tool_nlu_process,
                parameters={
                    "type": "object",
                    "properties": {
                        "text": {"type": "string", "description": "Natural language input"},
                        "language": {"type": "string", "enum": ["es", "en", "auto"]},
                    },
                    "required": ["text"],
                },
                required_capabilities=["nlu_processing"],
            ),
            AgentTool(
                name="connector.call",
                description="Invoke a registered connector action",
                handler=self._tool_connector_call,
                parameters={
                    "type": "object",
                    "properties": {
                        "connector_name": {"type": "string"},
                        "action": {"type": "string"},
                        "params": {"type": "object"},
                    },
                    "required": ["connector_name", "action"],
                },
                required_capabilities=["api_calls", "tool_use"],
                dangerous=True,
            ),
            AgentTool(
                name="data.query",
                description="Query data from the platform database",
                handler=self._tool_data_query,
                parameters={
                    "type": "object",
                    "properties": {
                        "table": {"type": "string"},
                        "filters": {"type": "object"},
                        "limit": {"type": "integer"},
                    },
                    "required": ["table"],
                },
                required_capabilities=["data_analysis"],
            ),
            AgentTool(
                name="code.execute",
                description="Execute Python code in a sandboxed environment",
                handler=self._tool_code_execute,
                parameters={
                    "type": "object",
                    "properties": {
                        "code": {"type": "string", "description": "Python code to execute"},
                        "timeout": {"type": "integer", "description": "Timeout in seconds"},
                    },
                    "required": ["code"],
                },
                required_capabilities=["code_generation"],
                dangerous=True,
                timeout_seconds=60.0,
            ),
            AgentTool(
                name="file.read",
                description="Read a file from the workspace",
                handler=self._tool_file_read,
                parameters={
                    "type": "object",
                    "properties": {
                        "path": {"type": "string", "description": "File path"},
                    },
                    "required": ["path"],
                },
                required_capabilities=["file_operations"],
            ),
            AgentTool(
                name="file.write",
                description="Write content to a file in the workspace",
                handler=self._tool_file_write,
                parameters={
                    "type": "object",
                    "properties": {
                        "path": {"type": "string"},
                        "content": {"type": "string"},
                    },
                    "required": ["path", "content"],
                },
                required_capabilities=["file_operations"],
                dangerous=True,
            ),
            AgentTool(
                name="web.search",
                description="Search the web for information",
                handler=self._tool_web_search,
                parameters={
                    "type": "object",
                    "properties": {
                        "query": {"type": "string"},
                        "num_results": {"type": "integer"},
                    },
                    "required": ["query"],
                },
                required_capabilities=["api_calls"],
            ),
        ]

        for tool in builtin_tools:
            self.register(tool)

    # ── Invocation ──────────────────────────────────────────

    def invoke(
        self,
        agent_id: str,
        tool_id_or_name: str,
        parameters: dict[str, Any] | None = None,
    ) -> ToolInvocation:
        """Invoke a tool on behalf of an agent.

        Args:
            agent_id: The agent requesting the invocation.
            tool_id_or_name: Tool ID or name to invoke.
            parameters: Parameters to pass to the tool handler.

        Returns:
            A ToolInvocation record with the result or error.
        """
        invocation = ToolInvocation(
            agent_id=agent_id,
            tool_id=tool_id_or_name,
            parameters=parameters or {},
            started_at=time.time(),
        )

        with self._tool_lock:
            tool = self._tools.get(tool_id_or_name)

        if tool is None:
            invocation.error = f"Tool not found: {tool_id_or_name}"
            invocation.completed_at = time.time()
            invocation.duration_ms = (invocation.completed_at - invocation.started_at) * 1000
            self._record_invocation(invocation)
            return invocation

        if tool.handler is None:
            invocation.error = f"Tool has no handler: {tool_id_or_name}"
            invocation.completed_at = time.time()
            invocation.duration_ms = (invocation.completed_at - invocation.started_at) * 1000
            self._record_invocation(invocation)
            return invocation

        try:
            result = tool.handler(parameters or {})
            invocation.result = result
        except Exception as exc:
            invocation.error = str(exc)
            logger.error("Tool %s invocation failed: %s", tool_id_or_name, exc)
        finally:
            invocation.completed_at = time.time()
            invocation.duration_ms = (invocation.completed_at - invocation.started_at) * 1000
            tool.usage_count += 1
            tool.last_used = invocation.completed_at
            self._record_invocation(invocation)

        return invocation

    def _record_invocation(self, invocation: ToolInvocation) -> None:
        """Record an invocation for auditing and analytics."""
        self._invocations.append(invocation)
        if len(self._invocations) > self._max_invocation_history:
            self._invocations = self._invocations[-self._max_invocation_history:]

    # ── Discovery ───────────────────────────────────────────

    def list_tools(
        self,
        capability: str | None = None,
        dangerous: bool | None = None,
    ) -> list[AgentTool]:
        """List available tools, optionally filtered."""
        with self._tool_lock:
            # Deduplicate by tool_id (since we index by name too)
            seen_ids: set[str] = set()
            tools = []
            for tool in self._tools.values():
                if tool.tool_id in seen_ids:
                    continue
                seen_ids.add(tool.tool_id)
                if capability and capability not in tool.required_capabilities:
                    continue
                if dangerous is not None and tool.dangerous != dangerous:
                    continue
                tools.append(tool)
            return tools

    def get_tool(self, tool_id_or_name: str) -> AgentTool | None:
        """Get a tool by ID or name."""
        with self._tool_lock:
            return self._tools.get(tool_id_or_name)

    # ── Builtin Tool Handlers (implementaciones reales — fix Sprint 2 bug #18) ──
    # Antes estos handlers eran stubs que retornaban {"status": "dispatched"}
    # sin invocar los servicios reales. Ahora llaman a WorkflowEngine,
    # NLUPipeline, ConnectorRegistry y DatabaseManager respectivamente.

    def _tool_workflow_execute(self, params: dict[str, Any]) -> dict[str, Any]:
        """Execute a workflow via the WorkflowEngine.

        Fix Sprint 2 bug #18: ahora invoca WorkflowEngine.execute() real.
        """
        workflow_id = params.get("workflow_id")
        trigger_data = params.get("trigger_data") or {}

        if not workflow_id:
            return {"status": "error", "error": "workflow_id required"}

        try:
            from src.workflow.engine import WorkflowEngine
            engine = WorkflowEngine()
            result = engine.execute(int(workflow_id), trigger_data=trigger_data)
            return {
                "status": result.status,
                "execution_id": result.execution_id,
                "workflow_id": result.workflow_id,
                "duration_ms": result.duration_ms,
                "step_count": len(result.step_results),
                "error": result.error_message,
                "orbital_resonance": getattr(result, "orbital_resonance", 0.0),
            }
        except ValueError as e:
            return {"status": "error", "error": f"Invalid workflow_id: {e}"}
        except Exception as e:
            return {"status": "error", "error": f"Workflow execution failed: {e}"}

    def _tool_nlu_process(self, params: dict[str, Any]) -> dict[str, Any]:
        """Process text through the NLU pipeline.

        Fix Sprint 2 bug #18: ahora invoca NLUPipeline.understand() real.
        """
        text = params.get("text", "")
        language = params.get("language", "auto")

        if not text:
            return {"status": "error", "error": "text required"}

        try:
            from src.nlu.pipeline import NLUPipeline
            pipeline = NLUPipeline()
            result = pipeline.understand(text, language=language)
            return {
                "status": "processed",
                "input": text,
                "language": language,
                "intent": getattr(result, "intent", "unknown"),
                "entities": getattr(result, "entities", []),
                "confidence": getattr(result, "confidence", 0.0),
            }
        except ImportError:
            return {
                "status": "error",
                "error": "NLUPipeline not available",
                "input": text,
            }
        except Exception as e:
            return {
                "status": "error",
                "error": f"NLU processing failed: {e}",
                "input": text,
            }

    def _tool_connector_call(self, params: dict[str, Any]) -> dict[str, Any]:
        """Call a connector action via ConnectorRegistry.

        Fix Sprint 2 bug #18: ahora invoca ConnectorRegistry.get(name).execute() real.
        """
        connector_name = params.get("connector_name")
        action = params.get("action")
        call_params = params.get("params") or {}

        if not connector_name or not action:
            return {"status": "error", "error": "connector_name and action required"}

        try:
            from src.sdk.registry import ConnectorRegistry
            registry = ConnectorRegistry()
            connector_cls = registry.get(connector_name)
            if connector_cls is None:
                return {"status": "error", "error": f"Connector '{connector_name}' not registered"}

            # Instanciar y ejecutar (safe_execute aplica circuit breaker + rate limit)
            connector = connector_cls()
            if hasattr(connector, "safe_execute"):
                result = connector.safe_execute(action, call_params)
            else:
                result = connector.execute(action, call_params)
            return {
                "status": "success",
                "connector": connector_name,
                "action": action,
                "result": result,
            }
        except Exception as e:
            return {
                "status": "error",
                "connector": connector_name,
                "action": action,
                "error": f"Connector call failed: {e}",
            }

    def _tool_data_query(self, params: dict[str, Any]) -> dict[str, Any]:
        """Query data from the SQLite database.

        Fix Sprint 2 bug #18: ahora ejecuta queries reales via DatabaseManager.
        Solo permite SELECT (no DML/DDL) por seguridad.
        """
        sql = params.get("sql", "").strip()
        query_params = params.get("params") or []
        limit = min(int(params.get("limit", 100)), 1000)  # cap en 1000 rows

        if not sql:
            return {"status": "error", "error": "sql required"}

        # Seguridad: solo SELECT permitido
        sql_upper = sql.upper().lstrip()
        if not sql_upper.startswith("SELECT") and not sql_upper.startswith("WITH"):
            return {
                "status": "error",
                "error": "Only SELECT/WITH queries allowed via data.query tool",
            }

        # Añadir LIMIT si no tiene
        if "LIMIT" not in sql_upper:
            sql = f"{sql.rstrip(';')} LIMIT {limit}"

        try:
            from src.data.database_manager import DatabaseManager
            db = DatabaseManager()
            rows = db.fetchall(sql, tuple(query_params) if query_params else ())
            return {
                "status": "success",
                "rows": rows if rows else [],
                "row_count": len(rows) if rows else 0,
                "truncated": bool(rows) and len(rows) >= limit,
            }
        except Exception as e:
            return {
                "status": "error",
                "error": f"Query failed: {e}",
                "sql": sql,
            }

    def _tool_code_execute(self, params: dict[str, Any]) -> dict[str, Any]:
        """Execute code in sandbox.

        Fix Sprint 2 bug #18: ahora invoca CodeSandbox real.
        """
        code = params.get("code", "")
        timeout = min(int(params.get("timeout", 10)), 30)  # cap en 30s

        if not code:
            return {"status": "error", "error": "code required"}

        try:
            from src.tools.code_runner.sandbox import CodeSandbox
            sandbox = CodeSandbox()
            result = sandbox.execute(code, timeout=timeout)
            return {
                "status": "success" if result.get("success") else "error",
                "output": result.get("output", ""),
                "error": result.get("error"),
                "stdout": result.get("stdout", ""),
                "stderr": result.get("stderr", ""),
                "duration_ms": result.get("duration_ms", 0),
            }
        except ImportError:
            return {
                "status": "error",
                "error": "CodeSandbox not available",
            }
        except Exception as e:
            return {
                "status": "error",
                "error": f"Code execution failed: {e}",
            }

    def _tool_file_read(self, params: dict[str, Any]) -> dict[str, Any]:
        """Read a file from the workspace.

        Fix NEW-BUG-5 (verificación Sprint 4): antes era stub. Ahora lee
        archivos reales con sandboxing (solo dentro de WORKSPACE_DIR).
        """
        path_str = params.get("path", "")
        if not path_str:
            return {"status": "error", "error": "path required"}

        try:
            from pathlib import Path
            from src.config import DATA_DIR

            # Sandboxing: solo permitir lectura dentro de DATA_DIR/workspace/
            workspace = Path(DATA_DIR) / "workspace"
            workspace.mkdir(parents=True, exist_ok=True)

            target = (workspace / path_str).resolve()
            # Prevenir path traversal: el target debe estar dentro de workspace
            if not str(target).startswith(str(workspace.resolve())):
                return {
                    "status": "error",
                    "error": f"Path fuera del workspace permitido: {path_str}",
                }

            if not target.exists() or not target.is_file():
                return {"status": "error", "error": f"Archivo no encontrado: {path_str}"}

            # Límite de tamaño: 1MB para evitar OOM
            size = target.stat().st_size
            if size > 1024 * 1024:
                return {"status": "error", "error": f"Archivo demasiado grande ({size} bytes, máx 1MB)"}

            content = target.read_text(encoding="utf-8", errors="replace")
            return {
                "status": "success",
                "path": path_str,
                "content": content,
                "size": size,
            }
        except Exception as e:
            return {"status": "error", "error": f"File read failed: {e}", "path": path_str}

    def _tool_file_write(self, params: dict[str, Any]) -> dict[str, Any]:
        """Write content to a file in the workspace.

        Fix NEW-BUG-5: ahora escribe archivos reales con sandboxing.
        """
        path_str = params.get("path", "")
        content = params.get("content", "")
        if not path_str:
            return {"status": "error", "error": "path required"}

        try:
            from pathlib import Path
            from src.config import DATA_DIR

            workspace = Path(DATA_DIR) / "workspace"
            workspace.mkdir(parents=True, exist_ok=True)

            target = (workspace / path_str).resolve()
            # Prevenir path traversal
            if not str(target).startswith(str(workspace.resolve())):
                return {
                    "status": "error",
                    "error": f"Path fuera del workspace permitido: {path_str}",
                }

            # Crear directorios padre si no existen
            target.parent.mkdir(parents=True, exist_ok=True)

            # Límite de tamaño: 1MB
            if len(content) > 1024 * 1024:
                return {"status": "error", "error": "Contenido demasiado grande (máx 1MB)"}

            target.write_text(content, encoding="utf-8")
            return {
                "status": "success",
                "path": path_str,
                "bytes_written": len(content.encode("utf-8")),
            }
        except Exception as e:
            return {"status": "error", "error": f"File write failed: {e}", "path": path_str}

    def _tool_web_search(self, params: dict[str, Any]) -> dict[str, Any]:
        """Search the web for information.

        Fix NEW-BUG-5: ahora usa urllib para búsqueda real (limitado a
        búsquedas HTTP GET simples; para búsqueda con API real, integrar
        con z-ai-web-dev-sdk web_search function).
        """
        query = params.get("query", "")
        num_results = min(int(params.get("num_results", 5)), 20)

        if not query:
            return {"status": "error", "error": "query required"}

        try:
            # Intentar usar z-ai-web-dev-sdk si está disponible (mejor opción)
            try:
                import json as _json
                import subprocess as _sp
                result = _sp.run(
                    ["z-ai", "function", "-n", "web_search",
                     "-a", _json.dumps({"query": query, "num": num_results})],
                    capture_output=True, text=True, timeout=30,
                )
                if result.returncode == 0 and result.stdout.strip():
                    return {
                        "status": "success",
                        "query": query,
                        "results": _json.loads(result.stdout),
                    }
            except (FileNotFoundError, _sp.TimeoutExpired):
                pass  # z-ai CLI no disponible, fallback abajo

            # Fallback: not implemented en este entorno
            return {
                "status": "error",
                "error": "Web search no disponible — instala z-ai-web-dev-sdk o integra con API de búsqueda",
                "query": query,
            }
        except Exception as e:
            return {"status": "error", "error": f"Web search failed: {e}", "query": query}

    # ── Stats ───────────────────────────────────────────────

    def get_stats(self) -> dict[str, Any]:
        """Get registry statistics."""
        with self._tool_lock:
            total_invocations = len(self._invocations)
            error_count = sum(1 for inv in self._invocations if inv.error)
            total_duration = sum(inv.duration_ms for inv in self._invocations)

        return {
            "total_tools": len(self.list_tools()),
            "total_invocations": total_invocations,
            "error_count": error_count,
            "avg_duration_ms": total_duration / max(total_invocations, 1),
            "tools_by_capability": self._tools_by_capability(),
        }

    def _tools_by_capability(self) -> dict[str, int]:
        """Count tools by required capability."""
        counts: dict[str, int] = {}
        for tool in self.list_tools():
            for cap in tool.required_capabilities:
                counts[cap] = counts.get(cap, 0) + 1
        return counts
