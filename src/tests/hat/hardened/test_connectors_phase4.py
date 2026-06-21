"""Tests para conectores externos registrados en HAT Level 5.

Verifica que los 61 conectores de src/connectors/ están registrados
en ToolsRegistry._REGISTRY como ToolRegistration entries.

Cubre:
- _REGISTRY tiene 80 entries (19 nativas + 61 conectores).
- Cada dominio tiene el número correcto de conectores.
- CONNECTORS_REGISTRY tiene 61 entradas.
- Names únicos (no duplicados con tools nativas).
- Todos los dominios son válidos.
"""
from __future__ import annotations

import pytest

from src.hat.level5_tools.connectors_registry import CONNECTORS_REGISTRY
from src.hat.level5_tools.registry import _REGISTRY, ToolRegistration, ToolsRegistry


class TestConnectorsRegistry:
    """CONNECTORS_REGISTRY tiene las 61 entradas esperadas."""

    def test_connectors_registry_has_61_entries(self) -> None:
        """CONNECTORS_REGISTRY tiene exactamente 61 entradas."""
        assert len(CONNECTORS_REGISTRY) == 61

    def test_all_entries_are_tuples_of_6(self) -> None:
        """Cada entrada es una tupla de 6 elementos."""
        for entry in CONNECTORS_REGISTRY:
            assert isinstance(entry, tuple)
            assert len(entry) == 6

    def test_unique_connector_names(self) -> None:
        """Todos los names son únicos."""
        names = [e[0] for e in CONNECTORS_REGISTRY]
        assert len(names) == len(set(names))

    def test_all_domains_valid(self) -> None:
        """Todos los dominios son válidos."""
        valid_domains = {"operaciones", "comunicaciones", "datos_auto"}
        for _, domain, _, _, _, _ in CONNECTORS_REGISTRY:
            assert domain in valid_domains

    def test_operaciones_has_20_connectors(self) -> None:
        """operaciones tiene 20 conectores."""
        ops = [e for e in CONNECTORS_REGISTRY if e[1] == "operaciones"]
        assert len(ops) == 20

    def test_comunicaciones_has_11_connectors(self) -> None:
        """comunicaciones tiene 11 conectores."""
        comms = [e for e in CONNECTORS_REGISTRY if e[1] == "comunicaciones"]
        assert len(comms) == 11

    def test_datos_auto_has_30_connectors(self) -> None:
        """datos_auto tiene 30 conectores."""
        datos = [e for e in CONNECTORS_REGISTRY if e[1] == "datos_auto"]
        assert len(datos) == 30


class TestMergedRegistry:
    """_REGISTRY tiene 19 nativas + 61 conectores = 80 total."""

    def test_registry_has_80_entries(self) -> None:
        """_REGISTRY tiene 80 entries tras Phase 4."""
        assert len(_REGISTRY) == 80

    def test_all_entries_are_tool_registration(self) -> None:
        """Todas las entradas son ToolRegistration."""
        for reg in _REGISTRY:
            assert isinstance(reg, ToolRegistration)

    def test_unique_names_in_merged_registry(self) -> None:
        """Todos los names son únicos en el registry combinado."""
        names = [r.name for r in _REGISTRY]
        assert len(names) == len(set(names))

    def test_native_tools_present(self) -> None:
        """Las 19 tools nativas siguen presentes."""
        native_names = {
            "crm", "invoice", "inventory",
            "stripe", "mercadopago",
            "notification", "gmail", "slack", "telegram",
            "data_keeper", "api_connector", "sheets", "drive", "postgresql",
            "code_runner", "logic_gate", "autopilot", "openai", "ollama",
        }
        registry_names = {r.name for r in _REGISTRY}
        for name in native_names:
            assert name in registry_names, f"native tool '{name}' missing"

    def test_connector_tools_present(self) -> None:
        """Conectores clave están presentes."""
        key_connectors = {
            "salesforce", "hubspot", "jira", "github", "gitlab",
            "slack", "twilio", "paypal", "shopify",
            "datadog", "grafana", "notion",
        }
        registry_names = {r.name for r in _REGISTRY}
        for name in key_connectors:
            assert name in registry_names, f"connector '{name}' missing"

    def test_domains_distribution(self) -> None:
        """Distribución por dominio es correcta."""
        ops = [r for r in _REGISTRY if r.domain == "operaciones"]
        comms = [r for r in _REGISTRY if r.domain == "comunicaciones"]
        datos = [r for r in _REGISTRY if r.domain == "datos_auto"]
        # operaciones: 3 business + 2 payments + 20 connectors = 25
        assert len(ops) == 25
        # comunicaciones: 4 native + 11 connectors = 15
        assert len(comms) == 15
        # datos_auto: 5 data + 5 automation + 30 connectors = 40
        assert len(datos) == 40


class TestToolsRegistryWithConnectors:
    """ToolsRegistry funciona con los conectores registrados."""

    def test_list_domains_returns_3(self) -> None:
        """list_domains() retorna los 3 dominios."""
        ToolsRegistry._instance = None
        registry = ToolsRegistry()
        domains = registry.list_domains()
        assert "operaciones" in domains
        assert "comunicaciones" in domains
        assert "datos_auto" in domains

    def test_list_categories_includes_all(self) -> None:
        """list_categories() incluye todas las categorías."""
        ToolsRegistry._instance = None
        registry = ToolsRegistry()
        cats = registry.list_categories()
        for expected in ("business", "payments", "communications", "data", "automation"):
            assert expected in cats

    def test_get_spec_for_connector(self) -> None:
        """get_spec() retorna ToolRegistration para un conector."""
        ToolsRegistry._instance = None
        registry = ToolsRegistry()
        spec = registry.get_spec("salesforce")
        assert spec is not None
        assert spec.domain == "operaciones"
        assert spec.category == "business"

    def test_get_spec_for_native_tool(self) -> None:
        """get_spec() funciona para tools nativas."""
        ToolsRegistry._instance = None
        registry = ToolsRegistry()
        spec = registry.get_spec("crm")
        assert spec is not None
        assert spec.domain == "operaciones"

    def test_get_spec_returns_none_for_unknown(self) -> None:
        """get_spec() retorna None para tool desconocida."""
        ToolsRegistry._instance = None
        registry = ToolsRegistry()
        assert registry.get_spec("nonexistent_tool") is None

    def test_list_by_domain_operaciones(self) -> None:
        """list_by_domain('operaciones') retorna 25 specs."""
        ToolsRegistry._instance = None
        registry = ToolsRegistry()
        ops_specs = {
            name for name, spec in registry._specs.items()
            if spec.domain == "operaciones"
        }
        assert len(ops_specs) == 25

    def test_len_registry_specs(self) -> None:
        """len(registry._specs) == 80."""
        ToolsRegistry._instance = None
        registry = ToolsRegistry()
        assert len(registry._specs) == 80
