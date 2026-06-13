"""
ForkHandler — Ejecución en paralelo (DAG Fork/Join)
=====================================================

NOTA: Este archivo es el entry point delgado.
Las implementaciones ForkHandler y JoinHandler completas
están en src/workflow/execution/parallel.py.
"""

from __future__ import annotations

from src.workflow.execution.parallel import ForkHandler, JoinHandler
from src.workflow.execution.result import ForkResult, JoinResult

__all__ = [
    "ForkHandler",
    "ForkResult",
    "JoinHandler",
    "JoinResult",
]
