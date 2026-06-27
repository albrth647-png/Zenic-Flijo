"""
Workflow Determinista — Configuración Global

Seguridad: Los secrets (SESSION_SECRET, LICENSE_SECRET_KEY) DEBEN configurarse
via variables de entorno en producción. Si se usan los valores por defecto
en modo producción, el sistema se rehusa a arrancar.
"""

import base64
import hashlib
import os
import secrets
import warnings
from pathlib import Path

# ── Rutas base ──────────────────────────────────────────────
BASE_DIR = Path(os.path.dirname(os.path.abspath(__file__))).parent
DATA_DIR = Path(os.environ.get("WFD_DATA_DIR", Path.home() / ".workflow_determinista"))
DATA_DIR.mkdir(parents=True, exist_ok=True)

# ── Modo de ejecución ───────────────────────────────────────
# PRODUCTION=true implica validación estricta de secrets
PRODUCTION = os.environ.get("WFD_PRODUCTION", "false").lower() == "true"

# ── Base de datos (unificada) ──────────────────────────────
DB_PATH = DATA_DIR / "workflow_determinista.db"
DB_WAL_MODE = True

# ── Servidor web ───────────────────────────────────────────
WEB_HOST = os.environ.get("WFD_WEB_HOST", "127.0.0.1")
WEB_PORT = int(os.environ.get("WFD_WEB_PORT", "8080"))
WEBHOOK_PORT = int(os.environ.get("WFD_WEBHOOK_PORT", "8081"))

# ── Sesiones ───────────────────────────────────────────────
# En producción: WFD_SESSION_SECRET DEBE establecerse (mínimo 32 caracteres).
# En desarrollo: si no se establece, se genera uno aleatorio por sesión.
_INSECURE_SESSION_DEFAULT = "REDACTED_generar_aleatorio_64chars"
_session_secret_env = os.environ.get("WFD_SESSION_SECRET", "")

if _session_secret_env:
    SESSION_SECRET = _session_secret_env
elif PRODUCTION:
    raise RuntimeError(
        "SEGURIDAD: WFD_SESSION_SECRET no configurado en modo producción. "
        "Establezca la variable de entorno WFD_SESSION_SECRET con un valor "
        "aleatorio de al menos 64 caracteres antes de desplegar."
    )
else:
    # Modo desarrollo: generar secret aleatorio y advertir
    SESSION_SECRET = secrets.token_urlsafe(48)
    warnings.warn(
        "WFD_SESSION_SECRET no configurado. Se generó un secret aleatorio para "
        "esta sesión. Configure WFD_SESSION_SECRET antes de desplegar en producción.",
        stacklevel=2,
    )

SESSION_EXPIRY_HOURS = 24
SESSION_COOKIE_SECURE = os.environ.get("WFD_SESSION_SECURE", "false").lower() == "true"

# ── Rate Limiting ──────────────────────────────────────────
LOGIN_MAX_ATTEMPTS = 10
LOGIN_WINDOW_MINUTES = 15
API_MAX_REQUESTS = 100
API_WINDOW_MINUTES = 15

# ── Schedule Worker ────────────────────────────────────────
SCHEDULE_INTERVAL_SECONDS = 60

# ── Webhook ────────────────────────────────────────────────
WEBHOOK_API_KEY_ENABLED = os.environ.get("WFD_WEBHOOK_API_KEY_ENABLED", "true").lower() == "true"

# ── Error Handler ──────────────────────────────────────────
ERROR_MAX_RETRIES = 3
ERROR_BASE_DELAY_SECONDS = 5
ERROR_RETRY_MULTIPLIER = 2
ERROR_USE_FALLBACK = True

# ── Trial ──────────────────────────────────────────────────
TRIAL_DAYS = 30

# ── License ────────────────────────────────────────────────
# En producción: WFD_LICENSE_SECRET DEBE establecerse.
# En desarrollo: si no se establece, se genera uno aleatorio.
_INSECURE_LICENSE_DEFAULT = "REDACTED_clave_maestra_hmac"
_license_secret_env = os.environ.get("WFD_LICENSE_SECRET", "")

if _license_secret_env:
    LICENSE_SECRET_KEY = _license_secret_env
elif PRODUCTION:
    raise RuntimeError(
        "SEGURIDAD: WFD_LICENSE_SECRET no configurado en modo producción. "
        "Establezca la variable de entorno WFD_LICENSE_SECRET con un valor "
        "aleatorio de al menos 64 caracteres antes de desplegar."
    )
else:
    # Modo desarrollo: generar clave aleatoria y advertir
    LICENSE_SECRET_KEY = secrets.token_urlsafe(48)
    warnings.warn(
        "WFD_LICENSE_SECRET no configurado. Se generó una clave aleatoria para "
        "esta sesión. Configure WFD_LICENSE_SECRET antes de desplegar en producción.",
        stacklevel=2,
    )

# ── Encryption ────────────────────────────────────────────
# Derivada de SESSION_SECRET para cifrar tokens sensibles (WhatsApp, etc.)
WHATSAPP_ENCRYPTION_KEY = base64.urlsafe_b64encode(hashlib.sha256(SESSION_SECRET.encode()).digest())

# ── Free Tier Limits ──────────────────────────────────────
FREE_TIER_MAX_WORKFLOWS = 3
FREE_TIER_ALLOWED_TOOLS = ["crm"]  # Solo CRM en free

# ── Ollama (AI Enhancement) ────────────────────────────────
OLLAMA_ENABLED = os.environ.get("WFD_OLLAMA_ENABLED", "false").lower() == "true"
OLLAMA_BASE_URL = os.environ.get("WFD_OLLAMA_URL", "http://localhost:11434")
OLLAMA_MODEL = os.environ.get("WFD_OLLAMA_MODEL", "llama3.2")
OLLAMA_TIMEOUT = int(os.environ.get("WFD_OLLAMA_TIMEOUT", "30"))

# ── Logging ────────────────────────────────────────────────
LOG_LEVEL = os.environ.get("WFD_LOG_LEVEL", "INFO")
LOG_FORMAT = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_validate_config__mutmut: MutantDict = {}  # type: ignore


# ── Validación de configuración ────────────────────────────


@_mutmut_mutated(mutants_x_validate_config__mutmut)
def validate_config() -> list[str]:
    """
    Valida la configuración del sistema y retorna una lista de advertencias.

    En producción, los secrets faltantes causan RuntimeError al importar.
    Esta función permite detectar problemas adicionales en cualquier modo.

    Returns:
        Lista de mensajes de advertencia (vacía si todo está bien)
    """
    warnings_list = []

    # Verificar que los secrets no sean los valores por defecto inseguros
    if SESSION_SECRET == _INSECURE_SESSION_DEFAULT:
        warnings_list.append(
            "SESSION_SECRET usa el valor por defecto inseguro. Configure WFD_SESSION_SECRET antes de desplegar."
        )

    if LICENSE_SECRET_KEY == _INSECURE_LICENSE_DEFAULT:
        warnings_list.append(
            "LICENSE_SECRET_KEY usa el valor por defecto inseguro. Configure WFD_LICENSE_SECRET antes de desplegar."
        )

    # Verificar que SESSION_SECRET tenga suficiente entropía
    if len(SESSION_SECRET) < 32:
        warnings_list.append(
            f"SESSION_SECRET tiene solo {len(SESSION_SECRET)} caracteres. "
            "Se recomienda al menos 64 caracteres para producción."
        )

    # Verificar que SESSION_COOKIE_SECURE esté activado en producción
    if PRODUCTION and not SESSION_COOKIE_SECURE:
        warnings_list.append(
            "SESSION_COOKIE_SECURE está desactivado en modo producción. "
            "Active WFD_SESSION_SECURE=true para cookies seguras sobre HTTPS."
        )

    return warnings_list


