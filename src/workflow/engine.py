"""
ORBITAL — WorkflowEngine Orbital (Motor Unico — OVC Compartido)
================================================================

WorkflowEngine con retroalimentacion circular usando OVC compartido via OrbitalContext.

NOTA: Este archivo es el entry point delgado (~250 líneas).
La lógica de ejecución de pasos, subworkflows, parallel/fork,
async, y orbital está en src/workflow/execution/ y src/workflow/orbital/.
"""

from __future__ import annotations

import threading
import time

from src.orbital.context import OrbitalContext
from src.orbital.models import DEFAULT_THRESHOLD, RETROFEEDBACK_DAMPING
from src.utils.logger import setup_logging
from src.workflow.branch_handler import BranchHandler
from src.workflow.condition_evaluator import ConditionEvaluator
from src.workflow.execution.async_executor import AsyncExecutionService
from src.workflow.execution.result import ExecutionResult
from src.workflow.execution.step_execution import StepExecutionService
from src.workflow.loop_handler import LoopHandler
from src.workflow.orbital.steps import inject_steps_as_orbital
from src.workflow.orbital.trigger import inject_trigger_as_orbital
from src.workflow.repository import WorkflowDefinition, WorkflowRepository
from src.workflow.step_executor import StepExecutor

logger = setup_logging(__name__)


