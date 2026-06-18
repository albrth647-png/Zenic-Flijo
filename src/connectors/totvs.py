"""Conector Totvs — ERP brasileiro Protheus API REST."""

from __future__ import annotations

import base64
from typing import Any

from src.sdk.base import BaseConnector
from src.sdk.http_client import HttpClient, HTTPClientError
from src.sdk.schema import ActionDefinition, AuthRequirement, ConnectorSchema
from src.utils.logger import setup_logging

logger = setup_logging(__name__)


class TotvsConnector(BaseConnector):
    name = "totvs"
    version = "1.0.0"
    description = "Integra con Totvs Protheus via REST API para datos maestros, fiscais e financeiros"
    category = "erp"
    icon = "database"
    author = "Zenic-Flijo"

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._base_url: str = ""; self._username: str = ""; self._password: str = ""
        self._company: str = ""; self._branch: str = ""
        self._http: HttpClient | None = None

    def connect(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate(): return False
        if hasattr(self._auth_provider, "_credentials"):
            c = self._auth_provider._credentials; self._base_url = c.get("base_url", "").rstrip("/")
            self._username = c.get("username", ""); self._password = c.get("password", "")
            self._company = c.get("company", "01"); self._branch = c.get("branch", "01")
        if not self._base_url or not self._username or not self._password:
            logger.error("Totvs: base_url, username y password requeridos"); return False
        auth = base64.b64encode(f"{self._username}:{self._password}".encode()).decode()
        self._http = HttpClient(base_url=f"{self._base_url}/api/v1", connector_name=self.name)
        self._http.set_header("Authorization", f"Basic {auth}")
        self._http.set_header("company", self._company)
        self._http.set_header("branch", self._branch)
        self._connected = True; self._log_operation("connect", f"totvs={self._base_url}"); return True

    def execute(self, action: str, params: dict[str, Any]) -> Any:
        action_map = {"get_products": self._get_products, "get_customers": self._get_customers, "get_suppliers": self._get_suppliers,
                       "get_invoices": self._get_invoices, "get_sales_orders": self._get_sales_orders, "get_financial": self._get_financial}
        handler = action_map.get(action)
        return handler(params) if handler else {"error": f"Accion '{action}' no soportada", "available": list(action_map.keys())}

    def validate(self) -> bool: return bool(self._auth_provider and self._auth_provider.validate())
    def disconnect(self) -> bool: self._connected = False; self._http = None; self._log_operation("disconnect"); return True

    def _api(self, method: str, path: str, **kw: Any) -> dict:
        if not self._http: return {"success": False, "error": "Not connected"}
        try:
            resp = getattr(self._http, method)(path, **kw)
            d = resp.json() if hasattr(resp, "json") and callable(resp.json) else {}
            if resp.ok: return {"success": True, "data": d.get("items", d)}
            return {"success": False, "error": d.get("error", {}).get("message", f"HTTP {resp.status_code}")}
        except HTTPClientError as e: return {"success": False, "error": str(e)}
        except Exception as e: return {"success": False, "error": str(e)}

    def _get_products(self, p: dict) -> dict: return self._api("get", "/products", params=p)
    def _get_customers(self, p: dict) -> dict: return self._api("get", "/customers", params=p)
    def _get_suppliers(self, p: dict) -> dict: return self._api("get", "/suppliers", params=p)
    def _get_invoices(self, p: dict) -> dict: return self._api("get", "/invoices", params=p)
    def _get_sales_orders(self, p: dict) -> dict: return self._api("get", "/sales-orders", params=p)
    def _get_financial(self, p: dict) -> dict: return self._api("get", "/financial", params=p)


TOTVS_SCHEMA = ConnectorSchema(name="totvs", version="1.0.0", description="Integra con Totvs Protheus para ERP brasileiro",
    category="erp", icon="database", author="Zenic-Flijo", actions=[
    ActionDefinition(name="get_products", description="Lista productos del ERP", category="read"),
    ActionDefinition(name="get_customers", description="Lista clientes del ERP", category="read"),
    ActionDefinition(name="get_suppliers", description="Lista proveedores del ERP", category="read"),
    ActionDefinition(name="get_invoices", description="Lista facturas del ERP", category="read"),
    ActionDefinition(name="get_sales_orders", description="Lista pedidos de venta", category="read"),
    ActionDefinition(name="get_financial", description="Lista movimientos financieros", category="read"),
], auth_requirements=[AuthRequirement(auth_type="basic", required_fields=["base_url", "username", "password"])])
