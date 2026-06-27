"""SSO subpackage — SAML, OIDC, Keycloak, sessions.

Original sso.py module has been moved here as service.py to avoid
the module/package name collision that previously required an
importlib hack.
"""
from src.core.security.sso.constants import (
    KEYCLOAK_REALM,
    KEYCLOAK_URL,
    OIDC_STATE_PREFIX,
    SAML_NS,
    SSO_BASE_URL,
    SSO_SESSION_PREFIX,
    SSO_SESSION_TTL,
)
from src.core.security.sso.keycloak import auto_configure_keycloak
from src.core.security.sso.oidc import OIDCHandler
from src.core.security.sso.provider_manager import (
    configure_provider,
    ensure_tables,
    get_provider,
    get_providers,
    remove_provider,
)
from src.core.security.sso.routes import register_sso_routes
from src.core.security.sso.saml import SAMLHandler
from src.core.security.sso.service import SSOService
from src.core.security.sso.session import (
    cleanup_expired_sessions,
    create_or_link_user,
    create_sso_session,
    link_existing_user,
    logout_session,
    validate_sso_session,
)

__all__ = [
    "KEYCLOAK_REALM",
    "KEYCLOAK_URL",
    "OIDC_STATE_PREFIX",
    "SAML_NS",
    "SSO_BASE_URL",
    "SSO_SESSION_PREFIX",
    "SSO_SESSION_TTL",
    "OIDCHandler",
    "SAMLHandler",
    "SSOService",
    "auto_configure_keycloak",
    "cleanup_expired_sessions",
    "configure_provider",
    "create_or_link_user",
    "create_sso_session",
    "ensure_tables",
    "get_provider",
    "get_providers",
    "link_existing_user",
    "logout_session",
    "register_sso_routes",
    "remove_provider",
    "validate_sso_session",
]
