"""
Paquete de metricas para observabilidad.

Este paquete consolida:

- ``MetricsRegistry`` (en ``registry.py``): registro centralizado de
  contadores, histogramas y gauges Prometheus-compatible. Re-exportado
  aqui para que ``from src.observability.metrics import MetricsRegistry``
  siga funcionando (backward compatibility con la version previa del
  modulo ``metrics.py`` plano).
- ``OTEL_METRICS_PORT``: constante de configuracion re-exportada desde
  ``src.observability.telemetry_config`` para mantener backward
  compatibility con ``from src.observability.metrics import OTEL_METRICS_PORT``.
- 15 mixins (uno por dominio) que ``TelemetryService`` hereda para
  componer su API publica de ``record_*`` / ``set_*`` sin duplicar
  logica. Cada mixin asume que la clase coordinadora provee los
  atributos ``_metrics`` (MetricsRegistry), ``_tracing``
  (TracingManager), ``_active_spans`` (dict),
  ``_active_workflow_timers`` (dict) y ``_db`` (DatabaseManager).

Convenciones:
- Los mixins NO definen ``__init__``: la inicializacion vive en
  ``TelemetryService``.
- Cada archivo mixin debe mantenerse <200 LOC.
"""

from src.observability.metrics.agent_metrics import AgentMetricsMixin
from src.observability.metrics.auth_metrics import AuthMetricsMixin
from src.observability.metrics.bpmn_metrics import BPMNMetricsMixin
from src.observability.metrics.compliance_metrics import ComplianceMetricsMixin
from src.observability.metrics.connector_metrics import ConnectorMetricsMixin
from src.observability.metrics.db_metrics import DBMetricsMixin
from src.observability.metrics.marketplace_metrics import MarketplaceMetricsMixin
from src.observability.metrics.mobile_metrics import MobileMetricsMixin
from src.observability.metrics.nlu_metrics import NLUMetricsMixin
from src.observability.metrics.partner_metrics import PartnerMetricsMixin
from src.observability.metrics.registry import MetricsRegistry
from src.observability.metrics.step_metrics import StepMetricsMixin
from src.observability.metrics.sync_metrics import SyncMetricsMixin
from src.observability.metrics.system_metrics import SystemMetricsMixin
from src.observability.metrics.tenant_metrics import TenantMetricsMixin
from src.observability.metrics.workflow_metrics import WorkflowMetricsMixin
from src.observability.telemetry_config import OTEL_METRICS_PORT

__all__ = [
    "AgentMetricsMixin",
    "AuthMetricsMixin",
    "BPMNMetricsMixin",
    "ComplianceMetricsMixin",
    "ConnectorMetricsMixin",
    "DBMetricsMixin",
    "MarketplaceMetricsMixin",
    "MetricsRegistry",
    "MobileMetricsMixin",
    "NLUMetricsMixin",
    "OTEL_METRICS_PORT",
    "PartnerMetricsMixin",
    "StepMetricsMixin",
    "SyncMetricsMixin",
    "SystemMetricsMixin",
    "TenantMetricsMixin",
    "WorkflowMetricsMixin",
]
