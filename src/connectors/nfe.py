"""
Conector NF-e/NFC-e — Nota Fiscal Eletrônica Brasileira
==========================================================

Implementa integração com o sistema de Nota Fiscal Eletrônica (NF-e)
e Nota Fiscal ao Consumidor Eletrônica (NFC-e) do Brasil.

Funcionalidades:
- Emissão de NF-e (modelo 55) com certificado A1/A3
- Emissão de NFC-e (modelo 65) para varejo
- Consulta de status na SEFAZ
- Cancelamento e inutilização de notas
- Download de XML e DANFE (PDF)
- Carta de correção eletrônica (CC-e)
- Manifestação do destinatário
- DPEC (contigência)
- Integração com SEFAZ autorizadora por UF
"""

from __future__ import annotations

from typing import Any

from src.sdk.base import BaseConnector
from src.sdk.http_client import HttpClient, HTTPClientError
from src.sdk.schema import ActionDefinition, AuthRequirement, ConnectorSchema
from src.core.logging import setup_logging

logger = setup_logging(__name__)

# Mapeamento de UFs para SEFAZ autorizadoras (produção)
UF_AUTHORIZERS_PROD: dict[str, str] = {
    "AM": "nfe.sefaz.am.gov.br", "BA": "nfe.sefaz.ba.gov.br",
    "CE": "nfe.sefaz.ce.gov.br", "GO": "nfe.sefaz.go.gov.br",
    "MG": "nfe.fazenda.mg.gov.br", "MS": "nfe.sefaz.ms.gov.br",
    "MT": "nfe.sefaz.mt.gov.br", "PE": "nfe.sefaz.pe.gov.br",
    "PR": "nfe.sefaz.pr.gov.br", "RS": "nfe.sefaz.rs.gov.br",
    "SP": "nfe.fazenda.sp.gov.br", "SVRS": "nfe.sefazvirtual.rs.gov.br",
    "SVAN": "nfe.sefazvirtual.fazenda.gov.br",
}

# Mapeamento de UFs para SEFAZ homologação
UF_AUTHORIZERS_HOM: dict[str, str] = {
    "AM": "hom1.sefazvirtual.am.gov.br", "BA": "hnfe.sefaz.ba.gov.br",
    "CE": "nfe.sefaz.ce.gov.br", "GO": "homolog.sefaz.go.gov.br",
    "MG": "hnfe.fazenda.mg.gov.br", "MS": "hom.nfe.ms.gov.br",
    "MT": "hom1.sefaz.mt.gov.br", "PE": "nfehomolog.sefaz.pe.gov.br",
    "PR": "homnfe.sefa.pr.gov.br", "RS": "nfe-homologacao.sefazrs.rs.gov.br",
    "SP": "hom1.nfe.fazenda.sp.gov.br", "SVRS": "hom1.sefazvirtual.rs.gov.br",
    "SVAN": "hom.sefazvirtual.fazenda.gov.br",
}

# Ambientes
AMBIENTES = {"producao": "1", "homologacao": "2"}

# Status possíveis de NF-e
STATUS_NFE = {
    "100": "Autorizada",
    "101": "Cancelada",
    "102": "Inutilizada",
    "104": "Denegada",
    "107": "Denegada (SCE)",
    "110": "Denegada (sujeição a regime especial)",
    "128": "Lote sem nota fiscal",
    "135": "Evento de EPEC registrado",
    "136": "Evento de CC-e registrado",
    "137": "Evento de cancelamento registrado",
    "138": "Evento de EPEC cancelado",
    "150": "Processando lote (aguardando autorização)",
    "151": "Serviço em contingência",
    "155": "Sistema em contingência",
    "200": "Autorizada fora de prazo",
    "201": "Denegada fora de prazo",
    "202": "Cancelada fora de prazo",
    "203": "Nota fiscal de emissão própria",
    "204": "Emissão em contingência",
    "205": "Emissão em contingência cancelada",
    "206": "Emissão em contingência denegada",
    "301": "Uso Denegado (irregularidade fiscal do destinatário)",
    "302": "Uso Denegado (irregularidade fiscal do emitente)",
    "303": "Pedido de Cancelamento em andamento",
}