# ── Validación de configuración ────────────────────────────


def x_validate_config__mutmut_orig() -> list[str]:
    """
    Valida la configuración del sistema y retorna una lista de advertencias.

    En producción, los secrets faltantes causan RuntimeError al importar.
    Esta función permite detectar problemas adicionales en cualquier modo.

    Returns:
        Lista de mensajes de advertencia (vacía si todo está bien)
    """
    warnings_list = []

    # Verificar que los secrets no sean los valores por defecto inseguros
    if SESSION_SECRET == _INSECURE_SESSION_DEFAULT:
        warnings_list.append(
            "SESSION_SECRET usa el valor por defecto inseguro. Configure WFD_SESSION_SECRET antes de desplegar."
        )

    if LICENSE_SECRET_KEY == _INSECURE_LICENSE_DEFAULT:
        warnings_list.append(
            "LICENSE_SECRET_KEY usa el valor por defecto inseguro. Configure WFD_LICENSE_SECRET antes de desplegar."
        )

    # Verificar que SESSION_SECRET tenga suficiente entropía
    if len(SESSION_SECRET) < 32:
        warnings_list.append(
            f"SESSION_SECRET tiene solo {len(SESSION_SECRET)} caracteres. "
            "Se recomienda al menos 64 caracteres para producción."
        )

    # Verificar que SESSION_COOKIE_SECURE esté activado en producción
    if PRODUCTION and not SESSION_COOKIE_SECURE:
        warnings_list.append(
            "SESSION_COOKIE_SECURE está desactivado en modo producción. "
            "Active WFD_SESSION_SECURE=true para cookies seguras sobre HTTPS."
        )

    return warnings_list


# ── Validación de configuración ────────────────────────────


def x_validate_config__mutmut_1() -> list[str]:
    """
    Valida la configuración del sistema y retorna una lista de advertencias.

    En producción, los secrets faltantes causan RuntimeError al importar.
    Esta función permite detectar problemas adicionales en cualquier modo.

    Returns:
        Lista de mensajes de advertencia (vacía si todo está bien)
    """
    warnings_list = None

    # Verificar que los secrets no sean los valores por defecto inseguros
    if SESSION_SECRET == _INSECURE_SESSION_DEFAULT:
        warnings_list.append(
            "SESSION_SECRET usa el valor por defecto inseguro. Configure WFD_SESSION_SECRET antes de desplegar."
        )

    if LICENSE_SECRET_KEY == _INSECURE_LICENSE_DEFAULT:
        warnings_list.append(
            "LICENSE_SECRET_KEY usa el valor por defecto inseguro. Configure WFD_LICENSE_SECRET antes de desplegar."
        )

    # Verificar que SESSION_SECRET tenga suficiente entropía
    if len(SESSION_SECRET) < 32:
        warnings_list.append(
            f"SESSION_SECRET tiene solo {len(SESSION_SECRET)} caracteres. "
            "Se recomienda al menos 64 caracteres para producción."
        )

    # Verificar que SESSION_COOKIE_SECURE esté activado en producción
    if PRODUCTION and not SESSION_COOKIE_SECURE:
        warnings_list.append(
            "SESSION_COOKIE_SECURE está desactivado en modo producción. "
            "Active WFD_SESSION_SECURE=true para cookies seguras sobre HTTPS."
        )

    return warnings_list


# ── Validación de configuración ────────────────────────────


def x_validate_config__mutmut_2() -> list[str]:
    """
    Valida la configuración del sistema y retorna una lista de advertencias.

    En producción, los secrets faltantes causan RuntimeError al importar.
    Esta función permite detectar problemas adicionales en cualquier modo.

    Returns:
        Lista de mensajes de advertencia (vacía si todo está bien)
    """
    warnings_list = []

    # Verificar que los secrets no sean los valores por defecto inseguros
    if SESSION_SECRET != _INSECURE_SESSION_DEFAULT:
        warnings_list.append(
            "SESSION_SECRET usa el valor por defecto inseguro. Configure WFD_SESSION_SECRET antes de desplegar."
        )

    if LICENSE_SECRET_KEY == _INSECURE_LICENSE_DEFAULT:
        warnings_list.append(
            "LICENSE_SECRET_KEY usa el valor por defecto inseguro. Configure WFD_LICENSE_SECRET antes de desplegar."
        )

    # Verificar que SESSION_SECRET tenga suficiente entropía
    if len(SESSION_SECRET) < 32:
        warnings_list.append(
            f"SESSION_SECRET tiene solo {len(SESSION_SECRET)} caracteres. "
            "Se recomienda al menos 64 caracteres para producción."
        )

    # Verificar que SESSION_COOKIE_SECURE esté activado en producción
    if PRODUCTION and not SESSION_COOKIE_SECURE:
        warnings_list.append(
            "SESSION_COOKIE_SECURE está desactivado en modo producción. "
            "Active WFD_SESSION_SECURE=true para cookies seguras sobre HTTPS."
        )

    return warnings_list


# ── Validación de configuración ────────────────────────────


def x_validate_config__mutmut_3() -> list[str]:
    """
    Valida la configuración del sistema y retorna una lista de advertencias.

    En producción, los secrets faltantes causan RuntimeError al importar.
    Esta función permite detectar problemas adicionales en cualquier modo.

    Returns:
        Lista de mensajes de advertencia (vacía si todo está bien)
    """
    warnings_list = []

    # Verificar que los secrets no sean los valores por defecto inseguros
    if SESSION_SECRET == _INSECURE_SESSION_DEFAULT:
        warnings_list.append(
            None
        )

    if LICENSE_SECRET_KEY == _INSECURE_LICENSE_DEFAULT:
        warnings_list.append(
            "LICENSE_SECRET_KEY usa el valor por defecto inseguro. Configure WFD_LICENSE_SECRET antes de desplegar."
        )

    # Verificar que SESSION_SECRET tenga suficiente entropía
    if len(SESSION_SECRET) < 32:
        warnings_list.append(
            f"SESSION_SECRET tiene solo {len(SESSION_SECRET)} caracteres. "
            "Se recomienda al menos 64 caracteres para producción."
        )

    # Verificar que SESSION_COOKIE_SECURE esté activado en producción
    if PRODUCTION and not SESSION_COOKIE_SECURE:
        warnings_list.append(
            "SESSION_COOKIE_SECURE está desactivado en modo producción. "
            "Active WFD_SESSION_SECURE=true para cookies seguras sobre HTTPS."
        )

    return warnings_list


