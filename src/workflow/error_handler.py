"""
ORBITAL — ErrorHandler Orbital (OVC Compartido)
==================================================

ErrorHandler con retroalimentacion orbital usando OVC compartido via OrbitalContext.

MEJORA vs version anterior:
- Ahora usa OrbitalContext → OVC compartido con todos los demas componentes
- Los errores retroalimentan al mismo OVC que los pasos y condiciones

Compatibilidad: mantiene la misma API que ErrorHandler.
"""

from __future__ import annotations

import hashlib
import time
from typing import Callable

from src.orbital.models import TWO_PI
from src.orbital.context import OrbitalContext
from src.config import ERROR_MAX_RETRIES, ERROR_BASE_DELAY_SECONDS, ERROR_RETRY_MULTIPLIER, ERROR_USE_FALLBACK
from src.utils.logger import setup_logging

logger = setup_logging(__name__)


class ErrorHandlerResult:
    """Resultado del manejo de error."""

    def __init__(self, status: str, output_data: dict | None = None,
                 error_message: str | None = None, retries: int = 0,
                 orbital_theta: float = 0.0, orbital_alignment: float = 0.0):
        self.status = status  # 'recovered' | 'failed' | 'dead_letter'
        self.output_data = output_data or {}
        self.error_message = error_message
        self.retries = retries
        self.orbital_theta = orbital_theta
        self.orbital_alignment = orbital_alignment