class NfeConnector(BaseConnector):
    """Conector para NF-e/NFC-e brasileira com SEFAZ."""

    name = "nfe"
    version = "1.0.0"
    description = "Emite, consulta e gerencia NF-e (modelo 55) e NFC-e (modelo 65) do Brasil"
    category = "latam"
    icon = "file-text"
    author = "Zenic-Flijo"

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._base_url: str = ""
        self._http: HttpClient | None = None
        self._uf: str = "SP"
        self._ambiente: str = "homologacao"
        self._cnpj: str = ""
        self._cert_path: str = ""
        self._cert_password: str = ""

    def connect(self) -> bool:
        """Estabelece conexão com a SEFAZ autorizadora."""
        if not self._auth_provider or not self._auth_provider.validate():
            logger.error("NfeConnector: credenciais não configuradas")
            return False
        try:
            creds = self._auth_provider.get_credentials()
            self._uf = creds.get("uf", "SP").upper()
            self._ambiente = creds.get("ambiente", "homologacao")
            self._cnpj = creds.get("cnpj", "")
            self._cert_path = creds.get("cert_path", "")
            self._cert_password = creds.get("cert_password", "")

            # Determinar URL da SEFAZ (produção ou homologação)
            uf_map = UF_AUTHORIZERS_PROD if self._ambiente == "producao" else UF_AUTHORIZERS_HOM
            sefaz_host = uf_map.get(self._uf, uf_map["SVRS"])
            self._base_url = f"https://{sefaz_host}/NfeAutorizacao/ws"

            self._http = HttpClient(
                base_url=self._base_url,
                connector_name=self.name,
            )
            if self._cnpj:
                self._http.set_header("X-CNPJ", self._cnpj)

            self._connected = True
            self._log_operation("connect", f"SEFAZ {self._uf} conectada ({self._ambiente})")
            return True
        except HTTPClientError as e:
            logger.error(f"NfeConnector: erro de conexão SEFAZ - {e}")
            return False
        except Exception as e:
            logger.error(f"NfeConnector: erro inesperado - {e}")
            return False

    def execute(self, action: str, params: dict[str, Any]) -> Any:
        """Executa uma ação do conector NF-e/NFC-e."""
        action_map: dict[str, Any] = {
            "emitir_nfe": self._emitir_nfe,
            "emitir_nfce": self._emitir_nfce,
            "consultar_status": self._consultar_status,
            "cancelar_nfe": self._cancelar_nfe,
            "inutilizar_faixa": self._inutilizar_faixa,
            "consultar_nfe": self._consultar_nfe,
            "download_xml": self._download_xml,
            "download_danfe": self._download_danfe,
            "carta_correcao": self._carta_correcao,
            "manifestar_destinatario": self._manifestar_destinatario,
        }
        handler = action_map.get(action)
        if handler is None:
            return {"error": f"Ação '{action}' não suportada", "available": list(action_map.keys())}
        return handler(params)

    def validate(self) -> bool:
        """Valida as credenciais do conector NF-e."""
        if not self._auth_provider:
            return False
        return self._auth_provider.validate()

    def disconnect(self) -> bool:
        """Desconecta da SEFAZ."""
        self._http = None
        self._connected = False
        self._log_operation("disconnect")
        return True

    def _emitir_nfe(self, params: dict[str, Any]) -> dict[str, Any]:
        """Emite uma NF-e (modelo 55).

        Args:
            params: Deve conter 'destinatario', 'produtos', 'natureza_operacao'
        """
        destinatario = params.get("destinatario", {})
        produtos = params.get("produtos", [])
        if not destinatario or not produtos:
            return {"success": False, "error": "Parâmetros obrigatórios: destinatario, produtos"}
        self._log_operation("emitir_nfe", f"destinatario={destinatario.get('cnpj', destinatario.get('cpf', 'N/A'))}")

        payload = {
            "modelo": "55",
            "ambiente": AMBIENTES.get(self._ambiente, "2"),
            "natureza_operacao": params.get("natureza_operacao", "Venda"),
            "destinatario": destinatario,
            "produtos": produtos,
            "forma_pagamento": params.get("forma_pagamento", []),
            "frete": params.get("frete", {}),
            "informacoes_adicionais": params.get("informacoes_adicionais", ""),
            "emitente": {"cnpj": self._cnpj} if self._cnpj else {},
        }
        if params.get("pedido"):
            payload["pedido"] = params["pedido"]

        try:
            resp = self._http.post("/nfe/emitir", json=payload)
            if resp.ok:
                data = resp.json() or {}
                return {
                    "success": True,
                    "chave": data.get("chave", ""),
                    "numero": data.get("numero", ""),
                    "serie": data.get("serie", ""),
                    "status": data.get("status", ""),
                    "protocolo": data.get("protocolo", ""),
                    "xml": data.get("xml", ""),
                    "danfe_base64": data.get("danfe_base64", ""),
                    "data": data,
                }
            return {"success": False, "error": f"HTTP {resp.status_code}: {resp.body}"}
        except HTTPClientError as e:
            return {"success": False, "error": str(e)}

    def _emitir_nfce(self, params: dict[str, Any]) -> dict[str, Any]:
        """Emite uma NFC-e (modelo 65) para varejo.

        Args:
            params: Deve conter 'itens', 'forma_pagamento', 'cpf_cnpj_consumidor'
        """
        itens = params.get("itens", [])
        forma_pagamento = params.get("forma_pagamento", [])
        if not itens or not forma_pagamento:
            return {"success": False, "error": "Parâmetros obrigatórios: itens, forma_pagamento"}
        self._log_operation("emitir_nfce", f"{len(itens)} itens")

        payload = {
            "modelo": "65",
            "ambiente": AMBIENTES.get(self._ambiente, "2"),
            "itens": itens,
            "forma_pagamento": forma_pagamento,
            "consumidor": {"cpf_cnpj": params.get("cpf_cnpj_consumidor", "")},
            "informacoes_adicionais": params.get("informacoes_adicionais", ""),
        }

        try:
            resp = self._http.post("/nfce/emitir", json=payload)
            if resp.ok:
                data = resp.json() or {}
                return {
                    "success": True,
                    "chave": data.get("chave", ""),
                    "numero": data.get("numero", ""),
                    "status": data.get("status", ""),
                    "protocolo": data.get("protocolo", ""),
                    "xml": data.get("xml", ""),
                    "danfe_base64": data.get("danfe_base64", ""),
                    "qr_code": data.get("qr_code", ""),
                    "data": data,
                }
            return {"success": False, "error": f"HTTP {resp.status_code}: {resp.body}"}
        except HTTPClientError as e:
            return {"success": False, "error": str(e)}

    def _consultar_status(self, params: dict[str, Any] | None = None) -> dict[str, Any]:
        """Consulta o status da SEFAZ."""
        self._log_operation("consultar_status")

        try:
            resp = self._http.get(f"/status/{self._uf}")
            if resp.ok:
                data = resp.json() or {}
                return {
                    "success": True,
                    "uf": self._uf,
                    "ambiente": self._ambiente,
                    "status": data.get("status", ""),
                    "data_hora": data.get("data_hora", ""),
                    "tempo_medio": data.get("tempo_medio", 0),
                    "data": data,
                }
            return {"success": False, "error": f"HTTP {resp.status_code}: {resp.body}"}
        except HTTPClientError as e:
            return {"success": False, "error": str(e)}

    def _cancelar_nfe(self, params: dict[str, Any]) -> dict[str, Any]:
        """Cancela uma NF-e/NFC-e já autorizada.

        Args:
            params: Deve conter 'chave', 'justificativa'
        """
        chave = params.get("chave", "")
        justificativa = params.get("justificativa", "")
        if not chave or not justificativa:
            return {"success": False, "error": "Parâmetros obrigatórios: chave, justificativa"}
        if len(justificativa) < 15:
            return {"success": False, "error": "Justificativa deve ter no mínimo 15 caracteres"}
        self._log_operation("cancelar_nfe", f"chave={chave}")

        try:
            resp = self._http.post(
                f"/nfe/{chave}/cancelar",
                json={"chave": chave, "justificativa": justificativa, "cnpj": self._cnpj},
            )
            if resp.ok:
                data = resp.json() or {}
                return {
                    "success": True,
                    "chave": chave,
                    "status": data.get("status", "Cancelada"),
                    "protocolo": data.get("protocolo", ""),
                    "data": data,
                }
            return {"success": False, "error": f"HTTP {resp.status_code}: {resp.body}"}
        except HTTPClientError as e:
            return {"success": False, "error": str(e)}

    def _inutilizar_faixa(self, params: dict[str, Any]) -> dict[str, Any]:
        """Inutiliza uma faixa de numeração de NF-e.

        Args:
            params: Deve conter 'serie', 'numero_inicial', 'numero_final', 'justificativa'
        """
        serie = params.get("serie", "")
        num_ini = params.get("numero_inicial", "")
        num_fim = params.get("numero_final", "")
        justificativa = params.get("justificativa", "")
        if not serie or not num_ini or not num_fim or not justificativa:
            return {"success": False, "error": "Parâmetros obrigatórios: serie, numero_inicial, numero_final, justificativa"}
        self._log_operation("inutilizar_faixa", f"serie={serie} ({num_ini}-{num_fim})")

        try:
            resp = self._http.post(
                "/nfe/inutilizar",
                json={"cnpj": self._cnpj, "serie": serie, "numero_inicial": num_ini,
                      "numero_final": num_fim, "justificativa": justificativa,
                      "ambiente": AMBIENTES.get(self._ambiente, "2")},
            )
            if resp.ok:
                data = resp.json() or {}
                return {"success": True, "protocolo": data.get("protocolo", ""), "data": data}
            return {"success": False, "error": f"HTTP {resp.status_code}: {resp.body}"}
        except HTTPClientError as e:
            return {"success": False, "error": str(e)}

    def _consultar_nfe(self, params: dict[str, Any]) -> dict[str, Any]:
        """Consulta NF-e por chave de acesso.

        Args:
            params: Deve conter 'chave'
        """
        chave = params.get("chave", "")
        if not chave:
            return {"success": False, "error": "Parâmetro obrigatório: chave"}
        self._log_operation("consultar_nfe", f"chave={chave}")

        try:
            resp = self._http.get(f"/nfe/{chave}")
            if resp.ok:
                data = resp.json() or {}
                return {
                    "success": True,
                    "chave": chave,
                    "status": data.get("status", ""),
                    "status_descricao": STATUS_NFE.get(data.get("status", ""), ""),
                    "data": data,
                }
            return {"success": False, "error": f"HTTP {resp.status_code}: {resp.body}"}
        except HTTPClientError as e:
            return {"success": False, "error": str(e)}

    def _download_xml(self, params: dict[str, Any]) -> dict[str, Any]:
        """Download do XML da NF-e.

        Args:
            params: Deve conter 'chave'
        """
        chave = params.get("chave", "")
        if not chave:
            return {"success": False, "error": "Parâmetro obrigatório: chave"}
        self._log_operation("download_xml", f"chave={chave}")

        try:
            resp = self._http.get(f"/nfe/{chave}/xml")
            if resp.ok:
                data = resp.json() or {}
                return {"success": True, "chave": chave, "xml": data.get("xml", ""), "data": data}
            return {"success": False, "error": f"HTTP {resp.status_code}: {resp.body}"}
        except HTTPClientError as e:
            return {"success": False, "error": str(e)}

    def _download_danfe(self, params: dict[str, Any]) -> dict[str, Any]:
        """Download do DANFE em PDF (base64).

        Args:
            params: Deve conter 'chave'
        """
        chave = params.get("chave", "")
        if not chave:
            return {"success": False, "error": "Parâmetro obrigatório: chave"}
        self._log_operation("download_danfe", f"chave={chave}")

        try:
            resp = self._http.get(f"/nfe/{chave}/danfe")
            if resp.ok:
                data = resp.json() or {}
                return {
                    "success": True,
                    "chave": chave,
                    "danfe_base64": data.get("danfe_base64", ""),
                    "content_type": "application/pdf",
                    "data": data,
                }
            return {"success": False, "error": f"HTTP {resp.status_code}: {resp.body}"}
        except HTTPClientError as e:
            return {"success": False, "error": str(e)}

    def _carta_correcao(self, params: dict[str, Any]) -> dict[str, Any]:
        """Carta de Correção Eletrônica (CC-e).

        Args:
            params: Deve conter 'chave', 'correcoes' (lista de {campo, novo_valor, motivo})
        """
        chave = params.get("chave", "")
        correcoes = params.get("correcoes", [])
        if not chave or not correcoes:
            return {"success": False, "error": "Parâmetros obrigatórios: chave, correcoes"}
        self._log_operation("carta_correcao", f"chave={chave}, {len(correcoes)} correções")

        try:
            resp = self._http.post(
                f"/nfe/{chave}/cc-e",
                json={"chave": chave, "correcoes": correcoes, "cnpj": self._cnpj},
            )
            if resp.ok:
                data = resp.json() or {}
                return {
                    "success": True,
                    "chave": chave,
                    "sequencia": data.get("sequencia", 1),
                    "protocolo": data.get("protocolo", ""),
                    "data": data,
                }
            return {"success": False, "error": f"HTTP {resp.status_code}: {resp.body}"}
        except HTTPClientError as e:
            return {"success": False, "error": str(e)}

    def _manifestar_destinatario(self, params: dict[str, Any]) -> dict[str, Any]:
        """Manifestação do destinatário (confirmar/ciência/desconhecer).

        Args:
            params: Deve conter 'chave', 'tipo'
                    (confirmacao, ciencia, desconhecimento, nao_realizar)
        """
        chave = params.get("chave", "")
        tipo = params.get("tipo", "")
        tipos_validos = ["confirmacao", "ciencia", "desconhecimento", "nao_realizar"]
        if not chave or tipo not in tipos_validos:
            return {"success": False, "error": f"Parâmetros obrigatórios: chave, tipo ({', '.join(tipos_validos)})"}
        self._log_operation("manifestar_destinatario", f"chave={chave}, tipo={tipo}")

        try:
            resp = self._http.post(
                f"/nfe/{chave}/manifestar",
                json={"chave": chave, "tipo": tipo, "cnpj": self._cnpj},
            )
            if resp.ok:
                data = resp.json() or {}
                return {"success": True, "chave": chave, "protocolo": data.get("protocolo", ""), "data": data}
            return {"success": False, "error": f"HTTP {resp.status_code}: {resp.body}"}
        except HTTPClientError as e:
            return {"success": False, "error": str(e)}