# ── Validación de configuración ────────────────────────────


def x_validate_config__mutmut_4() -> list[str]:
    """
    Valida la configuración del sistema y retorna una lista de advertencias.

    En producción, los secrets faltantes causan RuntimeError al importar.
    Esta función permite detectar problemas adicionales en cualquier modo.

    Returns:
        Lista de mensajes de advertencia (vacía si todo está bien)
    """
    warnings_list = []

    # Verificar que los secrets no sean los valores por defecto inseguros
    if SESSION_SECRET == _INSECURE_SESSION_DEFAULT:
        warnings_list.append(
            "XXSESSION_SECRET usa el valor por defecto inseguro. Configure WFD_SESSION_SECRET antes de desplegar.XX"
        )

    if LICENSE_SECRET_KEY == _INSECURE_LICENSE_DEFAULT:
        warnings_list.append(
            "LICENSE_SECRET_KEY usa el valor por defecto inseguro. Configure WFD_LICENSE_SECRET antes de desplegar."
        )

    # Verificar que SESSION_SECRET tenga suficiente entropía
    if len(SESSION_SECRET) < 32:
        warnings_list.append(
            f"SESSION_SECRET tiene solo {len(SESSION_SECRET)} caracteres. "
            "Se recomienda al menos 64 caracteres para producción."
        )

    # Verificar que SESSION_COOKIE_SECURE esté activado en producción
    if PRODUCTION and not SESSION_COOKIE_SECURE:
        warnings_list.append(
            "SESSION_COOKIE_SECURE está desactivado en modo producción. "
            "Active WFD_SESSION_SECURE=true para cookies seguras sobre HTTPS."
        )

    return warnings_list


# ── Validación de configuración ────────────────────────────


def x_validate_config__mutmut_5() -> list[str]:
    """
    Valida la configuración del sistema y retorna una lista de advertencias.

    En producción, los secrets faltantes causan RuntimeError al importar.
    Esta función permite detectar problemas adicionales en cualquier modo.

    Returns:
        Lista de mensajes de advertencia (vacía si todo está bien)
    """
    warnings_list = []

    # Verificar que los secrets no sean los valores por defecto inseguros
    if SESSION_SECRET == _INSECURE_SESSION_DEFAULT:
        warnings_list.append(
            "session_secret usa el valor por defecto inseguro. configure wfd_session_secret antes de desplegar."
        )

    if LICENSE_SECRET_KEY == _INSECURE_LICENSE_DEFAULT:
        warnings_list.append(
            "LICENSE_SECRET_KEY usa el valor por defecto inseguro. Configure WFD_LICENSE_SECRET antes de desplegar."
        )

    # Verificar que SESSION_SECRET tenga suficiente entropía
    if len(SESSION_SECRET) < 32:
        warnings_list.append(
            f"SESSION_SECRET tiene solo {len(SESSION_SECRET)} caracteres. "
            "Se recomienda al menos 64 caracteres para producción."
        )

    # Verificar que SESSION_COOKIE_SECURE esté activado en producción
    if PRODUCTION and not SESSION_COOKIE_SECURE:
        warnings_list.append(
            "SESSION_COOKIE_SECURE está desactivado en modo producción. "
            "Active WFD_SESSION_SECURE=true para cookies seguras sobre HTTPS."
        )

    return warnings_list


# ── Validación de configuración ────────────────────────────


def x_validate_config__mutmut_6() -> list[str]:
    """
    Valida la configuración del sistema y retorna una lista de advertencias.

    En producción, los secrets faltantes causan RuntimeError al importar.
    Esta función permite detectar problemas adicionales en cualquier modo.

    Returns:
        Lista de mensajes de advertencia (vacía si todo está bien)
    """
    warnings_list = []

    # Verificar que los secrets no sean los valores por defecto inseguros
    if SESSION_SECRET == _INSECURE_SESSION_DEFAULT:
        warnings_list.append(
            "SESSION_SECRET USA EL VALOR POR DEFECTO INSEGURO. CONFIGURE WFD_SESSION_SECRET ANTES DE DESPLEGAR."
        )

    if LICENSE_SECRET_KEY == _INSECURE_LICENSE_DEFAULT:
        warnings_list.append(
            "LICENSE_SECRET_KEY usa el valor por defecto inseguro. Configure WFD_LICENSE_SECRET antes de desplegar."
        )

    # Verificar que SESSION_SECRET tenga suficiente entropía
    if len(SESSION_SECRET) < 32:
        warnings_list.append(
            f"SESSION_SECRET tiene solo {len(SESSION_SECRET)} caracteres. "
            "Se recomienda al menos 64 caracteres para producción."
        )

    # Verificar que SESSION_COOKIE_SECURE esté activado en producción
    if PRODUCTION and not SESSION_COOKIE_SECURE:
        warnings_list.append(
            "SESSION_COOKIE_SECURE está desactivado en modo producción. "
            "Active WFD_SESSION_SECURE=true para cookies seguras sobre HTTPS."
        )

    return warnings_list


# ── Validación de configuración ────────────────────────────


def x_validate_config__mutmut_7() -> list[str]:
    """
    Valida la configuración del sistema y retorna una lista de advertencias.

    En producción, los secrets faltantes causan RuntimeError al importar.
    Esta función permite detectar problemas adicionales en cualquier modo.

    Returns:
        Lista de mensajes de advertencia (vacía si todo está bien)
    """
    warnings_list = []

    # Verificar que los secrets no sean los valores por defecto inseguros
    if SESSION_SECRET == _INSECURE_SESSION_DEFAULT:
        warnings_list.append(
            "SESSION_SECRET usa el valor por defecto inseguro. Configure WFD_SESSION_SECRET antes de desplegar."
        )

    if LICENSE_SECRET_KEY != _INSECURE_LICENSE_DEFAULT:
        warnings_list.append(
            "LICENSE_SECRET_KEY usa el valor por defecto inseguro. Configure WFD_LICENSE_SECRET antes de desplegar."
        )

    # Verificar que SESSION_SECRET tenga suficiente entropía
    if len(SESSION_SECRET) < 32:
        warnings_list.append(
            f"SESSION_SECRET tiene solo {len(SESSION_SECRET)} caracteres. "
            "Se recomienda al menos 64 caracteres para producción."
        )

    # Verificar que SESSION_COOKIE_SECURE esté activado en producción
    if PRODUCTION and not SESSION_COOKIE_SECURE:
        warnings_list.append(
            "SESSION_COOKIE_SECURE está desactivado en modo producción. "
            "Active WFD_SESSION_SECURE=true para cookies seguras sobre HTTPS."
        )

    return warnings_list


# ── Validación de configuración ────────────────────────────


