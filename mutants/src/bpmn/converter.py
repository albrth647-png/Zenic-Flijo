"""BPMN to Workflow converter — converts BPMN processes to Zenic-Flijo workflows.

Extracted from src/bpmn/__init__.py.
"""

from __future__ import annotations

from typing import Any

from src.bpmn.models import BPMNElementType, BPMNProcess


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁBPMNToWorkflowConverterǁ_get_task_type_map__mutmut: MutantDict = {}  # type: ignore
mutants_xǁBPMNToWorkflowConverterǁconvert__mutmut: MutantDict = {}  # type: ignore
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut: MutantDict = {}  # type: ignore
mutants_xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut: MutantDict = {}  # type: ignore
mutants_xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut: MutantDict = {}  # type: ignore


class BPMNToWorkflowConverter:
    """Convert BPMN process definitions to Zenic-Flijo workflow definitions."""

    TASK_TYPE_MAP: dict[BPMNElementType, str] | None = None

    @_mutmut_mutated(mutants_xǁBPMNToWorkflowConverterǁ_get_task_type_map__mutmut)
    def _get_task_type_map(self) -> dict[BPMNElementType, str]:
        if self.TASK_TYPE_MAP is None:
            self.TASK_TYPE_MAP = {
                BPMNElementType.USER_TASK: "input",
                BPMNElementType.SERVICE_TASK: "api_call",
                BPMNElementType.SCRIPT_TASK: "code_runner",
                BPMNElementType.MANUAL_TASK: "notification",
            }
        return self.TASK_TYPE_MAP

    def xǁBPMNToWorkflowConverterǁ_get_task_type_map__mutmut_orig(self) -> dict[BPMNElementType, str]:
        if self.TASK_TYPE_MAP is None:
            self.TASK_TYPE_MAP = {
                BPMNElementType.USER_TASK: "input",
                BPMNElementType.SERVICE_TASK: "api_call",
                BPMNElementType.SCRIPT_TASK: "code_runner",
                BPMNElementType.MANUAL_TASK: "notification",
            }
        return self.TASK_TYPE_MAP

    def xǁBPMNToWorkflowConverterǁ_get_task_type_map__mutmut_1(self) -> dict[BPMNElementType, str]:
        if self.TASK_TYPE_MAP is not None:
            self.TASK_TYPE_MAP = {
                BPMNElementType.USER_TASK: "input",
                BPMNElementType.SERVICE_TASK: "api_call",
                BPMNElementType.SCRIPT_TASK: "code_runner",
                BPMNElementType.MANUAL_TASK: "notification",
            }
        return self.TASK_TYPE_MAP

    def xǁBPMNToWorkflowConverterǁ_get_task_type_map__mutmut_2(self) -> dict[BPMNElementType, str]:
        if self.TASK_TYPE_MAP is None:
            self.TASK_TYPE_MAP = None
        return self.TASK_TYPE_MAP

    def xǁBPMNToWorkflowConverterǁ_get_task_type_map__mutmut_3(self) -> dict[BPMNElementType, str]:
        if self.TASK_TYPE_MAP is None:
            self.TASK_TYPE_MAP = {
                BPMNElementType.USER_TASK: "XXinputXX",
                BPMNElementType.SERVICE_TASK: "api_call",
                BPMNElementType.SCRIPT_TASK: "code_runner",
                BPMNElementType.MANUAL_TASK: "notification",
            }
        return self.TASK_TYPE_MAP

    def xǁBPMNToWorkflowConverterǁ_get_task_type_map__mutmut_4(self) -> dict[BPMNElementType, str]:
        if self.TASK_TYPE_MAP is None:
            self.TASK_TYPE_MAP = {
                BPMNElementType.USER_TASK: "INPUT",
                BPMNElementType.SERVICE_TASK: "api_call",
                BPMNElementType.SCRIPT_TASK: "code_runner",
                BPMNElementType.MANUAL_TASK: "notification",
            }
        return self.TASK_TYPE_MAP

    def xǁBPMNToWorkflowConverterǁ_get_task_type_map__mutmut_5(self) -> dict[BPMNElementType, str]:
        if self.TASK_TYPE_MAP is None:
            self.TASK_TYPE_MAP = {
                BPMNElementType.USER_TASK: "input",
                BPMNElementType.SERVICE_TASK: "XXapi_callXX",
                BPMNElementType.SCRIPT_TASK: "code_runner",
                BPMNElementType.MANUAL_TASK: "notification",
            }
        return self.TASK_TYPE_MAP

    def xǁBPMNToWorkflowConverterǁ_get_task_type_map__mutmut_6(self) -> dict[BPMNElementType, str]:
        if self.TASK_TYPE_MAP is None:
            self.TASK_TYPE_MAP = {
                BPMNElementType.USER_TASK: "input",
                BPMNElementType.SERVICE_TASK: "API_CALL",
                BPMNElementType.SCRIPT_TASK: "code_runner",
                BPMNElementType.MANUAL_TASK: "notification",
            }
        return self.TASK_TYPE_MAP

    def xǁBPMNToWorkflowConverterǁ_get_task_type_map__mutmut_7(self) -> dict[BPMNElementType, str]:
        if self.TASK_TYPE_MAP is None:
            self.TASK_TYPE_MAP = {
                BPMNElementType.USER_TASK: "input",
                BPMNElementType.SERVICE_TASK: "api_call",
                BPMNElementType.SCRIPT_TASK: "XXcode_runnerXX",
                BPMNElementType.MANUAL_TASK: "notification",
            }
        return self.TASK_TYPE_MAP

    def xǁBPMNToWorkflowConverterǁ_get_task_type_map__mutmut_8(self) -> dict[BPMNElementType, str]:
        if self.TASK_TYPE_MAP is None:
            self.TASK_TYPE_MAP = {
                BPMNElementType.USER_TASK: "input",
                BPMNElementType.SERVICE_TASK: "api_call",
                BPMNElementType.SCRIPT_TASK: "CODE_RUNNER",
                BPMNElementType.MANUAL_TASK: "notification",
            }
        return self.TASK_TYPE_MAP

    def xǁBPMNToWorkflowConverterǁ_get_task_type_map__mutmut_9(self) -> dict[BPMNElementType, str]:
        if self.TASK_TYPE_MAP is None:
            self.TASK_TYPE_MAP = {
                BPMNElementType.USER_TASK: "input",
                BPMNElementType.SERVICE_TASK: "api_call",
                BPMNElementType.SCRIPT_TASK: "code_runner",
                BPMNElementType.MANUAL_TASK: "XXnotificationXX",
            }
        return self.TASK_TYPE_MAP

    def xǁBPMNToWorkflowConverterǁ_get_task_type_map__mutmut_10(self) -> dict[BPMNElementType, str]:
        if self.TASK_TYPE_MAP is None:
            self.TASK_TYPE_MAP = {
                BPMNElementType.USER_TASK: "input",
                BPMNElementType.SERVICE_TASK: "api_call",
                BPMNElementType.SCRIPT_TASK: "code_runner",
                BPMNElementType.MANUAL_TASK: "NOTIFICATION",
            }
        return self.TASK_TYPE_MAP

    @_mutmut_mutated(mutants_xǁBPMNToWorkflowConverterǁconvert__mutmut)
    def convert(self, process: BPMNProcess) -> dict[str, Any]:
        """Convert a BPMNProcess to a Zenic-Flijo workflow definition."""
        steps = []
        step_id_map: dict[str, str] = {}

        for element in process.elements.values():
            step = self._element_to_step(element, process)
            if step:
                step_id_map[element.element_id] = step["id"]
                steps.append(step)

        for flow in process.flows.values():
            source_step_id = step_id_map.get(flow.source_ref)
            target_step_id = step_id_map.get(flow.target_ref)
            if source_step_id and target_step_id:
                self._update_next_steps(steps, source_step_id, target_step_id, flow)

        start_events = process.get_start_events()
        entry_step_id = step_id_map.get(start_events[0].element_id) if start_events else None

        return {
            "name": process.name or process.process_id,
            "description": process.documentation or f"BPMN Process: {process.name}",
            "steps": steps,
            "entry_step_id": entry_step_id,
            "metadata": {"source": "bpmn", "bpmn_process_id": process.process_id, "version": process.version},
        }

    def xǁBPMNToWorkflowConverterǁconvert__mutmut_orig(self, process: BPMNProcess) -> dict[str, Any]:
        """Convert a BPMNProcess to a Zenic-Flijo workflow definition."""
        steps = []
        step_id_map: dict[str, str] = {}

        for element in process.elements.values():
            step = self._element_to_step(element, process)
            if step:
                step_id_map[element.element_id] = step["id"]
                steps.append(step)

        for flow in process.flows.values():
            source_step_id = step_id_map.get(flow.source_ref)
            target_step_id = step_id_map.get(flow.target_ref)
            if source_step_id and target_step_id:
                self._update_next_steps(steps, source_step_id, target_step_id, flow)

        start_events = process.get_start_events()
        entry_step_id = step_id_map.get(start_events[0].element_id) if start_events else None

        return {
            "name": process.name or process.process_id,
            "description": process.documentation or f"BPMN Process: {process.name}",
            "steps": steps,
            "entry_step_id": entry_step_id,
            "metadata": {"source": "bpmn", "bpmn_process_id": process.process_id, "version": process.version},
        }

    def xǁBPMNToWorkflowConverterǁconvert__mutmut_1(self, process: BPMNProcess) -> dict[str, Any]:
        """Convert a BPMNProcess to a Zenic-Flijo workflow definition."""
        steps = None
        step_id_map: dict[str, str] = {}

        for element in process.elements.values():
            step = self._element_to_step(element, process)
            if step:
                step_id_map[element.element_id] = step["id"]
                steps.append(step)

        for flow in process.flows.values():
            source_step_id = step_id_map.get(flow.source_ref)
            target_step_id = step_id_map.get(flow.target_ref)
            if source_step_id and target_step_id:
                self._update_next_steps(steps, source_step_id, target_step_id, flow)

        start_events = process.get_start_events()
        entry_step_id = step_id_map.get(start_events[0].element_id) if start_events else None

        return {
            "name": process.name or process.process_id,
            "description": process.documentation or f"BPMN Process: {process.name}",
            "steps": steps,
            "entry_step_id": entry_step_id,
            "metadata": {"source": "bpmn", "bpmn_process_id": process.process_id, "version": process.version},
        }

    def xǁBPMNToWorkflowConverterǁconvert__mutmut_2(self, process: BPMNProcess) -> dict[str, Any]:
        """Convert a BPMNProcess to a Zenic-Flijo workflow definition."""
        steps = []
        step_id_map: dict[str, str] = None

        for element in process.elements.values():
            step = self._element_to_step(element, process)
            if step:
                step_id_map[element.element_id] = step["id"]
                steps.append(step)

        for flow in process.flows.values():
            source_step_id = step_id_map.get(flow.source_ref)
            target_step_id = step_id_map.get(flow.target_ref)
            if source_step_id and target_step_id:
                self._update_next_steps(steps, source_step_id, target_step_id, flow)

        start_events = process.get_start_events()
        entry_step_id = step_id_map.get(start_events[0].element_id) if start_events else None

        return {
            "name": process.name or process.process_id,
            "description": process.documentation or f"BPMN Process: {process.name}",
            "steps": steps,
            "entry_step_id": entry_step_id,
            "metadata": {"source": "bpmn", "bpmn_process_id": process.process_id, "version": process.version},
        }

    def xǁBPMNToWorkflowConverterǁconvert__mutmut_3(self, process: BPMNProcess) -> dict[str, Any]:
        """Convert a BPMNProcess to a Zenic-Flijo workflow definition."""
        steps = []
        step_id_map: dict[str, str] = {}

        for element in process.elements.values():
            step = None
            if step:
                step_id_map[element.element_id] = step["id"]
                steps.append(step)

        for flow in process.flows.values():
            source_step_id = step_id_map.get(flow.source_ref)
            target_step_id = step_id_map.get(flow.target_ref)
            if source_step_id and target_step_id:
                self._update_next_steps(steps, source_step_id, target_step_id, flow)

        start_events = process.get_start_events()
        entry_step_id = step_id_map.get(start_events[0].element_id) if start_events else None

        return {
            "name": process.name or process.process_id,
            "description": process.documentation or f"BPMN Process: {process.name}",
            "steps": steps,
            "entry_step_id": entry_step_id,
            "metadata": {"source": "bpmn", "bpmn_process_id": process.process_id, "version": process.version},
        }

    def xǁBPMNToWorkflowConverterǁconvert__mutmut_4(self, process: BPMNProcess) -> dict[str, Any]:
        """Convert a BPMNProcess to a Zenic-Flijo workflow definition."""
        steps = []
        step_id_map: dict[str, str] = {}

        for element in process.elements.values():
            step = self._element_to_step(None, process)
            if step:
                step_id_map[element.element_id] = step["id"]
                steps.append(step)

        for flow in process.flows.values():
            source_step_id = step_id_map.get(flow.source_ref)
            target_step_id = step_id_map.get(flow.target_ref)
            if source_step_id and target_step_id:
                self._update_next_steps(steps, source_step_id, target_step_id, flow)

        start_events = process.get_start_events()
        entry_step_id = step_id_map.get(start_events[0].element_id) if start_events else None

        return {
            "name": process.name or process.process_id,
            "description": process.documentation or f"BPMN Process: {process.name}",
            "steps": steps,
            "entry_step_id": entry_step_id,
            "metadata": {"source": "bpmn", "bpmn_process_id": process.process_id, "version": process.version},
        }

    def xǁBPMNToWorkflowConverterǁconvert__mutmut_5(self, process: BPMNProcess) -> dict[str, Any]:
        """Convert a BPMNProcess to a Zenic-Flijo workflow definition."""
        steps = []
        step_id_map: dict[str, str] = {}

        for element in process.elements.values():
            step = self._element_to_step(element, None)
            if step:
                step_id_map[element.element_id] = step["id"]
                steps.append(step)

        for flow in process.flows.values():
            source_step_id = step_id_map.get(flow.source_ref)
            target_step_id = step_id_map.get(flow.target_ref)
            if source_step_id and target_step_id:
                self._update_next_steps(steps, source_step_id, target_step_id, flow)

        start_events = process.get_start_events()
        entry_step_id = step_id_map.get(start_events[0].element_id) if start_events else None

        return {
            "name": process.name or process.process_id,
            "description": process.documentation or f"BPMN Process: {process.name}",
            "steps": steps,
            "entry_step_id": entry_step_id,
            "metadata": {"source": "bpmn", "bpmn_process_id": process.process_id, "version": process.version},
        }

    def xǁBPMNToWorkflowConverterǁconvert__mutmut_6(self, process: BPMNProcess) -> dict[str, Any]:
        """Convert a BPMNProcess to a Zenic-Flijo workflow definition."""
        steps = []
        step_id_map: dict[str, str] = {}

        for element in process.elements.values():
            step = self._element_to_step(process)
            if step:
                step_id_map[element.element_id] = step["id"]
                steps.append(step)

        for flow in process.flows.values():
            source_step_id = step_id_map.get(flow.source_ref)
            target_step_id = step_id_map.get(flow.target_ref)
            if source_step_id and target_step_id:
                self._update_next_steps(steps, source_step_id, target_step_id, flow)

        start_events = process.get_start_events()
        entry_step_id = step_id_map.get(start_events[0].element_id) if start_events else None

        return {
            "name": process.name or process.process_id,
            "description": process.documentation or f"BPMN Process: {process.name}",
            "steps": steps,
            "entry_step_id": entry_step_id,
            "metadata": {"source": "bpmn", "bpmn_process_id": process.process_id, "version": process.version},
        }

    def xǁBPMNToWorkflowConverterǁconvert__mutmut_7(self, process: BPMNProcess) -> dict[str, Any]:
        """Convert a BPMNProcess to a Zenic-Flijo workflow definition."""
        steps = []
        step_id_map: dict[str, str] = {}

        for element in process.elements.values():
            step = self._element_to_step(element, )
            if step:
                step_id_map[element.element_id] = step["id"]
                steps.append(step)

        for flow in process.flows.values():
            source_step_id = step_id_map.get(flow.source_ref)
            target_step_id = step_id_map.get(flow.target_ref)
            if source_step_id and target_step_id:
                self._update_next_steps(steps, source_step_id, target_step_id, flow)

        start_events = process.get_start_events()
        entry_step_id = step_id_map.get(start_events[0].element_id) if start_events else None

        return {
            "name": process.name or process.process_id,
            "description": process.documentation or f"BPMN Process: {process.name}",
            "steps": steps,
            "entry_step_id": entry_step_id,
            "metadata": {"source": "bpmn", "bpmn_process_id": process.process_id, "version": process.version},
        }

    def xǁBPMNToWorkflowConverterǁconvert__mutmut_8(self, process: BPMNProcess) -> dict[str, Any]:
        """Convert a BPMNProcess to a Zenic-Flijo workflow definition."""
        steps = []
        step_id_map: dict[str, str] = {}

        for element in process.elements.values():
            step = self._element_to_step(element, process)
            if step:
                step_id_map[element.element_id] = None
                steps.append(step)

        for flow in process.flows.values():
            source_step_id = step_id_map.get(flow.source_ref)
            target_step_id = step_id_map.get(flow.target_ref)
            if source_step_id and target_step_id:
                self._update_next_steps(steps, source_step_id, target_step_id, flow)

        start_events = process.get_start_events()
        entry_step_id = step_id_map.get(start_events[0].element_id) if start_events else None

        return {
            "name": process.name or process.process_id,
            "description": process.documentation or f"BPMN Process: {process.name}",
            "steps": steps,
            "entry_step_id": entry_step_id,
            "metadata": {"source": "bpmn", "bpmn_process_id": process.process_id, "version": process.version},
        }

    def xǁBPMNToWorkflowConverterǁconvert__mutmut_9(self, process: BPMNProcess) -> dict[str, Any]:
        """Convert a BPMNProcess to a Zenic-Flijo workflow definition."""
        steps = []
        step_id_map: dict[str, str] = {}

        for element in process.elements.values():
            step = self._element_to_step(element, process)
            if step:
                step_id_map[element.element_id] = step["XXidXX"]
                steps.append(step)

        for flow in process.flows.values():
            source_step_id = step_id_map.get(flow.source_ref)
            target_step_id = step_id_map.get(flow.target_ref)
            if source_step_id and target_step_id:
                self._update_next_steps(steps, source_step_id, target_step_id, flow)

        start_events = process.get_start_events()
        entry_step_id = step_id_map.get(start_events[0].element_id) if start_events else None

        return {
            "name": process.name or process.process_id,
            "description": process.documentation or f"BPMN Process: {process.name}",
            "steps": steps,
            "entry_step_id": entry_step_id,
            "metadata": {"source": "bpmn", "bpmn_process_id": process.process_id, "version": process.version},
        }

    def xǁBPMNToWorkflowConverterǁconvert__mutmut_10(self, process: BPMNProcess) -> dict[str, Any]:
        """Convert a BPMNProcess to a Zenic-Flijo workflow definition."""
        steps = []
        step_id_map: dict[str, str] = {}

        for element in process.elements.values():
            step = self._element_to_step(element, process)
            if step:
                step_id_map[element.element_id] = step["ID"]
                steps.append(step)

        for flow in process.flows.values():
            source_step_id = step_id_map.get(flow.source_ref)
            target_step_id = step_id_map.get(flow.target_ref)
            if source_step_id and target_step_id:
                self._update_next_steps(steps, source_step_id, target_step_id, flow)

        start_events = process.get_start_events()
        entry_step_id = step_id_map.get(start_events[0].element_id) if start_events else None

        return {
            "name": process.name or process.process_id,
            "description": process.documentation or f"BPMN Process: {process.name}",
            "steps": steps,
            "entry_step_id": entry_step_id,
            "metadata": {"source": "bpmn", "bpmn_process_id": process.process_id, "version": process.version},
        }

    def xǁBPMNToWorkflowConverterǁconvert__mutmut_11(self, process: BPMNProcess) -> dict[str, Any]:
        """Convert a BPMNProcess to a Zenic-Flijo workflow definition."""
        steps = []
        step_id_map: dict[str, str] = {}

        for element in process.elements.values():
            step = self._element_to_step(element, process)
            if step:
                step_id_map[element.element_id] = step["id"]
                steps.append(None)

        for flow in process.flows.values():
            source_step_id = step_id_map.get(flow.source_ref)
            target_step_id = step_id_map.get(flow.target_ref)
            if source_step_id and target_step_id:
                self._update_next_steps(steps, source_step_id, target_step_id, flow)

        start_events = process.get_start_events()
        entry_step_id = step_id_map.get(start_events[0].element_id) if start_events else None

        return {
            "name": process.name or process.process_id,
            "description": process.documentation or f"BPMN Process: {process.name}",
            "steps": steps,
            "entry_step_id": entry_step_id,
            "metadata": {"source": "bpmn", "bpmn_process_id": process.process_id, "version": process.version},
        }

    def xǁBPMNToWorkflowConverterǁconvert__mutmut_12(self, process: BPMNProcess) -> dict[str, Any]:
        """Convert a BPMNProcess to a Zenic-Flijo workflow definition."""
        steps = []
        step_id_map: dict[str, str] = {}

        for element in process.elements.values():
            step = self._element_to_step(element, process)
            if step:
                step_id_map[element.element_id] = step["id"]
                steps.append(step)

        for flow in process.flows.values():
            source_step_id = None
            target_step_id = step_id_map.get(flow.target_ref)
            if source_step_id and target_step_id:
                self._update_next_steps(steps, source_step_id, target_step_id, flow)

        start_events = process.get_start_events()
        entry_step_id = step_id_map.get(start_events[0].element_id) if start_events else None

        return {
            "name": process.name or process.process_id,
            "description": process.documentation or f"BPMN Process: {process.name}",
            "steps": steps,
            "entry_step_id": entry_step_id,
            "metadata": {"source": "bpmn", "bpmn_process_id": process.process_id, "version": process.version},
        }

    def xǁBPMNToWorkflowConverterǁconvert__mutmut_13(self, process: BPMNProcess) -> dict[str, Any]:
        """Convert a BPMNProcess to a Zenic-Flijo workflow definition."""
        steps = []
        step_id_map: dict[str, str] = {}

        for element in process.elements.values():
            step = self._element_to_step(element, process)
            if step:
                step_id_map[element.element_id] = step["id"]
                steps.append(step)

        for flow in process.flows.values():
            source_step_id = step_id_map.get(None)
            target_step_id = step_id_map.get(flow.target_ref)
            if source_step_id and target_step_id:
                self._update_next_steps(steps, source_step_id, target_step_id, flow)

        start_events = process.get_start_events()
        entry_step_id = step_id_map.get(start_events[0].element_id) if start_events else None

        return {
            "name": process.name or process.process_id,
            "description": process.documentation or f"BPMN Process: {process.name}",
            "steps": steps,
            "entry_step_id": entry_step_id,
            "metadata": {"source": "bpmn", "bpmn_process_id": process.process_id, "version": process.version},
        }

    def xǁBPMNToWorkflowConverterǁconvert__mutmut_14(self, process: BPMNProcess) -> dict[str, Any]:
        """Convert a BPMNProcess to a Zenic-Flijo workflow definition."""
        steps = []
        step_id_map: dict[str, str] = {}

        for element in process.elements.values():
            step = self._element_to_step(element, process)
            if step:
                step_id_map[element.element_id] = step["id"]
                steps.append(step)

        for flow in process.flows.values():
            source_step_id = step_id_map.get(flow.source_ref)
            target_step_id = None
            if source_step_id and target_step_id:
                self._update_next_steps(steps, source_step_id, target_step_id, flow)

        start_events = process.get_start_events()
        entry_step_id = step_id_map.get(start_events[0].element_id) if start_events else None

        return {
            "name": process.name or process.process_id,
            "description": process.documentation or f"BPMN Process: {process.name}",
            "steps": steps,
            "entry_step_id": entry_step_id,
            "metadata": {"source": "bpmn", "bpmn_process_id": process.process_id, "version": process.version},
        }

    def xǁBPMNToWorkflowConverterǁconvert__mutmut_15(self, process: BPMNProcess) -> dict[str, Any]:
        """Convert a BPMNProcess to a Zenic-Flijo workflow definition."""
        steps = []
        step_id_map: dict[str, str] = {}

        for element in process.elements.values():
            step = self._element_to_step(element, process)
            if step:
                step_id_map[element.element_id] = step["id"]
                steps.append(step)

        for flow in process.flows.values():
            source_step_id = step_id_map.get(flow.source_ref)
            target_step_id = step_id_map.get(None)
            if source_step_id and target_step_id:
                self._update_next_steps(steps, source_step_id, target_step_id, flow)

        start_events = process.get_start_events()
        entry_step_id = step_id_map.get(start_events[0].element_id) if start_events else None

        return {
            "name": process.name or process.process_id,
            "description": process.documentation or f"BPMN Process: {process.name}",
            "steps": steps,
            "entry_step_id": entry_step_id,
            "metadata": {"source": "bpmn", "bpmn_process_id": process.process_id, "version": process.version},
        }

    def xǁBPMNToWorkflowConverterǁconvert__mutmut_16(self, process: BPMNProcess) -> dict[str, Any]:
        """Convert a BPMNProcess to a Zenic-Flijo workflow definition."""
        steps = []
        step_id_map: dict[str, str] = {}

        for element in process.elements.values():
            step = self._element_to_step(element, process)
            if step:
                step_id_map[element.element_id] = step["id"]
                steps.append(step)

        for flow in process.flows.values():
            source_step_id = step_id_map.get(flow.source_ref)
            target_step_id = step_id_map.get(flow.target_ref)
            if source_step_id or target_step_id:
                self._update_next_steps(steps, source_step_id, target_step_id, flow)

        start_events = process.get_start_events()
        entry_step_id = step_id_map.get(start_events[0].element_id) if start_events else None

        return {
            "name": process.name or process.process_id,
            "description": process.documentation or f"BPMN Process: {process.name}",
            "steps": steps,
            "entry_step_id": entry_step_id,
            "metadata": {"source": "bpmn", "bpmn_process_id": process.process_id, "version": process.version},
        }

    def xǁBPMNToWorkflowConverterǁconvert__mutmut_17(self, process: BPMNProcess) -> dict[str, Any]:
        """Convert a BPMNProcess to a Zenic-Flijo workflow definition."""
        steps = []
        step_id_map: dict[str, str] = {}

        for element in process.elements.values():
            step = self._element_to_step(element, process)
            if step:
                step_id_map[element.element_id] = step["id"]
                steps.append(step)

        for flow in process.flows.values():
            source_step_id = step_id_map.get(flow.source_ref)
            target_step_id = step_id_map.get(flow.target_ref)
            if source_step_id and target_step_id:
                self._update_next_steps(None, source_step_id, target_step_id, flow)

        start_events = process.get_start_events()
        entry_step_id = step_id_map.get(start_events[0].element_id) if start_events else None

        return {
            "name": process.name or process.process_id,
            "description": process.documentation or f"BPMN Process: {process.name}",
            "steps": steps,
            "entry_step_id": entry_step_id,
            "metadata": {"source": "bpmn", "bpmn_process_id": process.process_id, "version": process.version},
        }

    def xǁBPMNToWorkflowConverterǁconvert__mutmut_18(self, process: BPMNProcess) -> dict[str, Any]:
        """Convert a BPMNProcess to a Zenic-Flijo workflow definition."""
        steps = []
        step_id_map: dict[str, str] = {}

        for element in process.elements.values():
            step = self._element_to_step(element, process)
            if step:
                step_id_map[element.element_id] = step["id"]
                steps.append(step)

        for flow in process.flows.values():
            source_step_id = step_id_map.get(flow.source_ref)
            target_step_id = step_id_map.get(flow.target_ref)
            if source_step_id and target_step_id:
                self._update_next_steps(steps, None, target_step_id, flow)

        start_events = process.get_start_events()
        entry_step_id = step_id_map.get(start_events[0].element_id) if start_events else None

        return {
            "name": process.name or process.process_id,
            "description": process.documentation or f"BPMN Process: {process.name}",
            "steps": steps,
            "entry_step_id": entry_step_id,
            "metadata": {"source": "bpmn", "bpmn_process_id": process.process_id, "version": process.version},
        }

    def xǁBPMNToWorkflowConverterǁconvert__mutmut_19(self, process: BPMNProcess) -> dict[str, Any]:
        """Convert a BPMNProcess to a Zenic-Flijo workflow definition."""
        steps = []
        step_id_map: dict[str, str] = {}

        for element in process.elements.values():
            step = self._element_to_step(element, process)
            if step:
                step_id_map[element.element_id] = step["id"]
                steps.append(step)

        for flow in process.flows.values():
            source_step_id = step_id_map.get(flow.source_ref)
            target_step_id = step_id_map.get(flow.target_ref)
            if source_step_id and target_step_id:
                self._update_next_steps(steps, source_step_id, None, flow)

        start_events = process.get_start_events()
        entry_step_id = step_id_map.get(start_events[0].element_id) if start_events else None

        return {
            "name": process.name or process.process_id,
            "description": process.documentation or f"BPMN Process: {process.name}",
            "steps": steps,
            "entry_step_id": entry_step_id,
            "metadata": {"source": "bpmn", "bpmn_process_id": process.process_id, "version": process.version},
        }

    def xǁBPMNToWorkflowConverterǁconvert__mutmut_20(self, process: BPMNProcess) -> dict[str, Any]:
        """Convert a BPMNProcess to a Zenic-Flijo workflow definition."""
        steps = []
        step_id_map: dict[str, str] = {}

        for element in process.elements.values():
            step = self._element_to_step(element, process)
            if step:
                step_id_map[element.element_id] = step["id"]
                steps.append(step)

        for flow in process.flows.values():
            source_step_id = step_id_map.get(flow.source_ref)
            target_step_id = step_id_map.get(flow.target_ref)
            if source_step_id and target_step_id:
                self._update_next_steps(steps, source_step_id, target_step_id, None)

        start_events = process.get_start_events()
        entry_step_id = step_id_map.get(start_events[0].element_id) if start_events else None

        return {
            "name": process.name or process.process_id,
            "description": process.documentation or f"BPMN Process: {process.name}",
            "steps": steps,
            "entry_step_id": entry_step_id,
            "metadata": {"source": "bpmn", "bpmn_process_id": process.process_id, "version": process.version},
        }

    def xǁBPMNToWorkflowConverterǁconvert__mutmut_21(self, process: BPMNProcess) -> dict[str, Any]:
        """Convert a BPMNProcess to a Zenic-Flijo workflow definition."""
        steps = []
        step_id_map: dict[str, str] = {}

        for element in process.elements.values():
            step = self._element_to_step(element, process)
            if step:
                step_id_map[element.element_id] = step["id"]
                steps.append(step)

        for flow in process.flows.values():
            source_step_id = step_id_map.get(flow.source_ref)
            target_step_id = step_id_map.get(flow.target_ref)
            if source_step_id and target_step_id:
                self._update_next_steps(source_step_id, target_step_id, flow)

        start_events = process.get_start_events()
        entry_step_id = step_id_map.get(start_events[0].element_id) if start_events else None

        return {
            "name": process.name or process.process_id,
            "description": process.documentation or f"BPMN Process: {process.name}",
            "steps": steps,
            "entry_step_id": entry_step_id,
            "metadata": {"source": "bpmn", "bpmn_process_id": process.process_id, "version": process.version},
        }

    def xǁBPMNToWorkflowConverterǁconvert__mutmut_22(self, process: BPMNProcess) -> dict[str, Any]:
        """Convert a BPMNProcess to a Zenic-Flijo workflow definition."""
        steps = []
        step_id_map: dict[str, str] = {}

        for element in process.elements.values():
            step = self._element_to_step(element, process)
            if step:
                step_id_map[element.element_id] = step["id"]
                steps.append(step)

        for flow in process.flows.values():
            source_step_id = step_id_map.get(flow.source_ref)
            target_step_id = step_id_map.get(flow.target_ref)
            if source_step_id and target_step_id:
                self._update_next_steps(steps, target_step_id, flow)

        start_events = process.get_start_events()
        entry_step_id = step_id_map.get(start_events[0].element_id) if start_events else None

        return {
            "name": process.name or process.process_id,
            "description": process.documentation or f"BPMN Process: {process.name}",
            "steps": steps,
            "entry_step_id": entry_step_id,
            "metadata": {"source": "bpmn", "bpmn_process_id": process.process_id, "version": process.version},
        }

    def xǁBPMNToWorkflowConverterǁconvert__mutmut_23(self, process: BPMNProcess) -> dict[str, Any]:
        """Convert a BPMNProcess to a Zenic-Flijo workflow definition."""
        steps = []
        step_id_map: dict[str, str] = {}

        for element in process.elements.values():
            step = self._element_to_step(element, process)
            if step:
                step_id_map[element.element_id] = step["id"]
                steps.append(step)

        for flow in process.flows.values():
            source_step_id = step_id_map.get(flow.source_ref)
            target_step_id = step_id_map.get(flow.target_ref)
            if source_step_id and target_step_id:
                self._update_next_steps(steps, source_step_id, flow)

        start_events = process.get_start_events()
        entry_step_id = step_id_map.get(start_events[0].element_id) if start_events else None

        return {
            "name": process.name or process.process_id,
            "description": process.documentation or f"BPMN Process: {process.name}",
            "steps": steps,
            "entry_step_id": entry_step_id,
            "metadata": {"source": "bpmn", "bpmn_process_id": process.process_id, "version": process.version},
        }

    def xǁBPMNToWorkflowConverterǁconvert__mutmut_24(self, process: BPMNProcess) -> dict[str, Any]:
        """Convert a BPMNProcess to a Zenic-Flijo workflow definition."""
        steps = []
        step_id_map: dict[str, str] = {}

        for element in process.elements.values():
            step = self._element_to_step(element, process)
            if step:
                step_id_map[element.element_id] = step["id"]
                steps.append(step)

        for flow in process.flows.values():
            source_step_id = step_id_map.get(flow.source_ref)
            target_step_id = step_id_map.get(flow.target_ref)
            if source_step_id and target_step_id:
                self._update_next_steps(steps, source_step_id, target_step_id, )

        start_events = process.get_start_events()
        entry_step_id = step_id_map.get(start_events[0].element_id) if start_events else None

        return {
            "name": process.name or process.process_id,
            "description": process.documentation or f"BPMN Process: {process.name}",
            "steps": steps,
            "entry_step_id": entry_step_id,
            "metadata": {"source": "bpmn", "bpmn_process_id": process.process_id, "version": process.version},
        }

    def xǁBPMNToWorkflowConverterǁconvert__mutmut_25(self, process: BPMNProcess) -> dict[str, Any]:
        """Convert a BPMNProcess to a Zenic-Flijo workflow definition."""
        steps = []
        step_id_map: dict[str, str] = {}

        for element in process.elements.values():
            step = self._element_to_step(element, process)
            if step:
                step_id_map[element.element_id] = step["id"]
                steps.append(step)

        for flow in process.flows.values():
            source_step_id = step_id_map.get(flow.source_ref)
            target_step_id = step_id_map.get(flow.target_ref)
            if source_step_id and target_step_id:
                self._update_next_steps(steps, source_step_id, target_step_id, flow)

        start_events = None
        entry_step_id = step_id_map.get(start_events[0].element_id) if start_events else None

        return {
            "name": process.name or process.process_id,
            "description": process.documentation or f"BPMN Process: {process.name}",
            "steps": steps,
            "entry_step_id": entry_step_id,
            "metadata": {"source": "bpmn", "bpmn_process_id": process.process_id, "version": process.version},
        }

    def xǁBPMNToWorkflowConverterǁconvert__mutmut_26(self, process: BPMNProcess) -> dict[str, Any]:
        """Convert a BPMNProcess to a Zenic-Flijo workflow definition."""
        steps = []
        step_id_map: dict[str, str] = {}

        for element in process.elements.values():
            step = self._element_to_step(element, process)
            if step:
                step_id_map[element.element_id] = step["id"]
                steps.append(step)

        for flow in process.flows.values():
            source_step_id = step_id_map.get(flow.source_ref)
            target_step_id = step_id_map.get(flow.target_ref)
            if source_step_id and target_step_id:
                self._update_next_steps(steps, source_step_id, target_step_id, flow)

        start_events = process.get_start_events()
        entry_step_id = None

        return {
            "name": process.name or process.process_id,
            "description": process.documentation or f"BPMN Process: {process.name}",
            "steps": steps,
            "entry_step_id": entry_step_id,
            "metadata": {"source": "bpmn", "bpmn_process_id": process.process_id, "version": process.version},
        }

    def xǁBPMNToWorkflowConverterǁconvert__mutmut_27(self, process: BPMNProcess) -> dict[str, Any]:
        """Convert a BPMNProcess to a Zenic-Flijo workflow definition."""
        steps = []
        step_id_map: dict[str, str] = {}

        for element in process.elements.values():
            step = self._element_to_step(element, process)
            if step:
                step_id_map[element.element_id] = step["id"]
                steps.append(step)

        for flow in process.flows.values():
            source_step_id = step_id_map.get(flow.source_ref)
            target_step_id = step_id_map.get(flow.target_ref)
            if source_step_id and target_step_id:
                self._update_next_steps(steps, source_step_id, target_step_id, flow)

        start_events = process.get_start_events()
        entry_step_id = step_id_map.get(None) if start_events else None

        return {
            "name": process.name or process.process_id,
            "description": process.documentation or f"BPMN Process: {process.name}",
            "steps": steps,
            "entry_step_id": entry_step_id,
            "metadata": {"source": "bpmn", "bpmn_process_id": process.process_id, "version": process.version},
        }

    def xǁBPMNToWorkflowConverterǁconvert__mutmut_28(self, process: BPMNProcess) -> dict[str, Any]:
        """Convert a BPMNProcess to a Zenic-Flijo workflow definition."""
        steps = []
        step_id_map: dict[str, str] = {}

        for element in process.elements.values():
            step = self._element_to_step(element, process)
            if step:
                step_id_map[element.element_id] = step["id"]
                steps.append(step)

        for flow in process.flows.values():
            source_step_id = step_id_map.get(flow.source_ref)
            target_step_id = step_id_map.get(flow.target_ref)
            if source_step_id and target_step_id:
                self._update_next_steps(steps, source_step_id, target_step_id, flow)

        start_events = process.get_start_events()
        entry_step_id = step_id_map.get(start_events[1].element_id) if start_events else None

        return {
            "name": process.name or process.process_id,
            "description": process.documentation or f"BPMN Process: {process.name}",
            "steps": steps,
            "entry_step_id": entry_step_id,
            "metadata": {"source": "bpmn", "bpmn_process_id": process.process_id, "version": process.version},
        }

    def xǁBPMNToWorkflowConverterǁconvert__mutmut_29(self, process: BPMNProcess) -> dict[str, Any]:
        """Convert a BPMNProcess to a Zenic-Flijo workflow definition."""
        steps = []
        step_id_map: dict[str, str] = {}

        for element in process.elements.values():
            step = self._element_to_step(element, process)
            if step:
                step_id_map[element.element_id] = step["id"]
                steps.append(step)

        for flow in process.flows.values():
            source_step_id = step_id_map.get(flow.source_ref)
            target_step_id = step_id_map.get(flow.target_ref)
            if source_step_id and target_step_id:
                self._update_next_steps(steps, source_step_id, target_step_id, flow)

        start_events = process.get_start_events()
        entry_step_id = step_id_map.get(start_events[0].element_id) if start_events else None

        return {
            "XXnameXX": process.name or process.process_id,
            "description": process.documentation or f"BPMN Process: {process.name}",
            "steps": steps,
            "entry_step_id": entry_step_id,
            "metadata": {"source": "bpmn", "bpmn_process_id": process.process_id, "version": process.version},
        }

    def xǁBPMNToWorkflowConverterǁconvert__mutmut_30(self, process: BPMNProcess) -> dict[str, Any]:
        """Convert a BPMNProcess to a Zenic-Flijo workflow definition."""
        steps = []
        step_id_map: dict[str, str] = {}

        for element in process.elements.values():
            step = self._element_to_step(element, process)
            if step:
                step_id_map[element.element_id] = step["id"]
                steps.append(step)

        for flow in process.flows.values():
            source_step_id = step_id_map.get(flow.source_ref)
            target_step_id = step_id_map.get(flow.target_ref)
            if source_step_id and target_step_id:
                self._update_next_steps(steps, source_step_id, target_step_id, flow)

        start_events = process.get_start_events()
        entry_step_id = step_id_map.get(start_events[0].element_id) if start_events else None

        return {
            "NAME": process.name or process.process_id,
            "description": process.documentation or f"BPMN Process: {process.name}",
            "steps": steps,
            "entry_step_id": entry_step_id,
            "metadata": {"source": "bpmn", "bpmn_process_id": process.process_id, "version": process.version},
        }

    def xǁBPMNToWorkflowConverterǁconvert__mutmut_31(self, process: BPMNProcess) -> dict[str, Any]:
        """Convert a BPMNProcess to a Zenic-Flijo workflow definition."""
        steps = []
        step_id_map: dict[str, str] = {}

        for element in process.elements.values():
            step = self._element_to_step(element, process)
            if step:
                step_id_map[element.element_id] = step["id"]
                steps.append(step)

        for flow in process.flows.values():
            source_step_id = step_id_map.get(flow.source_ref)
            target_step_id = step_id_map.get(flow.target_ref)
            if source_step_id and target_step_id:
                self._update_next_steps(steps, source_step_id, target_step_id, flow)

        start_events = process.get_start_events()
        entry_step_id = step_id_map.get(start_events[0].element_id) if start_events else None

        return {
            "name": process.name and process.process_id,
            "description": process.documentation or f"BPMN Process: {process.name}",
            "steps": steps,
            "entry_step_id": entry_step_id,
            "metadata": {"source": "bpmn", "bpmn_process_id": process.process_id, "version": process.version},
        }

    def xǁBPMNToWorkflowConverterǁconvert__mutmut_32(self, process: BPMNProcess) -> dict[str, Any]:
        """Convert a BPMNProcess to a Zenic-Flijo workflow definition."""
        steps = []
        step_id_map: dict[str, str] = {}

        for element in process.elements.values():
            step = self._element_to_step(element, process)
            if step:
                step_id_map[element.element_id] = step["id"]
                steps.append(step)

        for flow in process.flows.values():
            source_step_id = step_id_map.get(flow.source_ref)
            target_step_id = step_id_map.get(flow.target_ref)
            if source_step_id and target_step_id:
                self._update_next_steps(steps, source_step_id, target_step_id, flow)

        start_events = process.get_start_events()
        entry_step_id = step_id_map.get(start_events[0].element_id) if start_events else None

        return {
            "name": process.name or process.process_id,
            "XXdescriptionXX": process.documentation or f"BPMN Process: {process.name}",
            "steps": steps,
            "entry_step_id": entry_step_id,
            "metadata": {"source": "bpmn", "bpmn_process_id": process.process_id, "version": process.version},
        }

    def xǁBPMNToWorkflowConverterǁconvert__mutmut_33(self, process: BPMNProcess) -> dict[str, Any]:
        """Convert a BPMNProcess to a Zenic-Flijo workflow definition."""
        steps = []
        step_id_map: dict[str, str] = {}

        for element in process.elements.values():
            step = self._element_to_step(element, process)
            if step:
                step_id_map[element.element_id] = step["id"]
                steps.append(step)

        for flow in process.flows.values():
            source_step_id = step_id_map.get(flow.source_ref)
            target_step_id = step_id_map.get(flow.target_ref)
            if source_step_id and target_step_id:
                self._update_next_steps(steps, source_step_id, target_step_id, flow)

        start_events = process.get_start_events()
        entry_step_id = step_id_map.get(start_events[0].element_id) if start_events else None

        return {
            "name": process.name or process.process_id,
            "DESCRIPTION": process.documentation or f"BPMN Process: {process.name}",
            "steps": steps,
            "entry_step_id": entry_step_id,
            "metadata": {"source": "bpmn", "bpmn_process_id": process.process_id, "version": process.version},
        }

    def xǁBPMNToWorkflowConverterǁconvert__mutmut_34(self, process: BPMNProcess) -> dict[str, Any]:
        """Convert a BPMNProcess to a Zenic-Flijo workflow definition."""
        steps = []
        step_id_map: dict[str, str] = {}

        for element in process.elements.values():
            step = self._element_to_step(element, process)
            if step:
                step_id_map[element.element_id] = step["id"]
                steps.append(step)

        for flow in process.flows.values():
            source_step_id = step_id_map.get(flow.source_ref)
            target_step_id = step_id_map.get(flow.target_ref)
            if source_step_id and target_step_id:
                self._update_next_steps(steps, source_step_id, target_step_id, flow)

        start_events = process.get_start_events()
        entry_step_id = step_id_map.get(start_events[0].element_id) if start_events else None

        return {
            "name": process.name or process.process_id,
            "description": process.documentation and f"BPMN Process: {process.name}",
            "steps": steps,
            "entry_step_id": entry_step_id,
            "metadata": {"source": "bpmn", "bpmn_process_id": process.process_id, "version": process.version},
        }

    def xǁBPMNToWorkflowConverterǁconvert__mutmut_35(self, process: BPMNProcess) -> dict[str, Any]:
        """Convert a BPMNProcess to a Zenic-Flijo workflow definition."""
        steps = []
        step_id_map: dict[str, str] = {}

        for element in process.elements.values():
            step = self._element_to_step(element, process)
            if step:
                step_id_map[element.element_id] = step["id"]
                steps.append(step)

        for flow in process.flows.values():
            source_step_id = step_id_map.get(flow.source_ref)
            target_step_id = step_id_map.get(flow.target_ref)
            if source_step_id and target_step_id:
                self._update_next_steps(steps, source_step_id, target_step_id, flow)

        start_events = process.get_start_events()
        entry_step_id = step_id_map.get(start_events[0].element_id) if start_events else None

        return {
            "name": process.name or process.process_id,
            "description": process.documentation or f"BPMN Process: {process.name}",
            "XXstepsXX": steps,
            "entry_step_id": entry_step_id,
            "metadata": {"source": "bpmn", "bpmn_process_id": process.process_id, "version": process.version},
        }

    def xǁBPMNToWorkflowConverterǁconvert__mutmut_36(self, process: BPMNProcess) -> dict[str, Any]:
        """Convert a BPMNProcess to a Zenic-Flijo workflow definition."""
        steps = []
        step_id_map: dict[str, str] = {}

        for element in process.elements.values():
            step = self._element_to_step(element, process)
            if step:
                step_id_map[element.element_id] = step["id"]
                steps.append(step)

        for flow in process.flows.values():
            source_step_id = step_id_map.get(flow.source_ref)
            target_step_id = step_id_map.get(flow.target_ref)
            if source_step_id and target_step_id:
                self._update_next_steps(steps, source_step_id, target_step_id, flow)

        start_events = process.get_start_events()
        entry_step_id = step_id_map.get(start_events[0].element_id) if start_events else None

        return {
            "name": process.name or process.process_id,
            "description": process.documentation or f"BPMN Process: {process.name}",
            "STEPS": steps,
            "entry_step_id": entry_step_id,
            "metadata": {"source": "bpmn", "bpmn_process_id": process.process_id, "version": process.version},
        }

    def xǁBPMNToWorkflowConverterǁconvert__mutmut_37(self, process: BPMNProcess) -> dict[str, Any]:
        """Convert a BPMNProcess to a Zenic-Flijo workflow definition."""
        steps = []
        step_id_map: dict[str, str] = {}

        for element in process.elements.values():
            step = self._element_to_step(element, process)
            if step:
                step_id_map[element.element_id] = step["id"]
                steps.append(step)

        for flow in process.flows.values():
            source_step_id = step_id_map.get(flow.source_ref)
            target_step_id = step_id_map.get(flow.target_ref)
            if source_step_id and target_step_id:
                self._update_next_steps(steps, source_step_id, target_step_id, flow)

        start_events = process.get_start_events()
        entry_step_id = step_id_map.get(start_events[0].element_id) if start_events else None

        return {
            "name": process.name or process.process_id,
            "description": process.documentation or f"BPMN Process: {process.name}",
            "steps": steps,
            "XXentry_step_idXX": entry_step_id,
            "metadata": {"source": "bpmn", "bpmn_process_id": process.process_id, "version": process.version},
        }

    def xǁBPMNToWorkflowConverterǁconvert__mutmut_38(self, process: BPMNProcess) -> dict[str, Any]:
        """Convert a BPMNProcess to a Zenic-Flijo workflow definition."""
        steps = []
        step_id_map: dict[str, str] = {}

        for element in process.elements.values():
            step = self._element_to_step(element, process)
            if step:
                step_id_map[element.element_id] = step["id"]
                steps.append(step)

        for flow in process.flows.values():
            source_step_id = step_id_map.get(flow.source_ref)
            target_step_id = step_id_map.get(flow.target_ref)
            if source_step_id and target_step_id:
                self._update_next_steps(steps, source_step_id, target_step_id, flow)

        start_events = process.get_start_events()
        entry_step_id = step_id_map.get(start_events[0].element_id) if start_events else None

        return {
            "name": process.name or process.process_id,
            "description": process.documentation or f"BPMN Process: {process.name}",
            "steps": steps,
            "ENTRY_STEP_ID": entry_step_id,
            "metadata": {"source": "bpmn", "bpmn_process_id": process.process_id, "version": process.version},
        }

    def xǁBPMNToWorkflowConverterǁconvert__mutmut_39(self, process: BPMNProcess) -> dict[str, Any]:
        """Convert a BPMNProcess to a Zenic-Flijo workflow definition."""
        steps = []
        step_id_map: dict[str, str] = {}

        for element in process.elements.values():
            step = self._element_to_step(element, process)
            if step:
                step_id_map[element.element_id] = step["id"]
                steps.append(step)

        for flow in process.flows.values():
            source_step_id = step_id_map.get(flow.source_ref)
            target_step_id = step_id_map.get(flow.target_ref)
            if source_step_id and target_step_id:
                self._update_next_steps(steps, source_step_id, target_step_id, flow)

        start_events = process.get_start_events()
        entry_step_id = step_id_map.get(start_events[0].element_id) if start_events else None

        return {
            "name": process.name or process.process_id,
            "description": process.documentation or f"BPMN Process: {process.name}",
            "steps": steps,
            "entry_step_id": entry_step_id,
            "XXmetadataXX": {"source": "bpmn", "bpmn_process_id": process.process_id, "version": process.version},
        }

    def xǁBPMNToWorkflowConverterǁconvert__mutmut_40(self, process: BPMNProcess) -> dict[str, Any]:
        """Convert a BPMNProcess to a Zenic-Flijo workflow definition."""
        steps = []
        step_id_map: dict[str, str] = {}

        for element in process.elements.values():
            step = self._element_to_step(element, process)
            if step:
                step_id_map[element.element_id] = step["id"]
                steps.append(step)

        for flow in process.flows.values():
            source_step_id = step_id_map.get(flow.source_ref)
            target_step_id = step_id_map.get(flow.target_ref)
            if source_step_id and target_step_id:
                self._update_next_steps(steps, source_step_id, target_step_id, flow)

        start_events = process.get_start_events()
        entry_step_id = step_id_map.get(start_events[0].element_id) if start_events else None

        return {
            "name": process.name or process.process_id,
            "description": process.documentation or f"BPMN Process: {process.name}",
            "steps": steps,
            "entry_step_id": entry_step_id,
            "METADATA": {"source": "bpmn", "bpmn_process_id": process.process_id, "version": process.version},
        }

    def xǁBPMNToWorkflowConverterǁconvert__mutmut_41(self, process: BPMNProcess) -> dict[str, Any]:
        """Convert a BPMNProcess to a Zenic-Flijo workflow definition."""
        steps = []
        step_id_map: dict[str, str] = {}

        for element in process.elements.values():
            step = self._element_to_step(element, process)
            if step:
                step_id_map[element.element_id] = step["id"]
                steps.append(step)

        for flow in process.flows.values():
            source_step_id = step_id_map.get(flow.source_ref)
            target_step_id = step_id_map.get(flow.target_ref)
            if source_step_id and target_step_id:
                self._update_next_steps(steps, source_step_id, target_step_id, flow)

        start_events = process.get_start_events()
        entry_step_id = step_id_map.get(start_events[0].element_id) if start_events else None

        return {
            "name": process.name or process.process_id,
            "description": process.documentation or f"BPMN Process: {process.name}",
            "steps": steps,
            "entry_step_id": entry_step_id,
            "metadata": {"XXsourceXX": "bpmn", "bpmn_process_id": process.process_id, "version": process.version},
        }

    def xǁBPMNToWorkflowConverterǁconvert__mutmut_42(self, process: BPMNProcess) -> dict[str, Any]:
        """Convert a BPMNProcess to a Zenic-Flijo workflow definition."""
        steps = []
        step_id_map: dict[str, str] = {}

        for element in process.elements.values():
            step = self._element_to_step(element, process)
            if step:
                step_id_map[element.element_id] = step["id"]
                steps.append(step)

        for flow in process.flows.values():
            source_step_id = step_id_map.get(flow.source_ref)
            target_step_id = step_id_map.get(flow.target_ref)
            if source_step_id and target_step_id:
                self._update_next_steps(steps, source_step_id, target_step_id, flow)

        start_events = process.get_start_events()
        entry_step_id = step_id_map.get(start_events[0].element_id) if start_events else None

        return {
            "name": process.name or process.process_id,
            "description": process.documentation or f"BPMN Process: {process.name}",
            "steps": steps,
            "entry_step_id": entry_step_id,
            "metadata": {"SOURCE": "bpmn", "bpmn_process_id": process.process_id, "version": process.version},
        }

    def xǁBPMNToWorkflowConverterǁconvert__mutmut_43(self, process: BPMNProcess) -> dict[str, Any]:
        """Convert a BPMNProcess to a Zenic-Flijo workflow definition."""
        steps = []
        step_id_map: dict[str, str] = {}

        for element in process.elements.values():
            step = self._element_to_step(element, process)
            if step:
                step_id_map[element.element_id] = step["id"]
                steps.append(step)

        for flow in process.flows.values():
            source_step_id = step_id_map.get(flow.source_ref)
            target_step_id = step_id_map.get(flow.target_ref)
            if source_step_id and target_step_id:
                self._update_next_steps(steps, source_step_id, target_step_id, flow)

        start_events = process.get_start_events()
        entry_step_id = step_id_map.get(start_events[0].element_id) if start_events else None

        return {
            "name": process.name or process.process_id,
            "description": process.documentation or f"BPMN Process: {process.name}",
            "steps": steps,
            "entry_step_id": entry_step_id,
            "metadata": {"source": "XXbpmnXX", "bpmn_process_id": process.process_id, "version": process.version},
        }

    def xǁBPMNToWorkflowConverterǁconvert__mutmut_44(self, process: BPMNProcess) -> dict[str, Any]:
        """Convert a BPMNProcess to a Zenic-Flijo workflow definition."""
        steps = []
        step_id_map: dict[str, str] = {}

        for element in process.elements.values():
            step = self._element_to_step(element, process)
            if step:
                step_id_map[element.element_id] = step["id"]
                steps.append(step)

        for flow in process.flows.values():
            source_step_id = step_id_map.get(flow.source_ref)
            target_step_id = step_id_map.get(flow.target_ref)
            if source_step_id and target_step_id:
                self._update_next_steps(steps, source_step_id, target_step_id, flow)

        start_events = process.get_start_events()
        entry_step_id = step_id_map.get(start_events[0].element_id) if start_events else None

        return {
            "name": process.name or process.process_id,
            "description": process.documentation or f"BPMN Process: {process.name}",
            "steps": steps,
            "entry_step_id": entry_step_id,
            "metadata": {"source": "BPMN", "bpmn_process_id": process.process_id, "version": process.version},
        }

    def xǁBPMNToWorkflowConverterǁconvert__mutmut_45(self, process: BPMNProcess) -> dict[str, Any]:
        """Convert a BPMNProcess to a Zenic-Flijo workflow definition."""
        steps = []
        step_id_map: dict[str, str] = {}

        for element in process.elements.values():
            step = self._element_to_step(element, process)
            if step:
                step_id_map[element.element_id] = step["id"]
                steps.append(step)

        for flow in process.flows.values():
            source_step_id = step_id_map.get(flow.source_ref)
            target_step_id = step_id_map.get(flow.target_ref)
            if source_step_id and target_step_id:
                self._update_next_steps(steps, source_step_id, target_step_id, flow)

        start_events = process.get_start_events()
        entry_step_id = step_id_map.get(start_events[0].element_id) if start_events else None

        return {
            "name": process.name or process.process_id,
            "description": process.documentation or f"BPMN Process: {process.name}",
            "steps": steps,
            "entry_step_id": entry_step_id,
            "metadata": {"source": "bpmn", "XXbpmn_process_idXX": process.process_id, "version": process.version},
        }

    def xǁBPMNToWorkflowConverterǁconvert__mutmut_46(self, process: BPMNProcess) -> dict[str, Any]:
        """Convert a BPMNProcess to a Zenic-Flijo workflow definition."""
        steps = []
        step_id_map: dict[str, str] = {}

        for element in process.elements.values():
            step = self._element_to_step(element, process)
            if step:
                step_id_map[element.element_id] = step["id"]
                steps.append(step)

        for flow in process.flows.values():
            source_step_id = step_id_map.get(flow.source_ref)
            target_step_id = step_id_map.get(flow.target_ref)
            if source_step_id and target_step_id:
                self._update_next_steps(steps, source_step_id, target_step_id, flow)

        start_events = process.get_start_events()
        entry_step_id = step_id_map.get(start_events[0].element_id) if start_events else None

        return {
            "name": process.name or process.process_id,
            "description": process.documentation or f"BPMN Process: {process.name}",
            "steps": steps,
            "entry_step_id": entry_step_id,
            "metadata": {"source": "bpmn", "BPMN_PROCESS_ID": process.process_id, "version": process.version},
        }

    def xǁBPMNToWorkflowConverterǁconvert__mutmut_47(self, process: BPMNProcess) -> dict[str, Any]:
        """Convert a BPMNProcess to a Zenic-Flijo workflow definition."""
        steps = []
        step_id_map: dict[str, str] = {}

        for element in process.elements.values():
            step = self._element_to_step(element, process)
            if step:
                step_id_map[element.element_id] = step["id"]
                steps.append(step)

        for flow in process.flows.values():
            source_step_id = step_id_map.get(flow.source_ref)
            target_step_id = step_id_map.get(flow.target_ref)
            if source_step_id and target_step_id:
                self._update_next_steps(steps, source_step_id, target_step_id, flow)

        start_events = process.get_start_events()
        entry_step_id = step_id_map.get(start_events[0].element_id) if start_events else None

        return {
            "name": process.name or process.process_id,
            "description": process.documentation or f"BPMN Process: {process.name}",
            "steps": steps,
            "entry_step_id": entry_step_id,
            "metadata": {"source": "bpmn", "bpmn_process_id": process.process_id, "XXversionXX": process.version},
        }

    def xǁBPMNToWorkflowConverterǁconvert__mutmut_48(self, process: BPMNProcess) -> dict[str, Any]:
        """Convert a BPMNProcess to a Zenic-Flijo workflow definition."""
        steps = []
        step_id_map: dict[str, str] = {}

        for element in process.elements.values():
            step = self._element_to_step(element, process)
            if step:
                step_id_map[element.element_id] = step["id"]
                steps.append(step)

        for flow in process.flows.values():
            source_step_id = step_id_map.get(flow.source_ref)
            target_step_id = step_id_map.get(flow.target_ref)
            if source_step_id and target_step_id:
                self._update_next_steps(steps, source_step_id, target_step_id, flow)

        start_events = process.get_start_events()
        entry_step_id = step_id_map.get(start_events[0].element_id) if start_events else None

        return {
            "name": process.name or process.process_id,
            "description": process.documentation or f"BPMN Process: {process.name}",
            "steps": steps,
            "entry_step_id": entry_step_id,
            "metadata": {"source": "bpmn", "bpmn_process_id": process.process_id, "VERSION": process.version},
        }

    @_mutmut_mutated(mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut)
    def _element_to_step(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_orig(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_1(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = None
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_2(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(None)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_3(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is not None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_4(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = None

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_5(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "XXidXX": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_6(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "ID": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_7(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "XXnameXX": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_8(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "NAME": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_9(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name and element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_10(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "XXtypeXX": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_11(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "TYPE": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_12(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "XXnext_stepXX": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_13(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "NEXT_STEP": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_14(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "XXconfigXX": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_15(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "CONFIG": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_16(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type not in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_17(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = None
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_18(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["XXconfigXX"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_19(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["CONFIG"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_20(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["XXtool_typeXX"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_21(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["TOOL_TYPE"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_22(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = None
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_23(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["XXconfigXX"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_24(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["CONFIG"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_25(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["XXbpmn_task_typeXX"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_26(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["BPMN_TASK_TYPE"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_27(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type != BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_28(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = None
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_29(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["XXtypeXX"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_30(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["TYPE"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_31(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "XXconditionXX"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_32(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "CONDITION"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_33(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = None
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_34(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["XXconfigXX"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_35(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["CONFIG"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_36(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["XXgateway_typeXX"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_37(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["GATEWAY_TYPE"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_38(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "XXexclusiveXX"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_39(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "EXCLUSIVE"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_40(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type != BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_41(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = None
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_42(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["XXtypeXX"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_43(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["TYPE"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_44(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "XXforkXX"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_45(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "FORK"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_46(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = None
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_47(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["XXconfigXX"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_48(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["CONFIG"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_49(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["XXgateway_typeXX"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_50(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["GATEWAY_TYPE"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_51(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "XXparallelXX"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_52(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "PARALLEL"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_53(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type != BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_54(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = None
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_55(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["XXtypeXX"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_56(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["TYPE"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_57(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "XXtriggerXX"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_58(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "TRIGGER"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_59(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = None
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_60(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["XXconfigXX"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_61(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["CONFIG"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_62(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["XXtrigger_typeXX"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_63(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["TRIGGER_TYPE"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_64(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "XXmanualXX"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_65(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "MANUAL"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_66(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type != BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_67(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = ""
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_68(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["XXnext_stepXX"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_69(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["NEXT_STEP"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_70(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = None
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_71(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["XXconfigXX"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_72(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["CONFIG"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_73(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["XXis_terminalXX"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_74(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["IS_TERMINAL"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_75(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = False
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_76(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type != BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_77(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = None
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_78(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["XXtypeXX"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_79(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["TYPE"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_80(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "XXsubworkflowXX"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_81(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "SUBWORKFLOW"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_82(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = None

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_83(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["XXconfigXX"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_84(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["CONFIG"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_85(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["XXsubprocess_idXX"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_86(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["SUBPROCESS_ID"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_87(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get(None, "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_88(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", None)

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_89(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_90(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", )

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_91(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("XXcalledElementXX", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_92(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledelement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_93(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("CALLEDELEMENT", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_94(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "XXXX")

        if element.extensions:
            step["config"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_95(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["bpmn_extensions"] = None
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_96(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["XXconfigXX"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_97(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["CONFIG"]["bpmn_extensions"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_98(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["XXbpmn_extensionsXX"] = element.extensions
        return step

    def xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_99(self, element, process: BPMNProcess) -> dict[str, Any] | None:
        step_type = self._map_element_type(element.element_type)
        if step_type is None:
            return None

        step: dict[str, Any] = {
            "id": f"step_{element.element_id}", "name": element.name or element.element_id,
            "type": step_type, "next_step": None, "config": {},
        }

        if element.element_type in self._get_task_type_map():
            step["config"]["tool_type"] = self._get_task_type_map()[element.element_type]
            step["config"]["bpmn_task_type"] = element.element_type.value
        elif element.element_type == BPMNElementType.EXCLUSIVE_GATEWAY:
            step["type"] = "condition"
            step["config"]["gateway_type"] = "exclusive"
        elif element.element_type == BPMNElementType.PARALLEL_GATEWAY:
            step["type"] = "fork"
            step["config"]["gateway_type"] = "parallel"
        elif element.element_type == BPMNElementType.START_EVENT:
            step["type"] = "trigger"
            step["config"]["trigger_type"] = "manual"
        elif element.element_type == BPMNElementType.END_EVENT:
            step["next_step"] = None
            step["config"]["is_terminal"] = True
        elif element.element_type == BPMNElementType.SUB_PROCESS:
            step["type"] = "subworkflow"
            step["config"]["subprocess_id"] = element.properties.get("calledElement", "")

        if element.extensions:
            step["config"]["BPMN_EXTENSIONS"] = element.extensions
        return step

    @staticmethod
    @_mutmut_mutated(mutants_xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut)
    def _map_element_type(element_type: BPMNElementType) -> str | None:
        mapping = {
            BPMNElementType.START_EVENT: "trigger",
            BPMNElementType.END_EVENT: "output",
            BPMNElementType.USER_TASK: "input",
            BPMNElementType.SERVICE_TASK: "api_call",
            BPMNElementType.SCRIPT_TASK: "code_runner",
            BPMNElementType.MANUAL_TASK: "notification",
            BPMNElementType.EXCLUSIVE_GATEWAY: "condition",
            BPMNElementType.PARALLEL_GATEWAY: "fork",
            BPMNElementType.INCLUSIVE_GATEWAY: "condition",
            BPMNElementType.SUB_PROCESS: "subworkflow",
            BPMNElementType.CALL_ACTIVITY: "subworkflow",
            BPMNElementType.INTERMEDIATE_CATCH_EVENT: "webhook",
            BPMNElementType.INTERMEDIATE_THROW_EVENT: "notification",
        }
        return mapping.get(element_type)

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_orig(element_type: BPMNElementType) -> str | None:
        mapping = {
            BPMNElementType.START_EVENT: "trigger",
            BPMNElementType.END_EVENT: "output",
            BPMNElementType.USER_TASK: "input",
            BPMNElementType.SERVICE_TASK: "api_call",
            BPMNElementType.SCRIPT_TASK: "code_runner",
            BPMNElementType.MANUAL_TASK: "notification",
            BPMNElementType.EXCLUSIVE_GATEWAY: "condition",
            BPMNElementType.PARALLEL_GATEWAY: "fork",
            BPMNElementType.INCLUSIVE_GATEWAY: "condition",
            BPMNElementType.SUB_PROCESS: "subworkflow",
            BPMNElementType.CALL_ACTIVITY: "subworkflow",
            BPMNElementType.INTERMEDIATE_CATCH_EVENT: "webhook",
            BPMNElementType.INTERMEDIATE_THROW_EVENT: "notification",
        }
        return mapping.get(element_type)

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_1(element_type: BPMNElementType) -> str | None:
        mapping = None
        return mapping.get(element_type)

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_2(element_type: BPMNElementType) -> str | None:
        mapping = {
            BPMNElementType.START_EVENT: "XXtriggerXX",
            BPMNElementType.END_EVENT: "output",
            BPMNElementType.USER_TASK: "input",
            BPMNElementType.SERVICE_TASK: "api_call",
            BPMNElementType.SCRIPT_TASK: "code_runner",
            BPMNElementType.MANUAL_TASK: "notification",
            BPMNElementType.EXCLUSIVE_GATEWAY: "condition",
            BPMNElementType.PARALLEL_GATEWAY: "fork",
            BPMNElementType.INCLUSIVE_GATEWAY: "condition",
            BPMNElementType.SUB_PROCESS: "subworkflow",
            BPMNElementType.CALL_ACTIVITY: "subworkflow",
            BPMNElementType.INTERMEDIATE_CATCH_EVENT: "webhook",
            BPMNElementType.INTERMEDIATE_THROW_EVENT: "notification",
        }
        return mapping.get(element_type)

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_3(element_type: BPMNElementType) -> str | None:
        mapping = {
            BPMNElementType.START_EVENT: "TRIGGER",
            BPMNElementType.END_EVENT: "output",
            BPMNElementType.USER_TASK: "input",
            BPMNElementType.SERVICE_TASK: "api_call",
            BPMNElementType.SCRIPT_TASK: "code_runner",
            BPMNElementType.MANUAL_TASK: "notification",
            BPMNElementType.EXCLUSIVE_GATEWAY: "condition",
            BPMNElementType.PARALLEL_GATEWAY: "fork",
            BPMNElementType.INCLUSIVE_GATEWAY: "condition",
            BPMNElementType.SUB_PROCESS: "subworkflow",
            BPMNElementType.CALL_ACTIVITY: "subworkflow",
            BPMNElementType.INTERMEDIATE_CATCH_EVENT: "webhook",
            BPMNElementType.INTERMEDIATE_THROW_EVENT: "notification",
        }
        return mapping.get(element_type)

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_4(element_type: BPMNElementType) -> str | None:
        mapping = {
            BPMNElementType.START_EVENT: "trigger",
            BPMNElementType.END_EVENT: "XXoutputXX",
            BPMNElementType.USER_TASK: "input",
            BPMNElementType.SERVICE_TASK: "api_call",
            BPMNElementType.SCRIPT_TASK: "code_runner",
            BPMNElementType.MANUAL_TASK: "notification",
            BPMNElementType.EXCLUSIVE_GATEWAY: "condition",
            BPMNElementType.PARALLEL_GATEWAY: "fork",
            BPMNElementType.INCLUSIVE_GATEWAY: "condition",
            BPMNElementType.SUB_PROCESS: "subworkflow",
            BPMNElementType.CALL_ACTIVITY: "subworkflow",
            BPMNElementType.INTERMEDIATE_CATCH_EVENT: "webhook",
            BPMNElementType.INTERMEDIATE_THROW_EVENT: "notification",
        }
        return mapping.get(element_type)

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_5(element_type: BPMNElementType) -> str | None:
        mapping = {
            BPMNElementType.START_EVENT: "trigger",
            BPMNElementType.END_EVENT: "OUTPUT",
            BPMNElementType.USER_TASK: "input",
            BPMNElementType.SERVICE_TASK: "api_call",
            BPMNElementType.SCRIPT_TASK: "code_runner",
            BPMNElementType.MANUAL_TASK: "notification",
            BPMNElementType.EXCLUSIVE_GATEWAY: "condition",
            BPMNElementType.PARALLEL_GATEWAY: "fork",
            BPMNElementType.INCLUSIVE_GATEWAY: "condition",
            BPMNElementType.SUB_PROCESS: "subworkflow",
            BPMNElementType.CALL_ACTIVITY: "subworkflow",
            BPMNElementType.INTERMEDIATE_CATCH_EVENT: "webhook",
            BPMNElementType.INTERMEDIATE_THROW_EVENT: "notification",
        }
        return mapping.get(element_type)

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_6(element_type: BPMNElementType) -> str | None:
        mapping = {
            BPMNElementType.START_EVENT: "trigger",
            BPMNElementType.END_EVENT: "output",
            BPMNElementType.USER_TASK: "XXinputXX",
            BPMNElementType.SERVICE_TASK: "api_call",
            BPMNElementType.SCRIPT_TASK: "code_runner",
            BPMNElementType.MANUAL_TASK: "notification",
            BPMNElementType.EXCLUSIVE_GATEWAY: "condition",
            BPMNElementType.PARALLEL_GATEWAY: "fork",
            BPMNElementType.INCLUSIVE_GATEWAY: "condition",
            BPMNElementType.SUB_PROCESS: "subworkflow",
            BPMNElementType.CALL_ACTIVITY: "subworkflow",
            BPMNElementType.INTERMEDIATE_CATCH_EVENT: "webhook",
            BPMNElementType.INTERMEDIATE_THROW_EVENT: "notification",
        }
        return mapping.get(element_type)

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_7(element_type: BPMNElementType) -> str | None:
        mapping = {
            BPMNElementType.START_EVENT: "trigger",
            BPMNElementType.END_EVENT: "output",
            BPMNElementType.USER_TASK: "INPUT",
            BPMNElementType.SERVICE_TASK: "api_call",
            BPMNElementType.SCRIPT_TASK: "code_runner",
            BPMNElementType.MANUAL_TASK: "notification",
            BPMNElementType.EXCLUSIVE_GATEWAY: "condition",
            BPMNElementType.PARALLEL_GATEWAY: "fork",
            BPMNElementType.INCLUSIVE_GATEWAY: "condition",
            BPMNElementType.SUB_PROCESS: "subworkflow",
            BPMNElementType.CALL_ACTIVITY: "subworkflow",
            BPMNElementType.INTERMEDIATE_CATCH_EVENT: "webhook",
            BPMNElementType.INTERMEDIATE_THROW_EVENT: "notification",
        }
        return mapping.get(element_type)

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_8(element_type: BPMNElementType) -> str | None:
        mapping = {
            BPMNElementType.START_EVENT: "trigger",
            BPMNElementType.END_EVENT: "output",
            BPMNElementType.USER_TASK: "input",
            BPMNElementType.SERVICE_TASK: "XXapi_callXX",
            BPMNElementType.SCRIPT_TASK: "code_runner",
            BPMNElementType.MANUAL_TASK: "notification",
            BPMNElementType.EXCLUSIVE_GATEWAY: "condition",
            BPMNElementType.PARALLEL_GATEWAY: "fork",
            BPMNElementType.INCLUSIVE_GATEWAY: "condition",
            BPMNElementType.SUB_PROCESS: "subworkflow",
            BPMNElementType.CALL_ACTIVITY: "subworkflow",
            BPMNElementType.INTERMEDIATE_CATCH_EVENT: "webhook",
            BPMNElementType.INTERMEDIATE_THROW_EVENT: "notification",
        }
        return mapping.get(element_type)

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_9(element_type: BPMNElementType) -> str | None:
        mapping = {
            BPMNElementType.START_EVENT: "trigger",
            BPMNElementType.END_EVENT: "output",
            BPMNElementType.USER_TASK: "input",
            BPMNElementType.SERVICE_TASK: "API_CALL",
            BPMNElementType.SCRIPT_TASK: "code_runner",
            BPMNElementType.MANUAL_TASK: "notification",
            BPMNElementType.EXCLUSIVE_GATEWAY: "condition",
            BPMNElementType.PARALLEL_GATEWAY: "fork",
            BPMNElementType.INCLUSIVE_GATEWAY: "condition",
            BPMNElementType.SUB_PROCESS: "subworkflow",
            BPMNElementType.CALL_ACTIVITY: "subworkflow",
            BPMNElementType.INTERMEDIATE_CATCH_EVENT: "webhook",
            BPMNElementType.INTERMEDIATE_THROW_EVENT: "notification",
        }
        return mapping.get(element_type)

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_10(element_type: BPMNElementType) -> str | None:
        mapping = {
            BPMNElementType.START_EVENT: "trigger",
            BPMNElementType.END_EVENT: "output",
            BPMNElementType.USER_TASK: "input",
            BPMNElementType.SERVICE_TASK: "api_call",
            BPMNElementType.SCRIPT_TASK: "XXcode_runnerXX",
            BPMNElementType.MANUAL_TASK: "notification",
            BPMNElementType.EXCLUSIVE_GATEWAY: "condition",
            BPMNElementType.PARALLEL_GATEWAY: "fork",
            BPMNElementType.INCLUSIVE_GATEWAY: "condition",
            BPMNElementType.SUB_PROCESS: "subworkflow",
            BPMNElementType.CALL_ACTIVITY: "subworkflow",
            BPMNElementType.INTERMEDIATE_CATCH_EVENT: "webhook",
            BPMNElementType.INTERMEDIATE_THROW_EVENT: "notification",
        }
        return mapping.get(element_type)

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_11(element_type: BPMNElementType) -> str | None:
        mapping = {
            BPMNElementType.START_EVENT: "trigger",
            BPMNElementType.END_EVENT: "output",
            BPMNElementType.USER_TASK: "input",
            BPMNElementType.SERVICE_TASK: "api_call",
            BPMNElementType.SCRIPT_TASK: "CODE_RUNNER",
            BPMNElementType.MANUAL_TASK: "notification",
            BPMNElementType.EXCLUSIVE_GATEWAY: "condition",
            BPMNElementType.PARALLEL_GATEWAY: "fork",
            BPMNElementType.INCLUSIVE_GATEWAY: "condition",
            BPMNElementType.SUB_PROCESS: "subworkflow",
            BPMNElementType.CALL_ACTIVITY: "subworkflow",
            BPMNElementType.INTERMEDIATE_CATCH_EVENT: "webhook",
            BPMNElementType.INTERMEDIATE_THROW_EVENT: "notification",
        }
        return mapping.get(element_type)

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_12(element_type: BPMNElementType) -> str | None:
        mapping = {
            BPMNElementType.START_EVENT: "trigger",
            BPMNElementType.END_EVENT: "output",
            BPMNElementType.USER_TASK: "input",
            BPMNElementType.SERVICE_TASK: "api_call",
            BPMNElementType.SCRIPT_TASK: "code_runner",
            BPMNElementType.MANUAL_TASK: "XXnotificationXX",
            BPMNElementType.EXCLUSIVE_GATEWAY: "condition",
            BPMNElementType.PARALLEL_GATEWAY: "fork",
            BPMNElementType.INCLUSIVE_GATEWAY: "condition",
            BPMNElementType.SUB_PROCESS: "subworkflow",
            BPMNElementType.CALL_ACTIVITY: "subworkflow",
            BPMNElementType.INTERMEDIATE_CATCH_EVENT: "webhook",
            BPMNElementType.INTERMEDIATE_THROW_EVENT: "notification",
        }
        return mapping.get(element_type)

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_13(element_type: BPMNElementType) -> str | None:
        mapping = {
            BPMNElementType.START_EVENT: "trigger",
            BPMNElementType.END_EVENT: "output",
            BPMNElementType.USER_TASK: "input",
            BPMNElementType.SERVICE_TASK: "api_call",
            BPMNElementType.SCRIPT_TASK: "code_runner",
            BPMNElementType.MANUAL_TASK: "NOTIFICATION",
            BPMNElementType.EXCLUSIVE_GATEWAY: "condition",
            BPMNElementType.PARALLEL_GATEWAY: "fork",
            BPMNElementType.INCLUSIVE_GATEWAY: "condition",
            BPMNElementType.SUB_PROCESS: "subworkflow",
            BPMNElementType.CALL_ACTIVITY: "subworkflow",
            BPMNElementType.INTERMEDIATE_CATCH_EVENT: "webhook",
            BPMNElementType.INTERMEDIATE_THROW_EVENT: "notification",
        }
        return mapping.get(element_type)

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_14(element_type: BPMNElementType) -> str | None:
        mapping = {
            BPMNElementType.START_EVENT: "trigger",
            BPMNElementType.END_EVENT: "output",
            BPMNElementType.USER_TASK: "input",
            BPMNElementType.SERVICE_TASK: "api_call",
            BPMNElementType.SCRIPT_TASK: "code_runner",
            BPMNElementType.MANUAL_TASK: "notification",
            BPMNElementType.EXCLUSIVE_GATEWAY: "XXconditionXX",
            BPMNElementType.PARALLEL_GATEWAY: "fork",
            BPMNElementType.INCLUSIVE_GATEWAY: "condition",
            BPMNElementType.SUB_PROCESS: "subworkflow",
            BPMNElementType.CALL_ACTIVITY: "subworkflow",
            BPMNElementType.INTERMEDIATE_CATCH_EVENT: "webhook",
            BPMNElementType.INTERMEDIATE_THROW_EVENT: "notification",
        }
        return mapping.get(element_type)

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_15(element_type: BPMNElementType) -> str | None:
        mapping = {
            BPMNElementType.START_EVENT: "trigger",
            BPMNElementType.END_EVENT: "output",
            BPMNElementType.USER_TASK: "input",
            BPMNElementType.SERVICE_TASK: "api_call",
            BPMNElementType.SCRIPT_TASK: "code_runner",
            BPMNElementType.MANUAL_TASK: "notification",
            BPMNElementType.EXCLUSIVE_GATEWAY: "CONDITION",
            BPMNElementType.PARALLEL_GATEWAY: "fork",
            BPMNElementType.INCLUSIVE_GATEWAY: "condition",
            BPMNElementType.SUB_PROCESS: "subworkflow",
            BPMNElementType.CALL_ACTIVITY: "subworkflow",
            BPMNElementType.INTERMEDIATE_CATCH_EVENT: "webhook",
            BPMNElementType.INTERMEDIATE_THROW_EVENT: "notification",
        }
        return mapping.get(element_type)

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_16(element_type: BPMNElementType) -> str | None:
        mapping = {
            BPMNElementType.START_EVENT: "trigger",
            BPMNElementType.END_EVENT: "output",
            BPMNElementType.USER_TASK: "input",
            BPMNElementType.SERVICE_TASK: "api_call",
            BPMNElementType.SCRIPT_TASK: "code_runner",
            BPMNElementType.MANUAL_TASK: "notification",
            BPMNElementType.EXCLUSIVE_GATEWAY: "condition",
            BPMNElementType.PARALLEL_GATEWAY: "XXforkXX",
            BPMNElementType.INCLUSIVE_GATEWAY: "condition",
            BPMNElementType.SUB_PROCESS: "subworkflow",
            BPMNElementType.CALL_ACTIVITY: "subworkflow",
            BPMNElementType.INTERMEDIATE_CATCH_EVENT: "webhook",
            BPMNElementType.INTERMEDIATE_THROW_EVENT: "notification",
        }
        return mapping.get(element_type)

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_17(element_type: BPMNElementType) -> str | None:
        mapping = {
            BPMNElementType.START_EVENT: "trigger",
            BPMNElementType.END_EVENT: "output",
            BPMNElementType.USER_TASK: "input",
            BPMNElementType.SERVICE_TASK: "api_call",
            BPMNElementType.SCRIPT_TASK: "code_runner",
            BPMNElementType.MANUAL_TASK: "notification",
            BPMNElementType.EXCLUSIVE_GATEWAY: "condition",
            BPMNElementType.PARALLEL_GATEWAY: "FORK",
            BPMNElementType.INCLUSIVE_GATEWAY: "condition",
            BPMNElementType.SUB_PROCESS: "subworkflow",
            BPMNElementType.CALL_ACTIVITY: "subworkflow",
            BPMNElementType.INTERMEDIATE_CATCH_EVENT: "webhook",
            BPMNElementType.INTERMEDIATE_THROW_EVENT: "notification",
        }
        return mapping.get(element_type)

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_18(element_type: BPMNElementType) -> str | None:
        mapping = {
            BPMNElementType.START_EVENT: "trigger",
            BPMNElementType.END_EVENT: "output",
            BPMNElementType.USER_TASK: "input",
            BPMNElementType.SERVICE_TASK: "api_call",
            BPMNElementType.SCRIPT_TASK: "code_runner",
            BPMNElementType.MANUAL_TASK: "notification",
            BPMNElementType.EXCLUSIVE_GATEWAY: "condition",
            BPMNElementType.PARALLEL_GATEWAY: "fork",
            BPMNElementType.INCLUSIVE_GATEWAY: "XXconditionXX",
            BPMNElementType.SUB_PROCESS: "subworkflow",
            BPMNElementType.CALL_ACTIVITY: "subworkflow",
            BPMNElementType.INTERMEDIATE_CATCH_EVENT: "webhook",
            BPMNElementType.INTERMEDIATE_THROW_EVENT: "notification",
        }
        return mapping.get(element_type)

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_19(element_type: BPMNElementType) -> str | None:
        mapping = {
            BPMNElementType.START_EVENT: "trigger",
            BPMNElementType.END_EVENT: "output",
            BPMNElementType.USER_TASK: "input",
            BPMNElementType.SERVICE_TASK: "api_call",
            BPMNElementType.SCRIPT_TASK: "code_runner",
            BPMNElementType.MANUAL_TASK: "notification",
            BPMNElementType.EXCLUSIVE_GATEWAY: "condition",
            BPMNElementType.PARALLEL_GATEWAY: "fork",
            BPMNElementType.INCLUSIVE_GATEWAY: "CONDITION",
            BPMNElementType.SUB_PROCESS: "subworkflow",
            BPMNElementType.CALL_ACTIVITY: "subworkflow",
            BPMNElementType.INTERMEDIATE_CATCH_EVENT: "webhook",
            BPMNElementType.INTERMEDIATE_THROW_EVENT: "notification",
        }
        return mapping.get(element_type)

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_20(element_type: BPMNElementType) -> str | None:
        mapping = {
            BPMNElementType.START_EVENT: "trigger",
            BPMNElementType.END_EVENT: "output",
            BPMNElementType.USER_TASK: "input",
            BPMNElementType.SERVICE_TASK: "api_call",
            BPMNElementType.SCRIPT_TASK: "code_runner",
            BPMNElementType.MANUAL_TASK: "notification",
            BPMNElementType.EXCLUSIVE_GATEWAY: "condition",
            BPMNElementType.PARALLEL_GATEWAY: "fork",
            BPMNElementType.INCLUSIVE_GATEWAY: "condition",
            BPMNElementType.SUB_PROCESS: "XXsubworkflowXX",
            BPMNElementType.CALL_ACTIVITY: "subworkflow",
            BPMNElementType.INTERMEDIATE_CATCH_EVENT: "webhook",
            BPMNElementType.INTERMEDIATE_THROW_EVENT: "notification",
        }
        return mapping.get(element_type)

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_21(element_type: BPMNElementType) -> str | None:
        mapping = {
            BPMNElementType.START_EVENT: "trigger",
            BPMNElementType.END_EVENT: "output",
            BPMNElementType.USER_TASK: "input",
            BPMNElementType.SERVICE_TASK: "api_call",
            BPMNElementType.SCRIPT_TASK: "code_runner",
            BPMNElementType.MANUAL_TASK: "notification",
            BPMNElementType.EXCLUSIVE_GATEWAY: "condition",
            BPMNElementType.PARALLEL_GATEWAY: "fork",
            BPMNElementType.INCLUSIVE_GATEWAY: "condition",
            BPMNElementType.SUB_PROCESS: "SUBWORKFLOW",
            BPMNElementType.CALL_ACTIVITY: "subworkflow",
            BPMNElementType.INTERMEDIATE_CATCH_EVENT: "webhook",
            BPMNElementType.INTERMEDIATE_THROW_EVENT: "notification",
        }
        return mapping.get(element_type)

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_22(element_type: BPMNElementType) -> str | None:
        mapping = {
            BPMNElementType.START_EVENT: "trigger",
            BPMNElementType.END_EVENT: "output",
            BPMNElementType.USER_TASK: "input",
            BPMNElementType.SERVICE_TASK: "api_call",
            BPMNElementType.SCRIPT_TASK: "code_runner",
            BPMNElementType.MANUAL_TASK: "notification",
            BPMNElementType.EXCLUSIVE_GATEWAY: "condition",
            BPMNElementType.PARALLEL_GATEWAY: "fork",
            BPMNElementType.INCLUSIVE_GATEWAY: "condition",
            BPMNElementType.SUB_PROCESS: "subworkflow",
            BPMNElementType.CALL_ACTIVITY: "XXsubworkflowXX",
            BPMNElementType.INTERMEDIATE_CATCH_EVENT: "webhook",
            BPMNElementType.INTERMEDIATE_THROW_EVENT: "notification",
        }
        return mapping.get(element_type)

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_23(element_type: BPMNElementType) -> str | None:
        mapping = {
            BPMNElementType.START_EVENT: "trigger",
            BPMNElementType.END_EVENT: "output",
            BPMNElementType.USER_TASK: "input",
            BPMNElementType.SERVICE_TASK: "api_call",
            BPMNElementType.SCRIPT_TASK: "code_runner",
            BPMNElementType.MANUAL_TASK: "notification",
            BPMNElementType.EXCLUSIVE_GATEWAY: "condition",
            BPMNElementType.PARALLEL_GATEWAY: "fork",
            BPMNElementType.INCLUSIVE_GATEWAY: "condition",
            BPMNElementType.SUB_PROCESS: "subworkflow",
            BPMNElementType.CALL_ACTIVITY: "SUBWORKFLOW",
            BPMNElementType.INTERMEDIATE_CATCH_EVENT: "webhook",
            BPMNElementType.INTERMEDIATE_THROW_EVENT: "notification",
        }
        return mapping.get(element_type)

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_24(element_type: BPMNElementType) -> str | None:
        mapping = {
            BPMNElementType.START_EVENT: "trigger",
            BPMNElementType.END_EVENT: "output",
            BPMNElementType.USER_TASK: "input",
            BPMNElementType.SERVICE_TASK: "api_call",
            BPMNElementType.SCRIPT_TASK: "code_runner",
            BPMNElementType.MANUAL_TASK: "notification",
            BPMNElementType.EXCLUSIVE_GATEWAY: "condition",
            BPMNElementType.PARALLEL_GATEWAY: "fork",
            BPMNElementType.INCLUSIVE_GATEWAY: "condition",
            BPMNElementType.SUB_PROCESS: "subworkflow",
            BPMNElementType.CALL_ACTIVITY: "subworkflow",
            BPMNElementType.INTERMEDIATE_CATCH_EVENT: "XXwebhookXX",
            BPMNElementType.INTERMEDIATE_THROW_EVENT: "notification",
        }
        return mapping.get(element_type)

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_25(element_type: BPMNElementType) -> str | None:
        mapping = {
            BPMNElementType.START_EVENT: "trigger",
            BPMNElementType.END_EVENT: "output",
            BPMNElementType.USER_TASK: "input",
            BPMNElementType.SERVICE_TASK: "api_call",
            BPMNElementType.SCRIPT_TASK: "code_runner",
            BPMNElementType.MANUAL_TASK: "notification",
            BPMNElementType.EXCLUSIVE_GATEWAY: "condition",
            BPMNElementType.PARALLEL_GATEWAY: "fork",
            BPMNElementType.INCLUSIVE_GATEWAY: "condition",
            BPMNElementType.SUB_PROCESS: "subworkflow",
            BPMNElementType.CALL_ACTIVITY: "subworkflow",
            BPMNElementType.INTERMEDIATE_CATCH_EVENT: "WEBHOOK",
            BPMNElementType.INTERMEDIATE_THROW_EVENT: "notification",
        }
        return mapping.get(element_type)

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_26(element_type: BPMNElementType) -> str | None:
        mapping = {
            BPMNElementType.START_EVENT: "trigger",
            BPMNElementType.END_EVENT: "output",
            BPMNElementType.USER_TASK: "input",
            BPMNElementType.SERVICE_TASK: "api_call",
            BPMNElementType.SCRIPT_TASK: "code_runner",
            BPMNElementType.MANUAL_TASK: "notification",
            BPMNElementType.EXCLUSIVE_GATEWAY: "condition",
            BPMNElementType.PARALLEL_GATEWAY: "fork",
            BPMNElementType.INCLUSIVE_GATEWAY: "condition",
            BPMNElementType.SUB_PROCESS: "subworkflow",
            BPMNElementType.CALL_ACTIVITY: "subworkflow",
            BPMNElementType.INTERMEDIATE_CATCH_EVENT: "webhook",
            BPMNElementType.INTERMEDIATE_THROW_EVENT: "XXnotificationXX",
        }
        return mapping.get(element_type)

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_27(element_type: BPMNElementType) -> str | None:
        mapping = {
            BPMNElementType.START_EVENT: "trigger",
            BPMNElementType.END_EVENT: "output",
            BPMNElementType.USER_TASK: "input",
            BPMNElementType.SERVICE_TASK: "api_call",
            BPMNElementType.SCRIPT_TASK: "code_runner",
            BPMNElementType.MANUAL_TASK: "notification",
            BPMNElementType.EXCLUSIVE_GATEWAY: "condition",
            BPMNElementType.PARALLEL_GATEWAY: "fork",
            BPMNElementType.INCLUSIVE_GATEWAY: "condition",
            BPMNElementType.SUB_PROCESS: "subworkflow",
            BPMNElementType.CALL_ACTIVITY: "subworkflow",
            BPMNElementType.INTERMEDIATE_CATCH_EVENT: "webhook",
            BPMNElementType.INTERMEDIATE_THROW_EVENT: "NOTIFICATION",
        }
        return mapping.get(element_type)

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_28(element_type: BPMNElementType) -> str | None:
        mapping = {
            BPMNElementType.START_EVENT: "trigger",
            BPMNElementType.END_EVENT: "output",
            BPMNElementType.USER_TASK: "input",
            BPMNElementType.SERVICE_TASK: "api_call",
            BPMNElementType.SCRIPT_TASK: "code_runner",
            BPMNElementType.MANUAL_TASK: "notification",
            BPMNElementType.EXCLUSIVE_GATEWAY: "condition",
            BPMNElementType.PARALLEL_GATEWAY: "fork",
            BPMNElementType.INCLUSIVE_GATEWAY: "condition",
            BPMNElementType.SUB_PROCESS: "subworkflow",
            BPMNElementType.CALL_ACTIVITY: "subworkflow",
            BPMNElementType.INTERMEDIATE_CATCH_EVENT: "webhook",
            BPMNElementType.INTERMEDIATE_THROW_EVENT: "notification",
        }
        return mapping.get(None)

    @staticmethod
    @_mutmut_mutated(mutants_xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut)
    def _update_next_steps(steps: list[dict[str, Any]], source_step_id: str, target_step_id: str, flow) -> None:
        for step in steps:
            if step["id"] == source_step_id:
                if step["type"] in ("condition", "fork"):
                    if "branches" not in step:
                        step["branches"] = []
                    step["branches"].append({
                        "next_step": target_step_id,
                        "condition": flow.condition_expression or "",
                        "label": flow.name or f"Branch {len(step['branches']) + 1}",
                    })
                else:
                    if step.get("next_step") is None or step["type"] == "output":
                        step["next_step"] = target_step_id
                break

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_orig(steps: list[dict[str, Any]], source_step_id: str, target_step_id: str, flow) -> None:
        for step in steps:
            if step["id"] == source_step_id:
                if step["type"] in ("condition", "fork"):
                    if "branches" not in step:
                        step["branches"] = []
                    step["branches"].append({
                        "next_step": target_step_id,
                        "condition": flow.condition_expression or "",
                        "label": flow.name or f"Branch {len(step['branches']) + 1}",
                    })
                else:
                    if step.get("next_step") is None or step["type"] == "output":
                        step["next_step"] = target_step_id
                break

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_1(steps: list[dict[str, Any]], source_step_id: str, target_step_id: str, flow) -> None:
        for step in steps:
            if step["XXidXX"] == source_step_id:
                if step["type"] in ("condition", "fork"):
                    if "branches" not in step:
                        step["branches"] = []
                    step["branches"].append({
                        "next_step": target_step_id,
                        "condition": flow.condition_expression or "",
                        "label": flow.name or f"Branch {len(step['branches']) + 1}",
                    })
                else:
                    if step.get("next_step") is None or step["type"] == "output":
                        step["next_step"] = target_step_id
                break

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_2(steps: list[dict[str, Any]], source_step_id: str, target_step_id: str, flow) -> None:
        for step in steps:
            if step["ID"] == source_step_id:
                if step["type"] in ("condition", "fork"):
                    if "branches" not in step:
                        step["branches"] = []
                    step["branches"].append({
                        "next_step": target_step_id,
                        "condition": flow.condition_expression or "",
                        "label": flow.name or f"Branch {len(step['branches']) + 1}",
                    })
                else:
                    if step.get("next_step") is None or step["type"] == "output":
                        step["next_step"] = target_step_id
                break

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_3(steps: list[dict[str, Any]], source_step_id: str, target_step_id: str, flow) -> None:
        for step in steps:
            if step["id"] != source_step_id:
                if step["type"] in ("condition", "fork"):
                    if "branches" not in step:
                        step["branches"] = []
                    step["branches"].append({
                        "next_step": target_step_id,
                        "condition": flow.condition_expression or "",
                        "label": flow.name or f"Branch {len(step['branches']) + 1}",
                    })
                else:
                    if step.get("next_step") is None or step["type"] == "output":
                        step["next_step"] = target_step_id
                break

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_4(steps: list[dict[str, Any]], source_step_id: str, target_step_id: str, flow) -> None:
        for step in steps:
            if step["id"] == source_step_id:
                if step["XXtypeXX"] in ("condition", "fork"):
                    if "branches" not in step:
                        step["branches"] = []
                    step["branches"].append({
                        "next_step": target_step_id,
                        "condition": flow.condition_expression or "",
                        "label": flow.name or f"Branch {len(step['branches']) + 1}",
                    })
                else:
                    if step.get("next_step") is None or step["type"] == "output":
                        step["next_step"] = target_step_id
                break

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_5(steps: list[dict[str, Any]], source_step_id: str, target_step_id: str, flow) -> None:
        for step in steps:
            if step["id"] == source_step_id:
                if step["TYPE"] in ("condition", "fork"):
                    if "branches" not in step:
                        step["branches"] = []
                    step["branches"].append({
                        "next_step": target_step_id,
                        "condition": flow.condition_expression or "",
                        "label": flow.name or f"Branch {len(step['branches']) + 1}",
                    })
                else:
                    if step.get("next_step") is None or step["type"] == "output":
                        step["next_step"] = target_step_id
                break

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_6(steps: list[dict[str, Any]], source_step_id: str, target_step_id: str, flow) -> None:
        for step in steps:
            if step["id"] == source_step_id:
                if step["type"] not in ("condition", "fork"):
                    if "branches" not in step:
                        step["branches"] = []
                    step["branches"].append({
                        "next_step": target_step_id,
                        "condition": flow.condition_expression or "",
                        "label": flow.name or f"Branch {len(step['branches']) + 1}",
                    })
                else:
                    if step.get("next_step") is None or step["type"] == "output":
                        step["next_step"] = target_step_id
                break

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_7(steps: list[dict[str, Any]], source_step_id: str, target_step_id: str, flow) -> None:
        for step in steps:
            if step["id"] == source_step_id:
                if step["type"] in ("XXconditionXX", "fork"):
                    if "branches" not in step:
                        step["branches"] = []
                    step["branches"].append({
                        "next_step": target_step_id,
                        "condition": flow.condition_expression or "",
                        "label": flow.name or f"Branch {len(step['branches']) + 1}",
                    })
                else:
                    if step.get("next_step") is None or step["type"] == "output":
                        step["next_step"] = target_step_id
                break

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_8(steps: list[dict[str, Any]], source_step_id: str, target_step_id: str, flow) -> None:
        for step in steps:
            if step["id"] == source_step_id:
                if step["type"] in ("CONDITION", "fork"):
                    if "branches" not in step:
                        step["branches"] = []
                    step["branches"].append({
                        "next_step": target_step_id,
                        "condition": flow.condition_expression or "",
                        "label": flow.name or f"Branch {len(step['branches']) + 1}",
                    })
                else:
                    if step.get("next_step") is None or step["type"] == "output":
                        step["next_step"] = target_step_id
                break

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_9(steps: list[dict[str, Any]], source_step_id: str, target_step_id: str, flow) -> None:
        for step in steps:
            if step["id"] == source_step_id:
                if step["type"] in ("condition", "XXforkXX"):
                    if "branches" not in step:
                        step["branches"] = []
                    step["branches"].append({
                        "next_step": target_step_id,
                        "condition": flow.condition_expression or "",
                        "label": flow.name or f"Branch {len(step['branches']) + 1}",
                    })
                else:
                    if step.get("next_step") is None or step["type"] == "output":
                        step["next_step"] = target_step_id
                break

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_10(steps: list[dict[str, Any]], source_step_id: str, target_step_id: str, flow) -> None:
        for step in steps:
            if step["id"] == source_step_id:
                if step["type"] in ("condition", "FORK"):
                    if "branches" not in step:
                        step["branches"] = []
                    step["branches"].append({
                        "next_step": target_step_id,
                        "condition": flow.condition_expression or "",
                        "label": flow.name or f"Branch {len(step['branches']) + 1}",
                    })
                else:
                    if step.get("next_step") is None or step["type"] == "output":
                        step["next_step"] = target_step_id
                break

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_11(steps: list[dict[str, Any]], source_step_id: str, target_step_id: str, flow) -> None:
        for step in steps:
            if step["id"] == source_step_id:
                if step["type"] in ("condition", "fork"):
                    if "XXbranchesXX" not in step:
                        step["branches"] = []
                    step["branches"].append({
                        "next_step": target_step_id,
                        "condition": flow.condition_expression or "",
                        "label": flow.name or f"Branch {len(step['branches']) + 1}",
                    })
                else:
                    if step.get("next_step") is None or step["type"] == "output":
                        step["next_step"] = target_step_id
                break

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_12(steps: list[dict[str, Any]], source_step_id: str, target_step_id: str, flow) -> None:
        for step in steps:
            if step["id"] == source_step_id:
                if step["type"] in ("condition", "fork"):
                    if "BRANCHES" not in step:
                        step["branches"] = []
                    step["branches"].append({
                        "next_step": target_step_id,
                        "condition": flow.condition_expression or "",
                        "label": flow.name or f"Branch {len(step['branches']) + 1}",
                    })
                else:
                    if step.get("next_step") is None or step["type"] == "output":
                        step["next_step"] = target_step_id
                break

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_13(steps: list[dict[str, Any]], source_step_id: str, target_step_id: str, flow) -> None:
        for step in steps:
            if step["id"] == source_step_id:
                if step["type"] in ("condition", "fork"):
                    if "branches" in step:
                        step["branches"] = []
                    step["branches"].append({
                        "next_step": target_step_id,
                        "condition": flow.condition_expression or "",
                        "label": flow.name or f"Branch {len(step['branches']) + 1}",
                    })
                else:
                    if step.get("next_step") is None or step["type"] == "output":
                        step["next_step"] = target_step_id
                break

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_14(steps: list[dict[str, Any]], source_step_id: str, target_step_id: str, flow) -> None:
        for step in steps:
            if step["id"] == source_step_id:
                if step["type"] in ("condition", "fork"):
                    if "branches" not in step:
                        step["branches"] = None
                    step["branches"].append({
                        "next_step": target_step_id,
                        "condition": flow.condition_expression or "",
                        "label": flow.name or f"Branch {len(step['branches']) + 1}",
                    })
                else:
                    if step.get("next_step") is None or step["type"] == "output":
                        step["next_step"] = target_step_id
                break

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_15(steps: list[dict[str, Any]], source_step_id: str, target_step_id: str, flow) -> None:
        for step in steps:
            if step["id"] == source_step_id:
                if step["type"] in ("condition", "fork"):
                    if "branches" not in step:
                        step["XXbranchesXX"] = []
                    step["branches"].append({
                        "next_step": target_step_id,
                        "condition": flow.condition_expression or "",
                        "label": flow.name or f"Branch {len(step['branches']) + 1}",
                    })
                else:
                    if step.get("next_step") is None or step["type"] == "output":
                        step["next_step"] = target_step_id
                break

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_16(steps: list[dict[str, Any]], source_step_id: str, target_step_id: str, flow) -> None:
        for step in steps:
            if step["id"] == source_step_id:
                if step["type"] in ("condition", "fork"):
                    if "branches" not in step:
                        step["BRANCHES"] = []
                    step["branches"].append({
                        "next_step": target_step_id,
                        "condition": flow.condition_expression or "",
                        "label": flow.name or f"Branch {len(step['branches']) + 1}",
                    })
                else:
                    if step.get("next_step") is None or step["type"] == "output":
                        step["next_step"] = target_step_id
                break

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_17(steps: list[dict[str, Any]], source_step_id: str, target_step_id: str, flow) -> None:
        for step in steps:
            if step["id"] == source_step_id:
                if step["type"] in ("condition", "fork"):
                    if "branches" not in step:
                        step["branches"] = []
                    step["branches"].append(None)
                else:
                    if step.get("next_step") is None or step["type"] == "output":
                        step["next_step"] = target_step_id
                break

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_18(steps: list[dict[str, Any]], source_step_id: str, target_step_id: str, flow) -> None:
        for step in steps:
            if step["id"] == source_step_id:
                if step["type"] in ("condition", "fork"):
                    if "branches" not in step:
                        step["branches"] = []
                    step["XXbranchesXX"].append({
                        "next_step": target_step_id,
                        "condition": flow.condition_expression or "",
                        "label": flow.name or f"Branch {len(step['branches']) + 1}",
                    })
                else:
                    if step.get("next_step") is None or step["type"] == "output":
                        step["next_step"] = target_step_id
                break

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_19(steps: list[dict[str, Any]], source_step_id: str, target_step_id: str, flow) -> None:
        for step in steps:
            if step["id"] == source_step_id:
                if step["type"] in ("condition", "fork"):
                    if "branches" not in step:
                        step["branches"] = []
                    step["BRANCHES"].append({
                        "next_step": target_step_id,
                        "condition": flow.condition_expression or "",
                        "label": flow.name or f"Branch {len(step['branches']) + 1}",
                    })
                else:
                    if step.get("next_step") is None or step["type"] == "output":
                        step["next_step"] = target_step_id
                break

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_20(steps: list[dict[str, Any]], source_step_id: str, target_step_id: str, flow) -> None:
        for step in steps:
            if step["id"] == source_step_id:
                if step["type"] in ("condition", "fork"):
                    if "branches" not in step:
                        step["branches"] = []
                    step["branches"].append({
                        "XXnext_stepXX": target_step_id,
                        "condition": flow.condition_expression or "",
                        "label": flow.name or f"Branch {len(step['branches']) + 1}",
                    })
                else:
                    if step.get("next_step") is None or step["type"] == "output":
                        step["next_step"] = target_step_id
                break

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_21(steps: list[dict[str, Any]], source_step_id: str, target_step_id: str, flow) -> None:
        for step in steps:
            if step["id"] == source_step_id:
                if step["type"] in ("condition", "fork"):
                    if "branches" not in step:
                        step["branches"] = []
                    step["branches"].append({
                        "NEXT_STEP": target_step_id,
                        "condition": flow.condition_expression or "",
                        "label": flow.name or f"Branch {len(step['branches']) + 1}",
                    })
                else:
                    if step.get("next_step") is None or step["type"] == "output":
                        step["next_step"] = target_step_id
                break

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_22(steps: list[dict[str, Any]], source_step_id: str, target_step_id: str, flow) -> None:
        for step in steps:
            if step["id"] == source_step_id:
                if step["type"] in ("condition", "fork"):
                    if "branches" not in step:
                        step["branches"] = []
                    step["branches"].append({
                        "next_step": target_step_id,
                        "XXconditionXX": flow.condition_expression or "",
                        "label": flow.name or f"Branch {len(step['branches']) + 1}",
                    })
                else:
                    if step.get("next_step") is None or step["type"] == "output":
                        step["next_step"] = target_step_id
                break

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_23(steps: list[dict[str, Any]], source_step_id: str, target_step_id: str, flow) -> None:
        for step in steps:
            if step["id"] == source_step_id:
                if step["type"] in ("condition", "fork"):
                    if "branches" not in step:
                        step["branches"] = []
                    step["branches"].append({
                        "next_step": target_step_id,
                        "CONDITION": flow.condition_expression or "",
                        "label": flow.name or f"Branch {len(step['branches']) + 1}",
                    })
                else:
                    if step.get("next_step") is None or step["type"] == "output":
                        step["next_step"] = target_step_id
                break

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_24(steps: list[dict[str, Any]], source_step_id: str, target_step_id: str, flow) -> None:
        for step in steps:
            if step["id"] == source_step_id:
                if step["type"] in ("condition", "fork"):
                    if "branches" not in step:
                        step["branches"] = []
                    step["branches"].append({
                        "next_step": target_step_id,
                        "condition": flow.condition_expression and "",
                        "label": flow.name or f"Branch {len(step['branches']) + 1}",
                    })
                else:
                    if step.get("next_step") is None or step["type"] == "output":
                        step["next_step"] = target_step_id
                break

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_25(steps: list[dict[str, Any]], source_step_id: str, target_step_id: str, flow) -> None:
        for step in steps:
            if step["id"] == source_step_id:
                if step["type"] in ("condition", "fork"):
                    if "branches" not in step:
                        step["branches"] = []
                    step["branches"].append({
                        "next_step": target_step_id,
                        "condition": flow.condition_expression or "XXXX",
                        "label": flow.name or f"Branch {len(step['branches']) + 1}",
                    })
                else:
                    if step.get("next_step") is None or step["type"] == "output":
                        step["next_step"] = target_step_id
                break

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_26(steps: list[dict[str, Any]], source_step_id: str, target_step_id: str, flow) -> None:
        for step in steps:
            if step["id"] == source_step_id:
                if step["type"] in ("condition", "fork"):
                    if "branches" not in step:
                        step["branches"] = []
                    step["branches"].append({
                        "next_step": target_step_id,
                        "condition": flow.condition_expression or "",
                        "XXlabelXX": flow.name or f"Branch {len(step['branches']) + 1}",
                    })
                else:
                    if step.get("next_step") is None or step["type"] == "output":
                        step["next_step"] = target_step_id
                break

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_27(steps: list[dict[str, Any]], source_step_id: str, target_step_id: str, flow) -> None:
        for step in steps:
            if step["id"] == source_step_id:
                if step["type"] in ("condition", "fork"):
                    if "branches" not in step:
                        step["branches"] = []
                    step["branches"].append({
                        "next_step": target_step_id,
                        "condition": flow.condition_expression or "",
                        "LABEL": flow.name or f"Branch {len(step['branches']) + 1}",
                    })
                else:
                    if step.get("next_step") is None or step["type"] == "output":
                        step["next_step"] = target_step_id
                break

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_28(steps: list[dict[str, Any]], source_step_id: str, target_step_id: str, flow) -> None:
        for step in steps:
            if step["id"] == source_step_id:
                if step["type"] in ("condition", "fork"):
                    if "branches" not in step:
                        step["branches"] = []
                    step["branches"].append({
                        "next_step": target_step_id,
                        "condition": flow.condition_expression or "",
                        "label": flow.name and f"Branch {len(step['branches']) + 1}",
                    })
                else:
                    if step.get("next_step") is None or step["type"] == "output":
                        step["next_step"] = target_step_id
                break

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_29(steps: list[dict[str, Any]], source_step_id: str, target_step_id: str, flow) -> None:
        for step in steps:
            if step["id"] == source_step_id:
                if step["type"] in ("condition", "fork"):
                    if "branches" not in step:
                        step["branches"] = []
                    step["branches"].append({
                        "next_step": target_step_id,
                        "condition": flow.condition_expression or "",
                        "label": flow.name or f"Branch {len(step['branches']) - 1}",
                    })
                else:
                    if step.get("next_step") is None or step["type"] == "output":
                        step["next_step"] = target_step_id
                break

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_30(steps: list[dict[str, Any]], source_step_id: str, target_step_id: str, flow) -> None:
        for step in steps:
            if step["id"] == source_step_id:
                if step["type"] in ("condition", "fork"):
                    if "branches" not in step:
                        step["branches"] = []
                    step["branches"].append({
                        "next_step": target_step_id,
                        "condition": flow.condition_expression or "",
                        "label": flow.name or f"Branch {len(step['branches']) + 2}",
                    })
                else:
                    if step.get("next_step") is None or step["type"] == "output":
                        step["next_step"] = target_step_id
                break

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_31(steps: list[dict[str, Any]], source_step_id: str, target_step_id: str, flow) -> None:
        for step in steps:
            if step["id"] == source_step_id:
                if step["type"] in ("condition", "fork"):
                    if "branches" not in step:
                        step["branches"] = []
                    step["branches"].append({
                        "next_step": target_step_id,
                        "condition": flow.condition_expression or "",
                        "label": flow.name or f"Branch {len(step['branches']) + 1}",
                    })
                else:
                    if step.get("next_step") is None and step["type"] == "output":
                        step["next_step"] = target_step_id
                break

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_32(steps: list[dict[str, Any]], source_step_id: str, target_step_id: str, flow) -> None:
        for step in steps:
            if step["id"] == source_step_id:
                if step["type"] in ("condition", "fork"):
                    if "branches" not in step:
                        step["branches"] = []
                    step["branches"].append({
                        "next_step": target_step_id,
                        "condition": flow.condition_expression or "",
                        "label": flow.name or f"Branch {len(step['branches']) + 1}",
                    })
                else:
                    if step.get(None) is None or step["type"] == "output":
                        step["next_step"] = target_step_id
                break

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_33(steps: list[dict[str, Any]], source_step_id: str, target_step_id: str, flow) -> None:
        for step in steps:
            if step["id"] == source_step_id:
                if step["type"] in ("condition", "fork"):
                    if "branches" not in step:
                        step["branches"] = []
                    step["branches"].append({
                        "next_step": target_step_id,
                        "condition": flow.condition_expression or "",
                        "label": flow.name or f"Branch {len(step['branches']) + 1}",
                    })
                else:
                    if step.get("XXnext_stepXX") is None or step["type"] == "output":
                        step["next_step"] = target_step_id
                break

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_34(steps: list[dict[str, Any]], source_step_id: str, target_step_id: str, flow) -> None:
        for step in steps:
            if step["id"] == source_step_id:
                if step["type"] in ("condition", "fork"):
                    if "branches" not in step:
                        step["branches"] = []
                    step["branches"].append({
                        "next_step": target_step_id,
                        "condition": flow.condition_expression or "",
                        "label": flow.name or f"Branch {len(step['branches']) + 1}",
                    })
                else:
                    if step.get("NEXT_STEP") is None or step["type"] == "output":
                        step["next_step"] = target_step_id
                break

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_35(steps: list[dict[str, Any]], source_step_id: str, target_step_id: str, flow) -> None:
        for step in steps:
            if step["id"] == source_step_id:
                if step["type"] in ("condition", "fork"):
                    if "branches" not in step:
                        step["branches"] = []
                    step["branches"].append({
                        "next_step": target_step_id,
                        "condition": flow.condition_expression or "",
                        "label": flow.name or f"Branch {len(step['branches']) + 1}",
                    })
                else:
                    if step.get("next_step") is not None or step["type"] == "output":
                        step["next_step"] = target_step_id
                break

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_36(steps: list[dict[str, Any]], source_step_id: str, target_step_id: str, flow) -> None:
        for step in steps:
            if step["id"] == source_step_id:
                if step["type"] in ("condition", "fork"):
                    if "branches" not in step:
                        step["branches"] = []
                    step["branches"].append({
                        "next_step": target_step_id,
                        "condition": flow.condition_expression or "",
                        "label": flow.name or f"Branch {len(step['branches']) + 1}",
                    })
                else:
                    if step.get("next_step") is None or step["XXtypeXX"] == "output":
                        step["next_step"] = target_step_id
                break

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_37(steps: list[dict[str, Any]], source_step_id: str, target_step_id: str, flow) -> None:
        for step in steps:
            if step["id"] == source_step_id:
                if step["type"] in ("condition", "fork"):
                    if "branches" not in step:
                        step["branches"] = []
                    step["branches"].append({
                        "next_step": target_step_id,
                        "condition": flow.condition_expression or "",
                        "label": flow.name or f"Branch {len(step['branches']) + 1}",
                    })
                else:
                    if step.get("next_step") is None or step["TYPE"] == "output":
                        step["next_step"] = target_step_id
                break

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_38(steps: list[dict[str, Any]], source_step_id: str, target_step_id: str, flow) -> None:
        for step in steps:
            if step["id"] == source_step_id:
                if step["type"] in ("condition", "fork"):
                    if "branches" not in step:
                        step["branches"] = []
                    step["branches"].append({
                        "next_step": target_step_id,
                        "condition": flow.condition_expression or "",
                        "label": flow.name or f"Branch {len(step['branches']) + 1}",
                    })
                else:
                    if step.get("next_step") is None or step["type"] != "output":
                        step["next_step"] = target_step_id
                break

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_39(steps: list[dict[str, Any]], source_step_id: str, target_step_id: str, flow) -> None:
        for step in steps:
            if step["id"] == source_step_id:
                if step["type"] in ("condition", "fork"):
                    if "branches" not in step:
                        step["branches"] = []
                    step["branches"].append({
                        "next_step": target_step_id,
                        "condition": flow.condition_expression or "",
                        "label": flow.name or f"Branch {len(step['branches']) + 1}",
                    })
                else:
                    if step.get("next_step") is None or step["type"] == "XXoutputXX":
                        step["next_step"] = target_step_id
                break

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_40(steps: list[dict[str, Any]], source_step_id: str, target_step_id: str, flow) -> None:
        for step in steps:
            if step["id"] == source_step_id:
                if step["type"] in ("condition", "fork"):
                    if "branches" not in step:
                        step["branches"] = []
                    step["branches"].append({
                        "next_step": target_step_id,
                        "condition": flow.condition_expression or "",
                        "label": flow.name or f"Branch {len(step['branches']) + 1}",
                    })
                else:
                    if step.get("next_step") is None or step["type"] == "OUTPUT":
                        step["next_step"] = target_step_id
                break

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_41(steps: list[dict[str, Any]], source_step_id: str, target_step_id: str, flow) -> None:
        for step in steps:
            if step["id"] == source_step_id:
                if step["type"] in ("condition", "fork"):
                    if "branches" not in step:
                        step["branches"] = []
                    step["branches"].append({
                        "next_step": target_step_id,
                        "condition": flow.condition_expression or "",
                        "label": flow.name or f"Branch {len(step['branches']) + 1}",
                    })
                else:
                    if step.get("next_step") is None or step["type"] == "output":
                        step["next_step"] = None
                break

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_42(steps: list[dict[str, Any]], source_step_id: str, target_step_id: str, flow) -> None:
        for step in steps:
            if step["id"] == source_step_id:
                if step["type"] in ("condition", "fork"):
                    if "branches" not in step:
                        step["branches"] = []
                    step["branches"].append({
                        "next_step": target_step_id,
                        "condition": flow.condition_expression or "",
                        "label": flow.name or f"Branch {len(step['branches']) + 1}",
                    })
                else:
                    if step.get("next_step") is None or step["type"] == "output":
                        step["XXnext_stepXX"] = target_step_id
                break

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_43(steps: list[dict[str, Any]], source_step_id: str, target_step_id: str, flow) -> None:
        for step in steps:
            if step["id"] == source_step_id:
                if step["type"] in ("condition", "fork"):
                    if "branches" not in step:
                        step["branches"] = []
                    step["branches"].append({
                        "next_step": target_step_id,
                        "condition": flow.condition_expression or "",
                        "label": flow.name or f"Branch {len(step['branches']) + 1}",
                    })
                else:
                    if step.get("next_step") is None or step["type"] == "output":
                        step["NEXT_STEP"] = target_step_id
                break

    @staticmethod
    def xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_44(steps: list[dict[str, Any]], source_step_id: str, target_step_id: str, flow) -> None:
        for step in steps:
            if step["id"] == source_step_id:
                if step["type"] in ("condition", "fork"):
                    if "branches" not in step:
                        step["branches"] = []
                    step["branches"].append({
                        "next_step": target_step_id,
                        "condition": flow.condition_expression or "",
                        "label": flow.name or f"Branch {len(step['branches']) + 1}",
                    })
                else:
                    if step.get("next_step") is None or step["type"] == "output":
                        step["next_step"] = target_step_id
                return

mutants_xǁBPMNToWorkflowConverterǁ_get_task_type_map__mutmut['_mutmut_orig'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_get_task_type_map__mutmut_orig # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_get_task_type_map__mutmut['xǁBPMNToWorkflowConverterǁ_get_task_type_map__mutmut_1'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_get_task_type_map__mutmut_1 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_get_task_type_map__mutmut['xǁBPMNToWorkflowConverterǁ_get_task_type_map__mutmut_2'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_get_task_type_map__mutmut_2 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_get_task_type_map__mutmut['xǁBPMNToWorkflowConverterǁ_get_task_type_map__mutmut_3'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_get_task_type_map__mutmut_3 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_get_task_type_map__mutmut['xǁBPMNToWorkflowConverterǁ_get_task_type_map__mutmut_4'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_get_task_type_map__mutmut_4 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_get_task_type_map__mutmut['xǁBPMNToWorkflowConverterǁ_get_task_type_map__mutmut_5'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_get_task_type_map__mutmut_5 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_get_task_type_map__mutmut['xǁBPMNToWorkflowConverterǁ_get_task_type_map__mutmut_6'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_get_task_type_map__mutmut_6 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_get_task_type_map__mutmut['xǁBPMNToWorkflowConverterǁ_get_task_type_map__mutmut_7'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_get_task_type_map__mutmut_7 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_get_task_type_map__mutmut['xǁBPMNToWorkflowConverterǁ_get_task_type_map__mutmut_8'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_get_task_type_map__mutmut_8 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_get_task_type_map__mutmut['xǁBPMNToWorkflowConverterǁ_get_task_type_map__mutmut_9'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_get_task_type_map__mutmut_9 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_get_task_type_map__mutmut['xǁBPMNToWorkflowConverterǁ_get_task_type_map__mutmut_10'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_get_task_type_map__mutmut_10 # type: ignore # mutmut generated

mutants_xǁBPMNToWorkflowConverterǁconvert__mutmut['_mutmut_orig'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁconvert__mutmut_orig # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁconvert__mutmut['xǁBPMNToWorkflowConverterǁconvert__mutmut_1'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁconvert__mutmut_1 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁconvert__mutmut['xǁBPMNToWorkflowConverterǁconvert__mutmut_2'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁconvert__mutmut_2 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁconvert__mutmut['xǁBPMNToWorkflowConverterǁconvert__mutmut_3'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁconvert__mutmut_3 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁconvert__mutmut['xǁBPMNToWorkflowConverterǁconvert__mutmut_4'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁconvert__mutmut_4 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁconvert__mutmut['xǁBPMNToWorkflowConverterǁconvert__mutmut_5'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁconvert__mutmut_5 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁconvert__mutmut['xǁBPMNToWorkflowConverterǁconvert__mutmut_6'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁconvert__mutmut_6 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁconvert__mutmut['xǁBPMNToWorkflowConverterǁconvert__mutmut_7'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁconvert__mutmut_7 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁconvert__mutmut['xǁBPMNToWorkflowConverterǁconvert__mutmut_8'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁconvert__mutmut_8 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁconvert__mutmut['xǁBPMNToWorkflowConverterǁconvert__mutmut_9'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁconvert__mutmut_9 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁconvert__mutmut['xǁBPMNToWorkflowConverterǁconvert__mutmut_10'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁconvert__mutmut_10 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁconvert__mutmut['xǁBPMNToWorkflowConverterǁconvert__mutmut_11'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁconvert__mutmut_11 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁconvert__mutmut['xǁBPMNToWorkflowConverterǁconvert__mutmut_12'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁconvert__mutmut_12 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁconvert__mutmut['xǁBPMNToWorkflowConverterǁconvert__mutmut_13'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁconvert__mutmut_13 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁconvert__mutmut['xǁBPMNToWorkflowConverterǁconvert__mutmut_14'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁconvert__mutmut_14 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁconvert__mutmut['xǁBPMNToWorkflowConverterǁconvert__mutmut_15'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁconvert__mutmut_15 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁconvert__mutmut['xǁBPMNToWorkflowConverterǁconvert__mutmut_16'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁconvert__mutmut_16 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁconvert__mutmut['xǁBPMNToWorkflowConverterǁconvert__mutmut_17'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁconvert__mutmut_17 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁconvert__mutmut['xǁBPMNToWorkflowConverterǁconvert__mutmut_18'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁconvert__mutmut_18 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁconvert__mutmut['xǁBPMNToWorkflowConverterǁconvert__mutmut_19'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁconvert__mutmut_19 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁconvert__mutmut['xǁBPMNToWorkflowConverterǁconvert__mutmut_20'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁconvert__mutmut_20 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁconvert__mutmut['xǁBPMNToWorkflowConverterǁconvert__mutmut_21'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁconvert__mutmut_21 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁconvert__mutmut['xǁBPMNToWorkflowConverterǁconvert__mutmut_22'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁconvert__mutmut_22 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁconvert__mutmut['xǁBPMNToWorkflowConverterǁconvert__mutmut_23'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁconvert__mutmut_23 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁconvert__mutmut['xǁBPMNToWorkflowConverterǁconvert__mutmut_24'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁconvert__mutmut_24 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁconvert__mutmut['xǁBPMNToWorkflowConverterǁconvert__mutmut_25'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁconvert__mutmut_25 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁconvert__mutmut['xǁBPMNToWorkflowConverterǁconvert__mutmut_26'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁconvert__mutmut_26 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁconvert__mutmut['xǁBPMNToWorkflowConverterǁconvert__mutmut_27'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁconvert__mutmut_27 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁconvert__mutmut['xǁBPMNToWorkflowConverterǁconvert__mutmut_28'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁconvert__mutmut_28 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁconvert__mutmut['xǁBPMNToWorkflowConverterǁconvert__mutmut_29'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁconvert__mutmut_29 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁconvert__mutmut['xǁBPMNToWorkflowConverterǁconvert__mutmut_30'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁconvert__mutmut_30 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁconvert__mutmut['xǁBPMNToWorkflowConverterǁconvert__mutmut_31'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁconvert__mutmut_31 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁconvert__mutmut['xǁBPMNToWorkflowConverterǁconvert__mutmut_32'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁconvert__mutmut_32 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁconvert__mutmut['xǁBPMNToWorkflowConverterǁconvert__mutmut_33'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁconvert__mutmut_33 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁconvert__mutmut['xǁBPMNToWorkflowConverterǁconvert__mutmut_34'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁconvert__mutmut_34 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁconvert__mutmut['xǁBPMNToWorkflowConverterǁconvert__mutmut_35'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁconvert__mutmut_35 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁconvert__mutmut['xǁBPMNToWorkflowConverterǁconvert__mutmut_36'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁconvert__mutmut_36 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁconvert__mutmut['xǁBPMNToWorkflowConverterǁconvert__mutmut_37'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁconvert__mutmut_37 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁconvert__mutmut['xǁBPMNToWorkflowConverterǁconvert__mutmut_38'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁconvert__mutmut_38 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁconvert__mutmut['xǁBPMNToWorkflowConverterǁconvert__mutmut_39'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁconvert__mutmut_39 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁconvert__mutmut['xǁBPMNToWorkflowConverterǁconvert__mutmut_40'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁconvert__mutmut_40 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁconvert__mutmut['xǁBPMNToWorkflowConverterǁconvert__mutmut_41'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁconvert__mutmut_41 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁconvert__mutmut['xǁBPMNToWorkflowConverterǁconvert__mutmut_42'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁconvert__mutmut_42 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁconvert__mutmut['xǁBPMNToWorkflowConverterǁconvert__mutmut_43'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁconvert__mutmut_43 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁconvert__mutmut['xǁBPMNToWorkflowConverterǁconvert__mutmut_44'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁconvert__mutmut_44 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁconvert__mutmut['xǁBPMNToWorkflowConverterǁconvert__mutmut_45'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁconvert__mutmut_45 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁconvert__mutmut['xǁBPMNToWorkflowConverterǁconvert__mutmut_46'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁconvert__mutmut_46 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁconvert__mutmut['xǁBPMNToWorkflowConverterǁconvert__mutmut_47'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁconvert__mutmut_47 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁconvert__mutmut['xǁBPMNToWorkflowConverterǁconvert__mutmut_48'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁconvert__mutmut_48 # type: ignore # mutmut generated

mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['_mutmut_orig'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_orig # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_1'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_1 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_2'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_2 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_3'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_3 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_4'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_4 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_5'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_5 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_6'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_6 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_7'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_7 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_8'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_8 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_9'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_9 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_10'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_10 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_11'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_11 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_12'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_12 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_13'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_13 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_14'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_14 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_15'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_15 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_16'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_16 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_17'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_17 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_18'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_18 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_19'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_19 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_20'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_20 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_21'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_21 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_22'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_22 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_23'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_23 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_24'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_24 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_25'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_25 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_26'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_26 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_27'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_27 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_28'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_28 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_29'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_29 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_30'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_30 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_31'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_31 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_32'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_32 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_33'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_33 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_34'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_34 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_35'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_35 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_36'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_36 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_37'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_37 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_38'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_38 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_39'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_39 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_40'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_40 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_41'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_41 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_42'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_42 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_43'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_43 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_44'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_44 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_45'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_45 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_46'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_46 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_47'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_47 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_48'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_48 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_49'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_49 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_50'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_50 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_51'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_51 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_52'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_52 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_53'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_53 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_54'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_54 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_55'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_55 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_56'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_56 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_57'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_57 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_58'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_58 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_59'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_59 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_60'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_60 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_61'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_61 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_62'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_62 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_63'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_63 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_64'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_64 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_65'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_65 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_66'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_66 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_67'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_67 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_68'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_68 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_69'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_69 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_70'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_70 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_71'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_71 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_72'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_72 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_73'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_73 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_74'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_74 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_75'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_75 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_76'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_76 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_77'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_77 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_78'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_78 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_79'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_79 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_80'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_80 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_81'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_81 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_82'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_82 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_83'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_83 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_84'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_84 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_85'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_85 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_86'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_86 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_87'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_87 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_88'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_88 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_89'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_89 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_90'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_90 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_91'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_91 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_92'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_92 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_93'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_93 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_94'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_94 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_95'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_95 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_96'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_96 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_97'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_97 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_98'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_98 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut['xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_99'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_element_to_step__mutmut_99 # type: ignore # mutmut generated

mutants_xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut['_mutmut_orig'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_orig # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut['xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_1'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_1 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut['xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_2'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_2 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut['xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_3'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_3 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut['xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_4'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_4 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut['xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_5'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_5 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut['xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_6'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_6 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut['xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_7'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_7 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut['xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_8'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_8 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut['xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_9'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_9 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut['xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_10'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_10 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut['xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_11'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_11 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut['xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_12'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_12 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut['xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_13'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_13 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut['xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_14'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_14 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut['xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_15'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_15 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut['xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_16'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_16 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut['xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_17'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_17 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut['xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_18'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_18 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut['xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_19'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_19 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut['xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_20'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_20 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut['xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_21'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_21 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut['xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_22'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_22 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut['xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_23'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_23 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut['xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_24'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_24 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut['xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_25'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_25 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut['xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_26'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_26 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut['xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_27'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_27 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut['xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_28'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_map_element_type__mutmut_28 # type: ignore # mutmut generated

mutants_xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut['_mutmut_orig'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_orig # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut['xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_1'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_1 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut['xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_2'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_2 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut['xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_3'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_3 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut['xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_4'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_4 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut['xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_5'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_5 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut['xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_6'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_6 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut['xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_7'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_7 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut['xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_8'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_8 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut['xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_9'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_9 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut['xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_10'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_10 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut['xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_11'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_11 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut['xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_12'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_12 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut['xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_13'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_13 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut['xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_14'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_14 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut['xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_15'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_15 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut['xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_16'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_16 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut['xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_17'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_17 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut['xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_18'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_18 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut['xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_19'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_19 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut['xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_20'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_20 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut['xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_21'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_21 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut['xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_22'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_22 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut['xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_23'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_23 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut['xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_24'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_24 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut['xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_25'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_25 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut['xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_26'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_26 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut['xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_27'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_27 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut['xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_28'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_28 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut['xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_29'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_29 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut['xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_30'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_30 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut['xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_31'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_31 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut['xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_32'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_32 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut['xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_33'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_33 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut['xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_34'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_34 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut['xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_35'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_35 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut['xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_36'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_36 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut['xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_37'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_37 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut['xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_38'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_38 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut['xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_39'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_39 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut['xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_40'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_40 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut['xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_41'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_41 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut['xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_42'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_42 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut['xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_43'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_43 # type: ignore # mutmut generated
mutants_xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut['xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_44'] = BPMNToWorkflowConverter.xǁBPMNToWorkflowConverterǁ_update_next_steps__mutmut_44 # type: ignore # mutmut generated
