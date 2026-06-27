"""
Zenic-Flujo — Logging Estructurado Centralizado
=================================================

Provee funciones de logging consistentes en toda la aplicacion.
Usar setup_logging(__name__) como unico punto de entrada.

La configuracion centralizada se define en src.utils.logging_config
con formatos, niveles y manejadores estandar.

Ejemplo:
    from src.utils.logger import setup_logging
    logger = setup_logging(__name__)
"""

import logging
from pathlib import Path

from src.config import DATA_DIR, LOG_DATE_FORMAT, LOG_FORMAT, LOG_LEVEL
from src.utils.logging_config import configure_logger


class AuditLogger:
    """Logger especifico para eventos de auditoria."""

    def __init__(self, log_dir: Path | None = None):
        self.log_dir = log_dir or DATA_DIR
        self.log_dir.mkdir(parents=True, exist_ok=True)

    def log(self, event: str, details: str | None = None, ip_address: str | None = None) -> None:
        """Registra un evento de auditoria en el log y en la base de datos."""
        msg = f"[AUDIT] event={event}"
        if details:
            msg += f" details={details}"
        if ip_address:
            msg += f" ip={ip_address}"
        logging.getLogger("audit").info(msg)


def get_logger(name: str = "zenic_flujo") -> logging.Logger:
    """Alias de setup_logging para compatibilidad con imports existentes.

    Args:
        name: Nombre del logger (tipicamente __name__)

    Retorna:
        Logger configurado
    """
    return setup_logging(name)


def setup_logging(name: str = "zenic_flujo") -> logging.Logger:
    """Configura y retorna un logger para el modulo especificado.

    Es la funcion canonica para obtener loggers en toda la aplicacion.
    Usa configure_logger() para la configuracion centralizada.

    Args:
        name: Nombre del logger (tipicamente __name__)

    Retorna:
        Logger configurado con handler de consola y archivo
    """
    return configure_logger(
        name=name,
        level=getattr(logging, LOG_LEVEL.upper(), logging.INFO),
        log_format=LOG_FORMAT,
        date_format=LOG_DATE_FORMAT,
        log_dir=DATA_DIR,
        log_file="zenic_flujo.log",
    )