def x_validate_config__mutmut_8() -> list[str]:
    """
    Valida la configuración del sistema y retorna una lista de advertencias.

    En producción, los secrets faltantes causan RuntimeError al importar.
    Esta función permite detectar problemas adicionales en cualquier modo.

    Returns:
        Lista de mensajes de advertencia (vacía si todo está bien)
    """
    warnings_list = []

    # Verificar que los secrets no sean los valores por defecto inseguros
    if SESSION_SECRET == _INSECURE_SESSION_DEFAULT:
        warnings_list.append(
            "SESSION_SECRET usa el valor por defecto inseguro. Configure WFD_SESSION_SECRET antes de desplegar."
        )

    if LICENSE_SECRET_KEY == _INSECURE_LICENSE_DEFAULT:
        warnings_list.append(
            None
        )

    # Verificar que SESSION_SECRET tenga suficiente entropía
    if len(SESSION_SECRET) < 32:
        warnings_list.append(
            f"SESSION_SECRET tiene solo {len(SESSION_SECRET)} caracteres. "
            "Se recomienda al menos 64 caracteres para producción."
        )

    # Verificar que SESSION_COOKIE_SECURE esté activado en producción
    if PRODUCTION and not SESSION_COOKIE_SECURE:
        warnings_list.append(
            "SESSION_COOKIE_SECURE está desactivado en modo producción. "
            "Active WFD_SESSION_SECURE=true para cookies seguras sobre HTTPS."
        )

    return warnings_list


# ── Validación de configuración ────────────────────────────


def x_validate_config__mutmut_9() -> list[str]:
    """
    Valida la configuración del sistema y retorna una lista de advertencias.

    En producción, los secrets faltantes causan RuntimeError al importar.
    Esta función permite detectar problemas adicionales en cualquier modo.

    Returns:
        Lista de mensajes de advertencia (vacía si todo está bien)
    """
    warnings_list = []

    # Verificar que los secrets no sean los valores por defecto inseguros
    if SESSION_SECRET == _INSECURE_SESSION_DEFAULT:
        warnings_list.append(
            "SESSION_SECRET usa el valor por defecto inseguro. Configure WFD_SESSION_SECRET antes de desplegar."
        )

    if LICENSE_SECRET_KEY == _INSECURE_LICENSE_DEFAULT:
        warnings_list.append(
            "XXLICENSE_SECRET_KEY usa el valor por defecto inseguro. Configure WFD_LICENSE_SECRET antes de desplegar.XX"
        )

    # Verificar que SESSION_SECRET tenga suficiente entropía
    if len(SESSION_SECRET) < 32:
        warnings_list.append(
            f"SESSION_SECRET tiene solo {len(SESSION_SECRET)} caracteres. "
            "Se recomienda al menos 64 caracteres para producción."
        )

    # Verificar que SESSION_COOKIE_SECURE esté activado en producción
    if PRODUCTION and not SESSION_COOKIE_SECURE:
        warnings_list.append(
            "SESSION_COOKIE_SECURE está desactivado en modo producción. "
            "Active WFD_SESSION_SECURE=true para cookies seguras sobre HTTPS."
        )

    return warnings_list


# ── Validación de configuración ────────────────────────────


def x_validate_config__mutmut_10() -> list[str]:
    """
    Valida la configuración del sistema y retorna una lista de advertencias.

    En producción, los secrets faltantes causan RuntimeError al importar.
    Esta función permite detectar problemas adicionales en cualquier modo.

    Returns:
        Lista de mensajes de advertencia (vacía si todo está bien)
    """
    warnings_list = []

    # Verificar que los secrets no sean los valores por defecto inseguros
    if SESSION_SECRET == _INSECURE_SESSION_DEFAULT:
        warnings_list.append(
            "SESSION_SECRET usa el valor por defecto inseguro. Configure WFD_SESSION_SECRET antes de desplegar."
        )

    if LICENSE_SECRET_KEY == _INSECURE_LICENSE_DEFAULT:
        warnings_list.append(
            "license_secret_key usa el valor por defecto inseguro. configure wfd_license_secret antes de desplegar."
        )

    # Verificar que SESSION_SECRET tenga suficiente entropía
    if len(SESSION_SECRET) < 32:
        warnings_list.append(
            f"SESSION_SECRET tiene solo {len(SESSION_SECRET)} caracteres. "
            "Se recomienda al menos 64 caracteres para producción."
        )

    # Verificar que SESSION_COOKIE_SECURE esté activado en producción
    if PRODUCTION and not SESSION_COOKIE_SECURE:
        warnings_list.append(
            "SESSION_COOKIE_SECURE está desactivado en modo producción. "
            "Active WFD_SESSION_SECURE=true para cookies seguras sobre HTTPS."
        )

    return warnings_list


# ── Validación de configuración ────────────────────────────


def x_validate_config__mutmut_11() -> list[str]:
    """
    Valida la configuración del sistema y retorna una lista de advertencias.

    En producción, los secrets faltantes causan RuntimeError al importar.
    Esta función permite detectar problemas adicionales en cualquier modo.

    Returns:
        Lista de mensajes de advertencia (vacía si todo está bien)
    """
    warnings_list = []

    # Verificar que los secrets no sean los valores por defecto inseguros
    if SESSION_SECRET == _INSECURE_SESSION_DEFAULT:
        warnings_list.append(
            "SESSION_SECRET usa el valor por defecto inseguro. Configure WFD_SESSION_SECRET antes de desplegar."
        )

    if LICENSE_SECRET_KEY == _INSECURE_LICENSE_DEFAULT:
        warnings_list.append(
            "LICENSE_SECRET_KEY USA EL VALOR POR DEFECTO INSEGURO. CONFIGURE WFD_LICENSE_SECRET ANTES DE DESPLEGAR."
        )

    # Verificar que SESSION_SECRET tenga suficiente entropía
    if len(SESSION_SECRET) < 32:
        warnings_list.append(
            f"SESSION_SECRET tiene solo {len(SESSION_SECRET)} caracteres. "
            "Se recomienda al menos 64 caracteres para producción."
        )

    # Verificar que SESSION_COOKIE_SECURE esté activado en producción
    if PRODUCTION and not SESSION_COOKIE_SECURE:
        warnings_list.append(
            "SESSION_COOKIE_SECURE está desactivado en modo producción. "
            "Active WFD_SESSION_SECURE=true para cookies seguras sobre HTTPS."
        )

    return warnings_list


# ── Validación de configuración ────────────────────────────


