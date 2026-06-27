"""Políticas de retención de evidencia por jurisdicción LATAM.

Foso 1 — Compliance Reproducible Banca LATAM.

Reguladores y requerimientos de retención (años):

    País       Regulador   Bank/Fin  Healthcare  PII
    ----------------------------------------------------
    México     CNBV        10        10          5
    Brasil     BACEN       10        10          5
    Argentina  BCRA/CNV    10        10          5
    Colombia   SFC         5         10          5
    Chile      CMF         5         10          5
    Perú       SBS         10        10          5
    Ecuador    SBS         7         10          5
    Uruguay    BCU         10        10          5
    Paraguay   BCP         5         10          5
    Bolivia    ASFI        10        10          5

Las políticas se aplican al purgar audit_log_chain y orbital_executions:
cualquier entry con antiguedad > retention_days NO se elimina, sino que
se archiva (move-to-cold-storage) o se mantiene en sitio.

Uso:
    from src.compliance.retention_policy import get_retention_days, should_purge
    days = get_retention_days("MX", "banking")  # → 3650
    should = should_purge(entry_timestamp, country="MX", data_type="banking")
"""
from __future__ import annotations

import time
from typing import Any

# Retención en días por (país, tipo_de_dato).
# Tipo: banking | healthcare | pii | general
# Basado en regulaciones LATAM vigentes a junio 2026.
RETENTION_DAYS: dict[tuple[str, str], int] = {
    # México — CNBV (banca) / INAI (PII)
    ("MX", "banking"): 365 * 10,
    ("MX", "healthcare"): 365 * 10,
    ("MX", "pii"): 365 * 5,
    ("MX", "general"): 365 * 5,
    # Brasil — BACEN (banca) / ANPD (PII, LGPD)
    ("BR", "banking"): 365 * 10,
    ("BR", "healthcare"): 365 * 10,
    ("BR", "pii"): 365 * 5,
    ("BR", "general"): 365 * 5,
    # Argentina — BCRA (banca) / CNV (financiero) / AAIP (PII)
    ("AR", "banking"): 365 * 10,
    ("AR", "healthcare"): 365 * 10,
    ("AR", "pii"): 365 * 5,
    ("AR", "general"): 365 * 5,
    # Colombia — SFC (financiero) / SIC (PII)
    ("CO", "banking"): 365 * 5,
    ("CO", "healthcare"): 365 * 10,
    ("CO", "pii"): 365 * 5,
    ("CO", "general"): 365 * 5,
    # Chile — CMF (banca) / SAG (salud)
    ("CL", "banking"): 365 * 5,
    ("CL", "healthcare"): 365 * 10,
    ("CL", "pii"): 365 * 5,
    ("CL", "general"): 365 * 5,
    # Perú — SBS (banca) / INDECOPI (PII)
    ("PE", "banking"): 365 * 10,
    ("PE", "healthcare"): 365 * 10,
    ("PE", "pii"): 365 * 5,
    ("PE", "general"): 365 * 5,
    # Ecuador — SBS (banca) / SPD (PII)
    ("EC", "banking"): 365 * 7,
    ("EC", "healthcare"): 365 * 10,
    ("EC", "pii"): 365 * 5,
    ("EC", "general"): 365 * 5,
    # Uruguay — BCU
    ("UY", "banking"): 365 * 10,
    ("UY", "healthcare"): 365 * 10,
    ("UY", "pii"): 365 * 5,
    ("UY", "general"): 365 * 5,
    # Paraguay — BCP
    ("PY", "banking"): 365 * 5,
    ("PY", "healthcare"): 365 * 10,
    ("PY", "pii"): 365 * 5,
    ("PY", "general"): 365 * 5,
    # Bolivia — ASFI
    ("BO", "banking"): 365 * 10,
    ("BO", "healthcare"): 365 * 10,
    ("BO", "pii"): 365 * 5,
    ("BO", "general"): 365 * 5,
}

# Default fallback (5 años, conservador) si país no está listado.
DEFAULT_RETENTION_DAYS = 365 * 5

# Regulador oficial por país (para reportes regulatorios).
REGULATOR_BY_COUNTRY: dict[str, str] = {
    "MX": "CNBV",
    "BR": "BACEN",
    "AR": "BCRA",
    "CO": "SFC",
    "CL": "CMF",
    "PE": "SBS",
    "EC": "SBS",
    "UY": "BCU",
    "PY": "BCP",
    "BO": "ASFI",
}


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_get_retention_days__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_retention_days__mutmut)
def get_retention_days(country_code: str, data_type: str = "banking") -> int:
    """Retorna los días de retención obligatoria para un país y tipo de dato.

    Args:
        country_code: ISO 3166-1 alpha-2 (MX, BR, AR, CO, CL, PE, EC, UY, PY, BO).
        data_type: Tipo de dato (banking, healthcare, pii, general).

    Returns:
        Días de retención. Default 5 años (1825) si país no está listado.
    """
    return RETENTION_DAYS.get(
        (country_code.upper(), data_type.lower()),
        DEFAULT_RETENTION_DAYS,
    )


def x_get_retention_days__mutmut_orig(country_code: str, data_type: str = "banking") -> int:
    """Retorna los días de retención obligatoria para un país y tipo de dato.

    Args:
        country_code: ISO 3166-1 alpha-2 (MX, BR, AR, CO, CL, PE, EC, UY, PY, BO).
        data_type: Tipo de dato (banking, healthcare, pii, general).

    Returns:
        Días de retención. Default 5 años (1825) si país no está listado.
    """
    return RETENTION_DAYS.get(
        (country_code.upper(), data_type.lower()),
        DEFAULT_RETENTION_DAYS,
    )


def x_get_retention_days__mutmut_1(country_code: str, data_type: str = "XXbankingXX") -> int:
    """Retorna los días de retención obligatoria para un país y tipo de dato.

    Args:
        country_code: ISO 3166-1 alpha-2 (MX, BR, AR, CO, CL, PE, EC, UY, PY, BO).
        data_type: Tipo de dato (banking, healthcare, pii, general).

    Returns:
        Días de retención. Default 5 años (1825) si país no está listado.
    """
    return RETENTION_DAYS.get(
        (country_code.upper(), data_type.lower()),
        DEFAULT_RETENTION_DAYS,
    )


