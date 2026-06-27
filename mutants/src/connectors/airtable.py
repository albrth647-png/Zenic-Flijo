"""Conector Airtable — Bases de datos sin codigo API."""

from __future__ import annotations

from typing import Any

from src.core.logging import setup_logging
from src.sdk.base import BaseConnector
from src.sdk.http_client import HttpClient, HTTPClientError
from src.sdk.schema import ActionDefinition, AuthRequirement, ConnectorSchema

logger = setup_logging(__name__)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁAirtableConnectorǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁAirtableConnectorǁconnect__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAirtableConnectorǁexecute__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAirtableConnectorǁvalidate__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAirtableConnectorǁdisconnect__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAirtableConnectorǁ_api__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAirtableConnectorǁ_list_records__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAirtableConnectorǁ_get_record__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAirtableConnectorǁ_create_record__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAirtableConnectorǁ_update_record__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAirtableConnectorǁ_delete_record__mutmut: MutantDict = {}  # type: ignore


class AirtableConnector(BaseConnector):
    name = "airtable"
    version = "1.0.0"
    description = "Lee y escribe registros en bases de Airtable"
    category = "database"
    icon = "grid"
    author = "Zenic-Flijo"

    @_mutmut_mutated(mutants_xǁAirtableConnectorǁ__init____mutmut)
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._api_key: str = ""; self._base_id: str = ""; self._http: HttpClient | None = None

    def xǁAirtableConnectorǁ__init____mutmut_orig(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._api_key: str = ""; self._base_id: str = ""; self._http: HttpClient | None = None

    def xǁAirtableConnectorǁ__init____mutmut_1(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._api_key: str = None; self._base_id: str = ""; self._http: HttpClient | None = None

    def xǁAirtableConnectorǁ__init____mutmut_2(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._api_key: str = "XXXX"; self._base_id: str = ""; self._http: HttpClient | None = None

    def xǁAirtableConnectorǁ__init____mutmut_3(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._api_key: str = ""; self._base_id: str = None; self._http: HttpClient | None = None

    def xǁAirtableConnectorǁ__init____mutmut_4(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._api_key: str = ""; self._base_id: str = "XXXX"; self._http: HttpClient | None = None

    def xǁAirtableConnectorǁ__init____mutmut_5(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._api_key: str = ""; self._base_id: str = ""; self._http: HttpClient | None = ""

    @_mutmut_mutated(mutants_xǁAirtableConnectorǁconnect__mutmut)
    def connect(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_credentials"):
            c = self._auth_provider._credentials; self._api_key = c.get("api_key", ""); self._base_id = c.get("base_id", "")
        if not self._api_key or not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header("Authorization", f"Bearer {self._api_key}")
        self._connected = True; self._log_operation("connect", f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_orig(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_credentials"):
            c = self._auth_provider._credentials; self._api_key = c.get("api_key", ""); self._base_id = c.get("base_id", "")
        if not self._api_key or not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header("Authorization", f"Bearer {self._api_key}")
        self._connected = True; self._log_operation("connect", f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_1(self) -> bool:
        if not self._auth_provider and not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_credentials"):
            c = self._auth_provider._credentials; self._api_key = c.get("api_key", ""); self._base_id = c.get("base_id", "")
        if not self._api_key or not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header("Authorization", f"Bearer {self._api_key}")
        self._connected = True; self._log_operation("connect", f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_2(self) -> bool:
        if self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_credentials"):
            c = self._auth_provider._credentials; self._api_key = c.get("api_key", ""); self._base_id = c.get("base_id", "")
        if not self._api_key or not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header("Authorization", f"Bearer {self._api_key}")
        self._connected = True; self._log_operation("connect", f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_3(self) -> bool:
        if not self._auth_provider or self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_credentials"):
            c = self._auth_provider._credentials; self._api_key = c.get("api_key", ""); self._base_id = c.get("base_id", "")
        if not self._api_key or not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header("Authorization", f"Bearer {self._api_key}")
        self._connected = True; self._log_operation("connect", f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_4(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return True
        if hasattr(self._auth_provider, "_credentials"):
            c = self._auth_provider._credentials; self._api_key = c.get("api_key", ""); self._base_id = c.get("base_id", "")
        if not self._api_key or not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header("Authorization", f"Bearer {self._api_key}")
        self._connected = True; self._log_operation("connect", f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_5(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(None, "_credentials"):
            c = self._auth_provider._credentials; self._api_key = c.get("api_key", ""); self._base_id = c.get("base_id", "")
        if not self._api_key or not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header("Authorization", f"Bearer {self._api_key}")
        self._connected = True; self._log_operation("connect", f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_6(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, None):
            c = self._auth_provider._credentials; self._api_key = c.get("api_key", ""); self._base_id = c.get("base_id", "")
        if not self._api_key or not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header("Authorization", f"Bearer {self._api_key}")
        self._connected = True; self._log_operation("connect", f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_7(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr("_credentials"):
            c = self._auth_provider._credentials; self._api_key = c.get("api_key", ""); self._base_id = c.get("base_id", "")
        if not self._api_key or not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header("Authorization", f"Bearer {self._api_key}")
        self._connected = True; self._log_operation("connect", f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_8(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, ):
            c = self._auth_provider._credentials; self._api_key = c.get("api_key", ""); self._base_id = c.get("base_id", "")
        if not self._api_key or not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header("Authorization", f"Bearer {self._api_key}")
        self._connected = True; self._log_operation("connect", f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_9(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "XX_credentialsXX"):
            c = self._auth_provider._credentials; self._api_key = c.get("api_key", ""); self._base_id = c.get("base_id", "")
        if not self._api_key or not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header("Authorization", f"Bearer {self._api_key}")
        self._connected = True; self._log_operation("connect", f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_10(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_CREDENTIALS"):
            c = self._auth_provider._credentials; self._api_key = c.get("api_key", ""); self._base_id = c.get("base_id", "")
        if not self._api_key or not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header("Authorization", f"Bearer {self._api_key}")
        self._connected = True; self._log_operation("connect", f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_11(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_credentials"):
            c = None; self._api_key = c.get("api_key", ""); self._base_id = c.get("base_id", "")
        if not self._api_key or not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header("Authorization", f"Bearer {self._api_key}")
        self._connected = True; self._log_operation("connect", f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_12(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_credentials"):
            c = self._auth_provider._credentials; self._api_key = None; self._base_id = c.get("base_id", "")
        if not self._api_key or not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header("Authorization", f"Bearer {self._api_key}")
        self._connected = True; self._log_operation("connect", f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_13(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_credentials"):
            c = self._auth_provider._credentials; self._api_key = c.get(None, ""); self._base_id = c.get("base_id", "")
        if not self._api_key or not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header("Authorization", f"Bearer {self._api_key}")
        self._connected = True; self._log_operation("connect", f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_14(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_credentials"):
            c = self._auth_provider._credentials; self._api_key = c.get("api_key", None); self._base_id = c.get("base_id", "")
        if not self._api_key or not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header("Authorization", f"Bearer {self._api_key}")
        self._connected = True; self._log_operation("connect", f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_15(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_credentials"):
            c = self._auth_provider._credentials; self._api_key = c.get(""); self._base_id = c.get("base_id", "")
        if not self._api_key or not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header("Authorization", f"Bearer {self._api_key}")
        self._connected = True; self._log_operation("connect", f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_16(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_credentials"):
            c = self._auth_provider._credentials; self._api_key = c.get("api_key", ); self._base_id = c.get("base_id", "")
        if not self._api_key or not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header("Authorization", f"Bearer {self._api_key}")
        self._connected = True; self._log_operation("connect", f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_17(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_credentials"):
            c = self._auth_provider._credentials; self._api_key = c.get("XXapi_keyXX", ""); self._base_id = c.get("base_id", "")
        if not self._api_key or not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header("Authorization", f"Bearer {self._api_key}")
        self._connected = True; self._log_operation("connect", f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_18(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_credentials"):
            c = self._auth_provider._credentials; self._api_key = c.get("API_KEY", ""); self._base_id = c.get("base_id", "")
        if not self._api_key or not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header("Authorization", f"Bearer {self._api_key}")
        self._connected = True; self._log_operation("connect", f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_19(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_credentials"):
            c = self._auth_provider._credentials; self._api_key = c.get("api_key", "XXXX"); self._base_id = c.get("base_id", "")
        if not self._api_key or not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header("Authorization", f"Bearer {self._api_key}")
        self._connected = True; self._log_operation("connect", f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_20(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_credentials"):
            c = self._auth_provider._credentials; self._api_key = c.get("api_key", ""); self._base_id = None
        if not self._api_key or not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header("Authorization", f"Bearer {self._api_key}")
        self._connected = True; self._log_operation("connect", f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_21(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_credentials"):
            c = self._auth_provider._credentials; self._api_key = c.get("api_key", ""); self._base_id = c.get(None, "")
        if not self._api_key or not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header("Authorization", f"Bearer {self._api_key}")
        self._connected = True; self._log_operation("connect", f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_22(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_credentials"):
            c = self._auth_provider._credentials; self._api_key = c.get("api_key", ""); self._base_id = c.get("base_id", None)
        if not self._api_key or not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header("Authorization", f"Bearer {self._api_key}")
        self._connected = True; self._log_operation("connect", f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_23(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_credentials"):
            c = self._auth_provider._credentials; self._api_key = c.get("api_key", ""); self._base_id = c.get("")
        if not self._api_key or not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header("Authorization", f"Bearer {self._api_key}")
        self._connected = True; self._log_operation("connect", f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_24(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_credentials"):
            c = self._auth_provider._credentials; self._api_key = c.get("api_key", ""); self._base_id = c.get("base_id", )
        if not self._api_key or not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header("Authorization", f"Bearer {self._api_key}")
        self._connected = True; self._log_operation("connect", f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_25(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_credentials"):
            c = self._auth_provider._credentials; self._api_key = c.get("api_key", ""); self._base_id = c.get("XXbase_idXX", "")
        if not self._api_key or not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header("Authorization", f"Bearer {self._api_key}")
        self._connected = True; self._log_operation("connect", f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_26(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_credentials"):
            c = self._auth_provider._credentials; self._api_key = c.get("api_key", ""); self._base_id = c.get("BASE_ID", "")
        if not self._api_key or not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header("Authorization", f"Bearer {self._api_key}")
        self._connected = True; self._log_operation("connect", f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_27(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_credentials"):
            c = self._auth_provider._credentials; self._api_key = c.get("api_key", ""); self._base_id = c.get("base_id", "XXXX")
        if not self._api_key or not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header("Authorization", f"Bearer {self._api_key}")
        self._connected = True; self._log_operation("connect", f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_28(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_credentials"):
            c = self._auth_provider._credentials; self._api_key = c.get("api_key", ""); self._base_id = c.get("base_id", "")
        if not self._api_key and not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header("Authorization", f"Bearer {self._api_key}")
        self._connected = True; self._log_operation("connect", f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_29(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_credentials"):
            c = self._auth_provider._credentials; self._api_key = c.get("api_key", ""); self._base_id = c.get("base_id", "")
        if self._api_key or not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header("Authorization", f"Bearer {self._api_key}")
        self._connected = True; self._log_operation("connect", f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_30(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_credentials"):
            c = self._auth_provider._credentials; self._api_key = c.get("api_key", ""); self._base_id = c.get("base_id", "")
        if not self._api_key or self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header("Authorization", f"Bearer {self._api_key}")
        self._connected = True; self._log_operation("connect", f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_31(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_credentials"):
            c = self._auth_provider._credentials; self._api_key = c.get("api_key", ""); self._base_id = c.get("base_id", "")
        if not self._api_key or not self._base_id:
            logger.error(None); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header("Authorization", f"Bearer {self._api_key}")
        self._connected = True; self._log_operation("connect", f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_32(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_credentials"):
            c = self._auth_provider._credentials; self._api_key = c.get("api_key", ""); self._base_id = c.get("base_id", "")
        if not self._api_key or not self._base_id:
            logger.error("XXAirtable: api_key y base_id requeridosXX"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header("Authorization", f"Bearer {self._api_key}")
        self._connected = True; self._log_operation("connect", f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_33(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_credentials"):
            c = self._auth_provider._credentials; self._api_key = c.get("api_key", ""); self._base_id = c.get("base_id", "")
        if not self._api_key or not self._base_id:
            logger.error("airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header("Authorization", f"Bearer {self._api_key}")
        self._connected = True; self._log_operation("connect", f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_34(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_credentials"):
            c = self._auth_provider._credentials; self._api_key = c.get("api_key", ""); self._base_id = c.get("base_id", "")
        if not self._api_key or not self._base_id:
            logger.error("AIRTABLE: API_KEY Y BASE_ID REQUERIDOS"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header("Authorization", f"Bearer {self._api_key}")
        self._connected = True; self._log_operation("connect", f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_35(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_credentials"):
            c = self._auth_provider._credentials; self._api_key = c.get("api_key", ""); self._base_id = c.get("base_id", "")
        if not self._api_key or not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return True
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header("Authorization", f"Bearer {self._api_key}")
        self._connected = True; self._log_operation("connect", f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_36(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_credentials"):
            c = self._auth_provider._credentials; self._api_key = c.get("api_key", ""); self._base_id = c.get("base_id", "")
        if not self._api_key or not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = None
        self._http.set_header("Authorization", f"Bearer {self._api_key}")
        self._connected = True; self._log_operation("connect", f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_37(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_credentials"):
            c = self._auth_provider._credentials; self._api_key = c.get("api_key", ""); self._base_id = c.get("base_id", "")
        if not self._api_key or not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(base_url=None, connector_name=self.name)
        self._http.set_header("Authorization", f"Bearer {self._api_key}")
        self._connected = True; self._log_operation("connect", f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_38(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_credentials"):
            c = self._auth_provider._credentials; self._api_key = c.get("api_key", ""); self._base_id = c.get("base_id", "")
        if not self._api_key or not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=None)
        self._http.set_header("Authorization", f"Bearer {self._api_key}")
        self._connected = True; self._log_operation("connect", f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_39(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_credentials"):
            c = self._auth_provider._credentials; self._api_key = c.get("api_key", ""); self._base_id = c.get("base_id", "")
        if not self._api_key or not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(connector_name=self.name)
        self._http.set_header("Authorization", f"Bearer {self._api_key}")
        self._connected = True; self._log_operation("connect", f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_40(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_credentials"):
            c = self._auth_provider._credentials; self._api_key = c.get("api_key", ""); self._base_id = c.get("base_id", "")
        if not self._api_key or not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", )
        self._http.set_header("Authorization", f"Bearer {self._api_key}")
        self._connected = True; self._log_operation("connect", f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_41(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_credentials"):
            c = self._auth_provider._credentials; self._api_key = c.get("api_key", ""); self._base_id = c.get("base_id", "")
        if not self._api_key or not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header(None, f"Bearer {self._api_key}")
        self._connected = True; self._log_operation("connect", f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_42(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_credentials"):
            c = self._auth_provider._credentials; self._api_key = c.get("api_key", ""); self._base_id = c.get("base_id", "")
        if not self._api_key or not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header("Authorization", None)
        self._connected = True; self._log_operation("connect", f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_43(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_credentials"):
            c = self._auth_provider._credentials; self._api_key = c.get("api_key", ""); self._base_id = c.get("base_id", "")
        if not self._api_key or not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header(f"Bearer {self._api_key}")
        self._connected = True; self._log_operation("connect", f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_44(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_credentials"):
            c = self._auth_provider._credentials; self._api_key = c.get("api_key", ""); self._base_id = c.get("base_id", "")
        if not self._api_key or not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header("Authorization", )
        self._connected = True; self._log_operation("connect", f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_45(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_credentials"):
            c = self._auth_provider._credentials; self._api_key = c.get("api_key", ""); self._base_id = c.get("base_id", "")
        if not self._api_key or not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header("XXAuthorizationXX", f"Bearer {self._api_key}")
        self._connected = True; self._log_operation("connect", f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_46(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_credentials"):
            c = self._auth_provider._credentials; self._api_key = c.get("api_key", ""); self._base_id = c.get("base_id", "")
        if not self._api_key or not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header("authorization", f"Bearer {self._api_key}")
        self._connected = True; self._log_operation("connect", f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_47(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_credentials"):
            c = self._auth_provider._credentials; self._api_key = c.get("api_key", ""); self._base_id = c.get("base_id", "")
        if not self._api_key or not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header("AUTHORIZATION", f"Bearer {self._api_key}")
        self._connected = True; self._log_operation("connect", f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_48(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_credentials"):
            c = self._auth_provider._credentials; self._api_key = c.get("api_key", ""); self._base_id = c.get("base_id", "")
        if not self._api_key or not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header("Authorization", f"Bearer {self._api_key}")
        self._connected = None; self._log_operation("connect", f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_49(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_credentials"):
            c = self._auth_provider._credentials; self._api_key = c.get("api_key", ""); self._base_id = c.get("base_id", "")
        if not self._api_key or not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header("Authorization", f"Bearer {self._api_key}")
        self._connected = False; self._log_operation("connect", f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_50(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_credentials"):
            c = self._auth_provider._credentials; self._api_key = c.get("api_key", ""); self._base_id = c.get("base_id", "")
        if not self._api_key or not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header("Authorization", f"Bearer {self._api_key}")
        self._connected = True; self._log_operation(None, f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_51(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_credentials"):
            c = self._auth_provider._credentials; self._api_key = c.get("api_key", ""); self._base_id = c.get("base_id", "")
        if not self._api_key or not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header("Authorization", f"Bearer {self._api_key}")
        self._connected = True; self._log_operation("connect", None); return True

    def xǁAirtableConnectorǁconnect__mutmut_52(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_credentials"):
            c = self._auth_provider._credentials; self._api_key = c.get("api_key", ""); self._base_id = c.get("base_id", "")
        if not self._api_key or not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header("Authorization", f"Bearer {self._api_key}")
        self._connected = True; self._log_operation(f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_53(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_credentials"):
            c = self._auth_provider._credentials; self._api_key = c.get("api_key", ""); self._base_id = c.get("base_id", "")
        if not self._api_key or not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header("Authorization", f"Bearer {self._api_key}")
        self._connected = True; self._log_operation("connect", ); return True

    def xǁAirtableConnectorǁconnect__mutmut_54(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_credentials"):
            c = self._auth_provider._credentials; self._api_key = c.get("api_key", ""); self._base_id = c.get("base_id", "")
        if not self._api_key or not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header("Authorization", f"Bearer {self._api_key}")
        self._connected = True; self._log_operation("XXconnectXX", f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_55(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_credentials"):
            c = self._auth_provider._credentials; self._api_key = c.get("api_key", ""); self._base_id = c.get("base_id", "")
        if not self._api_key or not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header("Authorization", f"Bearer {self._api_key}")
        self._connected = True; self._log_operation("CONNECT", f"base={self._base_id[:6]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_56(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_credentials"):
            c = self._auth_provider._credentials; self._api_key = c.get("api_key", ""); self._base_id = c.get("base_id", "")
        if not self._api_key or not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header("Authorization", f"Bearer {self._api_key}")
        self._connected = True; self._log_operation("connect", f"base={self._base_id[:7]}..."); return True

    def xǁAirtableConnectorǁconnect__mutmut_57(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_credentials"):
            c = self._auth_provider._credentials; self._api_key = c.get("api_key", ""); self._base_id = c.get("base_id", "")
        if not self._api_key or not self._base_id:
            logger.error("Airtable: api_key y base_id requeridos"); return False
        self._http = HttpClient(base_url=f"https://api.airtable.com/v0/{self._base_id}", connector_name=self.name)
        self._http.set_header("Authorization", f"Bearer {self._api_key}")
        self._connected = True; self._log_operation("connect", f"base={self._base_id[:6]}..."); return False

    @_mutmut_mutated(mutants_xǁAirtableConnectorǁexecute__mutmut)
    def execute(self, action: str, params: dict[str, Any]) -> Any:
        action_map = {"list_records": self._list_records, "get_record": self._get_record, "create_record": self._create_record,
                       "update_record": self._update_record, "delete_record": self._delete_record}
        handler = action_map.get(action)
        return handler(params) if handler else {"error": f"Accion '{action}' no soportada", "available": list(action_map.keys())}

    def xǁAirtableConnectorǁexecute__mutmut_orig(self, action: str, params: dict[str, Any]) -> Any:
        action_map = {"list_records": self._list_records, "get_record": self._get_record, "create_record": self._create_record,
                       "update_record": self._update_record, "delete_record": self._delete_record}
        handler = action_map.get(action)
        return handler(params) if handler else {"error": f"Accion '{action}' no soportada", "available": list(action_map.keys())}

    def xǁAirtableConnectorǁexecute__mutmut_1(self, action: str, params: dict[str, Any]) -> Any:
        action_map = None
        handler = action_map.get(action)
        return handler(params) if handler else {"error": f"Accion '{action}' no soportada", "available": list(action_map.keys())}

    def xǁAirtableConnectorǁexecute__mutmut_2(self, action: str, params: dict[str, Any]) -> Any:
        action_map = {"XXlist_recordsXX": self._list_records, "get_record": self._get_record, "create_record": self._create_record,
                       "update_record": self._update_record, "delete_record": self._delete_record}
        handler = action_map.get(action)
        return handler(params) if handler else {"error": f"Accion '{action}' no soportada", "available": list(action_map.keys())}

    def xǁAirtableConnectorǁexecute__mutmut_3(self, action: str, params: dict[str, Any]) -> Any:
        action_map = {"LIST_RECORDS": self._list_records, "get_record": self._get_record, "create_record": self._create_record,
                       "update_record": self._update_record, "delete_record": self._delete_record}
        handler = action_map.get(action)
        return handler(params) if handler else {"error": f"Accion '{action}' no soportada", "available": list(action_map.keys())}

    def xǁAirtableConnectorǁexecute__mutmut_4(self, action: str, params: dict[str, Any]) -> Any:
        action_map = {"list_records": self._list_records, "XXget_recordXX": self._get_record, "create_record": self._create_record,
                       "update_record": self._update_record, "delete_record": self._delete_record}
        handler = action_map.get(action)
        return handler(params) if handler else {"error": f"Accion '{action}' no soportada", "available": list(action_map.keys())}

    def xǁAirtableConnectorǁexecute__mutmut_5(self, action: str, params: dict[str, Any]) -> Any:
        action_map = {"list_records": self._list_records, "GET_RECORD": self._get_record, "create_record": self._create_record,
                       "update_record": self._update_record, "delete_record": self._delete_record}
        handler = action_map.get(action)
        return handler(params) if handler else {"error": f"Accion '{action}' no soportada", "available": list(action_map.keys())}

    def xǁAirtableConnectorǁexecute__mutmut_6(self, action: str, params: dict[str, Any]) -> Any:
        action_map = {"list_records": self._list_records, "get_record": self._get_record, "XXcreate_recordXX": self._create_record,
                       "update_record": self._update_record, "delete_record": self._delete_record}
        handler = action_map.get(action)
        return handler(params) if handler else {"error": f"Accion '{action}' no soportada", "available": list(action_map.keys())}

    def xǁAirtableConnectorǁexecute__mutmut_7(self, action: str, params: dict[str, Any]) -> Any:
        action_map = {"list_records": self._list_records, "get_record": self._get_record, "CREATE_RECORD": self._create_record,
                       "update_record": self._update_record, "delete_record": self._delete_record}
        handler = action_map.get(action)
        return handler(params) if handler else {"error": f"Accion '{action}' no soportada", "available": list(action_map.keys())}

    def xǁAirtableConnectorǁexecute__mutmut_8(self, action: str, params: dict[str, Any]) -> Any:
        action_map = {"list_records": self._list_records, "get_record": self._get_record, "create_record": self._create_record,
                       "XXupdate_recordXX": self._update_record, "delete_record": self._delete_record}
        handler = action_map.get(action)
        return handler(params) if handler else {"error": f"Accion '{action}' no soportada", "available": list(action_map.keys())}

    def xǁAirtableConnectorǁexecute__mutmut_9(self, action: str, params: dict[str, Any]) -> Any:
        action_map = {"list_records": self._list_records, "get_record": self._get_record, "create_record": self._create_record,
                       "UPDATE_RECORD": self._update_record, "delete_record": self._delete_record}
        handler = action_map.get(action)
        return handler(params) if handler else {"error": f"Accion '{action}' no soportada", "available": list(action_map.keys())}

    def xǁAirtableConnectorǁexecute__mutmut_10(self, action: str, params: dict[str, Any]) -> Any:
        action_map = {"list_records": self._list_records, "get_record": self._get_record, "create_record": self._create_record,
                       "update_record": self._update_record, "XXdelete_recordXX": self._delete_record}
        handler = action_map.get(action)
        return handler(params) if handler else {"error": f"Accion '{action}' no soportada", "available": list(action_map.keys())}

    def xǁAirtableConnectorǁexecute__mutmut_11(self, action: str, params: dict[str, Any]) -> Any:
        action_map = {"list_records": self._list_records, "get_record": self._get_record, "create_record": self._create_record,
                       "update_record": self._update_record, "DELETE_RECORD": self._delete_record}
        handler = action_map.get(action)
        return handler(params) if handler else {"error": f"Accion '{action}' no soportada", "available": list(action_map.keys())}

    def xǁAirtableConnectorǁexecute__mutmut_12(self, action: str, params: dict[str, Any]) -> Any:
        action_map = {"list_records": self._list_records, "get_record": self._get_record, "create_record": self._create_record,
                       "update_record": self._update_record, "delete_record": self._delete_record}
        handler = None
        return handler(params) if handler else {"error": f"Accion '{action}' no soportada", "available": list(action_map.keys())}

    def xǁAirtableConnectorǁexecute__mutmut_13(self, action: str, params: dict[str, Any]) -> Any:
        action_map = {"list_records": self._list_records, "get_record": self._get_record, "create_record": self._create_record,
                       "update_record": self._update_record, "delete_record": self._delete_record}
        handler = action_map.get(None)
        return handler(params) if handler else {"error": f"Accion '{action}' no soportada", "available": list(action_map.keys())}

    def xǁAirtableConnectorǁexecute__mutmut_14(self, action: str, params: dict[str, Any]) -> Any:
        action_map = {"list_records": self._list_records, "get_record": self._get_record, "create_record": self._create_record,
                       "update_record": self._update_record, "delete_record": self._delete_record}
        handler = action_map.get(action)
        return handler(None) if handler else {"error": f"Accion '{action}' no soportada", "available": list(action_map.keys())}

    def xǁAirtableConnectorǁexecute__mutmut_15(self, action: str, params: dict[str, Any]) -> Any:
        action_map = {"list_records": self._list_records, "get_record": self._get_record, "create_record": self._create_record,
                       "update_record": self._update_record, "delete_record": self._delete_record}
        handler = action_map.get(action)
        return handler(params) if handler else {"XXerrorXX": f"Accion '{action}' no soportada", "available": list(action_map.keys())}

    def xǁAirtableConnectorǁexecute__mutmut_16(self, action: str, params: dict[str, Any]) -> Any:
        action_map = {"list_records": self._list_records, "get_record": self._get_record, "create_record": self._create_record,
                       "update_record": self._update_record, "delete_record": self._delete_record}
        handler = action_map.get(action)
        return handler(params) if handler else {"ERROR": f"Accion '{action}' no soportada", "available": list(action_map.keys())}

    def xǁAirtableConnectorǁexecute__mutmut_17(self, action: str, params: dict[str, Any]) -> Any:
        action_map = {"list_records": self._list_records, "get_record": self._get_record, "create_record": self._create_record,
                       "update_record": self._update_record, "delete_record": self._delete_record}
        handler = action_map.get(action)
        return handler(params) if handler else {"error": f"Accion '{action}' no soportada", "XXavailableXX": list(action_map.keys())}

    def xǁAirtableConnectorǁexecute__mutmut_18(self, action: str, params: dict[str, Any]) -> Any:
        action_map = {"list_records": self._list_records, "get_record": self._get_record, "create_record": self._create_record,
                       "update_record": self._update_record, "delete_record": self._delete_record}
        handler = action_map.get(action)
        return handler(params) if handler else {"error": f"Accion '{action}' no soportada", "AVAILABLE": list(action_map.keys())}

    def xǁAirtableConnectorǁexecute__mutmut_19(self, action: str, params: dict[str, Any]) -> Any:
        action_map = {"list_records": self._list_records, "get_record": self._get_record, "create_record": self._create_record,
                       "update_record": self._update_record, "delete_record": self._delete_record}
        handler = action_map.get(action)
        return handler(params) if handler else {"error": f"Accion '{action}' no soportada", "available": list(None)}

    @_mutmut_mutated(mutants_xǁAirtableConnectorǁvalidate__mutmut)
    def validate(self) -> bool: return bool(self._auth_provider and self._auth_provider.validate())

    def xǁAirtableConnectorǁvalidate__mutmut_orig(self) -> bool: return bool(self._auth_provider and self._auth_provider.validate())

    def xǁAirtableConnectorǁvalidate__mutmut_1(self) -> bool: return bool(None)

    def xǁAirtableConnectorǁvalidate__mutmut_2(self) -> bool: return bool(self._auth_provider or self._auth_provider.validate())
    @_mutmut_mutated(mutants_xǁAirtableConnectorǁdisconnect__mutmut)
    def disconnect(self) -> bool: self._connected = False; self._http = None; self._log_operation("disconnect"); return True
    def xǁAirtableConnectorǁdisconnect__mutmut_orig(self) -> bool: self._connected = False; self._http = None; self._log_operation("disconnect"); return True
    def xǁAirtableConnectorǁdisconnect__mutmut_1(self) -> bool: self._connected = None; self._http = None; self._log_operation("disconnect"); return True
    def xǁAirtableConnectorǁdisconnect__mutmut_2(self) -> bool: self._connected = True; self._http = None; self._log_operation("disconnect"); return True
    def xǁAirtableConnectorǁdisconnect__mutmut_3(self) -> bool: self._connected = False; self._http = ""; self._log_operation("disconnect"); return True
    def xǁAirtableConnectorǁdisconnect__mutmut_4(self) -> bool: self._connected = False; self._http = None; self._log_operation(None); return True
    def xǁAirtableConnectorǁdisconnect__mutmut_5(self) -> bool: self._connected = False; self._http = None; self._log_operation("XXdisconnectXX"); return True
    def xǁAirtableConnectorǁdisconnect__mutmut_6(self) -> bool: self._connected = False; self._http = None; self._log_operation("DISCONNECT"); return True
    def xǁAirtableConnectorǁdisconnect__mutmut_7(self) -> bool: self._connected = False; self._http = None; self._log_operation("disconnect"); return False

    @_mutmut_mutated(mutants_xǁAirtableConnectorǁ_api__mutmut)
    def _api(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_orig(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_1(self, method: str, path: str, **kw: Any) -> dict:
        if self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_2(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"XXsuccessXX": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_3(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"SUCCESS": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_4(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": True, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_5(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "XXerrorXX": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_6(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "ERROR": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_7(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "XXNot connectedXX"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_8(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_9(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "NOT CONNECTED"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_10(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = None
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_11(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(None, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_12(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(**kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_13(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, )
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_14(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(None, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_15(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, None)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_16(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_17(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, )(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_18(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = None
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_19(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") or callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_20(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(None, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_21(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, None) and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_22(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr("json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_23(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, ) and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_24(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "XXjsonXX") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_25(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "JSON") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_26(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(None) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_27(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"XXsuccessXX": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_28(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"SUCCESS": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_29(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": False, "data": d.get("records", d)}
            return {"success": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_30(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "XXdataXX": d.get("records", d)}
            return {"success": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_31(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "DATA": d.get("records", d)}
            return {"success": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_32(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get(None, d)}
            return {"success": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_33(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", None)}
            return {"success": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_34(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get(d)}
            return {"success": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_35(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", )}
            return {"success": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_36(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("XXrecordsXX", d)}
            return {"success": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_37(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("RECORDS", d)}
            return {"success": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_38(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"XXsuccessXX": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_39(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"SUCCESS": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_40(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": True, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_41(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "XXerrorXX": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_42(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "ERROR": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_43(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get("error", {}).get(None, f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_44(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get("error", {}).get("message", None)}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_45(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get("error", {}).get(f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_46(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get("error", {}).get("message", )}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_47(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get(None, {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_48(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get("error", None).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_49(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get({}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_50(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get("error", ).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_51(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get("XXerrorXX", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_52(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get("ERROR", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_53(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get("error", {}).get("XXmessageXX", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_54(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get("error", {}).get("MESSAGE", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_55(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"XXsuccessXX": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_56(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"SUCCESS": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_57(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": True, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_58(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "XXerrorXX": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_59(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "ERROR": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_60(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(None)}
        except Exception as e: return {"success": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_61(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"XXsuccessXX": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_62(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"SUCCESS": False, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_63(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": True, "error": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_64(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "XXerrorXX": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_65(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "ERROR": str(e)}

    def xǁAirtableConnectorǁ_api__mutmut_66(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("records", d)}
            return {"success": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(None)}

    @_mutmut_mutated(mutants_xǁAirtableConnectorǁ_list_records__mutmut)
    def _list_records(self, p: dict) -> dict:
        table = p.pop("table", ""); return self._api("get", f"/{table}", params=p) if table else {"success": False, "error": "table requerido"}

    def xǁAirtableConnectorǁ_list_records__mutmut_orig(self, p: dict) -> dict:
        table = p.pop("table", ""); return self._api("get", f"/{table}", params=p) if table else {"success": False, "error": "table requerido"}

    def xǁAirtableConnectorǁ_list_records__mutmut_1(self, p: dict) -> dict:
        table = None; return self._api("get", f"/{table}", params=p) if table else {"success": False, "error": "table requerido"}

    def xǁAirtableConnectorǁ_list_records__mutmut_2(self, p: dict) -> dict:
        table = p.pop(None, ""); return self._api("get", f"/{table}", params=p) if table else {"success": False, "error": "table requerido"}

    def xǁAirtableConnectorǁ_list_records__mutmut_3(self, p: dict) -> dict:
        table = p.pop("table", None); return self._api("get", f"/{table}", params=p) if table else {"success": False, "error": "table requerido"}

    def xǁAirtableConnectorǁ_list_records__mutmut_4(self, p: dict) -> dict:
        table = p.pop(""); return self._api("get", f"/{table}", params=p) if table else {"success": False, "error": "table requerido"}

    def xǁAirtableConnectorǁ_list_records__mutmut_5(self, p: dict) -> dict:
        table = p.pop("table", ); return self._api("get", f"/{table}", params=p) if table else {"success": False, "error": "table requerido"}

    def xǁAirtableConnectorǁ_list_records__mutmut_6(self, p: dict) -> dict:
        table = p.pop("XXtableXX", ""); return self._api("get", f"/{table}", params=p) if table else {"success": False, "error": "table requerido"}

    def xǁAirtableConnectorǁ_list_records__mutmut_7(self, p: dict) -> dict:
        table = p.pop("TABLE", ""); return self._api("get", f"/{table}", params=p) if table else {"success": False, "error": "table requerido"}

    def xǁAirtableConnectorǁ_list_records__mutmut_8(self, p: dict) -> dict:
        table = p.pop("table", "XXXX"); return self._api("get", f"/{table}", params=p) if table else {"success": False, "error": "table requerido"}

    def xǁAirtableConnectorǁ_list_records__mutmut_9(self, p: dict) -> dict:
        table = p.pop("table", ""); return self._api(None, f"/{table}", params=p) if table else {"success": False, "error": "table requerido"}

    def xǁAirtableConnectorǁ_list_records__mutmut_10(self, p: dict) -> dict:
        table = p.pop("table", ""); return self._api("get", None, params=p) if table else {"success": False, "error": "table requerido"}

    def xǁAirtableConnectorǁ_list_records__mutmut_11(self, p: dict) -> dict:
        table = p.pop("table", ""); return self._api("get", f"/{table}", params=None) if table else {"success": False, "error": "table requerido"}

    def xǁAirtableConnectorǁ_list_records__mutmut_12(self, p: dict) -> dict:
        table = p.pop("table", ""); return self._api(f"/{table}", params=p) if table else {"success": False, "error": "table requerido"}

    def xǁAirtableConnectorǁ_list_records__mutmut_13(self, p: dict) -> dict:
        table = p.pop("table", ""); return self._api("get", params=p) if table else {"success": False, "error": "table requerido"}

    def xǁAirtableConnectorǁ_list_records__mutmut_14(self, p: dict) -> dict:
        table = p.pop("table", ""); return self._api("get", f"/{table}", ) if table else {"success": False, "error": "table requerido"}

    def xǁAirtableConnectorǁ_list_records__mutmut_15(self, p: dict) -> dict:
        table = p.pop("table", ""); return self._api("XXgetXX", f"/{table}", params=p) if table else {"success": False, "error": "table requerido"}

    def xǁAirtableConnectorǁ_list_records__mutmut_16(self, p: dict) -> dict:
        table = p.pop("table", ""); return self._api("GET", f"/{table}", params=p) if table else {"success": False, "error": "table requerido"}

    def xǁAirtableConnectorǁ_list_records__mutmut_17(self, p: dict) -> dict:
        table = p.pop("table", ""); return self._api("get", f"/{table}", params=p) if table else {"XXsuccessXX": False, "error": "table requerido"}

    def xǁAirtableConnectorǁ_list_records__mutmut_18(self, p: dict) -> dict:
        table = p.pop("table", ""); return self._api("get", f"/{table}", params=p) if table else {"SUCCESS": False, "error": "table requerido"}

    def xǁAirtableConnectorǁ_list_records__mutmut_19(self, p: dict) -> dict:
        table = p.pop("table", ""); return self._api("get", f"/{table}", params=p) if table else {"success": True, "error": "table requerido"}

    def xǁAirtableConnectorǁ_list_records__mutmut_20(self, p: dict) -> dict:
        table = p.pop("table", ""); return self._api("get", f"/{table}", params=p) if table else {"success": False, "XXerrorXX": "table requerido"}

    def xǁAirtableConnectorǁ_list_records__mutmut_21(self, p: dict) -> dict:
        table = p.pop("table", ""); return self._api("get", f"/{table}", params=p) if table else {"success": False, "ERROR": "table requerido"}

    def xǁAirtableConnectorǁ_list_records__mutmut_22(self, p: dict) -> dict:
        table = p.pop("table", ""); return self._api("get", f"/{table}", params=p) if table else {"success": False, "error": "XXtable requeridoXX"}

    def xǁAirtableConnectorǁ_list_records__mutmut_23(self, p: dict) -> dict:
        table = p.pop("table", ""); return self._api("get", f"/{table}", params=p) if table else {"success": False, "error": "TABLE REQUERIDO"}
    @_mutmut_mutated(mutants_xǁAirtableConnectorǁ_get_record__mutmut)
    def _get_record(self, p: dict) -> dict:
        table = p.get("table", ""); rec_id = p.get("record_id", "")
        return self._api("get", f"/{table}/{rec_id}") if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_get_record__mutmut_orig(self, p: dict) -> dict:
        table = p.get("table", ""); rec_id = p.get("record_id", "")
        return self._api("get", f"/{table}/{rec_id}") if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_get_record__mutmut_1(self, p: dict) -> dict:
        table = None; rec_id = p.get("record_id", "")
        return self._api("get", f"/{table}/{rec_id}") if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_get_record__mutmut_2(self, p: dict) -> dict:
        table = p.get(None, ""); rec_id = p.get("record_id", "")
        return self._api("get", f"/{table}/{rec_id}") if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_get_record__mutmut_3(self, p: dict) -> dict:
        table = p.get("table", None); rec_id = p.get("record_id", "")
        return self._api("get", f"/{table}/{rec_id}") if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_get_record__mutmut_4(self, p: dict) -> dict:
        table = p.get(""); rec_id = p.get("record_id", "")
        return self._api("get", f"/{table}/{rec_id}") if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_get_record__mutmut_5(self, p: dict) -> dict:
        table = p.get("table", ); rec_id = p.get("record_id", "")
        return self._api("get", f"/{table}/{rec_id}") if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_get_record__mutmut_6(self, p: dict) -> dict:
        table = p.get("XXtableXX", ""); rec_id = p.get("record_id", "")
        return self._api("get", f"/{table}/{rec_id}") if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_get_record__mutmut_7(self, p: dict) -> dict:
        table = p.get("TABLE", ""); rec_id = p.get("record_id", "")
        return self._api("get", f"/{table}/{rec_id}") if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_get_record__mutmut_8(self, p: dict) -> dict:
        table = p.get("table", "XXXX"); rec_id = p.get("record_id", "")
        return self._api("get", f"/{table}/{rec_id}") if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_get_record__mutmut_9(self, p: dict) -> dict:
        table = p.get("table", ""); rec_id = None
        return self._api("get", f"/{table}/{rec_id}") if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_get_record__mutmut_10(self, p: dict) -> dict:
        table = p.get("table", ""); rec_id = p.get(None, "")
        return self._api("get", f"/{table}/{rec_id}") if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_get_record__mutmut_11(self, p: dict) -> dict:
        table = p.get("table", ""); rec_id = p.get("record_id", None)
        return self._api("get", f"/{table}/{rec_id}") if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_get_record__mutmut_12(self, p: dict) -> dict:
        table = p.get("table", ""); rec_id = p.get("")
        return self._api("get", f"/{table}/{rec_id}") if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_get_record__mutmut_13(self, p: dict) -> dict:
        table = p.get("table", ""); rec_id = p.get("record_id", )
        return self._api("get", f"/{table}/{rec_id}") if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_get_record__mutmut_14(self, p: dict) -> dict:
        table = p.get("table", ""); rec_id = p.get("XXrecord_idXX", "")
        return self._api("get", f"/{table}/{rec_id}") if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_get_record__mutmut_15(self, p: dict) -> dict:
        table = p.get("table", ""); rec_id = p.get("RECORD_ID", "")
        return self._api("get", f"/{table}/{rec_id}") if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_get_record__mutmut_16(self, p: dict) -> dict:
        table = p.get("table", ""); rec_id = p.get("record_id", "XXXX")
        return self._api("get", f"/{table}/{rec_id}") if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_get_record__mutmut_17(self, p: dict) -> dict:
        table = p.get("table", ""); rec_id = p.get("record_id", "")
        return self._api(None, f"/{table}/{rec_id}") if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_get_record__mutmut_18(self, p: dict) -> dict:
        table = p.get("table", ""); rec_id = p.get("record_id", "")
        return self._api("get", None) if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_get_record__mutmut_19(self, p: dict) -> dict:
        table = p.get("table", ""); rec_id = p.get("record_id", "")
        return self._api(f"/{table}/{rec_id}") if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_get_record__mutmut_20(self, p: dict) -> dict:
        table = p.get("table", ""); rec_id = p.get("record_id", "")
        return self._api("get", ) if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_get_record__mutmut_21(self, p: dict) -> dict:
        table = p.get("table", ""); rec_id = p.get("record_id", "")
        return self._api("XXgetXX", f"/{table}/{rec_id}") if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_get_record__mutmut_22(self, p: dict) -> dict:
        table = p.get("table", ""); rec_id = p.get("record_id", "")
        return self._api("GET", f"/{table}/{rec_id}") if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_get_record__mutmut_23(self, p: dict) -> dict:
        table = p.get("table", ""); rec_id = p.get("record_id", "")
        return self._api("get", f"/{table}/{rec_id}") if table or rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_get_record__mutmut_24(self, p: dict) -> dict:
        table = p.get("table", ""); rec_id = p.get("record_id", "")
        return self._api("get", f"/{table}/{rec_id}") if table and rec_id else {"XXsuccessXX": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_get_record__mutmut_25(self, p: dict) -> dict:
        table = p.get("table", ""); rec_id = p.get("record_id", "")
        return self._api("get", f"/{table}/{rec_id}") if table and rec_id else {"SUCCESS": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_get_record__mutmut_26(self, p: dict) -> dict:
        table = p.get("table", ""); rec_id = p.get("record_id", "")
        return self._api("get", f"/{table}/{rec_id}") if table and rec_id else {"success": True, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_get_record__mutmut_27(self, p: dict) -> dict:
        table = p.get("table", ""); rec_id = p.get("record_id", "")
        return self._api("get", f"/{table}/{rec_id}") if table and rec_id else {"success": False, "XXerrorXX": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_get_record__mutmut_28(self, p: dict) -> dict:
        table = p.get("table", ""); rec_id = p.get("record_id", "")
        return self._api("get", f"/{table}/{rec_id}") if table and rec_id else {"success": False, "ERROR": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_get_record__mutmut_29(self, p: dict) -> dict:
        table = p.get("table", ""); rec_id = p.get("record_id", "")
        return self._api("get", f"/{table}/{rec_id}") if table and rec_id else {"success": False, "error": "XXtable y record_id requeridosXX"}
    def xǁAirtableConnectorǁ_get_record__mutmut_30(self, p: dict) -> dict:
        table = p.get("table", ""); rec_id = p.get("record_id", "")
        return self._api("get", f"/{table}/{rec_id}") if table and rec_id else {"success": False, "error": "TABLE Y RECORD_ID REQUERIDOS"}
    @_mutmut_mutated(mutants_xǁAirtableConnectorǁ_create_record__mutmut)
    def _create_record(self, p: dict) -> dict:
        table = p.pop("table", ""); return self._api("post", f"/{table}", json={"fields": p}) if table else {"success": False, "error": "table requerido"}
    def xǁAirtableConnectorǁ_create_record__mutmut_orig(self, p: dict) -> dict:
        table = p.pop("table", ""); return self._api("post", f"/{table}", json={"fields": p}) if table else {"success": False, "error": "table requerido"}
    def xǁAirtableConnectorǁ_create_record__mutmut_1(self, p: dict) -> dict:
        table = None; return self._api("post", f"/{table}", json={"fields": p}) if table else {"success": False, "error": "table requerido"}
    def xǁAirtableConnectorǁ_create_record__mutmut_2(self, p: dict) -> dict:
        table = p.pop(None, ""); return self._api("post", f"/{table}", json={"fields": p}) if table else {"success": False, "error": "table requerido"}
    def xǁAirtableConnectorǁ_create_record__mutmut_3(self, p: dict) -> dict:
        table = p.pop("table", None); return self._api("post", f"/{table}", json={"fields": p}) if table else {"success": False, "error": "table requerido"}
    def xǁAirtableConnectorǁ_create_record__mutmut_4(self, p: dict) -> dict:
        table = p.pop(""); return self._api("post", f"/{table}", json={"fields": p}) if table else {"success": False, "error": "table requerido"}
    def xǁAirtableConnectorǁ_create_record__mutmut_5(self, p: dict) -> dict:
        table = p.pop("table", ); return self._api("post", f"/{table}", json={"fields": p}) if table else {"success": False, "error": "table requerido"}
    def xǁAirtableConnectorǁ_create_record__mutmut_6(self, p: dict) -> dict:
        table = p.pop("XXtableXX", ""); return self._api("post", f"/{table}", json={"fields": p}) if table else {"success": False, "error": "table requerido"}
    def xǁAirtableConnectorǁ_create_record__mutmut_7(self, p: dict) -> dict:
        table = p.pop("TABLE", ""); return self._api("post", f"/{table}", json={"fields": p}) if table else {"success": False, "error": "table requerido"}
    def xǁAirtableConnectorǁ_create_record__mutmut_8(self, p: dict) -> dict:
        table = p.pop("table", "XXXX"); return self._api("post", f"/{table}", json={"fields": p}) if table else {"success": False, "error": "table requerido"}
    def xǁAirtableConnectorǁ_create_record__mutmut_9(self, p: dict) -> dict:
        table = p.pop("table", ""); return self._api(None, f"/{table}", json={"fields": p}) if table else {"success": False, "error": "table requerido"}
    def xǁAirtableConnectorǁ_create_record__mutmut_10(self, p: dict) -> dict:
        table = p.pop("table", ""); return self._api("post", None, json={"fields": p}) if table else {"success": False, "error": "table requerido"}
    def xǁAirtableConnectorǁ_create_record__mutmut_11(self, p: dict) -> dict:
        table = p.pop("table", ""); return self._api("post", f"/{table}", json=None) if table else {"success": False, "error": "table requerido"}
    def xǁAirtableConnectorǁ_create_record__mutmut_12(self, p: dict) -> dict:
        table = p.pop("table", ""); return self._api(f"/{table}", json={"fields": p}) if table else {"success": False, "error": "table requerido"}
    def xǁAirtableConnectorǁ_create_record__mutmut_13(self, p: dict) -> dict:
        table = p.pop("table", ""); return self._api("post", json={"fields": p}) if table else {"success": False, "error": "table requerido"}
    def xǁAirtableConnectorǁ_create_record__mutmut_14(self, p: dict) -> dict:
        table = p.pop("table", ""); return self._api("post", f"/{table}", ) if table else {"success": False, "error": "table requerido"}
    def xǁAirtableConnectorǁ_create_record__mutmut_15(self, p: dict) -> dict:
        table = p.pop("table", ""); return self._api("XXpostXX", f"/{table}", json={"fields": p}) if table else {"success": False, "error": "table requerido"}
    def xǁAirtableConnectorǁ_create_record__mutmut_16(self, p: dict) -> dict:
        table = p.pop("table", ""); return self._api("POST", f"/{table}", json={"fields": p}) if table else {"success": False, "error": "table requerido"}
    def xǁAirtableConnectorǁ_create_record__mutmut_17(self, p: dict) -> dict:
        table = p.pop("table", ""); return self._api("post", f"/{table}", json={"XXfieldsXX": p}) if table else {"success": False, "error": "table requerido"}
    def xǁAirtableConnectorǁ_create_record__mutmut_18(self, p: dict) -> dict:
        table = p.pop("table", ""); return self._api("post", f"/{table}", json={"FIELDS": p}) if table else {"success": False, "error": "table requerido"}
    def xǁAirtableConnectorǁ_create_record__mutmut_19(self, p: dict) -> dict:
        table = p.pop("table", ""); return self._api("post", f"/{table}", json={"fields": p}) if table else {"XXsuccessXX": False, "error": "table requerido"}
    def xǁAirtableConnectorǁ_create_record__mutmut_20(self, p: dict) -> dict:
        table = p.pop("table", ""); return self._api("post", f"/{table}", json={"fields": p}) if table else {"SUCCESS": False, "error": "table requerido"}
    def xǁAirtableConnectorǁ_create_record__mutmut_21(self, p: dict) -> dict:
        table = p.pop("table", ""); return self._api("post", f"/{table}", json={"fields": p}) if table else {"success": True, "error": "table requerido"}
    def xǁAirtableConnectorǁ_create_record__mutmut_22(self, p: dict) -> dict:
        table = p.pop("table", ""); return self._api("post", f"/{table}", json={"fields": p}) if table else {"success": False, "XXerrorXX": "table requerido"}
    def xǁAirtableConnectorǁ_create_record__mutmut_23(self, p: dict) -> dict:
        table = p.pop("table", ""); return self._api("post", f"/{table}", json={"fields": p}) if table else {"success": False, "ERROR": "table requerido"}
    def xǁAirtableConnectorǁ_create_record__mutmut_24(self, p: dict) -> dict:
        table = p.pop("table", ""); return self._api("post", f"/{table}", json={"fields": p}) if table else {"success": False, "error": "XXtable requeridoXX"}
    def xǁAirtableConnectorǁ_create_record__mutmut_25(self, p: dict) -> dict:
        table = p.pop("table", ""); return self._api("post", f"/{table}", json={"fields": p}) if table else {"success": False, "error": "TABLE REQUERIDO"}
    @_mutmut_mutated(mutants_xǁAirtableConnectorǁ_update_record__mutmut)
    def _update_record(self, p: dict) -> dict:
        table = p.pop("table", ""); rec_id = p.pop("record_id", "")
        return self._api("patch", f"/{table}/{rec_id}", json={"fields": p}) if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_update_record__mutmut_orig(self, p: dict) -> dict:
        table = p.pop("table", ""); rec_id = p.pop("record_id", "")
        return self._api("patch", f"/{table}/{rec_id}", json={"fields": p}) if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_update_record__mutmut_1(self, p: dict) -> dict:
        table = None; rec_id = p.pop("record_id", "")
        return self._api("patch", f"/{table}/{rec_id}", json={"fields": p}) if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_update_record__mutmut_2(self, p: dict) -> dict:
        table = p.pop(None, ""); rec_id = p.pop("record_id", "")
        return self._api("patch", f"/{table}/{rec_id}", json={"fields": p}) if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_update_record__mutmut_3(self, p: dict) -> dict:
        table = p.pop("table", None); rec_id = p.pop("record_id", "")
        return self._api("patch", f"/{table}/{rec_id}", json={"fields": p}) if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_update_record__mutmut_4(self, p: dict) -> dict:
        table = p.pop(""); rec_id = p.pop("record_id", "")
        return self._api("patch", f"/{table}/{rec_id}", json={"fields": p}) if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_update_record__mutmut_5(self, p: dict) -> dict:
        table = p.pop("table", ); rec_id = p.pop("record_id", "")
        return self._api("patch", f"/{table}/{rec_id}", json={"fields": p}) if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_update_record__mutmut_6(self, p: dict) -> dict:
        table = p.pop("XXtableXX", ""); rec_id = p.pop("record_id", "")
        return self._api("patch", f"/{table}/{rec_id}", json={"fields": p}) if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_update_record__mutmut_7(self, p: dict) -> dict:
        table = p.pop("TABLE", ""); rec_id = p.pop("record_id", "")
        return self._api("patch", f"/{table}/{rec_id}", json={"fields": p}) if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_update_record__mutmut_8(self, p: dict) -> dict:
        table = p.pop("table", "XXXX"); rec_id = p.pop("record_id", "")
        return self._api("patch", f"/{table}/{rec_id}", json={"fields": p}) if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_update_record__mutmut_9(self, p: dict) -> dict:
        table = p.pop("table", ""); rec_id = None
        return self._api("patch", f"/{table}/{rec_id}", json={"fields": p}) if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_update_record__mutmut_10(self, p: dict) -> dict:
        table = p.pop("table", ""); rec_id = p.pop(None, "")
        return self._api("patch", f"/{table}/{rec_id}", json={"fields": p}) if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_update_record__mutmut_11(self, p: dict) -> dict:
        table = p.pop("table", ""); rec_id = p.pop("record_id", None)
        return self._api("patch", f"/{table}/{rec_id}", json={"fields": p}) if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_update_record__mutmut_12(self, p: dict) -> dict:
        table = p.pop("table", ""); rec_id = p.pop("")
        return self._api("patch", f"/{table}/{rec_id}", json={"fields": p}) if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_update_record__mutmut_13(self, p: dict) -> dict:
        table = p.pop("table", ""); rec_id = p.pop("record_id", )
        return self._api("patch", f"/{table}/{rec_id}", json={"fields": p}) if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_update_record__mutmut_14(self, p: dict) -> dict:
        table = p.pop("table", ""); rec_id = p.pop("XXrecord_idXX", "")
        return self._api("patch", f"/{table}/{rec_id}", json={"fields": p}) if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_update_record__mutmut_15(self, p: dict) -> dict:
        table = p.pop("table", ""); rec_id = p.pop("RECORD_ID", "")
        return self._api("patch", f"/{table}/{rec_id}", json={"fields": p}) if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_update_record__mutmut_16(self, p: dict) -> dict:
        table = p.pop("table", ""); rec_id = p.pop("record_id", "XXXX")
        return self._api("patch", f"/{table}/{rec_id}", json={"fields": p}) if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_update_record__mutmut_17(self, p: dict) -> dict:
        table = p.pop("table", ""); rec_id = p.pop("record_id", "")
        return self._api(None, f"/{table}/{rec_id}", json={"fields": p}) if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_update_record__mutmut_18(self, p: dict) -> dict:
        table = p.pop("table", ""); rec_id = p.pop("record_id", "")
        return self._api("patch", None, json={"fields": p}) if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_update_record__mutmut_19(self, p: dict) -> dict:
        table = p.pop("table", ""); rec_id = p.pop("record_id", "")
        return self._api("patch", f"/{table}/{rec_id}", json=None) if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_update_record__mutmut_20(self, p: dict) -> dict:
        table = p.pop("table", ""); rec_id = p.pop("record_id", "")
        return self._api(f"/{table}/{rec_id}", json={"fields": p}) if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_update_record__mutmut_21(self, p: dict) -> dict:
        table = p.pop("table", ""); rec_id = p.pop("record_id", "")
        return self._api("patch", json={"fields": p}) if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_update_record__mutmut_22(self, p: dict) -> dict:
        table = p.pop("table", ""); rec_id = p.pop("record_id", "")
        return self._api("patch", f"/{table}/{rec_id}", ) if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_update_record__mutmut_23(self, p: dict) -> dict:
        table = p.pop("table", ""); rec_id = p.pop("record_id", "")
        return self._api("XXpatchXX", f"/{table}/{rec_id}", json={"fields": p}) if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_update_record__mutmut_24(self, p: dict) -> dict:
        table = p.pop("table", ""); rec_id = p.pop("record_id", "")
        return self._api("PATCH", f"/{table}/{rec_id}", json={"fields": p}) if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_update_record__mutmut_25(self, p: dict) -> dict:
        table = p.pop("table", ""); rec_id = p.pop("record_id", "")
        return self._api("patch", f"/{table}/{rec_id}", json={"XXfieldsXX": p}) if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_update_record__mutmut_26(self, p: dict) -> dict:
        table = p.pop("table", ""); rec_id = p.pop("record_id", "")
        return self._api("patch", f"/{table}/{rec_id}", json={"FIELDS": p}) if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_update_record__mutmut_27(self, p: dict) -> dict:
        table = p.pop("table", ""); rec_id = p.pop("record_id", "")
        return self._api("patch", f"/{table}/{rec_id}", json={"fields": p}) if table or rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_update_record__mutmut_28(self, p: dict) -> dict:
        table = p.pop("table", ""); rec_id = p.pop("record_id", "")
        return self._api("patch", f"/{table}/{rec_id}", json={"fields": p}) if table and rec_id else {"XXsuccessXX": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_update_record__mutmut_29(self, p: dict) -> dict:
        table = p.pop("table", ""); rec_id = p.pop("record_id", "")
        return self._api("patch", f"/{table}/{rec_id}", json={"fields": p}) if table and rec_id else {"SUCCESS": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_update_record__mutmut_30(self, p: dict) -> dict:
        table = p.pop("table", ""); rec_id = p.pop("record_id", "")
        return self._api("patch", f"/{table}/{rec_id}", json={"fields": p}) if table and rec_id else {"success": True, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_update_record__mutmut_31(self, p: dict) -> dict:
        table = p.pop("table", ""); rec_id = p.pop("record_id", "")
        return self._api("patch", f"/{table}/{rec_id}", json={"fields": p}) if table and rec_id else {"success": False, "XXerrorXX": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_update_record__mutmut_32(self, p: dict) -> dict:
        table = p.pop("table", ""); rec_id = p.pop("record_id", "")
        return self._api("patch", f"/{table}/{rec_id}", json={"fields": p}) if table and rec_id else {"success": False, "ERROR": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_update_record__mutmut_33(self, p: dict) -> dict:
        table = p.pop("table", ""); rec_id = p.pop("record_id", "")
        return self._api("patch", f"/{table}/{rec_id}", json={"fields": p}) if table and rec_id else {"success": False, "error": "XXtable y record_id requeridosXX"}
    def xǁAirtableConnectorǁ_update_record__mutmut_34(self, p: dict) -> dict:
        table = p.pop("table", ""); rec_id = p.pop("record_id", "")
        return self._api("patch", f"/{table}/{rec_id}", json={"fields": p}) if table and rec_id else {"success": False, "error": "TABLE Y RECORD_ID REQUERIDOS"}
    @_mutmut_mutated(mutants_xǁAirtableConnectorǁ_delete_record__mutmut)
    def _delete_record(self, p: dict) -> dict:
        table = p.get("table", ""); rec_id = p.get("record_id", "")
        return self._api("delete", f"/{table}/{rec_id}") if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_delete_record__mutmut_orig(self, p: dict) -> dict:
        table = p.get("table", ""); rec_id = p.get("record_id", "")
        return self._api("delete", f"/{table}/{rec_id}") if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_delete_record__mutmut_1(self, p: dict) -> dict:
        table = None; rec_id = p.get("record_id", "")
        return self._api("delete", f"/{table}/{rec_id}") if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_delete_record__mutmut_2(self, p: dict) -> dict:
        table = p.get(None, ""); rec_id = p.get("record_id", "")
        return self._api("delete", f"/{table}/{rec_id}") if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_delete_record__mutmut_3(self, p: dict) -> dict:
        table = p.get("table", None); rec_id = p.get("record_id", "")
        return self._api("delete", f"/{table}/{rec_id}") if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_delete_record__mutmut_4(self, p: dict) -> dict:
        table = p.get(""); rec_id = p.get("record_id", "")
        return self._api("delete", f"/{table}/{rec_id}") if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_delete_record__mutmut_5(self, p: dict) -> dict:
        table = p.get("table", ); rec_id = p.get("record_id", "")
        return self._api("delete", f"/{table}/{rec_id}") if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_delete_record__mutmut_6(self, p: dict) -> dict:
        table = p.get("XXtableXX", ""); rec_id = p.get("record_id", "")
        return self._api("delete", f"/{table}/{rec_id}") if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_delete_record__mutmut_7(self, p: dict) -> dict:
        table = p.get("TABLE", ""); rec_id = p.get("record_id", "")
        return self._api("delete", f"/{table}/{rec_id}") if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_delete_record__mutmut_8(self, p: dict) -> dict:
        table = p.get("table", "XXXX"); rec_id = p.get("record_id", "")
        return self._api("delete", f"/{table}/{rec_id}") if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_delete_record__mutmut_9(self, p: dict) -> dict:
        table = p.get("table", ""); rec_id = None
        return self._api("delete", f"/{table}/{rec_id}") if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_delete_record__mutmut_10(self, p: dict) -> dict:
        table = p.get("table", ""); rec_id = p.get(None, "")
        return self._api("delete", f"/{table}/{rec_id}") if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_delete_record__mutmut_11(self, p: dict) -> dict:
        table = p.get("table", ""); rec_id = p.get("record_id", None)
        return self._api("delete", f"/{table}/{rec_id}") if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_delete_record__mutmut_12(self, p: dict) -> dict:
        table = p.get("table", ""); rec_id = p.get("")
        return self._api("delete", f"/{table}/{rec_id}") if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_delete_record__mutmut_13(self, p: dict) -> dict:
        table = p.get("table", ""); rec_id = p.get("record_id", )
        return self._api("delete", f"/{table}/{rec_id}") if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_delete_record__mutmut_14(self, p: dict) -> dict:
        table = p.get("table", ""); rec_id = p.get("XXrecord_idXX", "")
        return self._api("delete", f"/{table}/{rec_id}") if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_delete_record__mutmut_15(self, p: dict) -> dict:
        table = p.get("table", ""); rec_id = p.get("RECORD_ID", "")
        return self._api("delete", f"/{table}/{rec_id}") if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_delete_record__mutmut_16(self, p: dict) -> dict:
        table = p.get("table", ""); rec_id = p.get("record_id", "XXXX")
        return self._api("delete", f"/{table}/{rec_id}") if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_delete_record__mutmut_17(self, p: dict) -> dict:
        table = p.get("table", ""); rec_id = p.get("record_id", "")
        return self._api(None, f"/{table}/{rec_id}") if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_delete_record__mutmut_18(self, p: dict) -> dict:
        table = p.get("table", ""); rec_id = p.get("record_id", "")
        return self._api("delete", None) if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_delete_record__mutmut_19(self, p: dict) -> dict:
        table = p.get("table", ""); rec_id = p.get("record_id", "")
        return self._api(f"/{table}/{rec_id}") if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_delete_record__mutmut_20(self, p: dict) -> dict:
        table = p.get("table", ""); rec_id = p.get("record_id", "")
        return self._api("delete", ) if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_delete_record__mutmut_21(self, p: dict) -> dict:
        table = p.get("table", ""); rec_id = p.get("record_id", "")
        return self._api("XXdeleteXX", f"/{table}/{rec_id}") if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_delete_record__mutmut_22(self, p: dict) -> dict:
        table = p.get("table", ""); rec_id = p.get("record_id", "")
        return self._api("DELETE", f"/{table}/{rec_id}") if table and rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_delete_record__mutmut_23(self, p: dict) -> dict:
        table = p.get("table", ""); rec_id = p.get("record_id", "")
        return self._api("delete", f"/{table}/{rec_id}") if table or rec_id else {"success": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_delete_record__mutmut_24(self, p: dict) -> dict:
        table = p.get("table", ""); rec_id = p.get("record_id", "")
        return self._api("delete", f"/{table}/{rec_id}") if table and rec_id else {"XXsuccessXX": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_delete_record__mutmut_25(self, p: dict) -> dict:
        table = p.get("table", ""); rec_id = p.get("record_id", "")
        return self._api("delete", f"/{table}/{rec_id}") if table and rec_id else {"SUCCESS": False, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_delete_record__mutmut_26(self, p: dict) -> dict:
        table = p.get("table", ""); rec_id = p.get("record_id", "")
        return self._api("delete", f"/{table}/{rec_id}") if table and rec_id else {"success": True, "error": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_delete_record__mutmut_27(self, p: dict) -> dict:
        table = p.get("table", ""); rec_id = p.get("record_id", "")
        return self._api("delete", f"/{table}/{rec_id}") if table and rec_id else {"success": False, "XXerrorXX": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_delete_record__mutmut_28(self, p: dict) -> dict:
        table = p.get("table", ""); rec_id = p.get("record_id", "")
        return self._api("delete", f"/{table}/{rec_id}") if table and rec_id else {"success": False, "ERROR": "table y record_id requeridos"}
    def xǁAirtableConnectorǁ_delete_record__mutmut_29(self, p: dict) -> dict:
        table = p.get("table", ""); rec_id = p.get("record_id", "")
        return self._api("delete", f"/{table}/{rec_id}") if table and rec_id else {"success": False, "error": "XXtable y record_id requeridosXX"}
    def xǁAirtableConnectorǁ_delete_record__mutmut_30(self, p: dict) -> dict:
        table = p.get("table", ""); rec_id = p.get("record_id", "")
        return self._api("delete", f"/{table}/{rec_id}") if table and rec_id else {"success": False, "error": "TABLE Y RECORD_ID REQUERIDOS"}

mutants_xǁAirtableConnectorǁ__init____mutmut['_mutmut_orig'] = AirtableConnector.xǁAirtableConnectorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ__init____mutmut['xǁAirtableConnectorǁ__init____mutmut_1'] = AirtableConnector.xǁAirtableConnectorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ__init____mutmut['xǁAirtableConnectorǁ__init____mutmut_2'] = AirtableConnector.xǁAirtableConnectorǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ__init____mutmut['xǁAirtableConnectorǁ__init____mutmut_3'] = AirtableConnector.xǁAirtableConnectorǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ__init____mutmut['xǁAirtableConnectorǁ__init____mutmut_4'] = AirtableConnector.xǁAirtableConnectorǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ__init____mutmut['xǁAirtableConnectorǁ__init____mutmut_5'] = AirtableConnector.xǁAirtableConnectorǁ__init____mutmut_5 # type: ignore # mutmut generated

mutants_xǁAirtableConnectorǁconnect__mutmut['_mutmut_orig'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_1'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_2'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_3'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_4'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_5'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_6'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_7'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_8'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_9'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_10'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_11'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_12'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_13'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_14'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_15'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_15 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_16'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_16 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_17'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_17 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_18'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_18 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_19'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_19 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_20'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_20 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_21'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_21 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_22'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_22 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_23'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_23 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_24'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_24 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_25'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_25 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_26'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_26 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_27'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_27 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_28'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_28 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_29'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_29 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_30'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_30 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_31'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_31 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_32'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_32 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_33'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_33 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_34'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_34 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_35'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_35 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_36'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_36 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_37'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_37 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_38'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_38 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_39'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_39 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_40'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_40 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_41'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_41 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_42'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_42 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_43'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_43 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_44'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_44 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_45'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_45 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_46'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_46 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_47'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_47 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_48'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_48 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_49'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_49 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_50'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_50 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_51'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_51 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_52'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_52 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_53'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_53 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_54'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_54 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_55'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_55 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_56'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_56 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁconnect__mutmut['xǁAirtableConnectorǁconnect__mutmut_57'] = AirtableConnector.xǁAirtableConnectorǁconnect__mutmut_57 # type: ignore # mutmut generated

mutants_xǁAirtableConnectorǁexecute__mutmut['_mutmut_orig'] = AirtableConnector.xǁAirtableConnectorǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁexecute__mutmut['xǁAirtableConnectorǁexecute__mutmut_1'] = AirtableConnector.xǁAirtableConnectorǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁexecute__mutmut['xǁAirtableConnectorǁexecute__mutmut_2'] = AirtableConnector.xǁAirtableConnectorǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁexecute__mutmut['xǁAirtableConnectorǁexecute__mutmut_3'] = AirtableConnector.xǁAirtableConnectorǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁexecute__mutmut['xǁAirtableConnectorǁexecute__mutmut_4'] = AirtableConnector.xǁAirtableConnectorǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁexecute__mutmut['xǁAirtableConnectorǁexecute__mutmut_5'] = AirtableConnector.xǁAirtableConnectorǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁexecute__mutmut['xǁAirtableConnectorǁexecute__mutmut_6'] = AirtableConnector.xǁAirtableConnectorǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁexecute__mutmut['xǁAirtableConnectorǁexecute__mutmut_7'] = AirtableConnector.xǁAirtableConnectorǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁexecute__mutmut['xǁAirtableConnectorǁexecute__mutmut_8'] = AirtableConnector.xǁAirtableConnectorǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁexecute__mutmut['xǁAirtableConnectorǁexecute__mutmut_9'] = AirtableConnector.xǁAirtableConnectorǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁexecute__mutmut['xǁAirtableConnectorǁexecute__mutmut_10'] = AirtableConnector.xǁAirtableConnectorǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁexecute__mutmut['xǁAirtableConnectorǁexecute__mutmut_11'] = AirtableConnector.xǁAirtableConnectorǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁexecute__mutmut['xǁAirtableConnectorǁexecute__mutmut_12'] = AirtableConnector.xǁAirtableConnectorǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁexecute__mutmut['xǁAirtableConnectorǁexecute__mutmut_13'] = AirtableConnector.xǁAirtableConnectorǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁexecute__mutmut['xǁAirtableConnectorǁexecute__mutmut_14'] = AirtableConnector.xǁAirtableConnectorǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁexecute__mutmut['xǁAirtableConnectorǁexecute__mutmut_15'] = AirtableConnector.xǁAirtableConnectorǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁexecute__mutmut['xǁAirtableConnectorǁexecute__mutmut_16'] = AirtableConnector.xǁAirtableConnectorǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁexecute__mutmut['xǁAirtableConnectorǁexecute__mutmut_17'] = AirtableConnector.xǁAirtableConnectorǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁexecute__mutmut['xǁAirtableConnectorǁexecute__mutmut_18'] = AirtableConnector.xǁAirtableConnectorǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁexecute__mutmut['xǁAirtableConnectorǁexecute__mutmut_19'] = AirtableConnector.xǁAirtableConnectorǁexecute__mutmut_19 # type: ignore # mutmut generated

mutants_xǁAirtableConnectorǁvalidate__mutmut['_mutmut_orig'] = AirtableConnector.xǁAirtableConnectorǁvalidate__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁvalidate__mutmut['xǁAirtableConnectorǁvalidate__mutmut_1'] = AirtableConnector.xǁAirtableConnectorǁvalidate__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁvalidate__mutmut['xǁAirtableConnectorǁvalidate__mutmut_2'] = AirtableConnector.xǁAirtableConnectorǁvalidate__mutmut_2 # type: ignore # mutmut generated

mutants_xǁAirtableConnectorǁdisconnect__mutmut['_mutmut_orig'] = AirtableConnector.xǁAirtableConnectorǁdisconnect__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁdisconnect__mutmut['xǁAirtableConnectorǁdisconnect__mutmut_1'] = AirtableConnector.xǁAirtableConnectorǁdisconnect__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁdisconnect__mutmut['xǁAirtableConnectorǁdisconnect__mutmut_2'] = AirtableConnector.xǁAirtableConnectorǁdisconnect__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁdisconnect__mutmut['xǁAirtableConnectorǁdisconnect__mutmut_3'] = AirtableConnector.xǁAirtableConnectorǁdisconnect__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁdisconnect__mutmut['xǁAirtableConnectorǁdisconnect__mutmut_4'] = AirtableConnector.xǁAirtableConnectorǁdisconnect__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁdisconnect__mutmut['xǁAirtableConnectorǁdisconnect__mutmut_5'] = AirtableConnector.xǁAirtableConnectorǁdisconnect__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁdisconnect__mutmut['xǁAirtableConnectorǁdisconnect__mutmut_6'] = AirtableConnector.xǁAirtableConnectorǁdisconnect__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁdisconnect__mutmut['xǁAirtableConnectorǁdisconnect__mutmut_7'] = AirtableConnector.xǁAirtableConnectorǁdisconnect__mutmut_7 # type: ignore # mutmut generated

mutants_xǁAirtableConnectorǁ_api__mutmut['_mutmut_orig'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_1'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_2'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_3'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_4'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_5'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_6'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_7'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_8'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_9'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_10'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_11'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_12'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_13'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_14'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_15'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_15 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_16'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_16 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_17'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_17 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_18'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_18 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_19'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_19 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_20'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_20 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_21'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_21 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_22'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_22 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_23'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_23 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_24'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_24 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_25'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_25 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_26'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_26 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_27'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_27 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_28'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_28 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_29'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_29 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_30'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_30 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_31'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_31 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_32'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_32 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_33'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_33 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_34'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_34 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_35'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_35 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_36'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_36 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_37'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_37 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_38'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_38 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_39'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_39 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_40'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_40 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_41'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_41 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_42'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_42 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_43'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_43 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_44'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_44 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_45'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_45 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_46'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_46 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_47'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_47 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_48'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_48 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_49'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_49 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_50'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_50 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_51'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_51 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_52'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_52 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_53'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_53 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_54'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_54 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_55'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_55 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_56'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_56 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_57'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_57 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_58'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_58 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_59'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_59 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_60'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_60 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_61'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_61 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_62'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_62 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_63'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_63 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_64'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_64 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_65'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_65 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_api__mutmut['xǁAirtableConnectorǁ_api__mutmut_66'] = AirtableConnector.xǁAirtableConnectorǁ_api__mutmut_66 # type: ignore # mutmut generated

mutants_xǁAirtableConnectorǁ_list_records__mutmut['_mutmut_orig'] = AirtableConnector.xǁAirtableConnectorǁ_list_records__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_list_records__mutmut['xǁAirtableConnectorǁ_list_records__mutmut_1'] = AirtableConnector.xǁAirtableConnectorǁ_list_records__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_list_records__mutmut['xǁAirtableConnectorǁ_list_records__mutmut_2'] = AirtableConnector.xǁAirtableConnectorǁ_list_records__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_list_records__mutmut['xǁAirtableConnectorǁ_list_records__mutmut_3'] = AirtableConnector.xǁAirtableConnectorǁ_list_records__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_list_records__mutmut['xǁAirtableConnectorǁ_list_records__mutmut_4'] = AirtableConnector.xǁAirtableConnectorǁ_list_records__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_list_records__mutmut['xǁAirtableConnectorǁ_list_records__mutmut_5'] = AirtableConnector.xǁAirtableConnectorǁ_list_records__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_list_records__mutmut['xǁAirtableConnectorǁ_list_records__mutmut_6'] = AirtableConnector.xǁAirtableConnectorǁ_list_records__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_list_records__mutmut['xǁAirtableConnectorǁ_list_records__mutmut_7'] = AirtableConnector.xǁAirtableConnectorǁ_list_records__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_list_records__mutmut['xǁAirtableConnectorǁ_list_records__mutmut_8'] = AirtableConnector.xǁAirtableConnectorǁ_list_records__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_list_records__mutmut['xǁAirtableConnectorǁ_list_records__mutmut_9'] = AirtableConnector.xǁAirtableConnectorǁ_list_records__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_list_records__mutmut['xǁAirtableConnectorǁ_list_records__mutmut_10'] = AirtableConnector.xǁAirtableConnectorǁ_list_records__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_list_records__mutmut['xǁAirtableConnectorǁ_list_records__mutmut_11'] = AirtableConnector.xǁAirtableConnectorǁ_list_records__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_list_records__mutmut['xǁAirtableConnectorǁ_list_records__mutmut_12'] = AirtableConnector.xǁAirtableConnectorǁ_list_records__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_list_records__mutmut['xǁAirtableConnectorǁ_list_records__mutmut_13'] = AirtableConnector.xǁAirtableConnectorǁ_list_records__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_list_records__mutmut['xǁAirtableConnectorǁ_list_records__mutmut_14'] = AirtableConnector.xǁAirtableConnectorǁ_list_records__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_list_records__mutmut['xǁAirtableConnectorǁ_list_records__mutmut_15'] = AirtableConnector.xǁAirtableConnectorǁ_list_records__mutmut_15 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_list_records__mutmut['xǁAirtableConnectorǁ_list_records__mutmut_16'] = AirtableConnector.xǁAirtableConnectorǁ_list_records__mutmut_16 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_list_records__mutmut['xǁAirtableConnectorǁ_list_records__mutmut_17'] = AirtableConnector.xǁAirtableConnectorǁ_list_records__mutmut_17 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_list_records__mutmut['xǁAirtableConnectorǁ_list_records__mutmut_18'] = AirtableConnector.xǁAirtableConnectorǁ_list_records__mutmut_18 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_list_records__mutmut['xǁAirtableConnectorǁ_list_records__mutmut_19'] = AirtableConnector.xǁAirtableConnectorǁ_list_records__mutmut_19 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_list_records__mutmut['xǁAirtableConnectorǁ_list_records__mutmut_20'] = AirtableConnector.xǁAirtableConnectorǁ_list_records__mutmut_20 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_list_records__mutmut['xǁAirtableConnectorǁ_list_records__mutmut_21'] = AirtableConnector.xǁAirtableConnectorǁ_list_records__mutmut_21 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_list_records__mutmut['xǁAirtableConnectorǁ_list_records__mutmut_22'] = AirtableConnector.xǁAirtableConnectorǁ_list_records__mutmut_22 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_list_records__mutmut['xǁAirtableConnectorǁ_list_records__mutmut_23'] = AirtableConnector.xǁAirtableConnectorǁ_list_records__mutmut_23 # type: ignore # mutmut generated

mutants_xǁAirtableConnectorǁ_get_record__mutmut['_mutmut_orig'] = AirtableConnector.xǁAirtableConnectorǁ_get_record__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_get_record__mutmut['xǁAirtableConnectorǁ_get_record__mutmut_1'] = AirtableConnector.xǁAirtableConnectorǁ_get_record__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_get_record__mutmut['xǁAirtableConnectorǁ_get_record__mutmut_2'] = AirtableConnector.xǁAirtableConnectorǁ_get_record__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_get_record__mutmut['xǁAirtableConnectorǁ_get_record__mutmut_3'] = AirtableConnector.xǁAirtableConnectorǁ_get_record__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_get_record__mutmut['xǁAirtableConnectorǁ_get_record__mutmut_4'] = AirtableConnector.xǁAirtableConnectorǁ_get_record__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_get_record__mutmut['xǁAirtableConnectorǁ_get_record__mutmut_5'] = AirtableConnector.xǁAirtableConnectorǁ_get_record__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_get_record__mutmut['xǁAirtableConnectorǁ_get_record__mutmut_6'] = AirtableConnector.xǁAirtableConnectorǁ_get_record__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_get_record__mutmut['xǁAirtableConnectorǁ_get_record__mutmut_7'] = AirtableConnector.xǁAirtableConnectorǁ_get_record__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_get_record__mutmut['xǁAirtableConnectorǁ_get_record__mutmut_8'] = AirtableConnector.xǁAirtableConnectorǁ_get_record__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_get_record__mutmut['xǁAirtableConnectorǁ_get_record__mutmut_9'] = AirtableConnector.xǁAirtableConnectorǁ_get_record__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_get_record__mutmut['xǁAirtableConnectorǁ_get_record__mutmut_10'] = AirtableConnector.xǁAirtableConnectorǁ_get_record__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_get_record__mutmut['xǁAirtableConnectorǁ_get_record__mutmut_11'] = AirtableConnector.xǁAirtableConnectorǁ_get_record__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_get_record__mutmut['xǁAirtableConnectorǁ_get_record__mutmut_12'] = AirtableConnector.xǁAirtableConnectorǁ_get_record__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_get_record__mutmut['xǁAirtableConnectorǁ_get_record__mutmut_13'] = AirtableConnector.xǁAirtableConnectorǁ_get_record__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_get_record__mutmut['xǁAirtableConnectorǁ_get_record__mutmut_14'] = AirtableConnector.xǁAirtableConnectorǁ_get_record__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_get_record__mutmut['xǁAirtableConnectorǁ_get_record__mutmut_15'] = AirtableConnector.xǁAirtableConnectorǁ_get_record__mutmut_15 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_get_record__mutmut['xǁAirtableConnectorǁ_get_record__mutmut_16'] = AirtableConnector.xǁAirtableConnectorǁ_get_record__mutmut_16 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_get_record__mutmut['xǁAirtableConnectorǁ_get_record__mutmut_17'] = AirtableConnector.xǁAirtableConnectorǁ_get_record__mutmut_17 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_get_record__mutmut['xǁAirtableConnectorǁ_get_record__mutmut_18'] = AirtableConnector.xǁAirtableConnectorǁ_get_record__mutmut_18 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_get_record__mutmut['xǁAirtableConnectorǁ_get_record__mutmut_19'] = AirtableConnector.xǁAirtableConnectorǁ_get_record__mutmut_19 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_get_record__mutmut['xǁAirtableConnectorǁ_get_record__mutmut_20'] = AirtableConnector.xǁAirtableConnectorǁ_get_record__mutmut_20 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_get_record__mutmut['xǁAirtableConnectorǁ_get_record__mutmut_21'] = AirtableConnector.xǁAirtableConnectorǁ_get_record__mutmut_21 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_get_record__mutmut['xǁAirtableConnectorǁ_get_record__mutmut_22'] = AirtableConnector.xǁAirtableConnectorǁ_get_record__mutmut_22 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_get_record__mutmut['xǁAirtableConnectorǁ_get_record__mutmut_23'] = AirtableConnector.xǁAirtableConnectorǁ_get_record__mutmut_23 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_get_record__mutmut['xǁAirtableConnectorǁ_get_record__mutmut_24'] = AirtableConnector.xǁAirtableConnectorǁ_get_record__mutmut_24 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_get_record__mutmut['xǁAirtableConnectorǁ_get_record__mutmut_25'] = AirtableConnector.xǁAirtableConnectorǁ_get_record__mutmut_25 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_get_record__mutmut['xǁAirtableConnectorǁ_get_record__mutmut_26'] = AirtableConnector.xǁAirtableConnectorǁ_get_record__mutmut_26 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_get_record__mutmut['xǁAirtableConnectorǁ_get_record__mutmut_27'] = AirtableConnector.xǁAirtableConnectorǁ_get_record__mutmut_27 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_get_record__mutmut['xǁAirtableConnectorǁ_get_record__mutmut_28'] = AirtableConnector.xǁAirtableConnectorǁ_get_record__mutmut_28 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_get_record__mutmut['xǁAirtableConnectorǁ_get_record__mutmut_29'] = AirtableConnector.xǁAirtableConnectorǁ_get_record__mutmut_29 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_get_record__mutmut['xǁAirtableConnectorǁ_get_record__mutmut_30'] = AirtableConnector.xǁAirtableConnectorǁ_get_record__mutmut_30 # type: ignore # mutmut generated

mutants_xǁAirtableConnectorǁ_create_record__mutmut['_mutmut_orig'] = AirtableConnector.xǁAirtableConnectorǁ_create_record__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_create_record__mutmut['xǁAirtableConnectorǁ_create_record__mutmut_1'] = AirtableConnector.xǁAirtableConnectorǁ_create_record__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_create_record__mutmut['xǁAirtableConnectorǁ_create_record__mutmut_2'] = AirtableConnector.xǁAirtableConnectorǁ_create_record__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_create_record__mutmut['xǁAirtableConnectorǁ_create_record__mutmut_3'] = AirtableConnector.xǁAirtableConnectorǁ_create_record__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_create_record__mutmut['xǁAirtableConnectorǁ_create_record__mutmut_4'] = AirtableConnector.xǁAirtableConnectorǁ_create_record__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_create_record__mutmut['xǁAirtableConnectorǁ_create_record__mutmut_5'] = AirtableConnector.xǁAirtableConnectorǁ_create_record__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_create_record__mutmut['xǁAirtableConnectorǁ_create_record__mutmut_6'] = AirtableConnector.xǁAirtableConnectorǁ_create_record__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_create_record__mutmut['xǁAirtableConnectorǁ_create_record__mutmut_7'] = AirtableConnector.xǁAirtableConnectorǁ_create_record__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_create_record__mutmut['xǁAirtableConnectorǁ_create_record__mutmut_8'] = AirtableConnector.xǁAirtableConnectorǁ_create_record__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_create_record__mutmut['xǁAirtableConnectorǁ_create_record__mutmut_9'] = AirtableConnector.xǁAirtableConnectorǁ_create_record__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_create_record__mutmut['xǁAirtableConnectorǁ_create_record__mutmut_10'] = AirtableConnector.xǁAirtableConnectorǁ_create_record__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_create_record__mutmut['xǁAirtableConnectorǁ_create_record__mutmut_11'] = AirtableConnector.xǁAirtableConnectorǁ_create_record__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_create_record__mutmut['xǁAirtableConnectorǁ_create_record__mutmut_12'] = AirtableConnector.xǁAirtableConnectorǁ_create_record__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_create_record__mutmut['xǁAirtableConnectorǁ_create_record__mutmut_13'] = AirtableConnector.xǁAirtableConnectorǁ_create_record__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_create_record__mutmut['xǁAirtableConnectorǁ_create_record__mutmut_14'] = AirtableConnector.xǁAirtableConnectorǁ_create_record__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_create_record__mutmut['xǁAirtableConnectorǁ_create_record__mutmut_15'] = AirtableConnector.xǁAirtableConnectorǁ_create_record__mutmut_15 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_create_record__mutmut['xǁAirtableConnectorǁ_create_record__mutmut_16'] = AirtableConnector.xǁAirtableConnectorǁ_create_record__mutmut_16 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_create_record__mutmut['xǁAirtableConnectorǁ_create_record__mutmut_17'] = AirtableConnector.xǁAirtableConnectorǁ_create_record__mutmut_17 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_create_record__mutmut['xǁAirtableConnectorǁ_create_record__mutmut_18'] = AirtableConnector.xǁAirtableConnectorǁ_create_record__mutmut_18 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_create_record__mutmut['xǁAirtableConnectorǁ_create_record__mutmut_19'] = AirtableConnector.xǁAirtableConnectorǁ_create_record__mutmut_19 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_create_record__mutmut['xǁAirtableConnectorǁ_create_record__mutmut_20'] = AirtableConnector.xǁAirtableConnectorǁ_create_record__mutmut_20 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_create_record__mutmut['xǁAirtableConnectorǁ_create_record__mutmut_21'] = AirtableConnector.xǁAirtableConnectorǁ_create_record__mutmut_21 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_create_record__mutmut['xǁAirtableConnectorǁ_create_record__mutmut_22'] = AirtableConnector.xǁAirtableConnectorǁ_create_record__mutmut_22 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_create_record__mutmut['xǁAirtableConnectorǁ_create_record__mutmut_23'] = AirtableConnector.xǁAirtableConnectorǁ_create_record__mutmut_23 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_create_record__mutmut['xǁAirtableConnectorǁ_create_record__mutmut_24'] = AirtableConnector.xǁAirtableConnectorǁ_create_record__mutmut_24 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_create_record__mutmut['xǁAirtableConnectorǁ_create_record__mutmut_25'] = AirtableConnector.xǁAirtableConnectorǁ_create_record__mutmut_25 # type: ignore # mutmut generated

mutants_xǁAirtableConnectorǁ_update_record__mutmut['_mutmut_orig'] = AirtableConnector.xǁAirtableConnectorǁ_update_record__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_update_record__mutmut['xǁAirtableConnectorǁ_update_record__mutmut_1'] = AirtableConnector.xǁAirtableConnectorǁ_update_record__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_update_record__mutmut['xǁAirtableConnectorǁ_update_record__mutmut_2'] = AirtableConnector.xǁAirtableConnectorǁ_update_record__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_update_record__mutmut['xǁAirtableConnectorǁ_update_record__mutmut_3'] = AirtableConnector.xǁAirtableConnectorǁ_update_record__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_update_record__mutmut['xǁAirtableConnectorǁ_update_record__mutmut_4'] = AirtableConnector.xǁAirtableConnectorǁ_update_record__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_update_record__mutmut['xǁAirtableConnectorǁ_update_record__mutmut_5'] = AirtableConnector.xǁAirtableConnectorǁ_update_record__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_update_record__mutmut['xǁAirtableConnectorǁ_update_record__mutmut_6'] = AirtableConnector.xǁAirtableConnectorǁ_update_record__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_update_record__mutmut['xǁAirtableConnectorǁ_update_record__mutmut_7'] = AirtableConnector.xǁAirtableConnectorǁ_update_record__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_update_record__mutmut['xǁAirtableConnectorǁ_update_record__mutmut_8'] = AirtableConnector.xǁAirtableConnectorǁ_update_record__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_update_record__mutmut['xǁAirtableConnectorǁ_update_record__mutmut_9'] = AirtableConnector.xǁAirtableConnectorǁ_update_record__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_update_record__mutmut['xǁAirtableConnectorǁ_update_record__mutmut_10'] = AirtableConnector.xǁAirtableConnectorǁ_update_record__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_update_record__mutmut['xǁAirtableConnectorǁ_update_record__mutmut_11'] = AirtableConnector.xǁAirtableConnectorǁ_update_record__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_update_record__mutmut['xǁAirtableConnectorǁ_update_record__mutmut_12'] = AirtableConnector.xǁAirtableConnectorǁ_update_record__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_update_record__mutmut['xǁAirtableConnectorǁ_update_record__mutmut_13'] = AirtableConnector.xǁAirtableConnectorǁ_update_record__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_update_record__mutmut['xǁAirtableConnectorǁ_update_record__mutmut_14'] = AirtableConnector.xǁAirtableConnectorǁ_update_record__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_update_record__mutmut['xǁAirtableConnectorǁ_update_record__mutmut_15'] = AirtableConnector.xǁAirtableConnectorǁ_update_record__mutmut_15 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_update_record__mutmut['xǁAirtableConnectorǁ_update_record__mutmut_16'] = AirtableConnector.xǁAirtableConnectorǁ_update_record__mutmut_16 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_update_record__mutmut['xǁAirtableConnectorǁ_update_record__mutmut_17'] = AirtableConnector.xǁAirtableConnectorǁ_update_record__mutmut_17 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_update_record__mutmut['xǁAirtableConnectorǁ_update_record__mutmut_18'] = AirtableConnector.xǁAirtableConnectorǁ_update_record__mutmut_18 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_update_record__mutmut['xǁAirtableConnectorǁ_update_record__mutmut_19'] = AirtableConnector.xǁAirtableConnectorǁ_update_record__mutmut_19 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_update_record__mutmut['xǁAirtableConnectorǁ_update_record__mutmut_20'] = AirtableConnector.xǁAirtableConnectorǁ_update_record__mutmut_20 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_update_record__mutmut['xǁAirtableConnectorǁ_update_record__mutmut_21'] = AirtableConnector.xǁAirtableConnectorǁ_update_record__mutmut_21 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_update_record__mutmut['xǁAirtableConnectorǁ_update_record__mutmut_22'] = AirtableConnector.xǁAirtableConnectorǁ_update_record__mutmut_22 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_update_record__mutmut['xǁAirtableConnectorǁ_update_record__mutmut_23'] = AirtableConnector.xǁAirtableConnectorǁ_update_record__mutmut_23 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_update_record__mutmut['xǁAirtableConnectorǁ_update_record__mutmut_24'] = AirtableConnector.xǁAirtableConnectorǁ_update_record__mutmut_24 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_update_record__mutmut['xǁAirtableConnectorǁ_update_record__mutmut_25'] = AirtableConnector.xǁAirtableConnectorǁ_update_record__mutmut_25 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_update_record__mutmut['xǁAirtableConnectorǁ_update_record__mutmut_26'] = AirtableConnector.xǁAirtableConnectorǁ_update_record__mutmut_26 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_update_record__mutmut['xǁAirtableConnectorǁ_update_record__mutmut_27'] = AirtableConnector.xǁAirtableConnectorǁ_update_record__mutmut_27 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_update_record__mutmut['xǁAirtableConnectorǁ_update_record__mutmut_28'] = AirtableConnector.xǁAirtableConnectorǁ_update_record__mutmut_28 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_update_record__mutmut['xǁAirtableConnectorǁ_update_record__mutmut_29'] = AirtableConnector.xǁAirtableConnectorǁ_update_record__mutmut_29 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_update_record__mutmut['xǁAirtableConnectorǁ_update_record__mutmut_30'] = AirtableConnector.xǁAirtableConnectorǁ_update_record__mutmut_30 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_update_record__mutmut['xǁAirtableConnectorǁ_update_record__mutmut_31'] = AirtableConnector.xǁAirtableConnectorǁ_update_record__mutmut_31 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_update_record__mutmut['xǁAirtableConnectorǁ_update_record__mutmut_32'] = AirtableConnector.xǁAirtableConnectorǁ_update_record__mutmut_32 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_update_record__mutmut['xǁAirtableConnectorǁ_update_record__mutmut_33'] = AirtableConnector.xǁAirtableConnectorǁ_update_record__mutmut_33 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_update_record__mutmut['xǁAirtableConnectorǁ_update_record__mutmut_34'] = AirtableConnector.xǁAirtableConnectorǁ_update_record__mutmut_34 # type: ignore # mutmut generated

mutants_xǁAirtableConnectorǁ_delete_record__mutmut['_mutmut_orig'] = AirtableConnector.xǁAirtableConnectorǁ_delete_record__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_delete_record__mutmut['xǁAirtableConnectorǁ_delete_record__mutmut_1'] = AirtableConnector.xǁAirtableConnectorǁ_delete_record__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_delete_record__mutmut['xǁAirtableConnectorǁ_delete_record__mutmut_2'] = AirtableConnector.xǁAirtableConnectorǁ_delete_record__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_delete_record__mutmut['xǁAirtableConnectorǁ_delete_record__mutmut_3'] = AirtableConnector.xǁAirtableConnectorǁ_delete_record__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_delete_record__mutmut['xǁAirtableConnectorǁ_delete_record__mutmut_4'] = AirtableConnector.xǁAirtableConnectorǁ_delete_record__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_delete_record__mutmut['xǁAirtableConnectorǁ_delete_record__mutmut_5'] = AirtableConnector.xǁAirtableConnectorǁ_delete_record__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_delete_record__mutmut['xǁAirtableConnectorǁ_delete_record__mutmut_6'] = AirtableConnector.xǁAirtableConnectorǁ_delete_record__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_delete_record__mutmut['xǁAirtableConnectorǁ_delete_record__mutmut_7'] = AirtableConnector.xǁAirtableConnectorǁ_delete_record__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_delete_record__mutmut['xǁAirtableConnectorǁ_delete_record__mutmut_8'] = AirtableConnector.xǁAirtableConnectorǁ_delete_record__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_delete_record__mutmut['xǁAirtableConnectorǁ_delete_record__mutmut_9'] = AirtableConnector.xǁAirtableConnectorǁ_delete_record__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_delete_record__mutmut['xǁAirtableConnectorǁ_delete_record__mutmut_10'] = AirtableConnector.xǁAirtableConnectorǁ_delete_record__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_delete_record__mutmut['xǁAirtableConnectorǁ_delete_record__mutmut_11'] = AirtableConnector.xǁAirtableConnectorǁ_delete_record__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_delete_record__mutmut['xǁAirtableConnectorǁ_delete_record__mutmut_12'] = AirtableConnector.xǁAirtableConnectorǁ_delete_record__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_delete_record__mutmut['xǁAirtableConnectorǁ_delete_record__mutmut_13'] = AirtableConnector.xǁAirtableConnectorǁ_delete_record__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_delete_record__mutmut['xǁAirtableConnectorǁ_delete_record__mutmut_14'] = AirtableConnector.xǁAirtableConnectorǁ_delete_record__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_delete_record__mutmut['xǁAirtableConnectorǁ_delete_record__mutmut_15'] = AirtableConnector.xǁAirtableConnectorǁ_delete_record__mutmut_15 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_delete_record__mutmut['xǁAirtableConnectorǁ_delete_record__mutmut_16'] = AirtableConnector.xǁAirtableConnectorǁ_delete_record__mutmut_16 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_delete_record__mutmut['xǁAirtableConnectorǁ_delete_record__mutmut_17'] = AirtableConnector.xǁAirtableConnectorǁ_delete_record__mutmut_17 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_delete_record__mutmut['xǁAirtableConnectorǁ_delete_record__mutmut_18'] = AirtableConnector.xǁAirtableConnectorǁ_delete_record__mutmut_18 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_delete_record__mutmut['xǁAirtableConnectorǁ_delete_record__mutmut_19'] = AirtableConnector.xǁAirtableConnectorǁ_delete_record__mutmut_19 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_delete_record__mutmut['xǁAirtableConnectorǁ_delete_record__mutmut_20'] = AirtableConnector.xǁAirtableConnectorǁ_delete_record__mutmut_20 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_delete_record__mutmut['xǁAirtableConnectorǁ_delete_record__mutmut_21'] = AirtableConnector.xǁAirtableConnectorǁ_delete_record__mutmut_21 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_delete_record__mutmut['xǁAirtableConnectorǁ_delete_record__mutmut_22'] = AirtableConnector.xǁAirtableConnectorǁ_delete_record__mutmut_22 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_delete_record__mutmut['xǁAirtableConnectorǁ_delete_record__mutmut_23'] = AirtableConnector.xǁAirtableConnectorǁ_delete_record__mutmut_23 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_delete_record__mutmut['xǁAirtableConnectorǁ_delete_record__mutmut_24'] = AirtableConnector.xǁAirtableConnectorǁ_delete_record__mutmut_24 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_delete_record__mutmut['xǁAirtableConnectorǁ_delete_record__mutmut_25'] = AirtableConnector.xǁAirtableConnectorǁ_delete_record__mutmut_25 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_delete_record__mutmut['xǁAirtableConnectorǁ_delete_record__mutmut_26'] = AirtableConnector.xǁAirtableConnectorǁ_delete_record__mutmut_26 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_delete_record__mutmut['xǁAirtableConnectorǁ_delete_record__mutmut_27'] = AirtableConnector.xǁAirtableConnectorǁ_delete_record__mutmut_27 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_delete_record__mutmut['xǁAirtableConnectorǁ_delete_record__mutmut_28'] = AirtableConnector.xǁAirtableConnectorǁ_delete_record__mutmut_28 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_delete_record__mutmut['xǁAirtableConnectorǁ_delete_record__mutmut_29'] = AirtableConnector.xǁAirtableConnectorǁ_delete_record__mutmut_29 # type: ignore # mutmut generated
mutants_xǁAirtableConnectorǁ_delete_record__mutmut['xǁAirtableConnectorǁ_delete_record__mutmut_30'] = AirtableConnector.xǁAirtableConnectorǁ_delete_record__mutmut_30 # type: ignore # mutmut generated


AIRTABLE_SCHEMA = ConnectorSchema(name="airtable", version="1.0.0", description="Lee y escribe registros en Airtable",
    category="database", icon="grid", author="Zenic-Flijo", actions=[
    ActionDefinition(name="list_records", description="Lista registros de una tabla", category="read"),
    ActionDefinition(name="get_record", description="Obtiene un registro por ID", category="read"),
    ActionDefinition(name="create_record", description="Crea un nuevo registro", category="write"),
    ActionDefinition(name="update_record", description="Actualiza un registro existente", category="write"),
    ActionDefinition(name="delete_record", description="Elimina un registro", category="write"),
], auth_requirements=[AuthRequirement(auth_type="bearer_token", required_fields=["api_key", "base_id"])])