def x_validate_config__mutmut_12() -> list[str]:
    """
    Valida la configuración del sistema y retorna una lista de advertencias.

    En producción, los secrets faltantes causan RuntimeError al importar.
    Esta función permite detectar problemas adicionales en cualquier modo.

    Returns:
        Lista de mensajes de advertencia (vacía si todo está bien)
    """
    warnings_list = []

    # Verificar que los secrets no sean los valores por defecto inseguros
    if SESSION_SECRET == _INSECURE_SESSION_DEFAULT:
        warnings_list.append(
            "SESSION_SECRET usa el valor por defecto inseguro. Configure WFD_SESSION_SECRET antes de desplegar."
        )

    if LICENSE_SECRET_KEY == _INSECURE_LICENSE_DEFAULT:
        warnings_list.append(
            "LICENSE_SECRET_KEY usa el valor por defecto inseguro. Configure WFD_LICENSE_SECRET antes de desplegar."
        )

    # Verificar que SESSION_SECRET tenga suficiente entropía
    if len(SESSION_SECRET) <= 32:
        warnings_list.append(
            f"SESSION_SECRET tiene solo {len(SESSION_SECRET)} caracteres. "
            "Se recomienda al menos 64 caracteres para producción."
        )

    # Verificar que SESSION_COOKIE_SECURE esté activado en producción
    if PRODUCTION and not SESSION_COOKIE_SECURE:
        warnings_list.append(
            "SESSION_COOKIE_SECURE está desactivado en modo producción. "
            "Active WFD_SESSION_SECURE=true para cookies seguras sobre HTTPS."
        )

    return warnings_list


# ── Validación de configuración ────────────────────────────


def x_validate_config__mutmut_13() -> list[str]:
    """
    Valida la configuración del sistema y retorna una lista de advertencias.

    En producción, los secrets faltantes causan RuntimeError al importar.
    Esta función permite detectar problemas adicionales en cualquier modo.

    Returns:
        Lista de mensajes de advertencia (vacía si todo está bien)
    """
    warnings_list = []

    # Verificar que los secrets no sean los valores por defecto inseguros
    if SESSION_SECRET == _INSECURE_SESSION_DEFAULT:
        warnings_list.append(
            "SESSION_SECRET usa el valor por defecto inseguro. Configure WFD_SESSION_SECRET antes de desplegar."
        )

    if LICENSE_SECRET_KEY == _INSECURE_LICENSE_DEFAULT:
        warnings_list.append(
            "LICENSE_SECRET_KEY usa el valor por defecto inseguro. Configure WFD_LICENSE_SECRET antes de desplegar."
        )

    # Verificar que SESSION_SECRET tenga suficiente entropía
    if len(SESSION_SECRET) < 33:
        warnings_list.append(
            f"SESSION_SECRET tiene solo {len(SESSION_SECRET)} caracteres. "
            "Se recomienda al menos 64 caracteres para producción."
        )

    # Verificar que SESSION_COOKIE_SECURE esté activado en producción
    if PRODUCTION and not SESSION_COOKIE_SECURE:
        warnings_list.append(
            "SESSION_COOKIE_SECURE está desactivado en modo producción. "
            "Active WFD_SESSION_SECURE=true para cookies seguras sobre HTTPS."
        )

    return warnings_list


# ── Validación de configuración ────────────────────────────


def x_validate_config__mutmut_14() -> list[str]:
    """
    Valida la configuración del sistema y retorna una lista de advertencias.

    En producción, los secrets faltantes causan RuntimeError al importar.
    Esta función permite detectar problemas adicionales en cualquier modo.

    Returns:
        Lista de mensajes de advertencia (vacía si todo está bien)
    """
    warnings_list = []

    # Verificar que los secrets no sean los valores por defecto inseguros
    if SESSION_SECRET == _INSECURE_SESSION_DEFAULT:
        warnings_list.append(
            "SESSION_SECRET usa el valor por defecto inseguro. Configure WFD_SESSION_SECRET antes de desplegar."
        )

    if LICENSE_SECRET_KEY == _INSECURE_LICENSE_DEFAULT:
        warnings_list.append(
            "LICENSE_SECRET_KEY usa el valor por defecto inseguro. Configure WFD_LICENSE_SECRET antes de desplegar."
        )

    # Verificar que SESSION_SECRET tenga suficiente entropía
    if len(SESSION_SECRET) < 32:
        warnings_list.append(
            None
        )

    # Verificar que SESSION_COOKIE_SECURE esté activado en producción
    if PRODUCTION and not SESSION_COOKIE_SECURE:
        warnings_list.append(
            "SESSION_COOKIE_SECURE está desactivado en modo producción. "
            "Active WFD_SESSION_SECURE=true para cookies seguras sobre HTTPS."
        )

    return warnings_list


# ── Validación de configuración ────────────────────────────


def x_validate_config__mutmut_15() -> list[str]:
    """
    Valida la configuración del sistema y retorna una lista de advertencias.

    En producción, los secrets faltantes causan RuntimeError al importar.
    Esta función permite detectar problemas adicionales en cualquier modo.

    Returns:
        Lista de mensajes de advertencia (vacía si todo está bien)
    """
    warnings_list = []

    # Verificar que los secrets no sean los valores por defecto inseguros
    if SESSION_SECRET == _INSECURE_SESSION_DEFAULT:
        warnings_list.append(
            "SESSION_SECRET usa el valor por defecto inseguro. Configure WFD_SESSION_SECRET antes de desplegar."
        )

    if LICENSE_SECRET_KEY == _INSECURE_LICENSE_DEFAULT:
        warnings_list.append(
            "LICENSE_SECRET_KEY usa el valor por defecto inseguro. Configure WFD_LICENSE_SECRET antes de desplegar."
        )

    # Verificar que SESSION_SECRET tenga suficiente entropía
    if len(SESSION_SECRET) < 32:
        warnings_list.append(
            f"SESSION_SECRET tiene solo {len(SESSION_SECRET)} caracteres. "
            "XXSe recomienda al menos 64 caracteres para producción.XX"
        )

    # Verificar que SESSION_COOKIE_SECURE esté activado en producción
    if PRODUCTION and not SESSION_COOKIE_SECURE:
        warnings_list.append(
            "SESSION_COOKIE_SECURE está desactivado en modo producción. "
            "Active WFD_SESSION_SECURE=true para cookies seguras sobre HTTPS."
        )

    return warnings_list


# ── Validación de configuración ────────────────────────────


def x_validate_config__mutmut_16() -> list[str]:
    """
    Valida la configuración del sistema y retorna una lista de advertencias.

    En producción, los secrets faltantes causan RuntimeError al importar.
    Esta función permite detectar problemas adicionales en cualquier modo.

    Returns:
        Lista de mensajes de advertencia (vacía si todo está bien)
    """
    warnings_list = []

    # Verificar que los secrets no sean los valores por defecto inseguros
    if SESSION_SECRET == _INSECURE_SESSION_DEFAULT:
        warnings_list.append(
            "SESSION_SECRET usa el valor por defecto inseguro. Configure WFD_SESSION_SECRET antes de desplegar."
        )

    if LICENSE_SECRET_KEY == _INSECURE_LICENSE_DEFAULT:
        warnings_list.append(
            "LICENSE_SECRET_KEY usa el valor por defecto inseguro. Configure WFD_LICENSE_SECRET antes de desplegar."
        )

    # Verificar que SESSION_SECRET tenga suficiente entropía
    if len(SESSION_SECRET) < 32:
        warnings_list.append(
            f"SESSION_SECRET tiene solo {len(SESSION_SECRET)} caracteres. "
            "se recomienda al menos 64 caracteres para producción."
        )

    # Verificar que SESSION_COOKIE_SECURE esté activado en producción
    if PRODUCTION and not SESSION_COOKIE_SECURE:
        warnings_list.append(
            "SESSION_COOKIE_SECURE está desactivado en modo producción. "
            "Active WFD_SESSION_SECURE=true para cookies seguras sobre HTTPS."
        )

    return warnings_list


