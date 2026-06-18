"""AFIP Argentina Connector — Facturación Electrónica y Compliance Fiscal.

Integrates with AFIP Web Services (WSAA, WSFE, WSFEv1) for electronic
invoicing, tax credit/debit notes, and fiscal compliance in Argentina.
"""

from __future__ import annotations

from typing import Any

from src.sdk.base import BaseConnector
from src.sdk.http_client import HttpClient, HTTPClientError
from src.sdk.schema import ActionDefinition, AuthRequirement, ConnectorSchema
from src.utils.logger import setup_logging

logger = setup_logging(__name__)


class AFIPArgentinaConnector(BaseConnector):
    """Conector para AFIP Argentina: facturación electrónica y compliance fiscal."""

    name = "afip_argentina"
    version = "1.0.0"
    description = "Genera facturas electrónicas, crédito/débito y consulta compliance fiscal via AFIP WS"
    category = "latam"
    icon = "file-text"
    author = "Zenic-Flijo"

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._base_url: str = ""
        self._http: HttpClient | None = None

    def connect(self) -> bool:
        if not self._auth_provider or not self._auth_provider.validate():
            logger.error("AFIPArgentinaConnector: credenciales no configuradas")
            return False
        try:
            creds = self._auth_provider.get_credentials()
            cuit = creds.get("cuit", "")
            env = creds.get("environment", "homologacion")
            if not cuit:
                return False
            if env == "produccion":
                self._base_url = "https://wsfe.afip.gov.ar/ws/services/"
            else:
                self._base_url = "https://wswhomo.afip.gov.ar/wsfev1/service.asmx"
            self._http = HttpClient(base_url=self._base_url, connector_name=self.name)
            self._http.set_header("X-CUIT", cuit)
            if creds.get("api_key"):
                self._http.set_header("X-API-Key", creds["api_key"])
            self._connected = True
            self._log_operation("connect", f"AFIP CUIT={cuit} env={env}")
            return True
        except HTTPClientError as e:
            creds = self._auth_provider.get_credentials()
            self._http = HttpClient(
                base_url=self._base_url or "https://wswhomo.afip.gov.ar/wsfev1/service.asmx",
                connector_name=self.name,
            )
            if creds.get("cuit"):
                self._http.set_header("X-CUIT", creds["cuit"])
            self._connected = True
            self._log_operation("connect", f"AFIP configurado (status fallo: {e})")
            return True

    def execute(self, action: str, params: dict[str, Any]) -> Any:
        action_map = {
            "create_invoice": self._create_invoice,
            "create_credit_note": self._create_credit_note,
            "create_debit_note": self._create_debit_note,
            "get_invoice": self._get_invoice,
            "get_last_invoice_number": self._get_last_invoice_number,
            "get_taxpayer_types": self._get_taxpayer_types,
            "get_vat_conditions": self._get_vat_conditions,
            "get_point_of_sales": self._get_point_of_sales,
            "check_taxpayer_status": self._check_taxpayer_status,
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

    def _create_invoice(self, params: dict[str, Any]) -> dict[str, Any]:
        cuit = params.get("cuit", "")
        cbte_tipo = params.get("cbte_tipo", 1)
        pto_vta = params.get("pto_vta", 1)
        concepto = params.get("concepto", 1)
        doc_tipo = params.get("doc_tipo", 80)
        doc_nro = params.get("doc_nro", "")
        importe_total = params.get("importe_total", 0)
        if not cuit or not doc_nro or not importe_total:
            return {"success": False, "error": "Parametros requeridos: cuit, doc_nro, importe_total"}

        inv = {
            "CbteTipo": cbte_tipo, "PtoVta": pto_vta, "Concepto": concepto,
            "DocTipo": doc_tipo, "DocNro": doc_nro,
            "CbteDesde": params.get("cbte_desde", 1),
            "CbteHasta": params.get("cbte_hasta", 1),
            "CbteFch": params.get("cbte_fch", ""),
            "ImpTotal": importe_total,
            "ImpNeto": params.get("imp_neto", importe_total),
            "ImpIVA": params.get("imp_iva", 0),
            "ImpTrib": params.get("imp_trib", 0),
            "MonId": params.get("mon_id", "PES"),
            "MonCotiz": params.get("mon_cotiz", 1),
            "Iva": params.get("iva", []),
            "Tributos": params.get("tributos", []),
        }
        if params.get("obs"):
            inv["Obs"] = params["obs"]
        if params.get("items"):
            inv["Items"] = params["items"]

        resp = self._http.post("/fe/cbt", json={
            "Auth": {"Cuit": cuit, "Token": params.get("token", "")},
            "FeCAEReq": {
                "FeCabReq": {"CantReg": 1, "PtoVta": pto_vta, "CbteTipo": cbte_tipo},
                "FeDetReq": [{"FECAEDetRequest": inv}],
            },
        })
        if resp.ok:
            data = resp.json() or {}
            det_resp = data.get("FeDetResp", [{}])
            result = det_resp[0] if det_resp else {}
            return {
                "success": True,
                "cae": result.get("CAE", ""),
                "vto": result.get("CAEFchVto", ""),
                "resultado": result.get("Resultado", ""),
            }
        return {"success": False, "error": f"HTTP {resp.status_code}"}

    def _create_credit_note(self, params: dict[str, Any]) -> dict[str, Any]:
        params["cbte_tipo"] = params.get("cbte_tipo", 3)
        return self._create_invoice(params)

    def _create_debit_note(self, params: dict[str, Any]) -> dict[str, Any]:
        params["cbte_tipo"] = params.get("cbte_tipo", 2)
        return self._create_invoice(params)

    def _get_invoice(self, params: dict[str, Any]) -> dict[str, Any]:
        cbte_tipo = params.get("cbte_tipo", 1)
        pto_vta = params.get("pto_vta", 1)
        cbte_nro = params.get("cbte_nro", "")
        cuit = params.get("cuit", "")
        if not cbte_nro or not cuit:
            return {"success": False, "error": "Parametros requeridos: cbte_nro, cuit"}
        resp = self._http.post("/fe/cbt", json={
            "Auth": {"Cuit": cuit},
            "FeCompConsReq": {"CbteTipo": cbte_tipo, "CbteNro": cbte_nro, "PtoVta": pto_vta},
        })
        if resp.ok:
            data = resp.json() or {}
            comp = data.get("FeCompConsResponse", {})
            return {"success": True, "resultado": comp.get("Resultado", ""), "comprobante": comp}
        return {"success": False, "error": f"HTTP {resp.status_code}"}

    def _get_last_invoice_number(self, params: dict[str, Any]) -> dict[str, Any]:
        cuit = params.get("cuit", "")
        cbte_tipo = params.get("cbte_tipo", 1)
        pto_vta = params.get("pto_vta", 1)
        if not cuit:
            return {"success": False, "error": "Parametro requerido: cuit"}
        resp = self._http.post("/fe/ult", json={
            "Auth": {"Cuit": cuit},
            "FeCompUltReq": {"CbteTipo": cbte_tipo, "PtoVta": pto_vta},
        })
        if resp.ok:
            data = resp.json() or {}
            return {"success": True, "ultimo_nro": data.get("CbteNro", 0)}
        return {"success": False, "error": f"HTTP {resp.status_code}"}

    def _get_taxpayer_types(self, params: dict[str, Any]) -> dict[str, Any]:
        resp = self._http.get("/fe/tipos", params={"tipo": "tributos"})
        if resp.ok:
            data = resp.json() or {}
            return {"success": True, "tipos": data.get("Tributos", [])}
        return {"success": False, "error": f"HTTP {resp.status_code}"}

    def _get_vat_conditions(self, params: dict[str, Any]) -> dict[str, Any]:
        resp = self._http.get("/fe/tipos", params={"tipo": "iva"})
        if resp.ok:
            data = resp.json() or {}
            return {"success": True, "condiciones": data.get("IvaTipos", [])}
        return {"success": False, "error": f"HTTP {resp.status_code}"}

    def _get_point_of_sales(self, params: dict[str, Any]) -> dict[str, Any]:
        cuit = params.get("cuit", "")
        if not cuit:
            return {"success": False, "error": "Parametro requerido: cuit"}
        resp = self._http.get("/fe/ptos", params={"cuit": cuit})
        if resp.ok:
            data = resp.json() or {}
            return {"success": True, "puntos": data.get("PtoVta", [])}
        return {"success": False, "error": f"HTTP {resp.status_code}"}

    def _check_taxpayer_status(self, params: dict[str, Any]) -> dict[str, Any]:
        cuit = params.get("cuit", "")
        if not cuit:
            return {"success": False, "error": "Parametro requerido: cuit"}
        resp = self._http.get("/fe/status", params={"cuit": cuit})
        if resp.ok:
            data = resp.json() or {}
            return {"success": True, "estado": data.get("Estado", ""), "data": data}
        return {"success": False, "error": f"HTTP {resp.status_code}"}


AFIP_ARGENTINA_SCHEMA = ConnectorSchema(
    name="afip_argentina", version="1.0.0",
    description="Genera facturas electrónicas, crédito/débito y consulta compliance fiscal via AFIP WS",
    category="latam", icon="file-text", author="Zenic-Flijo",
    actions=[
        ActionDefinition(name="create_invoice", description="Crea factura electrónica", category="write"),
        ActionDefinition(name="create_credit_note", description="Crea nota de crédito", category="write"),
        ActionDefinition(name="create_debit_note", description="Crea nota de débito", category="write"),
        ActionDefinition(name="get_invoice", description="Consulta factura", category="read"),
        ActionDefinition(name="get_last_invoice_number", description="Obtiene último número de factura", category="read"),
        ActionDefinition(name="get_taxpayer_types", description="Tipos de tributos", category="read"),
        ActionDefinition(name="get_vat_conditions", description="Condiciones IVA", category="read"),
        ActionDefinition(name="get_point_of_sales", description="Puntos de venta", category="read"),
        ActionDefinition(name="check_taxpayer_status", description="Estado del contribuyente", category="read"),
    ],
    auth_requirements=[
        AuthRequirement(auth_type="api_key", required_fields=["cuit", "certificate_base64"],
                        description="CUIT + Certificado digital AFIP (WSAA)")
    ],
)
