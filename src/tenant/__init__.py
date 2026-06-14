"""
Zenic-Flujo — Tenant Multi-Tenancy Service
=============================================

Modulos del sistema de multi-tenancy:

- service.py: TenantService principal (CRUD, resolucion, settings)
- context.py: Contexto thread-local (get/set/clear tenant_id)
- storage.py: Aprovisionamiento de BD por tenant
- middleware.py: Middleware Flask para resolucion de tenant
- features.py: Feature flags por tenant
"""

from src.tenant.context import (
    TenantContext,
    clear_tenant_context,
    get_current_tenant_id,
    set_current_tenant_id,
)
from src.tenant.features import TenantFeatureManager
from src.tenant.middleware import TenantMiddleware
from src.tenant.service import TenantService
from src.tenant.storage import TENANT_PLANS, TenantConnectionPool, TenantStorageProvisioner

__all__ = [
    "TENANT_PLANS",
    "TenantConnectionPool",
    "TenantContext",
    "TenantFeatureManager",
    "TenantMiddleware",
    "TenantService",
    "TenantStorageProvisioner",
    "clear_tenant_context",
    "get_current_tenant_id",
    "set_current_tenant_id",
]