# ── Validación de configuración ────────────────────────────


def x_validate_config__mutmut_17() -> list[str]:
    """
    Valida la configuración del sistema y retorna una lista de advertencias.

    En producción, los secrets faltantes causan RuntimeError al importar.
    Esta función permite detectar problemas adicionales en cualquier modo.

    Returns:
        Lista de mensajes de advertencia (vacía si todo está bien)
    """
    warnings_list = []

    # Verificar que los secrets no sean los valores por defecto inseguros
    if SESSION_SECRET == _INSECURE_SESSION_DEFAULT:
        warnings_list.append(
            "SESSION_SECRET usa el valor por defecto inseguro. Configure WFD_SESSION_SECRET antes de desplegar."
        )

    if LICENSE_SECRET_KEY == _INSECURE_LICENSE_DEFAULT:
        warnings_list.append(
            "LICENSE_SECRET_KEY usa el valor por defecto inseguro. Configure WFD_LICENSE_SECRET antes de desplegar."
        )

    # Verificar que SESSION_SECRET tenga suficiente entropía
    if len(SESSION_SECRET) < 32:
        warnings_list.append(
            f"SESSION_SECRET tiene solo {len(SESSION_SECRET)} caracteres. "
            "SE RECOMIENDA AL MENOS 64 CARACTERES PARA PRODUCCIÓN."
        )

    # Verificar que SESSION_COOKIE_SECURE esté activado en producción
    if PRODUCTION and not SESSION_COOKIE_SECURE:
        warnings_list.append(
            "SESSION_COOKIE_SECURE está desactivado en modo producción. "
            "Active WFD_SESSION_SECURE=true para cookies seguras sobre HTTPS."
        )

    return warnings_list


# ── Validación de configuración ────────────────────────────


def x_validate_config__mutmut_18() -> list[str]:
    """
    Valida la configuración del sistema y retorna una lista de advertencias.

    En producción, los secrets faltantes causan RuntimeError al importar.
    Esta función permite detectar problemas adicionales en cualquier modo.

    Returns:
        Lista de mensajes de advertencia (vacía si todo está bien)
    """
    warnings_list = []

    # Verificar que los secrets no sean los valores por defecto inseguros
    if SESSION_SECRET == _INSECURE_SESSION_DEFAULT:
        warnings_list.append(
            "SESSION_SECRET usa el valor por defecto inseguro. Configure WFD_SESSION_SECRET antes de desplegar."
        )

    if LICENSE_SECRET_KEY == _INSECURE_LICENSE_DEFAULT:
        warnings_list.append(
            "LICENSE_SECRET_KEY usa el valor por defecto inseguro. Configure WFD_LICENSE_SECRET antes de desplegar."
        )

    # Verificar que SESSION_SECRET tenga suficiente entropía
    if len(SESSION_SECRET) < 32:
        warnings_list.append(
            f"SESSION_SECRET tiene solo {len(SESSION_SECRET)} caracteres. "
            "Se recomienda al menos 64 caracteres para producción."
        )

    # Verificar que SESSION_COOKIE_SECURE esté activado en producción
    if PRODUCTION or not SESSION_COOKIE_SECURE:
        warnings_list.append(
            "SESSION_COOKIE_SECURE está desactivado en modo producción. "
            "Active WFD_SESSION_SECURE=true para cookies seguras sobre HTTPS."
        )

    return warnings_list


# ── Validación de configuración ────────────────────────────


def x_validate_config__mutmut_19() -> list[str]:
    """
    Valida la configuración del sistema y retorna una lista de advertencias.

    En producción, los secrets faltantes causan RuntimeError al importar.
    Esta función permite detectar problemas adicionales en cualquier modo.

    Returns:
        Lista de mensajes de advertencia (vacía si todo está bien)
    """
    warnings_list = []

    # Verificar que los secrets no sean los valores por defecto inseguros
    if SESSION_SECRET == _INSECURE_SESSION_DEFAULT:
        warnings_list.append(
            "SESSION_SECRET usa el valor por defecto inseguro. Configure WFD_SESSION_SECRET antes de desplegar."
        )

    if LICENSE_SECRET_KEY == _INSECURE_LICENSE_DEFAULT:
        warnings_list.append(
            "LICENSE_SECRET_KEY usa el valor por defecto inseguro. Configure WFD_LICENSE_SECRET antes de desplegar."
        )

    # Verificar que SESSION_SECRET tenga suficiente entropía
    if len(SESSION_SECRET) < 32:
        warnings_list.append(
            f"SESSION_SECRET tiene solo {len(SESSION_SECRET)} caracteres. "
            "Se recomienda al menos 64 caracteres para producción."
        )

    # Verificar que SESSION_COOKIE_SECURE esté activado en producción
    if PRODUCTION and SESSION_COOKIE_SECURE:
        warnings_list.append(
            "SESSION_COOKIE_SECURE está desactivado en modo producción. "
            "Active WFD_SESSION_SECURE=true para cookies seguras sobre HTTPS."
        )

    return warnings_list


# ── Validación de configuración ────────────────────────────


def x_validate_config__mutmut_20() -> list[str]:
    """
    Valida la configuración del sistema y retorna una lista de advertencias.

    En producción, los secrets faltantes causan RuntimeError al importar.
    Esta función permite detectar problemas adicionales en cualquier modo.

    Returns:
        Lista de mensajes de advertencia (vacía si todo está bien)
    """
    warnings_list = []

    # Verificar que los secrets no sean los valores por defecto inseguros
    if SESSION_SECRET == _INSECURE_SESSION_DEFAULT:
        warnings_list.append(
            "SESSION_SECRET usa el valor por defecto inseguro. Configure WFD_SESSION_SECRET antes de desplegar."
        )

    if LICENSE_SECRET_KEY == _INSECURE_LICENSE_DEFAULT:
        warnings_list.append(
            "LICENSE_SECRET_KEY usa el valor por defecto inseguro. Configure WFD_LICENSE_SECRET antes de desplegar."
        )

    # Verificar que SESSION_SECRET tenga suficiente entropía
    if len(SESSION_SECRET) < 32:
        warnings_list.append(
            f"SESSION_SECRET tiene solo {len(SESSION_SECRET)} caracteres. "
            "Se recomienda al menos 64 caracteres para producción."
        )

    # Verificar que SESSION_COOKIE_SECURE esté activado en producción
    if PRODUCTION and not SESSION_COOKIE_SECURE:
        warnings_list.append(
            None
        )

    return warnings_list


