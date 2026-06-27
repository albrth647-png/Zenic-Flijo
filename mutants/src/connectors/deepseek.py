"""
Conector DeepSeek — IA via DeepSeek API
============================================

Permite generar texto, razonamiento y codificacion
via la API de DeepSeek (OpenAI-compatible).
"""

from __future__ import annotations

from typing import Any

from src.core.logging import setup_logging
from src.sdk.base import BaseConnector
from src.sdk.http_client import HttpClient, HTTPClientError
from src.sdk.schema import ActionDefinition, AuthRequirement, ConnectorSchema

logger = setup_logging(__name__)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁDeepseekConnectorǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁDeepseekConnectorǁ_get_api_key__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDeepseekConnectorǁconnect__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDeepseekConnectorǁexecute__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDeepseekConnectorǁvalidate__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDeepseekConnectorǁdisconnect__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDeepseekConnectorǁ_list_models__mutmut: MutantDict = {}  # type: ignore


class DeepseekConnector(BaseConnector):
    """Conector para DeepSeek: generacion de texto y razonamiento."""

    name = "deepseek"
    version = "1.0.0"
    description = "Genera texto y razonamiento avanzado via DeepSeek AI"
    category = "ai_data"
    icon = "sparkles"
    author = "Zenic-Flijo"

    @_mutmut_mutated(mutants_xǁDeepseekConnectorǁ__init____mutmut)
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._base_url: str = "https://api.deepseek.com/v1"
        self._http: HttpClient | None = None

    def xǁDeepseekConnectorǁ__init____mutmut_orig(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._base_url: str = "https://api.deepseek.com/v1"
        self._http: HttpClient | None = None

    def xǁDeepseekConnectorǁ__init____mutmut_1(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._base_url: str = None
        self._http: HttpClient | None = None

    def xǁDeepseekConnectorǁ__init____mutmut_2(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._base_url: str = "XXhttps://api.deepseek.com/v1XX"
        self._http: HttpClient | None = None

    def xǁDeepseekConnectorǁ__init____mutmut_3(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._base_url: str = "HTTPS://API.DEEPSEEK.COM/V1"
        self._http: HttpClient | None = None

    def xǁDeepseekConnectorǁ__init____mutmut_4(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._base_url: str = "https://api.deepseek.com/v1"
        self._http: HttpClient | None = ""

    @_mutmut_mutated(mutants_xǁDeepseekConnectorǁ_get_api_key__mutmut)
    def _get_api_key(self) -> str:
        """Extract API key from the auth provider."""
        if not self._auth_provider:
            return ""
        # Try to access _api_key directly (APIKeyAuth)
        api_key = getattr(self._auth_provider, "_api_key", "")
        if api_key:
            return api_key
        # Fallback: use apply_auth and extract from headers
        auth_request: dict[str, Any] = {"headers": {}, "params": {}}
        self._auth_provider.apply_auth(auth_request)
        headers = auth_request.get("headers", {})
        api_key = headers.get("X-API-Key", headers.get("Authorization", "").replace("Bearer ", ""))
        return api_key

    def xǁDeepseekConnectorǁ_get_api_key__mutmut_orig(self) -> str:
        """Extract API key from the auth provider."""
        if not self._auth_provider:
            return ""
        # Try to access _api_key directly (APIKeyAuth)
        api_key = getattr(self._auth_provider, "_api_key", "")
        if api_key:
            return api_key
        # Fallback: use apply_auth and extract from headers
        auth_request: dict[str, Any] = {"headers": {}, "params": {}}
        self._auth_provider.apply_auth(auth_request)
        headers = auth_request.get("headers", {})
        api_key = headers.get("X-API-Key", headers.get("Authorization", "").replace("Bearer ", ""))
        return api_key

    def xǁDeepseekConnectorǁ_get_api_key__mutmut_1(self) -> str:
        """Extract API key from the auth provider."""
        if self._auth_provider:
            return ""
        # Try to access _api_key directly (APIKeyAuth)
        api_key = getattr(self._auth_provider, "_api_key", "")
        if api_key:
            return api_key
        # Fallback: use apply_auth and extract from headers
        auth_request: dict[str, Any] = {"headers": {}, "params": {}}
        self._auth_provider.apply_auth(auth_request)
        headers = auth_request.get("headers", {})
        api_key = headers.get("X-API-Key", headers.get("Authorization", "").replace("Bearer ", ""))
        return api_key

    def xǁDeepseekConnectorǁ_get_api_key__mutmut_2(self) -> str:
        """Extract API key from the auth provider."""
        if not self._auth_provider:
            return "XXXX"
        # Try to access _api_key directly (APIKeyAuth)
        api_key = getattr(self._auth_provider, "_api_key", "")
        if api_key:
            return api_key
        # Fallback: use apply_auth and extract from headers
        auth_request: dict[str, Any] = {"headers": {}, "params": {}}
        self._auth_provider.apply_auth(auth_request)
        headers = auth_request.get("headers", {})
        api_key = headers.get("X-API-Key", headers.get("Authorization", "").replace("Bearer ", ""))
        return api_key

    def xǁDeepseekConnectorǁ_get_api_key__mutmut_3(self) -> str:
        """Extract API key from the auth provider."""
        if not self._auth_provider:
            return ""
        # Try to access _api_key directly (APIKeyAuth)
        api_key = None
        if api_key:
            return api_key
        # Fallback: use apply_auth and extract from headers
        auth_request: dict[str, Any] = {"headers": {}, "params": {}}
        self._auth_provider.apply_auth(auth_request)
        headers = auth_request.get("headers", {})
        api_key = headers.get("X-API-Key", headers.get("Authorization", "").replace("Bearer ", ""))
        return api_key

    def xǁDeepseekConnectorǁ_get_api_key__mutmut_4(self) -> str:
        """Extract API key from the auth provider."""
        if not self._auth_provider:
            return ""
        # Try to access _api_key directly (APIKeyAuth)
        api_key = getattr(None, "_api_key", "")
        if api_key:
            return api_key
        # Fallback: use apply_auth and extract from headers
        auth_request: dict[str, Any] = {"headers": {}, "params": {}}
        self._auth_provider.apply_auth(auth_request)
        headers = auth_request.get("headers", {})
        api_key = headers.get("X-API-Key", headers.get("Authorization", "").replace("Bearer ", ""))
        return api_key

    def xǁDeepseekConnectorǁ_get_api_key__mutmut_5(self) -> str:
        """Extract API key from the auth provider."""
        if not self._auth_provider:
            return ""
        # Try to access _api_key directly (APIKeyAuth)
        api_key = getattr(self._auth_provider, None, "")
        if api_key:
            return api_key
        # Fallback: use apply_auth and extract from headers
        auth_request: dict[str, Any] = {"headers": {}, "params": {}}
        self._auth_provider.apply_auth(auth_request)
        headers = auth_request.get("headers", {})
        api_key = headers.get("X-API-Key", headers.get("Authorization", "").replace("Bearer ", ""))
        return api_key

    def xǁDeepseekConnectorǁ_get_api_key__mutmut_6(self) -> str:
        """Extract API key from the auth provider."""
        if not self._auth_provider:
            return ""
        # Try to access _api_key directly (APIKeyAuth)
        api_key = getattr(self._auth_provider, "_api_key", None)
        if api_key:
            return api_key
        # Fallback: use apply_auth and extract from headers
        auth_request: dict[str, Any] = {"headers": {}, "params": {}}
        self._auth_provider.apply_auth(auth_request)
        headers = auth_request.get("headers", {})
        api_key = headers.get("X-API-Key", headers.get("Authorization", "").replace("Bearer ", ""))
        return api_key

    def xǁDeepseekConnectorǁ_get_api_key__mutmut_7(self) -> str:
        """Extract API key from the auth provider."""
        if not self._auth_provider:
            return ""
        # Try to access _api_key directly (APIKeyAuth)
        api_key = getattr("_api_key", "")
        if api_key:
            return api_key
        # Fallback: use apply_auth and extract from headers
        auth_request: dict[str, Any] = {"headers": {}, "params": {}}
        self._auth_provider.apply_auth(auth_request)
        headers = auth_request.get("headers", {})
        api_key = headers.get("X-API-Key", headers.get("Authorization", "").replace("Bearer ", ""))
        return api_key

    def xǁDeepseekConnectorǁ_get_api_key__mutmut_8(self) -> str:
        """Extract API key from the auth provider."""
        if not self._auth_provider:
            return ""
        # Try to access _api_key directly (APIKeyAuth)
        api_key = getattr(self._auth_provider, "")
        if api_key:
            return api_key
        # Fallback: use apply_auth and extract from headers
        auth_request: dict[str, Any] = {"headers": {}, "params": {}}
        self._auth_provider.apply_auth(auth_request)
        headers = auth_request.get("headers", {})
        api_key = headers.get("X-API-Key", headers.get("Authorization", "").replace("Bearer ", ""))
        return api_key

    def xǁDeepseekConnectorǁ_get_api_key__mutmut_9(self) -> str:
        """Extract API key from the auth provider."""
        if not self._auth_provider:
            return ""
        # Try to access _api_key directly (APIKeyAuth)
        api_key = getattr(self._auth_provider, "_api_key", )
        if api_key:
            return api_key
        # Fallback: use apply_auth and extract from headers
        auth_request: dict[str, Any] = {"headers": {}, "params": {}}
        self._auth_provider.apply_auth(auth_request)
        headers = auth_request.get("headers", {})
        api_key = headers.get("X-API-Key", headers.get("Authorization", "").replace("Bearer ", ""))
        return api_key

    def xǁDeepseekConnectorǁ_get_api_key__mutmut_10(self) -> str:
        """Extract API key from the auth provider."""
        if not self._auth_provider:
            return ""
        # Try to access _api_key directly (APIKeyAuth)
        api_key = getattr(self._auth_provider, "XX_api_keyXX", "")
        if api_key:
            return api_key
        # Fallback: use apply_auth and extract from headers
        auth_request: dict[str, Any] = {"headers": {}, "params": {}}
        self._auth_provider.apply_auth(auth_request)
        headers = auth_request.get("headers", {})
        api_key = headers.get("X-API-Key", headers.get("Authorization", "").replace("Bearer ", ""))
        return api_key

    def xǁDeepseekConnectorǁ_get_api_key__mutmut_11(self) -> str:
        """Extract API key from the auth provider."""
        if not self._auth_provider:
            return ""
        # Try to access _api_key directly (APIKeyAuth)
        api_key = getattr(self._auth_provider, "_API_KEY", "")
        if api_key:
            return api_key
        # Fallback: use apply_auth and extract from headers
        auth_request: dict[str, Any] = {"headers": {}, "params": {}}
        self._auth_provider.apply_auth(auth_request)
        headers = auth_request.get("headers", {})
        api_key = headers.get("X-API-Key", headers.get("Authorization", "").replace("Bearer ", ""))
        return api_key

    def xǁDeepseekConnectorǁ_get_api_key__mutmut_12(self) -> str:
        """Extract API key from the auth provider."""
        if not self._auth_provider:
            return ""
        # Try to access _api_key directly (APIKeyAuth)
        api_key = getattr(self._auth_provider, "_api_key", "XXXX")
        if api_key:
            return api_key
        # Fallback: use apply_auth and extract from headers
        auth_request: dict[str, Any] = {"headers": {}, "params": {}}
        self._auth_provider.apply_auth(auth_request)
        headers = auth_request.get("headers", {})
        api_key = headers.get("X-API-Key", headers.get("Authorization", "").replace("Bearer ", ""))
        return api_key

    def xǁDeepseekConnectorǁ_get_api_key__mutmut_13(self) -> str:
        """Extract API key from the auth provider."""
        if not self._auth_provider:
            return ""
        # Try to access _api_key directly (APIKeyAuth)
        api_key = getattr(self._auth_provider, "_api_key", "")
        if api_key:
            return api_key
        # Fallback: use apply_auth and extract from headers
        auth_request: dict[str, Any] = None
        self._auth_provider.apply_auth(auth_request)
        headers = auth_request.get("headers", {})
        api_key = headers.get("X-API-Key", headers.get("Authorization", "").replace("Bearer ", ""))
        return api_key

    def xǁDeepseekConnectorǁ_get_api_key__mutmut_14(self) -> str:
        """Extract API key from the auth provider."""
        if not self._auth_provider:
            return ""
        # Try to access _api_key directly (APIKeyAuth)
        api_key = getattr(self._auth_provider, "_api_key", "")
        if api_key:
            return api_key
        # Fallback: use apply_auth and extract from headers
        auth_request: dict[str, Any] = {"XXheadersXX": {}, "params": {}}
        self._auth_provider.apply_auth(auth_request)
        headers = auth_request.get("headers", {})
        api_key = headers.get("X-API-Key", headers.get("Authorization", "").replace("Bearer ", ""))
        return api_key

    def xǁDeepseekConnectorǁ_get_api_key__mutmut_15(self) -> str:
        """Extract API key from the auth provider."""
        if not self._auth_provider:
            return ""
        # Try to access _api_key directly (APIKeyAuth)
        api_key = getattr(self._auth_provider, "_api_key", "")
        if api_key:
            return api_key
        # Fallback: use apply_auth and extract from headers
        auth_request: dict[str, Any] = {"HEADERS": {}, "params": {}}
        self._auth_provider.apply_auth(auth_request)
        headers = auth_request.get("headers", {})
        api_key = headers.get("X-API-Key", headers.get("Authorization", "").replace("Bearer ", ""))
        return api_key

    def xǁDeepseekConnectorǁ_get_api_key__mutmut_16(self) -> str:
        """Extract API key from the auth provider."""
        if not self._auth_provider:
            return ""
        # Try to access _api_key directly (APIKeyAuth)
        api_key = getattr(self._auth_provider, "_api_key", "")
        if api_key:
            return api_key
        # Fallback: use apply_auth and extract from headers
        auth_request: dict[str, Any] = {"headers": {}, "XXparamsXX": {}}
        self._auth_provider.apply_auth(auth_request)
        headers = auth_request.get("headers", {})
        api_key = headers.get("X-API-Key", headers.get("Authorization", "").replace("Bearer ", ""))
        return api_key

    def xǁDeepseekConnectorǁ_get_api_key__mutmut_17(self) -> str:
        """Extract API key from the auth provider."""
        if not self._auth_provider:
            return ""
        # Try to access _api_key directly (APIKeyAuth)
        api_key = getattr(self._auth_provider, "_api_key", "")
        if api_key:
            return api_key
        # Fallback: use apply_auth and extract from headers
        auth_request: dict[str, Any] = {"headers": {}, "PARAMS": {}}
        self._auth_provider.apply_auth(auth_request)
        headers = auth_request.get("headers", {})
        api_key = headers.get("X-API-Key", headers.get("Authorization", "").replace("Bearer ", ""))
        return api_key

    def xǁDeepseekConnectorǁ_get_api_key__mutmut_18(self) -> str:
        """Extract API key from the auth provider."""
        if not self._auth_provider:
            return ""
        # Try to access _api_key directly (APIKeyAuth)
        api_key = getattr(self._auth_provider, "_api_key", "")
        if api_key:
            return api_key
        # Fallback: use apply_auth and extract from headers
        auth_request: dict[str, Any] = {"headers": {}, "params": {}}
        self._auth_provider.apply_auth(None)
        headers = auth_request.get("headers", {})
        api_key = headers.get("X-API-Key", headers.get("Authorization", "").replace("Bearer ", ""))
        return api_key

    def xǁDeepseekConnectorǁ_get_api_key__mutmut_19(self) -> str:
        """Extract API key from the auth provider."""
        if not self._auth_provider:
            return ""
        # Try to access _api_key directly (APIKeyAuth)
        api_key = getattr(self._auth_provider, "_api_key", "")
        if api_key:
            return api_key
        # Fallback: use apply_auth and extract from headers
        auth_request: dict[str, Any] = {"headers": {}, "params": {}}
        self._auth_provider.apply_auth(auth_request)
        headers = None
        api_key = headers.get("X-API-Key", headers.get("Authorization", "").replace("Bearer ", ""))
        return api_key

    def xǁDeepseekConnectorǁ_get_api_key__mutmut_20(self) -> str:
        """Extract API key from the auth provider."""
        if not self._auth_provider:
            return ""
        # Try to access _api_key directly (APIKeyAuth)
        api_key = getattr(self._auth_provider, "_api_key", "")
        if api_key:
            return api_key
        # Fallback: use apply_auth and extract from headers
        auth_request: dict[str, Any] = {"headers": {}, "params": {}}
        self._auth_provider.apply_auth(auth_request)
        headers = auth_request.get(None, {})
        api_key = headers.get("X-API-Key", headers.get("Authorization", "").replace("Bearer ", ""))
        return api_key

    def xǁDeepseekConnectorǁ_get_api_key__mutmut_21(self) -> str:
        """Extract API key from the auth provider."""
        if not self._auth_provider:
            return ""
        # Try to access _api_key directly (APIKeyAuth)
        api_key = getattr(self._auth_provider, "_api_key", "")
        if api_key:
            return api_key
        # Fallback: use apply_auth and extract from headers
        auth_request: dict[str, Any] = {"headers": {}, "params": {}}
        self._auth_provider.apply_auth(auth_request)
        headers = auth_request.get("headers", None)
        api_key = headers.get("X-API-Key", headers.get("Authorization", "").replace("Bearer ", ""))
        return api_key

    def xǁDeepseekConnectorǁ_get_api_key__mutmut_22(self) -> str:
        """Extract API key from the auth provider."""
        if not self._auth_provider:
            return ""
        # Try to access _api_key directly (APIKeyAuth)
        api_key = getattr(self._auth_provider, "_api_key", "")
        if api_key:
            return api_key
        # Fallback: use apply_auth and extract from headers
        auth_request: dict[str, Any] = {"headers": {}, "params": {}}
        self._auth_provider.apply_auth(auth_request)
        headers = auth_request.get({})
        api_key = headers.get("X-API-Key", headers.get("Authorization", "").replace("Bearer ", ""))
        return api_key

    def xǁDeepseekConnectorǁ_get_api_key__mutmut_23(self) -> str:
        """Extract API key from the auth provider."""
        if not self._auth_provider:
            return ""
        # Try to access _api_key directly (APIKeyAuth)
        api_key = getattr(self._auth_provider, "_api_key", "")
        if api_key:
            return api_key
        # Fallback: use apply_auth and extract from headers
        auth_request: dict[str, Any] = {"headers": {}, "params": {}}
        self._auth_provider.apply_auth(auth_request)
        headers = auth_request.get("headers", )
        api_key = headers.get("X-API-Key", headers.get("Authorization", "").replace("Bearer ", ""))
        return api_key

    def xǁDeepseekConnectorǁ_get_api_key__mutmut_24(self) -> str:
        """Extract API key from the auth provider."""
        if not self._auth_provider:
            return ""
        # Try to access _api_key directly (APIKeyAuth)
        api_key = getattr(self._auth_provider, "_api_key", "")
        if api_key:
            return api_key
        # Fallback: use apply_auth and extract from headers
        auth_request: dict[str, Any] = {"headers": {}, "params": {}}
        self._auth_provider.apply_auth(auth_request)
        headers = auth_request.get("XXheadersXX", {})
        api_key = headers.get("X-API-Key", headers.get("Authorization", "").replace("Bearer ", ""))
        return api_key

    def xǁDeepseekConnectorǁ_get_api_key__mutmut_25(self) -> str:
        """Extract API key from the auth provider."""
        if not self._auth_provider:
            return ""
        # Try to access _api_key directly (APIKeyAuth)
        api_key = getattr(self._auth_provider, "_api_key", "")
        if api_key:
            return api_key
        # Fallback: use apply_auth and extract from headers
        auth_request: dict[str, Any] = {"headers": {}, "params": {}}
        self._auth_provider.apply_auth(auth_request)
        headers = auth_request.get("HEADERS", {})
        api_key = headers.get("X-API-Key", headers.get("Authorization", "").replace("Bearer ", ""))
        return api_key

    def xǁDeepseekConnectorǁ_get_api_key__mutmut_26(self) -> str:
        """Extract API key from the auth provider."""
        if not self._auth_provider:
            return ""
        # Try to access _api_key directly (APIKeyAuth)
        api_key = getattr(self._auth_provider, "_api_key", "")
        if api_key:
            return api_key
        # Fallback: use apply_auth and extract from headers
        auth_request: dict[str, Any] = {"headers": {}, "params": {}}
        self._auth_provider.apply_auth(auth_request)
        headers = auth_request.get("headers", {})
        api_key = None
        return api_key

    def xǁDeepseekConnectorǁ_get_api_key__mutmut_27(self) -> str:
        """Extract API key from the auth provider."""
        if not self._auth_provider:
            return ""
        # Try to access _api_key directly (APIKeyAuth)
        api_key = getattr(self._auth_provider, "_api_key", "")
        if api_key:
            return api_key
        # Fallback: use apply_auth and extract from headers
        auth_request: dict[str, Any] = {"headers": {}, "params": {}}
        self._auth_provider.apply_auth(auth_request)
        headers = auth_request.get("headers", {})
        api_key = headers.get(None, headers.get("Authorization", "").replace("Bearer ", ""))
        return api_key

    def xǁDeepseekConnectorǁ_get_api_key__mutmut_28(self) -> str:
        """Extract API key from the auth provider."""
        if not self._auth_provider:
            return ""
        # Try to access _api_key directly (APIKeyAuth)
        api_key = getattr(self._auth_provider, "_api_key", "")
        if api_key:
            return api_key
        # Fallback: use apply_auth and extract from headers
        auth_request: dict[str, Any] = {"headers": {}, "params": {}}
        self._auth_provider.apply_auth(auth_request)
        headers = auth_request.get("headers", {})
        api_key = headers.get("X-API-Key", None)
        return api_key

    def xǁDeepseekConnectorǁ_get_api_key__mutmut_29(self) -> str:
        """Extract API key from the auth provider."""
        if not self._auth_provider:
            return ""
        # Try to access _api_key directly (APIKeyAuth)
        api_key = getattr(self._auth_provider, "_api_key", "")
        if api_key:
            return api_key
        # Fallback: use apply_auth and extract from headers
        auth_request: dict[str, Any] = {"headers": {}, "params": {}}
        self._auth_provider.apply_auth(auth_request)
        headers = auth_request.get("headers", {})
        api_key = headers.get(headers.get("Authorization", "").replace("Bearer ", ""))
        return api_key

    def xǁDeepseekConnectorǁ_get_api_key__mutmut_30(self) -> str:
        """Extract API key from the auth provider."""
        if not self._auth_provider:
            return ""
        # Try to access _api_key directly (APIKeyAuth)
        api_key = getattr(self._auth_provider, "_api_key", "")
        if api_key:
            return api_key
        # Fallback: use apply_auth and extract from headers
        auth_request: dict[str, Any] = {"headers": {}, "params": {}}
        self._auth_provider.apply_auth(auth_request)
        headers = auth_request.get("headers", {})
        api_key = headers.get("X-API-Key", )
        return api_key

    def xǁDeepseekConnectorǁ_get_api_key__mutmut_31(self) -> str:
        """Extract API key from the auth provider."""
        if not self._auth_provider:
            return ""
        # Try to access _api_key directly (APIKeyAuth)
        api_key = getattr(self._auth_provider, "_api_key", "")
        if api_key:
            return api_key
        # Fallback: use apply_auth and extract from headers
        auth_request: dict[str, Any] = {"headers": {}, "params": {}}
        self._auth_provider.apply_auth(auth_request)
        headers = auth_request.get("headers", {})
        api_key = headers.get("XXX-API-KeyXX", headers.get("Authorization", "").replace("Bearer ", ""))
        return api_key

    def xǁDeepseekConnectorǁ_get_api_key__mutmut_32(self) -> str:
        """Extract API key from the auth provider."""
        if not self._auth_provider:
            return ""
        # Try to access _api_key directly (APIKeyAuth)
        api_key = getattr(self._auth_provider, "_api_key", "")
        if api_key:
            return api_key
        # Fallback: use apply_auth and extract from headers
        auth_request: dict[str, Any] = {"headers": {}, "params": {}}
        self._auth_provider.apply_auth(auth_request)
        headers = auth_request.get("headers", {})
        api_key = headers.get("x-api-key", headers.get("Authorization", "").replace("Bearer ", ""))
        return api_key

    def xǁDeepseekConnectorǁ_get_api_key__mutmut_33(self) -> str:
        """Extract API key from the auth provider."""
        if not self._auth_provider:
            return ""
        # Try to access _api_key directly (APIKeyAuth)
        api_key = getattr(self._auth_provider, "_api_key", "")
        if api_key:
            return api_key
        # Fallback: use apply_auth and extract from headers
        auth_request: dict[str, Any] = {"headers": {}, "params": {}}
        self._auth_provider.apply_auth(auth_request)
        headers = auth_request.get("headers", {})
        api_key = headers.get("X-API-KEY", headers.get("Authorization", "").replace("Bearer ", ""))
        return api_key

    def xǁDeepseekConnectorǁ_get_api_key__mutmut_34(self) -> str:
        """Extract API key from the auth provider."""
        if not self._auth_provider:
            return ""
        # Try to access _api_key directly (APIKeyAuth)
        api_key = getattr(self._auth_provider, "_api_key", "")
        if api_key:
            return api_key
        # Fallback: use apply_auth and extract from headers
        auth_request: dict[str, Any] = {"headers": {}, "params": {}}
        self._auth_provider.apply_auth(auth_request)
        headers = auth_request.get("headers", {})
        api_key = headers.get("X-API-Key", headers.get("Authorization", "").replace(None, ""))
        return api_key

    def xǁDeepseekConnectorǁ_get_api_key__mutmut_35(self) -> str:
        """Extract API key from the auth provider."""
        if not self._auth_provider:
            return ""
        # Try to access _api_key directly (APIKeyAuth)
        api_key = getattr(self._auth_provider, "_api_key", "")
        if api_key:
            return api_key
        # Fallback: use apply_auth and extract from headers
        auth_request: dict[str, Any] = {"headers": {}, "params": {}}
        self._auth_provider.apply_auth(auth_request)
        headers = auth_request.get("headers", {})
        api_key = headers.get("X-API-Key", headers.get("Authorization", "").replace("Bearer ", None))
        return api_key

    def xǁDeepseekConnectorǁ_get_api_key__mutmut_36(self) -> str:
        """Extract API key from the auth provider."""
        if not self._auth_provider:
            return ""
        # Try to access _api_key directly (APIKeyAuth)
        api_key = getattr(self._auth_provider, "_api_key", "")
        if api_key:
            return api_key
        # Fallback: use apply_auth and extract from headers
        auth_request: dict[str, Any] = {"headers": {}, "params": {}}
        self._auth_provider.apply_auth(auth_request)
        headers = auth_request.get("headers", {})
        api_key = headers.get("X-API-Key", headers.get("Authorization", "").replace(""))
        return api_key

    def xǁDeepseekConnectorǁ_get_api_key__mutmut_37(self) -> str:
        """Extract API key from the auth provider."""
        if not self._auth_provider:
            return ""
        # Try to access _api_key directly (APIKeyAuth)
        api_key = getattr(self._auth_provider, "_api_key", "")
        if api_key:
            return api_key
        # Fallback: use apply_auth and extract from headers
        auth_request: dict[str, Any] = {"headers": {}, "params": {}}
        self._auth_provider.apply_auth(auth_request)
        headers = auth_request.get("headers", {})
        api_key = headers.get("X-API-Key", headers.get("Authorization", "").replace("Bearer ", ))
        return api_key

    def xǁDeepseekConnectorǁ_get_api_key__mutmut_38(self) -> str:
        """Extract API key from the auth provider."""
        if not self._auth_provider:
            return ""
        # Try to access _api_key directly (APIKeyAuth)
        api_key = getattr(self._auth_provider, "_api_key", "")
        if api_key:
            return api_key
        # Fallback: use apply_auth and extract from headers
        auth_request: dict[str, Any] = {"headers": {}, "params": {}}
        self._auth_provider.apply_auth(auth_request)
        headers = auth_request.get("headers", {})
        api_key = headers.get("X-API-Key", headers.get(None, "").replace("Bearer ", ""))
        return api_key

    def xǁDeepseekConnectorǁ_get_api_key__mutmut_39(self) -> str:
        """Extract API key from the auth provider."""
        if not self._auth_provider:
            return ""
        # Try to access _api_key directly (APIKeyAuth)
        api_key = getattr(self._auth_provider, "_api_key", "")
        if api_key:
            return api_key
        # Fallback: use apply_auth and extract from headers
        auth_request: dict[str, Any] = {"headers": {}, "params": {}}
        self._auth_provider.apply_auth(auth_request)
        headers = auth_request.get("headers", {})
        api_key = headers.get("X-API-Key", headers.get("Authorization", None).replace("Bearer ", ""))
        return api_key

    def xǁDeepseekConnectorǁ_get_api_key__mutmut_40(self) -> str:
        """Extract API key from the auth provider."""
        if not self._auth_provider:
            return ""
        # Try to access _api_key directly (APIKeyAuth)
        api_key = getattr(self._auth_provider, "_api_key", "")
        if api_key:
            return api_key
        # Fallback: use apply_auth and extract from headers
        auth_request: dict[str, Any] = {"headers": {}, "params": {}}
        self._auth_provider.apply_auth(auth_request)
        headers = auth_request.get("headers", {})
        api_key = headers.get("X-API-Key", headers.get("").replace("Bearer ", ""))
        return api_key

    def xǁDeepseekConnectorǁ_get_api_key__mutmut_41(self) -> str:
        """Extract API key from the auth provider."""
        if not self._auth_provider:
            return ""
        # Try to access _api_key directly (APIKeyAuth)
        api_key = getattr(self._auth_provider, "_api_key", "")
        if api_key:
            return api_key
        # Fallback: use apply_auth and extract from headers
        auth_request: dict[str, Any] = {"headers": {}, "params": {}}
        self._auth_provider.apply_auth(auth_request)
        headers = auth_request.get("headers", {})
        api_key = headers.get("X-API-Key", headers.get("Authorization", ).replace("Bearer ", ""))
        return api_key

    def xǁDeepseekConnectorǁ_get_api_key__mutmut_42(self) -> str:
        """Extract API key from the auth provider."""
        if not self._auth_provider:
            return ""
        # Try to access _api_key directly (APIKeyAuth)
        api_key = getattr(self._auth_provider, "_api_key", "")
        if api_key:
            return api_key
        # Fallback: use apply_auth and extract from headers
        auth_request: dict[str, Any] = {"headers": {}, "params": {}}
        self._auth_provider.apply_auth(auth_request)
        headers = auth_request.get("headers", {})
        api_key = headers.get("X-API-Key", headers.get("XXAuthorizationXX", "").replace("Bearer ", ""))
        return api_key

    def xǁDeepseekConnectorǁ_get_api_key__mutmut_43(self) -> str:
        """Extract API key from the auth provider."""
        if not self._auth_provider:
            return ""
        # Try to access _api_key directly (APIKeyAuth)
        api_key = getattr(self._auth_provider, "_api_key", "")
        if api_key:
            return api_key
        # Fallback: use apply_auth and extract from headers
        auth_request: dict[str, Any] = {"headers": {}, "params": {}}
        self._auth_provider.apply_auth(auth_request)
        headers = auth_request.get("headers", {})
        api_key = headers.get("X-API-Key", headers.get("authorization", "").replace("Bearer ", ""))
        return api_key

    def xǁDeepseekConnectorǁ_get_api_key__mutmut_44(self) -> str:
        """Extract API key from the auth provider."""
        if not self._auth_provider:
            return ""
        # Try to access _api_key directly (APIKeyAuth)
        api_key = getattr(self._auth_provider, "_api_key", "")
        if api_key:
            return api_key
        # Fallback: use apply_auth and extract from headers
        auth_request: dict[str, Any] = {"headers": {}, "params": {}}
        self._auth_provider.apply_auth(auth_request)
        headers = auth_request.get("headers", {})
        api_key = headers.get("X-API-Key", headers.get("AUTHORIZATION", "").replace("Bearer ", ""))
        return api_key

    def xǁDeepseekConnectorǁ_get_api_key__mutmut_45(self) -> str:
        """Extract API key from the auth provider."""
        if not self._auth_provider:
            return ""
        # Try to access _api_key directly (APIKeyAuth)
        api_key = getattr(self._auth_provider, "_api_key", "")
        if api_key:
            return api_key
        # Fallback: use apply_auth and extract from headers
        auth_request: dict[str, Any] = {"headers": {}, "params": {}}
        self._auth_provider.apply_auth(auth_request)
        headers = auth_request.get("headers", {})
        api_key = headers.get("X-API-Key", headers.get("Authorization", "XXXX").replace("Bearer ", ""))
        return api_key

    def xǁDeepseekConnectorǁ_get_api_key__mutmut_46(self) -> str:
        """Extract API key from the auth provider."""
        if not self._auth_provider:
            return ""
        # Try to access _api_key directly (APIKeyAuth)
        api_key = getattr(self._auth_provider, "_api_key", "")
        if api_key:
            return api_key
        # Fallback: use apply_auth and extract from headers
        auth_request: dict[str, Any] = {"headers": {}, "params": {}}
        self._auth_provider.apply_auth(auth_request)
        headers = auth_request.get("headers", {})
        api_key = headers.get("X-API-Key", headers.get("Authorization", "").replace("XXBearer XX", ""))
        return api_key

    def xǁDeepseekConnectorǁ_get_api_key__mutmut_47(self) -> str:
        """Extract API key from the auth provider."""
        if not self._auth_provider:
            return ""
        # Try to access _api_key directly (APIKeyAuth)
        api_key = getattr(self._auth_provider, "_api_key", "")
        if api_key:
            return api_key
        # Fallback: use apply_auth and extract from headers
        auth_request: dict[str, Any] = {"headers": {}, "params": {}}
        self._auth_provider.apply_auth(auth_request)
        headers = auth_request.get("headers", {})
        api_key = headers.get("X-API-Key", headers.get("Authorization", "").replace("bearer ", ""))
        return api_key

    def xǁDeepseekConnectorǁ_get_api_key__mutmut_48(self) -> str:
        """Extract API key from the auth provider."""
        if not self._auth_provider:
            return ""
        # Try to access _api_key directly (APIKeyAuth)
        api_key = getattr(self._auth_provider, "_api_key", "")
        if api_key:
            return api_key
        # Fallback: use apply_auth and extract from headers
        auth_request: dict[str, Any] = {"headers": {}, "params": {}}
        self._auth_provider.apply_auth(auth_request)
        headers = auth_request.get("headers", {})
        api_key = headers.get("X-API-Key", headers.get("Authorization", "").replace("BEARER ", ""))
        return api_key

    def xǁDeepseekConnectorǁ_get_api_key__mutmut_49(self) -> str:
        """Extract API key from the auth provider."""
        if not self._auth_provider:
            return ""
        # Try to access _api_key directly (APIKeyAuth)
        api_key = getattr(self._auth_provider, "_api_key", "")
        if api_key:
            return api_key
        # Fallback: use apply_auth and extract from headers
        auth_request: dict[str, Any] = {"headers": {}, "params": {}}
        self._auth_provider.apply_auth(auth_request)
        headers = auth_request.get("headers", {})
        api_key = headers.get("X-API-Key", headers.get("Authorization", "").replace("Bearer ", "XXXX"))
        return api_key

    @_mutmut_mutated(mutants_xǁDeepseekConnectorǁconnect__mutmut)
    def connect(self) -> bool:
        """Establece conexion con la API de DeepSeek."""
        if not self._auth_provider or not self._auth_provider.validate():
            logger.error("DeepseekConnector: API Key no configurada")
            return False

        api_key = self._get_api_key()
        if not api_key:
            logger.error("DeepseekConnector: No se pudo extraer la API Key del auth provider")
            return False

        self._http = HttpClient(
            base_url=self._base_url,
            connector_name=self.name,
        )
        self._http.set_auth("Bearer", token=api_key)

        self._connected = True
        self._log_operation("connect", "API Key configurada, HttpClient inicializado")
        return True

    def xǁDeepseekConnectorǁconnect__mutmut_orig(self) -> bool:
        """Establece conexion con la API de DeepSeek."""
        if not self._auth_provider or not self._auth_provider.validate():
            logger.error("DeepseekConnector: API Key no configurada")
            return False

        api_key = self._get_api_key()
        if not api_key:
            logger.error("DeepseekConnector: No se pudo extraer la API Key del auth provider")
            return False

        self._http = HttpClient(
            base_url=self._base_url,
            connector_name=self.name,
        )
        self._http.set_auth("Bearer", token=api_key)

        self._connected = True
        self._log_operation("connect", "API Key configurada, HttpClient inicializado")
        return True

    def xǁDeepseekConnectorǁconnect__mutmut_1(self) -> bool:
        """Establece conexion con la API de DeepSeek."""
        if not self._auth_provider and not self._auth_provider.validate():
            logger.error("DeepseekConnector: API Key no configurada")
            return False

        api_key = self._get_api_key()
        if not api_key:
            logger.error("DeepseekConnector: No se pudo extraer la API Key del auth provider")
            return False

        self._http = HttpClient(
            base_url=self._base_url,
            connector_name=self.name,
        )
        self._http.set_auth("Bearer", token=api_key)

        self._connected = True
        self._log_operation("connect", "API Key configurada, HttpClient inicializado")
        return True

    def xǁDeepseekConnectorǁconnect__mutmut_2(self) -> bool:
        """Establece conexion con la API de DeepSeek."""
        if self._auth_provider or not self._auth_provider.validate():
            logger.error("DeepseekConnector: API Key no configurada")
            return False

        api_key = self._get_api_key()
        if not api_key:
            logger.error("DeepseekConnector: No se pudo extraer la API Key del auth provider")
            return False

        self._http = HttpClient(
            base_url=self._base_url,
            connector_name=self.name,
        )
        self._http.set_auth("Bearer", token=api_key)

        self._connected = True
        self._log_operation("connect", "API Key configurada, HttpClient inicializado")
        return True

    def xǁDeepseekConnectorǁconnect__mutmut_3(self) -> bool:
        """Establece conexion con la API de DeepSeek."""
        if not self._auth_provider or self._auth_provider.validate():
            logger.error("DeepseekConnector: API Key no configurada")
            return False

        api_key = self._get_api_key()
        if not api_key:
            logger.error("DeepseekConnector: No se pudo extraer la API Key del auth provider")
            return False

        self._http = HttpClient(
            base_url=self._base_url,
            connector_name=self.name,
        )
        self._http.set_auth("Bearer", token=api_key)

        self._connected = True
        self._log_operation("connect", "API Key configurada, HttpClient inicializado")
        return True

    def xǁDeepseekConnectorǁconnect__mutmut_4(self) -> bool:
        """Establece conexion con la API de DeepSeek."""
        if not self._auth_provider or not self._auth_provider.validate():
            logger.error(None)
            return False

        api_key = self._get_api_key()
        if not api_key:
            logger.error("DeepseekConnector: No se pudo extraer la API Key del auth provider")
            return False

        self._http = HttpClient(
            base_url=self._base_url,
            connector_name=self.name,
        )
        self._http.set_auth("Bearer", token=api_key)

        self._connected = True
        self._log_operation("connect", "API Key configurada, HttpClient inicializado")
        return True

    def xǁDeepseekConnectorǁconnect__mutmut_5(self) -> bool:
        """Establece conexion con la API de DeepSeek."""
        if not self._auth_provider or not self._auth_provider.validate():
            logger.error("XXDeepseekConnector: API Key no configuradaXX")
            return False

        api_key = self._get_api_key()
        if not api_key:
            logger.error("DeepseekConnector: No se pudo extraer la API Key del auth provider")
            return False

        self._http = HttpClient(
            base_url=self._base_url,
            connector_name=self.name,
        )
        self._http.set_auth("Bearer", token=api_key)

        self._connected = True
        self._log_operation("connect", "API Key configurada, HttpClient inicializado")
        return True

    def xǁDeepseekConnectorǁconnect__mutmut_6(self) -> bool:
        """Establece conexion con la API de DeepSeek."""
        if not self._auth_provider or not self._auth_provider.validate():
            logger.error("deepseekconnector: api key no configurada")
            return False

        api_key = self._get_api_key()
        if not api_key:
            logger.error("DeepseekConnector: No se pudo extraer la API Key del auth provider")
            return False

        self._http = HttpClient(
            base_url=self._base_url,
            connector_name=self.name,
        )
        self._http.set_auth("Bearer", token=api_key)

        self._connected = True
        self._log_operation("connect", "API Key configurada, HttpClient inicializado")
        return True

    def xǁDeepseekConnectorǁconnect__mutmut_7(self) -> bool:
        """Establece conexion con la API de DeepSeek."""
        if not self._auth_provider or not self._auth_provider.validate():
            logger.error("DEEPSEEKCONNECTOR: API KEY NO CONFIGURADA")
            return False

        api_key = self._get_api_key()
        if not api_key:
            logger.error("DeepseekConnector: No se pudo extraer la API Key del auth provider")
            return False

        self._http = HttpClient(
            base_url=self._base_url,
            connector_name=self.name,
        )
        self._http.set_auth("Bearer", token=api_key)

        self._connected = True
        self._log_operation("connect", "API Key configurada, HttpClient inicializado")
        return True

    def xǁDeepseekConnectorǁconnect__mutmut_8(self) -> bool:
        """Establece conexion con la API de DeepSeek."""
        if not self._auth_provider or not self._auth_provider.validate():
            logger.error("DeepseekConnector: API Key no configurada")
            return True

        api_key = self._get_api_key()
        if not api_key:
            logger.error("DeepseekConnector: No se pudo extraer la API Key del auth provider")
            return False

        self._http = HttpClient(
            base_url=self._base_url,
            connector_name=self.name,
        )
        self._http.set_auth("Bearer", token=api_key)

        self._connected = True
        self._log_operation("connect", "API Key configurada, HttpClient inicializado")
        return True

    def xǁDeepseekConnectorǁconnect__mutmut_9(self) -> bool:
        """Establece conexion con la API de DeepSeek."""
        if not self._auth_provider or not self._auth_provider.validate():
            logger.error("DeepseekConnector: API Key no configurada")
            return False

        api_key = None
        if not api_key:
            logger.error("DeepseekConnector: No se pudo extraer la API Key del auth provider")
            return False

        self._http = HttpClient(
            base_url=self._base_url,
            connector_name=self.name,
        )
        self._http.set_auth("Bearer", token=api_key)

        self._connected = True
        self._log_operation("connect", "API Key configurada, HttpClient inicializado")
        return True

    def xǁDeepseekConnectorǁconnect__mutmut_10(self) -> bool:
        """Establece conexion con la API de DeepSeek."""
        if not self._auth_provider or not self._auth_provider.validate():
            logger.error("DeepseekConnector: API Key no configurada")
            return False

        api_key = self._get_api_key()
        if api_key:
            logger.error("DeepseekConnector: No se pudo extraer la API Key del auth provider")
            return False

        self._http = HttpClient(
            base_url=self._base_url,
            connector_name=self.name,
        )
        self._http.set_auth("Bearer", token=api_key)

        self._connected = True
        self._log_operation("connect", "API Key configurada, HttpClient inicializado")
        return True

    def xǁDeepseekConnectorǁconnect__mutmut_11(self) -> bool:
        """Establece conexion con la API de DeepSeek."""
        if not self._auth_provider or not self._auth_provider.validate():
            logger.error("DeepseekConnector: API Key no configurada")
            return False

        api_key = self._get_api_key()
        if not api_key:
            logger.error(None)
            return False

        self._http = HttpClient(
            base_url=self._base_url,
            connector_name=self.name,
        )
        self._http.set_auth("Bearer", token=api_key)

        self._connected = True
        self._log_operation("connect", "API Key configurada, HttpClient inicializado")
        return True

    def xǁDeepseekConnectorǁconnect__mutmut_12(self) -> bool:
        """Establece conexion con la API de DeepSeek."""
        if not self._auth_provider or not self._auth_provider.validate():
            logger.error("DeepseekConnector: API Key no configurada")
            return False

        api_key = self._get_api_key()
        if not api_key:
            logger.error("XXDeepseekConnector: No se pudo extraer la API Key del auth providerXX")
            return False

        self._http = HttpClient(
            base_url=self._base_url,
            connector_name=self.name,
        )
        self._http.set_auth("Bearer", token=api_key)

        self._connected = True
        self._log_operation("connect", "API Key configurada, HttpClient inicializado")
        return True

    def xǁDeepseekConnectorǁconnect__mutmut_13(self) -> bool:
        """Establece conexion con la API de DeepSeek."""
        if not self._auth_provider or not self._auth_provider.validate():
            logger.error("DeepseekConnector: API Key no configurada")
            return False

        api_key = self._get_api_key()
        if not api_key:
            logger.error("deepseekconnector: no se pudo extraer la api key del auth provider")
            return False

        self._http = HttpClient(
            base_url=self._base_url,
            connector_name=self.name,
        )
        self._http.set_auth("Bearer", token=api_key)

        self._connected = True
        self._log_operation("connect", "API Key configurada, HttpClient inicializado")
        return True

    def xǁDeepseekConnectorǁconnect__mutmut_14(self) -> bool:
        """Establece conexion con la API de DeepSeek."""
        if not self._auth_provider or not self._auth_provider.validate():
            logger.error("DeepseekConnector: API Key no configurada")
            return False

        api_key = self._get_api_key()
        if not api_key:
            logger.error("DEEPSEEKCONNECTOR: NO SE PUDO EXTRAER LA API KEY DEL AUTH PROVIDER")
            return False

        self._http = HttpClient(
            base_url=self._base_url,
            connector_name=self.name,
        )
        self._http.set_auth("Bearer", token=api_key)

        self._connected = True
        self._log_operation("connect", "API Key configurada, HttpClient inicializado")
        return True

    def xǁDeepseekConnectorǁconnect__mutmut_15(self) -> bool:
        """Establece conexion con la API de DeepSeek."""
        if not self._auth_provider or not self._auth_provider.validate():
            logger.error("DeepseekConnector: API Key no configurada")
            return False

        api_key = self._get_api_key()
        if not api_key:
            logger.error("DeepseekConnector: No se pudo extraer la API Key del auth provider")
            return True

        self._http = HttpClient(
            base_url=self._base_url,
            connector_name=self.name,
        )
        self._http.set_auth("Bearer", token=api_key)

        self._connected = True
        self._log_operation("connect", "API Key configurada, HttpClient inicializado")
        return True

    def xǁDeepseekConnectorǁconnect__mutmut_16(self) -> bool:
        """Establece conexion con la API de DeepSeek."""
        if not self._auth_provider or not self._auth_provider.validate():
            logger.error("DeepseekConnector: API Key no configurada")
            return False

        api_key = self._get_api_key()
        if not api_key:
            logger.error("DeepseekConnector: No se pudo extraer la API Key del auth provider")
            return False

        self._http = None
        self._http.set_auth("Bearer", token=api_key)

        self._connected = True
        self._log_operation("connect", "API Key configurada, HttpClient inicializado")
        return True

    def xǁDeepseekConnectorǁconnect__mutmut_17(self) -> bool:
        """Establece conexion con la API de DeepSeek."""
        if not self._auth_provider or not self._auth_provider.validate():
            logger.error("DeepseekConnector: API Key no configurada")
            return False

        api_key = self._get_api_key()
        if not api_key:
            logger.error("DeepseekConnector: No se pudo extraer la API Key del auth provider")
            return False

        self._http = HttpClient(
            base_url=None,
            connector_name=self.name,
        )
        self._http.set_auth("Bearer", token=api_key)

        self._connected = True
        self._log_operation("connect", "API Key configurada, HttpClient inicializado")
        return True

    def xǁDeepseekConnectorǁconnect__mutmut_18(self) -> bool:
        """Establece conexion con la API de DeepSeek."""
        if not self._auth_provider or not self._auth_provider.validate():
            logger.error("DeepseekConnector: API Key no configurada")
            return False

        api_key = self._get_api_key()
        if not api_key:
            logger.error("DeepseekConnector: No se pudo extraer la API Key del auth provider")
            return False

        self._http = HttpClient(
            base_url=self._base_url,
            connector_name=None,
        )
        self._http.set_auth("Bearer", token=api_key)

        self._connected = True
        self._log_operation("connect", "API Key configurada, HttpClient inicializado")
        return True

    def xǁDeepseekConnectorǁconnect__mutmut_19(self) -> bool:
        """Establece conexion con la API de DeepSeek."""
        if not self._auth_provider or not self._auth_provider.validate():
            logger.error("DeepseekConnector: API Key no configurada")
            return False

        api_key = self._get_api_key()
        if not api_key:
            logger.error("DeepseekConnector: No se pudo extraer la API Key del auth provider")
            return False

        self._http = HttpClient(
            connector_name=self.name,
        )
        self._http.set_auth("Bearer", token=api_key)

        self._connected = True
        self._log_operation("connect", "API Key configurada, HttpClient inicializado")
        return True

    def xǁDeepseekConnectorǁconnect__mutmut_20(self) -> bool:
        """Establece conexion con la API de DeepSeek."""
        if not self._auth_provider or not self._auth_provider.validate():
            logger.error("DeepseekConnector: API Key no configurada")
            return False

        api_key = self._get_api_key()
        if not api_key:
            logger.error("DeepseekConnector: No se pudo extraer la API Key del auth provider")
            return False

        self._http = HttpClient(
            base_url=self._base_url,
            )
        self._http.set_auth("Bearer", token=api_key)

        self._connected = True
        self._log_operation("connect", "API Key configurada, HttpClient inicializado")
        return True

    def xǁDeepseekConnectorǁconnect__mutmut_21(self) -> bool:
        """Establece conexion con la API de DeepSeek."""
        if not self._auth_provider or not self._auth_provider.validate():
            logger.error("DeepseekConnector: API Key no configurada")
            return False

        api_key = self._get_api_key()
        if not api_key:
            logger.error("DeepseekConnector: No se pudo extraer la API Key del auth provider")
            return False

        self._http = HttpClient(
            base_url=self._base_url,
            connector_name=self.name,
        )
        self._http.set_auth(None, token=api_key)

        self._connected = True
        self._log_operation("connect", "API Key configurada, HttpClient inicializado")
        return True

    def xǁDeepseekConnectorǁconnect__mutmut_22(self) -> bool:
        """Establece conexion con la API de DeepSeek."""
        if not self._auth_provider or not self._auth_provider.validate():
            logger.error("DeepseekConnector: API Key no configurada")
            return False

        api_key = self._get_api_key()
        if not api_key:
            logger.error("DeepseekConnector: No se pudo extraer la API Key del auth provider")
            return False

        self._http = HttpClient(
            base_url=self._base_url,
            connector_name=self.name,
        )
        self._http.set_auth("Bearer", token=None)

        self._connected = True
        self._log_operation("connect", "API Key configurada, HttpClient inicializado")
        return True

    def xǁDeepseekConnectorǁconnect__mutmut_23(self) -> bool:
        """Establece conexion con la API de DeepSeek."""
        if not self._auth_provider or not self._auth_provider.validate():
            logger.error("DeepseekConnector: API Key no configurada")
            return False

        api_key = self._get_api_key()
        if not api_key:
            logger.error("DeepseekConnector: No se pudo extraer la API Key del auth provider")
            return False

        self._http = HttpClient(
            base_url=self._base_url,
            connector_name=self.name,
        )
        self._http.set_auth(token=api_key)

        self._connected = True
        self._log_operation("connect", "API Key configurada, HttpClient inicializado")
        return True

    def xǁDeepseekConnectorǁconnect__mutmut_24(self) -> bool:
        """Establece conexion con la API de DeepSeek."""
        if not self._auth_provider or not self._auth_provider.validate():
            logger.error("DeepseekConnector: API Key no configurada")
            return False

        api_key = self._get_api_key()
        if not api_key:
            logger.error("DeepseekConnector: No se pudo extraer la API Key del auth provider")
            return False

        self._http = HttpClient(
            base_url=self._base_url,
            connector_name=self.name,
        )
        self._http.set_auth("Bearer", )

        self._connected = True
        self._log_operation("connect", "API Key configurada, HttpClient inicializado")
        return True

    def xǁDeepseekConnectorǁconnect__mutmut_25(self) -> bool:
        """Establece conexion con la API de DeepSeek."""
        if not self._auth_provider or not self._auth_provider.validate():
            logger.error("DeepseekConnector: API Key no configurada")
            return False

        api_key = self._get_api_key()
        if not api_key:
            logger.error("DeepseekConnector: No se pudo extraer la API Key del auth provider")
            return False

        self._http = HttpClient(
            base_url=self._base_url,
            connector_name=self.name,
        )
        self._http.set_auth("XXBearerXX", token=api_key)

        self._connected = True
        self._log_operation("connect", "API Key configurada, HttpClient inicializado")
        return True

    def xǁDeepseekConnectorǁconnect__mutmut_26(self) -> bool:
        """Establece conexion con la API de DeepSeek."""
        if not self._auth_provider or not self._auth_provider.validate():
            logger.error("DeepseekConnector: API Key no configurada")
            return False

        api_key = self._get_api_key()
        if not api_key:
            logger.error("DeepseekConnector: No se pudo extraer la API Key del auth provider")
            return False

        self._http = HttpClient(
            base_url=self._base_url,
            connector_name=self.name,
        )
        self._http.set_auth("bearer", token=api_key)

        self._connected = True
        self._log_operation("connect", "API Key configurada, HttpClient inicializado")
        return True

    def xǁDeepseekConnectorǁconnect__mutmut_27(self) -> bool:
        """Establece conexion con la API de DeepSeek."""
        if not self._auth_provider or not self._auth_provider.validate():
            logger.error("DeepseekConnector: API Key no configurada")
            return False

        api_key = self._get_api_key()
        if not api_key:
            logger.error("DeepseekConnector: No se pudo extraer la API Key del auth provider")
            return False

        self._http = HttpClient(
            base_url=self._base_url,
            connector_name=self.name,
        )
        self._http.set_auth("BEARER", token=api_key)

        self._connected = True
        self._log_operation("connect", "API Key configurada, HttpClient inicializado")
        return True

    def xǁDeepseekConnectorǁconnect__mutmut_28(self) -> bool:
        """Establece conexion con la API de DeepSeek."""
        if not self._auth_provider or not self._auth_provider.validate():
            logger.error("DeepseekConnector: API Key no configurada")
            return False

        api_key = self._get_api_key()
        if not api_key:
            logger.error("DeepseekConnector: No se pudo extraer la API Key del auth provider")
            return False

        self._http = HttpClient(
            base_url=self._base_url,
            connector_name=self.name,
        )
        self._http.set_auth("Bearer", token=api_key)

        self._connected = None
        self._log_operation("connect", "API Key configurada, HttpClient inicializado")
        return True

    def xǁDeepseekConnectorǁconnect__mutmut_29(self) -> bool:
        """Establece conexion con la API de DeepSeek."""
        if not self._auth_provider or not self._auth_provider.validate():
            logger.error("DeepseekConnector: API Key no configurada")
            return False

        api_key = self._get_api_key()
        if not api_key:
            logger.error("DeepseekConnector: No se pudo extraer la API Key del auth provider")
            return False

        self._http = HttpClient(
            base_url=self._base_url,
            connector_name=self.name,
        )
        self._http.set_auth("Bearer", token=api_key)

        self._connected = False
        self._log_operation("connect", "API Key configurada, HttpClient inicializado")
        return True

    def xǁDeepseekConnectorǁconnect__mutmut_30(self) -> bool:
        """Establece conexion con la API de DeepSeek."""
        if not self._auth_provider or not self._auth_provider.validate():
            logger.error("DeepseekConnector: API Key no configurada")
            return False

        api_key = self._get_api_key()
        if not api_key:
            logger.error("DeepseekConnector: No se pudo extraer la API Key del auth provider")
            return False

        self._http = HttpClient(
            base_url=self._base_url,
            connector_name=self.name,
        )
        self._http.set_auth("Bearer", token=api_key)

        self._connected = True
        self._log_operation(None, "API Key configurada, HttpClient inicializado")
        return True

    def xǁDeepseekConnectorǁconnect__mutmut_31(self) -> bool:
        """Establece conexion con la API de DeepSeek."""
        if not self._auth_provider or not self._auth_provider.validate():
            logger.error("DeepseekConnector: API Key no configurada")
            return False

        api_key = self._get_api_key()
        if not api_key:
            logger.error("DeepseekConnector: No se pudo extraer la API Key del auth provider")
            return False

        self._http = HttpClient(
            base_url=self._base_url,
            connector_name=self.name,
        )
        self._http.set_auth("Bearer", token=api_key)

        self._connected = True
        self._log_operation("connect", None)
        return True

    def xǁDeepseekConnectorǁconnect__mutmut_32(self) -> bool:
        """Establece conexion con la API de DeepSeek."""
        if not self._auth_provider or not self._auth_provider.validate():
            logger.error("DeepseekConnector: API Key no configurada")
            return False

        api_key = self._get_api_key()
        if not api_key:
            logger.error("DeepseekConnector: No se pudo extraer la API Key del auth provider")
            return False

        self._http = HttpClient(
            base_url=self._base_url,
            connector_name=self.name,
        )
        self._http.set_auth("Bearer", token=api_key)

        self._connected = True
        self._log_operation("API Key configurada, HttpClient inicializado")
        return True

    def xǁDeepseekConnectorǁconnect__mutmut_33(self) -> bool:
        """Establece conexion con la API de DeepSeek."""
        if not self._auth_provider or not self._auth_provider.validate():
            logger.error("DeepseekConnector: API Key no configurada")
            return False

        api_key = self._get_api_key()
        if not api_key:
            logger.error("DeepseekConnector: No se pudo extraer la API Key del auth provider")
            return False

        self._http = HttpClient(
            base_url=self._base_url,
            connector_name=self.name,
        )
        self._http.set_auth("Bearer", token=api_key)

        self._connected = True
        self._log_operation("connect", )
        return True

    def xǁDeepseekConnectorǁconnect__mutmut_34(self) -> bool:
        """Establece conexion con la API de DeepSeek."""
        if not self._auth_provider or not self._auth_provider.validate():
            logger.error("DeepseekConnector: API Key no configurada")
            return False

        api_key = self._get_api_key()
        if not api_key:
            logger.error("DeepseekConnector: No se pudo extraer la API Key del auth provider")
            return False

        self._http = HttpClient(
            base_url=self._base_url,
            connector_name=self.name,
        )
        self._http.set_auth("Bearer", token=api_key)

        self._connected = True
        self._log_operation("XXconnectXX", "API Key configurada, HttpClient inicializado")
        return True

    def xǁDeepseekConnectorǁconnect__mutmut_35(self) -> bool:
        """Establece conexion con la API de DeepSeek."""
        if not self._auth_provider or not self._auth_provider.validate():
            logger.error("DeepseekConnector: API Key no configurada")
            return False

        api_key = self._get_api_key()
        if not api_key:
            logger.error("DeepseekConnector: No se pudo extraer la API Key del auth provider")
            return False

        self._http = HttpClient(
            base_url=self._base_url,
            connector_name=self.name,
        )
        self._http.set_auth("Bearer", token=api_key)

        self._connected = True
        self._log_operation("CONNECT", "API Key configurada, HttpClient inicializado")
        return True

    def xǁDeepseekConnectorǁconnect__mutmut_36(self) -> bool:
        """Establece conexion con la API de DeepSeek."""
        if not self._auth_provider or not self._auth_provider.validate():
            logger.error("DeepseekConnector: API Key no configurada")
            return False

        api_key = self._get_api_key()
        if not api_key:
            logger.error("DeepseekConnector: No se pudo extraer la API Key del auth provider")
            return False

        self._http = HttpClient(
            base_url=self._base_url,
            connector_name=self.name,
        )
        self._http.set_auth("Bearer", token=api_key)

        self._connected = True
        self._log_operation("connect", "XXAPI Key configurada, HttpClient inicializadoXX")
        return True

    def xǁDeepseekConnectorǁconnect__mutmut_37(self) -> bool:
        """Establece conexion con la API de DeepSeek."""
        if not self._auth_provider or not self._auth_provider.validate():
            logger.error("DeepseekConnector: API Key no configurada")
            return False

        api_key = self._get_api_key()
        if not api_key:
            logger.error("DeepseekConnector: No se pudo extraer la API Key del auth provider")
            return False

        self._http = HttpClient(
            base_url=self._base_url,
            connector_name=self.name,
        )
        self._http.set_auth("Bearer", token=api_key)

        self._connected = True
        self._log_operation("connect", "api key configurada, httpclient inicializado")
        return True

    def xǁDeepseekConnectorǁconnect__mutmut_38(self) -> bool:
        """Establece conexion con la API de DeepSeek."""
        if not self._auth_provider or not self._auth_provider.validate():
            logger.error("DeepseekConnector: API Key no configurada")
            return False

        api_key = self._get_api_key()
        if not api_key:
            logger.error("DeepseekConnector: No se pudo extraer la API Key del auth provider")
            return False

        self._http = HttpClient(
            base_url=self._base_url,
            connector_name=self.name,
        )
        self._http.set_auth("Bearer", token=api_key)

        self._connected = True
        self._log_operation("connect", "API KEY CONFIGURADA, HTTPCLIENT INICIALIZADO")
        return True

    def xǁDeepseekConnectorǁconnect__mutmut_39(self) -> bool:
        """Establece conexion con la API de DeepSeek."""
        if not self._auth_provider or not self._auth_provider.validate():
            logger.error("DeepseekConnector: API Key no configurada")
            return False

        api_key = self._get_api_key()
        if not api_key:
            logger.error("DeepseekConnector: No se pudo extraer la API Key del auth provider")
            return False

        self._http = HttpClient(
            base_url=self._base_url,
            connector_name=self.name,
        )
        self._http.set_auth("Bearer", token=api_key)

        self._connected = True
        self._log_operation("connect", "API Key configurada, HttpClient inicializado")
        return False

    @_mutmut_mutated(mutants_xǁDeepseekConnectorǁexecute__mutmut)
    def execute(self, action: str, params: dict[str, Any]) -> Any:
        """Ejecuta una accion del conector DeepSeek.

        Args:
            action: Nombre de la accion a ejecutar
            params: Parametros de la accion
        """
        action_map: dict[str, Any] = {
            "chat_completion": self._chat_completion,
            "reasoning_completion": self._reasoning_completion,
            "code_completion": self._code_completion,
            "list_models": self._list_models,
        }
        handler = action_map.get(action)
        if handler is None:
            return {"error": f"Accion '{action}' no soportada", "available": list(action_map.keys())}
        return handler(params)

    def xǁDeepseekConnectorǁexecute__mutmut_orig(self, action: str, params: dict[str, Any]) -> Any:
        """Ejecuta una accion del conector DeepSeek.

        Args:
            action: Nombre de la accion a ejecutar
            params: Parametros de la accion
        """
        action_map: dict[str, Any] = {
            "chat_completion": self._chat_completion,
            "reasoning_completion": self._reasoning_completion,
            "code_completion": self._code_completion,
            "list_models": self._list_models,
        }
        handler = action_map.get(action)
        if handler is None:
            return {"error": f"Accion '{action}' no soportada", "available": list(action_map.keys())}
        return handler(params)

    def xǁDeepseekConnectorǁexecute__mutmut_1(self, action: str, params: dict[str, Any]) -> Any:
        """Ejecuta una accion del conector DeepSeek.

        Args:
            action: Nombre de la accion a ejecutar
            params: Parametros de la accion
        """
        action_map: dict[str, Any] = None
        handler = action_map.get(action)
        if handler is None:
            return {"error": f"Accion '{action}' no soportada", "available": list(action_map.keys())}
        return handler(params)

    def xǁDeepseekConnectorǁexecute__mutmut_2(self, action: str, params: dict[str, Any]) -> Any:
        """Ejecuta una accion del conector DeepSeek.

        Args:
            action: Nombre de la accion a ejecutar
            params: Parametros de la accion
        """
        action_map: dict[str, Any] = {
            "XXchat_completionXX": self._chat_completion,
            "reasoning_completion": self._reasoning_completion,
            "code_completion": self._code_completion,
            "list_models": self._list_models,
        }
        handler = action_map.get(action)
        if handler is None:
            return {"error": f"Accion '{action}' no soportada", "available": list(action_map.keys())}
        return handler(params)

    def xǁDeepseekConnectorǁexecute__mutmut_3(self, action: str, params: dict[str, Any]) -> Any:
        """Ejecuta una accion del conector DeepSeek.

        Args:
            action: Nombre de la accion a ejecutar
            params: Parametros de la accion
        """
        action_map: dict[str, Any] = {
            "CHAT_COMPLETION": self._chat_completion,
            "reasoning_completion": self._reasoning_completion,
            "code_completion": self._code_completion,
            "list_models": self._list_models,
        }
        handler = action_map.get(action)
        if handler is None:
            return {"error": f"Accion '{action}' no soportada", "available": list(action_map.keys())}
        return handler(params)

    def xǁDeepseekConnectorǁexecute__mutmut_4(self, action: str, params: dict[str, Any]) -> Any:
        """Ejecuta una accion del conector DeepSeek.

        Args:
            action: Nombre de la accion a ejecutar
            params: Parametros de la accion
        """
        action_map: dict[str, Any] = {
            "chat_completion": self._chat_completion,
            "XXreasoning_completionXX": self._reasoning_completion,
            "code_completion": self._code_completion,
            "list_models": self._list_models,
        }
        handler = action_map.get(action)
        if handler is None:
            return {"error": f"Accion '{action}' no soportada", "available": list(action_map.keys())}
        return handler(params)

    def xǁDeepseekConnectorǁexecute__mutmut_5(self, action: str, params: dict[str, Any]) -> Any:
        """Ejecuta una accion del conector DeepSeek.

        Args:
            action: Nombre de la accion a ejecutar
            params: Parametros de la accion
        """
        action_map: dict[str, Any] = {
            "chat_completion": self._chat_completion,
            "REASONING_COMPLETION": self._reasoning_completion,
            "code_completion": self._code_completion,
            "list_models": self._list_models,
        }
        handler = action_map.get(action)
        if handler is None:
            return {"error": f"Accion '{action}' no soportada", "available": list(action_map.keys())}
        return handler(params)

    def xǁDeepseekConnectorǁexecute__mutmut_6(self, action: str, params: dict[str, Any]) -> Any:
        """Ejecuta una accion del conector DeepSeek.

        Args:
            action: Nombre de la accion a ejecutar
            params: Parametros de la accion
        """
        action_map: dict[str, Any] = {
            "chat_completion": self._chat_completion,
            "reasoning_completion": self._reasoning_completion,
            "XXcode_completionXX": self._code_completion,
            "list_models": self._list_models,
        }
        handler = action_map.get(action)
        if handler is None:
            return {"error": f"Accion '{action}' no soportada", "available": list(action_map.keys())}
        return handler(params)

    def xǁDeepseekConnectorǁexecute__mutmut_7(self, action: str, params: dict[str, Any]) -> Any:
        """Ejecuta una accion del conector DeepSeek.

        Args:
            action: Nombre de la accion a ejecutar
            params: Parametros de la accion
        """
        action_map: dict[str, Any] = {
            "chat_completion": self._chat_completion,
            "reasoning_completion": self._reasoning_completion,
            "CODE_COMPLETION": self._code_completion,
            "list_models": self._list_models,
        }
        handler = action_map.get(action)
        if handler is None:
            return {"error": f"Accion '{action}' no soportada", "available": list(action_map.keys())}
        return handler(params)

    def xǁDeepseekConnectorǁexecute__mutmut_8(self, action: str, params: dict[str, Any]) -> Any:
        """Ejecuta una accion del conector DeepSeek.

        Args:
            action: Nombre de la accion a ejecutar
            params: Parametros de la accion
        """
        action_map: dict[str, Any] = {
            "chat_completion": self._chat_completion,
            "reasoning_completion": self._reasoning_completion,
            "code_completion": self._code_completion,
            "XXlist_modelsXX": self._list_models,
        }
        handler = action_map.get(action)
        if handler is None:
            return {"error": f"Accion '{action}' no soportada", "available": list(action_map.keys())}
        return handler(params)

    def xǁDeepseekConnectorǁexecute__mutmut_9(self, action: str, params: dict[str, Any]) -> Any:
        """Ejecuta una accion del conector DeepSeek.

        Args:
            action: Nombre de la accion a ejecutar
            params: Parametros de la accion
        """
        action_map: dict[str, Any] = {
            "chat_completion": self._chat_completion,
            "reasoning_completion": self._reasoning_completion,
            "code_completion": self._code_completion,
            "LIST_MODELS": self._list_models,
        }
        handler = action_map.get(action)
        if handler is None:
            return {"error": f"Accion '{action}' no soportada", "available": list(action_map.keys())}
        return handler(params)

    def xǁDeepseekConnectorǁexecute__mutmut_10(self, action: str, params: dict[str, Any]) -> Any:
        """Ejecuta una accion del conector DeepSeek.

        Args:
            action: Nombre de la accion a ejecutar
            params: Parametros de la accion
        """
        action_map: dict[str, Any] = {
            "chat_completion": self._chat_completion,
            "reasoning_completion": self._reasoning_completion,
            "code_completion": self._code_completion,
            "list_models": self._list_models,
        }
        handler = None
        if handler is None:
            return {"error": f"Accion '{action}' no soportada", "available": list(action_map.keys())}
        return handler(params)

    def xǁDeepseekConnectorǁexecute__mutmut_11(self, action: str, params: dict[str, Any]) -> Any:
        """Ejecuta una accion del conector DeepSeek.

        Args:
            action: Nombre de la accion a ejecutar
            params: Parametros de la accion
        """
        action_map: dict[str, Any] = {
            "chat_completion": self._chat_completion,
            "reasoning_completion": self._reasoning_completion,
            "code_completion": self._code_completion,
            "list_models": self._list_models,
        }
        handler = action_map.get(None)
        if handler is None:
            return {"error": f"Accion '{action}' no soportada", "available": list(action_map.keys())}
        return handler(params)

    def xǁDeepseekConnectorǁexecute__mutmut_12(self, action: str, params: dict[str, Any]) -> Any:
        """Ejecuta una accion del conector DeepSeek.

        Args:
            action: Nombre de la accion a ejecutar
            params: Parametros de la accion
        """
        action_map: dict[str, Any] = {
            "chat_completion": self._chat_completion,
            "reasoning_completion": self._reasoning_completion,
            "code_completion": self._code_completion,
            "list_models": self._list_models,
        }
        handler = action_map.get(action)
        if handler is not None:
            return {"error": f"Accion '{action}' no soportada", "available": list(action_map.keys())}
        return handler(params)

    def xǁDeepseekConnectorǁexecute__mutmut_13(self, action: str, params: dict[str, Any]) -> Any:
        """Ejecuta una accion del conector DeepSeek.

        Args:
            action: Nombre de la accion a ejecutar
            params: Parametros de la accion
        """
        action_map: dict[str, Any] = {
            "chat_completion": self._chat_completion,
            "reasoning_completion": self._reasoning_completion,
            "code_completion": self._code_completion,
            "list_models": self._list_models,
        }
        handler = action_map.get(action)
        if handler is None:
            return {"XXerrorXX": f"Accion '{action}' no soportada", "available": list(action_map.keys())}
        return handler(params)

    def xǁDeepseekConnectorǁexecute__mutmut_14(self, action: str, params: dict[str, Any]) -> Any:
        """Ejecuta una accion del conector DeepSeek.

        Args:
            action: Nombre de la accion a ejecutar
            params: Parametros de la accion
        """
        action_map: dict[str, Any] = {
            "chat_completion": self._chat_completion,
            "reasoning_completion": self._reasoning_completion,
            "code_completion": self._code_completion,
            "list_models": self._list_models,
        }
        handler = action_map.get(action)
        if handler is None:
            return {"ERROR": f"Accion '{action}' no soportada", "available": list(action_map.keys())}
        return handler(params)

    def xǁDeepseekConnectorǁexecute__mutmut_15(self, action: str, params: dict[str, Any]) -> Any:
        """Ejecuta una accion del conector DeepSeek.

        Args:
            action: Nombre de la accion a ejecutar
            params: Parametros de la accion
        """
        action_map: dict[str, Any] = {
            "chat_completion": self._chat_completion,
            "reasoning_completion": self._reasoning_completion,
            "code_completion": self._code_completion,
            "list_models": self._list_models,
        }
        handler = action_map.get(action)
        if handler is None:
            return {"error": f"Accion '{action}' no soportada", "XXavailableXX": list(action_map.keys())}
        return handler(params)

    def xǁDeepseekConnectorǁexecute__mutmut_16(self, action: str, params: dict[str, Any]) -> Any:
        """Ejecuta una accion del conector DeepSeek.

        Args:
            action: Nombre de la accion a ejecutar
            params: Parametros de la accion
        """
        action_map: dict[str, Any] = {
            "chat_completion": self._chat_completion,
            "reasoning_completion": self._reasoning_completion,
            "code_completion": self._code_completion,
            "list_models": self._list_models,
        }
        handler = action_map.get(action)
        if handler is None:
            return {"error": f"Accion '{action}' no soportada", "AVAILABLE": list(action_map.keys())}
        return handler(params)

    def xǁDeepseekConnectorǁexecute__mutmut_17(self, action: str, params: dict[str, Any]) -> Any:
        """Ejecuta una accion del conector DeepSeek.

        Args:
            action: Nombre de la accion a ejecutar
            params: Parametros de la accion
        """
        action_map: dict[str, Any] = {
            "chat_completion": self._chat_completion,
            "reasoning_completion": self._reasoning_completion,
            "code_completion": self._code_completion,
            "list_models": self._list_models,
        }
        handler = action_map.get(action)
        if handler is None:
            return {"error": f"Accion '{action}' no soportada", "available": list(None)}
        return handler(params)

    def xǁDeepseekConnectorǁexecute__mutmut_18(self, action: str, params: dict[str, Any]) -> Any:
        """Ejecuta una accion del conector DeepSeek.

        Args:
            action: Nombre de la accion a ejecutar
            params: Parametros de la accion
        """
        action_map: dict[str, Any] = {
            "chat_completion": self._chat_completion,
            "reasoning_completion": self._reasoning_completion,
            "code_completion": self._code_completion,
            "list_models": self._list_models,
        }
        handler = action_map.get(action)
        if handler is None:
            return {"error": f"Accion '{action}' no soportada", "available": list(action_map.keys())}
        return handler(None)

    @_mutmut_mutated(mutants_xǁDeepseekConnectorǁvalidate__mutmut)
    def validate(self) -> bool:
        """Valida que la API Key de DeepSeek este configurada."""
        if not self._auth_provider:
            return False
        return self._auth_provider.validate()

    def xǁDeepseekConnectorǁvalidate__mutmut_orig(self) -> bool:
        """Valida que la API Key de DeepSeek este configurada."""
        if not self._auth_provider:
            return False
        return self._auth_provider.validate()

    def xǁDeepseekConnectorǁvalidate__mutmut_1(self) -> bool:
        """Valida que la API Key de DeepSeek este configurada."""
        if self._auth_provider:
            return False
        return self._auth_provider.validate()

    def xǁDeepseekConnectorǁvalidate__mutmut_2(self) -> bool:
        """Valida que la API Key de DeepSeek este configurada."""
        if not self._auth_provider:
            return True
        return self._auth_provider.validate()

    @_mutmut_mutated(mutants_xǁDeepseekConnectorǁdisconnect__mutmut)
    def disconnect(self) -> bool:
        """Cierra la conexion con DeepSeek."""
        self._http = None
        self._connected = False
        self._log_operation("disconnect")
        return True

    def xǁDeepseekConnectorǁdisconnect__mutmut_orig(self) -> bool:
        """Cierra la conexion con DeepSeek."""
        self._http = None
        self._connected = False
        self._log_operation("disconnect")
        return True

    def xǁDeepseekConnectorǁdisconnect__mutmut_1(self) -> bool:
        """Cierra la conexion con DeepSeek."""
        self._http = ""
        self._connected = False
        self._log_operation("disconnect")
        return True

    def xǁDeepseekConnectorǁdisconnect__mutmut_2(self) -> bool:
        """Cierra la conexion con DeepSeek."""
        self._http = None
        self._connected = None
        self._log_operation("disconnect")
        return True

    def xǁDeepseekConnectorǁdisconnect__mutmut_3(self) -> bool:
        """Cierra la conexion con DeepSeek."""
        self._http = None
        self._connected = True
        self._log_operation("disconnect")
        return True

    def xǁDeepseekConnectorǁdisconnect__mutmut_4(self) -> bool:
        """Cierra la conexion con DeepSeek."""
        self._http = None
        self._connected = False
        self._log_operation(None)
        return True

    def xǁDeepseekConnectorǁdisconnect__mutmut_5(self) -> bool:
        """Cierra la conexion con DeepSeek."""
        self._http = None
        self._connected = False
        self._log_operation("XXdisconnectXX")
        return True

    def xǁDeepseekConnectorǁdisconnect__mutmut_6(self) -> bool:
        """Cierra la conexion con DeepSeek."""
        self._http = None
        self._connected = False
        self._log_operation("DISCONNECT")
        return True

    def xǁDeepseekConnectorǁdisconnect__mutmut_7(self) -> bool:
        """Cierra la conexion con DeepSeek."""
        self._http = None
        self._connected = False
        self._log_operation("disconnect")
        return False

    @_mutmut_mutated(mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut)
    def _chat_completion(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_orig(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_1(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = None
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_2(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get(None, [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_3(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", None)
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_4(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get([])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_5(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", )
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_6(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("XXmessagesXX", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_7(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("MESSAGES", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_8(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = None
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_9(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get(None, "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_10(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", None)
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_11(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_12(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", )
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_13(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("XXmodelXX", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_14(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("MODEL", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_15(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "XXdeepseek-chatXX")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_16(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "DEEPSEEK-CHAT")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_17(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_18(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"XXsuccessXX": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_19(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"SUCCESS": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_20(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": True, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_21(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "XXerrorXX": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_22(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "ERROR": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_23(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "XXParametro requerido: messagesXX"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_24(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_25(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "PARAMETRO REQUERIDO: MESSAGES"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_26(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation(None, f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_27(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", None)

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_28(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation(f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_29(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", )

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_30(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("XXchat_completionXX", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_31(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("CHAT_COMPLETION", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_32(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = None
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_33(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "XXmodelXX": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_34(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "MODEL": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_35(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "XXmessagesXX": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_36(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "MESSAGES": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_37(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "XXtemperatureXX" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_38(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "TEMPERATURE" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_39(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" not in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_40(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = None
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_41(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["XXtemperatureXX"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_42(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["TEMPERATURE"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_43(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["XXtemperatureXX"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_44(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["TEMPERATURE"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_45(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "XXmax_tokensXX" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_46(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "MAX_TOKENS" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_47(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" not in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_48(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = None
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_49(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["XXmax_tokensXX"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_50(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["MAX_TOKENS"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_51(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["XXmax_tokensXX"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_52(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["MAX_TOKENS"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_53(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "XXtop_pXX" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_54(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "TOP_P" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_55(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" not in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_56(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = None
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_57(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["XXtop_pXX"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_58(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["TOP_P"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_59(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["XXtop_pXX"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_60(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["TOP_P"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_61(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "XXfrequency_penaltyXX" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_62(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "FREQUENCY_PENALTY" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_63(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" not in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_64(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = None
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_65(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["XXfrequency_penaltyXX"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_66(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["FREQUENCY_PENALTY"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_67(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["XXfrequency_penaltyXX"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_68(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["FREQUENCY_PENALTY"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_69(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "XXpresence_penaltyXX" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_70(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "PRESENCE_PENALTY" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_71(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" not in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_72(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = None
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_73(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["XXpresence_penaltyXX"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_74(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["PRESENCE_PENALTY"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_75(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["XXpresence_penaltyXX"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_76(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["PRESENCE_PENALTY"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_77(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "XXstreamXX" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_78(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "STREAM" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_79(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" not in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_80(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = None  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_81(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["XXstreamXX"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_82(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["STREAM"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_83(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = True  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_84(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = None

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_85(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post(None, json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_86(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=None, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_87(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=None)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_88(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post(json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_89(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_90(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, )

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_91(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("XX/chat/completionsXX", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_92(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/CHAT/COMPLETIONS", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_93(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=121)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_94(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_95(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = None
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_96(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() and response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_97(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"XXsuccessXX": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_98(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"SUCCESS": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_99(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": True, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_100(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "XXerrorXX": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_101(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "ERROR": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_102(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = None
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_103(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"XXsuccessXX": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_104(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"SUCCESS": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_105(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": False, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_106(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(None)
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_107(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"XXsuccessXX": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_108(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"SUCCESS": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_109(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": True, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_110(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "XXerrorXX": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_111(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "ERROR": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_112(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(None)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_113(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(None)
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_114(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"XXsuccessXX": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_115(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"SUCCESS": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_116(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": True, "error": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_117(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "XXerrorXX": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_118(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "ERROR": str(e)}

    def xǁDeepseekConnectorǁ_chat_completion__mutmut_119(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta de chat con DeepSeek.

        DeepSeek's API is OpenAI-compatible, using the /chat/completions endpoint.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'temperature', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-chat")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("chat_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "frequency_penalty" in params:
                body["frequency_penalty"] = params["frequency_penalty"]
            if "presence_penalty" in params:
                body["presence_penalty"] = params["presence_penalty"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.chat_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.chat_completion: error: {e}")
            return {"success": False, "error": str(None)}

    @_mutmut_mutated(mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut)
    def _reasoning_completion(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_orig(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_1(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = None
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_2(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get(None, [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_3(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", None)
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_4(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get([])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_5(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", )
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_6(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("XXmessagesXX", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_7(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("MESSAGES", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_8(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = None
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_9(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get(None, "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_10(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", None)
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_11(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_12(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", )
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_13(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("XXmodelXX", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_14(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("MODEL", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_15(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "XXdeepseek-reasonerXX")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_16(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "DEEPSEEK-REASONER")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_17(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_18(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"XXsuccessXX": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_19(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"SUCCESS": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_20(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": True, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_21(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "XXerrorXX": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_22(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "ERROR": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_23(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "XXParametro requerido: messagesXX"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_24(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_25(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "PARAMETRO REQUERIDO: MESSAGES"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_26(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation(None, f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_27(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", None)

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_28(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation(f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_29(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", )

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_30(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("XXreasoning_completionXX", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_31(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("REASONING_COMPLETION", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_32(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = None
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_33(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "XXmodelXX": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_34(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "MODEL": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_35(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "XXmessagesXX": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_36(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "MESSAGES": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_37(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "XXmax_tokensXX" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_38(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "MAX_TOKENS" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_39(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" not in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_40(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = None
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_41(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["XXmax_tokensXX"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_42(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["MAX_TOKENS"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_43(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["XXmax_tokensXX"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_44(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["MAX_TOKENS"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_45(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "XXtemperatureXX" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_46(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "TEMPERATURE" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_47(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" not in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_48(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = None
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_49(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["XXtemperatureXX"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_50(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["TEMPERATURE"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_51(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["XXtemperatureXX"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_52(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["TEMPERATURE"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_53(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "XXtop_pXX" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_54(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "TOP_P" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_55(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" not in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_56(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = None
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_57(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["XXtop_pXX"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_58(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["TOP_P"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_59(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["XXtop_pXX"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_60(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["TOP_P"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_61(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "XXstreamXX" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_62(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "STREAM" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_63(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" not in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_64(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = None  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_65(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["XXstreamXX"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_66(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["STREAM"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_67(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = True  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_68(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = None

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_69(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post(None, json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_70(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=None, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_71(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=None)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_72(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post(json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_73(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_74(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, )

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_75(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("XX/chat/completionsXX", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_76(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/CHAT/COMPLETIONS", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_77(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=181)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_78(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_79(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = None
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_80(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() and response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_81(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"XXsuccessXX": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_82(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"SUCCESS": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_83(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": True, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_84(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "XXerrorXX": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_85(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "ERROR": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_86(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = None
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_87(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"XXsuccessXX": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_88(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"SUCCESS": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_89(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": False, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_90(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(None)
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_91(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"XXsuccessXX": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_92(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"SUCCESS": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_93(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": True, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_94(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "XXerrorXX": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_95(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "ERROR": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_96(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(None)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_97(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(None)
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_98(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"XXsuccessXX": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_99(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"SUCCESS": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_100(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": True, "error": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_101(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "XXerrorXX": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_102(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "ERROR": str(e)}

    def xǁDeepseekConnectorǁ_reasoning_completion__mutmut_103(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera una respuesta con razonamiento extendido (DeepSeek-R1).

        Uses the /chat/completions endpoint with deepseek-reasoner model.
        The response includes a reasoning_content field in the message.

        Args:
            params: Debe contener 'messages' y opcionalmente 'model', 'max_tokens'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-reasoner")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("reasoning_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=180)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.reasoning_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.reasoning_completion: error: {e}")
            return {"success": False, "error": str(None)}

    @_mutmut_mutated(mutants_xǁDeepseekConnectorǁ_code_completion__mutmut)
    def _code_completion(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_orig(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_1(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = None
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_2(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get(None, [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_3(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", None)
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_4(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get([])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_5(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", )
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_6(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("XXmessagesXX", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_7(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("MESSAGES", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_8(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = None
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_9(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get(None, "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_10(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", None)
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_11(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_12(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", )
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_13(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("XXmodelXX", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_14(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("MODEL", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_15(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "XXdeepseek-coderXX")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_16(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "DEEPSEEK-CODER")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_17(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_18(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"XXsuccessXX": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_19(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"SUCCESS": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_20(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": True, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_21(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "XXerrorXX": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_22(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "ERROR": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_23(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "XXParametro requerido: messagesXX"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_24(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_25(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "PARAMETRO REQUERIDO: MESSAGES"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_26(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation(None, f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_27(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", None)

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_28(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation(f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_29(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", )

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_30(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("XXcode_completionXX", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_31(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("CODE_COMPLETION", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_32(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = None
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_33(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "XXmodelXX": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_34(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "MODEL": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_35(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "XXmessagesXX": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_36(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "MESSAGES": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_37(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "XXtemperatureXX" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_38(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "TEMPERATURE" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_39(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" not in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_40(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = None
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_41(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["XXtemperatureXX"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_42(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["TEMPERATURE"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_43(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["XXtemperatureXX"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_44(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["TEMPERATURE"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_45(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "XXmax_tokensXX" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_46(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "MAX_TOKENS" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_47(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" not in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_48(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = None
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_49(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["XXmax_tokensXX"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_50(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["MAX_TOKENS"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_51(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["XXmax_tokensXX"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_52(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["MAX_TOKENS"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_53(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "XXtop_pXX" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_54(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "TOP_P" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_55(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" not in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_56(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = None
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_57(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["XXtop_pXX"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_58(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["TOP_P"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_59(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["XXtop_pXX"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_60(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["TOP_P"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_61(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "XXstreamXX" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_62(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "STREAM" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_63(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" not in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_64(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = None  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_65(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["XXstreamXX"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_66(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["STREAM"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_67(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = True  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_68(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = None

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_69(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post(None, json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_70(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=None, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_71(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=None)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_72(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post(json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_73(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_74(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, )

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_75(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("XX/chat/completionsXX", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_76(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/CHAT/COMPLETIONS", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_77(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=121)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_78(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_79(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = None
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_80(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() and response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_81(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"XXsuccessXX": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_82(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"SUCCESS": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_83(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": True, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_84(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "XXerrorXX": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_85(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "ERROR": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_86(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = None
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_87(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"XXsuccessXX": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_88(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"SUCCESS": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_89(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": False, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_90(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(None)
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_91(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"XXsuccessXX": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_92(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"SUCCESS": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_93(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": True, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_94(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "XXerrorXX": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_95(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "ERROR": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_96(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(None)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_97(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(None)
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_98(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"XXsuccessXX": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_99(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"SUCCESS": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_100(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": True, "error": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_101(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "XXerrorXX": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_102(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "ERROR": str(e)}

    def xǁDeepseekConnectorǁ_code_completion__mutmut_103(self, params: dict[str, Any]) -> dict[str, Any]:
        """Genera completacion de codigo con DeepSeek-Coder.

        Uses the /chat/completions endpoint with deepseek-coder model.

        Args:
            params: Debe contener 'messages' (con prompt de codigo), opcionalmente 'model', 'temperature'
        """
        messages = params.get("messages", [])
        model = params.get("model", "deepseek-coder")
        if not messages:
            return {"success": False, "error": "Parametro requerido: messages"}

        self._log_operation("code_completion", f"model={model}")

        try:
            body: dict[str, Any] = {
                "model": model,
                "messages": messages,
            }
            if "temperature" in params:
                body["temperature"] = params["temperature"]
            if "max_tokens" in params:
                body["max_tokens"] = params["max_tokens"]
            if "top_p" in params:
                body["top_p"] = params["top_p"]
            if "stream" in params:
                body["stream"] = False  # Force non-streaming for simplicity

            response = self._http.post("/chat/completions", json=body, timeout=120)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.code_completion: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.code_completion: error: {e}")
            return {"success": False, "error": str(None)}

    @_mutmut_mutated(mutants_xǁDeepseekConnectorǁ_list_models__mutmut)
    def _list_models(self, params: dict[str, Any]) -> dict[str, Any]:
        """Lista los modelos disponibles de DeepSeek.

        DeepSeek's API is OpenAI-compatible and provides a /models endpoint.
        """
        self._log_operation("list_models")

        try:
            response = self._http.get("/models", timeout=30)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.list_models: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.list_models: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_list_models__mutmut_orig(self, params: dict[str, Any]) -> dict[str, Any]:
        """Lista los modelos disponibles de DeepSeek.

        DeepSeek's API is OpenAI-compatible and provides a /models endpoint.
        """
        self._log_operation("list_models")

        try:
            response = self._http.get("/models", timeout=30)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.list_models: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.list_models: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_list_models__mutmut_1(self, params: dict[str, Any]) -> dict[str, Any]:
        """Lista los modelos disponibles de DeepSeek.

        DeepSeek's API is OpenAI-compatible and provides a /models endpoint.
        """
        self._log_operation(None)

        try:
            response = self._http.get("/models", timeout=30)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.list_models: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.list_models: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_list_models__mutmut_2(self, params: dict[str, Any]) -> dict[str, Any]:
        """Lista los modelos disponibles de DeepSeek.

        DeepSeek's API is OpenAI-compatible and provides a /models endpoint.
        """
        self._log_operation("XXlist_modelsXX")

        try:
            response = self._http.get("/models", timeout=30)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.list_models: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.list_models: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_list_models__mutmut_3(self, params: dict[str, Any]) -> dict[str, Any]:
        """Lista los modelos disponibles de DeepSeek.

        DeepSeek's API is OpenAI-compatible and provides a /models endpoint.
        """
        self._log_operation("LIST_MODELS")

        try:
            response = self._http.get("/models", timeout=30)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.list_models: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.list_models: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_list_models__mutmut_4(self, params: dict[str, Any]) -> dict[str, Any]:
        """Lista los modelos disponibles de DeepSeek.

        DeepSeek's API is OpenAI-compatible and provides a /models endpoint.
        """
        self._log_operation("list_models")

        try:
            response = None

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.list_models: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.list_models: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_list_models__mutmut_5(self, params: dict[str, Any]) -> dict[str, Any]:
        """Lista los modelos disponibles de DeepSeek.

        DeepSeek's API is OpenAI-compatible and provides a /models endpoint.
        """
        self._log_operation("list_models")

        try:
            response = self._http.get(None, timeout=30)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.list_models: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.list_models: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_list_models__mutmut_6(self, params: dict[str, Any]) -> dict[str, Any]:
        """Lista los modelos disponibles de DeepSeek.

        DeepSeek's API is OpenAI-compatible and provides a /models endpoint.
        """
        self._log_operation("list_models")

        try:
            response = self._http.get("/models", timeout=None)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.list_models: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.list_models: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_list_models__mutmut_7(self, params: dict[str, Any]) -> dict[str, Any]:
        """Lista los modelos disponibles de DeepSeek.

        DeepSeek's API is OpenAI-compatible and provides a /models endpoint.
        """
        self._log_operation("list_models")

        try:
            response = self._http.get(timeout=30)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.list_models: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.list_models: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_list_models__mutmut_8(self, params: dict[str, Any]) -> dict[str, Any]:
        """Lista los modelos disponibles de DeepSeek.

        DeepSeek's API is OpenAI-compatible and provides a /models endpoint.
        """
        self._log_operation("list_models")

        try:
            response = self._http.get("/models", )

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.list_models: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.list_models: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_list_models__mutmut_9(self, params: dict[str, Any]) -> dict[str, Any]:
        """Lista los modelos disponibles de DeepSeek.

        DeepSeek's API is OpenAI-compatible and provides a /models endpoint.
        """
        self._log_operation("list_models")

        try:
            response = self._http.get("XX/modelsXX", timeout=30)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.list_models: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.list_models: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_list_models__mutmut_10(self, params: dict[str, Any]) -> dict[str, Any]:
        """Lista los modelos disponibles de DeepSeek.

        DeepSeek's API is OpenAI-compatible and provides a /models endpoint.
        """
        self._log_operation("list_models")

        try:
            response = self._http.get("/MODELS", timeout=30)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.list_models: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.list_models: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_list_models__mutmut_11(self, params: dict[str, Any]) -> dict[str, Any]:
        """Lista los modelos disponibles de DeepSeek.

        DeepSeek's API is OpenAI-compatible and provides a /models endpoint.
        """
        self._log_operation("list_models")

        try:
            response = self._http.get("/models", timeout=31)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.list_models: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.list_models: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_list_models__mutmut_12(self, params: dict[str, Any]) -> dict[str, Any]:
        """Lista los modelos disponibles de DeepSeek.

        DeepSeek's API is OpenAI-compatible and provides a /models endpoint.
        """
        self._log_operation("list_models")

        try:
            response = self._http.get("/models", timeout=30)

            if response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.list_models: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.list_models: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_list_models__mutmut_13(self, params: dict[str, Any]) -> dict[str, Any]:
        """Lista los modelos disponibles de DeepSeek.

        DeepSeek's API is OpenAI-compatible and provides a /models endpoint.
        """
        self._log_operation("list_models")

        try:
            response = self._http.get("/models", timeout=30)

            if not response.ok:
                error_body = None
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.list_models: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.list_models: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_list_models__mutmut_14(self, params: dict[str, Any]) -> dict[str, Any]:
        """Lista los modelos disponibles de DeepSeek.

        DeepSeek's API is OpenAI-compatible and provides a /models endpoint.
        """
        self._log_operation("list_models")

        try:
            response = self._http.get("/models", timeout=30)

            if not response.ok:
                error_body = response.json() and response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.list_models: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.list_models: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_list_models__mutmut_15(self, params: dict[str, Any]) -> dict[str, Any]:
        """Lista los modelos disponibles de DeepSeek.

        DeepSeek's API is OpenAI-compatible and provides a /models endpoint.
        """
        self._log_operation("list_models")

        try:
            response = self._http.get("/models", timeout=30)

            if not response.ok:
                error_body = response.json() or response.body
                return {"XXsuccessXX": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.list_models: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.list_models: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_list_models__mutmut_16(self, params: dict[str, Any]) -> dict[str, Any]:
        """Lista los modelos disponibles de DeepSeek.

        DeepSeek's API is OpenAI-compatible and provides a /models endpoint.
        """
        self._log_operation("list_models")

        try:
            response = self._http.get("/models", timeout=30)

            if not response.ok:
                error_body = response.json() or response.body
                return {"SUCCESS": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.list_models: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.list_models: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_list_models__mutmut_17(self, params: dict[str, Any]) -> dict[str, Any]:
        """Lista los modelos disponibles de DeepSeek.

        DeepSeek's API is OpenAI-compatible and provides a /models endpoint.
        """
        self._log_operation("list_models")

        try:
            response = self._http.get("/models", timeout=30)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": True, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.list_models: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.list_models: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_list_models__mutmut_18(self, params: dict[str, Any]) -> dict[str, Any]:
        """Lista los modelos disponibles de DeepSeek.

        DeepSeek's API is OpenAI-compatible and provides a /models endpoint.
        """
        self._log_operation("list_models")

        try:
            response = self._http.get("/models", timeout=30)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "XXerrorXX": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.list_models: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.list_models: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_list_models__mutmut_19(self, params: dict[str, Any]) -> dict[str, Any]:
        """Lista los modelos disponibles de DeepSeek.

        DeepSeek's API is OpenAI-compatible and provides a /models endpoint.
        """
        self._log_operation("list_models")

        try:
            response = self._http.get("/models", timeout=30)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "ERROR": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.list_models: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.list_models: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_list_models__mutmut_20(self, params: dict[str, Any]) -> dict[str, Any]:
        """Lista los modelos disponibles de DeepSeek.

        DeepSeek's API is OpenAI-compatible and provides a /models endpoint.
        """
        self._log_operation("list_models")

        try:
            response = self._http.get("/models", timeout=30)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = None
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.list_models: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.list_models: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_list_models__mutmut_21(self, params: dict[str, Any]) -> dict[str, Any]:
        """Lista los modelos disponibles de DeepSeek.

        DeepSeek's API is OpenAI-compatible and provides a /models endpoint.
        """
        self._log_operation("list_models")

        try:
            response = self._http.get("/models", timeout=30)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"XXsuccessXX": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.list_models: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.list_models: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_list_models__mutmut_22(self, params: dict[str, Any]) -> dict[str, Any]:
        """Lista los modelos disponibles de DeepSeek.

        DeepSeek's API is OpenAI-compatible and provides a /models endpoint.
        """
        self._log_operation("list_models")

        try:
            response = self._http.get("/models", timeout=30)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"SUCCESS": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.list_models: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.list_models: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_list_models__mutmut_23(self, params: dict[str, Any]) -> dict[str, Any]:
        """Lista los modelos disponibles de DeepSeek.

        DeepSeek's API is OpenAI-compatible and provides a /models endpoint.
        """
        self._log_operation("list_models")

        try:
            response = self._http.get("/models", timeout=30)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": False, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.list_models: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.list_models: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_list_models__mutmut_24(self, params: dict[str, Any]) -> dict[str, Any]:
        """Lista los modelos disponibles de DeepSeek.

        DeepSeek's API is OpenAI-compatible and provides a /models endpoint.
        """
        self._log_operation("list_models")

        try:
            response = self._http.get("/models", timeout=30)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(None)
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.list_models: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_list_models__mutmut_25(self, params: dict[str, Any]) -> dict[str, Any]:
        """Lista los modelos disponibles de DeepSeek.

        DeepSeek's API is OpenAI-compatible and provides a /models endpoint.
        """
        self._log_operation("list_models")

        try:
            response = self._http.get("/models", timeout=30)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.list_models: HTTP error: {e}")
            return {"XXsuccessXX": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.list_models: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_list_models__mutmut_26(self, params: dict[str, Any]) -> dict[str, Any]:
        """Lista los modelos disponibles de DeepSeek.

        DeepSeek's API is OpenAI-compatible and provides a /models endpoint.
        """
        self._log_operation("list_models")

        try:
            response = self._http.get("/models", timeout=30)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.list_models: HTTP error: {e}")
            return {"SUCCESS": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.list_models: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_list_models__mutmut_27(self, params: dict[str, Any]) -> dict[str, Any]:
        """Lista los modelos disponibles de DeepSeek.

        DeepSeek's API is OpenAI-compatible and provides a /models endpoint.
        """
        self._log_operation("list_models")

        try:
            response = self._http.get("/models", timeout=30)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.list_models: HTTP error: {e}")
            return {"success": True, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.list_models: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_list_models__mutmut_28(self, params: dict[str, Any]) -> dict[str, Any]:
        """Lista los modelos disponibles de DeepSeek.

        DeepSeek's API is OpenAI-compatible and provides a /models endpoint.
        """
        self._log_operation("list_models")

        try:
            response = self._http.get("/models", timeout=30)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.list_models: HTTP error: {e}")
            return {"success": False, "XXerrorXX": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.list_models: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_list_models__mutmut_29(self, params: dict[str, Any]) -> dict[str, Any]:
        """Lista los modelos disponibles de DeepSeek.

        DeepSeek's API is OpenAI-compatible and provides a /models endpoint.
        """
        self._log_operation("list_models")

        try:
            response = self._http.get("/models", timeout=30)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.list_models: HTTP error: {e}")
            return {"success": False, "ERROR": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.list_models: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_list_models__mutmut_30(self, params: dict[str, Any]) -> dict[str, Any]:
        """Lista los modelos disponibles de DeepSeek.

        DeepSeek's API is OpenAI-compatible and provides a /models endpoint.
        """
        self._log_operation("list_models")

        try:
            response = self._http.get("/models", timeout=30)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.list_models: HTTP error: {e}")
            return {"success": False, "error": str(None)}
        except Exception as e:
            logger.error(f"DeepseekConnector.list_models: error: {e}")
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_list_models__mutmut_31(self, params: dict[str, Any]) -> dict[str, Any]:
        """Lista los modelos disponibles de DeepSeek.

        DeepSeek's API is OpenAI-compatible and provides a /models endpoint.
        """
        self._log_operation("list_models")

        try:
            response = self._http.get("/models", timeout=30)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.list_models: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(None)
            return {"success": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_list_models__mutmut_32(self, params: dict[str, Any]) -> dict[str, Any]:
        """Lista los modelos disponibles de DeepSeek.

        DeepSeek's API is OpenAI-compatible and provides a /models endpoint.
        """
        self._log_operation("list_models")

        try:
            response = self._http.get("/models", timeout=30)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.list_models: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.list_models: error: {e}")
            return {"XXsuccessXX": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_list_models__mutmut_33(self, params: dict[str, Any]) -> dict[str, Any]:
        """Lista los modelos disponibles de DeepSeek.

        DeepSeek's API is OpenAI-compatible and provides a /models endpoint.
        """
        self._log_operation("list_models")

        try:
            response = self._http.get("/models", timeout=30)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.list_models: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.list_models: error: {e}")
            return {"SUCCESS": False, "error": str(e)}

    def xǁDeepseekConnectorǁ_list_models__mutmut_34(self, params: dict[str, Any]) -> dict[str, Any]:
        """Lista los modelos disponibles de DeepSeek.

        DeepSeek's API is OpenAI-compatible and provides a /models endpoint.
        """
        self._log_operation("list_models")

        try:
            response = self._http.get("/models", timeout=30)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.list_models: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.list_models: error: {e}")
            return {"success": True, "error": str(e)}

    def xǁDeepseekConnectorǁ_list_models__mutmut_35(self, params: dict[str, Any]) -> dict[str, Any]:
        """Lista los modelos disponibles de DeepSeek.

        DeepSeek's API is OpenAI-compatible and provides a /models endpoint.
        """
        self._log_operation("list_models")

        try:
            response = self._http.get("/models", timeout=30)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.list_models: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.list_models: error: {e}")
            return {"success": False, "XXerrorXX": str(e)}

    def xǁDeepseekConnectorǁ_list_models__mutmut_36(self, params: dict[str, Any]) -> dict[str, Any]:
        """Lista los modelos disponibles de DeepSeek.

        DeepSeek's API is OpenAI-compatible and provides a /models endpoint.
        """
        self._log_operation("list_models")

        try:
            response = self._http.get("/models", timeout=30)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.list_models: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.list_models: error: {e}")
            return {"success": False, "ERROR": str(e)}

    def xǁDeepseekConnectorǁ_list_models__mutmut_37(self, params: dict[str, Any]) -> dict[str, Any]:
        """Lista los modelos disponibles de DeepSeek.

        DeepSeek's API is OpenAI-compatible and provides a /models endpoint.
        """
        self._log_operation("list_models")

        try:
            response = self._http.get("/models", timeout=30)

            if not response.ok:
                error_body = response.json() or response.body
                return {"success": False, "error": f"DeepSeek API error ({response.status_code}): {error_body}"}

            data = response.json()
            return {"success": True, **data}

        except HTTPClientError as e:
            logger.error(f"DeepseekConnector.list_models: HTTP error: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logger.error(f"DeepseekConnector.list_models: error: {e}")
            return {"success": False, "error": str(None)}

mutants_xǁDeepseekConnectorǁ__init____mutmut['_mutmut_orig'] = DeepseekConnector.xǁDeepseekConnectorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ__init____mutmut['xǁDeepseekConnectorǁ__init____mutmut_1'] = DeepseekConnector.xǁDeepseekConnectorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ__init____mutmut['xǁDeepseekConnectorǁ__init____mutmut_2'] = DeepseekConnector.xǁDeepseekConnectorǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ__init____mutmut['xǁDeepseekConnectorǁ__init____mutmut_3'] = DeepseekConnector.xǁDeepseekConnectorǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ__init____mutmut['xǁDeepseekConnectorǁ__init____mutmut_4'] = DeepseekConnector.xǁDeepseekConnectorǁ__init____mutmut_4 # type: ignore # mutmut generated

mutants_xǁDeepseekConnectorǁ_get_api_key__mutmut['_mutmut_orig'] = DeepseekConnector.xǁDeepseekConnectorǁ_get_api_key__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_get_api_key__mutmut['xǁDeepseekConnectorǁ_get_api_key__mutmut_1'] = DeepseekConnector.xǁDeepseekConnectorǁ_get_api_key__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_get_api_key__mutmut['xǁDeepseekConnectorǁ_get_api_key__mutmut_2'] = DeepseekConnector.xǁDeepseekConnectorǁ_get_api_key__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_get_api_key__mutmut['xǁDeepseekConnectorǁ_get_api_key__mutmut_3'] = DeepseekConnector.xǁDeepseekConnectorǁ_get_api_key__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_get_api_key__mutmut['xǁDeepseekConnectorǁ_get_api_key__mutmut_4'] = DeepseekConnector.xǁDeepseekConnectorǁ_get_api_key__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_get_api_key__mutmut['xǁDeepseekConnectorǁ_get_api_key__mutmut_5'] = DeepseekConnector.xǁDeepseekConnectorǁ_get_api_key__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_get_api_key__mutmut['xǁDeepseekConnectorǁ_get_api_key__mutmut_6'] = DeepseekConnector.xǁDeepseekConnectorǁ_get_api_key__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_get_api_key__mutmut['xǁDeepseekConnectorǁ_get_api_key__mutmut_7'] = DeepseekConnector.xǁDeepseekConnectorǁ_get_api_key__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_get_api_key__mutmut['xǁDeepseekConnectorǁ_get_api_key__mutmut_8'] = DeepseekConnector.xǁDeepseekConnectorǁ_get_api_key__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_get_api_key__mutmut['xǁDeepseekConnectorǁ_get_api_key__mutmut_9'] = DeepseekConnector.xǁDeepseekConnectorǁ_get_api_key__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_get_api_key__mutmut['xǁDeepseekConnectorǁ_get_api_key__mutmut_10'] = DeepseekConnector.xǁDeepseekConnectorǁ_get_api_key__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_get_api_key__mutmut['xǁDeepseekConnectorǁ_get_api_key__mutmut_11'] = DeepseekConnector.xǁDeepseekConnectorǁ_get_api_key__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_get_api_key__mutmut['xǁDeepseekConnectorǁ_get_api_key__mutmut_12'] = DeepseekConnector.xǁDeepseekConnectorǁ_get_api_key__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_get_api_key__mutmut['xǁDeepseekConnectorǁ_get_api_key__mutmut_13'] = DeepseekConnector.xǁDeepseekConnectorǁ_get_api_key__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_get_api_key__mutmut['xǁDeepseekConnectorǁ_get_api_key__mutmut_14'] = DeepseekConnector.xǁDeepseekConnectorǁ_get_api_key__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_get_api_key__mutmut['xǁDeepseekConnectorǁ_get_api_key__mutmut_15'] = DeepseekConnector.xǁDeepseekConnectorǁ_get_api_key__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_get_api_key__mutmut['xǁDeepseekConnectorǁ_get_api_key__mutmut_16'] = DeepseekConnector.xǁDeepseekConnectorǁ_get_api_key__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_get_api_key__mutmut['xǁDeepseekConnectorǁ_get_api_key__mutmut_17'] = DeepseekConnector.xǁDeepseekConnectorǁ_get_api_key__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_get_api_key__mutmut['xǁDeepseekConnectorǁ_get_api_key__mutmut_18'] = DeepseekConnector.xǁDeepseekConnectorǁ_get_api_key__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_get_api_key__mutmut['xǁDeepseekConnectorǁ_get_api_key__mutmut_19'] = DeepseekConnector.xǁDeepseekConnectorǁ_get_api_key__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_get_api_key__mutmut['xǁDeepseekConnectorǁ_get_api_key__mutmut_20'] = DeepseekConnector.xǁDeepseekConnectorǁ_get_api_key__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_get_api_key__mutmut['xǁDeepseekConnectorǁ_get_api_key__mutmut_21'] = DeepseekConnector.xǁDeepseekConnectorǁ_get_api_key__mutmut_21 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_get_api_key__mutmut['xǁDeepseekConnectorǁ_get_api_key__mutmut_22'] = DeepseekConnector.xǁDeepseekConnectorǁ_get_api_key__mutmut_22 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_get_api_key__mutmut['xǁDeepseekConnectorǁ_get_api_key__mutmut_23'] = DeepseekConnector.xǁDeepseekConnectorǁ_get_api_key__mutmut_23 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_get_api_key__mutmut['xǁDeepseekConnectorǁ_get_api_key__mutmut_24'] = DeepseekConnector.xǁDeepseekConnectorǁ_get_api_key__mutmut_24 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_get_api_key__mutmut['xǁDeepseekConnectorǁ_get_api_key__mutmut_25'] = DeepseekConnector.xǁDeepseekConnectorǁ_get_api_key__mutmut_25 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_get_api_key__mutmut['xǁDeepseekConnectorǁ_get_api_key__mutmut_26'] = DeepseekConnector.xǁDeepseekConnectorǁ_get_api_key__mutmut_26 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_get_api_key__mutmut['xǁDeepseekConnectorǁ_get_api_key__mutmut_27'] = DeepseekConnector.xǁDeepseekConnectorǁ_get_api_key__mutmut_27 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_get_api_key__mutmut['xǁDeepseekConnectorǁ_get_api_key__mutmut_28'] = DeepseekConnector.xǁDeepseekConnectorǁ_get_api_key__mutmut_28 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_get_api_key__mutmut['xǁDeepseekConnectorǁ_get_api_key__mutmut_29'] = DeepseekConnector.xǁDeepseekConnectorǁ_get_api_key__mutmut_29 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_get_api_key__mutmut['xǁDeepseekConnectorǁ_get_api_key__mutmut_30'] = DeepseekConnector.xǁDeepseekConnectorǁ_get_api_key__mutmut_30 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_get_api_key__mutmut['xǁDeepseekConnectorǁ_get_api_key__mutmut_31'] = DeepseekConnector.xǁDeepseekConnectorǁ_get_api_key__mutmut_31 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_get_api_key__mutmut['xǁDeepseekConnectorǁ_get_api_key__mutmut_32'] = DeepseekConnector.xǁDeepseekConnectorǁ_get_api_key__mutmut_32 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_get_api_key__mutmut['xǁDeepseekConnectorǁ_get_api_key__mutmut_33'] = DeepseekConnector.xǁDeepseekConnectorǁ_get_api_key__mutmut_33 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_get_api_key__mutmut['xǁDeepseekConnectorǁ_get_api_key__mutmut_34'] = DeepseekConnector.xǁDeepseekConnectorǁ_get_api_key__mutmut_34 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_get_api_key__mutmut['xǁDeepseekConnectorǁ_get_api_key__mutmut_35'] = DeepseekConnector.xǁDeepseekConnectorǁ_get_api_key__mutmut_35 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_get_api_key__mutmut['xǁDeepseekConnectorǁ_get_api_key__mutmut_36'] = DeepseekConnector.xǁDeepseekConnectorǁ_get_api_key__mutmut_36 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_get_api_key__mutmut['xǁDeepseekConnectorǁ_get_api_key__mutmut_37'] = DeepseekConnector.xǁDeepseekConnectorǁ_get_api_key__mutmut_37 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_get_api_key__mutmut['xǁDeepseekConnectorǁ_get_api_key__mutmut_38'] = DeepseekConnector.xǁDeepseekConnectorǁ_get_api_key__mutmut_38 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_get_api_key__mutmut['xǁDeepseekConnectorǁ_get_api_key__mutmut_39'] = DeepseekConnector.xǁDeepseekConnectorǁ_get_api_key__mutmut_39 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_get_api_key__mutmut['xǁDeepseekConnectorǁ_get_api_key__mutmut_40'] = DeepseekConnector.xǁDeepseekConnectorǁ_get_api_key__mutmut_40 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_get_api_key__mutmut['xǁDeepseekConnectorǁ_get_api_key__mutmut_41'] = DeepseekConnector.xǁDeepseekConnectorǁ_get_api_key__mutmut_41 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_get_api_key__mutmut['xǁDeepseekConnectorǁ_get_api_key__mutmut_42'] = DeepseekConnector.xǁDeepseekConnectorǁ_get_api_key__mutmut_42 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_get_api_key__mutmut['xǁDeepseekConnectorǁ_get_api_key__mutmut_43'] = DeepseekConnector.xǁDeepseekConnectorǁ_get_api_key__mutmut_43 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_get_api_key__mutmut['xǁDeepseekConnectorǁ_get_api_key__mutmut_44'] = DeepseekConnector.xǁDeepseekConnectorǁ_get_api_key__mutmut_44 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_get_api_key__mutmut['xǁDeepseekConnectorǁ_get_api_key__mutmut_45'] = DeepseekConnector.xǁDeepseekConnectorǁ_get_api_key__mutmut_45 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_get_api_key__mutmut['xǁDeepseekConnectorǁ_get_api_key__mutmut_46'] = DeepseekConnector.xǁDeepseekConnectorǁ_get_api_key__mutmut_46 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_get_api_key__mutmut['xǁDeepseekConnectorǁ_get_api_key__mutmut_47'] = DeepseekConnector.xǁDeepseekConnectorǁ_get_api_key__mutmut_47 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_get_api_key__mutmut['xǁDeepseekConnectorǁ_get_api_key__mutmut_48'] = DeepseekConnector.xǁDeepseekConnectorǁ_get_api_key__mutmut_48 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_get_api_key__mutmut['xǁDeepseekConnectorǁ_get_api_key__mutmut_49'] = DeepseekConnector.xǁDeepseekConnectorǁ_get_api_key__mutmut_49 # type: ignore # mutmut generated

mutants_xǁDeepseekConnectorǁconnect__mutmut['_mutmut_orig'] = DeepseekConnector.xǁDeepseekConnectorǁconnect__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁconnect__mutmut['xǁDeepseekConnectorǁconnect__mutmut_1'] = DeepseekConnector.xǁDeepseekConnectorǁconnect__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁconnect__mutmut['xǁDeepseekConnectorǁconnect__mutmut_2'] = DeepseekConnector.xǁDeepseekConnectorǁconnect__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁconnect__mutmut['xǁDeepseekConnectorǁconnect__mutmut_3'] = DeepseekConnector.xǁDeepseekConnectorǁconnect__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁconnect__mutmut['xǁDeepseekConnectorǁconnect__mutmut_4'] = DeepseekConnector.xǁDeepseekConnectorǁconnect__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁconnect__mutmut['xǁDeepseekConnectorǁconnect__mutmut_5'] = DeepseekConnector.xǁDeepseekConnectorǁconnect__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁconnect__mutmut['xǁDeepseekConnectorǁconnect__mutmut_6'] = DeepseekConnector.xǁDeepseekConnectorǁconnect__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁconnect__mutmut['xǁDeepseekConnectorǁconnect__mutmut_7'] = DeepseekConnector.xǁDeepseekConnectorǁconnect__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁconnect__mutmut['xǁDeepseekConnectorǁconnect__mutmut_8'] = DeepseekConnector.xǁDeepseekConnectorǁconnect__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁconnect__mutmut['xǁDeepseekConnectorǁconnect__mutmut_9'] = DeepseekConnector.xǁDeepseekConnectorǁconnect__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁconnect__mutmut['xǁDeepseekConnectorǁconnect__mutmut_10'] = DeepseekConnector.xǁDeepseekConnectorǁconnect__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁconnect__mutmut['xǁDeepseekConnectorǁconnect__mutmut_11'] = DeepseekConnector.xǁDeepseekConnectorǁconnect__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁconnect__mutmut['xǁDeepseekConnectorǁconnect__mutmut_12'] = DeepseekConnector.xǁDeepseekConnectorǁconnect__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁconnect__mutmut['xǁDeepseekConnectorǁconnect__mutmut_13'] = DeepseekConnector.xǁDeepseekConnectorǁconnect__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁconnect__mutmut['xǁDeepseekConnectorǁconnect__mutmut_14'] = DeepseekConnector.xǁDeepseekConnectorǁconnect__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁconnect__mutmut['xǁDeepseekConnectorǁconnect__mutmut_15'] = DeepseekConnector.xǁDeepseekConnectorǁconnect__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁconnect__mutmut['xǁDeepseekConnectorǁconnect__mutmut_16'] = DeepseekConnector.xǁDeepseekConnectorǁconnect__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁconnect__mutmut['xǁDeepseekConnectorǁconnect__mutmut_17'] = DeepseekConnector.xǁDeepseekConnectorǁconnect__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁconnect__mutmut['xǁDeepseekConnectorǁconnect__mutmut_18'] = DeepseekConnector.xǁDeepseekConnectorǁconnect__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁconnect__mutmut['xǁDeepseekConnectorǁconnect__mutmut_19'] = DeepseekConnector.xǁDeepseekConnectorǁconnect__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁconnect__mutmut['xǁDeepseekConnectorǁconnect__mutmut_20'] = DeepseekConnector.xǁDeepseekConnectorǁconnect__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁconnect__mutmut['xǁDeepseekConnectorǁconnect__mutmut_21'] = DeepseekConnector.xǁDeepseekConnectorǁconnect__mutmut_21 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁconnect__mutmut['xǁDeepseekConnectorǁconnect__mutmut_22'] = DeepseekConnector.xǁDeepseekConnectorǁconnect__mutmut_22 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁconnect__mutmut['xǁDeepseekConnectorǁconnect__mutmut_23'] = DeepseekConnector.xǁDeepseekConnectorǁconnect__mutmut_23 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁconnect__mutmut['xǁDeepseekConnectorǁconnect__mutmut_24'] = DeepseekConnector.xǁDeepseekConnectorǁconnect__mutmut_24 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁconnect__mutmut['xǁDeepseekConnectorǁconnect__mutmut_25'] = DeepseekConnector.xǁDeepseekConnectorǁconnect__mutmut_25 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁconnect__mutmut['xǁDeepseekConnectorǁconnect__mutmut_26'] = DeepseekConnector.xǁDeepseekConnectorǁconnect__mutmut_26 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁconnect__mutmut['xǁDeepseekConnectorǁconnect__mutmut_27'] = DeepseekConnector.xǁDeepseekConnectorǁconnect__mutmut_27 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁconnect__mutmut['xǁDeepseekConnectorǁconnect__mutmut_28'] = DeepseekConnector.xǁDeepseekConnectorǁconnect__mutmut_28 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁconnect__mutmut['xǁDeepseekConnectorǁconnect__mutmut_29'] = DeepseekConnector.xǁDeepseekConnectorǁconnect__mutmut_29 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁconnect__mutmut['xǁDeepseekConnectorǁconnect__mutmut_30'] = DeepseekConnector.xǁDeepseekConnectorǁconnect__mutmut_30 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁconnect__mutmut['xǁDeepseekConnectorǁconnect__mutmut_31'] = DeepseekConnector.xǁDeepseekConnectorǁconnect__mutmut_31 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁconnect__mutmut['xǁDeepseekConnectorǁconnect__mutmut_32'] = DeepseekConnector.xǁDeepseekConnectorǁconnect__mutmut_32 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁconnect__mutmut['xǁDeepseekConnectorǁconnect__mutmut_33'] = DeepseekConnector.xǁDeepseekConnectorǁconnect__mutmut_33 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁconnect__mutmut['xǁDeepseekConnectorǁconnect__mutmut_34'] = DeepseekConnector.xǁDeepseekConnectorǁconnect__mutmut_34 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁconnect__mutmut['xǁDeepseekConnectorǁconnect__mutmut_35'] = DeepseekConnector.xǁDeepseekConnectorǁconnect__mutmut_35 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁconnect__mutmut['xǁDeepseekConnectorǁconnect__mutmut_36'] = DeepseekConnector.xǁDeepseekConnectorǁconnect__mutmut_36 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁconnect__mutmut['xǁDeepseekConnectorǁconnect__mutmut_37'] = DeepseekConnector.xǁDeepseekConnectorǁconnect__mutmut_37 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁconnect__mutmut['xǁDeepseekConnectorǁconnect__mutmut_38'] = DeepseekConnector.xǁDeepseekConnectorǁconnect__mutmut_38 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁconnect__mutmut['xǁDeepseekConnectorǁconnect__mutmut_39'] = DeepseekConnector.xǁDeepseekConnectorǁconnect__mutmut_39 # type: ignore # mutmut generated

mutants_xǁDeepseekConnectorǁexecute__mutmut['_mutmut_orig'] = DeepseekConnector.xǁDeepseekConnectorǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁexecute__mutmut['xǁDeepseekConnectorǁexecute__mutmut_1'] = DeepseekConnector.xǁDeepseekConnectorǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁexecute__mutmut['xǁDeepseekConnectorǁexecute__mutmut_2'] = DeepseekConnector.xǁDeepseekConnectorǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁexecute__mutmut['xǁDeepseekConnectorǁexecute__mutmut_3'] = DeepseekConnector.xǁDeepseekConnectorǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁexecute__mutmut['xǁDeepseekConnectorǁexecute__mutmut_4'] = DeepseekConnector.xǁDeepseekConnectorǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁexecute__mutmut['xǁDeepseekConnectorǁexecute__mutmut_5'] = DeepseekConnector.xǁDeepseekConnectorǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁexecute__mutmut['xǁDeepseekConnectorǁexecute__mutmut_6'] = DeepseekConnector.xǁDeepseekConnectorǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁexecute__mutmut['xǁDeepseekConnectorǁexecute__mutmut_7'] = DeepseekConnector.xǁDeepseekConnectorǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁexecute__mutmut['xǁDeepseekConnectorǁexecute__mutmut_8'] = DeepseekConnector.xǁDeepseekConnectorǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁexecute__mutmut['xǁDeepseekConnectorǁexecute__mutmut_9'] = DeepseekConnector.xǁDeepseekConnectorǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁexecute__mutmut['xǁDeepseekConnectorǁexecute__mutmut_10'] = DeepseekConnector.xǁDeepseekConnectorǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁexecute__mutmut['xǁDeepseekConnectorǁexecute__mutmut_11'] = DeepseekConnector.xǁDeepseekConnectorǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁexecute__mutmut['xǁDeepseekConnectorǁexecute__mutmut_12'] = DeepseekConnector.xǁDeepseekConnectorǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁexecute__mutmut['xǁDeepseekConnectorǁexecute__mutmut_13'] = DeepseekConnector.xǁDeepseekConnectorǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁexecute__mutmut['xǁDeepseekConnectorǁexecute__mutmut_14'] = DeepseekConnector.xǁDeepseekConnectorǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁexecute__mutmut['xǁDeepseekConnectorǁexecute__mutmut_15'] = DeepseekConnector.xǁDeepseekConnectorǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁexecute__mutmut['xǁDeepseekConnectorǁexecute__mutmut_16'] = DeepseekConnector.xǁDeepseekConnectorǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁexecute__mutmut['xǁDeepseekConnectorǁexecute__mutmut_17'] = DeepseekConnector.xǁDeepseekConnectorǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁexecute__mutmut['xǁDeepseekConnectorǁexecute__mutmut_18'] = DeepseekConnector.xǁDeepseekConnectorǁexecute__mutmut_18 # type: ignore # mutmut generated

mutants_xǁDeepseekConnectorǁvalidate__mutmut['_mutmut_orig'] = DeepseekConnector.xǁDeepseekConnectorǁvalidate__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁvalidate__mutmut['xǁDeepseekConnectorǁvalidate__mutmut_1'] = DeepseekConnector.xǁDeepseekConnectorǁvalidate__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁvalidate__mutmut['xǁDeepseekConnectorǁvalidate__mutmut_2'] = DeepseekConnector.xǁDeepseekConnectorǁvalidate__mutmut_2 # type: ignore # mutmut generated

mutants_xǁDeepseekConnectorǁdisconnect__mutmut['_mutmut_orig'] = DeepseekConnector.xǁDeepseekConnectorǁdisconnect__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁdisconnect__mutmut['xǁDeepseekConnectorǁdisconnect__mutmut_1'] = DeepseekConnector.xǁDeepseekConnectorǁdisconnect__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁdisconnect__mutmut['xǁDeepseekConnectorǁdisconnect__mutmut_2'] = DeepseekConnector.xǁDeepseekConnectorǁdisconnect__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁdisconnect__mutmut['xǁDeepseekConnectorǁdisconnect__mutmut_3'] = DeepseekConnector.xǁDeepseekConnectorǁdisconnect__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁdisconnect__mutmut['xǁDeepseekConnectorǁdisconnect__mutmut_4'] = DeepseekConnector.xǁDeepseekConnectorǁdisconnect__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁdisconnect__mutmut['xǁDeepseekConnectorǁdisconnect__mutmut_5'] = DeepseekConnector.xǁDeepseekConnectorǁdisconnect__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁdisconnect__mutmut['xǁDeepseekConnectorǁdisconnect__mutmut_6'] = DeepseekConnector.xǁDeepseekConnectorǁdisconnect__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁdisconnect__mutmut['xǁDeepseekConnectorǁdisconnect__mutmut_7'] = DeepseekConnector.xǁDeepseekConnectorǁdisconnect__mutmut_7 # type: ignore # mutmut generated

mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['_mutmut_orig'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_1'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_2'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_3'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_4'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_5'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_6'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_7'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_8'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_9'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_10'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_11'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_12'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_13'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_14'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_15'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_16'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_17'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_18'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_19'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_20'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_21'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_21 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_22'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_22 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_23'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_23 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_24'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_24 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_25'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_25 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_26'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_26 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_27'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_27 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_28'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_28 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_29'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_29 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_30'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_30 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_31'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_31 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_32'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_32 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_33'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_33 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_34'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_34 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_35'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_35 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_36'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_36 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_37'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_37 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_38'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_38 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_39'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_39 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_40'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_40 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_41'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_41 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_42'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_42 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_43'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_43 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_44'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_44 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_45'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_45 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_46'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_46 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_47'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_47 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_48'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_48 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_49'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_49 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_50'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_50 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_51'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_51 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_52'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_52 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_53'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_53 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_54'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_54 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_55'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_55 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_56'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_56 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_57'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_57 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_58'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_58 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_59'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_59 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_60'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_60 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_61'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_61 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_62'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_62 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_63'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_63 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_64'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_64 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_65'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_65 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_66'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_66 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_67'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_67 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_68'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_68 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_69'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_69 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_70'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_70 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_71'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_71 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_72'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_72 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_73'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_73 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_74'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_74 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_75'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_75 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_76'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_76 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_77'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_77 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_78'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_78 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_79'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_79 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_80'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_80 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_81'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_81 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_82'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_82 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_83'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_83 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_84'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_84 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_85'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_85 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_86'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_86 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_87'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_87 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_88'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_88 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_89'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_89 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_90'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_90 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_91'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_91 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_92'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_92 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_93'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_93 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_94'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_94 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_95'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_95 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_96'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_96 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_97'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_97 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_98'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_98 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_99'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_99 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_100'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_100 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_101'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_101 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_102'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_102 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_103'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_103 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_104'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_104 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_105'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_105 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_106'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_106 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_107'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_107 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_108'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_108 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_109'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_109 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_110'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_110 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_111'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_111 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_112'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_112 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_113'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_113 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_114'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_114 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_115'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_115 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_116'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_116 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_117'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_117 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_118'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_118 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_chat_completion__mutmut['xǁDeepseekConnectorǁ_chat_completion__mutmut_119'] = DeepseekConnector.xǁDeepseekConnectorǁ_chat_completion__mutmut_119 # type: ignore # mutmut generated

mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['_mutmut_orig'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_1'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_2'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_3'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_4'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_5'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_6'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_7'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_8'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_9'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_10'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_11'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_12'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_13'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_14'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_15'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_16'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_17'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_18'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_19'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_20'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_21'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_21 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_22'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_22 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_23'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_23 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_24'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_24 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_25'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_25 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_26'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_26 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_27'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_27 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_28'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_28 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_29'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_29 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_30'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_30 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_31'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_31 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_32'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_32 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_33'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_33 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_34'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_34 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_35'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_35 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_36'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_36 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_37'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_37 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_38'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_38 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_39'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_39 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_40'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_40 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_41'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_41 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_42'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_42 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_43'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_43 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_44'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_44 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_45'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_45 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_46'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_46 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_47'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_47 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_48'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_48 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_49'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_49 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_50'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_50 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_51'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_51 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_52'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_52 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_53'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_53 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_54'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_54 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_55'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_55 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_56'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_56 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_57'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_57 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_58'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_58 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_59'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_59 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_60'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_60 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_61'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_61 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_62'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_62 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_63'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_63 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_64'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_64 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_65'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_65 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_66'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_66 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_67'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_67 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_68'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_68 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_69'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_69 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_70'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_70 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_71'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_71 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_72'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_72 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_73'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_73 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_74'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_74 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_75'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_75 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_76'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_76 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_77'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_77 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_78'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_78 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_79'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_79 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_80'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_80 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_81'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_81 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_82'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_82 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_83'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_83 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_84'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_84 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_85'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_85 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_86'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_86 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_87'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_87 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_88'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_88 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_89'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_89 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_90'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_90 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_91'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_91 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_92'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_92 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_93'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_93 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_94'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_94 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_95'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_95 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_96'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_96 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_97'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_97 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_98'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_98 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_99'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_99 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_100'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_100 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_101'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_101 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_102'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_102 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_reasoning_completion__mutmut['xǁDeepseekConnectorǁ_reasoning_completion__mutmut_103'] = DeepseekConnector.xǁDeepseekConnectorǁ_reasoning_completion__mutmut_103 # type: ignore # mutmut generated

mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['_mutmut_orig'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_1'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_2'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_3'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_4'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_5'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_6'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_7'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_8'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_9'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_10'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_11'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_12'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_13'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_14'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_15'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_16'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_17'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_18'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_19'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_20'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_21'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_21 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_22'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_22 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_23'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_23 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_24'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_24 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_25'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_25 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_26'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_26 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_27'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_27 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_28'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_28 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_29'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_29 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_30'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_30 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_31'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_31 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_32'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_32 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_33'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_33 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_34'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_34 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_35'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_35 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_36'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_36 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_37'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_37 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_38'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_38 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_39'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_39 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_40'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_40 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_41'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_41 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_42'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_42 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_43'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_43 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_44'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_44 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_45'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_45 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_46'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_46 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_47'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_47 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_48'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_48 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_49'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_49 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_50'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_50 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_51'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_51 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_52'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_52 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_53'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_53 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_54'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_54 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_55'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_55 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_56'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_56 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_57'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_57 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_58'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_58 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_59'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_59 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_60'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_60 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_61'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_61 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_62'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_62 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_63'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_63 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_64'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_64 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_65'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_65 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_66'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_66 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_67'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_67 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_68'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_68 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_69'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_69 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_70'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_70 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_71'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_71 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_72'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_72 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_73'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_73 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_74'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_74 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_75'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_75 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_76'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_76 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_77'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_77 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_78'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_78 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_79'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_79 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_80'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_80 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_81'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_81 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_82'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_82 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_83'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_83 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_84'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_84 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_85'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_85 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_86'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_86 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_87'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_87 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_88'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_88 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_89'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_89 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_90'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_90 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_91'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_91 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_92'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_92 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_93'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_93 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_94'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_94 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_95'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_95 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_96'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_96 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_97'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_97 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_98'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_98 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_99'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_99 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_100'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_100 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_101'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_101 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_102'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_102 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_code_completion__mutmut['xǁDeepseekConnectorǁ_code_completion__mutmut_103'] = DeepseekConnector.xǁDeepseekConnectorǁ_code_completion__mutmut_103 # type: ignore # mutmut generated

mutants_xǁDeepseekConnectorǁ_list_models__mutmut['_mutmut_orig'] = DeepseekConnector.xǁDeepseekConnectorǁ_list_models__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_list_models__mutmut['xǁDeepseekConnectorǁ_list_models__mutmut_1'] = DeepseekConnector.xǁDeepseekConnectorǁ_list_models__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_list_models__mutmut['xǁDeepseekConnectorǁ_list_models__mutmut_2'] = DeepseekConnector.xǁDeepseekConnectorǁ_list_models__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_list_models__mutmut['xǁDeepseekConnectorǁ_list_models__mutmut_3'] = DeepseekConnector.xǁDeepseekConnectorǁ_list_models__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_list_models__mutmut['xǁDeepseekConnectorǁ_list_models__mutmut_4'] = DeepseekConnector.xǁDeepseekConnectorǁ_list_models__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_list_models__mutmut['xǁDeepseekConnectorǁ_list_models__mutmut_5'] = DeepseekConnector.xǁDeepseekConnectorǁ_list_models__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_list_models__mutmut['xǁDeepseekConnectorǁ_list_models__mutmut_6'] = DeepseekConnector.xǁDeepseekConnectorǁ_list_models__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_list_models__mutmut['xǁDeepseekConnectorǁ_list_models__mutmut_7'] = DeepseekConnector.xǁDeepseekConnectorǁ_list_models__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_list_models__mutmut['xǁDeepseekConnectorǁ_list_models__mutmut_8'] = DeepseekConnector.xǁDeepseekConnectorǁ_list_models__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_list_models__mutmut['xǁDeepseekConnectorǁ_list_models__mutmut_9'] = DeepseekConnector.xǁDeepseekConnectorǁ_list_models__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_list_models__mutmut['xǁDeepseekConnectorǁ_list_models__mutmut_10'] = DeepseekConnector.xǁDeepseekConnectorǁ_list_models__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_list_models__mutmut['xǁDeepseekConnectorǁ_list_models__mutmut_11'] = DeepseekConnector.xǁDeepseekConnectorǁ_list_models__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_list_models__mutmut['xǁDeepseekConnectorǁ_list_models__mutmut_12'] = DeepseekConnector.xǁDeepseekConnectorǁ_list_models__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_list_models__mutmut['xǁDeepseekConnectorǁ_list_models__mutmut_13'] = DeepseekConnector.xǁDeepseekConnectorǁ_list_models__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_list_models__mutmut['xǁDeepseekConnectorǁ_list_models__mutmut_14'] = DeepseekConnector.xǁDeepseekConnectorǁ_list_models__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_list_models__mutmut['xǁDeepseekConnectorǁ_list_models__mutmut_15'] = DeepseekConnector.xǁDeepseekConnectorǁ_list_models__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_list_models__mutmut['xǁDeepseekConnectorǁ_list_models__mutmut_16'] = DeepseekConnector.xǁDeepseekConnectorǁ_list_models__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_list_models__mutmut['xǁDeepseekConnectorǁ_list_models__mutmut_17'] = DeepseekConnector.xǁDeepseekConnectorǁ_list_models__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_list_models__mutmut['xǁDeepseekConnectorǁ_list_models__mutmut_18'] = DeepseekConnector.xǁDeepseekConnectorǁ_list_models__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_list_models__mutmut['xǁDeepseekConnectorǁ_list_models__mutmut_19'] = DeepseekConnector.xǁDeepseekConnectorǁ_list_models__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_list_models__mutmut['xǁDeepseekConnectorǁ_list_models__mutmut_20'] = DeepseekConnector.xǁDeepseekConnectorǁ_list_models__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_list_models__mutmut['xǁDeepseekConnectorǁ_list_models__mutmut_21'] = DeepseekConnector.xǁDeepseekConnectorǁ_list_models__mutmut_21 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_list_models__mutmut['xǁDeepseekConnectorǁ_list_models__mutmut_22'] = DeepseekConnector.xǁDeepseekConnectorǁ_list_models__mutmut_22 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_list_models__mutmut['xǁDeepseekConnectorǁ_list_models__mutmut_23'] = DeepseekConnector.xǁDeepseekConnectorǁ_list_models__mutmut_23 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_list_models__mutmut['xǁDeepseekConnectorǁ_list_models__mutmut_24'] = DeepseekConnector.xǁDeepseekConnectorǁ_list_models__mutmut_24 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_list_models__mutmut['xǁDeepseekConnectorǁ_list_models__mutmut_25'] = DeepseekConnector.xǁDeepseekConnectorǁ_list_models__mutmut_25 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_list_models__mutmut['xǁDeepseekConnectorǁ_list_models__mutmut_26'] = DeepseekConnector.xǁDeepseekConnectorǁ_list_models__mutmut_26 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_list_models__mutmut['xǁDeepseekConnectorǁ_list_models__mutmut_27'] = DeepseekConnector.xǁDeepseekConnectorǁ_list_models__mutmut_27 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_list_models__mutmut['xǁDeepseekConnectorǁ_list_models__mutmut_28'] = DeepseekConnector.xǁDeepseekConnectorǁ_list_models__mutmut_28 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_list_models__mutmut['xǁDeepseekConnectorǁ_list_models__mutmut_29'] = DeepseekConnector.xǁDeepseekConnectorǁ_list_models__mutmut_29 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_list_models__mutmut['xǁDeepseekConnectorǁ_list_models__mutmut_30'] = DeepseekConnector.xǁDeepseekConnectorǁ_list_models__mutmut_30 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_list_models__mutmut['xǁDeepseekConnectorǁ_list_models__mutmut_31'] = DeepseekConnector.xǁDeepseekConnectorǁ_list_models__mutmut_31 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_list_models__mutmut['xǁDeepseekConnectorǁ_list_models__mutmut_32'] = DeepseekConnector.xǁDeepseekConnectorǁ_list_models__mutmut_32 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_list_models__mutmut['xǁDeepseekConnectorǁ_list_models__mutmut_33'] = DeepseekConnector.xǁDeepseekConnectorǁ_list_models__mutmut_33 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_list_models__mutmut['xǁDeepseekConnectorǁ_list_models__mutmut_34'] = DeepseekConnector.xǁDeepseekConnectorǁ_list_models__mutmut_34 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_list_models__mutmut['xǁDeepseekConnectorǁ_list_models__mutmut_35'] = DeepseekConnector.xǁDeepseekConnectorǁ_list_models__mutmut_35 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_list_models__mutmut['xǁDeepseekConnectorǁ_list_models__mutmut_36'] = DeepseekConnector.xǁDeepseekConnectorǁ_list_models__mutmut_36 # type: ignore # mutmut generated
mutants_xǁDeepseekConnectorǁ_list_models__mutmut['xǁDeepseekConnectorǁ_list_models__mutmut_37'] = DeepseekConnector.xǁDeepseekConnectorǁ_list_models__mutmut_37 # type: ignore # mutmut generated


DEEPSEEK_SCHEMA = ConnectorSchema(
    name="deepseek",
    version="1.0.0",
    description="Genera texto y razonamiento avanzado via DeepSeek AI",
    category="ai_data",
    icon="sparkles",
    author="Zenic-Flijo",
    actions=[
        ActionDefinition(name="chat_completion", description="Chat con DeepSeek", category="write"),
        ActionDefinition(name="reasoning_completion", description="Razonamiento extendido", category="write"),
        ActionDefinition(name="code_completion", description="Completacion de codigo", category="write"),
        ActionDefinition(name="list_models", description="Lista modelos", category="read"),
    ],
    auth_requirements=[
        AuthRequirement(auth_type="api_key", required_fields=["api_key"], description="DeepSeek API Key")
    ],
)
