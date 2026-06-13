"""Orbital trigger injection — convierte datos de trigger en variables orbitales.

Extraído de WorkflowEngine._inject_trigger_as_orbital().
"""

from __future__ import annotations

from src.orbital.models import TWO_PI
from src.utils.logger import setup_logging

logger = setup_logging(__name__)


def inject_trigger_as_orbital(trigger_data: dict, ovc) -> None:
    """Convierte los datos del trigger en variables orbitales (OVC compartido)."""
    for key, value in trigger_data.items():
        if isinstance(value, (int, float)):
            try:
                ovc.create_variable(
                    name=f"input_{key}",
                    theta=abs(value) % TWO_PI if value != 0 else 0.0,
                    amplitude=abs(value) if value != 0 else 1.0,
                    velocity=0.05,
                    orbit_group="trigger_data",
                    metadata={"source": "trigger", "original_key": key},
                )
            except ValueError:
                var = ovc.get_variable(f"input_{key}")
                if var:
                    var.amplitude = abs(value) if value != 0 else 1.0