# ── Validación de configuración ────────────────────────────


def x_validate_config__mutmut_21() -> list[str]:
    """
    Valida la configuración del sistema y retorna una lista de advertencias.

    En producción, los secrets faltantes causan RuntimeError al importar.
    Esta función permite detectar problemas adicionales en cualquier modo.

    Returns:
        Lista de mensajes de advertencia (vacía si todo está bien)
    """
    warnings_list = []

    # Verificar que los secrets no sean los valores por defecto inseguros
    if SESSION_SECRET == _INSECURE_SESSION_DEFAULT:
        warnings_list.append(
            "SESSION_SECRET usa el valor por defecto inseguro. Configure WFD_SESSION_SECRET antes de desplegar."
        )

    if LICENSE_SECRET_KEY == _INSECURE_LICENSE_DEFAULT:
        warnings_list.append(
            "LICENSE_SECRET_KEY usa el valor por defecto inseguro. Configure WFD_LICENSE_SECRET antes de desplegar."
        )

    # Verificar que SESSION_SECRET tenga suficiente entropía
    if len(SESSION_SECRET) < 32:
        warnings_list.append(
            f"SESSION_SECRET tiene solo {len(SESSION_SECRET)} caracteres. "
            "Se recomienda al menos 64 caracteres para producción."
        )

    # Verificar que SESSION_COOKIE_SECURE esté activado en producción
    if PRODUCTION and not SESSION_COOKIE_SECURE:
        warnings_list.append(
            "XXSESSION_COOKIE_SECURE está desactivado en modo producción. XX"
            "Active WFD_SESSION_SECURE=true para cookies seguras sobre HTTPS."
        )

    return warnings_list


# ── Validación de configuración ────────────────────────────


def x_validate_config__mutmut_22() -> list[str]:
    """
    Valida la configuración del sistema y retorna una lista de advertencias.

    En producción, los secrets faltantes causan RuntimeError al importar.
    Esta función permite detectar problemas adicionales en cualquier modo.

    Returns:
        Lista de mensajes de advertencia (vacía si todo está bien)
    """
    warnings_list = []

    # Verificar que los secrets no sean los valores por defecto inseguros
    if SESSION_SECRET == _INSECURE_SESSION_DEFAULT:
        warnings_list.append(
            "SESSION_SECRET usa el valor por defecto inseguro. Configure WFD_SESSION_SECRET antes de desplegar."
        )

    if LICENSE_SECRET_KEY == _INSECURE_LICENSE_DEFAULT:
        warnings_list.append(
            "LICENSE_SECRET_KEY usa el valor por defecto inseguro. Configure WFD_LICENSE_SECRET antes de desplegar."
        )

    # Verificar que SESSION_SECRET tenga suficiente entropía
    if len(SESSION_SECRET) < 32:
        warnings_list.append(
            f"SESSION_SECRET tiene solo {len(SESSION_SECRET)} caracteres. "
            "Se recomienda al menos 64 caracteres para producción."
        )

    # Verificar que SESSION_COOKIE_SECURE esté activado en producción
    if PRODUCTION and not SESSION_COOKIE_SECURE:
        warnings_list.append(
            "session_cookie_secure está desactivado en modo producción. "
            "Active WFD_SESSION_SECURE=true para cookies seguras sobre HTTPS."
        )

    return warnings_list


# ── Validación de configuración ────────────────────────────


def x_validate_config__mutmut_23() -> list[str]:
    """
    Valida la configuración del sistema y retorna una lista de advertencias.

    En producción, los secrets faltantes causan RuntimeError al importar.
    Esta función permite detectar problemas adicionales en cualquier modo.

    Returns:
        Lista de mensajes de advertencia (vacía si todo está bien)
    """
    warnings_list = []

    # Verificar que los secrets no sean los valores por defecto inseguros
    if SESSION_SECRET == _INSECURE_SESSION_DEFAULT:
        warnings_list.append(
            "SESSION_SECRET usa el valor por defecto inseguro. Configure WFD_SESSION_SECRET antes de desplegar."
        )

    if LICENSE_SECRET_KEY == _INSECURE_LICENSE_DEFAULT:
        warnings_list.append(
            "LICENSE_SECRET_KEY usa el valor por defecto inseguro. Configure WFD_LICENSE_SECRET antes de desplegar."
        )

    # Verificar que SESSION_SECRET tenga suficiente entropía
    if len(SESSION_SECRET) < 32:
        warnings_list.append(
            f"SESSION_SECRET tiene solo {len(SESSION_SECRET)} caracteres. "
            "Se recomienda al menos 64 caracteres para producción."
        )

    # Verificar que SESSION_COOKIE_SECURE esté activado en producción
    if PRODUCTION and not SESSION_COOKIE_SECURE:
        warnings_list.append(
            "SESSION_COOKIE_SECURE ESTÁ DESACTIVADO EN MODO PRODUCCIÓN. "
            "Active WFD_SESSION_SECURE=true para cookies seguras sobre HTTPS."
        )

    return warnings_list


# ── Validación de configuración ────────────────────────────


def x_validate_config__mutmut_24() -> list[str]:
    """
    Valida la configuración del sistema y retorna una lista de advertencias.

    En producción, los secrets faltantes causan RuntimeError al importar.
    Esta función permite detectar problemas adicionales en cualquier modo.

    Returns:
        Lista de mensajes de advertencia (vacía si todo está bien)
    """
    warnings_list = []

    # Verificar que los secrets no sean los valores por defecto inseguros
    if SESSION_SECRET == _INSECURE_SESSION_DEFAULT:
        warnings_list.append(
            "SESSION_SECRET usa el valor por defecto inseguro. Configure WFD_SESSION_SECRET antes de desplegar."
        )

    if LICENSE_SECRET_KEY == _INSECURE_LICENSE_DEFAULT:
        warnings_list.append(
            "LICENSE_SECRET_KEY usa el valor por defecto inseguro. Configure WFD_LICENSE_SECRET antes de desplegar."
        )

    # Verificar que SESSION_SECRET tenga suficiente entropía
    if len(SESSION_SECRET) < 32:
        warnings_list.append(
            f"SESSION_SECRET tiene solo {len(SESSION_SECRET)} caracteres. "
            "Se recomienda al menos 64 caracteres para producción."
        )

    # Verificar que SESSION_COOKIE_SECURE esté activado en producción
    if PRODUCTION and not SESSION_COOKIE_SECURE:
        warnings_list.append(
            "SESSION_COOKIE_SECURE está desactivado en modo producción. "
            "XXActive WFD_SESSION_SECURE=true para cookies seguras sobre HTTPS.XX"
        )

    return warnings_list


# ── Validación de configuración ────────────────────────────