def x_get_retention_days__mutmut_2(country_code: str, data_type: str = "BANKING") -> int:
    """Retorna los días de retención obligatoria para un país y tipo de dato.

    Args:
        country_code: ISO 3166-1 alpha-2 (MX, BR, AR, CO, CL, PE, EC, UY, PY, BO).
        data_type: Tipo de dato (banking, healthcare, pii, general).

    Returns:
        Días de retención. Default 5 años (1825) si país no está listado.
    """
    return RETENTION_DAYS.get(
        (country_code.upper(), data_type.lower()),
        DEFAULT_RETENTION_DAYS,
    )


def x_get_retention_days__mutmut_3(country_code: str, data_type: str = "banking") -> int:
    """Retorna los días de retención obligatoria para un país y tipo de dato.

    Args:
        country_code: ISO 3166-1 alpha-2 (MX, BR, AR, CO, CL, PE, EC, UY, PY, BO).
        data_type: Tipo de dato (banking, healthcare, pii, general).

    Returns:
        Días de retención. Default 5 años (1825) si país no está listado.
    """
    return RETENTION_DAYS.get(
        None,
        DEFAULT_RETENTION_DAYS,
    )


def x_get_retention_days__mutmut_4(country_code: str, data_type: str = "banking") -> int:
    """Retorna los días de retención obligatoria para un país y tipo de dato.

    Args:
        country_code: ISO 3166-1 alpha-2 (MX, BR, AR, CO, CL, PE, EC, UY, PY, BO).
        data_type: Tipo de dato (banking, healthcare, pii, general).

    Returns:
        Días de retención. Default 5 años (1825) si país no está listado.
    """
    return RETENTION_DAYS.get(
        (country_code.upper(), data_type.lower()),
        None,
    )


def x_get_retention_days__mutmut_5(country_code: str, data_type: str = "banking") -> int:
    """Retorna los días de retención obligatoria para un país y tipo de dato.

    Args:
        country_code: ISO 3166-1 alpha-2 (MX, BR, AR, CO, CL, PE, EC, UY, PY, BO).
        data_type: Tipo de dato (banking, healthcare, pii, general).

    Returns:
        Días de retención. Default 5 años (1825) si país no está listado.
    """
    return RETENTION_DAYS.get(
        DEFAULT_RETENTION_DAYS,
    )


def x_get_retention_days__mutmut_6(country_code: str, data_type: str = "banking") -> int:
    """Retorna los días de retención obligatoria para un país y tipo de dato.

    Args:
        country_code: ISO 3166-1 alpha-2 (MX, BR, AR, CO, CL, PE, EC, UY, PY, BO).
        data_type: Tipo de dato (banking, healthcare, pii, general).

    Returns:
        Días de retención. Default 5 años (1825) si país no está listado.
    """
    return RETENTION_DAYS.get(
        (country_code.upper(), data_type.lower()),
        )


def x_get_retention_days__mutmut_7(country_code: str, data_type: str = "banking") -> int:
    """Retorna los días de retención obligatoria para un país y tipo de dato.

    Args:
        country_code: ISO 3166-1 alpha-2 (MX, BR, AR, CO, CL, PE, EC, UY, PY, BO).
        data_type: Tipo de dato (banking, healthcare, pii, general).

    Returns:
        Días de retención. Default 5 años (1825) si país no está listado.
    """
    return RETENTION_DAYS.get(
        (country_code.lower(), data_type.lower()),
        DEFAULT_RETENTION_DAYS,
    )


def x_get_retention_days__mutmut_8(country_code: str, data_type: str = "banking") -> int:
    """Retorna los días de retención obligatoria para un país y tipo de dato.

    Args:
        country_code: ISO 3166-1 alpha-2 (MX, BR, AR, CO, CL, PE, EC, UY, PY, BO).
        data_type: Tipo de dato (banking, healthcare, pii, general).

    Returns:
        Días de retención. Default 5 años (1825) si país no está listado.
    """
    return RETENTION_DAYS.get(
        (country_code.upper(), data_type.upper()),
        DEFAULT_RETENTION_DAYS,
    )

mutants_x_get_retention_days__mutmut['_mutmut_orig'] = x_get_retention_days__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_retention_days__mutmut['x_get_retention_days__mutmut_1'] = x_get_retention_days__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_retention_days__mutmut['x_get_retention_days__mutmut_2'] = x_get_retention_days__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_retention_days__mutmut['x_get_retention_days__mutmut_3'] = x_get_retention_days__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_retention_days__mutmut['x_get_retention_days__mutmut_4'] = x_get_retention_days__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_retention_days__mutmut['x_get_retention_days__mutmut_5'] = x_get_retention_days__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_retention_days__mutmut['x_get_retention_days__mutmut_6'] = x_get_retention_days__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_retention_days__mutmut['x_get_retention_days__mutmut_7'] = x_get_retention_days__mutmut_7 # type: ignore # mutmut generated
mutants_x_get_retention_days__mutmut['x_get_retention_days__mutmut_8'] = x_get_retention_days__mutmut_8 # type: ignore # mutmut generated
mutants_x_get_regulator_name__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_regulator_name__mutmut)
def get_regulator_name(country_code: str) -> str:
    """Retorna el nombre del regulador financiero de un país LATAM."""
    return REGULATOR_BY_COUNTRY.get(country_code.upper(), "Desconocido")


def x_get_regulator_name__mutmut_orig(country_code: str) -> str:
    """Retorna el nombre del regulador financiero de un país LATAM."""
    return REGULATOR_BY_COUNTRY.get(country_code.upper(), "Desconocido")


def x_get_regulator_name__mutmut_1(country_code: str) -> str:
    """Retorna el nombre del regulador financiero de un país LATAM."""
    return REGULATOR_BY_COUNTRY.get(None, "Desconocido")


def x_get_regulator_name__mutmut_2(country_code: str) -> str:
    """Retorna el nombre del regulador financiero de un país LATAM."""
    return REGULATOR_BY_COUNTRY.get(country_code.upper(), None)


