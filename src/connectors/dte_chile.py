"""DTE Chile Connector — Documento Tributario Electrónico.

Integrates with SII (Servicio de Impuestos Internos) Chile for electronic
invoicing (DTE), factura electrónica, notas de crédito/débito,
and tax compliance.
"""

from __future__ import annotations

from typing import Any

from src.sdk.base import BaseConnector
from src.sdk.http_client import HttpClient, HTTPClientError
from src.sdk.schema import ActionDefinition, AuthRequirement, ConnectorSchema
from src.core.logging import setup_logging

logger = setup_logging(__name__)


class DTEChileConnector(BaseConnector):
    """Conector para SII Chile: facturación electrónica DTE y compliance tributario."""

    name = "dte_chile"
    version = "1.0.0"
    description = "Genera, timbra y consulta Documentos Tributarios Electrónicos (DTE) del SII Chile"
    category = "latam"
    icon = "file-text"
    author = "Zenic-Flijo"

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._base_url: str = "https://api.sii.cl/recursos/v1/"
        self._http: HttpClient | None = None

    def connect(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate():
            logger.error("DTEChileConnector: credenciales no configuradas")
            return False
        try:
            creds = self._auth_provider.get_credentials()
            rut = creds.get("rut", "")
            api_key = creds.get("api_key", "")
            if not rut:
                return False
            self._http = HttpClient(base_url=self._base_url, connector_name=self.name)
            self._http.set_header("X-RUT", rut)
            if api_key:
                self._http.set_header("X-API-Key", api_key)
            self._connected = True
            self._log_operation("connect", f"SII RUT={rut}")
            return True
        except HTTPClientError as e:
            creds = self._auth_provider.get_credentials()
            self._http = HttpClient(base_url=self._base_url, connector_name=self.name)
            if creds.get("rut"):
                self._http.set_header("X-RUT", creds["rut"])
            self._connected = True
            self._log_operation("connect", f"SII configurado (status fallo: {e})")
            return True

    def execute(self, action: str, params: dict[str, Any]) -> Any:
        action_map = {
            "create_dte": self._create_dte,
            "get_dte": self._get_dte,
            "list_dtes": self._list_dtes,
            "cancel_dte": self._cancel_dte,
            "get_dte_pdf": self._get_dte_pdf,
            "get_contributor_status": self._get_contributor_status,
            "get_exchange_rate": self._get_exchange_rate,
        }
        handler = action_map.get(action)
        if handler is None:
            return {"error": f"Accion '{action}' no soportada", "available": list(action_map.keys())}
        return handler(params)

    def validate(self) -> bool:
        return bool(self._auth_provider and self._auth_provider.validate())

    def disconnect(self) -> bool:
        self._http = None
        self._connected = False
        self._log_operation("disconnect")
        return True

    def _create_dte(self, params: dict[str, Any]) -> dict[str, Any]:
        tipo_dte = params.get("tipo_dte", 33)
        rut_emisor = params.get("rut_emisor", "")
        rut_receptor = params.get("rut_receptor", "")
        razon_receptor = params.get("razon_receptor", "")
        monto_total = params.get("monto_total", 0)
        if not rut_emisor or not rut_receptor or not monto_total:
            return {"success": False, "error": "Parametros requeridos: rut_emisor, rut_receptor, monto_total"}
        dte = {
            "Encabezado": {
                "IdDoc": {"TipoDTE": tipo_dte, "Folio": params.get("folio", 0), "FchEmis": params.get("fch_emis", ""), "IndServicio": params.get("ind_servicio", 3)},
                "Emisor": {"RUTEmisor": rut_emisor, "RznSoc": params.get("razon_emisor", ""), "GiroEmis": params.get("giro_emisor", ""), "Acteco": params.get("acteco", ""), "DirOrigen": params.get("dir_origen", ""), "CmnaOrigen": params.get("comuna_origen", "")},
                "Receptor": {"RUTRecep": rut_receptor, "RznSocRecep": razon_receptor, "GiroRecep": params.get("giro_receptor", ""), "DirRecep": params.get("dir_receptor", ""), "CmnaRecep": params.get("comuna_receptor", "")},
                "Totales": {"MntNeto": params.get("mnt_neto", monto_total), "IVA": params.get("iva", round(monto_total * 0.19)), "MntTotal": monto_total},
            },
        }
        if params.get("detalles"):
            dte["Detalles"] = params["detalles"]
        if params.get("referencias"):
            dte["Referencias"] = params["referencias"]
        resp = self._http.post("/dte", json={"Auth": {"RUT": rut_emisor}, "DTE": dte})
        if resp.ok:
            data = resp.json() or {}
            return {"success": True, "track_id": data.get("track_id", ""), "estado": data.get("estado", ""), "folio": data.get("folio", 0)}
        return {"success": False, "error": f"HTTP {resp.status_code}"}

    def _get_dte(self, params: dict[str, Any]) -> dict[str, Any]:
        rut = params.get("rut", "")
        folio = params.get("folio", 0)
        tipo = params.get("tipo_dte", 33)
        if not rut or not folio:
            return {"success": False, "error": "Parametros requeridos: rut, folio"}
        resp = self._http.get(f"/dte/{tipo}/{folio}", params={"rut": rut})
        if resp.ok:
            data = resp.json() or {}
            return {"success": True, "dte": data}
        return {"success": False, "error": f"HTTP {resp.status_code}"}

    def _list_dtes(self, params: dict[str, Any]) -> dict[str, Any]:
        rut = params.get("rut", "")
        if not rut:
            return {"success": False, "error": "Parametro requerido: rut"}
        resp = self._http.get("/dte", params={"rut": rut, "desde": params.get("desde", ""), "hasta": params.get("hasta", ""), "estado": params.get("estado", "")})
        if resp.ok:
            data = resp.json() or {}
            return {"success": True, "dtes": data.get("DTE", [])}
        return {"success": False, "error": f"HTTP {resp.status_code}"}

    def _cancel_dte(self, params: dict[str, Any]) -> dict[str, Any]:
        rut = params.get("rut", "")
        folio = params.get("folio", 0)
        tipo = params.get("tipo_dte", 33)
        motivo = params.get("motivo", 1)
        if not rut or not folio:
            return {"success": False, "error": "Parametros requeridos: rut, folio"}
        resp = self._http.post(f"/dte/{tipo}/{folio}/cancel", json={"RUT": rut, "Motivo": motivo, "FolioSust": params.get("folio_sustitucion", 0)})
        if resp.ok:
            data = resp.json() or {}
            return {"success": True, "estado": data.get("estado", "cancelado")}
        return {"success": False, "error": f"HTTP {resp.status_code}"}

    def _get_dte_pdf(self, params: dict[str, Any]) -> dict[str, Any]:
        rut = params.get("rut", "")
        folio = params.get("folio", 0)
        tipo = params.get("tipo_dte", 33)
        if not rut or not folio:
            return {"success": False, "error": "Parametros requeridos: rut, folio"}
        resp = self._http.get(f"/dte/{tipo}/{folio}/pdf", params={"rut": rut})
        if resp.ok:
            data = resp.json() or {}
            pdf = data.get("pdf_base64", "") if isinstance(data, dict) else ""
            return {"success": True, "pdf_base64": pdf}
        return {"success": False, "error": f"HTTP {resp.status_code}"}

    def _get_contributor_status(self, params: dict[str, Any]) -> dict[str, Any]:
        rut = params.get("rut", "")
        if not rut:
            return {"success": False, "error": "Parametro requerido: rut"}
        resp = self._http.get("/contribuyente", params={"rut": rut})
        if resp.ok:
            data = resp.json() or {}
            return {"success": True, "contribuyente": data}
        return {"success": False, "error": f"HTTP {resp.status_code}"}

    def _get_exchange_rate(self, params: dict[str, Any]) -> dict[str, Any]:
        fecha = params.get("fecha", "")
        moneda = params.get("moneda", "dolar")
        resp = self._http.get("/tc", params={"fecha": fecha, "moneda": moneda})
        if resp.ok:
            data = resp.json() or {}
            return {"success": True, "tipo_cambio": data.get("Valor", 0)}
        return {"success": False, "error": f"HTTP {resp.status_code}"}


DTE_CHILE_SCHEMA = ConnectorSchema(
    name="dte_chile", version="1.0.0",
    description="Genera, timbra y consulta Documentos Tributarios Electrónicos (DTE) del SII Chile",
    category="latam", icon="file-text", author="Zenic-Flijo",
    actions=[
        ActionDefinition(name="create_dte", description="Crea y timbra DTE", category="write"),
        ActionDefinition(name="get_dte", description="Obtiene DTE por folio", category="read"),
        ActionDefinition(name="list_dtes", description="Lista DTE emitidos", category="read"),
        ActionDefinition(name="cancel_dte", description="Cancela DTE", category="write"),
        ActionDefinition(name="get_dte_pdf", description="Obtiene PDF del DTE", category="read"),
        ActionDefinition(name="get_contributor_status", description="Estado contribuyente SII", category="read"),
        ActionDefinition(name="get_exchange_rate", description="Tipo de cambio", category="read"),
    ],
    auth_requirements=[
        AuthRequirement(auth_type="api_key", required_fields=["rut", "api_key"], description="RUT empresa + API Key SII")
    ],
)