class ErrorHandler:
    """
    OrbitalRecovery — Manejo de errores por retroalimentacion orbital (OVC compartido).

    Usa OrbitalContext para compartir el OVC con todos los componentes.
    Los errores retroalimentan al OVC compartido, afectando las fases
    de las variables orbitales que otros componentes ven.
    """

    def __init__(self):
        self.max_retries = ERROR_MAX_RETRIES
        self.base_delay = ERROR_BASE_DELAY_SECONDS
        self.multiplier = ERROR_RETRY_MULTIPLIER
        self.use_fallback = ERROR_USE_FALLBACK
        self._fallback_actions: dict[str, Callable] = {}
        # ── ORBITAL COMPARTIDO ───────────────────────────
        self._ctx = OrbitalContext()

    def handle(self, step: dict, error: Exception, context: dict,
               step_executor) -> ErrorHandlerResult:
        """Maneja un error durante la ejecucion de un paso (OVC compartido)."""
        step_id = step.get("id", 0)
        step_retry_config = step.get("retry", {})
        max_retries = step_retry_config.get("max_attempts", self.max_retries)
        base_delay = step_retry_config.get("base_delay", self.base_delay)
        multiplier = step_retry_config.get("multiplier", self.multiplier)
        use_fallback = step_retry_config.get("use_fallback", self.use_fallback)

        # 1. Crear variable orbital para el error (en OVC compartido)
        error_type = type(error).__name__
        error_var_name = f"error_{step_id}_{error_type}"
        self._ensure_error_variable(error_var_name, step_id, error_type)

        # 2. Calcular TOR(error, contexto)
        orbital_alignment = 0.0
        context_var_name = f"ctx_{step_id}"
        self._ensure_context_variable(context_var_name, context)

        try:
            tor_result = self._ctx.tor.calculate(error_var_name, context_var_name)
            orbital_alignment = tor_result.tor_value
        except KeyError:
            pass

        error_var = self._ctx.ovc.get_variable(error_var_name)
        orbital_theta = error_var.theta if error_var else 0.0

        logger.warning(
            f"OrbitalRecovery: Error en paso {step_id} ({error_type}) — "
            f"TOR={orbital_alignment:.4f} theta={orbital_theta:.2f} "
            f"{'RECUPERABLE' if orbital_alignment > 0 else 'DIFICIL RECUPERACION'}"
        )

        # 3. Ajustar reintentos segun alineacion orbital
        if orbital_alignment > 0:
            effective_max_retries = max(max_retries, 1)
        else:
            effective_max_retries = max(max_retries // 2, 1)

        # 4. Reintentar con retroalimentacion orbital
        for attempt in range(1, effective_max_retries + 1):
            delay = base_delay * (multiplier ** (attempt - 1))
            if orbital_alignment > 0:
                delay *= 0.7
            else:
                delay *= 1.5

            logger.info(f"Reintento {attempt}/{effective_max_retries} en {delay:.1f}s...")
            time.sleep(delay)

            try:
                result = step_executor.execute(step, context)
                if result.status == "completed":
                    if error_var:
                        error_var.retrofeed(0.3, damping=0.3)

                    logger.info(f"OrbitalRecovery: Reintento {attempt} exitoso para paso {step_id}")
                    return ErrorHandlerResult(
                        status="recovered",
                        output_data=result.output_data,
                        retries=attempt,
                        orbital_theta=error_var.theta if error_var else 0.0,
                        orbital_alignment=orbital_alignment,
                    )
            except Exception as retry_error:
                if error_var:
                    error_var.retrofeed(-0.1, damping=0.3)
                logger.warning(f"OrbitalRecovery: Reintento {attempt} fallo: {retry_error}")

        # 5. Fallback action
        if use_fallback and self._has_fallback(step):
            try:
                fallback_result = self._execute_fallback(step, context)
                if error_var:
                    error_var.retrofeed(0.1, damping=0.3)
                logger.info(f"OrbitalRecovery: Fallback ejecutado para paso {step_id}")
                return ErrorHandlerResult(
                    status="recovered",
                    output_data=fallback_result,
                    retries=effective_max_retries,
                    orbital_theta=error_var.theta if error_var else 0.0,
                    orbital_alignment=orbital_alignment,
                )
            except Exception as fb_error:
                logger.error(f"OrbitalRecovery: Fallback fallo: {fb_error}")

        # 6. Dead letter con metadatos orbitales
        self._send_to_dead_letter(step, error, effective_max_retries, orbital_alignment)
        if error_var:
            error_var.retrofeed(-0.5, damping=0.3)

        logger.error(
            f"OrbitalRecovery: Paso {step_id} → dead letter despues de "
            f"{effective_max_retries} reintentos (alignment={orbital_alignment:.4f})"
        )

        return ErrorHandlerResult(
            status="dead_letter",
            error_message=f"Error despues de {effective_max_retries} reintentos: {error}",
            retries=effective_max_retries,
            orbital_theta=error_var.theta if error_var else 0.0,
            orbital_alignment=orbital_alignment,
        )

    def register_fallback(self, action_name: str, func: Callable) -> None:
        self._fallback_actions[action_name] = func

    def _has_fallback(self, step: dict) -> bool:
        fallback = step.get("fallback")
        if fallback is None:
            return False
        if isinstance(fallback, str):
            return fallback in self._fallback_actions or fallback == "skip"
        if isinstance(fallback, dict):
            return True
        return False

    def _execute_fallback(self, step: dict, context: dict) -> dict:
        fallback = step.get("fallback", {})

        if isinstance(fallback, str):
            if fallback == "skip":
                return {"status": "skipped", "reason": "fallback_skip"}
            if fallback in self._fallback_actions:
                return self._fallback_actions[fallback](step, context)
            raise ValueError(f"Funcion de fallback desconocida: {fallback}")

        if isinstance(fallback, dict):
            action = fallback.get("action", "skip")
            params = fallback.get("params", {})

            if action == "skip":
                return {"status": "skipped", "reason": "fallback_skip"}
            if action == "set_default":
                return {"status": "completed", "data": params.get("default_value", {})}
            if action in self._fallback_actions:
                return self._fallback_actions[action](step, context, params)

            raise ValueError(f"Accion de fallback desconocida: {action}")

        raise ValueError(f"Configuracion de fallback invalida: {fallback}")

    def _send_to_dead_letter(self, step: dict, error: Exception, retries: int,
                              orbital_alignment: float = 0.0) -> None:
        """Envia el paso fallido a la cola de dead letter con metadatos orbitales."""
        from src.data.database_manager import DatabaseManager
        db = DatabaseManager()

        db.execute(
            """INSERT INTO event_queue
               (event_type, event_data, status)
               VALUES (?, ?, ?)""",
            (
                "dead_letter.step_failed",
                str({
                    "step_id": step.get("id"),
                    "tool": step.get("tool"),
                    "action": step.get("action"),
                    "error": str(error),
                    "retries": retries,
                    "orbital_alignment": orbital_alignment,
                    "step_definition": step,
                }),
                "failed",
            ),
        )
        db.commit()

    # ── Helpers orbitales (OVC compartido) ───────────────────

    def _ensure_error_variable(self, var_name: str, step_id: int, error_type: str) -> None:
        if self._ctx.ovc.get_variable(var_name) is None:
            hash_val = int(hashlib.md5(var_name.encode()).hexdigest()[:8], 16)
            theta = (hash_val % 1000) / 1000.0 * TWO_PI
            self._ctx.ovc.create_variable(
                name=var_name,
                theta=theta,
                amplitude=0.5,
                velocity=0.2,
                orbit_group="errors",
                metadata={"source": "error_handler", "step_id": step_id, "error_type": error_type},
            )

    def _ensure_context_variable(self, var_name: str, context: dict) -> None:
        if self._ctx.ovc.get_variable(var_name) is None:
            hash_val = int(hashlib.md5(str(context).encode()).hexdigest()[:8], 16)
            theta = (hash_val % 1000) / 1000.0 * TWO_PI
            self._ctx.ovc.create_variable(
                name=var_name,
                theta=theta,
                amplitude=1.0,
                velocity=0.05,
                orbit_group="error_context",
                metadata={"source": "error_handler"},
            )
