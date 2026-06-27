"""
Zenic-Flijo API v2 — Dependencias FastAPI Compartidas
======================================================

Dependencias reutilizables por todos los routers de la API v2:
- get_db: Sesion de base de datos (DatabaseManager)
- get_redis: Servicio de Redis (RedisService)
- get_workflow_engine: Motor de workflows (WorkflowEngine)
- get_nlu_pipeline: Pipeline NLU (Pipeline)
- get_connector_registry: Registro de conectores (ConnectorRegistry)
- get_tenant_service: Servicio de tenants (TenantService)
- get_pagination: Parametros de paginacion desde query params
- verify_tenant_ownership: Verifica que un usuario pertenece a un tenant
- require_tenant_access: Dependency que valida X-Tenant-ID contra user_tenants

Todas las dependencias usan singletons existentes del proyecto.
"""

from __future__ import annotations

from typing import Any

from fastapi import Depends, HTTPException, Query, Request, status

from src.api_v2.models import PaginationParams


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


async def get_db() -> Any:
    """Obtiene la instancia singleton de DatabaseManager.

    Returns:
        DatabaseManager: Instancia de la base de datos SQLite
    """
    from src.core.db import DatabaseManager

    return DatabaseManager()


async def get_redis() -> Any:
    """Obtiene la instancia singleton de RedisService.

    Returns:
        RedisService: Instancia del servicio de Redis
    """
    from src.core.db import RedisService

    return RedisService()


async def get_workflow_engine() -> Any:
    """Obtiene la instancia singleton de WorkflowEngine.

    Returns:
        WorkflowEngine: Instancia del motor de workflows
    """
    from src.workflow.engine import WorkflowEngine

    return WorkflowEngine()


async def get_workflow_repository() -> Any:
    """Obtiene una nueva instancia de WorkflowRepository.

    Returns:
        WorkflowRepository: Instancia del repositorio de workflows
    """
    from src.workflow.repository import WorkflowRepository

    return WorkflowRepository()


async def get_nlu_pipeline() -> Any:
    """Obtiene una nueva instancia del Pipeline NLU.

    Returns:
        Pipeline: Instancia del pipeline de procesamiento de lenguaje natural
    """
    from src.nlu.pipeline import Pipeline

    return Pipeline()


async def get_connector_registry() -> Any:
    """Obtiene la instancia singleton de ConnectorRegistry.

    Returns:
        ConnectorRegistry: Instancia del registro de conectores
    """
    from src.sdk.registry import ConnectorRegistry

    return ConnectorRegistry()


async def get_tenant_service() -> Any:
    """Obtiene la instancia singleton de TenantService.

    Returns:
        TenantService: Instancia del servicio de multi-tenancy
    """
    from src.tenant.service import TenantService

    return TenantService()


async def get_rbac_manager() -> Any:
    """Obtiene la instancia singleton de RBACManager.

    Returns:
        RBACManager: Instancia del gestor de RBAC granular
    """
    from src.core.security.rbac import RBACManager

    return RBACManager()


async def get_telemetry_service() -> Any:
    """Obtiene la instancia singleton de TelemetryService.

    Returns:
        TelemetryService: Instancia del servicio de telemetria
    """
    from src.core.observability.telemetry import TelemetryService

    return TelemetryService()
mutants_x_get_pagination__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_pagination__mutmut)
def get_pagination(
    page: int = Query(default=1, ge=1, description="Numero de pagina"),
    page_size: int = Query(default=20, ge=1, le=100, description="Elementos por pagina"),
) -> PaginationParams:
    """Extrae parametros de paginacion desde query params.

    Args:
        page: Numero de pagina (default: 1)
        page_size: Elementos por pagina (default: 20, max: 100)

    Returns:
        PaginationParams: Parametros de paginacion validados
    """
    return PaginationParams(page=page, page_size=page_size)


def x_get_pagination__mutmut_orig(
    page: int = Query(default=1, ge=1, description="Numero de pagina"),
    page_size: int = Query(default=20, ge=1, le=100, description="Elementos por pagina"),
) -> PaginationParams:
    """Extrae parametros de paginacion desde query params.

    Args:
        page: Numero de pagina (default: 1)
        page_size: Elementos por pagina (default: 20, max: 100)

    Returns:
        PaginationParams: Parametros de paginacion validados
    """
    return PaginationParams(page=page, page_size=page_size)


def x_get_pagination__mutmut_1(
    page: int = Query(default=1, ge=1, description="Numero de pagina"),
    page_size: int = Query(default=20, ge=1, le=100, description="Elementos por pagina"),
) -> PaginationParams:
    """Extrae parametros de paginacion desde query params.

    Args:
        page: Numero de pagina (default: 1)
        page_size: Elementos por pagina (default: 20, max: 100)

    Returns:
        PaginationParams: Parametros de paginacion validados
    """
    return PaginationParams(page=None, page_size=page_size)


def x_get_pagination__mutmut_2(
    page: int = Query(default=1, ge=1, description="Numero de pagina"),
    page_size: int = Query(default=20, ge=1, le=100, description="Elementos por pagina"),
) -> PaginationParams:
    """Extrae parametros de paginacion desde query params.

    Args:
        page: Numero de pagina (default: 1)
        page_size: Elementos por pagina (default: 20, max: 100)

    Returns:
        PaginationParams: Parametros de paginacion validados
    """
    return PaginationParams(page=page, page_size=None)


def x_get_pagination__mutmut_3(
    page: int = Query(default=1, ge=1, description="Numero de pagina"),
    page_size: int = Query(default=20, ge=1, le=100, description="Elementos por pagina"),
) -> PaginationParams:
    """Extrae parametros de paginacion desde query params.

    Args:
        page: Numero de pagina (default: 1)
        page_size: Elementos por pagina (default: 20, max: 100)

    Returns:
        PaginationParams: Parametros de paginacion validados
    """
    return PaginationParams(page_size=page_size)


def x_get_pagination__mutmut_4(
    page: int = Query(default=1, ge=1, description="Numero de pagina"),
    page_size: int = Query(default=20, ge=1, le=100, description="Elementos por pagina"),
) -> PaginationParams:
    """Extrae parametros de paginacion desde query params.

    Args:
        page: Numero de pagina (default: 1)
        page_size: Elementos por pagina (default: 20, max: 100)

    Returns:
        PaginationParams: Parametros de paginacion validados
    """
    return PaginationParams(page=page, )

mutants_x_get_pagination__mutmut['_mutmut_orig'] = x_get_pagination__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_pagination__mutmut['x_get_pagination__mutmut_1'] = x_get_pagination__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_pagination__mutmut['x_get_pagination__mutmut_2'] = x_get_pagination__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_pagination__mutmut['x_get_pagination__mutmut_3'] = x_get_pagination__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_pagination__mutmut['x_get_pagination__mutmut_4'] = x_get_pagination__mutmut_4 # type: ignore # mutmut generated
mutants_x_verify_tenant_ownership__mutmut: MutantDict = {}  # type: ignore


# ─── Bug TENANT-03: X-Tenant-ID bypass ─────────────────────────────────
# Cualquier usuario autenticado podia pasar X-Tenant-ID: <otro_tenant>
# en el header y acceder a datos ajenos sin verificacion de ownership.
# verify_tenant_ownership() valida contra la tabla user_tenants que el
# usuario pertenece al tenant solicitado. require_tenant_access() es la
# dependencia FastAPI que se usa en routers que acepten X-Tenant-ID.


@_mutmut_mutated(mutants_x_verify_tenant_ownership__mutmut)
def verify_tenant_ownership(user: dict[str, Any], tenant_id: str) -> bool:
    """Verifica que el usuario pertenece al tenant solicitado.

    Fuente de verdad: tabla ``user_tenants`` en SQLite (clave compuesta
    ``(user_id, tenant_id)``). Si el usuario no tiene asignado el tenant,
    retorna False y el caller debe denegar el acceso con 403.

    Args:
        user: Dict con al menos ``user_id`` (devuelto por get_current_user).
        tenant_id: ID del tenant que se quiere acceder (del header X-Tenant-ID).

    Returns:
        True si el usuario pertenece al tenant, False en caso contrario.
    """
    if not tenant_id:
        return False

    user_id = user.get("user_id") if isinstance(user, dict) else None
    if not user_id:
        return False

    # Lazy import para romper circular: sqlite_manager <-> repositorios.
    from src.core.db import DatabaseManager

    db = DatabaseManager()
    row = db.fetchone(
        "SELECT 1 AS ok FROM user_tenants WHERE user_id = ? AND tenant_id = ? LIMIT 1",
        (user_id, tenant_id),
    )
    return bool(row)


# ─── Bug TENANT-03: X-Tenant-ID bypass ─────────────────────────────────
# Cualquier usuario autenticado podia pasar X-Tenant-ID: <otro_tenant>
# en el header y acceder a datos ajenos sin verificacion de ownership.
# verify_tenant_ownership() valida contra la tabla user_tenants que el
# usuario pertenece al tenant solicitado. require_tenant_access() es la
# dependencia FastAPI que se usa en routers que acepten X-Tenant-ID.


def x_verify_tenant_ownership__mutmut_orig(user: dict[str, Any], tenant_id: str) -> bool:
    """Verifica que el usuario pertenece al tenant solicitado.

    Fuente de verdad: tabla ``user_tenants`` en SQLite (clave compuesta
    ``(user_id, tenant_id)``). Si el usuario no tiene asignado el tenant,
    retorna False y el caller debe denegar el acceso con 403.

    Args:
        user: Dict con al menos ``user_id`` (devuelto por get_current_user).
        tenant_id: ID del tenant que se quiere acceder (del header X-Tenant-ID).

    Returns:
        True si el usuario pertenece al tenant, False en caso contrario.
    """
    if not tenant_id:
        return False

    user_id = user.get("user_id") if isinstance(user, dict) else None
    if not user_id:
        return False

    # Lazy import para romper circular: sqlite_manager <-> repositorios.
    from src.core.db import DatabaseManager

    db = DatabaseManager()
    row = db.fetchone(
        "SELECT 1 AS ok FROM user_tenants WHERE user_id = ? AND tenant_id = ? LIMIT 1",
        (user_id, tenant_id),
    )
    return bool(row)


# ─── Bug TENANT-03: X-Tenant-ID bypass ─────────────────────────────────
# Cualquier usuario autenticado podia pasar X-Tenant-ID: <otro_tenant>
# en el header y acceder a datos ajenos sin verificacion de ownership.
# verify_tenant_ownership() valida contra la tabla user_tenants que el
# usuario pertenece al tenant solicitado. require_tenant_access() es la
# dependencia FastAPI que se usa en routers que acepten X-Tenant-ID.


def x_verify_tenant_ownership__mutmut_1(user: dict[str, Any], tenant_id: str) -> bool:
    """Verifica que el usuario pertenece al tenant solicitado.

    Fuente de verdad: tabla ``user_tenants`` en SQLite (clave compuesta
    ``(user_id, tenant_id)``). Si el usuario no tiene asignado el tenant,
    retorna False y el caller debe denegar el acceso con 403.

    Args:
        user: Dict con al menos ``user_id`` (devuelto por get_current_user).
        tenant_id: ID del tenant que se quiere acceder (del header X-Tenant-ID).

    Returns:
        True si el usuario pertenece al tenant, False en caso contrario.
    """
    if tenant_id:
        return False

    user_id = user.get("user_id") if isinstance(user, dict) else None
    if not user_id:
        return False

    # Lazy import para romper circular: sqlite_manager <-> repositorios.
    from src.core.db import DatabaseManager

    db = DatabaseManager()
    row = db.fetchone(
        "SELECT 1 AS ok FROM user_tenants WHERE user_id = ? AND tenant_id = ? LIMIT 1",
        (user_id, tenant_id),
    )
    return bool(row)


# ─── Bug TENANT-03: X-Tenant-ID bypass ─────────────────────────────────
# Cualquier usuario autenticado podia pasar X-Tenant-ID: <otro_tenant>
# en el header y acceder a datos ajenos sin verificacion de ownership.
# verify_tenant_ownership() valida contra la tabla user_tenants que el
# usuario pertenece al tenant solicitado. require_tenant_access() es la
# dependencia FastAPI que se usa en routers que acepten X-Tenant-ID.


def x_verify_tenant_ownership__mutmut_2(user: dict[str, Any], tenant_id: str) -> bool:
    """Verifica que el usuario pertenece al tenant solicitado.

    Fuente de verdad: tabla ``user_tenants`` en SQLite (clave compuesta
    ``(user_id, tenant_id)``). Si el usuario no tiene asignado el tenant,
    retorna False y el caller debe denegar el acceso con 403.

    Args:
        user: Dict con al menos ``user_id`` (devuelto por get_current_user).
        tenant_id: ID del tenant que se quiere acceder (del header X-Tenant-ID).

    Returns:
        True si el usuario pertenece al tenant, False en caso contrario.
    """
    if not tenant_id:
        return True

    user_id = user.get("user_id") if isinstance(user, dict) else None
    if not user_id:
        return False

    # Lazy import para romper circular: sqlite_manager <-> repositorios.
    from src.core.db import DatabaseManager

    db = DatabaseManager()
    row = db.fetchone(
        "SELECT 1 AS ok FROM user_tenants WHERE user_id = ? AND tenant_id = ? LIMIT 1",
        (user_id, tenant_id),
    )
    return bool(row)


# ─── Bug TENANT-03: X-Tenant-ID bypass ─────────────────────────────────
# Cualquier usuario autenticado podia pasar X-Tenant-ID: <otro_tenant>
# en el header y acceder a datos ajenos sin verificacion de ownership.
# verify_tenant_ownership() valida contra la tabla user_tenants que el
# usuario pertenece al tenant solicitado. require_tenant_access() es la
# dependencia FastAPI que se usa en routers que acepten X-Tenant-ID.


def x_verify_tenant_ownership__mutmut_3(user: dict[str, Any], tenant_id: str) -> bool:
    """Verifica que el usuario pertenece al tenant solicitado.

    Fuente de verdad: tabla ``user_tenants`` en SQLite (clave compuesta
    ``(user_id, tenant_id)``). Si el usuario no tiene asignado el tenant,
    retorna False y el caller debe denegar el acceso con 403.

    Args:
        user: Dict con al menos ``user_id`` (devuelto por get_current_user).
        tenant_id: ID del tenant que se quiere acceder (del header X-Tenant-ID).

    Returns:
        True si el usuario pertenece al tenant, False en caso contrario.
    """
    if not tenant_id:
        return False

    user_id = None
    if not user_id:
        return False

    # Lazy import para romper circular: sqlite_manager <-> repositorios.
    from src.core.db import DatabaseManager

    db = DatabaseManager()
    row = db.fetchone(
        "SELECT 1 AS ok FROM user_tenants WHERE user_id = ? AND tenant_id = ? LIMIT 1",
        (user_id, tenant_id),
    )
    return bool(row)


# ─── Bug TENANT-03: X-Tenant-ID bypass ─────────────────────────────────
# Cualquier usuario autenticado podia pasar X-Tenant-ID: <otro_tenant>
# en el header y acceder a datos ajenos sin verificacion de ownership.
# verify_tenant_ownership() valida contra la tabla user_tenants que el
# usuario pertenece al tenant solicitado. require_tenant_access() es la
# dependencia FastAPI que se usa en routers que acepten X-Tenant-ID.


def x_verify_tenant_ownership__mutmut_4(user: dict[str, Any], tenant_id: str) -> bool:
    """Verifica que el usuario pertenece al tenant solicitado.

    Fuente de verdad: tabla ``user_tenants`` en SQLite (clave compuesta
    ``(user_id, tenant_id)``). Si el usuario no tiene asignado el tenant,
    retorna False y el caller debe denegar el acceso con 403.

    Args:
        user: Dict con al menos ``user_id`` (devuelto por get_current_user).
        tenant_id: ID del tenant que se quiere acceder (del header X-Tenant-ID).

    Returns:
        True si el usuario pertenece al tenant, False en caso contrario.
    """
    if not tenant_id:
        return False

    user_id = user.get(None) if isinstance(user, dict) else None
    if not user_id:
        return False

    # Lazy import para romper circular: sqlite_manager <-> repositorios.
    from src.core.db import DatabaseManager

    db = DatabaseManager()
    row = db.fetchone(
        "SELECT 1 AS ok FROM user_tenants WHERE user_id = ? AND tenant_id = ? LIMIT 1",
        (user_id, tenant_id),
    )
    return bool(row)


# ─── Bug TENANT-03: X-Tenant-ID bypass ─────────────────────────────────
# Cualquier usuario autenticado podia pasar X-Tenant-ID: <otro_tenant>
# en el header y acceder a datos ajenos sin verificacion de ownership.
# verify_tenant_ownership() valida contra la tabla user_tenants que el
# usuario pertenece al tenant solicitado. require_tenant_access() es la
# dependencia FastAPI que se usa en routers que acepten X-Tenant-ID.


def x_verify_tenant_ownership__mutmut_5(user: dict[str, Any], tenant_id: str) -> bool:
    """Verifica que el usuario pertenece al tenant solicitado.

    Fuente de verdad: tabla ``user_tenants`` en SQLite (clave compuesta
    ``(user_id, tenant_id)``). Si el usuario no tiene asignado el tenant,
    retorna False y el caller debe denegar el acceso con 403.

    Args:
        user: Dict con al menos ``user_id`` (devuelto por get_current_user).
        tenant_id: ID del tenant que se quiere acceder (del header X-Tenant-ID).

    Returns:
        True si el usuario pertenece al tenant, False en caso contrario.
    """
    if not tenant_id:
        return False

    user_id = user.get("XXuser_idXX") if isinstance(user, dict) else None
    if not user_id:
        return False

    # Lazy import para romper circular: sqlite_manager <-> repositorios.
    from src.core.db import DatabaseManager

    db = DatabaseManager()
    row = db.fetchone(
        "SELECT 1 AS ok FROM user_tenants WHERE user_id = ? AND tenant_id = ? LIMIT 1",
        (user_id, tenant_id),
    )
    return bool(row)