class WorkflowEngine:
    """
    Motor de Workflows Orbital — Motor unico con OVC compartido via OrbitalContext.

    Singleton como el original. Delega la lógica de ejecución de pasos,
    subworkflows, parallel/fork, async y orbital a servicios especializados.
    """

    _instance: WorkflowEngine | None = None
    _lock = threading.RLock()

    def __new__(cls) -> WorkflowEngine:
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if hasattr(self, "_initialized") and self._initialized:
            return
        with self._lock:
            if hasattr(self, "_initialized") and self._initialized:
                return
            self._initialized = True
            self._repository = WorkflowRepository()
            self._step_executor = StepExecutor()
            self._condition_evaluator = ConditionEvaluator()
            self._branch_handler = BranchHandler()
            self._loop_handler = LoopHandler()
            from src.workflow.error_handler import ErrorHandler
            self._error_handler = ErrorHandler()
            from src.workflow.execution.parallel import ForkHandler, JoinHandler
            self._fork_handler = ForkHandler(self._step_executor)
            self._join_handler = JoinHandler()
            self._tools: dict[str, object] = {}
            # ── ORBITAL COMPARTIDO ───────────────────
            self._ctx = OrbitalContext()
            self._orbital_results: list = []

            # ── SERVICIOS ESPECIALIZADOS ─────────────
            self._step_execution_service = StepExecutionService(
                branch_handler=self._branch_handler,
                loop_handler=self._loop_handler,
                fork_handler=self._fork_handler,
                join_handler=self._join_handler,
                step_executor=self._step_executor,
                condition_evaluator=self._condition_evaluator,
                error_handler=self._error_handler,
                repository=self._repository,
                orbital_engine=self._ctx.engine,
                ctx=self._ctx,
            )
            self._async_service = AsyncExecutionService(repository=self._repository)

    # ── Registro de herramientas ────────────────────────────

    def register_tool(self, tool_name: str, tool_instance: object) -> None:
        """Registra una herramienta de negocio en el motor."""
        self._tools[tool_name] = tool_instance
        self._step_executor.register_tool(tool_name, tool_instance)
        logger.info(f"Tool registrada: {tool_name}")

    def get_registered_tools(self) -> list[str]:
        """Retorna la lista de herramientas registradas."""
        return list(self._tools.keys())

    # ── Ejecucion ORBITAL ───────────────────────────────────

    def execute(self, workflow_id: int, trigger_data: dict | None = None) -> ExecutionResult:
        """Ejecuta un workflow completo en modo orbital (OVC compartido)."""
        start_time = time.time()

        # 1. Cargar definicion
        definition = self._repository.get(workflow_id)
        if not definition:
            raise ValueError(f"Workflow no encontrado: {workflow_id}")
        if definition.status != "active":
            raise ValueError(f"Workflow '{definition.name}' no esta activo (estado: {definition.status})")

        logger.info(f"OrbitalWorkflowEngine: Ejecutando workflow '{definition.name}' (ID: {workflow_id})")

        # 2-4. Crear ejecucion y preparar contexto
        execution = self._repository.create_execution(workflow_id, trigger_data)
        orbital_engine = self._ctx.engine
        continue_on_error = False
        context = {
            "input": trigger_data or {},
            "workflow": {"id": definition.id, "name": definition.name, "continue_on_error": continue_on_error},
            "output": {},
            "steps_output": {},
            "settings": self._load_settings(),
            "_execution_id": execution.id,
        }

        # 5-6. Inyectar trigger y pasos como variables orbitales
        if trigger_data:
            inject_trigger_as_orbital(trigger_data, self._ctx.ovc)
        inject_steps_as_orbital(definition.steps, self._ctx.ovc)

        # 7. Ejecutar pasos
        step_results = []
        final_status = "completed"
        error_message = None

        try:
            for step in definition.steps:
                step_result = self._step_execution_service.execute_step(step, context)
                step_results.append({
                    "step_id": step.get("id"), "tool": step.get("tool"), "action": step.get("action"),
                    "status": step_result.status, "output": step_result.output_data,
                    "duration_ms": step_result.duration_ms, "error": step_result.error_message,
                    "orbital_theta": getattr(step_result, "orbital_theta", 0.0),
                    "orbital_tension": getattr(step_result, "orbital_tension", 0.0),
                })
                step_id = str(step.get("id", 0))
                context["steps_output"][step_id] = step_result.output_data
                self._repository.save_step_log(
                    execution_id=execution.id, step_id=step.get("id", 0),
                    tool=step.get("tool", ""), action=step.get("action", ""),
                    input_data=step.get("params", {}), output_data=step_result.output_data,
                    status=step_result.status, duration_ms=step_result.duration_ms,
                    error_message=step_result.error_message,
                )
                if step_result.status == "failed":
                    error_message = step_result.error_message
                    logger.error(f"Workflow {workflow_id} fallo en paso {step.get('id')}: {error_message}")
                    if not continue_on_error:
                        final_status = "failed"
                        break
                    logger.info(f"continue_on_error=True: continuando despues de paso {step.get('id')}")
                if step_result.status == "skipped" and step_result.output_data.get("reason") == "continue_on_error":
                    logger.info(f"Paso {step.get('id')} skipped (continue_on_error)")
        except Exception as e:
            final_status = "failed"
            error_message = str(e)
            logger.error(f"Workflow {workflow_id} fallo con excepcion: {e}")

        # 8. Tick orbital
        orbital_espectro = None
        orbital_resonance = 0.0
        try:
            step_var_names = list(self._ctx.ovc.get_variable_names())
            if len(step_var_names) >= 2:
                orbital_engine.create_cycle("workflow_cycle", step_var_names[:10], threshold=DEFAULT_THRESHOLD)
            orbital_result = orbital_engine.run_tick(dt=1.0, retrofeed_damping=RETROFEEDBACK_DAMPING)
            self._orbital_results.append(orbital_result)
            if orbital_result.espectro:
                orbital_espectro = orbital_result.espectro.to_dict()
            if orbital_result.rcc_results:
                orbital_resonance = sum(r.resonance_strength for r in orbital_result.rcc_results) / len(orbital_result.rcc_results)
            logger.info(f"OrbitalWorkflowEngine: Workflow {workflow_id} completado — "
                        f"TOR={len(orbital_result.tor_results)} RCC={len(orbital_result.rcc_results)} "
                        f"Espectro={len(orbital_result.espectro.modes) if orbital_result.espectro else 0} modos "
                        f"Resonancia={orbital_resonance:.4f}")
        except Exception as e:
            logger.warning(f"OrbitalWorkflowEngine: Error orbital (no bloqueante): {e}")

        # 9-10. Finalizar y emitir evento
        duration = int((time.time() - start_time) * 1000)
        self._repository.complete_execution(execution.id, duration, error_message)
        self._emit_completion_event(definition, final_status, execution.id, duration)
        logger.info(f"Workflow {workflow_id} {final_status} en {duration}ms")

        return ExecutionResult(
            execution_id=execution.id, workflow_id=workflow_id, status=final_status,
            duration_ms=duration, step_results=step_results, error_message=error_message,
            orbital_espectro=orbital_espectro, orbital_variables=self._ctx.ovc.variable_count,
            orbital_resonance=orbital_resonance,
        )

    def _execute_step(self, step: dict, context: dict, orbital_engine=None) -> object:
        """Wrapper backward-compatible que delega al StepExecutionService."""
        return self._step_execution_service.execute_step(step, context)

    # ── Gestion de ciclo de vida ────────────────────────────

    def pause(self, workflow_id: int) -> bool:
        definition = self._repository.get(workflow_id)
        if not definition:
            return False
        self._repository.update(workflow_id, {"status": "paused"})
        self._remove_subscriptions(workflow_id)
        logger.info(f"Workflow {workflow_id} pausado")
        return True

    def resume(self, workflow_id: int) -> bool:
        definition = self._repository.get(workflow_id)
        if not definition:
            return False
        self._repository.update(workflow_id, {"status": "active"})
        self._restore_subscriptions(definition)
        logger.info(f"Workflow {workflow_id} reanudado")
        return True

    def archive(self, workflow_id: int) -> bool:
        definition = self._repository.get(workflow_id)
        if not definition:
            return False
        self._repository.update(workflow_id, {"status": "archived"})
        self._remove_subscriptions(workflow_id)
        logger.info(f"Workflow {workflow_id} archivado")
        return True

    def get_status(self, workflow_id: int) -> dict:
        definition = self._repository.get(workflow_id)
        if not definition:
            return {"error": "Workflow no encontrado"}
        executions = self._repository.list_executions(workflow_id, limit=1)
        last_execution = executions[0].to_dict() if executions else None
        status = {
            "workflow": definition.to_dict(), "last_execution": last_execution,
            "is_active": definition.status == "active", "is_paused": definition.status == "paused",
            "orbital_mode": True, "shared_context": True,
        }
        if self._orbital_results:
            status["orbital_espectro"] = self._orbital_results[-1].espectro.to_dict()
        return status

    # ── Helpers ─────────────────────────────────────────────

    def _load_settings(self) -> dict:
        from src.data.database_manager import DatabaseManager
        db = DatabaseManager()
        rows = db.fetchall("SELECT key, value FROM settings")
        return {row["key"]: row["value"] for row in rows}

    def _emit_completion_event(self, definition: WorkflowDefinition, status: str, execution_id: int, duration_ms: int) -> None:
        from src.events.bus import EventBus
        event_bus = EventBus()
        event_type = "workflow.completed" if status == "completed" else "workflow.failed"
        event_bus.publish(event_type, {
            "workflow_id": definition.id, "execution_id": execution_id,
            "duration_ms": duration_ms, "status": status,
        })

    def _remove_subscriptions(self, workflow_id: int) -> None:
        from src.events.bus import EventBus
        EventBus().unsubscribe_all(workflow_id)

    def _restore_subscriptions(self, definition: WorkflowDefinition) -> None:
        from src.events.bus import EventBus
        event_bus = EventBus()
        if definition.trigger_type == "event":
            event_config = definition.trigger_config
            event_type = event_config.get("event", "")
            if event_type:
                event_bus.subscribe(event_type, definition.id)

    # ── Consultas orbitales ─────────────────────────────────

    def get_orbital_results(self, limit: int = 10) -> list[dict]:
        return [r.to_dict() for r in self._orbital_results[-limit:]]

    def get_orbital_snapshot(self) -> dict:
        return {
            "orbital_mode": True, "shared_context": True,
            "ovc_variables": self._ctx.ovc.variable_count,
            "orbital_results_count": len(self._orbital_results),
            "tools_registered": self.get_registered_tools(),
        }

    def orbital_report(self) -> str:
        lines = ["=" * 60]
        lines.append("ORBITAL WORKFLOW ENGINE — Reporte (OVC Compartido)")
        lines.append("=" * 60)
        lines.append("  Modo: ORBITAL (OVC compartido)")
        lines.append(f"  OVC variables: {self._ctx.ovc.variable_count}")
        lines.append(f"  Tools registradas: {len(self.get_registered_tools())}")
        lines.append(f"  Ejecuciones orbitales: {len(self._orbital_results)}")
        if self._orbital_results:
            last = self._orbital_results[-1]
            lines.append(f"  Ultimo tick: {last.tick}")
            lines.append(f"  Variables orbitales: {len(last.variables)}")
            lines.append(f"  TOR pairs: {len(last.tor_results)}")
            lines.append(f"  RCC resultados: {len(last.rcc_results)}")
        lines.append("=" * 60)
        return "\n".join(lines)

    # ── Ejecucion Asincrona ─────────────────────────────────

    def execute_async(self, workflow_id: int, trigger_data: dict | None = None, priority: int = 0) -> dict:
        """Encola un workflow para ejecucion asincrona via WorkQueue."""
        return self._async_service.execute(workflow_id, trigger_data, priority)

    # ── Reset para testing ──────────────────────────────────

    @classmethod
    def _reset(cls) -> None:
        """Reinicia el singleton (para tests)."""
        cls._instance = None
