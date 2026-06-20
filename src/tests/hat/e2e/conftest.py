"""Pytest fixtures for E2E HAT tests.

Aisla la DB de tests (WFD_DATA_DIR), resetea singletons y provee un
HATRouter listo para atender requests end-to-end.
"""

from __future__ import annotations

import os
import shutil
import tempfile
from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def e2e_data_dir():
    """Crea un directorio temporal para la DB de tests E2E.

    Se usa WFD_DATA_DIR para redirigir la DB workflow_determinista.db
    a un path aislado del de producción (~/.workflow_determinista/).
    Se mantiene por toda la sesión de pytest y se limpia al final.
    """
    tmpdir = Path(tempfile.mkdtemp(prefix="e2e_hat_"))
    os.environ["WFD_DATA_DIR"] = str(tmpdir)
    yield tmpdir
    # Cleanup
    if "WFD_DATA_DIR" in os.environ:
        del os.environ["WFD_DATA_DIR"]
    shutil.rmtree(tmpdir, ignore_errors=True)


@pytest.fixture(scope="session")
def hat_router(e2e_data_dir):
    """Inicializa HAT una sola vez para toda la sesión de tests E2E.

    Bootstrap completo:
    - Nivel 5: 19 tools instanciadas
    - Nivel 4: ~101 workers auto-generados
    - Nivel 3: 9 specialists + AgentCards publicadas en OVC
    - Nivel 2: 3 supervisores con specialists
    - Nivel 1: HATRouter con supervisores inyectados

    Returns:
        HATRouter listo para atender requests.
    """
    # Reset singletons antes del bootstrap
    from src.core.db.sqlite_manager import DatabaseManager
    DatabaseManager._instance = None

    from src.events.bus import EventBus
    from src.hat.bootstrap import bootstrap_hat

    router = bootstrap_hat(event_bus=EventBus())
    return router


@pytest.fixture(autouse=True)
def _reset_orbital_context():
    """Reset OrbitalContext singleton antes de cada test.

    Evita que variables OVC de un test contamine al siguiente.
    El HATRouter usa OVC para ruteo por resonancia.
    """
    try:
        from src.orbital.context import OrbitalContext
        OrbitalContext._reset()
    except Exception:
        pass
    yield