# ─── Bug TENANT-03: X-Tenant-ID bypass ─────────────────────────────────
# Cualquier usuario autenticado podia pasar X-Tenant-ID: <otro_tenant>
# en el header y acceder a datos ajenos sin verificacion de ownership.
# verify_tenant_ownership() valida contra la tabla user_tenants que el
# usuario pertenece al tenant solicitado. require_tenant_access() es la
# dependencia FastAPI que se usa en routers que acepten X-Tenant-ID.


def x_verify_tenant_ownership__mutmut_6(user: dict[str, Any], tenant_id: str) -> bool:
    """Verifica que el usuario pertenece al tenant solicitado.

    Fuente de verdad: tabla ``user_tenants`` en SQLite (clave compuesta
    ``(user_id, tenant_id)``). Si el usuario no tiene asignado el tenant,
    retorna False y el caller debe denegar el acceso con 403.

    Args:
        user: Dict con al menos ``user_id`` (devuelto por get_current_user).
        tenant_id: ID del tenant que se quiere acceder (del header X-Tenant-ID).

    Returns:
        True si el usuario pertenece al tenant, False en caso contrario.
    """
    if not tenant_id:
        return False

    user_id = user.get("USER_ID") if isinstance(user, dict) else None
    if not user_id:
        return False

    # Lazy import para romper circular: sqlite_manager <-> repositorios.
    from src.core.db import DatabaseManager

    db = DatabaseManager()
    row = db.fetchone(
        "SELECT 1 AS ok FROM user_tenants WHERE user_id = ? AND tenant_id = ? LIMIT 1",
        (user_id, tenant_id),
    )
    return bool(row)


# ─── Bug TENANT-03: X-Tenant-ID bypass ─────────────────────────────────
# Cualquier usuario autenticado podia pasar X-Tenant-ID: <otro_tenant>
# en el header y acceder a datos ajenos sin verificacion de ownership.
# verify_tenant_ownership() valida contra la tabla user_tenants que el
# usuario pertenece al tenant solicitado. require_tenant_access() es la
# dependencia FastAPI que se usa en routers que acepten X-Tenant-ID.


def x_verify_tenant_ownership__mutmut_7(user: dict[str, Any], tenant_id: str) -> bool:
    """Verifica que el usuario pertenece al tenant solicitado.

    Fuente de verdad: tabla ``user_tenants`` en SQLite (clave compuesta
    ``(user_id, tenant_id)``). Si el usuario no tiene asignado el tenant,
    retorna False y el caller debe denegar el acceso con 403.

    Args:
        user: Dict con al menos ``user_id`` (devuelto por get_current_user).
        tenant_id: ID del tenant que se quiere acceder (del header X-Tenant-ID).

    Returns:
        True si el usuario pertenece al tenant, False en caso contrario.
    """
    if not tenant_id:
        return False

    user_id = user.get("user_id") if isinstance(user, dict) else None
    if user_id:
        return False

    # Lazy import para romper circular: sqlite_manager <-> repositorios.
    from src.core.db import DatabaseManager

    db = DatabaseManager()
    row = db.fetchone(
        "SELECT 1 AS ok FROM user_tenants WHERE user_id = ? AND tenant_id = ? LIMIT 1",
        (user_id, tenant_id),
    )
    return bool(row)


# ─── Bug TENANT-03: X-Tenant-ID bypass ─────────────────────────────────
# Cualquier usuario autenticado podia pasar X-Tenant-ID: <otro_tenant>
# en el header y acceder a datos ajenos sin verificacion de ownership.
# verify_tenant_ownership() valida contra la tabla user_tenants que el
# usuario pertenece al tenant solicitado. require_tenant_access() es la
# dependencia FastAPI que se usa en routers que acepten X-Tenant-ID.


def x_verify_tenant_ownership__mutmut_8(user: dict[str, Any], tenant_id: str) -> bool:
    """Verifica que el usuario pertenece al tenant solicitado.

    Fuente de verdad: tabla ``user_tenants`` en SQLite (clave compuesta
    ``(user_id, tenant_id)``). Si el usuario no tiene asignado el tenant,
    retorna False y el caller debe denegar el acceso con 403.

    Args:
        user: Dict con al menos ``user_id`` (devuelto por get_current_user).
        tenant_id: ID del tenant que se quiere acceder (del header X-Tenant-ID).

    Returns:
        True si el usuario pertenece al tenant, False en caso contrario.
    """
    if not tenant_id:
        return False

    user_id = user.get("user_id") if isinstance(user, dict) else None
    if not user_id:
        return True

    # Lazy import para romper circular: sqlite_manager <-> repositorios.
    from src.core.db import DatabaseManager

    db = DatabaseManager()
    row = db.fetchone(
        "SELECT 1 AS ok FROM user_tenants WHERE user_id = ? AND tenant_id = ? LIMIT 1",
        (user_id, tenant_id),
    )
    return bool(row)


# ─── Bug TENANT-03: X-Tenant-ID bypass ─────────────────────────────────
# Cualquier usuario autenticado podia pasar X-Tenant-ID: <otro_tenant>
# en el header y acceder a datos ajenos sin verificacion de ownership.
# verify_tenant_ownership() valida contra la tabla user_tenants que el
# usuario pertenece al tenant solicitado. require_tenant_access() es la
# dependencia FastAPI que se usa en routers que acepten X-Tenant-ID.


def x_verify_tenant_ownership__mutmut_9(user: dict[str, Any], tenant_id: str) -> bool:
    """Verifica que el usuario pertenece al tenant solicitado.

    Fuente de verdad: tabla ``user_tenants`` en SQLite (clave compuesta
    ``(user_id, tenant_id)``). Si el usuario no tiene asignado el tenant,
    retorna False y el caller debe denegar el acceso con 403.

    Args:
        user: Dict con al menos ``user_id`` (devuelto por get_current_user).
        tenant_id: ID del tenant que se quiere acceder (del header X-Tenant-ID).

    Returns:
        True si el usuario pertenece al tenant, False en caso contrario.
    """
    if not tenant_id:
        return False

    user_id = user.get("user_id") if isinstance(user, dict) else None
    if not user_id:
        return False

    # Lazy import para romper circular: sqlite_manager <-> repositorios.
    from src.core.db import DatabaseManager

    db = None
    row = db.fetchone(
        "SELECT 1 AS ok FROM user_tenants WHERE user_id = ? AND tenant_id = ? LIMIT 1",
        (user_id, tenant_id),
    )
    return bool(row)


# ─── Bug TENANT-03: X-Tenant-ID bypass ─────────────────────────────────
# Cualquier usuario autenticado podia pasar X-Tenant-ID: <otro_tenant>
# en el header y acceder a datos ajenos sin verificacion de ownership.
# verify_tenant_ownership() valida contra la tabla user_tenants que el
# usuario pertenece al tenant solicitado. require_tenant_access() es la
# dependencia FastAPI que se usa en routers que acepten X-Tenant-ID.


def x_verify_tenant_ownership__mutmut_10(user: dict[str, Any], tenant_id: str) -> bool:
    """Verifica que el usuario pertenece al tenant solicitado.

    Fuente de verdad: tabla ``user_tenants`` en SQLite (clave compuesta
    ``(user_id, tenant_id)``). Si el usuario no tiene asignado el tenant,
    retorna False y el caller debe denegar el acceso con 403.

    Args:
        user: Dict con al menos ``user_id`` (devuelto por get_current_user).
        tenant_id: ID del tenant que se quiere acceder (del header X-Tenant-ID).

    Returns:
        True si el usuario pertenece al tenant, False en caso contrario.
    """
    if not tenant_id:
        return False

    user_id = user.get("user_id") if isinstance(user, dict) else None
    if not user_id:
        return False

    # Lazy import para romper circular: sqlite_manager <-> repositorios.
    from src.core.db import DatabaseManager

    db = DatabaseManager()
    row = None
    return bool(row)


# ─── Bug TENANT-03: X-Tenant-ID bypass ─────────────────────────────────
# Cualquier usuario autenticado podia pasar X-Tenant-ID: <otro_tenant>
# en el header y acceder a datos ajenos sin verificacion de ownership.
# verify_tenant_ownership() valida contra la tabla user_tenants que el
# usuario pertenece al tenant solicitado. require_tenant_access() es la
# dependencia FastAPI que se usa en routers que acepten X-Tenant-ID.


def x_verify_tenant_ownership__mutmut_11(user: dict[str, Any], tenant_id: str) -> bool:
    """Verifica que el usuario pertenece al tenant solicitado.

    Fuente de verdad: tabla ``user_tenants`` en SQLite (clave compuesta
    ``(user_id, tenant_id)``). Si el usuario no tiene asignado el tenant,
    retorna False y el caller debe denegar el acceso con 403.

    Args:
        user: Dict con al menos ``user_id`` (devuelto por get_current_user).
        tenant_id: ID del tenant que se quiere acceder (del header X-Tenant-ID).

    Returns:
        True si el usuario pertenece al tenant, False en caso contrario.
    """
    if not tenant_id:
        return False

    user_id = user.get("user_id") if isinstance(user, dict) else None
    if not user_id:
        return False

    # Lazy import para romper circular: sqlite_manager <-> repositorios.
    from src.core.db import DatabaseManager

    db = DatabaseManager()
    row = db.fetchone(
        None,
        (user_id, tenant_id),
    )
    return bool(row)


# ─── Bug TENANT-03: X-Tenant-ID bypass ─────────────────────────────────
# Cualquier usuario autenticado podia pasar X-Tenant-ID: <otro_tenant>
# en el header y acceder a datos ajenos sin verificacion de ownership.
# verify_tenant_ownership() valida contra la tabla user_tenants que el
# usuario pertenece al tenant solicitado. require_tenant_access() es la
# dependencia FastAPI que se usa en routers que acepten X-Tenant-ID.


def x_verify_tenant_ownership__mutmut_12(user: dict[str, Any], tenant_id: str) -> bool:
    """Verifica que el usuario pertenece al tenant solicitado.

    Fuente de verdad: tabla ``user_tenants`` en SQLite (clave compuesta
    ``(user_id, tenant_id)``). Si el usuario no tiene asignado el tenant,
    retorna False y el caller debe denegar el acceso con 403.

    Args:
        user: Dict con al menos ``user_id`` (devuelto por get_current_user).
        tenant_id: ID del tenant que se quiere acceder (del header X-Tenant-ID).

    Returns:
        True si el usuario pertenece al tenant, False en caso contrario.
    """
    if not tenant_id:
        return False

    user_id = user.get("user_id") if isinstance(user, dict) else None
    if not user_id:
        return False

    # Lazy import para romper circular: sqlite_manager <-> repositorios.
    from src.core.db import DatabaseManager

    db = DatabaseManager()
    row = db.fetchone(
        "SELECT 1 AS ok FROM user_tenants WHERE user_id = ? AND tenant_id = ? LIMIT 1",
        None,
    )
    return bool(row)


# ─── Bug TENANT-03: X-Tenant-ID bypass ─────────────────────────────────
# Cualquier usuario autenticado podia pasar X-Tenant-ID: <otro_tenant>
# en el header y acceder a datos ajenos sin verificacion de ownership.
# verify_tenant_ownership() valida contra la tabla user_tenants que el
# usuario pertenece al tenant solicitado. require_tenant_access() es la
# dependencia FastAPI que se usa en routers que acepten X-Tenant-ID.


def x_verify_tenant_ownership__mutmut_13(user: dict[str, Any], tenant_id: str) -> bool:
    """Verifica que el usuario pertenece al tenant solicitado.

    Fuente de verdad: tabla ``user_tenants`` en SQLite (clave compuesta
    ``(user_id, tenant_id)``). Si el usuario no tiene asignado el tenant,
    retorna False y el caller debe denegar el acceso con 403.

    Args:
        user: Dict con al menos ``user_id`` (devuelto por get_current_user).
        tenant_id: ID del tenant que se quiere acceder (del header X-Tenant-ID).

    Returns:
        True si el usuario pertenece al tenant, False en caso contrario.
    """
    if not tenant_id:
        return False

    user_id = user.get("user_id") if isinstance(user, dict) else None
    if not user_id:
        return False

    # Lazy import para romper circular: sqlite_manager <-> repositorios.
    from src.core.db import DatabaseManager

    db = DatabaseManager()
    row = db.fetchone(
        (user_id, tenant_id),
    )
    return bool(row)


# ─── Bug TENANT-03: X-Tenant-ID bypass ─────────────────────────────────
# Cualquier usuario autenticado podia pasar X-Tenant-ID: <otro_tenant>
# en el header y acceder a datos ajenos sin verificacion de ownership.
# verify_tenant_ownership() valida contra la tabla user_tenants que el
# usuario pertenece al tenant solicitado. require_tenant_access() es la
# dependencia FastAPI que se usa en routers que acepten X-Tenant-ID.


def x_verify_tenant_ownership__mutmut_14(user: dict[str, Any], tenant_id: str) -> bool:
    """Verifica que el usuario pertenece al tenant solicitado.

    Fuente de verdad: tabla ``user_tenants`` en SQLite (clave compuesta
    ``(user_id, tenant_id)``). Si el usuario no tiene asignado el tenant,
    retorna False y el caller debe denegar el acceso con 403.

    Args:
        user: Dict con al menos ``user_id`` (devuelto por get_current_user).
        tenant_id: ID del tenant que se quiere acceder (del header X-Tenant-ID).

    Returns:
        True si el usuario pertenece al tenant, False en caso contrario.
    """
    if not tenant_id:
        return False

    user_id = user.get("user_id") if isinstance(user, dict) else None
    if not user_id:
        return False

    # Lazy import para romper circular: sqlite_manager <-> repositorios.
    from src.core.db import DatabaseManager

    db = DatabaseManager()
    row = db.fetchone(
        "SELECT 1 AS ok FROM user_tenants WHERE user_id = ? AND tenant_id = ? LIMIT 1",
        )
    return bool(row)


# ─── Bug TENANT-03: X-Tenant-ID bypass ─────────────────────────────────
# Cualquier usuario autenticado podia pasar X-Tenant-ID: <otro_tenant>
# en el header y acceder a datos ajenos sin verificacion de ownership.
# verify_tenant_ownership() valida contra la tabla user_tenants que el
# usuario pertenece al tenant solicitado. require_tenant_access() es la
# dependencia FastAPI que se usa en routers que acepten X-Tenant-ID.


def x_verify_tenant_ownership__mutmut_15(user: dict[str, Any], tenant_id: str) -> bool:
    """Verifica que el usuario pertenece al tenant solicitado.

    Fuente de verdad: tabla ``user_tenants`` en SQLite (clave compuesta
    ``(user_id, tenant_id)``). Si el usuario no tiene asignado el tenant,
    retorna False y el caller debe denegar el acceso con 403.

    Args:
        user: Dict con al menos ``user_id`` (devuelto por get_current_user).
        tenant_id: ID del tenant que se quiere acceder (del header X-Tenant-ID).

    Returns:
        True si el usuario pertenece al tenant, False en caso contrario.
    """
    if not tenant_id:
        return False

    user_id = user.get("user_id") if isinstance(user, dict) else None
    if not user_id:
        return False

    # Lazy import para romper circular: sqlite_manager <-> repositorios.
    from src.core.db import DatabaseManager

    db = DatabaseManager()
    row = db.fetchone(
        "XXSELECT 1 AS ok FROM user_tenants WHERE user_id = ? AND tenant_id = ? LIMIT 1XX",
        (user_id, tenant_id),
    )
    return bool(row)


# ─── Bug TENANT-03: X-Tenant-ID bypass ─────────────────────────────────
# Cualquier usuario autenticado podia pasar X-Tenant-ID: <otro_tenant>
# en el header y acceder a datos ajenos sin verificacion de ownership.
# verify_tenant_ownership() valida contra la tabla user_tenants que el
# usuario pertenece al tenant solicitado. require_tenant_access() es la
# dependencia FastAPI que se usa en routers que acepten X-Tenant-ID.


def x_verify_tenant_ownership__mutmut_16(user: dict[str, Any], tenant_id: str) -> bool:
    """Verifica que el usuario pertenece al tenant solicitado.

    Fuente de verdad: tabla ``user_tenants`` en SQLite (clave compuesta
    ``(user_id, tenant_id)``). Si el usuario no tiene asignado el tenant,
    retorna False y el caller debe denegar el acceso con 403.

    Args:
        user: Dict con al menos ``user_id`` (devuelto por get_current_user).
        tenant_id: ID del tenant que se quiere acceder (del header X-Tenant-ID).

    Returns:
        True si el usuario pertenece al tenant, False en caso contrario.
    """
    if not tenant_id:
        return False

    user_id = user.get("user_id") if isinstance(user, dict) else None
    if not user_id:
        return False

    # Lazy import para romper circular: sqlite_manager <-> repositorios.
    from src.core.db import DatabaseManager

    db = DatabaseManager()
    row = db.fetchone(
        "select 1 as ok from user_tenants where user_id = ? and tenant_id = ? limit 1",
        (user_id, tenant_id),
    )
    return bool(row)


# ─── Bug TENANT-03: X-Tenant-ID bypass ─────────────────────────────────
# Cualquier usuario autenticado podia pasar X-Tenant-ID: <otro_tenant>
# en el header y acceder a datos ajenos sin verificacion de ownership.
# verify_tenant_ownership() valida contra la tabla user_tenants que el
# usuario pertenece al tenant solicitado. require_tenant_access() es la
# dependencia FastAPI que se usa en routers que acepten X-Tenant-ID.