def x_get_regulator_name__mutmut_3(country_code: str) -> str:
    """Retorna el nombre del regulador financiero de un país LATAM."""
    return REGULATOR_BY_COUNTRY.get("Desconocido")


def x_get_regulator_name__mutmut_4(country_code: str) -> str:
    """Retorna el nombre del regulador financiero de un país LATAM."""
    return REGULATOR_BY_COUNTRY.get(country_code.upper(), )


def x_get_regulator_name__mutmut_5(country_code: str) -> str:
    """Retorna el nombre del regulador financiero de un país LATAM."""
    return REGULATOR_BY_COUNTRY.get(country_code.lower(), "Desconocido")


def x_get_regulator_name__mutmut_6(country_code: str) -> str:
    """Retorna el nombre del regulador financiero de un país LATAM."""
    return REGULATOR_BY_COUNTRY.get(country_code.upper(), "XXDesconocidoXX")


def x_get_regulator_name__mutmut_7(country_code: str) -> str:
    """Retorna el nombre del regulador financiero de un país LATAM."""
    return REGULATOR_BY_COUNTRY.get(country_code.upper(), "desconocido")


def x_get_regulator_name__mutmut_8(country_code: str) -> str:
    """Retorna el nombre del regulador financiero de un país LATAM."""
    return REGULATOR_BY_COUNTRY.get(country_code.upper(), "DESCONOCIDO")

mutants_x_get_regulator_name__mutmut['_mutmut_orig'] = x_get_regulator_name__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_regulator_name__mutmut['x_get_regulator_name__mutmut_1'] = x_get_regulator_name__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_regulator_name__mutmut['x_get_regulator_name__mutmut_2'] = x_get_regulator_name__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_regulator_name__mutmut['x_get_regulator_name__mutmut_3'] = x_get_regulator_name__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_regulator_name__mutmut['x_get_regulator_name__mutmut_4'] = x_get_regulator_name__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_regulator_name__mutmut['x_get_regulator_name__mutmut_5'] = x_get_regulator_name__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_regulator_name__mutmut['x_get_regulator_name__mutmut_6'] = x_get_regulator_name__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_regulator_name__mutmut['x_get_regulator_name__mutmut_7'] = x_get_regulator_name__mutmut_7 # type: ignore # mutmut generated
mutants_x_get_regulator_name__mutmut['x_get_regulator_name__mutmut_8'] = x_get_regulator_name__mutmut_8 # type: ignore # mutmut generated
mutants_x_should_purge__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_should_purge__mutmut)
def should_purge(
    entry_timestamp: float,
    country_code: str = "MX",
    data_type: str = "banking",
    now: float | None = None,
) -> bool:
    """Determina si un entry puede ser purgado/archivado según la política.

    Un entry puede purgarse cuando su antiguedad excede el período de retención
    obligatorio del país. Antes de eso, debe conservarse in situ para auditoría.

    Args:
        entry_timestamp: Unix timestamp del entry.
        country_code: ISO 3166-1 alpha-2.
        data_type: Tipo de dato.
        now: Timestamp de referencia (default: time.time()).

    Returns:
        True si el entry puede purgarse (retención cumplida), False si debe
        conservarse.
    """
    if now is None:
        now = time.time()
    age_days = (now - entry_timestamp) / 86400
    retention_days = get_retention_days(country_code, data_type)
    return age_days > retention_days


def x_should_purge__mutmut_orig(
    entry_timestamp: float,
    country_code: str = "MX",
    data_type: str = "banking",
    now: float | None = None,
) -> bool:
    """Determina si un entry puede ser purgado/archivado según la política.

    Un entry puede purgarse cuando su antiguedad excede el período de retención
    obligatorio del país. Antes de eso, debe conservarse in situ para auditoría.

    Args:
        entry_timestamp: Unix timestamp del entry.
        country_code: ISO 3166-1 alpha-2.
        data_type: Tipo de dato.
        now: Timestamp de referencia (default: time.time()).

    Returns:
        True si el entry puede purgarse (retención cumplida), False si debe
        conservarse.
    """
    if now is None:
        now = time.time()
    age_days = (now - entry_timestamp) / 86400
    retention_days = get_retention_days(country_code, data_type)
    return age_days > retention_days


def x_should_purge__mutmut_1(
    entry_timestamp: float,
    country_code: str = "XXMXXX",
    data_type: str = "banking",
    now: float | None = None,
) -> bool:
    """Determina si un entry puede ser purgado/archivado según la política.

    Un entry puede purgarse cuando su antiguedad excede el período de retención
    obligatorio del país. Antes de eso, debe conservarse in situ para auditoría.

    Args:
        entry_timestamp: Unix timestamp del entry.
        country_code: ISO 3166-1 alpha-2.
        data_type: Tipo de dato.
        now: Timestamp de referencia (default: time.time()).

    Returns:
        True si el entry puede purgarse (retención cumplida), False si debe
        conservarse.
    """
    if now is None:
        now = time.time()
    age_days = (now - entry_timestamp) / 86400
    retention_days = get_retention_days(country_code, data_type)
    return age_days > retention_days


def x_should_purge__mutmut_2(
    entry_timestamp: float,
    country_code: str = "mx",
    data_type: str = "banking",
    now: float | None = None,
) -> bool:
    """Determina si un entry puede ser purgado/archivado según la política.

    Un entry puede purgarse cuando su antiguedad excede el período de retención
    obligatorio del país. Antes de eso, debe conservarse in situ para auditoría.

    Args:
        entry_timestamp: Unix timestamp del entry.
        country_code: ISO 3166-1 alpha-2.
        data_type: Tipo de dato.
        now: Timestamp de referencia (default: time.time()).

    Returns:
        True si el entry puede purgarse (retención cumplida), False si debe
        conservarse.
    """
    if now is None:
        now = time.time()
    age_days = (now - entry_timestamp) / 86400
    retention_days = get_retention_days(country_code, data_type)
    return age_days > retention_days


