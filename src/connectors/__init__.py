"""
Conectores Enterprise — Registro de 60 Conectores del Marketplace
===================================================================

Registro completo de todos los conectores en el ConnectorRegistry.
"""

from __future__ import annotations

from src.connectors.airtable import AirtableConnector
from src.connectors.anthropic import AnthropicConnector
from src.connectors.asana import AsanaConnector
from src.connectors.aws_s3 import AwsS3Connector
from src.connectors.azure_ad import AzureADConnector
from src.connectors.azure_blob import AzureBlobConnector
from src.connectors.confluence import ConfluenceConnector
from src.connectors.datadog import DatadogConnector
from src.connectors.deepseek import DeepseekConnector
from src.connectors.discord import DiscordConnector
from src.connectors.dropbox import DropboxConnector
from src.connectors.elastic import ElasticConnector
from src.connectors.freshdesk import FreshdeskConnector
from src.connectors.gcs import GcsConnector
from src.connectors.github import GithubConnector
from src.connectors.gitlab import GitlabConnector
from src.connectors.hubspot import HubspotConnector
from src.connectors.huggingface import HuggingfaceConnector
from src.connectors.intercom import IntercomConnector
from src.connectors.jira import JiraConnector
from src.connectors.mailgun import MailgunConnector
from src.connectors.marketo import MarketoConnector
from src.connectors.mercadolibre import MercadolibreConnector
from src.connectors.mongo_connector import MongoConnectorConnector
from src.connectors.mysql_connector import MysqlConnectorConnector
from src.connectors.new_relic import NewRelicConnector
from src.connectors.nfe import NfeConnector
from src.connectors.notion import NotionConnector
from src.connectors.openai_v2 import OpenaiV2Connector
from src.connectors.pagerduty import PagerDutyConnector
from src.connectors.paypal import PaypalConnector
from src.connectors.pipedrive import PipedriveConnector
from src.connectors.pix_brazil import PixBrazilConnector
from src.connectors.quickbooks import QuickbooksConnector
from src.connectors.ruv import RuvConnector
from src.connectors.salesforce import SalesforceConnector
from src.connectors.sat_mexico import SatMexicoConnector
from src.connectors.sendgrid import SendGridConnector
from src.connectors.sentry import SentryConnector
from src.connectors.square import SquareConnector
from src.connectors.sumologic import SumoLogicConnector
from src.connectors.teams import TeamsConnector
from src.connectors.totvs import TotvsConnector
from src.connectors.trello import TrelloConnector
from src.connectors.twilio import TwilioConnector
from src.connectors.typeform import TypeformConnector
from src.connectors.vault import VaultConnector
from src.connectors.whatsapp import WhatsAppConnector
from src.connectors.wise import WiseConnector
from src.connectors.woocommerce import WooCommerceConnector
from src.connectors.zoho_crm import ZohoCrmConnector
from src.sdk.registry import ConnectorRegistry

# Todos los conectores registrados (60 total)
_ALL_CONNECTORS: list[type] = [
    # AI & Data (4)
    AnthropicConnector,
    DeepseekConnector,
    HuggingfaceConnector,
    OpenaiV2Connector,
    # Cloud Storage (4)
    AwsS3Connector,
    AzureBlobConnector,
    DropboxConnector,
    GcsConnector,
    # Communication (8)
    DiscordConnector,
    IntercomConnector,
    MailgunConnector,
    SendGridConnector,
    TeamsConnector,
    TwilioConnector,
    WhatsAppConnector,
    # CRM & Sales (4)
    HubspotConnector,
    PipedriveConnector,
    SalesforceConnector,
    ZohoCrmConnector,
    # Databases (3)
    ElasticConnector,
    MongoConnectorConnector,
    MysqlConnectorConnector,
    # DevOps & Monitoring (6)
    DatadogConnector,
    GithubConnector,
    GitlabConnector,
    NewRelicConnector,
    PagerDutyConnector,
    SentryConnector,
    # E-commerce (1)
    WooCommerceConnector,
    # ERP (1)
    TotvsConnector,
    # Finance & Payments (4)
    PaypalConnector,
    PixBrazilConnector,
    QuickbooksConnector,
    SquareConnector,
    WiseConnector,
    # Forms (1)
    TypeformConnector,
    # Identity (1)
    AzureADConnector,
    # Marketing (1)
    MarketoConnector,
    # LATAM (4)
    NfeConnector,
    MercadolibreConnector,
    RuvConnector,
    SatMexicoConnector,
    # Monitoring & Logging (1)
    SumoLogicConnector,
    # No-code Database (1)
    AirtableConnector,
    # Project Management (5)
    AsanaConnector,
    ConfluenceConnector,
    JiraConnector,
    NotionConnector,
    TrelloConnector,
    # Security (2)
    VaultConnector,
    # Support (1)
    FreshdeskConnector,
]


def register_all_connectors() -> list[str]:
    """Registra todos los conectores enterprise en el ConnectorRegistry.

    Retorna:
        Lista de nombres de conectores registrados exitosamente
    """
    registered: list[str] = []
    registry = ConnectorRegistry()
    for connector_cls in _ALL_CONNECTORS:
        try:
            registry.register(connector_cls, override=True)
            registered.append(connector_cls.name)
        except Exception as e:
            import logging
            logging.getLogger(__name__).warning(f"Error registrando {connector_cls.__name__}: {e}")
    return registered


# Auto-registro al importar el modulo
register_all_connectors()

__all__ = [
    "AirtableConnector",
    "AnthropicConnector",
    "AsanaConnector",
    "AwsS3Connector",
    "AzureADConnector",
    "AzureBlobConnector",
    "ConfluenceConnector",
    "DatadogConnector",
    "DeepseekConnector",
    "DiscordConnector",
    "DropboxConnector",
    "ElasticConnector",
    "FreshdeskConnector",
    "GcsConnector",
    "GithubConnector",
    "GitlabConnector",
    "HubspotConnector",
    "HuggingfaceConnector",
    "IntercomConnector",
    "JiraConnector",
    "MailgunConnector",
    "MarketoConnector",
    "MercadolibreConnector",
    "MongoConnectorConnector",
    "MysqlConnectorConnector",
    "NewRelicConnector",
    "NfeConnector",
    "NotionConnector",
    "OpenaiV2Connector",
    "PagerDutyConnector",
    "PaypalConnector",
    "PipedriveConnector",
    "PixBrazilConnector",
    "QuickbooksConnector",
    "RuvConnector",
    "SalesforceConnector",
    "SatMexicoConnector",
    "SendGridConnector",
    "SentryConnector",
    "SquareConnector",
    "SumoLogicConnector",
    "TeamsConnector",
    "TotvsConnector",
    "TrelloConnector",
    "TwilioConnector",
    "TypeformConnector",
    "VaultConnector",
    "WhatsAppConnector",
    "WiseConnector",
    "WooCommerceConnector",
    "ZohoCrmConnector",
    "register_all_connectors",
]