def x_verify_tenant_ownership__mutmut_17(user: dict[str, Any], tenant_id: str) -> bool:
    """Verifica que el usuario pertenece al tenant solicitado.

    Fuente de verdad: tabla ``user_tenants`` en SQLite (clave compuesta
    ``(user_id, tenant_id)``). Si el usuario no tiene asignado el tenant,
    retorna False y el caller debe denegar el acceso con 403.

    Args:
        user: Dict con al menos ``user_id`` (devuelto por get_current_user).
        tenant_id: ID del tenant que se quiere acceder (del header X-Tenant-ID).

    Returns:
        True si el usuario pertenece al tenant, False en caso contrario.
    """
    if not tenant_id:
        return False

    user_id = user.get("user_id") if isinstance(user, dict) else None
    if not user_id:
        return False

    # Lazy import para romper circular: sqlite_manager <-> repositorios.
    from src.core.db import DatabaseManager

    db = DatabaseManager()
    row = db.fetchone(
        "SELECT 1 AS OK FROM USER_TENANTS WHERE USER_ID = ? AND TENANT_ID = ? LIMIT 1",
        (user_id, tenant_id),
    )
    return bool(row)


# ─── Bug TENANT-03: X-Tenant-ID bypass ─────────────────────────────────
# Cualquier usuario autenticado podia pasar X-Tenant-ID: <otro_tenant>
# en el header y acceder a datos ajenos sin verificacion de ownership.
# verify_tenant_ownership() valida contra la tabla user_tenants que el
# usuario pertenece al tenant solicitado. require_tenant_access() es la
# dependencia FastAPI que se usa en routers que acepten X-Tenant-ID.


def x_verify_tenant_ownership__mutmut_18(user: dict[str, Any], tenant_id: str) -> bool:
    """Verifica que el usuario pertenece al tenant solicitado.

    Fuente de verdad: tabla ``user_tenants`` en SQLite (clave compuesta
    ``(user_id, tenant_id)``). Si el usuario no tiene asignado el tenant,
    retorna False y el caller debe denegar el acceso con 403.

    Args:
        user: Dict con al menos ``user_id`` (devuelto por get_current_user).
        tenant_id: ID del tenant que se quiere acceder (del header X-Tenant-ID).

    Returns:
        True si el usuario pertenece al tenant, False en caso contrario.
    """
    if not tenant_id:
        return False

    user_id = user.get("user_id") if isinstance(user, dict) else None
    if not user_id:
        return False

    # Lazy import para romper circular: sqlite_manager <-> repositorios.
    from src.core.db import DatabaseManager

    db = DatabaseManager()
    row = db.fetchone(
        "SELECT 1 AS ok FROM user_tenants WHERE user_id = ? AND tenant_id = ? LIMIT 1",
        (user_id, tenant_id),
    )
    return bool(None)

mutants_x_verify_tenant_ownership__mutmut['_mutmut_orig'] = x_verify_tenant_ownership__mutmut_orig # type: ignore # mutmut generated
mutants_x_verify_tenant_ownership__mutmut['x_verify_tenant_ownership__mutmut_1'] = x_verify_tenant_ownership__mutmut_1 # type: ignore # mutmut generated
mutants_x_verify_tenant_ownership__mutmut['x_verify_tenant_ownership__mutmut_2'] = x_verify_tenant_ownership__mutmut_2 # type: ignore # mutmut generated
mutants_x_verify_tenant_ownership__mutmut['x_verify_tenant_ownership__mutmut_3'] = x_verify_tenant_ownership__mutmut_3 # type: ignore # mutmut generated
mutants_x_verify_tenant_ownership__mutmut['x_verify_tenant_ownership__mutmut_4'] = x_verify_tenant_ownership__mutmut_4 # type: ignore # mutmut generated
mutants_x_verify_tenant_ownership__mutmut['x_verify_tenant_ownership__mutmut_5'] = x_verify_tenant_ownership__mutmut_5 # type: ignore # mutmut generated
mutants_x_verify_tenant_ownership__mutmut['x_verify_tenant_ownership__mutmut_6'] = x_verify_tenant_ownership__mutmut_6 # type: ignore # mutmut generated
mutants_x_verify_tenant_ownership__mutmut['x_verify_tenant_ownership__mutmut_7'] = x_verify_tenant_ownership__mutmut_7 # type: ignore # mutmut generated
mutants_x_verify_tenant_ownership__mutmut['x_verify_tenant_ownership__mutmut_8'] = x_verify_tenant_ownership__mutmut_8 # type: ignore # mutmut generated
mutants_x_verify_tenant_ownership__mutmut['x_verify_tenant_ownership__mutmut_9'] = x_verify_tenant_ownership__mutmut_9 # type: ignore # mutmut generated
mutants_x_verify_tenant_ownership__mutmut['x_verify_tenant_ownership__mutmut_10'] = x_verify_tenant_ownership__mutmut_10 # type: ignore # mutmut generated
mutants_x_verify_tenant_ownership__mutmut['x_verify_tenant_ownership__mutmut_11'] = x_verify_tenant_ownership__mutmut_11 # type: ignore # mutmut generated
mutants_x_verify_tenant_ownership__mutmut['x_verify_tenant_ownership__mutmut_12'] = x_verify_tenant_ownership__mutmut_12 # type: ignore # mutmut generated
mutants_x_verify_tenant_ownership__mutmut['x_verify_tenant_ownership__mutmut_13'] = x_verify_tenant_ownership__mutmut_13 # type: ignore # mutmut generated
mutants_x_verify_tenant_ownership__mutmut['x_verify_tenant_ownership__mutmut_14'] = x_verify_tenant_ownership__mutmut_14 # type: ignore # mutmut generated
mutants_x_verify_tenant_ownership__mutmut['x_verify_tenant_ownership__mutmut_15'] = x_verify_tenant_ownership__mutmut_15 # type: ignore # mutmut generated
mutants_x_verify_tenant_ownership__mutmut['x_verify_tenant_ownership__mutmut_16'] = x_verify_tenant_ownership__mutmut_16 # type: ignore # mutmut generated
mutants_x_verify_tenant_ownership__mutmut['x_verify_tenant_ownership__mutmut_17'] = x_verify_tenant_ownership__mutmut_17 # type: ignore # mutmut generated
mutants_x_verify_tenant_ownership__mutmut['x_verify_tenant_ownership__mutmut_18'] = x_verify_tenant_ownership__mutmut_18 # type: ignore # mutmut generated
mutants_x_require_tenant_access__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_require_tenant_access__mutmut)
async def require_tenant_access(
    request: Request,
    user: dict[str, Any] = Depends(lambda: None),
) -> dict[str, Any]:
    """Dependencia FastAPI que valida el acceso del usuario al tenant del header.

    Lee ``X-Tenant-ID`` del header, valida que el usuario autenticado
    pertenezca a ese tenant (vía ``verify_tenant_ownership`` contra
    ``user_tenants``) y retorna el contexto con ``tenant_id`` validado.

    Debe combinarse con ``get_current_user`` para autenticar al usuario.
    Uso tipico::

        @router.get("/workflows")
        async def list_workflows(
            ctx: dict = Depends(require_tenant_access),
        ):
            tenant_id = ctx["tenant_id"]
            ...

    Args:
        request: Solicitud HTTP (para leer el header X-Tenant-ID).
        user: Usuario autenticado (Depends(get_current_user)).

    Returns:
        Dict con ``user`` y ``tenant_id`` validado.

    Raises:
        HTTPException 401: Si no hay usuario autenticado.
        HTTPException 400: Si falta el header X-Tenant-ID.
        HTTPException 403: Si el usuario no pertenece al tenant.
    """
    # Import diferido para evitar ciclo con auth.py (que importa dependencies).
    from src.api_v2.auth import get_current_user

    if user is None:
        user = await get_current_user(request, None, None)

    if not user or not user.get("user_id"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Autenticacion requerida para acceder a recursos de tenant.",
        )

    tenant_id = (request.headers.get("X-Tenant-ID") or "").strip()
    if not tenant_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Header X-Tenant-ID requerido para este recurso.",
        )

    if not verify_tenant_ownership(user, tenant_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No autorizado para acceder al tenant solicitado.",
        )

    return {"user": user, "tenant_id": tenant_id}


async def x_require_tenant_access__mutmut_orig(
    request: Request,
    user: dict[str, Any] = Depends(lambda: None),
) -> dict[str, Any]:
    """Dependencia FastAPI que valida el acceso del usuario al tenant del header.

    Lee ``X-Tenant-ID`` del header, valida que el usuario autenticado
    pertenezca a ese tenant (vía ``verify_tenant_ownership`` contra
    ``user_tenants``) y retorna el contexto con ``tenant_id`` validado.

    Debe combinarse con ``get_current_user`` para autenticar al usuario.
    Uso tipico::

        @router.get("/workflows")
        async def list_workflows(
            ctx: dict = Depends(require_tenant_access),
        ):
            tenant_id = ctx["tenant_id"]
            ...

    Args:
        request: Solicitud HTTP (para leer el header X-Tenant-ID).
        user: Usuario autenticado (Depends(get_current_user)).

    Returns:
        Dict con ``user`` y ``tenant_id`` validado.

    Raises:
        HTTPException 401: Si no hay usuario autenticado.
        HTTPException 400: Si falta el header X-Tenant-ID.
        HTTPException 403: Si el usuario no pertenece al tenant.
    """
    # Import diferido para evitar ciclo con auth.py (que importa dependencies).
    from src.api_v2.auth import get_current_user

    if user is None:
        user = await get_current_user(request, None, None)

    if not user or not user.get("user_id"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Autenticacion requerida para acceder a recursos de tenant.",
        )

    tenant_id = (request.headers.get("X-Tenant-ID") or "").strip()
    if not tenant_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Header X-Tenant-ID requerido para este recurso.",
        )

    if not verify_tenant_ownership(user, tenant_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No autorizado para acceder al tenant solicitado.",
        )

    return {"user": user, "tenant_id": tenant_id}


async def x_require_tenant_access__mutmut_1(
    request: Request,
    user: dict[str, Any] = Depends(lambda: None),
) -> dict[str, Any]:
    """Dependencia FastAPI que valida el acceso del usuario al tenant del header.

    Lee ``X-Tenant-ID`` del header, valida que el usuario autenticado
    pertenezca a ese tenant (vía ``verify_tenant_ownership`` contra
    ``user_tenants``) y retorna el contexto con ``tenant_id`` validado.

    Debe combinarse con ``get_current_user`` para autenticar al usuario.
    Uso tipico::

        @router.get("/workflows")
        async def list_workflows(
            ctx: dict = Depends(require_tenant_access),
        ):
            tenant_id = ctx["tenant_id"]
            ...

    Args:
        request: Solicitud HTTP (para leer el header X-Tenant-ID).
        user: Usuario autenticado (Depends(get_current_user)).

    Returns:
        Dict con ``user`` y ``tenant_id`` validado.

    Raises:
        HTTPException 401: Si no hay usuario autenticado.
        HTTPException 400: Si falta el header X-Tenant-ID.
        HTTPException 403: Si el usuario no pertenece al tenant.
    """
    # Import diferido para evitar ciclo con auth.py (que importa dependencies).
    from src.api_v2.auth import get_current_user

    if user is not None:
        user = await get_current_user(request, None, None)

    if not user or not user.get("user_id"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Autenticacion requerida para acceder a recursos de tenant.",
        )

    tenant_id = (request.headers.get("X-Tenant-ID") or "").strip()
    if not tenant_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Header X-Tenant-ID requerido para este recurso.",
        )

    if not verify_tenant_ownership(user, tenant_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No autorizado para acceder al tenant solicitado.",
        )

    return {"user": user, "tenant_id": tenant_id}


async def x_require_tenant_access__mutmut_2(
    request: Request,
    user: dict[str, Any] = Depends(lambda: None),
) -> dict[str, Any]:
    """Dependencia FastAPI que valida el acceso del usuario al tenant del header.

    Lee ``X-Tenant-ID`` del header, valida que el usuario autenticado
    pertenezca a ese tenant (vía ``verify_tenant_ownership`` contra
    ``user_tenants``) y retorna el contexto con ``tenant_id`` validado.

    Debe combinarse con ``get_current_user`` para autenticar al usuario.
    Uso tipico::

        @router.get("/workflows")
        async def list_workflows(
            ctx: dict = Depends(require_tenant_access),
        ):
            tenant_id = ctx["tenant_id"]
            ...

    Args:
        request: Solicitud HTTP (para leer el header X-Tenant-ID).
        user: Usuario autenticado (Depends(get_current_user)).

    Returns:
        Dict con ``user`` y ``tenant_id`` validado.

    Raises:
        HTTPException 401: Si no hay usuario autenticado.
        HTTPException 400: Si falta el header X-Tenant-ID.
        HTTPException 403: Si el usuario no pertenece al tenant.
    """
    # Import diferido para evitar ciclo con auth.py (que importa dependencies).
    from src.api_v2.auth import get_current_user

    if user is None:
        user = None

    if not user or not user.get("user_id"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Autenticacion requerida para acceder a recursos de tenant.",
        )

    tenant_id = (request.headers.get("X-Tenant-ID") or "").strip()
    if not tenant_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Header X-Tenant-ID requerido para este recurso.",
        )

    if not verify_tenant_ownership(user, tenant_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No autorizado para acceder al tenant solicitado.",
        )

    return {"user": user, "tenant_id": tenant_id}


async def x_require_tenant_access__mutmut_3(
    request: Request,
    user: dict[str, Any] = Depends(lambda: None),
) -> dict[str, Any]:
    """Dependencia FastAPI que valida el acceso del usuario al tenant del header.

    Lee ``X-Tenant-ID`` del header, valida que el usuario autenticado
    pertenezca a ese tenant (vía ``verify_tenant_ownership`` contra
    ``user_tenants``) y retorna el contexto con ``tenant_id`` validado.

    Debe combinarse con ``get_current_user`` para autenticar al usuario.
    Uso tipico::

        @router.get("/workflows")
        async def list_workflows(
            ctx: dict = Depends(require_tenant_access),
        ):
            tenant_id = ctx["tenant_id"]
            ...

    Args:
        request: Solicitud HTTP (para leer el header X-Tenant-ID).
        user: Usuario autenticado (Depends(get_current_user)).

    Returns:
        Dict con ``user`` y ``tenant_id`` validado.

    Raises:
        HTTPException 401: Si no hay usuario autenticado.
        HTTPException 400: Si falta el header X-Tenant-ID.
        HTTPException 403: Si el usuario no pertenece al tenant.
    """
    # Import diferido para evitar ciclo con auth.py (que importa dependencies).
    from src.api_v2.auth import get_current_user

    if user is None:
        user = await get_current_user(None, None, None)

    if not user or not user.get("user_id"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Autenticacion requerida para acceder a recursos de tenant.",
        )

    tenant_id = (request.headers.get("X-Tenant-ID") or "").strip()
    if not tenant_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Header X-Tenant-ID requerido para este recurso.",
        )

    if not verify_tenant_ownership(user, tenant_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No autorizado para acceder al tenant solicitado.",
        )

    return {"user": user, "tenant_id": tenant_id}


async def x_require_tenant_access__mutmut_4(
    request: Request,
    user: dict[str, Any] = Depends(lambda: None),
) -> dict[str, Any]:
    """Dependencia FastAPI que valida el acceso del usuario al tenant del header.

    Lee ``X-Tenant-ID`` del header, valida que el usuario autenticado
    pertenezca a ese tenant (vía ``verify_tenant_ownership`` contra
    ``user_tenants``) y retorna el contexto con ``tenant_id`` validado.

    Debe combinarse con ``get_current_user`` para autenticar al usuario.
    Uso tipico::

        @router.get("/workflows")
        async def list_workflows(
            ctx: dict = Depends(require_tenant_access),
        ):
            tenant_id = ctx["tenant_id"]
            ...

    Args:
        request: Solicitud HTTP (para leer el header X-Tenant-ID).
        user: Usuario autenticado (Depends(get_current_user)).

    Returns:
        Dict con ``user`` y ``tenant_id`` validado.

    Raises:
        HTTPException 401: Si no hay usuario autenticado.
        HTTPException 400: Si falta el header X-Tenant-ID.
        HTTPException 403: Si el usuario no pertenece al tenant.
    """
    # Import diferido para evitar ciclo con auth.py (que importa dependencies).
    from src.api_v2.auth import get_current_user

    if user is None:
        user = await get_current_user(None, None)

    if not user or not user.get("user_id"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Autenticacion requerida para acceder a recursos de tenant.",
        )

    tenant_id = (request.headers.get("X-Tenant-ID") or "").strip()
    if not tenant_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Header X-Tenant-ID requerido para este recurso.",
        )

    if not verify_tenant_ownership(user, tenant_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No autorizado para acceder al tenant solicitado.",
        )

    return {"user": user, "tenant_id": tenant_id}


async def x_require_tenant_access__mutmut_5(
    request: Request,
    user: dict[str, Any] = Depends(lambda: None),
) -> dict[str, Any]:
    """Dependencia FastAPI que valida el acceso del usuario al tenant del header.

    Lee ``X-Tenant-ID`` del header, valida que el usuario autenticado
    pertenezca a ese tenant (vía ``verify_tenant_ownership`` contra
    ``user_tenants``) y retorna el contexto con ``tenant_id`` validado.

    Debe combinarse con ``get_current_user`` para autenticar al usuario.
    Uso tipico::

        @router.get("/workflows")
        async def list_workflows(
            ctx: dict = Depends(require_tenant_access),
        ):
            tenant_id = ctx["tenant_id"]
            ...

    Args:
        request: Solicitud HTTP (para leer el header X-Tenant-ID).
        user: Usuario autenticado (Depends(get_current_user)).

    Returns:
        Dict con ``user`` y ``tenant_id`` validado.

    Raises:
        HTTPException 401: Si no hay usuario autenticado.
        HTTPException 400: Si falta el header X-Tenant-ID.
        HTTPException 403: Si el usuario no pertenece al tenant.
    """
    # Import diferido para evitar ciclo con auth.py (que importa dependencies).
    from src.api_v2.auth import get_current_user

    if user is None:
        user = await get_current_user(request, None)

    if not user or not user.get("user_id"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Autenticacion requerida para acceder a recursos de tenant.",
        )

    tenant_id = (request.headers.get("X-Tenant-ID") or "").strip()
    if not tenant_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Header X-Tenant-ID requerido para este recurso.",
        )

    if not verify_tenant_ownership(user, tenant_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No autorizado para acceder al tenant solicitado.",
        )

    return {"user": user, "tenant_id": tenant_id}