def x_should_purge__mutmut_3(
    entry_timestamp: float,
    country_code: str = "MX",
    data_type: str = "XXbankingXX",
    now: float | None = None,
) -> bool:
    """Determina si un entry puede ser purgado/archivado según la política.

    Un entry puede purgarse cuando su antiguedad excede el período de retención
    obligatorio del país. Antes de eso, debe conservarse in situ para auditoría.

    Args:
        entry_timestamp: Unix timestamp del entry.
        country_code: ISO 3166-1 alpha-2.
        data_type: Tipo de dato.
        now: Timestamp de referencia (default: time.time()).

    Returns:
        True si el entry puede purgarse (retención cumplida), False si debe
        conservarse.
    """
    if now is None:
        now = time.time()
    age_days = (now - entry_timestamp) / 86400
    retention_days = get_retention_days(country_code, data_type)
    return age_days > retention_days


def x_should_purge__mutmut_4(
    entry_timestamp: float,
    country_code: str = "MX",
    data_type: str = "BANKING",
    now: float | None = None,
) -> bool:
    """Determina si un entry puede ser purgado/archivado según la política.

    Un entry puede purgarse cuando su antiguedad excede el período de retención
    obligatorio del país. Antes de eso, debe conservarse in situ para auditoría.

    Args:
        entry_timestamp: Unix timestamp del entry.
        country_code: ISO 3166-1 alpha-2.
        data_type: Tipo de dato.
        now: Timestamp de referencia (default: time.time()).

    Returns:
        True si el entry puede purgarse (retención cumplida), False si debe
        conservarse.
    """
    if now is None:
        now = time.time()
    age_days = (now - entry_timestamp) / 86400
    retention_days = get_retention_days(country_code, data_type)
    return age_days > retention_days


def x_should_purge__mutmut_5(
    entry_timestamp: float,
    country_code: str = "MX",
    data_type: str = "banking",
    now: float | None = None,
) -> bool:
    """Determina si un entry puede ser purgado/archivado según la política.

    Un entry puede purgarse cuando su antiguedad excede el período de retención
    obligatorio del país. Antes de eso, debe conservarse in situ para auditoría.

    Args:
        entry_timestamp: Unix timestamp del entry.
        country_code: ISO 3166-1 alpha-2.
        data_type: Tipo de dato.
        now: Timestamp de referencia (default: time.time()).

    Returns:
        True si el entry puede purgarse (retención cumplida), False si debe
        conservarse.
    """
    if now is not None:
        now = time.time()
    age_days = (now - entry_timestamp) / 86400
    retention_days = get_retention_days(country_code, data_type)
    return age_days > retention_days


def x_should_purge__mutmut_6(
    entry_timestamp: float,
    country_code: str = "MX",
    data_type: str = "banking",
    now: float | None = None,
) -> bool:
    """Determina si un entry puede ser purgado/archivado según la política.

    Un entry puede purgarse cuando su antiguedad excede el período de retención
    obligatorio del país. Antes de eso, debe conservarse in situ para auditoría.

    Args:
        entry_timestamp: Unix timestamp del entry.
        country_code: ISO 3166-1 alpha-2.
        data_type: Tipo de dato.
        now: Timestamp de referencia (default: time.time()).

    Returns:
        True si el entry puede purgarse (retención cumplida), False si debe
        conservarse.
    """
    if now is None:
        now = None
    age_days = (now - entry_timestamp) / 86400
    retention_days = get_retention_days(country_code, data_type)
    return age_days > retention_days


def x_should_purge__mutmut_7(
    entry_timestamp: float,
    country_code: str = "MX",
    data_type: str = "banking",
    now: float | None = None,
) -> bool:
    """Determina si un entry puede ser purgado/archivado según la política.

    Un entry puede purgarse cuando su antiguedad excede el período de retención
    obligatorio del país. Antes de eso, debe conservarse in situ para auditoría.

    Args:
        entry_timestamp: Unix timestamp del entry.
        country_code: ISO 3166-1 alpha-2.
        data_type: Tipo de dato.
        now: Timestamp de referencia (default: time.time()).

    Returns:
        True si el entry puede purgarse (retención cumplida), False si debe
        conservarse.
    """
    if now is None:
        now = time.time()
    age_days = None
    retention_days = get_retention_days(country_code, data_type)
    return age_days > retention_days


def x_should_purge__mutmut_8(
    entry_timestamp: float,
    country_code: str = "MX",
    data_type: str = "banking",
    now: float | None = None,
) -> bool:
    """Determina si un entry puede ser purgado/archivado según la política.

    Un entry puede purgarse cuando su antiguedad excede el período de retención
    obligatorio del país. Antes de eso, debe conservarse in situ para auditoría.

    Args:
        entry_timestamp: Unix timestamp del entry.
        country_code: ISO 3166-1 alpha-2.
        data_type: Tipo de dato.
        now: Timestamp de referencia (default: time.time()).

    Returns:
        True si el entry puede purgarse (retención cumplida), False si debe
        conservarse.
    """
    if now is None:
        now = time.time()
    age_days = (now - entry_timestamp) * 86400
    retention_days = get_retention_days(country_code, data_type)
    return age_days > retention_days


def x_should_purge__mutmut_9(
    entry_timestamp: float,
    country_code: str = "MX",
    data_type: str = "banking",
    now: float | None = None,
) -> bool:
    """Determina si un entry puede ser purgado/archivado según la política.

    Un entry puede purgarse cuando su antiguedad excede el período de retención
    obligatorio del país. Antes de eso, debe conservarse in situ para auditoría.

    Args:
        entry_timestamp: Unix timestamp del entry.
        country_code: ISO 3166-1 alpha-2.
        data_type: Tipo de dato.
        now: Timestamp de referencia (default: time.time()).

    Returns:
        True si el entry puede purgarse (retención cumplida), False si debe
        conservarse.
    """
    if now is None:
        now = time.time()
    age_days = (now + entry_timestamp) / 86400
    retention_days = get_retention_days(country_code, data_type)
    return age_days > retention_days