def x_validate_config__mutmut_25() -> list[str]:
    """
    Valida la configuración del sistema y retorna una lista de advertencias.

    En producción, los secrets faltantes causan RuntimeError al importar.
    Esta función permite detectar problemas adicionales en cualquier modo.

    Returns:
        Lista de mensajes de advertencia (vacía si todo está bien)
    """
    warnings_list = []

    # Verificar que los secrets no sean los valores por defecto inseguros
    if SESSION_SECRET == _INSECURE_SESSION_DEFAULT:
        warnings_list.append(
            "SESSION_SECRET usa el valor por defecto inseguro. Configure WFD_SESSION_SECRET antes de desplegar."
        )

    if LICENSE_SECRET_KEY == _INSECURE_LICENSE_DEFAULT:
        warnings_list.append(
            "LICENSE_SECRET_KEY usa el valor por defecto inseguro. Configure WFD_LICENSE_SECRET antes de desplegar."
        )

    # Verificar que SESSION_SECRET tenga suficiente entropía
    if len(SESSION_SECRET) < 32:
        warnings_list.append(
            f"SESSION_SECRET tiene solo {len(SESSION_SECRET)} caracteres. "
            "Se recomienda al menos 64 caracteres para producción."
        )

    # Verificar que SESSION_COOKIE_SECURE esté activado en producción
    if PRODUCTION and not SESSION_COOKIE_SECURE:
        warnings_list.append(
            "SESSION_COOKIE_SECURE está desactivado en modo producción. "
            "active wfd_session_secure=true para cookies seguras sobre https."
        )

    return warnings_list


# ── Validación de configuración ────────────────────────────


def x_validate_config__mutmut_26() -> list[str]:
    """
    Valida la configuración del sistema y retorna una lista de advertencias.

    En producción, los secrets faltantes causan RuntimeError al importar.
    Esta función permite detectar problemas adicionales en cualquier modo.

    Returns:
        Lista de mensajes de advertencia (vacía si todo está bien)
    """
    warnings_list = []

    # Verificar que los secrets no sean los valores por defecto inseguros
    if SESSION_SECRET == _INSECURE_SESSION_DEFAULT:
        warnings_list.append(
            "SESSION_SECRET usa el valor por defecto inseguro. Configure WFD_SESSION_SECRET antes de desplegar."
        )

    if LICENSE_SECRET_KEY == _INSECURE_LICENSE_DEFAULT:
        warnings_list.append(
            "LICENSE_SECRET_KEY usa el valor por defecto inseguro. Configure WFD_LICENSE_SECRET antes de desplegar."
        )

    # Verificar que SESSION_SECRET tenga suficiente entropía
    if len(SESSION_SECRET) < 32:
        warnings_list.append(
            f"SESSION_SECRET tiene solo {len(SESSION_SECRET)} caracteres. "
            "Se recomienda al menos 64 caracteres para producción."
        )

    # Verificar que SESSION_COOKIE_SECURE esté activado en producción
    if PRODUCTION and not SESSION_COOKIE_SECURE:
        warnings_list.append(
            "SESSION_COOKIE_SECURE está desactivado en modo producción. "
            "ACTIVE WFD_SESSION_SECURE=TRUE PARA COOKIES SEGURAS SOBRE HTTPS."
        )

    return warnings_list

mutants_x_validate_config__mutmut['_mutmut_orig'] = x_validate_config__mutmut_orig # type: ignore # mutmut generated
mutants_x_validate_config__mutmut['x_validate_config__mutmut_1'] = x_validate_config__mutmut_1 # type: ignore # mutmut generated
mutants_x_validate_config__mutmut['x_validate_config__mutmut_2'] = x_validate_config__mutmut_2 # type: ignore # mutmut generated
mutants_x_validate_config__mutmut['x_validate_config__mutmut_3'] = x_validate_config__mutmut_3 # type: ignore # mutmut generated
mutants_x_validate_config__mutmut['x_validate_config__mutmut_4'] = x_validate_config__mutmut_4 # type: ignore # mutmut generated
mutants_x_validate_config__mutmut['x_validate_config__mutmut_5'] = x_validate_config__mutmut_5 # type: ignore # mutmut generated
mutants_x_validate_config__mutmut['x_validate_config__mutmut_6'] = x_validate_config__mutmut_6 # type: ignore # mutmut generated
mutants_x_validate_config__mutmut['x_validate_config__mutmut_7'] = x_validate_config__mutmut_7 # type: ignore # mutmut generated
mutants_x_validate_config__mutmut['x_validate_config__mutmut_8'] = x_validate_config__mutmut_8 # type: ignore # mutmut generated
mutants_x_validate_config__mutmut['x_validate_config__mutmut_9'] = x_validate_config__mutmut_9 # type: ignore # mutmut generated
mutants_x_validate_config__mutmut['x_validate_config__mutmut_10'] = x_validate_config__mutmut_10 # type: ignore # mutmut generated
mutants_x_validate_config__mutmut['x_validate_config__mutmut_11'] = x_validate_config__mutmut_11 # type: ignore # mutmut generated
mutants_x_validate_config__mutmut['x_validate_config__mutmut_12'] = x_validate_config__mutmut_12 # type: ignore # mutmut generated
mutants_x_validate_config__mutmut['x_validate_config__mutmut_13'] = x_validate_config__mutmut_13 # type: ignore # mutmut generated
mutants_x_validate_config__mutmut['x_validate_config__mutmut_14'] = x_validate_config__mutmut_14 # type: ignore # mutmut generated
mutants_x_validate_config__mutmut['x_validate_config__mutmut_15'] = x_validate_config__mutmut_15 # type: ignore # mutmut generated
mutants_x_validate_config__mutmut['x_validate_config__mutmut_16'] = x_validate_config__mutmut_16 # type: ignore # mutmut generated
mutants_x_validate_config__mutmut['x_validate_config__mutmut_17'] = x_validate_config__mutmut_17 # type: ignore # mutmut generated
mutants_x_validate_config__mutmut['x_validate_config__mutmut_18'] = x_validate_config__mutmut_18 # type: ignore # mutmut generated
mutants_x_validate_config__mutmut['x_validate_config__mutmut_19'] = x_validate_config__mutmut_19 # type: ignore # mutmut generated
mutants_x_validate_config__mutmut['x_validate_config__mutmut_20'] = x_validate_config__mutmut_20 # type: ignore # mutmut generated
mutants_x_validate_config__mutmut['x_validate_config__mutmut_21'] = x_validate_config__mutmut_21 # type: ignore # mutmut generated
mutants_x_validate_config__mutmut['x_validate_config__mutmut_22'] = x_validate_config__mutmut_22 # type: ignore # mutmut generated
mutants_x_validate_config__mutmut['x_validate_config__mutmut_23'] = x_validate_config__mutmut_23 # type: ignore # mutmut generated
mutants_x_validate_config__mutmut['x_validate_config__mutmut_24'] = x_validate_config__mutmut_24 # type: ignore # mutmut generated
mutants_x_validate_config__mutmut['x_validate_config__mutmut_25'] = x_validate_config__mutmut_25 # type: ignore # mutmut generated
mutants_x_validate_config__mutmut['x_validate_config__mutmut_26'] = x_validate_config__mutmut_26 # type: ignore # mutmut generated