async def x_require_tenant_access__mutmut_6(
    request: Request,
    user: dict[str, Any] = Depends(lambda: None),
) -> dict[str, Any]:
    """Dependencia FastAPI que valida el acceso del usuario al tenant del header.

    Lee ``X-Tenant-ID`` del header, valida que el usuario autenticado
    pertenezca a ese tenant (vía ``verify_tenant_ownership`` contra
    ``user_tenants``) y retorna el contexto con ``tenant_id`` validado.

    Debe combinarse con ``get_current_user`` para autenticar al usuario.
    Uso tipico::

        @router.get("/workflows")
        async def list_workflows(
            ctx: dict = Depends(require_tenant_access),
        ):
            tenant_id = ctx["tenant_id"]
            ...

    Args:
        request: Solicitud HTTP (para leer el header X-Tenant-ID).
        user: Usuario autenticado (Depends(get_current_user)).

    Returns:
        Dict con ``user`` y ``tenant_id`` validado.

    Raises:
        HTTPException 401: Si no hay usuario autenticado.
        HTTPException 400: Si falta el header X-Tenant-ID.
        HTTPException 403: Si el usuario no pertenece al tenant.
    """
    # Import diferido para evitar ciclo con auth.py (que importa dependencies).
    from src.api_v2.auth import get_current_user

    if user is None:
        user = await get_current_user(request, None, )

    if not user or not user.get("user_id"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Autenticacion requerida para acceder a recursos de tenant.",
        )

    tenant_id = (request.headers.get("X-Tenant-ID") or "").strip()
    if not tenant_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Header X-Tenant-ID requerido para este recurso.",
        )

    if not verify_tenant_ownership(user, tenant_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No autorizado para acceder al tenant solicitado.",
        )

    return {"user": user, "tenant_id": tenant_id}


async def x_require_tenant_access__mutmut_7(
    request: Request,
    user: dict[str, Any] = Depends(lambda: None),
) -> dict[str, Any]:
    """Dependencia FastAPI que valida el acceso del usuario al tenant del header.

    Lee ``X-Tenant-ID`` del header, valida que el usuario autenticado
    pertenezca a ese tenant (vía ``verify_tenant_ownership`` contra
    ``user_tenants``) y retorna el contexto con ``tenant_id`` validado.

    Debe combinarse con ``get_current_user`` para autenticar al usuario.
    Uso tipico::

        @router.get("/workflows")
        async def list_workflows(
            ctx: dict = Depends(require_tenant_access),
        ):
            tenant_id = ctx["tenant_id"]
            ...

    Args:
        request: Solicitud HTTP (para leer el header X-Tenant-ID).
        user: Usuario autenticado (Depends(get_current_user)).

    Returns:
        Dict con ``user`` y ``tenant_id`` validado.

    Raises:
        HTTPException 401: Si no hay usuario autenticado.
        HTTPException 400: Si falta el header X-Tenant-ID.
        HTTPException 403: Si el usuario no pertenece al tenant.
    """
    # Import diferido para evitar ciclo con auth.py (que importa dependencies).
    from src.api_v2.auth import get_current_user

    if user is None:
        user = await get_current_user(request, None, None)

    if not user and not user.get("user_id"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Autenticacion requerida para acceder a recursos de tenant.",
        )

    tenant_id = (request.headers.get("X-Tenant-ID") or "").strip()
    if not tenant_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Header X-Tenant-ID requerido para este recurso.",
        )

    if not verify_tenant_ownership(user, tenant_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No autorizado para acceder al tenant solicitado.",
        )

    return {"user": user, "tenant_id": tenant_id}


async def x_require_tenant_access__mutmut_8(
    request: Request,
    user: dict[str, Any] = Depends(lambda: None),
) -> dict[str, Any]:
    """Dependencia FastAPI que valida el acceso del usuario al tenant del header.

    Lee ``X-Tenant-ID`` del header, valida que el usuario autenticado
    pertenezca a ese tenant (vía ``verify_tenant_ownership`` contra
    ``user_tenants``) y retorna el contexto con ``tenant_id`` validado.

    Debe combinarse con ``get_current_user`` para autenticar al usuario.
    Uso tipico::

        @router.get("/workflows")
        async def list_workflows(
            ctx: dict = Depends(require_tenant_access),
        ):
            tenant_id = ctx["tenant_id"]
            ...

    Args:
        request: Solicitud HTTP (para leer el header X-Tenant-ID).
        user: Usuario autenticado (Depends(get_current_user)).

    Returns:
        Dict con ``user`` y ``tenant_id`` validado.

    Raises:
        HTTPException 401: Si no hay usuario autenticado.
        HTTPException 400: Si falta el header X-Tenant-ID.
        HTTPException 403: Si el usuario no pertenece al tenant.
    """
    # Import diferido para evitar ciclo con auth.py (que importa dependencies).
    from src.api_v2.auth import get_current_user

    if user is None:
        user = await get_current_user(request, None, None)

    if user or not user.get("user_id"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Autenticacion requerida para acceder a recursos de tenant.",
        )

    tenant_id = (request.headers.get("X-Tenant-ID") or "").strip()
    if not tenant_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Header X-Tenant-ID requerido para este recurso.",
        )

    if not verify_tenant_ownership(user, tenant_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No autorizado para acceder al tenant solicitado.",
        )

    return {"user": user, "tenant_id": tenant_id}


async def x_require_tenant_access__mutmut_9(
    request: Request,
    user: dict[str, Any] = Depends(lambda: None),
) -> dict[str, Any]:
    """Dependencia FastAPI que valida el acceso del usuario al tenant del header.

    Lee ``X-Tenant-ID`` del header, valida que el usuario autenticado
    pertenezca a ese tenant (vía ``verify_tenant_ownership`` contra
    ``user_tenants``) y retorna el contexto con ``tenant_id`` validado.

    Debe combinarse con ``get_current_user`` para autenticar al usuario.
    Uso tipico::

        @router.get("/workflows")
        async def list_workflows(
            ctx: dict = Depends(require_tenant_access),
        ):
            tenant_id = ctx["tenant_id"]
            ...

    Args:
        request: Solicitud HTTP (para leer el header X-Tenant-ID).
        user: Usuario autenticado (Depends(get_current_user)).

    Returns:
        Dict con ``user`` y ``tenant_id`` validado.

    Raises:
        HTTPException 401: Si no hay usuario autenticado.
        HTTPException 400: Si falta el header X-Tenant-ID.
        HTTPException 403: Si el usuario no pertenece al tenant.
    """
    # Import diferido para evitar ciclo con auth.py (que importa dependencies).
    from src.api_v2.auth import get_current_user

    if user is None:
        user = await get_current_user(request, None, None)

    if not user or user.get("user_id"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Autenticacion requerida para acceder a recursos de tenant.",
        )

    tenant_id = (request.headers.get("X-Tenant-ID") or "").strip()
    if not tenant_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Header X-Tenant-ID requerido para este recurso.",
        )

    if not verify_tenant_ownership(user, tenant_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No autorizado para acceder al tenant solicitado.",
        )

    return {"user": user, "tenant_id": tenant_id}


async def x_require_tenant_access__mutmut_10(
    request: Request,
    user: dict[str, Any] = Depends(lambda: None),
) -> dict[str, Any]:
    """Dependencia FastAPI que valida el acceso del usuario al tenant del header.

    Lee ``X-Tenant-ID`` del header, valida que el usuario autenticado
    pertenezca a ese tenant (vía ``verify_tenant_ownership`` contra
    ``user_tenants``) y retorna el contexto con ``tenant_id`` validado.

    Debe combinarse con ``get_current_user`` para autenticar al usuario.
    Uso tipico::

        @router.get("/workflows")
        async def list_workflows(
            ctx: dict = Depends(require_tenant_access),
        ):
            tenant_id = ctx["tenant_id"]
            ...

    Args:
        request: Solicitud HTTP (para leer el header X-Tenant-ID).
        user: Usuario autenticado (Depends(get_current_user)).

    Returns:
        Dict con ``user`` y ``tenant_id`` validado.

    Raises:
        HTTPException 401: Si no hay usuario autenticado.
        HTTPException 400: Si falta el header X-Tenant-ID.
        HTTPException 403: Si el usuario no pertenece al tenant.
    """
    # Import diferido para evitar ciclo con auth.py (que importa dependencies).
    from src.api_v2.auth import get_current_user

    if user is None:
        user = await get_current_user(request, None, None)

    if not user or not user.get(None):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Autenticacion requerida para acceder a recursos de tenant.",
        )

    tenant_id = (request.headers.get("X-Tenant-ID") or "").strip()
    if not tenant_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Header X-Tenant-ID requerido para este recurso.",
        )

    if not verify_tenant_ownership(user, tenant_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No autorizado para acceder al tenant solicitado.",
        )

    return {"user": user, "tenant_id": tenant_id}


async def x_require_tenant_access__mutmut_11(
    request: Request,
    user: dict[str, Any] = Depends(lambda: None),
) -> dict[str, Any]:
    """Dependencia FastAPI que valida el acceso del usuario al tenant del header.

    Lee ``X-Tenant-ID`` del header, valida que el usuario autenticado
    pertenezca a ese tenant (vía ``verify_tenant_ownership`` contra
    ``user_tenants``) y retorna el contexto con ``tenant_id`` validado.

    Debe combinarse con ``get_current_user`` para autenticar al usuario.
    Uso tipico::

        @router.get("/workflows")
        async def list_workflows(
            ctx: dict = Depends(require_tenant_access),
        ):
            tenant_id = ctx["tenant_id"]
            ...

    Args:
        request: Solicitud HTTP (para leer el header X-Tenant-ID).
        user: Usuario autenticado (Depends(get_current_user)).

    Returns:
        Dict con ``user`` y ``tenant_id`` validado.

    Raises:
        HTTPException 401: Si no hay usuario autenticado.
        HTTPException 400: Si falta el header X-Tenant-ID.
        HTTPException 403: Si el usuario no pertenece al tenant.
    """
    # Import diferido para evitar ciclo con auth.py (que importa dependencies).
    from src.api_v2.auth import get_current_user

    if user is None:
        user = await get_current_user(request, None, None)

    if not user or not user.get("XXuser_idXX"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Autenticacion requerida para acceder a recursos de tenant.",
        )

    tenant_id = (request.headers.get("X-Tenant-ID") or "").strip()
    if not tenant_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Header X-Tenant-ID requerido para este recurso.",
        )

    if not verify_tenant_ownership(user, tenant_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No autorizado para acceder al tenant solicitado.",
        )

    return {"user": user, "tenant_id": tenant_id}


async def x_require_tenant_access__mutmut_12(
    request: Request,
    user: dict[str, Any] = Depends(lambda: None),
) -> dict[str, Any]:
    """Dependencia FastAPI que valida el acceso del usuario al tenant del header.

    Lee ``X-Tenant-ID`` del header, valida que el usuario autenticado
    pertenezca a ese tenant (vía ``verify_tenant_ownership`` contra
    ``user_tenants``) y retorna el contexto con ``tenant_id`` validado.

    Debe combinarse con ``get_current_user`` para autenticar al usuario.
    Uso tipico::

        @router.get("/workflows")
        async def list_workflows(
            ctx: dict = Depends(require_tenant_access),
        ):
            tenant_id = ctx["tenant_id"]
            ...

    Args:
        request: Solicitud HTTP (para leer el header X-Tenant-ID).
        user: Usuario autenticado (Depends(get_current_user)).

    Returns:
        Dict con ``user`` y ``tenant_id`` validado.

    Raises:
        HTTPException 401: Si no hay usuario autenticado.
        HTTPException 400: Si falta el header X-Tenant-ID.
        HTTPException 403: Si el usuario no pertenece al tenant.
    """
    # Import diferido para evitar ciclo con auth.py (que importa dependencies).
    from src.api_v2.auth import get_current_user

    if user is None:
        user = await get_current_user(request, None, None)

    if not user or not user.get("USER_ID"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Autenticacion requerida para acceder a recursos de tenant.",
        )

    tenant_id = (request.headers.get("X-Tenant-ID") or "").strip()
    if not tenant_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Header X-Tenant-ID requerido para este recurso.",
        )

    if not verify_tenant_ownership(user, tenant_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No autorizado para acceder al tenant solicitado.",
        )

    return {"user": user, "tenant_id": tenant_id}


async def x_require_tenant_access__mutmut_13(
    request: Request,
    user: dict[str, Any] = Depends(lambda: None),
) -> dict[str, Any]:
    """Dependencia FastAPI que valida el acceso del usuario al tenant del header.

    Lee ``X-Tenant-ID`` del header, valida que el usuario autenticado
    pertenezca a ese tenant (vía ``verify_tenant_ownership`` contra
    ``user_tenants``) y retorna el contexto con ``tenant_id`` validado.

    Debe combinarse con ``get_current_user`` para autenticar al usuario.
    Uso tipico::

        @router.get("/workflows")
        async def list_workflows(
            ctx: dict = Depends(require_tenant_access),
        ):
            tenant_id = ctx["tenant_id"]
            ...

    Args:
        request: Solicitud HTTP (para leer el header X-Tenant-ID).
        user: Usuario autenticado (Depends(get_current_user)).

    Returns:
        Dict con ``user`` y ``tenant_id`` validado.

    Raises:
        HTTPException 401: Si no hay usuario autenticado.
        HTTPException 400: Si falta el header X-Tenant-ID.
        HTTPException 403: Si el usuario no pertenece al tenant.
    """
    # Import diferido para evitar ciclo con auth.py (que importa dependencies).
    from src.api_v2.auth import get_current_user

    if user is None:
        user = await get_current_user(request, None, None)

    if not user or not user.get("user_id"):
        raise HTTPException(
            status_code=None,
            detail="Autenticacion requerida para acceder a recursos de tenant.",
        )

    tenant_id = (request.headers.get("X-Tenant-ID") or "").strip()
    if not tenant_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Header X-Tenant-ID requerido para este recurso.",
        )

    if not verify_tenant_ownership(user, tenant_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No autorizado para acceder al tenant solicitado.",
        )

    return {"user": user, "tenant_id": tenant_id}


async def x_require_tenant_access__mutmut_14(
    request: Request,
    user: dict[str, Any] = Depends(lambda: None),
) -> dict[str, Any]:
    """Dependencia FastAPI que valida el acceso del usuario al tenant del header.

    Lee ``X-Tenant-ID`` del header, valida que el usuario autenticado
    pertenezca a ese tenant (vía ``verify_tenant_ownership`` contra
    ``user_tenants``) y retorna el contexto con ``tenant_id`` validado.

    Debe combinarse con ``get_current_user`` para autenticar al usuario.
    Uso tipico::

        @router.get("/workflows")
        async def list_workflows(
            ctx: dict = Depends(require_tenant_access),
        ):
            tenant_id = ctx["tenant_id"]
            ...

    Args:
        request: Solicitud HTTP (para leer el header X-Tenant-ID).
        user: Usuario autenticado (Depends(get_current_user)).

    Returns:
        Dict con ``user`` y ``tenant_id`` validado.

    Raises:
        HTTPException 401: Si no hay usuario autenticado.
        HTTPException 400: Si falta el header X-Tenant-ID.
        HTTPException 403: Si el usuario no pertenece al tenant.
    """
    # Import diferido para evitar ciclo con auth.py (que importa dependencies).
    from src.api_v2.auth import get_current_user

    if user is None:
        user = await get_current_user(request, None, None)

    if not user or not user.get("user_id"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=None,
        )

    tenant_id = (request.headers.get("X-Tenant-ID") or "").strip()
    if not tenant_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Header X-Tenant-ID requerido para este recurso.",
        )

    if not verify_tenant_ownership(user, tenant_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No autorizado para acceder al tenant solicitado.",
        )

    return {"user": user, "tenant_id": tenant_id}


async def x_require_tenant_access__mutmut_15(
    request: Request,
    user: dict[str, Any] = Depends(lambda: None),
) -> dict[str, Any]:
    """Dependencia FastAPI que valida el acceso del usuario al tenant del header.

    Lee ``X-Tenant-ID`` del header, valida que el usuario autenticado
    pertenezca a ese tenant (vía ``verify_tenant_ownership`` contra
    ``user_tenants``) y retorna el contexto con ``tenant_id`` validado.

    Debe combinarse con ``get_current_user`` para autenticar al usuario.
    Uso tipico::

        @router.get("/workflows")
        async def list_workflows(
            ctx: dict = Depends(require_tenant_access),
        ):
            tenant_id = ctx["tenant_id"]
            ...

    Args:
        request: Solicitud HTTP (para leer el header X-Tenant-ID).
        user: Usuario autenticado (Depends(get_current_user)).

    Returns:
        Dict con ``user`` y ``tenant_id`` validado.

    Raises:
        HTTPException 401: Si no hay usuario autenticado.
        HTTPException 400: Si falta el header X-Tenant-ID.
        HTTPException 403: Si el usuario no pertenece al tenant.
    """
    # Import diferido para evitar ciclo con auth.py (que importa dependencies).
    from src.api_v2.auth import get_current_user

    if user is None:
        user = await get_current_user(request, None, None)

    if not user or not user.get("user_id"):
        raise HTTPException(
            detail="Autenticacion requerida para acceder a recursos de tenant.",
        )

    tenant_id = (request.headers.get("X-Tenant-ID") or "").strip()
    if not tenant_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Header X-Tenant-ID requerido para este recurso.",
        )

    if not verify_tenant_ownership(user, tenant_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No autorizado para acceder al tenant solicitado.",
        )

    return {"user": user, "tenant_id": tenant_id}