def x_should_purge__mutmut_10(
    entry_timestamp: float,
    country_code: str = "MX",
    data_type: str = "banking",
    now: float | None = None,
) -> bool:
    """Determina si un entry puede ser purgado/archivado según la política.

    Un entry puede purgarse cuando su antiguedad excede el período de retención
    obligatorio del país. Antes de eso, debe conservarse in situ para auditoría.

    Args:
        entry_timestamp: Unix timestamp del entry.
        country_code: ISO 3166-1 alpha-2.
        data_type: Tipo de dato.
        now: Timestamp de referencia (default: time.time()).

    Returns:
        True si el entry puede purgarse (retención cumplida), False si debe
        conservarse.
    """
    if now is None:
        now = time.time()
    age_days = (now - entry_timestamp) / 86401
    retention_days = get_retention_days(country_code, data_type)
    return age_days > retention_days


def x_should_purge__mutmut_11(
    entry_timestamp: float,
    country_code: str = "MX",
    data_type: str = "banking",
    now: float | None = None,
) -> bool:
    """Determina si un entry puede ser purgado/archivado según la política.

    Un entry puede purgarse cuando su antiguedad excede el período de retención
    obligatorio del país. Antes de eso, debe conservarse in situ para auditoría.

    Args:
        entry_timestamp: Unix timestamp del entry.
        country_code: ISO 3166-1 alpha-2.
        data_type: Tipo de dato.
        now: Timestamp de referencia (default: time.time()).

    Returns:
        True si el entry puede purgarse (retención cumplida), False si debe
        conservarse.
    """
    if now is None:
        now = time.time()
    age_days = (now - entry_timestamp) / 86400
    retention_days = None
    return age_days > retention_days


def x_should_purge__mutmut_12(
    entry_timestamp: float,
    country_code: str = "MX",
    data_type: str = "banking",
    now: float | None = None,
) -> bool:
    """Determina si un entry puede ser purgado/archivado según la política.

    Un entry puede purgarse cuando su antiguedad excede el período de retención
    obligatorio del país. Antes de eso, debe conservarse in situ para auditoría.

    Args:
        entry_timestamp: Unix timestamp del entry.
        country_code: ISO 3166-1 alpha-2.
        data_type: Tipo de dato.
        now: Timestamp de referencia (default: time.time()).

    Returns:
        True si el entry puede purgarse (retención cumplida), False si debe
        conservarse.
    """
    if now is None:
        now = time.time()
    age_days = (now - entry_timestamp) / 86400
    retention_days = get_retention_days(None, data_type)
    return age_days > retention_days


def x_should_purge__mutmut_13(
    entry_timestamp: float,
    country_code: str = "MX",
    data_type: str = "banking",
    now: float | None = None,
) -> bool:
    """Determina si un entry puede ser purgado/archivado según la política.

    Un entry puede purgarse cuando su antiguedad excede el período de retención
    obligatorio del país. Antes de eso, debe conservarse in situ para auditoría.

    Args:
        entry_timestamp: Unix timestamp del entry.
        country_code: ISO 3166-1 alpha-2.
        data_type: Tipo de dato.
        now: Timestamp de referencia (default: time.time()).

    Returns:
        True si el entry puede purgarse (retención cumplida), False si debe
        conservarse.
    """
    if now is None:
        now = time.time()
    age_days = (now - entry_timestamp) / 86400
    retention_days = get_retention_days(country_code, None)
    return age_days > retention_days


def x_should_purge__mutmut_14(
    entry_timestamp: float,
    country_code: str = "MX",
    data_type: str = "banking",
    now: float | None = None,
) -> bool:
    """Determina si un entry puede ser purgado/archivado según la política.

    Un entry puede purgarse cuando su antiguedad excede el período de retención
    obligatorio del país. Antes de eso, debe conservarse in situ para auditoría.

    Args:
        entry_timestamp: Unix timestamp del entry.
        country_code: ISO 3166-1 alpha-2.
        data_type: Tipo de dato.
        now: Timestamp de referencia (default: time.time()).

    Returns:
        True si el entry puede purgarse (retención cumplida), False si debe
        conservarse.
    """
    if now is None:
        now = time.time()
    age_days = (now - entry_timestamp) / 86400
    retention_days = get_retention_days(data_type)
    return age_days > retention_days


def x_should_purge__mutmut_15(
    entry_timestamp: float,
    country_code: str = "MX",
    data_type: str = "banking",
    now: float | None = None,
) -> bool:
    """Determina si un entry puede ser purgado/archivado según la política.

    Un entry puede purgarse cuando su antiguedad excede el período de retención
    obligatorio del país. Antes de eso, debe conservarse in situ para auditoría.

    Args:
        entry_timestamp: Unix timestamp del entry.
        country_code: ISO 3166-1 alpha-2.
        data_type: Tipo de dato.
        now: Timestamp de referencia (default: time.time()).

    Returns:
        True si el entry puede purgarse (retención cumplida), False si debe
        conservarse.
    """
    if now is None:
        now = time.time()
    age_days = (now - entry_timestamp) / 86400
    retention_days = get_retention_days(country_code, )
    return age_days > retention_days


def x_should_purge__mutmut_16(
    entry_timestamp: float,
    country_code: str = "MX",
    data_type: str = "banking",
    now: float | None = None,
) -> bool:
    """Determina si un entry puede ser purgado/archivado según la política.

    Un entry puede purgarse cuando su antiguedad excede el período de retención
    obligatorio del país. Antes de eso, debe conservarse in situ para auditoría.

    Args:
        entry_timestamp: Unix timestamp del entry.
        country_code: ISO 3166-1 alpha-2.
        data_type: Tipo de dato.
        now: Timestamp de referencia (default: time.time()).

    Returns:
        True si el entry puede purgarse (retención cumplida), False si debe
        conservarse.
    """
    if now is None:
        now = time.time()
    age_days = (now - entry_timestamp) / 86400
    retention_days = get_retention_days(country_code, data_type)
    return age_days >= retention_days