NFE_SCHEMA = ConnectorSchema(
    name="nfe",
    version="1.0.0",
    description="Emite, consulta e gerencia NF-e (modelo 55) e NFC-e (modelo 65) do Brasil",
    category="latam",
    icon="file-text",
    author="Zenic-Flijo",
    actions=[
        ActionDefinition(name="emitir_nfe", description="Emite NF-e modelo 55", category="write"),
        ActionDefinition(name="emitir_nfce", description="Emite NFC-e modelo 65 (varejo)", category="write"),
        ActionDefinition(name="consultar_status", description="Status da SEFAZ", category="read"),
        ActionDefinition(name="cancelar_nfe", description="Cancela NF-e/NFC-e autorizada", category="write"),
        ActionDefinition(name="inutilizar_faixa", description="Inutiliza faixa de numeração", category="write"),
        ActionDefinition(name="consultar_nfe", description="Consulta NF-e por chave", category="read"),
        ActionDefinition(name="download_xml", description="Download do XML da NF-e", category="read"),
        ActionDefinition(name="download_danfe", description="Download do DANFE em PDF", category="read"),
        ActionDefinition(name="carta_correcao", description="Carta de Correção Eletrônica CC-e", category="write"),
        ActionDefinition(name="manifestar_destinatario", description="Manifestação do destinatário", category="write"),
    ],
    auth_requirements=[
        AuthRequirement(auth_type="api_key", required_fields=["uf", "cnpj", "cert_path", "cert_password", "ambiente"],
                        description="Credenciais de acesso à SEFAZ + certificado A1/A3"),
    ],
)