async def x_require_tenant_access__mutmut_16(
    request: Request,
    user: dict[str, Any] = Depends(lambda: None),
) -> dict[str, Any]:
    """Dependencia FastAPI que valida el acceso del usuario al tenant del header.

    Lee ``X-Tenant-ID`` del header, valida que el usuario autenticado
    pertenezca a ese tenant (vía ``verify_tenant_ownership`` contra
    ``user_tenants``) y retorna el contexto con ``tenant_id`` validado.

    Debe combinarse con ``get_current_user`` para autenticar al usuario.
    Uso tipico::

        @router.get("/workflows")
        async def list_workflows(
            ctx: dict = Depends(require_tenant_access),
        ):
            tenant_id = ctx["tenant_id"]
            ...

    Args:
        request: Solicitud HTTP (para leer el header X-Tenant-ID).
        user: Usuario autenticado (Depends(get_current_user)).

    Returns:
        Dict con ``user`` y ``tenant_id`` validado.

    Raises:
        HTTPException 401: Si no hay usuario autenticado.
        HTTPException 400: Si falta el header X-Tenant-ID.
        HTTPException 403: Si el usuario no pertenece al tenant.
    """
    # Import diferido para evitar ciclo con auth.py (que importa dependencies).
    from src.api_v2.auth import get_current_user

    if user is None:
        user = await get_current_user(request, None, None)

    if not user or not user.get("user_id"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            )

    tenant_id = (request.headers.get("X-Tenant-ID") or "").strip()
    if not tenant_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Header X-Tenant-ID requerido para este recurso.",
        )

    if not verify_tenant_ownership(user, tenant_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No autorizado para acceder al tenant solicitado.",
        )

    return {"user": user, "tenant_id": tenant_id}


async def x_require_tenant_access__mutmut_17(
    request: Request,
    user: dict[str, Any] = Depends(lambda: None),
) -> dict[str, Any]:
    """Dependencia FastAPI que valida el acceso del usuario al tenant del header.

    Lee ``X-Tenant-ID`` del header, valida que el usuario autenticado
    pertenezca a ese tenant (vía ``verify_tenant_ownership`` contra
    ``user_tenants``) y retorna el contexto con ``tenant_id`` validado.

    Debe combinarse con ``get_current_user`` para autenticar al usuario.
    Uso tipico::

        @router.get("/workflows")
        async def list_workflows(
            ctx: dict = Depends(require_tenant_access),
        ):
            tenant_id = ctx["tenant_id"]
            ...

    Args:
        request: Solicitud HTTP (para leer el header X-Tenant-ID).
        user: Usuario autenticado (Depends(get_current_user)).

    Returns:
        Dict con ``user`` y ``tenant_id`` validado.

    Raises:
        HTTPException 401: Si no hay usuario autenticado.
        HTTPException 400: Si falta el header X-Tenant-ID.
        HTTPException 403: Si el usuario no pertenece al tenant.
    """
    # Import diferido para evitar ciclo con auth.py (que importa dependencies).
    from src.api_v2.auth import get_current_user

    if user is None:
        user = await get_current_user(request, None, None)

    if not user or not user.get("user_id"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="XXAutenticacion requerida para acceder a recursos de tenant.XX",
        )

    tenant_id = (request.headers.get("X-Tenant-ID") or "").strip()
    if not tenant_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Header X-Tenant-ID requerido para este recurso.",
        )

    if not verify_tenant_ownership(user, tenant_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No autorizado para acceder al tenant solicitado.",
        )

    return {"user": user, "tenant_id": tenant_id}


async def x_require_tenant_access__mutmut_18(
    request: Request,
    user: dict[str, Any] = Depends(lambda: None),
) -> dict[str, Any]:
    """Dependencia FastAPI que valida el acceso del usuario al tenant del header.

    Lee ``X-Tenant-ID`` del header, valida que el usuario autenticado
    pertenezca a ese tenant (vía ``verify_tenant_ownership`` contra
    ``user_tenants``) y retorna el contexto con ``tenant_id`` validado.

    Debe combinarse con ``get_current_user`` para autenticar al usuario.
    Uso tipico::

        @router.get("/workflows")
        async def list_workflows(
            ctx: dict = Depends(require_tenant_access),
        ):
            tenant_id = ctx["tenant_id"]
            ...

    Args:
        request: Solicitud HTTP (para leer el header X-Tenant-ID).
        user: Usuario autenticado (Depends(get_current_user)).

    Returns:
        Dict con ``user`` y ``tenant_id`` validado.

    Raises:
        HTTPException 401: Si no hay usuario autenticado.
        HTTPException 400: Si falta el header X-Tenant-ID.
        HTTPException 403: Si el usuario no pertenece al tenant.
    """
    # Import diferido para evitar ciclo con auth.py (que importa dependencies).
    from src.api_v2.auth import get_current_user

    if user is None:
        user = await get_current_user(request, None, None)

    if not user or not user.get("user_id"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="autenticacion requerida para acceder a recursos de tenant.",
        )

    tenant_id = (request.headers.get("X-Tenant-ID") or "").strip()
    if not tenant_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Header X-Tenant-ID requerido para este recurso.",
        )

    if not verify_tenant_ownership(user, tenant_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No autorizado para acceder al tenant solicitado.",
        )

    return {"user": user, "tenant_id": tenant_id}


async def x_require_tenant_access__mutmut_19(
    request: Request,
    user: dict[str, Any] = Depends(lambda: None),
) -> dict[str, Any]:
    """Dependencia FastAPI que valida el acceso del usuario al tenant del header.

    Lee ``X-Tenant-ID`` del header, valida que el usuario autenticado
    pertenezca a ese tenant (vía ``verify_tenant_ownership`` contra
    ``user_tenants``) y retorna el contexto con ``tenant_id`` validado.

    Debe combinarse con ``get_current_user`` para autenticar al usuario.
    Uso tipico::

        @router.get("/workflows")
        async def list_workflows(
            ctx: dict = Depends(require_tenant_access),
        ):
            tenant_id = ctx["tenant_id"]
            ...

    Args:
        request: Solicitud HTTP (para leer el header X-Tenant-ID).
        user: Usuario autenticado (Depends(get_current_user)).

    Returns:
        Dict con ``user`` y ``tenant_id`` validado.

    Raises:
        HTTPException 401: Si no hay usuario autenticado.
        HTTPException 400: Si falta el header X-Tenant-ID.
        HTTPException 403: Si el usuario no pertenece al tenant.
    """
    # Import diferido para evitar ciclo con auth.py (que importa dependencies).
    from src.api_v2.auth import get_current_user

    if user is None:
        user = await get_current_user(request, None, None)

    if not user or not user.get("user_id"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="AUTENTICACION REQUERIDA PARA ACCEDER A RECURSOS DE TENANT.",
        )

    tenant_id = (request.headers.get("X-Tenant-ID") or "").strip()
    if not tenant_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Header X-Tenant-ID requerido para este recurso.",
        )

    if not verify_tenant_ownership(user, tenant_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No autorizado para acceder al tenant solicitado.",
        )

    return {"user": user, "tenant_id": tenant_id}


async def x_require_tenant_access__mutmut_20(
    request: Request,
    user: dict[str, Any] = Depends(lambda: None),
) -> dict[str, Any]:
    """Dependencia FastAPI que valida el acceso del usuario al tenant del header.

    Lee ``X-Tenant-ID`` del header, valida que el usuario autenticado
    pertenezca a ese tenant (vía ``verify_tenant_ownership`` contra
    ``user_tenants``) y retorna el contexto con ``tenant_id`` validado.

    Debe combinarse con ``get_current_user`` para autenticar al usuario.
    Uso tipico::

        @router.get("/workflows")
        async def list_workflows(
            ctx: dict = Depends(require_tenant_access),
        ):
            tenant_id = ctx["tenant_id"]
            ...

    Args:
        request: Solicitud HTTP (para leer el header X-Tenant-ID).
        user: Usuario autenticado (Depends(get_current_user)).

    Returns:
        Dict con ``user`` y ``tenant_id`` validado.

    Raises:
        HTTPException 401: Si no hay usuario autenticado.
        HTTPException 400: Si falta el header X-Tenant-ID.
        HTTPException 403: Si el usuario no pertenece al tenant.
    """
    # Import diferido para evitar ciclo con auth.py (que importa dependencies).
    from src.api_v2.auth import get_current_user

    if user is None:
        user = await get_current_user(request, None, None)

    if not user or not user.get("user_id"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Autenticacion requerida para acceder a recursos de tenant.",
        )

    tenant_id = None
    if not tenant_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Header X-Tenant-ID requerido para este recurso.",
        )

    if not verify_tenant_ownership(user, tenant_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No autorizado para acceder al tenant solicitado.",
        )

    return {"user": user, "tenant_id": tenant_id}


async def x_require_tenant_access__mutmut_21(
    request: Request,
    user: dict[str, Any] = Depends(lambda: None),
) -> dict[str, Any]:
    """Dependencia FastAPI que valida el acceso del usuario al tenant del header.

    Lee ``X-Tenant-ID`` del header, valida que el usuario autenticado
    pertenezca a ese tenant (vía ``verify_tenant_ownership`` contra
    ``user_tenants``) y retorna el contexto con ``tenant_id`` validado.

    Debe combinarse con ``get_current_user`` para autenticar al usuario.
    Uso tipico::

        @router.get("/workflows")
        async def list_workflows(
            ctx: dict = Depends(require_tenant_access),
        ):
            tenant_id = ctx["tenant_id"]
            ...

    Args:
        request: Solicitud HTTP (para leer el header X-Tenant-ID).
        user: Usuario autenticado (Depends(get_current_user)).

    Returns:
        Dict con ``user`` y ``tenant_id`` validado.

    Raises:
        HTTPException 401: Si no hay usuario autenticado.
        HTTPException 400: Si falta el header X-Tenant-ID.
        HTTPException 403: Si el usuario no pertenece al tenant.
    """
    # Import diferido para evitar ciclo con auth.py (que importa dependencies).
    from src.api_v2.auth import get_current_user

    if user is None:
        user = await get_current_user(request, None, None)

    if not user or not user.get("user_id"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Autenticacion requerida para acceder a recursos de tenant.",
        )

    tenant_id = (request.headers.get("X-Tenant-ID") and "").strip()
    if not tenant_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Header X-Tenant-ID requerido para este recurso.",
        )

    if not verify_tenant_ownership(user, tenant_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No autorizado para acceder al tenant solicitado.",
        )

    return {"user": user, "tenant_id": tenant_id}


async def x_require_tenant_access__mutmut_22(
    request: Request,
    user: dict[str, Any] = Depends(lambda: None),
) -> dict[str, Any]:
    """Dependencia FastAPI que valida el acceso del usuario al tenant del header.

    Lee ``X-Tenant-ID`` del header, valida que el usuario autenticado
    pertenezca a ese tenant (vía ``verify_tenant_ownership`` contra
    ``user_tenants``) y retorna el contexto con ``tenant_id`` validado.

    Debe combinarse con ``get_current_user`` para autenticar al usuario.
    Uso tipico::

        @router.get("/workflows")
        async def list_workflows(
            ctx: dict = Depends(require_tenant_access),
        ):
            tenant_id = ctx["tenant_id"]
            ...

    Args:
        request: Solicitud HTTP (para leer el header X-Tenant-ID).
        user: Usuario autenticado (Depends(get_current_user)).

    Returns:
        Dict con ``user`` y ``tenant_id`` validado.

    Raises:
        HTTPException 401: Si no hay usuario autenticado.
        HTTPException 400: Si falta el header X-Tenant-ID.
        HTTPException 403: Si el usuario no pertenece al tenant.
    """
    # Import diferido para evitar ciclo con auth.py (que importa dependencies).
    from src.api_v2.auth import get_current_user

    if user is None:
        user = await get_current_user(request, None, None)

    if not user or not user.get("user_id"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Autenticacion requerida para acceder a recursos de tenant.",
        )

    tenant_id = (request.headers.get(None) or "").strip()
    if not tenant_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Header X-Tenant-ID requerido para este recurso.",
        )

    if not verify_tenant_ownership(user, tenant_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No autorizado para acceder al tenant solicitado.",
        )

    return {"user": user, "tenant_id": tenant_id}


async def x_require_tenant_access__mutmut_23(
    request: Request,
    user: dict[str, Any] = Depends(lambda: None),
) -> dict[str, Any]:
    """Dependencia FastAPI que valida el acceso del usuario al tenant del header.

    Lee ``X-Tenant-ID`` del header, valida que el usuario autenticado
    pertenezca a ese tenant (vía ``verify_tenant_ownership`` contra
    ``user_tenants``) y retorna el contexto con ``tenant_id`` validado.

    Debe combinarse con ``get_current_user`` para autenticar al usuario.
    Uso tipico::

        @router.get("/workflows")
        async def list_workflows(
            ctx: dict = Depends(require_tenant_access),
        ):
            tenant_id = ctx["tenant_id"]
            ...

    Args:
        request: Solicitud HTTP (para leer el header X-Tenant-ID).
        user: Usuario autenticado (Depends(get_current_user)).

    Returns:
        Dict con ``user`` y ``tenant_id`` validado.

    Raises:
        HTTPException 401: Si no hay usuario autenticado.
        HTTPException 400: Si falta el header X-Tenant-ID.
        HTTPException 403: Si el usuario no pertenece al tenant.
    """
    # Import diferido para evitar ciclo con auth.py (que importa dependencies).
    from src.api_v2.auth import get_current_user

    if user is None:
        user = await get_current_user(request, None, None)

    if not user or not user.get("user_id"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Autenticacion requerida para acceder a recursos de tenant.",
        )

    tenant_id = (request.headers.get("XXX-Tenant-IDXX") or "").strip()
    if not tenant_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Header X-Tenant-ID requerido para este recurso.",
        )

    if not verify_tenant_ownership(user, tenant_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No autorizado para acceder al tenant solicitado.",
        )

    return {"user": user, "tenant_id": tenant_id}


async def x_require_tenant_access__mutmut_24(
    request: Request,
    user: dict[str, Any] = Depends(lambda: None),
) -> dict[str, Any]:
    """Dependencia FastAPI que valida el acceso del usuario al tenant del header.

    Lee ``X-Tenant-ID`` del header, valida que el usuario autenticado
    pertenezca a ese tenant (vía ``verify_tenant_ownership`` contra
    ``user_tenants``) y retorna el contexto con ``tenant_id`` validado.

    Debe combinarse con ``get_current_user`` para autenticar al usuario.
    Uso tipico::

        @router.get("/workflows")
        async def list_workflows(
            ctx: dict = Depends(require_tenant_access),
        ):
            tenant_id = ctx["tenant_id"]
            ...

    Args:
        request: Solicitud HTTP (para leer el header X-Tenant-ID).
        user: Usuario autenticado (Depends(get_current_user)).

    Returns:
        Dict con ``user`` y ``tenant_id`` validado.

    Raises:
        HTTPException 401: Si no hay usuario autenticado.
        HTTPException 400: Si falta el header X-Tenant-ID.
        HTTPException 403: Si el usuario no pertenece al tenant.
    """
    # Import diferido para evitar ciclo con auth.py (que importa dependencies).
    from src.api_v2.auth import get_current_user

    if user is None:
        user = await get_current_user(request, None, None)

    if not user or not user.get("user_id"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Autenticacion requerida para acceder a recursos de tenant.",
        )

    tenant_id = (request.headers.get("x-tenant-id") or "").strip()
    if not tenant_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Header X-Tenant-ID requerido para este recurso.",
        )

    if not verify_tenant_ownership(user, tenant_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No autorizado para acceder al tenant solicitado.",
        )

    return {"user": user, "tenant_id": tenant_id}


async def x_require_tenant_access__mutmut_25(
    request: Request,
    user: dict[str, Any] = Depends(lambda: None),
) -> dict[str, Any]:
    """Dependencia FastAPI que valida el acceso del usuario al tenant del header.

    Lee ``X-Tenant-ID`` del header, valida que el usuario autenticado
    pertenezca a ese tenant (vía ``verify_tenant_ownership`` contra
    ``user_tenants``) y retorna el contexto con ``tenant_id`` validado.

    Debe combinarse con ``get_current_user`` para autenticar al usuario.
    Uso tipico::

        @router.get("/workflows")
        async def list_workflows(
            ctx: dict = Depends(require_tenant_access),
        ):
            tenant_id = ctx["tenant_id"]
            ...

    Args:
        request: Solicitud HTTP (para leer el header X-Tenant-ID).
        user: Usuario autenticado (Depends(get_current_user)).

    Returns:
        Dict con ``user`` y ``tenant_id`` validado.

    Raises:
        HTTPException 401: Si no hay usuario autenticado.
        HTTPException 400: Si falta el header X-Tenant-ID.
        HTTPException 403: Si el usuario no pertenece al tenant.
    """
    # Import diferido para evitar ciclo con auth.py (que importa dependencies).
    from src.api_v2.auth import get_current_user

    if user is None:
        user = await get_current_user(request, None, None)

    if not user or not user.get("user_id"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Autenticacion requerida para acceder a recursos de tenant.",
        )

    tenant_id = (request.headers.get("X-TENANT-ID") or "").strip()
    if not tenant_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Header X-Tenant-ID requerido para este recurso.",
        )

    if not verify_tenant_ownership(user, tenant_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No autorizado para acceder al tenant solicitado.",
        )

    return {"user": user, "tenant_id": tenant_id}