mutants_x_should_purge__mutmut['_mutmut_orig'] = x_should_purge__mutmut_orig # type: ignore # mutmut generated
mutants_x_should_purge__mutmut['x_should_purge__mutmut_1'] = x_should_purge__mutmut_1 # type: ignore # mutmut generated
mutants_x_should_purge__mutmut['x_should_purge__mutmut_2'] = x_should_purge__mutmut_2 # type: ignore # mutmut generated
mutants_x_should_purge__mutmut['x_should_purge__mutmut_3'] = x_should_purge__mutmut_3 # type: ignore # mutmut generated
mutants_x_should_purge__mutmut['x_should_purge__mutmut_4'] = x_should_purge__mutmut_4 # type: ignore # mutmut generated
mutants_x_should_purge__mutmut['x_should_purge__mutmut_5'] = x_should_purge__mutmut_5 # type: ignore # mutmut generated
mutants_x_should_purge__mutmut['x_should_purge__mutmut_6'] = x_should_purge__mutmut_6 # type: ignore # mutmut generated
mutants_x_should_purge__mutmut['x_should_purge__mutmut_7'] = x_should_purge__mutmut_7 # type: ignore # mutmut generated
mutants_x_should_purge__mutmut['x_should_purge__mutmut_8'] = x_should_purge__mutmut_8 # type: ignore # mutmut generated
mutants_x_should_purge__mutmut['x_should_purge__mutmut_9'] = x_should_purge__mutmut_9 # type: ignore # mutmut generated
mutants_x_should_purge__mutmut['x_should_purge__mutmut_10'] = x_should_purge__mutmut_10 # type: ignore # mutmut generated
mutants_x_should_purge__mutmut['x_should_purge__mutmut_11'] = x_should_purge__mutmut_11 # type: ignore # mutmut generated
mutants_x_should_purge__mutmut['x_should_purge__mutmut_12'] = x_should_purge__mutmut_12 # type: ignore # mutmut generated
mutants_x_should_purge__mutmut['x_should_purge__mutmut_13'] = x_should_purge__mutmut_13 # type: ignore # mutmut generated
mutants_x_should_purge__mutmut['x_should_purge__mutmut_14'] = x_should_purge__mutmut_14 # type: ignore # mutmut generated
mutants_x_should_purge__mutmut['x_should_purge__mutmut_15'] = x_should_purge__mutmut_15 # type: ignore # mutmut generated
mutants_x_should_purge__mutmut['x_should_purge__mutmut_16'] = x_should_purge__mutmut_16 # type: ignore # mutmut generated
mutants_x_list_retention_policies__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_list_retention_policies__mutmut)
def list_retention_policies() -> list[dict[str, Any]]:
    """Lista todas las políticas de retención como dicts ordenados.

    Útil para exponer vía API /api/v2/compliance/retention-policies.
    """
    policies: list[dict[str, Any]] = []
    for (country, data_type), days in sorted(RETENTION_DAYS.items()):
        policies.append(
            {
                "country": country,
                "regulator": get_regulator_name(country),
                "data_type": data_type,
                "retention_days": days,
                "retention_years": round(days / 365, 1),
            }
        )
    return policies


def x_list_retention_policies__mutmut_orig() -> list[dict[str, Any]]:
    """Lista todas las políticas de retención como dicts ordenados.

    Útil para exponer vía API /api/v2/compliance/retention-policies.
    """
    policies: list[dict[str, Any]] = []
    for (country, data_type), days in sorted(RETENTION_DAYS.items()):
        policies.append(
            {
                "country": country,
                "regulator": get_regulator_name(country),
                "data_type": data_type,
                "retention_days": days,
                "retention_years": round(days / 365, 1),
            }
        )
    return policies


def x_list_retention_policies__mutmut_1() -> list[dict[str, Any]]:
    """Lista todas las políticas de retención como dicts ordenados.

    Útil para exponer vía API /api/v2/compliance/retention-policies.
    """
    policies: list[dict[str, Any]] = None
    for (country, data_type), days in sorted(RETENTION_DAYS.items()):
        policies.append(
            {
                "country": country,
                "regulator": get_regulator_name(country),
                "data_type": data_type,
                "retention_days": days,
                "retention_years": round(days / 365, 1),
            }
        )
    return policies


def x_list_retention_policies__mutmut_2() -> list[dict[str, Any]]:
    """Lista todas las políticas de retención como dicts ordenados.

    Útil para exponer vía API /api/v2/compliance/retention-policies.
    """
    policies: list[dict[str, Any]] = []
    for (country, data_type), days in sorted(None):
        policies.append(
            {
                "country": country,
                "regulator": get_regulator_name(country),
                "data_type": data_type,
                "retention_days": days,
                "retention_years": round(days / 365, 1),
            }
        )
    return policies


def x_list_retention_policies__mutmut_3() -> list[dict[str, Any]]:
    """Lista todas las políticas de retención como dicts ordenados.

    Útil para exponer vía API /api/v2/compliance/retention-policies.
    """
    policies: list[dict[str, Any]] = []
    for (country, data_type), days in sorted(RETENTION_DAYS.items()):
        policies.append(
            None
        )
    return policies


def x_list_retention_policies__mutmut_4() -> list[dict[str, Any]]:
    """Lista todas las políticas de retención como dicts ordenados.

    Útil para exponer vía API /api/v2/compliance/retention-policies.
    """
    policies: list[dict[str, Any]] = []
    for (country, data_type), days in sorted(RETENTION_DAYS.items()):
        policies.append(
            {
                "XXcountryXX": country,
                "regulator": get_regulator_name(country),
                "data_type": data_type,
                "retention_days": days,
                "retention_years": round(days / 365, 1),
            }
        )
    return policies


def x_list_retention_policies__mutmut_5() -> list[dict[str, Any]]:
    """Lista todas las políticas de retención como dicts ordenados.

    Útil para exponer vía API /api/v2/compliance/retention-policies.
    """
    policies: list[dict[str, Any]] = []
    for (country, data_type), days in sorted(RETENTION_DAYS.items()):
        policies.append(
            {
                "COUNTRY": country,
                "regulator": get_regulator_name(country),
                "data_type": data_type,
                "retention_days": days,
                "retention_years": round(days / 365, 1),
            }
        )
    return policies


def x_list_retention_policies__mutmut_6() -> list[dict[str, Any]]:
    """Lista todas las políticas de retención como dicts ordenados.

    Útil para exponer vía API /api/v2/compliance/retention-policies.
    """
    policies: list[dict[str, Any]] = []
    for (country, data_type), days in sorted(RETENTION_DAYS.items()):
        policies.append(
            {
                "country": country,
                "XXregulatorXX": get_regulator_name(country),
                "data_type": data_type,
                "retention_days": days,
                "retention_years": round(days / 365, 1),
            }
        )
    return policies


