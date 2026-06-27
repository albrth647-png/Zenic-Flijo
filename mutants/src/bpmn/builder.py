"""Fluent BPMN process builder — programmatic BPMN process creation.

Extracted from src/bpmn/__init__.py.
"""

from __future__ import annotations

import uuid

from src.bpmn.models import BPMNElement, BPMNElementType, BPMNProcess, BPMNSequenceFlow


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁBPMNBuilderǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁBPMNBuilderǁstart_event__mutmut: MutantDict = {}  # type: ignore
mutants_xǁBPMNBuilderǁend_event__mutmut: MutantDict = {}  # type: ignore
mutants_xǁBPMNBuilderǁuser_task__mutmut: MutantDict = {}  # type: ignore
mutants_xǁBPMNBuilderǁservice_task__mutmut: MutantDict = {}  # type: ignore
mutants_xǁBPMNBuilderǁscript_task__mutmut: MutantDict = {}  # type: ignore
mutants_xǁBPMNBuilderǁexclusive_gateway__mutmut: MutantDict = {}  # type: ignore
mutants_xǁBPMNBuilderǁparallel_gateway__mutmut: MutantDict = {}  # type: ignore
mutants_xǁBPMNBuilderǁconnect__mutmut: MutantDict = {}  # type: ignore


class BPMNBuilder:
    """Fluent builder for creating BPMN processes programmatically."""

    @_mutmut_mutated(mutants_xǁBPMNBuilderǁ__init____mutmut)
    def __init__(self, name: str = "", process_id: str = "") -> None:
        self._process = BPMNProcess(
            process_id=process_id or f"process_{uuid.uuid4().hex[:8]}",
            name=name,
        )
        self._x_offset = 50.0
        self._y_offset = 50.0
        self._step_width = 150.0
        self._step_gap = 200.0

    def xǁBPMNBuilderǁ__init____mutmut_orig(self, name: str = "", process_id: str = "") -> None:
        self._process = BPMNProcess(
            process_id=process_id or f"process_{uuid.uuid4().hex[:8]}",
            name=name,
        )
        self._x_offset = 50.0
        self._y_offset = 50.0
        self._step_width = 150.0
        self._step_gap = 200.0

    def xǁBPMNBuilderǁ__init____mutmut_1(self, name: str = "XXXX", process_id: str = "") -> None:
        self._process = BPMNProcess(
            process_id=process_id or f"process_{uuid.uuid4().hex[:8]}",
            name=name,
        )
        self._x_offset = 50.0
        self._y_offset = 50.0
        self._step_width = 150.0
        self._step_gap = 200.0

    def xǁBPMNBuilderǁ__init____mutmut_2(self, name: str = "", process_id: str = "XXXX") -> None:
        self._process = BPMNProcess(
            process_id=process_id or f"process_{uuid.uuid4().hex[:8]}",
            name=name,
        )
        self._x_offset = 50.0
        self._y_offset = 50.0
        self._step_width = 150.0
        self._step_gap = 200.0

    def xǁBPMNBuilderǁ__init____mutmut_3(self, name: str = "", process_id: str = "") -> None:
        self._process = None
        self._x_offset = 50.0
        self._y_offset = 50.0
        self._step_width = 150.0
        self._step_gap = 200.0

    def xǁBPMNBuilderǁ__init____mutmut_4(self, name: str = "", process_id: str = "") -> None:
        self._process = BPMNProcess(
            process_id=None,
            name=name,
        )
        self._x_offset = 50.0
        self._y_offset = 50.0
        self._step_width = 150.0
        self._step_gap = 200.0

    def xǁBPMNBuilderǁ__init____mutmut_5(self, name: str = "", process_id: str = "") -> None:
        self._process = BPMNProcess(
            process_id=process_id or f"process_{uuid.uuid4().hex[:8]}",
            name=None,
        )
        self._x_offset = 50.0
        self._y_offset = 50.0
        self._step_width = 150.0
        self._step_gap = 200.0

    def xǁBPMNBuilderǁ__init____mutmut_6(self, name: str = "", process_id: str = "") -> None:
        self._process = BPMNProcess(
            name=name,
        )
        self._x_offset = 50.0
        self._y_offset = 50.0
        self._step_width = 150.0
        self._step_gap = 200.0

    def xǁBPMNBuilderǁ__init____mutmut_7(self, name: str = "", process_id: str = "") -> None:
        self._process = BPMNProcess(
            process_id=process_id or f"process_{uuid.uuid4().hex[:8]}",
            )
        self._x_offset = 50.0
        self._y_offset = 50.0
        self._step_width = 150.0
        self._step_gap = 200.0

    def xǁBPMNBuilderǁ__init____mutmut_8(self, name: str = "", process_id: str = "") -> None:
        self._process = BPMNProcess(
            process_id=process_id and f"process_{uuid.uuid4().hex[:8]}",
            name=name,
        )
        self._x_offset = 50.0
        self._y_offset = 50.0
        self._step_width = 150.0
        self._step_gap = 200.0

    def xǁBPMNBuilderǁ__init____mutmut_9(self, name: str = "", process_id: str = "") -> None:
        self._process = BPMNProcess(
            process_id=process_id or f"process_{uuid.uuid4().hex[:9]}",
            name=name,
        )
        self._x_offset = 50.0
        self._y_offset = 50.0
        self._step_width = 150.0
        self._step_gap = 200.0

    def xǁBPMNBuilderǁ__init____mutmut_10(self, name: str = "", process_id: str = "") -> None:
        self._process = BPMNProcess(
            process_id=process_id or f"process_{uuid.uuid4().hex[:8]}",
            name=name,
        )
        self._x_offset = None
        self._y_offset = 50.0
        self._step_width = 150.0
        self._step_gap = 200.0

    def xǁBPMNBuilderǁ__init____mutmut_11(self, name: str = "", process_id: str = "") -> None:
        self._process = BPMNProcess(
            process_id=process_id or f"process_{uuid.uuid4().hex[:8]}",
            name=name,
        )
        self._x_offset = 51.0
        self._y_offset = 50.0
        self._step_width = 150.0
        self._step_gap = 200.0

    def xǁBPMNBuilderǁ__init____mutmut_12(self, name: str = "", process_id: str = "") -> None:
        self._process = BPMNProcess(
            process_id=process_id or f"process_{uuid.uuid4().hex[:8]}",
            name=name,
        )
        self._x_offset = 50.0
        self._y_offset = None
        self._step_width = 150.0
        self._step_gap = 200.0

    def xǁBPMNBuilderǁ__init____mutmut_13(self, name: str = "", process_id: str = "") -> None:
        self._process = BPMNProcess(
            process_id=process_id or f"process_{uuid.uuid4().hex[:8]}",
            name=name,
        )
        self._x_offset = 50.0
        self._y_offset = 51.0
        self._step_width = 150.0
        self._step_gap = 200.0

    def xǁBPMNBuilderǁ__init____mutmut_14(self, name: str = "", process_id: str = "") -> None:
        self._process = BPMNProcess(
            process_id=process_id or f"process_{uuid.uuid4().hex[:8]}",
            name=name,
        )
        self._x_offset = 50.0
        self._y_offset = 50.0
        self._step_width = None
        self._step_gap = 200.0

    def xǁBPMNBuilderǁ__init____mutmut_15(self, name: str = "", process_id: str = "") -> None:
        self._process = BPMNProcess(
            process_id=process_id or f"process_{uuid.uuid4().hex[:8]}",
            name=name,
        )
        self._x_offset = 50.0
        self._y_offset = 50.0
        self._step_width = 151.0
        self._step_gap = 200.0

    def xǁBPMNBuilderǁ__init____mutmut_16(self, name: str = "", process_id: str = "") -> None:
        self._process = BPMNProcess(
            process_id=process_id or f"process_{uuid.uuid4().hex[:8]}",
            name=name,
        )
        self._x_offset = 50.0
        self._y_offset = 50.0
        self._step_width = 150.0
        self._step_gap = None

    def xǁBPMNBuilderǁ__init____mutmut_17(self, name: str = "", process_id: str = "") -> None:
        self._process = BPMNProcess(
            process_id=process_id or f"process_{uuid.uuid4().hex[:8]}",
            name=name,
        )
        self._x_offset = 50.0
        self._y_offset = 50.0
        self._step_width = 150.0
        self._step_gap = 201.0

    @_mutmut_mutated(mutants_xǁBPMNBuilderǁstart_event__mutmut)
    def start_event(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name or "Start",
                              element_type=BPMNElementType.START_EVENT,
                              x=self._x_offset, y=self._y_offset, width=36.0, height=36.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁstart_event__mutmut_orig(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name or "Start",
                              element_type=BPMNElementType.START_EVENT,
                              x=self._x_offset, y=self._y_offset, width=36.0, height=36.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁstart_event__mutmut_1(self, element_id: str, name: str = "XXXX") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name or "Start",
                              element_type=BPMNElementType.START_EVENT,
                              x=self._x_offset, y=self._y_offset, width=36.0, height=36.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁstart_event__mutmut_2(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = None
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁstart_event__mutmut_3(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=None, name=name or "Start",
                              element_type=BPMNElementType.START_EVENT,
                              x=self._x_offset, y=self._y_offset, width=36.0, height=36.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁstart_event__mutmut_4(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=None,
                              element_type=BPMNElementType.START_EVENT,
                              x=self._x_offset, y=self._y_offset, width=36.0, height=36.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁstart_event__mutmut_5(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name or "Start",
                              element_type=None,
                              x=self._x_offset, y=self._y_offset, width=36.0, height=36.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁstart_event__mutmut_6(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name or "Start",
                              element_type=BPMNElementType.START_EVENT,
                              x=None, y=self._y_offset, width=36.0, height=36.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁstart_event__mutmut_7(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name or "Start",
                              element_type=BPMNElementType.START_EVENT,
                              x=self._x_offset, y=None, width=36.0, height=36.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁstart_event__mutmut_8(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name or "Start",
                              element_type=BPMNElementType.START_EVENT,
                              x=self._x_offset, y=self._y_offset, width=None, height=36.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁstart_event__mutmut_9(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name or "Start",
                              element_type=BPMNElementType.START_EVENT,
                              x=self._x_offset, y=self._y_offset, width=36.0, height=None)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁstart_event__mutmut_10(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(name=name or "Start",
                              element_type=BPMNElementType.START_EVENT,
                              x=self._x_offset, y=self._y_offset, width=36.0, height=36.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁstart_event__mutmut_11(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, element_type=BPMNElementType.START_EVENT,
                              x=self._x_offset, y=self._y_offset, width=36.0, height=36.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁstart_event__mutmut_12(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name or "Start",
                              x=self._x_offset, y=self._y_offset, width=36.0, height=36.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁstart_event__mutmut_13(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name or "Start",
                              element_type=BPMNElementType.START_EVENT,
                              y=self._y_offset, width=36.0, height=36.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁstart_event__mutmut_14(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name or "Start",
                              element_type=BPMNElementType.START_EVENT,
                              x=self._x_offset, width=36.0, height=36.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁstart_event__mutmut_15(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name or "Start",
                              element_type=BPMNElementType.START_EVENT,
                              x=self._x_offset, y=self._y_offset, height=36.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁstart_event__mutmut_16(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name or "Start",
                              element_type=BPMNElementType.START_EVENT,
                              x=self._x_offset, y=self._y_offset, width=36.0, )
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁstart_event__mutmut_17(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name and "Start",
                              element_type=BPMNElementType.START_EVENT,
                              x=self._x_offset, y=self._y_offset, width=36.0, height=36.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁstart_event__mutmut_18(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name or "XXStartXX",
                              element_type=BPMNElementType.START_EVENT,
                              x=self._x_offset, y=self._y_offset, width=36.0, height=36.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁstart_event__mutmut_19(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name or "start",
                              element_type=BPMNElementType.START_EVENT,
                              x=self._x_offset, y=self._y_offset, width=36.0, height=36.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁstart_event__mutmut_20(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name or "START",
                              element_type=BPMNElementType.START_EVENT,
                              x=self._x_offset, y=self._y_offset, width=36.0, height=36.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁstart_event__mutmut_21(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name or "Start",
                              element_type=BPMNElementType.START_EVENT,
                              x=self._x_offset, y=self._y_offset, width=37.0, height=36.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁstart_event__mutmut_22(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name or "Start",
                              element_type=BPMNElementType.START_EVENT,
                              x=self._x_offset, y=self._y_offset, width=36.0, height=37.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁstart_event__mutmut_23(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name or "Start",
                              element_type=BPMNElementType.START_EVENT,
                              x=self._x_offset, y=self._y_offset, width=36.0, height=36.0)
        self._process.add_element(None)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁstart_event__mutmut_24(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name or "Start",
                              element_type=BPMNElementType.START_EVENT,
                              x=self._x_offset, y=self._y_offset, width=36.0, height=36.0)
        self._process.add_element(element)
        self._x_offset = self._step_gap
        return self

    def xǁBPMNBuilderǁstart_event__mutmut_25(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name or "Start",
                              element_type=BPMNElementType.START_EVENT,
                              x=self._x_offset, y=self._y_offset, width=36.0, height=36.0)
        self._process.add_element(element)
        self._x_offset -= self._step_gap
        return self

    @_mutmut_mutated(mutants_xǁBPMNBuilderǁend_event__mutmut)
    def end_event(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name or "End",
                              element_type=BPMNElementType.END_EVENT,
                              x=self._x_offset, y=self._y_offset, width=36.0, height=36.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁend_event__mutmut_orig(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name or "End",
                              element_type=BPMNElementType.END_EVENT,
                              x=self._x_offset, y=self._y_offset, width=36.0, height=36.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁend_event__mutmut_1(self, element_id: str, name: str = "XXXX") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name or "End",
                              element_type=BPMNElementType.END_EVENT,
                              x=self._x_offset, y=self._y_offset, width=36.0, height=36.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁend_event__mutmut_2(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = None
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁend_event__mutmut_3(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=None, name=name or "End",
                              element_type=BPMNElementType.END_EVENT,
                              x=self._x_offset, y=self._y_offset, width=36.0, height=36.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁend_event__mutmut_4(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=None,
                              element_type=BPMNElementType.END_EVENT,
                              x=self._x_offset, y=self._y_offset, width=36.0, height=36.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁend_event__mutmut_5(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name or "End",
                              element_type=None,
                              x=self._x_offset, y=self._y_offset, width=36.0, height=36.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁend_event__mutmut_6(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name or "End",
                              element_type=BPMNElementType.END_EVENT,
                              x=None, y=self._y_offset, width=36.0, height=36.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁend_event__mutmut_7(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name or "End",
                              element_type=BPMNElementType.END_EVENT,
                              x=self._x_offset, y=None, width=36.0, height=36.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁend_event__mutmut_8(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name or "End",
                              element_type=BPMNElementType.END_EVENT,
                              x=self._x_offset, y=self._y_offset, width=None, height=36.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁend_event__mutmut_9(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name or "End",
                              element_type=BPMNElementType.END_EVENT,
                              x=self._x_offset, y=self._y_offset, width=36.0, height=None)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁend_event__mutmut_10(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(name=name or "End",
                              element_type=BPMNElementType.END_EVENT,
                              x=self._x_offset, y=self._y_offset, width=36.0, height=36.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁend_event__mutmut_11(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, element_type=BPMNElementType.END_EVENT,
                              x=self._x_offset, y=self._y_offset, width=36.0, height=36.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁend_event__mutmut_12(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name or "End",
                              x=self._x_offset, y=self._y_offset, width=36.0, height=36.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁend_event__mutmut_13(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name or "End",
                              element_type=BPMNElementType.END_EVENT,
                              y=self._y_offset, width=36.0, height=36.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁend_event__mutmut_14(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name or "End",
                              element_type=BPMNElementType.END_EVENT,
                              x=self._x_offset, width=36.0, height=36.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁend_event__mutmut_15(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name or "End",
                              element_type=BPMNElementType.END_EVENT,
                              x=self._x_offset, y=self._y_offset, height=36.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁend_event__mutmut_16(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name or "End",
                              element_type=BPMNElementType.END_EVENT,
                              x=self._x_offset, y=self._y_offset, width=36.0, )
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁend_event__mutmut_17(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name and "End",
                              element_type=BPMNElementType.END_EVENT,
                              x=self._x_offset, y=self._y_offset, width=36.0, height=36.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁend_event__mutmut_18(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name or "XXEndXX",
                              element_type=BPMNElementType.END_EVENT,
                              x=self._x_offset, y=self._y_offset, width=36.0, height=36.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁend_event__mutmut_19(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name or "end",
                              element_type=BPMNElementType.END_EVENT,
                              x=self._x_offset, y=self._y_offset, width=36.0, height=36.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁend_event__mutmut_20(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name or "END",
                              element_type=BPMNElementType.END_EVENT,
                              x=self._x_offset, y=self._y_offset, width=36.0, height=36.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁend_event__mutmut_21(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name or "End",
                              element_type=BPMNElementType.END_EVENT,
                              x=self._x_offset, y=self._y_offset, width=37.0, height=36.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁend_event__mutmut_22(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name or "End",
                              element_type=BPMNElementType.END_EVENT,
                              x=self._x_offset, y=self._y_offset, width=36.0, height=37.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁend_event__mutmut_23(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name or "End",
                              element_type=BPMNElementType.END_EVENT,
                              x=self._x_offset, y=self._y_offset, width=36.0, height=36.0)
        self._process.add_element(None)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁend_event__mutmut_24(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name or "End",
                              element_type=BPMNElementType.END_EVENT,
                              x=self._x_offset, y=self._y_offset, width=36.0, height=36.0)
        self._process.add_element(element)
        self._x_offset = self._step_gap
        return self

    def xǁBPMNBuilderǁend_event__mutmut_25(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name or "End",
                              element_type=BPMNElementType.END_EVENT,
                              x=self._x_offset, y=self._y_offset, width=36.0, height=36.0)
        self._process.add_element(element)
        self._x_offset -= self._step_gap
        return self

    @_mutmut_mutated(mutants_xǁBPMNBuilderǁuser_task__mutmut)
    def user_task(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.USER_TASK,
                              x=self._x_offset, y=self._y_offset, width=self._step_width, height=80.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁuser_task__mutmut_orig(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.USER_TASK,
                              x=self._x_offset, y=self._y_offset, width=self._step_width, height=80.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁuser_task__mutmut_1(self, element_id: str, name: str = "XXXX") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.USER_TASK,
                              x=self._x_offset, y=self._y_offset, width=self._step_width, height=80.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁuser_task__mutmut_2(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = None
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁuser_task__mutmut_3(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=None, name=name,
                              element_type=BPMNElementType.USER_TASK,
                              x=self._x_offset, y=self._y_offset, width=self._step_width, height=80.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁuser_task__mutmut_4(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=None,
                              element_type=BPMNElementType.USER_TASK,
                              x=self._x_offset, y=self._y_offset, width=self._step_width, height=80.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁuser_task__mutmut_5(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=None,
                              x=self._x_offset, y=self._y_offset, width=self._step_width, height=80.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁuser_task__mutmut_6(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.USER_TASK,
                              x=None, y=self._y_offset, width=self._step_width, height=80.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁuser_task__mutmut_7(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.USER_TASK,
                              x=self._x_offset, y=None, width=self._step_width, height=80.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁuser_task__mutmut_8(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.USER_TASK,
                              x=self._x_offset, y=self._y_offset, width=None, height=80.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁuser_task__mutmut_9(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.USER_TASK,
                              x=self._x_offset, y=self._y_offset, width=self._step_width, height=None)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁuser_task__mutmut_10(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(name=name,
                              element_type=BPMNElementType.USER_TASK,
                              x=self._x_offset, y=self._y_offset, width=self._step_width, height=80.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁuser_task__mutmut_11(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, element_type=BPMNElementType.USER_TASK,
                              x=self._x_offset, y=self._y_offset, width=self._step_width, height=80.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁuser_task__mutmut_12(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              x=self._x_offset, y=self._y_offset, width=self._step_width, height=80.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁuser_task__mutmut_13(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.USER_TASK,
                              y=self._y_offset, width=self._step_width, height=80.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁuser_task__mutmut_14(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.USER_TASK,
                              x=self._x_offset, width=self._step_width, height=80.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁuser_task__mutmut_15(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.USER_TASK,
                              x=self._x_offset, y=self._y_offset, height=80.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁuser_task__mutmut_16(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.USER_TASK,
                              x=self._x_offset, y=self._y_offset, width=self._step_width, )
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁuser_task__mutmut_17(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.USER_TASK,
                              x=self._x_offset, y=self._y_offset, width=self._step_width, height=81.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁuser_task__mutmut_18(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.USER_TASK,
                              x=self._x_offset, y=self._y_offset, width=self._step_width, height=80.0)
        self._process.add_element(None)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁuser_task__mutmut_19(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.USER_TASK,
                              x=self._x_offset, y=self._y_offset, width=self._step_width, height=80.0)
        self._process.add_element(element)
        self._x_offset = self._step_gap
        return self

    def xǁBPMNBuilderǁuser_task__mutmut_20(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.USER_TASK,
                              x=self._x_offset, y=self._y_offset, width=self._step_width, height=80.0)
        self._process.add_element(element)
        self._x_offset -= self._step_gap
        return self

    @_mutmut_mutated(mutants_xǁBPMNBuilderǁservice_task__mutmut)
    def service_task(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.SERVICE_TASK,
                              x=self._x_offset, y=self._y_offset, width=self._step_width, height=80.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁservice_task__mutmut_orig(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.SERVICE_TASK,
                              x=self._x_offset, y=self._y_offset, width=self._step_width, height=80.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁservice_task__mutmut_1(self, element_id: str, name: str = "XXXX") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.SERVICE_TASK,
                              x=self._x_offset, y=self._y_offset, width=self._step_width, height=80.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁservice_task__mutmut_2(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = None
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁservice_task__mutmut_3(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=None, name=name,
                              element_type=BPMNElementType.SERVICE_TASK,
                              x=self._x_offset, y=self._y_offset, width=self._step_width, height=80.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁservice_task__mutmut_4(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=None,
                              element_type=BPMNElementType.SERVICE_TASK,
                              x=self._x_offset, y=self._y_offset, width=self._step_width, height=80.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁservice_task__mutmut_5(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=None,
                              x=self._x_offset, y=self._y_offset, width=self._step_width, height=80.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁservice_task__mutmut_6(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.SERVICE_TASK,
                              x=None, y=self._y_offset, width=self._step_width, height=80.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁservice_task__mutmut_7(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.SERVICE_TASK,
                              x=self._x_offset, y=None, width=self._step_width, height=80.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁservice_task__mutmut_8(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.SERVICE_TASK,
                              x=self._x_offset, y=self._y_offset, width=None, height=80.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁservice_task__mutmut_9(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.SERVICE_TASK,
                              x=self._x_offset, y=self._y_offset, width=self._step_width, height=None)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁservice_task__mutmut_10(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(name=name,
                              element_type=BPMNElementType.SERVICE_TASK,
                              x=self._x_offset, y=self._y_offset, width=self._step_width, height=80.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁservice_task__mutmut_11(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, element_type=BPMNElementType.SERVICE_TASK,
                              x=self._x_offset, y=self._y_offset, width=self._step_width, height=80.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁservice_task__mutmut_12(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              x=self._x_offset, y=self._y_offset, width=self._step_width, height=80.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁservice_task__mutmut_13(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.SERVICE_TASK,
                              y=self._y_offset, width=self._step_width, height=80.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁservice_task__mutmut_14(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.SERVICE_TASK,
                              x=self._x_offset, width=self._step_width, height=80.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁservice_task__mutmut_15(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.SERVICE_TASK,
                              x=self._x_offset, y=self._y_offset, height=80.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁservice_task__mutmut_16(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.SERVICE_TASK,
                              x=self._x_offset, y=self._y_offset, width=self._step_width, )
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁservice_task__mutmut_17(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.SERVICE_TASK,
                              x=self._x_offset, y=self._y_offset, width=self._step_width, height=81.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁservice_task__mutmut_18(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.SERVICE_TASK,
                              x=self._x_offset, y=self._y_offset, width=self._step_width, height=80.0)
        self._process.add_element(None)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁservice_task__mutmut_19(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.SERVICE_TASK,
                              x=self._x_offset, y=self._y_offset, width=self._step_width, height=80.0)
        self._process.add_element(element)
        self._x_offset = self._step_gap
        return self

    def xǁBPMNBuilderǁservice_task__mutmut_20(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.SERVICE_TASK,
                              x=self._x_offset, y=self._y_offset, width=self._step_width, height=80.0)
        self._process.add_element(element)
        self._x_offset -= self._step_gap
        return self

    @_mutmut_mutated(mutants_xǁBPMNBuilderǁscript_task__mutmut)
    def script_task(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.SCRIPT_TASK,
                              x=self._x_offset, y=self._y_offset, width=self._step_width, height=80.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁscript_task__mutmut_orig(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.SCRIPT_TASK,
                              x=self._x_offset, y=self._y_offset, width=self._step_width, height=80.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁscript_task__mutmut_1(self, element_id: str, name: str = "XXXX") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.SCRIPT_TASK,
                              x=self._x_offset, y=self._y_offset, width=self._step_width, height=80.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁscript_task__mutmut_2(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = None
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁscript_task__mutmut_3(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=None, name=name,
                              element_type=BPMNElementType.SCRIPT_TASK,
                              x=self._x_offset, y=self._y_offset, width=self._step_width, height=80.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁscript_task__mutmut_4(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=None,
                              element_type=BPMNElementType.SCRIPT_TASK,
                              x=self._x_offset, y=self._y_offset, width=self._step_width, height=80.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁscript_task__mutmut_5(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=None,
                              x=self._x_offset, y=self._y_offset, width=self._step_width, height=80.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁscript_task__mutmut_6(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.SCRIPT_TASK,
                              x=None, y=self._y_offset, width=self._step_width, height=80.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁscript_task__mutmut_7(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.SCRIPT_TASK,
                              x=self._x_offset, y=None, width=self._step_width, height=80.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁscript_task__mutmut_8(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.SCRIPT_TASK,
                              x=self._x_offset, y=self._y_offset, width=None, height=80.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁscript_task__mutmut_9(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.SCRIPT_TASK,
                              x=self._x_offset, y=self._y_offset, width=self._step_width, height=None)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁscript_task__mutmut_10(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(name=name,
                              element_type=BPMNElementType.SCRIPT_TASK,
                              x=self._x_offset, y=self._y_offset, width=self._step_width, height=80.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁscript_task__mutmut_11(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, element_type=BPMNElementType.SCRIPT_TASK,
                              x=self._x_offset, y=self._y_offset, width=self._step_width, height=80.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁscript_task__mutmut_12(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              x=self._x_offset, y=self._y_offset, width=self._step_width, height=80.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁscript_task__mutmut_13(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.SCRIPT_TASK,
                              y=self._y_offset, width=self._step_width, height=80.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁscript_task__mutmut_14(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.SCRIPT_TASK,
                              x=self._x_offset, width=self._step_width, height=80.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁscript_task__mutmut_15(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.SCRIPT_TASK,
                              x=self._x_offset, y=self._y_offset, height=80.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁscript_task__mutmut_16(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.SCRIPT_TASK,
                              x=self._x_offset, y=self._y_offset, width=self._step_width, )
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁscript_task__mutmut_17(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.SCRIPT_TASK,
                              x=self._x_offset, y=self._y_offset, width=self._step_width, height=81.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁscript_task__mutmut_18(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.SCRIPT_TASK,
                              x=self._x_offset, y=self._y_offset, width=self._step_width, height=80.0)
        self._process.add_element(None)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁscript_task__mutmut_19(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.SCRIPT_TASK,
                              x=self._x_offset, y=self._y_offset, width=self._step_width, height=80.0)
        self._process.add_element(element)
        self._x_offset = self._step_gap
        return self

    def xǁBPMNBuilderǁscript_task__mutmut_20(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.SCRIPT_TASK,
                              x=self._x_offset, y=self._y_offset, width=self._step_width, height=80.0)
        self._process.add_element(element)
        self._x_offset -= self._step_gap
        return self

    @_mutmut_mutated(mutants_xǁBPMNBuilderǁexclusive_gateway__mutmut)
    def exclusive_gateway(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.EXCLUSIVE_GATEWAY,
                              x=self._x_offset, y=self._y_offset, width=50.0, height=50.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁexclusive_gateway__mutmut_orig(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.EXCLUSIVE_GATEWAY,
                              x=self._x_offset, y=self._y_offset, width=50.0, height=50.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁexclusive_gateway__mutmut_1(self, element_id: str, name: str = "XXXX") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.EXCLUSIVE_GATEWAY,
                              x=self._x_offset, y=self._y_offset, width=50.0, height=50.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁexclusive_gateway__mutmut_2(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = None
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁexclusive_gateway__mutmut_3(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=None, name=name,
                              element_type=BPMNElementType.EXCLUSIVE_GATEWAY,
                              x=self._x_offset, y=self._y_offset, width=50.0, height=50.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁexclusive_gateway__mutmut_4(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=None,
                              element_type=BPMNElementType.EXCLUSIVE_GATEWAY,
                              x=self._x_offset, y=self._y_offset, width=50.0, height=50.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁexclusive_gateway__mutmut_5(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=None,
                              x=self._x_offset, y=self._y_offset, width=50.0, height=50.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁexclusive_gateway__mutmut_6(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.EXCLUSIVE_GATEWAY,
                              x=None, y=self._y_offset, width=50.0, height=50.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁexclusive_gateway__mutmut_7(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.EXCLUSIVE_GATEWAY,
                              x=self._x_offset, y=None, width=50.0, height=50.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁexclusive_gateway__mutmut_8(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.EXCLUSIVE_GATEWAY,
                              x=self._x_offset, y=self._y_offset, width=None, height=50.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁexclusive_gateway__mutmut_9(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.EXCLUSIVE_GATEWAY,
                              x=self._x_offset, y=self._y_offset, width=50.0, height=None)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁexclusive_gateway__mutmut_10(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(name=name,
                              element_type=BPMNElementType.EXCLUSIVE_GATEWAY,
                              x=self._x_offset, y=self._y_offset, width=50.0, height=50.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁexclusive_gateway__mutmut_11(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, element_type=BPMNElementType.EXCLUSIVE_GATEWAY,
                              x=self._x_offset, y=self._y_offset, width=50.0, height=50.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁexclusive_gateway__mutmut_12(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              x=self._x_offset, y=self._y_offset, width=50.0, height=50.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁexclusive_gateway__mutmut_13(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.EXCLUSIVE_GATEWAY,
                              y=self._y_offset, width=50.0, height=50.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁexclusive_gateway__mutmut_14(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.EXCLUSIVE_GATEWAY,
                              x=self._x_offset, width=50.0, height=50.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁexclusive_gateway__mutmut_15(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.EXCLUSIVE_GATEWAY,
                              x=self._x_offset, y=self._y_offset, height=50.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁexclusive_gateway__mutmut_16(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.EXCLUSIVE_GATEWAY,
                              x=self._x_offset, y=self._y_offset, width=50.0, )
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁexclusive_gateway__mutmut_17(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.EXCLUSIVE_GATEWAY,
                              x=self._x_offset, y=self._y_offset, width=51.0, height=50.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁexclusive_gateway__mutmut_18(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.EXCLUSIVE_GATEWAY,
                              x=self._x_offset, y=self._y_offset, width=50.0, height=51.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁexclusive_gateway__mutmut_19(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.EXCLUSIVE_GATEWAY,
                              x=self._x_offset, y=self._y_offset, width=50.0, height=50.0)
        self._process.add_element(None)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁexclusive_gateway__mutmut_20(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.EXCLUSIVE_GATEWAY,
                              x=self._x_offset, y=self._y_offset, width=50.0, height=50.0)
        self._process.add_element(element)
        self._x_offset = self._step_gap
        return self

    def xǁBPMNBuilderǁexclusive_gateway__mutmut_21(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.EXCLUSIVE_GATEWAY,
                              x=self._x_offset, y=self._y_offset, width=50.0, height=50.0)
        self._process.add_element(element)
        self._x_offset -= self._step_gap
        return self

    @_mutmut_mutated(mutants_xǁBPMNBuilderǁparallel_gateway__mutmut)
    def parallel_gateway(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.PARALLEL_GATEWAY,
                              x=self._x_offset, y=self._y_offset, width=50.0, height=50.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁparallel_gateway__mutmut_orig(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.PARALLEL_GATEWAY,
                              x=self._x_offset, y=self._y_offset, width=50.0, height=50.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁparallel_gateway__mutmut_1(self, element_id: str, name: str = "XXXX") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.PARALLEL_GATEWAY,
                              x=self._x_offset, y=self._y_offset, width=50.0, height=50.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁparallel_gateway__mutmut_2(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = None
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁparallel_gateway__mutmut_3(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=None, name=name,
                              element_type=BPMNElementType.PARALLEL_GATEWAY,
                              x=self._x_offset, y=self._y_offset, width=50.0, height=50.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁparallel_gateway__mutmut_4(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=None,
                              element_type=BPMNElementType.PARALLEL_GATEWAY,
                              x=self._x_offset, y=self._y_offset, width=50.0, height=50.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁparallel_gateway__mutmut_5(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=None,
                              x=self._x_offset, y=self._y_offset, width=50.0, height=50.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁparallel_gateway__mutmut_6(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.PARALLEL_GATEWAY,
                              x=None, y=self._y_offset, width=50.0, height=50.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁparallel_gateway__mutmut_7(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.PARALLEL_GATEWAY,
                              x=self._x_offset, y=None, width=50.0, height=50.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁparallel_gateway__mutmut_8(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.PARALLEL_GATEWAY,
                              x=self._x_offset, y=self._y_offset, width=None, height=50.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁparallel_gateway__mutmut_9(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.PARALLEL_GATEWAY,
                              x=self._x_offset, y=self._y_offset, width=50.0, height=None)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁparallel_gateway__mutmut_10(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(name=name,
                              element_type=BPMNElementType.PARALLEL_GATEWAY,
                              x=self._x_offset, y=self._y_offset, width=50.0, height=50.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁparallel_gateway__mutmut_11(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, element_type=BPMNElementType.PARALLEL_GATEWAY,
                              x=self._x_offset, y=self._y_offset, width=50.0, height=50.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁparallel_gateway__mutmut_12(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              x=self._x_offset, y=self._y_offset, width=50.0, height=50.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁparallel_gateway__mutmut_13(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.PARALLEL_GATEWAY,
                              y=self._y_offset, width=50.0, height=50.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁparallel_gateway__mutmut_14(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.PARALLEL_GATEWAY,
                              x=self._x_offset, width=50.0, height=50.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁparallel_gateway__mutmut_15(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.PARALLEL_GATEWAY,
                              x=self._x_offset, y=self._y_offset, height=50.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁparallel_gateway__mutmut_16(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.PARALLEL_GATEWAY,
                              x=self._x_offset, y=self._y_offset, width=50.0, )
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁparallel_gateway__mutmut_17(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.PARALLEL_GATEWAY,
                              x=self._x_offset, y=self._y_offset, width=51.0, height=50.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁparallel_gateway__mutmut_18(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.PARALLEL_GATEWAY,
                              x=self._x_offset, y=self._y_offset, width=50.0, height=51.0)
        self._process.add_element(element)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁparallel_gateway__mutmut_19(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.PARALLEL_GATEWAY,
                              x=self._x_offset, y=self._y_offset, width=50.0, height=50.0)
        self._process.add_element(None)
        self._x_offset += self._step_gap
        return self

    def xǁBPMNBuilderǁparallel_gateway__mutmut_20(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.PARALLEL_GATEWAY,
                              x=self._x_offset, y=self._y_offset, width=50.0, height=50.0)
        self._process.add_element(element)
        self._x_offset = self._step_gap
        return self

    def xǁBPMNBuilderǁparallel_gateway__mutmut_21(self, element_id: str, name: str = "") -> BPMNBuilder:
        element = BPMNElement(element_id=element_id, name=name,
                              element_type=BPMNElementType.PARALLEL_GATEWAY,
                              x=self._x_offset, y=self._y_offset, width=50.0, height=50.0)
        self._process.add_element(element)
        self._x_offset -= self._step_gap
        return self

    @_mutmut_mutated(mutants_xǁBPMNBuilderǁconnect__mutmut)
    def connect(self, source_id: str, target_id: str, name: str = "", condition: str = "") -> BPMNBuilder:
        flow = BPMNSequenceFlow(flow_id=f"flow_{source_id}_to_{target_id}", name=name,
                                source_ref=source_id, target_ref=target_id, condition_expression=condition)
        self._process.add_flow(flow)
        return self

    def xǁBPMNBuilderǁconnect__mutmut_orig(self, source_id: str, target_id: str, name: str = "", condition: str = "") -> BPMNBuilder:
        flow = BPMNSequenceFlow(flow_id=f"flow_{source_id}_to_{target_id}", name=name,
                                source_ref=source_id, target_ref=target_id, condition_expression=condition)
        self._process.add_flow(flow)
        return self

    def xǁBPMNBuilderǁconnect__mutmut_1(self, source_id: str, target_id: str, name: str = "XXXX", condition: str = "") -> BPMNBuilder:
        flow = BPMNSequenceFlow(flow_id=f"flow_{source_id}_to_{target_id}", name=name,
                                source_ref=source_id, target_ref=target_id, condition_expression=condition)
        self._process.add_flow(flow)
        return self

    def xǁBPMNBuilderǁconnect__mutmut_2(self, source_id: str, target_id: str, name: str = "", condition: str = "XXXX") -> BPMNBuilder:
        flow = BPMNSequenceFlow(flow_id=f"flow_{source_id}_to_{target_id}", name=name,
                                source_ref=source_id, target_ref=target_id, condition_expression=condition)
        self._process.add_flow(flow)
        return self

    def xǁBPMNBuilderǁconnect__mutmut_3(self, source_id: str, target_id: str, name: str = "", condition: str = "") -> BPMNBuilder:
        flow = None
        self._process.add_flow(flow)
        return self

    def xǁBPMNBuilderǁconnect__mutmut_4(self, source_id: str, target_id: str, name: str = "", condition: str = "") -> BPMNBuilder:
        flow = BPMNSequenceFlow(flow_id=None, name=name,
                                source_ref=source_id, target_ref=target_id, condition_expression=condition)
        self._process.add_flow(flow)
        return self

    def xǁBPMNBuilderǁconnect__mutmut_5(self, source_id: str, target_id: str, name: str = "", condition: str = "") -> BPMNBuilder:
        flow = BPMNSequenceFlow(flow_id=f"flow_{source_id}_to_{target_id}", name=None,
                                source_ref=source_id, target_ref=target_id, condition_expression=condition)
        self._process.add_flow(flow)
        return self

    def xǁBPMNBuilderǁconnect__mutmut_6(self, source_id: str, target_id: str, name: str = "", condition: str = "") -> BPMNBuilder:
        flow = BPMNSequenceFlow(flow_id=f"flow_{source_id}_to_{target_id}", name=name,
                                source_ref=None, target_ref=target_id, condition_expression=condition)
        self._process.add_flow(flow)
        return self

    def xǁBPMNBuilderǁconnect__mutmut_7(self, source_id: str, target_id: str, name: str = "", condition: str = "") -> BPMNBuilder:
        flow = BPMNSequenceFlow(flow_id=f"flow_{source_id}_to_{target_id}", name=name,
                                source_ref=source_id, target_ref=None, condition_expression=condition)
        self._process.add_flow(flow)
        return self

    def xǁBPMNBuilderǁconnect__mutmut_8(self, source_id: str, target_id: str, name: str = "", condition: str = "") -> BPMNBuilder:
        flow = BPMNSequenceFlow(flow_id=f"flow_{source_id}_to_{target_id}", name=name,
                                source_ref=source_id, target_ref=target_id, condition_expression=None)
        self._process.add_flow(flow)
        return self

    def xǁBPMNBuilderǁconnect__mutmut_9(self, source_id: str, target_id: str, name: str = "", condition: str = "") -> BPMNBuilder:
        flow = BPMNSequenceFlow(name=name,
                                source_ref=source_id, target_ref=target_id, condition_expression=condition)
        self._process.add_flow(flow)
        return self

    def xǁBPMNBuilderǁconnect__mutmut_10(self, source_id: str, target_id: str, name: str = "", condition: str = "") -> BPMNBuilder:
        flow = BPMNSequenceFlow(flow_id=f"flow_{source_id}_to_{target_id}", source_ref=source_id, target_ref=target_id, condition_expression=condition)
        self._process.add_flow(flow)
        return self

    def xǁBPMNBuilderǁconnect__mutmut_11(self, source_id: str, target_id: str, name: str = "", condition: str = "") -> BPMNBuilder:
        flow = BPMNSequenceFlow(flow_id=f"flow_{source_id}_to_{target_id}", name=name,
                                target_ref=target_id, condition_expression=condition)
        self._process.add_flow(flow)
        return self

    def xǁBPMNBuilderǁconnect__mutmut_12(self, source_id: str, target_id: str, name: str = "", condition: str = "") -> BPMNBuilder:
        flow = BPMNSequenceFlow(flow_id=f"flow_{source_id}_to_{target_id}", name=name,
                                source_ref=source_id, condition_expression=condition)
        self._process.add_flow(flow)
        return self

    def xǁBPMNBuilderǁconnect__mutmut_13(self, source_id: str, target_id: str, name: str = "", condition: str = "") -> BPMNBuilder:
        flow = BPMNSequenceFlow(flow_id=f"flow_{source_id}_to_{target_id}", name=name,
                                source_ref=source_id, target_ref=target_id, )
        self._process.add_flow(flow)
        return self

    def xǁBPMNBuilderǁconnect__mutmut_14(self, source_id: str, target_id: str, name: str = "", condition: str = "") -> BPMNBuilder:
        flow = BPMNSequenceFlow(flow_id=f"flow_{source_id}_to_{target_id}", name=name,
                                source_ref=source_id, target_ref=target_id, condition_expression=condition)
        self._process.add_flow(None)
        return self

    def build(self) -> BPMNProcess:
        """Build and return the BPMN process."""
        return self._process

mutants_xǁBPMNBuilderǁ__init____mutmut['_mutmut_orig'] = BPMNBuilder.xǁBPMNBuilderǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁ__init____mutmut['xǁBPMNBuilderǁ__init____mutmut_1'] = BPMNBuilder.xǁBPMNBuilderǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁ__init____mutmut['xǁBPMNBuilderǁ__init____mutmut_2'] = BPMNBuilder.xǁBPMNBuilderǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁ__init____mutmut['xǁBPMNBuilderǁ__init____mutmut_3'] = BPMNBuilder.xǁBPMNBuilderǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁ__init____mutmut['xǁBPMNBuilderǁ__init____mutmut_4'] = BPMNBuilder.xǁBPMNBuilderǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁ__init____mutmut['xǁBPMNBuilderǁ__init____mutmut_5'] = BPMNBuilder.xǁBPMNBuilderǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁ__init____mutmut['xǁBPMNBuilderǁ__init____mutmut_6'] = BPMNBuilder.xǁBPMNBuilderǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁ__init____mutmut['xǁBPMNBuilderǁ__init____mutmut_7'] = BPMNBuilder.xǁBPMNBuilderǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁ__init____mutmut['xǁBPMNBuilderǁ__init____mutmut_8'] = BPMNBuilder.xǁBPMNBuilderǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁ__init____mutmut['xǁBPMNBuilderǁ__init____mutmut_9'] = BPMNBuilder.xǁBPMNBuilderǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁ__init____mutmut['xǁBPMNBuilderǁ__init____mutmut_10'] = BPMNBuilder.xǁBPMNBuilderǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁ__init____mutmut['xǁBPMNBuilderǁ__init____mutmut_11'] = BPMNBuilder.xǁBPMNBuilderǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁ__init____mutmut['xǁBPMNBuilderǁ__init____mutmut_12'] = BPMNBuilder.xǁBPMNBuilderǁ__init____mutmut_12 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁ__init____mutmut['xǁBPMNBuilderǁ__init____mutmut_13'] = BPMNBuilder.xǁBPMNBuilderǁ__init____mutmut_13 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁ__init____mutmut['xǁBPMNBuilderǁ__init____mutmut_14'] = BPMNBuilder.xǁBPMNBuilderǁ__init____mutmut_14 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁ__init____mutmut['xǁBPMNBuilderǁ__init____mutmut_15'] = BPMNBuilder.xǁBPMNBuilderǁ__init____mutmut_15 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁ__init____mutmut['xǁBPMNBuilderǁ__init____mutmut_16'] = BPMNBuilder.xǁBPMNBuilderǁ__init____mutmut_16 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁ__init____mutmut['xǁBPMNBuilderǁ__init____mutmut_17'] = BPMNBuilder.xǁBPMNBuilderǁ__init____mutmut_17 # type: ignore # mutmut generated

mutants_xǁBPMNBuilderǁstart_event__mutmut['_mutmut_orig'] = BPMNBuilder.xǁBPMNBuilderǁstart_event__mutmut_orig # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁstart_event__mutmut['xǁBPMNBuilderǁstart_event__mutmut_1'] = BPMNBuilder.xǁBPMNBuilderǁstart_event__mutmut_1 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁstart_event__mutmut['xǁBPMNBuilderǁstart_event__mutmut_2'] = BPMNBuilder.xǁBPMNBuilderǁstart_event__mutmut_2 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁstart_event__mutmut['xǁBPMNBuilderǁstart_event__mutmut_3'] = BPMNBuilder.xǁBPMNBuilderǁstart_event__mutmut_3 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁstart_event__mutmut['xǁBPMNBuilderǁstart_event__mutmut_4'] = BPMNBuilder.xǁBPMNBuilderǁstart_event__mutmut_4 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁstart_event__mutmut['xǁBPMNBuilderǁstart_event__mutmut_5'] = BPMNBuilder.xǁBPMNBuilderǁstart_event__mutmut_5 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁstart_event__mutmut['xǁBPMNBuilderǁstart_event__mutmut_6'] = BPMNBuilder.xǁBPMNBuilderǁstart_event__mutmut_6 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁstart_event__mutmut['xǁBPMNBuilderǁstart_event__mutmut_7'] = BPMNBuilder.xǁBPMNBuilderǁstart_event__mutmut_7 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁstart_event__mutmut['xǁBPMNBuilderǁstart_event__mutmut_8'] = BPMNBuilder.xǁBPMNBuilderǁstart_event__mutmut_8 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁstart_event__mutmut['xǁBPMNBuilderǁstart_event__mutmut_9'] = BPMNBuilder.xǁBPMNBuilderǁstart_event__mutmut_9 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁstart_event__mutmut['xǁBPMNBuilderǁstart_event__mutmut_10'] = BPMNBuilder.xǁBPMNBuilderǁstart_event__mutmut_10 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁstart_event__mutmut['xǁBPMNBuilderǁstart_event__mutmut_11'] = BPMNBuilder.xǁBPMNBuilderǁstart_event__mutmut_11 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁstart_event__mutmut['xǁBPMNBuilderǁstart_event__mutmut_12'] = BPMNBuilder.xǁBPMNBuilderǁstart_event__mutmut_12 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁstart_event__mutmut['xǁBPMNBuilderǁstart_event__mutmut_13'] = BPMNBuilder.xǁBPMNBuilderǁstart_event__mutmut_13 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁstart_event__mutmut['xǁBPMNBuilderǁstart_event__mutmut_14'] = BPMNBuilder.xǁBPMNBuilderǁstart_event__mutmut_14 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁstart_event__mutmut['xǁBPMNBuilderǁstart_event__mutmut_15'] = BPMNBuilder.xǁBPMNBuilderǁstart_event__mutmut_15 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁstart_event__mutmut['xǁBPMNBuilderǁstart_event__mutmut_16'] = BPMNBuilder.xǁBPMNBuilderǁstart_event__mutmut_16 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁstart_event__mutmut['xǁBPMNBuilderǁstart_event__mutmut_17'] = BPMNBuilder.xǁBPMNBuilderǁstart_event__mutmut_17 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁstart_event__mutmut['xǁBPMNBuilderǁstart_event__mutmut_18'] = BPMNBuilder.xǁBPMNBuilderǁstart_event__mutmut_18 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁstart_event__mutmut['xǁBPMNBuilderǁstart_event__mutmut_19'] = BPMNBuilder.xǁBPMNBuilderǁstart_event__mutmut_19 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁstart_event__mutmut['xǁBPMNBuilderǁstart_event__mutmut_20'] = BPMNBuilder.xǁBPMNBuilderǁstart_event__mutmut_20 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁstart_event__mutmut['xǁBPMNBuilderǁstart_event__mutmut_21'] = BPMNBuilder.xǁBPMNBuilderǁstart_event__mutmut_21 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁstart_event__mutmut['xǁBPMNBuilderǁstart_event__mutmut_22'] = BPMNBuilder.xǁBPMNBuilderǁstart_event__mutmut_22 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁstart_event__mutmut['xǁBPMNBuilderǁstart_event__mutmut_23'] = BPMNBuilder.xǁBPMNBuilderǁstart_event__mutmut_23 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁstart_event__mutmut['xǁBPMNBuilderǁstart_event__mutmut_24'] = BPMNBuilder.xǁBPMNBuilderǁstart_event__mutmut_24 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁstart_event__mutmut['xǁBPMNBuilderǁstart_event__mutmut_25'] = BPMNBuilder.xǁBPMNBuilderǁstart_event__mutmut_25 # type: ignore # mutmut generated

mutants_xǁBPMNBuilderǁend_event__mutmut['_mutmut_orig'] = BPMNBuilder.xǁBPMNBuilderǁend_event__mutmut_orig # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁend_event__mutmut['xǁBPMNBuilderǁend_event__mutmut_1'] = BPMNBuilder.xǁBPMNBuilderǁend_event__mutmut_1 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁend_event__mutmut['xǁBPMNBuilderǁend_event__mutmut_2'] = BPMNBuilder.xǁBPMNBuilderǁend_event__mutmut_2 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁend_event__mutmut['xǁBPMNBuilderǁend_event__mutmut_3'] = BPMNBuilder.xǁBPMNBuilderǁend_event__mutmut_3 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁend_event__mutmut['xǁBPMNBuilderǁend_event__mutmut_4'] = BPMNBuilder.xǁBPMNBuilderǁend_event__mutmut_4 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁend_event__mutmut['xǁBPMNBuilderǁend_event__mutmut_5'] = BPMNBuilder.xǁBPMNBuilderǁend_event__mutmut_5 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁend_event__mutmut['xǁBPMNBuilderǁend_event__mutmut_6'] = BPMNBuilder.xǁBPMNBuilderǁend_event__mutmut_6 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁend_event__mutmut['xǁBPMNBuilderǁend_event__mutmut_7'] = BPMNBuilder.xǁBPMNBuilderǁend_event__mutmut_7 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁend_event__mutmut['xǁBPMNBuilderǁend_event__mutmut_8'] = BPMNBuilder.xǁBPMNBuilderǁend_event__mutmut_8 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁend_event__mutmut['xǁBPMNBuilderǁend_event__mutmut_9'] = BPMNBuilder.xǁBPMNBuilderǁend_event__mutmut_9 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁend_event__mutmut['xǁBPMNBuilderǁend_event__mutmut_10'] = BPMNBuilder.xǁBPMNBuilderǁend_event__mutmut_10 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁend_event__mutmut['xǁBPMNBuilderǁend_event__mutmut_11'] = BPMNBuilder.xǁBPMNBuilderǁend_event__mutmut_11 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁend_event__mutmut['xǁBPMNBuilderǁend_event__mutmut_12'] = BPMNBuilder.xǁBPMNBuilderǁend_event__mutmut_12 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁend_event__mutmut['xǁBPMNBuilderǁend_event__mutmut_13'] = BPMNBuilder.xǁBPMNBuilderǁend_event__mutmut_13 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁend_event__mutmut['xǁBPMNBuilderǁend_event__mutmut_14'] = BPMNBuilder.xǁBPMNBuilderǁend_event__mutmut_14 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁend_event__mutmut['xǁBPMNBuilderǁend_event__mutmut_15'] = BPMNBuilder.xǁBPMNBuilderǁend_event__mutmut_15 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁend_event__mutmut['xǁBPMNBuilderǁend_event__mutmut_16'] = BPMNBuilder.xǁBPMNBuilderǁend_event__mutmut_16 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁend_event__mutmut['xǁBPMNBuilderǁend_event__mutmut_17'] = BPMNBuilder.xǁBPMNBuilderǁend_event__mutmut_17 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁend_event__mutmut['xǁBPMNBuilderǁend_event__mutmut_18'] = BPMNBuilder.xǁBPMNBuilderǁend_event__mutmut_18 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁend_event__mutmut['xǁBPMNBuilderǁend_event__mutmut_19'] = BPMNBuilder.xǁBPMNBuilderǁend_event__mutmut_19 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁend_event__mutmut['xǁBPMNBuilderǁend_event__mutmut_20'] = BPMNBuilder.xǁBPMNBuilderǁend_event__mutmut_20 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁend_event__mutmut['xǁBPMNBuilderǁend_event__mutmut_21'] = BPMNBuilder.xǁBPMNBuilderǁend_event__mutmut_21 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁend_event__mutmut['xǁBPMNBuilderǁend_event__mutmut_22'] = BPMNBuilder.xǁBPMNBuilderǁend_event__mutmut_22 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁend_event__mutmut['xǁBPMNBuilderǁend_event__mutmut_23'] = BPMNBuilder.xǁBPMNBuilderǁend_event__mutmut_23 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁend_event__mutmut['xǁBPMNBuilderǁend_event__mutmut_24'] = BPMNBuilder.xǁBPMNBuilderǁend_event__mutmut_24 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁend_event__mutmut['xǁBPMNBuilderǁend_event__mutmut_25'] = BPMNBuilder.xǁBPMNBuilderǁend_event__mutmut_25 # type: ignore # mutmut generated

mutants_xǁBPMNBuilderǁuser_task__mutmut['_mutmut_orig'] = BPMNBuilder.xǁBPMNBuilderǁuser_task__mutmut_orig # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁuser_task__mutmut['xǁBPMNBuilderǁuser_task__mutmut_1'] = BPMNBuilder.xǁBPMNBuilderǁuser_task__mutmut_1 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁuser_task__mutmut['xǁBPMNBuilderǁuser_task__mutmut_2'] = BPMNBuilder.xǁBPMNBuilderǁuser_task__mutmut_2 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁuser_task__mutmut['xǁBPMNBuilderǁuser_task__mutmut_3'] = BPMNBuilder.xǁBPMNBuilderǁuser_task__mutmut_3 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁuser_task__mutmut['xǁBPMNBuilderǁuser_task__mutmut_4'] = BPMNBuilder.xǁBPMNBuilderǁuser_task__mutmut_4 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁuser_task__mutmut['xǁBPMNBuilderǁuser_task__mutmut_5'] = BPMNBuilder.xǁBPMNBuilderǁuser_task__mutmut_5 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁuser_task__mutmut['xǁBPMNBuilderǁuser_task__mutmut_6'] = BPMNBuilder.xǁBPMNBuilderǁuser_task__mutmut_6 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁuser_task__mutmut['xǁBPMNBuilderǁuser_task__mutmut_7'] = BPMNBuilder.xǁBPMNBuilderǁuser_task__mutmut_7 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁuser_task__mutmut['xǁBPMNBuilderǁuser_task__mutmut_8'] = BPMNBuilder.xǁBPMNBuilderǁuser_task__mutmut_8 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁuser_task__mutmut['xǁBPMNBuilderǁuser_task__mutmut_9'] = BPMNBuilder.xǁBPMNBuilderǁuser_task__mutmut_9 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁuser_task__mutmut['xǁBPMNBuilderǁuser_task__mutmut_10'] = BPMNBuilder.xǁBPMNBuilderǁuser_task__mutmut_10 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁuser_task__mutmut['xǁBPMNBuilderǁuser_task__mutmut_11'] = BPMNBuilder.xǁBPMNBuilderǁuser_task__mutmut_11 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁuser_task__mutmut['xǁBPMNBuilderǁuser_task__mutmut_12'] = BPMNBuilder.xǁBPMNBuilderǁuser_task__mutmut_12 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁuser_task__mutmut['xǁBPMNBuilderǁuser_task__mutmut_13'] = BPMNBuilder.xǁBPMNBuilderǁuser_task__mutmut_13 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁuser_task__mutmut['xǁBPMNBuilderǁuser_task__mutmut_14'] = BPMNBuilder.xǁBPMNBuilderǁuser_task__mutmut_14 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁuser_task__mutmut['xǁBPMNBuilderǁuser_task__mutmut_15'] = BPMNBuilder.xǁBPMNBuilderǁuser_task__mutmut_15 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁuser_task__mutmut['xǁBPMNBuilderǁuser_task__mutmut_16'] = BPMNBuilder.xǁBPMNBuilderǁuser_task__mutmut_16 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁuser_task__mutmut['xǁBPMNBuilderǁuser_task__mutmut_17'] = BPMNBuilder.xǁBPMNBuilderǁuser_task__mutmut_17 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁuser_task__mutmut['xǁBPMNBuilderǁuser_task__mutmut_18'] = BPMNBuilder.xǁBPMNBuilderǁuser_task__mutmut_18 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁuser_task__mutmut['xǁBPMNBuilderǁuser_task__mutmut_19'] = BPMNBuilder.xǁBPMNBuilderǁuser_task__mutmut_19 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁuser_task__mutmut['xǁBPMNBuilderǁuser_task__mutmut_20'] = BPMNBuilder.xǁBPMNBuilderǁuser_task__mutmut_20 # type: ignore # mutmut generated

mutants_xǁBPMNBuilderǁservice_task__mutmut['_mutmut_orig'] = BPMNBuilder.xǁBPMNBuilderǁservice_task__mutmut_orig # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁservice_task__mutmut['xǁBPMNBuilderǁservice_task__mutmut_1'] = BPMNBuilder.xǁBPMNBuilderǁservice_task__mutmut_1 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁservice_task__mutmut['xǁBPMNBuilderǁservice_task__mutmut_2'] = BPMNBuilder.xǁBPMNBuilderǁservice_task__mutmut_2 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁservice_task__mutmut['xǁBPMNBuilderǁservice_task__mutmut_3'] = BPMNBuilder.xǁBPMNBuilderǁservice_task__mutmut_3 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁservice_task__mutmut['xǁBPMNBuilderǁservice_task__mutmut_4'] = BPMNBuilder.xǁBPMNBuilderǁservice_task__mutmut_4 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁservice_task__mutmut['xǁBPMNBuilderǁservice_task__mutmut_5'] = BPMNBuilder.xǁBPMNBuilderǁservice_task__mutmut_5 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁservice_task__mutmut['xǁBPMNBuilderǁservice_task__mutmut_6'] = BPMNBuilder.xǁBPMNBuilderǁservice_task__mutmut_6 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁservice_task__mutmut['xǁBPMNBuilderǁservice_task__mutmut_7'] = BPMNBuilder.xǁBPMNBuilderǁservice_task__mutmut_7 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁservice_task__mutmut['xǁBPMNBuilderǁservice_task__mutmut_8'] = BPMNBuilder.xǁBPMNBuilderǁservice_task__mutmut_8 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁservice_task__mutmut['xǁBPMNBuilderǁservice_task__mutmut_9'] = BPMNBuilder.xǁBPMNBuilderǁservice_task__mutmut_9 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁservice_task__mutmut['xǁBPMNBuilderǁservice_task__mutmut_10'] = BPMNBuilder.xǁBPMNBuilderǁservice_task__mutmut_10 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁservice_task__mutmut['xǁBPMNBuilderǁservice_task__mutmut_11'] = BPMNBuilder.xǁBPMNBuilderǁservice_task__mutmut_11 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁservice_task__mutmut['xǁBPMNBuilderǁservice_task__mutmut_12'] = BPMNBuilder.xǁBPMNBuilderǁservice_task__mutmut_12 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁservice_task__mutmut['xǁBPMNBuilderǁservice_task__mutmut_13'] = BPMNBuilder.xǁBPMNBuilderǁservice_task__mutmut_13 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁservice_task__mutmut['xǁBPMNBuilderǁservice_task__mutmut_14'] = BPMNBuilder.xǁBPMNBuilderǁservice_task__mutmut_14 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁservice_task__mutmut['xǁBPMNBuilderǁservice_task__mutmut_15'] = BPMNBuilder.xǁBPMNBuilderǁservice_task__mutmut_15 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁservice_task__mutmut['xǁBPMNBuilderǁservice_task__mutmut_16'] = BPMNBuilder.xǁBPMNBuilderǁservice_task__mutmut_16 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁservice_task__mutmut['xǁBPMNBuilderǁservice_task__mutmut_17'] = BPMNBuilder.xǁBPMNBuilderǁservice_task__mutmut_17 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁservice_task__mutmut['xǁBPMNBuilderǁservice_task__mutmut_18'] = BPMNBuilder.xǁBPMNBuilderǁservice_task__mutmut_18 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁservice_task__mutmut['xǁBPMNBuilderǁservice_task__mutmut_19'] = BPMNBuilder.xǁBPMNBuilderǁservice_task__mutmut_19 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁservice_task__mutmut['xǁBPMNBuilderǁservice_task__mutmut_20'] = BPMNBuilder.xǁBPMNBuilderǁservice_task__mutmut_20 # type: ignore # mutmut generated

mutants_xǁBPMNBuilderǁscript_task__mutmut['_mutmut_orig'] = BPMNBuilder.xǁBPMNBuilderǁscript_task__mutmut_orig # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁscript_task__mutmut['xǁBPMNBuilderǁscript_task__mutmut_1'] = BPMNBuilder.xǁBPMNBuilderǁscript_task__mutmut_1 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁscript_task__mutmut['xǁBPMNBuilderǁscript_task__mutmut_2'] = BPMNBuilder.xǁBPMNBuilderǁscript_task__mutmut_2 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁscript_task__mutmut['xǁBPMNBuilderǁscript_task__mutmut_3'] = BPMNBuilder.xǁBPMNBuilderǁscript_task__mutmut_3 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁscript_task__mutmut['xǁBPMNBuilderǁscript_task__mutmut_4'] = BPMNBuilder.xǁBPMNBuilderǁscript_task__mutmut_4 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁscript_task__mutmut['xǁBPMNBuilderǁscript_task__mutmut_5'] = BPMNBuilder.xǁBPMNBuilderǁscript_task__mutmut_5 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁscript_task__mutmut['xǁBPMNBuilderǁscript_task__mutmut_6'] = BPMNBuilder.xǁBPMNBuilderǁscript_task__mutmut_6 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁscript_task__mutmut['xǁBPMNBuilderǁscript_task__mutmut_7'] = BPMNBuilder.xǁBPMNBuilderǁscript_task__mutmut_7 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁscript_task__mutmut['xǁBPMNBuilderǁscript_task__mutmut_8'] = BPMNBuilder.xǁBPMNBuilderǁscript_task__mutmut_8 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁscript_task__mutmut['xǁBPMNBuilderǁscript_task__mutmut_9'] = BPMNBuilder.xǁBPMNBuilderǁscript_task__mutmut_9 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁscript_task__mutmut['xǁBPMNBuilderǁscript_task__mutmut_10'] = BPMNBuilder.xǁBPMNBuilderǁscript_task__mutmut_10 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁscript_task__mutmut['xǁBPMNBuilderǁscript_task__mutmut_11'] = BPMNBuilder.xǁBPMNBuilderǁscript_task__mutmut_11 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁscript_task__mutmut['xǁBPMNBuilderǁscript_task__mutmut_12'] = BPMNBuilder.xǁBPMNBuilderǁscript_task__mutmut_12 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁscript_task__mutmut['xǁBPMNBuilderǁscript_task__mutmut_13'] = BPMNBuilder.xǁBPMNBuilderǁscript_task__mutmut_13 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁscript_task__mutmut['xǁBPMNBuilderǁscript_task__mutmut_14'] = BPMNBuilder.xǁBPMNBuilderǁscript_task__mutmut_14 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁscript_task__mutmut['xǁBPMNBuilderǁscript_task__mutmut_15'] = BPMNBuilder.xǁBPMNBuilderǁscript_task__mutmut_15 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁscript_task__mutmut['xǁBPMNBuilderǁscript_task__mutmut_16'] = BPMNBuilder.xǁBPMNBuilderǁscript_task__mutmut_16 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁscript_task__mutmut['xǁBPMNBuilderǁscript_task__mutmut_17'] = BPMNBuilder.xǁBPMNBuilderǁscript_task__mutmut_17 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁscript_task__mutmut['xǁBPMNBuilderǁscript_task__mutmut_18'] = BPMNBuilder.xǁBPMNBuilderǁscript_task__mutmut_18 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁscript_task__mutmut['xǁBPMNBuilderǁscript_task__mutmut_19'] = BPMNBuilder.xǁBPMNBuilderǁscript_task__mutmut_19 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁscript_task__mutmut['xǁBPMNBuilderǁscript_task__mutmut_20'] = BPMNBuilder.xǁBPMNBuilderǁscript_task__mutmut_20 # type: ignore # mutmut generated

mutants_xǁBPMNBuilderǁexclusive_gateway__mutmut['_mutmut_orig'] = BPMNBuilder.xǁBPMNBuilderǁexclusive_gateway__mutmut_orig # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁexclusive_gateway__mutmut['xǁBPMNBuilderǁexclusive_gateway__mutmut_1'] = BPMNBuilder.xǁBPMNBuilderǁexclusive_gateway__mutmut_1 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁexclusive_gateway__mutmut['xǁBPMNBuilderǁexclusive_gateway__mutmut_2'] = BPMNBuilder.xǁBPMNBuilderǁexclusive_gateway__mutmut_2 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁexclusive_gateway__mutmut['xǁBPMNBuilderǁexclusive_gateway__mutmut_3'] = BPMNBuilder.xǁBPMNBuilderǁexclusive_gateway__mutmut_3 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁexclusive_gateway__mutmut['xǁBPMNBuilderǁexclusive_gateway__mutmut_4'] = BPMNBuilder.xǁBPMNBuilderǁexclusive_gateway__mutmut_4 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁexclusive_gateway__mutmut['xǁBPMNBuilderǁexclusive_gateway__mutmut_5'] = BPMNBuilder.xǁBPMNBuilderǁexclusive_gateway__mutmut_5 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁexclusive_gateway__mutmut['xǁBPMNBuilderǁexclusive_gateway__mutmut_6'] = BPMNBuilder.xǁBPMNBuilderǁexclusive_gateway__mutmut_6 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁexclusive_gateway__mutmut['xǁBPMNBuilderǁexclusive_gateway__mutmut_7'] = BPMNBuilder.xǁBPMNBuilderǁexclusive_gateway__mutmut_7 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁexclusive_gateway__mutmut['xǁBPMNBuilderǁexclusive_gateway__mutmut_8'] = BPMNBuilder.xǁBPMNBuilderǁexclusive_gateway__mutmut_8 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁexclusive_gateway__mutmut['xǁBPMNBuilderǁexclusive_gateway__mutmut_9'] = BPMNBuilder.xǁBPMNBuilderǁexclusive_gateway__mutmut_9 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁexclusive_gateway__mutmut['xǁBPMNBuilderǁexclusive_gateway__mutmut_10'] = BPMNBuilder.xǁBPMNBuilderǁexclusive_gateway__mutmut_10 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁexclusive_gateway__mutmut['xǁBPMNBuilderǁexclusive_gateway__mutmut_11'] = BPMNBuilder.xǁBPMNBuilderǁexclusive_gateway__mutmut_11 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁexclusive_gateway__mutmut['xǁBPMNBuilderǁexclusive_gateway__mutmut_12'] = BPMNBuilder.xǁBPMNBuilderǁexclusive_gateway__mutmut_12 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁexclusive_gateway__mutmut['xǁBPMNBuilderǁexclusive_gateway__mutmut_13'] = BPMNBuilder.xǁBPMNBuilderǁexclusive_gateway__mutmut_13 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁexclusive_gateway__mutmut['xǁBPMNBuilderǁexclusive_gateway__mutmut_14'] = BPMNBuilder.xǁBPMNBuilderǁexclusive_gateway__mutmut_14 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁexclusive_gateway__mutmut['xǁBPMNBuilderǁexclusive_gateway__mutmut_15'] = BPMNBuilder.xǁBPMNBuilderǁexclusive_gateway__mutmut_15 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁexclusive_gateway__mutmut['xǁBPMNBuilderǁexclusive_gateway__mutmut_16'] = BPMNBuilder.xǁBPMNBuilderǁexclusive_gateway__mutmut_16 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁexclusive_gateway__mutmut['xǁBPMNBuilderǁexclusive_gateway__mutmut_17'] = BPMNBuilder.xǁBPMNBuilderǁexclusive_gateway__mutmut_17 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁexclusive_gateway__mutmut['xǁBPMNBuilderǁexclusive_gateway__mutmut_18'] = BPMNBuilder.xǁBPMNBuilderǁexclusive_gateway__mutmut_18 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁexclusive_gateway__mutmut['xǁBPMNBuilderǁexclusive_gateway__mutmut_19'] = BPMNBuilder.xǁBPMNBuilderǁexclusive_gateway__mutmut_19 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁexclusive_gateway__mutmut['xǁBPMNBuilderǁexclusive_gateway__mutmut_20'] = BPMNBuilder.xǁBPMNBuilderǁexclusive_gateway__mutmut_20 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁexclusive_gateway__mutmut['xǁBPMNBuilderǁexclusive_gateway__mutmut_21'] = BPMNBuilder.xǁBPMNBuilderǁexclusive_gateway__mutmut_21 # type: ignore # mutmut generated

mutants_xǁBPMNBuilderǁparallel_gateway__mutmut['_mutmut_orig'] = BPMNBuilder.xǁBPMNBuilderǁparallel_gateway__mutmut_orig # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁparallel_gateway__mutmut['xǁBPMNBuilderǁparallel_gateway__mutmut_1'] = BPMNBuilder.xǁBPMNBuilderǁparallel_gateway__mutmut_1 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁparallel_gateway__mutmut['xǁBPMNBuilderǁparallel_gateway__mutmut_2'] = BPMNBuilder.xǁBPMNBuilderǁparallel_gateway__mutmut_2 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁparallel_gateway__mutmut['xǁBPMNBuilderǁparallel_gateway__mutmut_3'] = BPMNBuilder.xǁBPMNBuilderǁparallel_gateway__mutmut_3 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁparallel_gateway__mutmut['xǁBPMNBuilderǁparallel_gateway__mutmut_4'] = BPMNBuilder.xǁBPMNBuilderǁparallel_gateway__mutmut_4 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁparallel_gateway__mutmut['xǁBPMNBuilderǁparallel_gateway__mutmut_5'] = BPMNBuilder.xǁBPMNBuilderǁparallel_gateway__mutmut_5 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁparallel_gateway__mutmut['xǁBPMNBuilderǁparallel_gateway__mutmut_6'] = BPMNBuilder.xǁBPMNBuilderǁparallel_gateway__mutmut_6 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁparallel_gateway__mutmut['xǁBPMNBuilderǁparallel_gateway__mutmut_7'] = BPMNBuilder.xǁBPMNBuilderǁparallel_gateway__mutmut_7 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁparallel_gateway__mutmut['xǁBPMNBuilderǁparallel_gateway__mutmut_8'] = BPMNBuilder.xǁBPMNBuilderǁparallel_gateway__mutmut_8 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁparallel_gateway__mutmut['xǁBPMNBuilderǁparallel_gateway__mutmut_9'] = BPMNBuilder.xǁBPMNBuilderǁparallel_gateway__mutmut_9 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁparallel_gateway__mutmut['xǁBPMNBuilderǁparallel_gateway__mutmut_10'] = BPMNBuilder.xǁBPMNBuilderǁparallel_gateway__mutmut_10 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁparallel_gateway__mutmut['xǁBPMNBuilderǁparallel_gateway__mutmut_11'] = BPMNBuilder.xǁBPMNBuilderǁparallel_gateway__mutmut_11 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁparallel_gateway__mutmut['xǁBPMNBuilderǁparallel_gateway__mutmut_12'] = BPMNBuilder.xǁBPMNBuilderǁparallel_gateway__mutmut_12 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁparallel_gateway__mutmut['xǁBPMNBuilderǁparallel_gateway__mutmut_13'] = BPMNBuilder.xǁBPMNBuilderǁparallel_gateway__mutmut_13 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁparallel_gateway__mutmut['xǁBPMNBuilderǁparallel_gateway__mutmut_14'] = BPMNBuilder.xǁBPMNBuilderǁparallel_gateway__mutmut_14 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁparallel_gateway__mutmut['xǁBPMNBuilderǁparallel_gateway__mutmut_15'] = BPMNBuilder.xǁBPMNBuilderǁparallel_gateway__mutmut_15 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁparallel_gateway__mutmut['xǁBPMNBuilderǁparallel_gateway__mutmut_16'] = BPMNBuilder.xǁBPMNBuilderǁparallel_gateway__mutmut_16 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁparallel_gateway__mutmut['xǁBPMNBuilderǁparallel_gateway__mutmut_17'] = BPMNBuilder.xǁBPMNBuilderǁparallel_gateway__mutmut_17 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁparallel_gateway__mutmut['xǁBPMNBuilderǁparallel_gateway__mutmut_18'] = BPMNBuilder.xǁBPMNBuilderǁparallel_gateway__mutmut_18 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁparallel_gateway__mutmut['xǁBPMNBuilderǁparallel_gateway__mutmut_19'] = BPMNBuilder.xǁBPMNBuilderǁparallel_gateway__mutmut_19 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁparallel_gateway__mutmut['xǁBPMNBuilderǁparallel_gateway__mutmut_20'] = BPMNBuilder.xǁBPMNBuilderǁparallel_gateway__mutmut_20 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁparallel_gateway__mutmut['xǁBPMNBuilderǁparallel_gateway__mutmut_21'] = BPMNBuilder.xǁBPMNBuilderǁparallel_gateway__mutmut_21 # type: ignore # mutmut generated

mutants_xǁBPMNBuilderǁconnect__mutmut['_mutmut_orig'] = BPMNBuilder.xǁBPMNBuilderǁconnect__mutmut_orig # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁconnect__mutmut['xǁBPMNBuilderǁconnect__mutmut_1'] = BPMNBuilder.xǁBPMNBuilderǁconnect__mutmut_1 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁconnect__mutmut['xǁBPMNBuilderǁconnect__mutmut_2'] = BPMNBuilder.xǁBPMNBuilderǁconnect__mutmut_2 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁconnect__mutmut['xǁBPMNBuilderǁconnect__mutmut_3'] = BPMNBuilder.xǁBPMNBuilderǁconnect__mutmut_3 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁconnect__mutmut['xǁBPMNBuilderǁconnect__mutmut_4'] = BPMNBuilder.xǁBPMNBuilderǁconnect__mutmut_4 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁconnect__mutmut['xǁBPMNBuilderǁconnect__mutmut_5'] = BPMNBuilder.xǁBPMNBuilderǁconnect__mutmut_5 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁconnect__mutmut['xǁBPMNBuilderǁconnect__mutmut_6'] = BPMNBuilder.xǁBPMNBuilderǁconnect__mutmut_6 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁconnect__mutmut['xǁBPMNBuilderǁconnect__mutmut_7'] = BPMNBuilder.xǁBPMNBuilderǁconnect__mutmut_7 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁconnect__mutmut['xǁBPMNBuilderǁconnect__mutmut_8'] = BPMNBuilder.xǁBPMNBuilderǁconnect__mutmut_8 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁconnect__mutmut['xǁBPMNBuilderǁconnect__mutmut_9'] = BPMNBuilder.xǁBPMNBuilderǁconnect__mutmut_9 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁconnect__mutmut['xǁBPMNBuilderǁconnect__mutmut_10'] = BPMNBuilder.xǁBPMNBuilderǁconnect__mutmut_10 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁconnect__mutmut['xǁBPMNBuilderǁconnect__mutmut_11'] = BPMNBuilder.xǁBPMNBuilderǁconnect__mutmut_11 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁconnect__mutmut['xǁBPMNBuilderǁconnect__mutmut_12'] = BPMNBuilder.xǁBPMNBuilderǁconnect__mutmut_12 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁconnect__mutmut['xǁBPMNBuilderǁconnect__mutmut_13'] = BPMNBuilder.xǁBPMNBuilderǁconnect__mutmut_13 # type: ignore # mutmut generated
mutants_xǁBPMNBuilderǁconnect__mutmut['xǁBPMNBuilderǁconnect__mutmut_14'] = BPMNBuilder.xǁBPMNBuilderǁconnect__mutmut_14 # type: ignore # mutmut generated