async def x_require_tenant_access__mutmut_26(
    request: Request,
    user: dict[str, Any] = Depends(lambda: None),
) -> dict[str, Any]:
    """Dependencia FastAPI que valida el acceso del usuario al tenant del header.

    Lee ``X-Tenant-ID`` del header, valida que el usuario autenticado
    pertenezca a ese tenant (vía ``verify_tenant_ownership`` contra
    ``user_tenants``) y retorna el contexto con ``tenant_id`` validado.

    Debe combinarse con ``get_current_user`` para autenticar al usuario.
    Uso tipico::

        @router.get("/workflows")
        async def list_workflows(
            ctx: dict = Depends(require_tenant_access),
        ):
            tenant_id = ctx["tenant_id"]
            ...

    Args:
        request: Solicitud HTTP (para leer el header X-Tenant-ID).
        user: Usuario autenticado (Depends(get_current_user)).

    Returns:
        Dict con ``user`` y ``tenant_id`` validado.

    Raises:
        HTTPException 401: Si no hay usuario autenticado.
        HTTPException 400: Si falta el header X-Tenant-ID.
        HTTPException 403: Si el usuario no pertenece al tenant.
    """
    # Import diferido para evitar ciclo con auth.py (que importa dependencies).
    from src.api_v2.auth import get_current_user

    if user is None:
        user = await get_current_user(request, None, None)

    if not user or not user.get("user_id"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Autenticacion requerida para acceder a recursos de tenant.",
        )

    tenant_id = (request.headers.get("X-Tenant-ID") or "XXXX").strip()
    if not tenant_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Header X-Tenant-ID requerido para este recurso.",
        )

    if not verify_tenant_ownership(user, tenant_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No autorizado para acceder al tenant solicitado.",
        )

    return {"user": user, "tenant_id": tenant_id}


async def x_require_tenant_access__mutmut_27(
    request: Request,
    user: dict[str, Any] = Depends(lambda: None),
) -> dict[str, Any]:
    """Dependencia FastAPI que valida el acceso del usuario al tenant del header.

    Lee ``X-Tenant-ID`` del header, valida que el usuario autenticado
    pertenezca a ese tenant (vía ``verify_tenant_ownership`` contra
    ``user_tenants``) y retorna el contexto con ``tenant_id`` validado.

    Debe combinarse con ``get_current_user`` para autenticar al usuario.
    Uso tipico::

        @router.get("/workflows")
        async def list_workflows(
            ctx: dict = Depends(require_tenant_access),
        ):
            tenant_id = ctx["tenant_id"]
            ...

    Args:
        request: Solicitud HTTP (para leer el header X-Tenant-ID).
        user: Usuario autenticado (Depends(get_current_user)).

    Returns:
        Dict con ``user`` y ``tenant_id`` validado.

    Raises:
        HTTPException 401: Si no hay usuario autenticado.
        HTTPException 400: Si falta el header X-Tenant-ID.
        HTTPException 403: Si el usuario no pertenece al tenant.
    """
    # Import diferido para evitar ciclo con auth.py (que importa dependencies).
    from src.api_v2.auth import get_current_user

    if user is None:
        user = await get_current_user(request, None, None)

    if not user or not user.get("user_id"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Autenticacion requerida para acceder a recursos de tenant.",
        )

    tenant_id = (request.headers.get("X-Tenant-ID") or "").strip()
    if tenant_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Header X-Tenant-ID requerido para este recurso.",
        )

    if not verify_tenant_ownership(user, tenant_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No autorizado para acceder al tenant solicitado.",
        )

    return {"user": user, "tenant_id": tenant_id}


async def x_require_tenant_access__mutmut_28(
    request: Request,
    user: dict[str, Any] = Depends(lambda: None),
) -> dict[str, Any]:
    """Dependencia FastAPI que valida el acceso del usuario al tenant del header.

    Lee ``X-Tenant-ID`` del header, valida que el usuario autenticado
    pertenezca a ese tenant (vía ``verify_tenant_ownership`` contra
    ``user_tenants``) y retorna el contexto con ``tenant_id`` validado.

    Debe combinarse con ``get_current_user`` para autenticar al usuario.
    Uso tipico::

        @router.get("/workflows")
        async def list_workflows(
            ctx: dict = Depends(require_tenant_access),
        ):
            tenant_id = ctx["tenant_id"]
            ...

    Args:
        request: Solicitud HTTP (para leer el header X-Tenant-ID).
        user: Usuario autenticado (Depends(get_current_user)).

    Returns:
        Dict con ``user`` y ``tenant_id`` validado.

    Raises:
        HTTPException 401: Si no hay usuario autenticado.
        HTTPException 400: Si falta el header X-Tenant-ID.
        HTTPException 403: Si el usuario no pertenece al tenant.
    """
    # Import diferido para evitar ciclo con auth.py (que importa dependencies).
    from src.api_v2.auth import get_current_user

    if user is None:
        user = await get_current_user(request, None, None)

    if not user or not user.get("user_id"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Autenticacion requerida para acceder a recursos de tenant.",
        )

    tenant_id = (request.headers.get("X-Tenant-ID") or "").strip()
    if not tenant_id:
        raise HTTPException(
            status_code=None,
            detail="Header X-Tenant-ID requerido para este recurso.",
        )

    if not verify_tenant_ownership(user, tenant_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No autorizado para acceder al tenant solicitado.",
        )

    return {"user": user, "tenant_id": tenant_id}


async def x_require_tenant_access__mutmut_29(
    request: Request,
    user: dict[str, Any] = Depends(lambda: None),
) -> dict[str, Any]:
    """Dependencia FastAPI que valida el acceso del usuario al tenant del header.

    Lee ``X-Tenant-ID`` del header, valida que el usuario autenticado
    pertenezca a ese tenant (vía ``verify_tenant_ownership`` contra
    ``user_tenants``) y retorna el contexto con ``tenant_id`` validado.

    Debe combinarse con ``get_current_user`` para autenticar al usuario.
    Uso tipico::

        @router.get("/workflows")
        async def list_workflows(
            ctx: dict = Depends(require_tenant_access),
        ):
            tenant_id = ctx["tenant_id"]
            ...

    Args:
        request: Solicitud HTTP (para leer el header X-Tenant-ID).
        user: Usuario autenticado (Depends(get_current_user)).

    Returns:
        Dict con ``user`` y ``tenant_id`` validado.

    Raises:
        HTTPException 401: Si no hay usuario autenticado.
        HTTPException 400: Si falta el header X-Tenant-ID.
        HTTPException 403: Si el usuario no pertenece al tenant.
    """
    # Import diferido para evitar ciclo con auth.py (que importa dependencies).
    from src.api_v2.auth import get_current_user

    if user is None:
        user = await get_current_user(request, None, None)

    if not user or not user.get("user_id"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Autenticacion requerida para acceder a recursos de tenant.",
        )

    tenant_id = (request.headers.get("X-Tenant-ID") or "").strip()
    if not tenant_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=None,
        )

    if not verify_tenant_ownership(user, tenant_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No autorizado para acceder al tenant solicitado.",
        )

    return {"user": user, "tenant_id": tenant_id}


async def x_require_tenant_access__mutmut_30(
    request: Request,
    user: dict[str, Any] = Depends(lambda: None),
) -> dict[str, Any]:
    """Dependencia FastAPI que valida el acceso del usuario al tenant del header.

    Lee ``X-Tenant-ID`` del header, valida que el usuario autenticado
    pertenezca a ese tenant (vía ``verify_tenant_ownership`` contra
    ``user_tenants``) y retorna el contexto con ``tenant_id`` validado.

    Debe combinarse con ``get_current_user`` para autenticar al usuario.
    Uso tipico::

        @router.get("/workflows")
        async def list_workflows(
            ctx: dict = Depends(require_tenant_access),
        ):
            tenant_id = ctx["tenant_id"]
            ...

    Args:
        request: Solicitud HTTP (para leer el header X-Tenant-ID).
        user: Usuario autenticado (Depends(get_current_user)).

    Returns:
        Dict con ``user`` y ``tenant_id`` validado.

    Raises:
        HTTPException 401: Si no hay usuario autenticado.
        HTTPException 400: Si falta el header X-Tenant-ID.
        HTTPException 403: Si el usuario no pertenece al tenant.
    """
    # Import diferido para evitar ciclo con auth.py (que importa dependencies).
    from src.api_v2.auth import get_current_user

    if user is None:
        user = await get_current_user(request, None, None)

    if not user or not user.get("user_id"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Autenticacion requerida para acceder a recursos de tenant.",
        )

    tenant_id = (request.headers.get("X-Tenant-ID") or "").strip()
    if not tenant_id:
        raise HTTPException(
            detail="Header X-Tenant-ID requerido para este recurso.",
        )

    if not verify_tenant_ownership(user, tenant_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No autorizado para acceder al tenant solicitado.",
        )

    return {"user": user, "tenant_id": tenant_id}


async def x_require_tenant_access__mutmut_31(
    request: Request,
    user: dict[str, Any] = Depends(lambda: None),
) -> dict[str, Any]:
    """Dependencia FastAPI que valida el acceso del usuario al tenant del header.

    Lee ``X-Tenant-ID`` del header, valida que el usuario autenticado
    pertenezca a ese tenant (vía ``verify_tenant_ownership`` contra
    ``user_tenants``) y retorna el contexto con ``tenant_id`` validado.

    Debe combinarse con ``get_current_user`` para autenticar al usuario.
    Uso tipico::

        @router.get("/workflows")
        async def list_workflows(
            ctx: dict = Depends(require_tenant_access),
        ):
            tenant_id = ctx["tenant_id"]
            ...

    Args:
        request: Solicitud HTTP (para leer el header X-Tenant-ID).
        user: Usuario autenticado (Depends(get_current_user)).

    Returns:
        Dict con ``user`` y ``tenant_id`` validado.

    Raises:
        HTTPException 401: Si no hay usuario autenticado.
        HTTPException 400: Si falta el header X-Tenant-ID.
        HTTPException 403: Si el usuario no pertenece al tenant.
    """
    # Import diferido para evitar ciclo con auth.py (que importa dependencies).
    from src.api_v2.auth import get_current_user

    if user is None:
        user = await get_current_user(request, None, None)

    if not user or not user.get("user_id"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Autenticacion requerida para acceder a recursos de tenant.",
        )

    tenant_id = (request.headers.get("X-Tenant-ID") or "").strip()
    if not tenant_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            )

    if not verify_tenant_ownership(user, tenant_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No autorizado para acceder al tenant solicitado.",
        )

    return {"user": user, "tenant_id": tenant_id}


async def x_require_tenant_access__mutmut_32(
    request: Request,
    user: dict[str, Any] = Depends(lambda: None),
) -> dict[str, Any]:
    """Dependencia FastAPI que valida el acceso del usuario al tenant del header.

    Lee ``X-Tenant-ID`` del header, valida que el usuario autenticado
    pertenezca a ese tenant (vía ``verify_tenant_ownership`` contra
    ``user_tenants``) y retorna el contexto con ``tenant_id`` validado.

    Debe combinarse con ``get_current_user`` para autenticar al usuario.
    Uso tipico::

        @router.get("/workflows")
        async def list_workflows(
            ctx: dict = Depends(require_tenant_access),
        ):
            tenant_id = ctx["tenant_id"]
            ...

    Args:
        request: Solicitud HTTP (para leer el header X-Tenant-ID).
        user: Usuario autenticado (Depends(get_current_user)).

    Returns:
        Dict con ``user`` y ``tenant_id`` validado.

    Raises:
        HTTPException 401: Si no hay usuario autenticado.
        HTTPException 400: Si falta el header X-Tenant-ID.
        HTTPException 403: Si el usuario no pertenece al tenant.
    """
    # Import diferido para evitar ciclo con auth.py (que importa dependencies).
    from src.api_v2.auth import get_current_user

    if user is None:
        user = await get_current_user(request, None, None)

    if not user or not user.get("user_id"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Autenticacion requerida para acceder a recursos de tenant.",
        )

    tenant_id = (request.headers.get("X-Tenant-ID") or "").strip()
    if not tenant_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="XXHeader X-Tenant-ID requerido para este recurso.XX",
        )

    if not verify_tenant_ownership(user, tenant_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No autorizado para acceder al tenant solicitado.",
        )

    return {"user": user, "tenant_id": tenant_id}


async def x_require_tenant_access__mutmut_33(
    request: Request,
    user: dict[str, Any] = Depends(lambda: None),
) -> dict[str, Any]:
    """Dependencia FastAPI que valida el acceso del usuario al tenant del header.

    Lee ``X-Tenant-ID`` del header, valida que el usuario autenticado
    pertenezca a ese tenant (vía ``verify_tenant_ownership`` contra
    ``user_tenants``) y retorna el contexto con ``tenant_id`` validado.

    Debe combinarse con ``get_current_user`` para autenticar al usuario.
    Uso tipico::

        @router.get("/workflows")
        async def list_workflows(
            ctx: dict = Depends(require_tenant_access),
        ):
            tenant_id = ctx["tenant_id"]
            ...

    Args:
        request: Solicitud HTTP (para leer el header X-Tenant-ID).
        user: Usuario autenticado (Depends(get_current_user)).

    Returns:
        Dict con ``user`` y ``tenant_id`` validado.

    Raises:
        HTTPException 401: Si no hay usuario autenticado.
        HTTPException 400: Si falta el header X-Tenant-ID.
        HTTPException 403: Si el usuario no pertenece al tenant.
    """
    # Import diferido para evitar ciclo con auth.py (que importa dependencies).
    from src.api_v2.auth import get_current_user

    if user is None:
        user = await get_current_user(request, None, None)

    if not user or not user.get("user_id"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Autenticacion requerida para acceder a recursos de tenant.",
        )

    tenant_id = (request.headers.get("X-Tenant-ID") or "").strip()
    if not tenant_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="header x-tenant-id requerido para este recurso.",
        )

    if not verify_tenant_ownership(user, tenant_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No autorizado para acceder al tenant solicitado.",
        )

    return {"user": user, "tenant_id": tenant_id}


async def x_require_tenant_access__mutmut_34(
    request: Request,
    user: dict[str, Any] = Depends(lambda: None),
) -> dict[str, Any]:
    """Dependencia FastAPI que valida el acceso del usuario al tenant del header.

    Lee ``X-Tenant-ID`` del header, valida que el usuario autenticado
    pertenezca a ese tenant (vía ``verify_tenant_ownership`` contra
    ``user_tenants``) y retorna el contexto con ``tenant_id`` validado.

    Debe combinarse con ``get_current_user`` para autenticar al usuario.
    Uso tipico::

        @router.get("/workflows")
        async def list_workflows(
            ctx: dict = Depends(require_tenant_access),
        ):
            tenant_id = ctx["tenant_id"]
            ...

    Args:
        request: Solicitud HTTP (para leer el header X-Tenant-ID).
        user: Usuario autenticado (Depends(get_current_user)).

    Returns:
        Dict con ``user`` y ``tenant_id`` validado.

    Raises:
        HTTPException 401: Si no hay usuario autenticado.
        HTTPException 400: Si falta el header X-Tenant-ID.
        HTTPException 403: Si el usuario no pertenece al tenant.
    """
    # Import diferido para evitar ciclo con auth.py (que importa dependencies).
    from src.api_v2.auth import get_current_user

    if user is None:
        user = await get_current_user(request, None, None)

    if not user or not user.get("user_id"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Autenticacion requerida para acceder a recursos de tenant.",
        )

    tenant_id = (request.headers.get("X-Tenant-ID") or "").strip()
    if not tenant_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="HEADER X-TENANT-ID REQUERIDO PARA ESTE RECURSO.",
        )

    if not verify_tenant_ownership(user, tenant_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No autorizado para acceder al tenant solicitado.",
        )

    return {"user": user, "tenant_id": tenant_id}


async def x_require_tenant_access__mutmut_35(
    request: Request,
    user: dict[str, Any] = Depends(lambda: None),
) -> dict[str, Any]:
    """Dependencia FastAPI que valida el acceso del usuario al tenant del header.

    Lee ``X-Tenant-ID`` del header, valida que el usuario autenticado
    pertenezca a ese tenant (vía ``verify_tenant_ownership`` contra
    ``user_tenants``) y retorna el contexto con ``tenant_id`` validado.

    Debe combinarse con ``get_current_user`` para autenticar al usuario.
    Uso tipico::

        @router.get("/workflows")
        async def list_workflows(
            ctx: dict = Depends(require_tenant_access),
        ):
            tenant_id = ctx["tenant_id"]
            ...

    Args:
        request: Solicitud HTTP (para leer el header X-Tenant-ID).
        user: Usuario autenticado (Depends(get_current_user)).

    Returns:
        Dict con ``user`` y ``tenant_id`` validado.

    Raises:
        HTTPException 401: Si no hay usuario autenticado.
        HTTPException 400: Si falta el header X-Tenant-ID.
        HTTPException 403: Si el usuario no pertenece al tenant.
    """
    # Import diferido para evitar ciclo con auth.py (que importa dependencies).
    from src.api_v2.auth import get_current_user

    if user is None:
        user = await get_current_user(request, None, None)

    if not user or not user.get("user_id"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Autenticacion requerida para acceder a recursos de tenant.",
        )

    tenant_id = (request.headers.get("X-Tenant-ID") or "").strip()
    if not tenant_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Header X-Tenant-ID requerido para este recurso.",
        )

    if verify_tenant_ownership(user, tenant_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No autorizado para acceder al tenant solicitado.",
        )

    return {"user": user, "tenant_id": tenant_id}