def x_list_retention_policies__mutmut_7() -> list[dict[str, Any]]:
    """Lista todas las políticas de retención como dicts ordenados.

    Útil para exponer vía API /api/v2/compliance/retention-policies.
    """
    policies: list[dict[str, Any]] = []
    for (country, data_type), days in sorted(RETENTION_DAYS.items()):
        policies.append(
            {
                "country": country,
                "REGULATOR": get_regulator_name(country),
                "data_type": data_type,
                "retention_days": days,
                "retention_years": round(days / 365, 1),
            }
        )
    return policies


def x_list_retention_policies__mutmut_8() -> list[dict[str, Any]]:
    """Lista todas las políticas de retención como dicts ordenados.

    Útil para exponer vía API /api/v2/compliance/retention-policies.
    """
    policies: list[dict[str, Any]] = []
    for (country, data_type), days in sorted(RETENTION_DAYS.items()):
        policies.append(
            {
                "country": country,
                "regulator": get_regulator_name(None),
                "data_type": data_type,
                "retention_days": days,
                "retention_years": round(days / 365, 1),
            }
        )
    return policies


def x_list_retention_policies__mutmut_9() -> list[dict[str, Any]]:
    """Lista todas las políticas de retención como dicts ordenados.

    Útil para exponer vía API /api/v2/compliance/retention-policies.
    """
    policies: list[dict[str, Any]] = []
    for (country, data_type), days in sorted(RETENTION_DAYS.items()):
        policies.append(
            {
                "country": country,
                "regulator": get_regulator_name(country),
                "XXdata_typeXX": data_type,
                "retention_days": days,
                "retention_years": round(days / 365, 1),
            }
        )
    return policies


def x_list_retention_policies__mutmut_10() -> list[dict[str, Any]]:
    """Lista todas las políticas de retención como dicts ordenados.

    Útil para exponer vía API /api/v2/compliance/retention-policies.
    """
    policies: list[dict[str, Any]] = []
    for (country, data_type), days in sorted(RETENTION_DAYS.items()):
        policies.append(
            {
                "country": country,
                "regulator": get_regulator_name(country),
                "DATA_TYPE": data_type,
                "retention_days": days,
                "retention_years": round(days / 365, 1),
            }
        )
    return policies


def x_list_retention_policies__mutmut_11() -> list[dict[str, Any]]:
    """Lista todas las políticas de retención como dicts ordenados.

    Útil para exponer vía API /api/v2/compliance/retention-policies.
    """
    policies: list[dict[str, Any]] = []
    for (country, data_type), days in sorted(RETENTION_DAYS.items()):
        policies.append(
            {
                "country": country,
                "regulator": get_regulator_name(country),
                "data_type": data_type,
                "XXretention_daysXX": days,
                "retention_years": round(days / 365, 1),
            }
        )
    return policies


def x_list_retention_policies__mutmut_12() -> list[dict[str, Any]]:
    """Lista todas las políticas de retención como dicts ordenados.

    Útil para exponer vía API /api/v2/compliance/retention-policies.
    """
    policies: list[dict[str, Any]] = []
    for (country, data_type), days in sorted(RETENTION_DAYS.items()):
        policies.append(
            {
                "country": country,
                "regulator": get_regulator_name(country),
                "data_type": data_type,
                "RETENTION_DAYS": days,
                "retention_years": round(days / 365, 1),
            }
        )
    return policies


def x_list_retention_policies__mutmut_13() -> list[dict[str, Any]]:
    """Lista todas las políticas de retención como dicts ordenados.

    Útil para exponer vía API /api/v2/compliance/retention-policies.
    """
    policies: list[dict[str, Any]] = []
    for (country, data_type), days in sorted(RETENTION_DAYS.items()):
        policies.append(
            {
                "country": country,
                "regulator": get_regulator_name(country),
                "data_type": data_type,
                "retention_days": days,
                "XXretention_yearsXX": round(days / 365, 1),
            }
        )
    return policies


def x_list_retention_policies__mutmut_14() -> list[dict[str, Any]]:
    """Lista todas las políticas de retención como dicts ordenados.

    Útil para exponer vía API /api/v2/compliance/retention-policies.
    """
    policies: list[dict[str, Any]] = []
    for (country, data_type), days in sorted(RETENTION_DAYS.items()):
        policies.append(
            {
                "country": country,
                "regulator": get_regulator_name(country),
                "data_type": data_type,
                "retention_days": days,
                "RETENTION_YEARS": round(days / 365, 1),
            }
        )
    return policies


def x_list_retention_policies__mutmut_15() -> list[dict[str, Any]]:
    """Lista todas las políticas de retención como dicts ordenados.

    Útil para exponer vía API /api/v2/compliance/retention-policies.
    """
    policies: list[dict[str, Any]] = []
    for (country, data_type), days in sorted(RETENTION_DAYS.items()):
        policies.append(
            {
                "country": country,
                "regulator": get_regulator_name(country),
                "data_type": data_type,
                "retention_days": days,
                "retention_years": round(None, 1),
            }
        )
    return policies


def x_list_retention_policies__mutmut_16() -> list[dict[str, Any]]:
    """Lista todas las políticas de retención como dicts ordenados.

    Útil para exponer vía API /api/v2/compliance/retention-policies.
    """
    policies: list[dict[str, Any]] = []
    for (country, data_type), days in sorted(RETENTION_DAYS.items()):
        policies.append(
            {
                "country": country,
                "regulator": get_regulator_name(country),
                "data_type": data_type,
                "retention_days": days,
                "retention_years": round(days / 365, None),
            }
        )
    return policies


def x_list_retention_policies__mutmut_17() -> list[dict[str, Any]]:
    """Lista todas las políticas de retención como dicts ordenados.

    Útil para exponer vía API /api/v2/compliance/retention-policies.
    """
    policies: list[dict[str, Any]] = []
    for (country, data_type), days in sorted(RETENTION_DAYS.items()):
        policies.append(
            {
                "country": country,
                "regulator": get_regulator_name(country),
                "data_type": data_type,
                "retention_days": days,
                "retention_years": round(1),
            }
        )
    return policies


