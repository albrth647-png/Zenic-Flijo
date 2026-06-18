"""
API Connector package — Sprint 5.
"""

from src.tools.api_connector.pagination import PaginationCollector
from src.tools.api_connector.rate_limiter import RateLimiter
from src.tools.api_connector.response_cache import ResponseCache
from src.tools.api_connector.service import APIConnectorService
from src.tools.api_connector.webhooks import WebhookCallbackRegistry
from src.tools.api_connector.xml_processor import XMLProcessor

__all__ = [
    "APIConnectorService",
    "PaginationCollector",
    "RateLimiter",
    "ResponseCache",
    "WebhookCallbackRegistry",
    "XMLProcessor",
]