async def x_require_tenant_access__mutmut_36(
    request: Request,
    user: dict[str, Any] = Depends(lambda: None),
) -> dict[str, Any]:
    """Dependencia FastAPI que valida el acceso del usuario al tenant del header.

    Lee ``X-Tenant-ID`` del header, valida que el usuario autenticado
    pertenezca a ese tenant (vía ``verify_tenant_ownership`` contra
    ``user_tenants``) y retorna el contexto con ``tenant_id`` validado.

    Debe combinarse con ``get_current_user`` para autenticar al usuario.
    Uso tipico::

        @router.get("/workflows")
        async def list_workflows(
            ctx: dict = Depends(require_tenant_access),
        ):
            tenant_id = ctx["tenant_id"]
            ...

    Args:
        request: Solicitud HTTP (para leer el header X-Tenant-ID).
        user: Usuario autenticado (Depends(get_current_user)).

    Returns:
        Dict con ``user`` y ``tenant_id`` validado.

    Raises:
        HTTPException 401: Si no hay usuario autenticado.
        HTTPException 400: Si falta el header X-Tenant-ID.
        HTTPException 403: Si el usuario no pertenece al tenant.
    """
    # Import diferido para evitar ciclo con auth.py (que importa dependencies).
    from src.api_v2.auth import get_current_user

    if user is None:
        user = await get_current_user(request, None, None)

    if not user or not user.get("user_id"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Autenticacion requerida para acceder a recursos de tenant.",
        )

    tenant_id = (request.headers.get("X-Tenant-ID") or "").strip()
    if not tenant_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Header X-Tenant-ID requerido para este recurso.",
        )

    if not verify_tenant_ownership(None, tenant_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No autorizado para acceder al tenant solicitado.",
        )

    return {"user": user, "tenant_id": tenant_id}


async def x_require_tenant_access__mutmut_37(
    request: Request,
    user: dict[str, Any] = Depends(lambda: None),
) -> dict[str, Any]:
    """Dependencia FastAPI que valida el acceso del usuario al tenant del header.

    Lee ``X-Tenant-ID`` del header, valida que el usuario autenticado
    pertenezca a ese tenant (vía ``verify_tenant_ownership`` contra
    ``user_tenants``) y retorna el contexto con ``tenant_id`` validado.

    Debe combinarse con ``get_current_user`` para autenticar al usuario.
    Uso tipico::

        @router.get("/workflows")
        async def list_workflows(
            ctx: dict = Depends(require_tenant_access),
        ):
            tenant_id = ctx["tenant_id"]
            ...

    Args:
        request: Solicitud HTTP (para leer el header X-Tenant-ID).
        user: Usuario autenticado (Depends(get_current_user)).

    Returns:
        Dict con ``user`` y ``tenant_id`` validado.

    Raises:
        HTTPException 401: Si no hay usuario autenticado.
        HTTPException 400: Si falta el header X-Tenant-ID.
        HTTPException 403: Si el usuario no pertenece al tenant.
    """
    # Import diferido para evitar ciclo con auth.py (que importa dependencies).
    from src.api_v2.auth import get_current_user

    if user is None:
        user = await get_current_user(request, None, None)

    if not user or not user.get("user_id"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Autenticacion requerida para acceder a recursos de tenant.",
        )

    tenant_id = (request.headers.get("X-Tenant-ID") or "").strip()
    if not tenant_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Header X-Tenant-ID requerido para este recurso.",
        )

    if not verify_tenant_ownership(user, None):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No autorizado para acceder al tenant solicitado.",
        )

    return {"user": user, "tenant_id": tenant_id}


async def x_require_tenant_access__mutmut_38(
    request: Request,
    user: dict[str, Any] = Depends(lambda: None),
) -> dict[str, Any]:
    """Dependencia FastAPI que valida el acceso del usuario al tenant del header.

    Lee ``X-Tenant-ID`` del header, valida que el usuario autenticado
    pertenezca a ese tenant (vía ``verify_tenant_ownership`` contra
    ``user_tenants``) y retorna el contexto con ``tenant_id`` validado.

    Debe combinarse con ``get_current_user`` para autenticar al usuario.
    Uso tipico::

        @router.get("/workflows")
        async def list_workflows(
            ctx: dict = Depends(require_tenant_access),
        ):
            tenant_id = ctx["tenant_id"]
            ...

    Args:
        request: Solicitud HTTP (para leer el header X-Tenant-ID).
        user: Usuario autenticado (Depends(get_current_user)).

    Returns:
        Dict con ``user`` y ``tenant_id`` validado.

    Raises:
        HTTPException 401: Si no hay usuario autenticado.
        HTTPException 400: Si falta el header X-Tenant-ID.
        HTTPException 403: Si el usuario no pertenece al tenant.
    """
    # Import diferido para evitar ciclo con auth.py (que importa dependencies).
    from src.api_v2.auth import get_current_user

    if user is None:
        user = await get_current_user(request, None, None)

    if not user or not user.get("user_id"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Autenticacion requerida para acceder a recursos de tenant.",
        )

    tenant_id = (request.headers.get("X-Tenant-ID") or "").strip()
    if not tenant_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Header X-Tenant-ID requerido para este recurso.",
        )

    if not verify_tenant_ownership(tenant_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No autorizado para acceder al tenant solicitado.",
        )

    return {"user": user, "tenant_id": tenant_id}


async def x_require_tenant_access__mutmut_39(
    request: Request,
    user: dict[str, Any] = Depends(lambda: None),
) -> dict[str, Any]:
    """Dependencia FastAPI que valida el acceso del usuario al tenant del header.

    Lee ``X-Tenant-ID`` del header, valida que el usuario autenticado
    pertenezca a ese tenant (vía ``verify_tenant_ownership`` contra
    ``user_tenants``) y retorna el contexto con ``tenant_id`` validado.

    Debe combinarse con ``get_current_user`` para autenticar al usuario.
    Uso tipico::

        @router.get("/workflows")
        async def list_workflows(
            ctx: dict = Depends(require_tenant_access),
        ):
            tenant_id = ctx["tenant_id"]
            ...

    Args:
        request: Solicitud HTTP (para leer el header X-Tenant-ID).
        user: Usuario autenticado (Depends(get_current_user)).

    Returns:
        Dict con ``user`` y ``tenant_id`` validado.

    Raises:
        HTTPException 401: Si no hay usuario autenticado.
        HTTPException 400: Si falta el header X-Tenant-ID.
        HTTPException 403: Si el usuario no pertenece al tenant.
    """
    # Import diferido para evitar ciclo con auth.py (que importa dependencies).
    from src.api_v2.auth import get_current_user

    if user is None:
        user = await get_current_user(request, None, None)

    if not user or not user.get("user_id"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Autenticacion requerida para acceder a recursos de tenant.",
        )

    tenant_id = (request.headers.get("X-Tenant-ID") or "").strip()
    if not tenant_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Header X-Tenant-ID requerido para este recurso.",
        )

    if not verify_tenant_ownership(user, ):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No autorizado para acceder al tenant solicitado.",
        )

    return {"user": user, "tenant_id": tenant_id}


async def x_require_tenant_access__mutmut_40(
    request: Request,
    user: dict[str, Any] = Depends(lambda: None),
) -> dict[str, Any]:
    """Dependencia FastAPI que valida el acceso del usuario al tenant del header.

    Lee ``X-Tenant-ID`` del header, valida que el usuario autenticado
    pertenezca a ese tenant (vía ``verify_tenant_ownership`` contra
    ``user_tenants``) y retorna el contexto con ``tenant_id`` validado.

    Debe combinarse con ``get_current_user`` para autenticar al usuario.
    Uso tipico::

        @router.get("/workflows")
        async def list_workflows(
            ctx: dict = Depends(require_tenant_access),
        ):
            tenant_id = ctx["tenant_id"]
            ...

    Args:
        request: Solicitud HTTP (para leer el header X-Tenant-ID).
        user: Usuario autenticado (Depends(get_current_user)).

    Returns:
        Dict con ``user`` y ``tenant_id`` validado.

    Raises:
        HTTPException 401: Si no hay usuario autenticado.
        HTTPException 400: Si falta el header X-Tenant-ID.
        HTTPException 403: Si el usuario no pertenece al tenant.
    """
    # Import diferido para evitar ciclo con auth.py (que importa dependencies).
    from src.api_v2.auth import get_current_user

    if user is None:
        user = await get_current_user(request, None, None)

    if not user or not user.get("user_id"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Autenticacion requerida para acceder a recursos de tenant.",
        )

    tenant_id = (request.headers.get("X-Tenant-ID") or "").strip()
    if not tenant_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Header X-Tenant-ID requerido para este recurso.",
        )

    if not verify_tenant_ownership(user, tenant_id):
        raise HTTPException(
            status_code=None,
            detail="No autorizado para acceder al tenant solicitado.",
        )

    return {"user": user, "tenant_id": tenant_id}


async def x_require_tenant_access__mutmut_41(
    request: Request,
    user: dict[str, Any] = Depends(lambda: None),
) -> dict[str, Any]:
    """Dependencia FastAPI que valida el acceso del usuario al tenant del header.

    Lee ``X-Tenant-ID`` del header, valida que el usuario autenticado
    pertenezca a ese tenant (vía ``verify_tenant_ownership`` contra
    ``user_tenants``) y retorna el contexto con ``tenant_id`` validado.

    Debe combinarse con ``get_current_user`` para autenticar al usuario.
    Uso tipico::

        @router.get("/workflows")
        async def list_workflows(
            ctx: dict = Depends(require_tenant_access),
        ):
            tenant_id = ctx["tenant_id"]
            ...

    Args:
        request: Solicitud HTTP (para leer el header X-Tenant-ID).
        user: Usuario autenticado (Depends(get_current_user)).

    Returns:
        Dict con ``user`` y ``tenant_id`` validado.

    Raises:
        HTTPException 401: Si no hay usuario autenticado.
        HTTPException 400: Si falta el header X-Tenant-ID.
        HTTPException 403: Si el usuario no pertenece al tenant.
    """
    # Import diferido para evitar ciclo con auth.py (que importa dependencies).
    from src.api_v2.auth import get_current_user

    if user is None:
        user = await get_current_user(request, None, None)

    if not user or not user.get("user_id"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Autenticacion requerida para acceder a recursos de tenant.",
        )

    tenant_id = (request.headers.get("X-Tenant-ID") or "").strip()
    if not tenant_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Header X-Tenant-ID requerido para este recurso.",
        )

    if not verify_tenant_ownership(user, tenant_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=None,
        )

    return {"user": user, "tenant_id": tenant_id}


async def x_require_tenant_access__mutmut_42(
    request: Request,
    user: dict[str, Any] = Depends(lambda: None),
) -> dict[str, Any]:
    """Dependencia FastAPI que valida el acceso del usuario al tenant del header.

    Lee ``X-Tenant-ID`` del header, valida que el usuario autenticado
    pertenezca a ese tenant (vía ``verify_tenant_ownership`` contra
    ``user_tenants``) y retorna el contexto con ``tenant_id`` validado.

    Debe combinarse con ``get_current_user`` para autenticar al usuario.
    Uso tipico::

        @router.get("/workflows")
        async def list_workflows(
            ctx: dict = Depends(require_tenant_access),
        ):
            tenant_id = ctx["tenant_id"]
            ...

    Args:
        request: Solicitud HTTP (para leer el header X-Tenant-ID).
        user: Usuario autenticado (Depends(get_current_user)).

    Returns:
        Dict con ``user`` y ``tenant_id`` validado.

    Raises:
        HTTPException 401: Si no hay usuario autenticado.
        HTTPException 400: Si falta el header X-Tenant-ID.
        HTTPException 403: Si el usuario no pertenece al tenant.
    """
    # Import diferido para evitar ciclo con auth.py (que importa dependencies).
    from src.api_v2.auth import get_current_user

    if user is None:
        user = await get_current_user(request, None, None)

    if not user or not user.get("user_id"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Autenticacion requerida para acceder a recursos de tenant.",
        )

    tenant_id = (request.headers.get("X-Tenant-ID") or "").strip()
    if not tenant_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Header X-Tenant-ID requerido para este recurso.",
        )

    if not verify_tenant_ownership(user, tenant_id):
        raise HTTPException(
            detail="No autorizado para acceder al tenant solicitado.",
        )

    return {"user": user, "tenant_id": tenant_id}


async def x_require_tenant_access__mutmut_43(
    request: Request,
    user: dict[str, Any] = Depends(lambda: None),
) -> dict[str, Any]:
    """Dependencia FastAPI que valida el acceso del usuario al tenant del header.

    Lee ``X-Tenant-ID`` del header, valida que el usuario autenticado
    pertenezca a ese tenant (vía ``verify_tenant_ownership`` contra
    ``user_tenants``) y retorna el contexto con ``tenant_id`` validado.

    Debe combinarse con ``get_current_user`` para autenticar al usuario.
    Uso tipico::

        @router.get("/workflows")
        async def list_workflows(
            ctx: dict = Depends(require_tenant_access),
        ):
            tenant_id = ctx["tenant_id"]
            ...

    Args:
        request: Solicitud HTTP (para leer el header X-Tenant-ID).
        user: Usuario autenticado (Depends(get_current_user)).

    Returns:
        Dict con ``user`` y ``tenant_id`` validado.

    Raises:
        HTTPException 401: Si no hay usuario autenticado.
        HTTPException 400: Si falta el header X-Tenant-ID.
        HTTPException 403: Si el usuario no pertenece al tenant.
    """
    # Import diferido para evitar ciclo con auth.py (que importa dependencies).
    from src.api_v2.auth import get_current_user

    if user is None:
        user = await get_current_user(request, None, None)

    if not user or not user.get("user_id"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Autenticacion requerida para acceder a recursos de tenant.",
        )

    tenant_id = (request.headers.get("X-Tenant-ID") or "").strip()
    if not tenant_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Header X-Tenant-ID requerido para este recurso.",
        )

    if not verify_tenant_ownership(user, tenant_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            )

    return {"user": user, "tenant_id": tenant_id}


async def x_require_tenant_access__mutmut_44(
    request: Request,
    user: dict[str, Any] = Depends(lambda: None),
) -> dict[str, Any]:
    """Dependencia FastAPI que valida el acceso del usuario al tenant del header.

    Lee ``X-Tenant-ID`` del header, valida que el usuario autenticado
    pertenezca a ese tenant (vía ``verify_tenant_ownership`` contra
    ``user_tenants``) y retorna el contexto con ``tenant_id`` validado.

    Debe combinarse con ``get_current_user`` para autenticar al usuario.
    Uso tipico::

        @router.get("/workflows")
        async def list_workflows(
            ctx: dict = Depends(require_tenant_access),
        ):
            tenant_id = ctx["tenant_id"]
            ...

    Args:
        request: Solicitud HTTP (para leer el header X-Tenant-ID).
        user: Usuario autenticado (Depends(get_current_user)).

    Returns:
        Dict con ``user`` y ``tenant_id`` validado.

    Raises:
        HTTPException 401: Si no hay usuario autenticado.
        HTTPException 400: Si falta el header X-Tenant-ID.
        HTTPException 403: Si el usuario no pertenece al tenant.
    """
    # Import diferido para evitar ciclo con auth.py (que importa dependencies).
    from src.api_v2.auth import get_current_user

    if user is None:
        user = await get_current_user(request, None, None)

    if not user or not user.get("user_id"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Autenticacion requerida para acceder a recursos de tenant.",
        )

    tenant_id = (request.headers.get("X-Tenant-ID") or "").strip()
    if not tenant_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Header X-Tenant-ID requerido para este recurso.",
        )

    if not verify_tenant_ownership(user, tenant_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="XXNo autorizado para acceder al tenant solicitado.XX",
        )

    return {"user": user, "tenant_id": tenant_id}


async def x_require_tenant_access__mutmut_45(
    request: Request,
    user: dict[str, Any] = Depends(lambda: None),
) -> dict[str, Any]:
    """Dependencia FastAPI que valida el acceso del usuario al tenant del header.

    Lee ``X-Tenant-ID`` del header, valida que el usuario autenticado
    pertenezca a ese tenant (vía ``verify_tenant_ownership`` contra
    ``user_tenants``) y retorna el contexto con ``tenant_id`` validado.

    Debe combinarse con ``get_current_user`` para autenticar al usuario.
    Uso tipico::

        @router.get("/workflows")
        async def list_workflows(
            ctx: dict = Depends(require_tenant_access),
        ):
            tenant_id = ctx["tenant_id"]
            ...

    Args:
        request: Solicitud HTTP (para leer el header X-Tenant-ID).
        user: Usuario autenticado (Depends(get_current_user)).

    Returns:
        Dict con ``user`` y ``tenant_id`` validado.

    Raises:
        HTTPException 401: Si no hay usuario autenticado.
        HTTPException 400: Si falta el header X-Tenant-ID.
        HTTPException 403: Si el usuario no pertenece al tenant.
    """
    # Import diferido para evitar ciclo con auth.py (que importa dependencies).
    from src.api_v2.auth import get_current_user

    if user is None:
        user = await get_current_user(request, None, None)

    if not user or not user.get("user_id"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Autenticacion requerida para acceder a recursos de tenant.",
        )

    tenant_id = (request.headers.get("X-Tenant-ID") or "").strip()
    if not tenant_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Header X-Tenant-ID requerido para este recurso.",
        )

    if not verify_tenant_ownership(user, tenant_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="no autorizado para acceder al tenant solicitado.",
        )

    return {"user": user, "tenant_id": tenant_id}