def x_list_retention_policies__mutmut_18() -> list[dict[str, Any]]:
    """Lista todas las políticas de retención como dicts ordenados.

    Útil para exponer vía API /api/v2/compliance/retention-policies.
    """
    policies: list[dict[str, Any]] = []
    for (country, data_type), days in sorted(RETENTION_DAYS.items()):
        policies.append(
            {
                "country": country,
                "regulator": get_regulator_name(country),
                "data_type": data_type,
                "retention_days": days,
                "retention_years": round(days / 365, ),
            }
        )
    return policies


def x_list_retention_policies__mutmut_19() -> list[dict[str, Any]]:
    """Lista todas las políticas de retención como dicts ordenados.

    Útil para exponer vía API /api/v2/compliance/retention-policies.
    """
    policies: list[dict[str, Any]] = []
    for (country, data_type), days in sorted(RETENTION_DAYS.items()):
        policies.append(
            {
                "country": country,
                "regulator": get_regulator_name(country),
                "data_type": data_type,
                "retention_days": days,
                "retention_years": round(days * 365, 1),
            }
        )
    return policies


def x_list_retention_policies__mutmut_20() -> list[dict[str, Any]]:
    """Lista todas las políticas de retención como dicts ordenados.

    Útil para exponer vía API /api/v2/compliance/retention-policies.
    """
    policies: list[dict[str, Any]] = []
    for (country, data_type), days in sorted(RETENTION_DAYS.items()):
        policies.append(
            {
                "country": country,
                "regulator": get_regulator_name(country),
                "data_type": data_type,
                "retention_days": days,
                "retention_years": round(days / 366, 1),
            }
        )
    return policies


def x_list_retention_policies__mutmut_21() -> list[dict[str, Any]]:
    """Lista todas las políticas de retención como dicts ordenados.

    Útil para exponer vía API /api/v2/compliance/retention-policies.
    """
    policies: list[dict[str, Any]] = []
    for (country, data_type), days in sorted(RETENTION_DAYS.items()):
        policies.append(
            {
                "country": country,
                "regulator": get_regulator_name(country),
                "data_type": data_type,
                "retention_days": days,
                "retention_years": round(days / 365, 2),
            }
        )
    return policies

mutants_x_list_retention_policies__mutmut['_mutmut_orig'] = x_list_retention_policies__mutmut_orig # type: ignore # mutmut generated
mutants_x_list_retention_policies__mutmut['x_list_retention_policies__mutmut_1'] = x_list_retention_policies__mutmut_1 # type: ignore # mutmut generated
mutants_x_list_retention_policies__mutmut['x_list_retention_policies__mutmut_2'] = x_list_retention_policies__mutmut_2 # type: ignore # mutmut generated
mutants_x_list_retention_policies__mutmut['x_list_retention_policies__mutmut_3'] = x_list_retention_policies__mutmut_3 # type: ignore # mutmut generated
mutants_x_list_retention_policies__mutmut['x_list_retention_policies__mutmut_4'] = x_list_retention_policies__mutmut_4 # type: ignore # mutmut generated
mutants_x_list_retention_policies__mutmut['x_list_retention_policies__mutmut_5'] = x_list_retention_policies__mutmut_5 # type: ignore # mutmut generated
mutants_x_list_retention_policies__mutmut['x_list_retention_policies__mutmut_6'] = x_list_retention_policies__mutmut_6 # type: ignore # mutmut generated
mutants_x_list_retention_policies__mutmut['x_list_retention_policies__mutmut_7'] = x_list_retention_policies__mutmut_7 # type: ignore # mutmut generated
mutants_x_list_retention_policies__mutmut['x_list_retention_policies__mutmut_8'] = x_list_retention_policies__mutmut_8 # type: ignore # mutmut generated
mutants_x_list_retention_policies__mutmut['x_list_retention_policies__mutmut_9'] = x_list_retention_policies__mutmut_9 # type: ignore # mutmut generated
mutants_x_list_retention_policies__mutmut['x_list_retention_policies__mutmut_10'] = x_list_retention_policies__mutmut_10 # type: ignore # mutmut generated
mutants_x_list_retention_policies__mutmut['x_list_retention_policies__mutmut_11'] = x_list_retention_policies__mutmut_11 # type: ignore # mutmut generated
mutants_x_list_retention_policies__mutmut['x_list_retention_policies__mutmut_12'] = x_list_retention_policies__mutmut_12 # type: ignore # mutmut generated
mutants_x_list_retention_policies__mutmut['x_list_retention_policies__mutmut_13'] = x_list_retention_policies__mutmut_13 # type: ignore # mutmut generated
mutants_x_list_retention_policies__mutmut['x_list_retention_policies__mutmut_14'] = x_list_retention_policies__mutmut_14 # type: ignore # mutmut generated
mutants_x_list_retention_policies__mutmut['x_list_retention_policies__mutmut_15'] = x_list_retention_policies__mutmut_15 # type: ignore # mutmut generated
mutants_x_list_retention_policies__mutmut['x_list_retention_policies__mutmut_16'] = x_list_retention_policies__mutmut_16 # type: ignore # mutmut generated
mutants_x_list_retention_policies__mutmut['x_list_retention_policies__mutmut_17'] = x_list_retention_policies__mutmut_17 # type: ignore # mutmut generated
mutants_x_list_retention_policies__mutmut['x_list_retention_policies__mutmut_18'] = x_list_retention_policies__mutmut_18 # type: ignore # mutmut generated
mutants_x_list_retention_policies__mutmut['x_list_retention_policies__mutmut_19'] = x_list_retention_policies__mutmut_19 # type: ignore # mutmut generated
mutants_x_list_retention_policies__mutmut['x_list_retention_policies__mutmut_20'] = x_list_retention_policies__mutmut_20 # type: ignore # mutmut generated
mutants_x_list_retention_policies__mutmut['x_list_retention_policies__mutmut_21'] = x_list_retention_policies__mutmut_21 # type: ignore # mutmut generated