async def x_require_tenant_access__mutmut_46(
    request: Request,
    user: dict[str, Any] = Depends(lambda: None),
) -> dict[str, Any]:
    """Dependencia FastAPI que valida el acceso del usuario al tenant del header.

    Lee ``X-Tenant-ID`` del header, valida que el usuario autenticado
    pertenezca a ese tenant (vía ``verify_tenant_ownership`` contra
    ``user_tenants``) y retorna el contexto con ``tenant_id`` validado.

    Debe combinarse con ``get_current_user`` para autenticar al usuario.
    Uso tipico::

        @router.get("/workflows")
        async def list_workflows(
            ctx: dict = Depends(require_tenant_access),
        ):
            tenant_id = ctx["tenant_id"]
            ...

    Args:
        request: Solicitud HTTP (para leer el header X-Tenant-ID).
        user: Usuario autenticado (Depends(get_current_user)).

    Returns:
        Dict con ``user`` y ``tenant_id`` validado.

    Raises:
        HTTPException 401: Si no hay usuario autenticado.
        HTTPException 400: Si falta el header X-Tenant-ID.
        HTTPException 403: Si el usuario no pertenece al tenant.
    """
    # Import diferido para evitar ciclo con auth.py (que importa dependencies).
    from src.api_v2.auth import get_current_user

    if user is None:
        user = await get_current_user(request, None, None)

    if not user or not user.get("user_id"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Autenticacion requerida para acceder a recursos de tenant.",
        )

    tenant_id = (request.headers.get("X-Tenant-ID") or "").strip()
    if not tenant_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Header X-Tenant-ID requerido para este recurso.",
        )

    if not verify_tenant_ownership(user, tenant_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="NO AUTORIZADO PARA ACCEDER AL TENANT SOLICITADO.",
        )

    return {"user": user, "tenant_id": tenant_id}


async def x_require_tenant_access__mutmut_47(
    request: Request,
    user: dict[str, Any] = Depends(lambda: None),
) -> dict[str, Any]:
    """Dependencia FastAPI que valida el acceso del usuario al tenant del header.

    Lee ``X-Tenant-ID`` del header, valida que el usuario autenticado
    pertenezca a ese tenant (vía ``verify_tenant_ownership`` contra
    ``user_tenants``) y retorna el contexto con ``tenant_id`` validado.

    Debe combinarse con ``get_current_user`` para autenticar al usuario.
    Uso tipico::

        @router.get("/workflows")
        async def list_workflows(
            ctx: dict = Depends(require_tenant_access),
        ):
            tenant_id = ctx["tenant_id"]
            ...

    Args:
        request: Solicitud HTTP (para leer el header X-Tenant-ID).
        user: Usuario autenticado (Depends(get_current_user)).

    Returns:
        Dict con ``user`` y ``tenant_id`` validado.

    Raises:
        HTTPException 401: Si no hay usuario autenticado.
        HTTPException 400: Si falta el header X-Tenant-ID.
        HTTPException 403: Si el usuario no pertenece al tenant.
    """
    # Import diferido para evitar ciclo con auth.py (que importa dependencies).
    from src.api_v2.auth import get_current_user

    if user is None:
        user = await get_current_user(request, None, None)

    if not user or not user.get("user_id"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Autenticacion requerida para acceder a recursos de tenant.",
        )

    tenant_id = (request.headers.get("X-Tenant-ID") or "").strip()
    if not tenant_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Header X-Tenant-ID requerido para este recurso.",
        )

    if not verify_tenant_ownership(user, tenant_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No autorizado para acceder al tenant solicitado.",
        )

    return {"XXuserXX": user, "tenant_id": tenant_id}


async def x_require_tenant_access__mutmut_48(
    request: Request,
    user: dict[str, Any] = Depends(lambda: None),
) -> dict[str, Any]:
    """Dependencia FastAPI que valida el acceso del usuario al tenant del header.

    Lee ``X-Tenant-ID`` del header, valida que el usuario autenticado
    pertenezca a ese tenant (vía ``verify_tenant_ownership`` contra
    ``user_tenants``) y retorna el contexto con ``tenant_id`` validado.

    Debe combinarse con ``get_current_user`` para autenticar al usuario.
    Uso tipico::

        @router.get("/workflows")
        async def list_workflows(
            ctx: dict = Depends(require_tenant_access),
        ):
            tenant_id = ctx["tenant_id"]
            ...

    Args:
        request: Solicitud HTTP (para leer el header X-Tenant-ID).
        user: Usuario autenticado (Depends(get_current_user)).

    Returns:
        Dict con ``user`` y ``tenant_id`` validado.

    Raises:
        HTTPException 401: Si no hay usuario autenticado.
        HTTPException 400: Si falta el header X-Tenant-ID.
        HTTPException 403: Si el usuario no pertenece al tenant.
    """
    # Import diferido para evitar ciclo con auth.py (que importa dependencies).
    from src.api_v2.auth import get_current_user

    if user is None:
        user = await get_current_user(request, None, None)

    if not user or not user.get("user_id"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Autenticacion requerida para acceder a recursos de tenant.",
        )

    tenant_id = (request.headers.get("X-Tenant-ID") or "").strip()
    if not tenant_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Header X-Tenant-ID requerido para este recurso.",
        )

    if not verify_tenant_ownership(user, tenant_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No autorizado para acceder al tenant solicitado.",
        )

    return {"USER": user, "tenant_id": tenant_id}


async def x_require_tenant_access__mutmut_49(
    request: Request,
    user: dict[str, Any] = Depends(lambda: None),
) -> dict[str, Any]:
    """Dependencia FastAPI que valida el acceso del usuario al tenant del header.

    Lee ``X-Tenant-ID`` del header, valida que el usuario autenticado
    pertenezca a ese tenant (vía ``verify_tenant_ownership`` contra
    ``user_tenants``) y retorna el contexto con ``tenant_id`` validado.

    Debe combinarse con ``get_current_user`` para autenticar al usuario.
    Uso tipico::

        @router.get("/workflows")
        async def list_workflows(
            ctx: dict = Depends(require_tenant_access),
        ):
            tenant_id = ctx["tenant_id"]
            ...

    Args:
        request: Solicitud HTTP (para leer el header X-Tenant-ID).
        user: Usuario autenticado (Depends(get_current_user)).

    Returns:
        Dict con ``user`` y ``tenant_id`` validado.

    Raises:
        HTTPException 401: Si no hay usuario autenticado.
        HTTPException 400: Si falta el header X-Tenant-ID.
        HTTPException 403: Si el usuario no pertenece al tenant.
    """
    # Import diferido para evitar ciclo con auth.py (que importa dependencies).
    from src.api_v2.auth import get_current_user

    if user is None:
        user = await get_current_user(request, None, None)

    if not user or not user.get("user_id"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Autenticacion requerida para acceder a recursos de tenant.",
        )

    tenant_id = (request.headers.get("X-Tenant-ID") or "").strip()
    if not tenant_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Header X-Tenant-ID requerido para este recurso.",
        )

    if not verify_tenant_ownership(user, tenant_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No autorizado para acceder al tenant solicitado.",
        )

    return {"user": user, "XXtenant_idXX": tenant_id}


async def x_require_tenant_access__mutmut_50(
    request: Request,
    user: dict[str, Any] = Depends(lambda: None),
) -> dict[str, Any]:
    """Dependencia FastAPI que valida el acceso del usuario al tenant del header.

    Lee ``X-Tenant-ID`` del header, valida que el usuario autenticado
    pertenezca a ese tenant (vía ``verify_tenant_ownership`` contra
    ``user_tenants``) y retorna el contexto con ``tenant_id`` validado.

    Debe combinarse con ``get_current_user`` para autenticar al usuario.
    Uso tipico::

        @router.get("/workflows")
        async def list_workflows(
            ctx: dict = Depends(require_tenant_access),
        ):
            tenant_id = ctx["tenant_id"]
            ...

    Args:
        request: Solicitud HTTP (para leer el header X-Tenant-ID).
        user: Usuario autenticado (Depends(get_current_user)).

    Returns:
        Dict con ``user`` y ``tenant_id`` validado.

    Raises:
        HTTPException 401: Si no hay usuario autenticado.
        HTTPException 400: Si falta el header X-Tenant-ID.
        HTTPException 403: Si el usuario no pertenece al tenant.
    """
    # Import diferido para evitar ciclo con auth.py (que importa dependencies).
    from src.api_v2.auth import get_current_user

    if user is None:
        user = await get_current_user(request, None, None)

    if not user or not user.get("user_id"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Autenticacion requerida para acceder a recursos de tenant.",
        )

    tenant_id = (request.headers.get("X-Tenant-ID") or "").strip()
    if not tenant_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Header X-Tenant-ID requerido para este recurso.",
        )

    if not verify_tenant_ownership(user, tenant_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No autorizado para acceder al tenant solicitado.",
        )

    return {"user": user, "TENANT_ID": tenant_id}

mutants_x_require_tenant_access__mutmut['_mutmut_orig'] = x_require_tenant_access__mutmut_orig # type: ignore # mutmut generated
mutants_x_require_tenant_access__mutmut['x_require_tenant_access__mutmut_1'] = x_require_tenant_access__mutmut_1 # type: ignore # mutmut generated
mutants_x_require_tenant_access__mutmut['x_require_tenant_access__mutmut_2'] = x_require_tenant_access__mutmut_2 # type: ignore # mutmut generated
mutants_x_require_tenant_access__mutmut['x_require_tenant_access__mutmut_3'] = x_require_tenant_access__mutmut_3 # type: ignore # mutmut generated
mutants_x_require_tenant_access__mutmut['x_require_tenant_access__mutmut_4'] = x_require_tenant_access__mutmut_4 # type: ignore # mutmut generated
mutants_x_require_tenant_access__mutmut['x_require_tenant_access__mutmut_5'] = x_require_tenant_access__mutmut_5 # type: ignore # mutmut generated
mutants_x_require_tenant_access__mutmut['x_require_tenant_access__mutmut_6'] = x_require_tenant_access__mutmut_6 # type: ignore # mutmut generated
mutants_x_require_tenant_access__mutmut['x_require_tenant_access__mutmut_7'] = x_require_tenant_access__mutmut_7 # type: ignore # mutmut generated
mutants_x_require_tenant_access__mutmut['x_require_tenant_access__mutmut_8'] = x_require_tenant_access__mutmut_8 # type: ignore # mutmut generated
mutants_x_require_tenant_access__mutmut['x_require_tenant_access__mutmut_9'] = x_require_tenant_access__mutmut_9 # type: ignore # mutmut generated
mutants_x_require_tenant_access__mutmut['x_require_tenant_access__mutmut_10'] = x_require_tenant_access__mutmut_10 # type: ignore # mutmut generated
mutants_x_require_tenant_access__mutmut['x_require_tenant_access__mutmut_11'] = x_require_tenant_access__mutmut_11 # type: ignore # mutmut generated
mutants_x_require_tenant_access__mutmut['x_require_tenant_access__mutmut_12'] = x_require_tenant_access__mutmut_12 # type: ignore # mutmut generated
mutants_x_require_tenant_access__mutmut['x_require_tenant_access__mutmut_13'] = x_require_tenant_access__mutmut_13 # type: ignore # mutmut generated
mutants_x_require_tenant_access__mutmut['x_require_tenant_access__mutmut_14'] = x_require_tenant_access__mutmut_14 # type: ignore # mutmut generated
mutants_x_require_tenant_access__mutmut['x_require_tenant_access__mutmut_15'] = x_require_tenant_access__mutmut_15 # type: ignore # mutmut generated
mutants_x_require_tenant_access__mutmut['x_require_tenant_access__mutmut_16'] = x_require_tenant_access__mutmut_16 # type: ignore # mutmut generated
mutants_x_require_tenant_access__mutmut['x_require_tenant_access__mutmut_17'] = x_require_tenant_access__mutmut_17 # type: ignore # mutmut generated
mutants_x_require_tenant_access__mutmut['x_require_tenant_access__mutmut_18'] = x_require_tenant_access__mutmut_18 # type: ignore # mutmut generated
mutants_x_require_tenant_access__mutmut['x_require_tenant_access__mutmut_19'] = x_require_tenant_access__mutmut_19 # type: ignore # mutmut generated
mutants_x_require_tenant_access__mutmut['x_require_tenant_access__mutmut_20'] = x_require_tenant_access__mutmut_20 # type: ignore # mutmut generated
mutants_x_require_tenant_access__mutmut['x_require_tenant_access__mutmut_21'] = x_require_tenant_access__mutmut_21 # type: ignore # mutmut generated
mutants_x_require_tenant_access__mutmut['x_require_tenant_access__mutmut_22'] = x_require_tenant_access__mutmut_22 # type: ignore # mutmut generated
mutants_x_require_tenant_access__mutmut['x_require_tenant_access__mutmut_23'] = x_require_tenant_access__mutmut_23 # type: ignore # mutmut generated
mutants_x_require_tenant_access__mutmut['x_require_tenant_access__mutmut_24'] = x_require_tenant_access__mutmut_24 # type: ignore # mutmut generated
mutants_x_require_tenant_access__mutmut['x_require_tenant_access__mutmut_25'] = x_require_tenant_access__mutmut_25 # type: ignore # mutmut generated
mutants_x_require_tenant_access__mutmut['x_require_tenant_access__mutmut_26'] = x_require_tenant_access__mutmut_26 # type: ignore # mutmut generated
mutants_x_require_tenant_access__mutmut['x_require_tenant_access__mutmut_27'] = x_require_tenant_access__mutmut_27 # type: ignore # mutmut generated
mutants_x_require_tenant_access__mutmut['x_require_tenant_access__mutmut_28'] = x_require_tenant_access__mutmut_28 # type: ignore # mutmut generated
mutants_x_require_tenant_access__mutmut['x_require_tenant_access__mutmut_29'] = x_require_tenant_access__mutmut_29 # type: ignore # mutmut generated
mutants_x_require_tenant_access__mutmut['x_require_tenant_access__mutmut_30'] = x_require_tenant_access__mutmut_30 # type: ignore # mutmut generated
mutants_x_require_tenant_access__mutmut['x_require_tenant_access__mutmut_31'] = x_require_tenant_access__mutmut_31 # type: ignore # mutmut generated
mutants_x_require_tenant_access__mutmut['x_require_tenant_access__mutmut_32'] = x_require_tenant_access__mutmut_32 # type: ignore # mutmut generated
mutants_x_require_tenant_access__mutmut['x_require_tenant_access__mutmut_33'] = x_require_tenant_access__mutmut_33 # type: ignore # mutmut generated
mutants_x_require_tenant_access__mutmut['x_require_tenant_access__mutmut_34'] = x_require_tenant_access__mutmut_34 # type: ignore # mutmut generated
mutants_x_require_tenant_access__mutmut['x_require_tenant_access__mutmut_35'] = x_require_tenant_access__mutmut_35 # type: ignore # mutmut generated
mutants_x_require_tenant_access__mutmut['x_require_tenant_access__mutmut_36'] = x_require_tenant_access__mutmut_36 # type: ignore # mutmut generated
mutants_x_require_tenant_access__mutmut['x_require_tenant_access__mutmut_37'] = x_require_tenant_access__mutmut_37 # type: ignore # mutmut generated
mutants_x_require_tenant_access__mutmut['x_require_tenant_access__mutmut_38'] = x_require_tenant_access__mutmut_38 # type: ignore # mutmut generated
mutants_x_require_tenant_access__mutmut['x_require_tenant_access__mutmut_39'] = x_require_tenant_access__mutmut_39 # type: ignore # mutmut generated
mutants_x_require_tenant_access__mutmut['x_require_tenant_access__mutmut_40'] = x_require_tenant_access__mutmut_40 # type: ignore # mutmut generated
mutants_x_require_tenant_access__mutmut['x_require_tenant_access__mutmut_41'] = x_require_tenant_access__mutmut_41 # type: ignore # mutmut generated
mutants_x_require_tenant_access__mutmut['x_require_tenant_access__mutmut_42'] = x_require_tenant_access__mutmut_42 # type: ignore # mutmut generated
mutants_x_require_tenant_access__mutmut['x_require_tenant_access__mutmut_43'] = x_require_tenant_access__mutmut_43 # type: ignore # mutmut generated
mutants_x_require_tenant_access__mutmut['x_require_tenant_access__mutmut_44'] = x_require_tenant_access__mutmut_44 # type: ignore # mutmut generated
mutants_x_require_tenant_access__mutmut['x_require_tenant_access__mutmut_45'] = x_require_tenant_access__mutmut_45 # type: ignore # mutmut generated
mutants_x_require_tenant_access__mutmut['x_require_tenant_access__mutmut_46'] = x_require_tenant_access__mutmut_46 # type: ignore # mutmut generated
mutants_x_require_tenant_access__mutmut['x_require_tenant_access__mutmut_47'] = x_require_tenant_access__mutmut_47 # type: ignore # mutmut generated
mutants_x_require_tenant_access__mutmut['x_require_tenant_access__mutmut_48'] = x_require_tenant_access__mutmut_48 # type: ignore # mutmut generated
mutants_x_require_tenant_access__mutmut['x_require_tenant_access__mutmut_49'] = x_require_tenant_access__mutmut_49 # type: ignore # mutmut generated
mutants_x_require_tenant_access__mutmut['x_require_tenant_access__mutmut_50'] = x_require_tenant_access__mutmut_50 # type: ignore # mutmut generated


# ─── Re-exports de auth (BUG-ARCH-03) ────────────────────────────────────
# Algunos routers importan `require_permission` y `get_current_user` desde
# `dependencies`, otros desde `auth`. Para eliminar el drift y hacer ambos
# imports válidos, re-exportamos aquí los símbolos de auth.
# La fuente de verdad sigue siendo src/api_v2/auth.py.
# Esto resuelve el ImportError que impedía cargar api_v2.app.

from src.api_v2.auth import (
    generate_token,
    validate_token,
    get_current_user,
    get_optional_user,
    require_permission,
    get_tenant,
)

__all__ = [
    "generate_token",
    "get_connector_registry",
    "get_current_user",
    "get_db",
    "get_nlu_pipeline",
    "get_optional_user",
    "get_pagination",
    "get_rbac_manager",
    "get_redis",
    "get_telemetry_service",
    "get_tenant",
    "get_tenant_service",
    "get_workflow_engine",
    "get_workflow_repository",
    # Bug TENANT-03 — X-Tenant-ID bypass
    "require_permission",
    "require_tenant_access",
    "validate_token",
    "verify_tenant_ownership",
]
