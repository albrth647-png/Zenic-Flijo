"""
DDE v3 — Guardrails: Orquestador
==================================

Punto de entrada unico para evaluar prompts y workflows
contra las tres capas de guardrails: contenido, ejecucion y PII.
"""

from __future__ import annotations

from src.nlu.guardrails.content import ContentGuardrails
from src.nlu.guardrails.execution import ExecutionGuardrails
from src.nlu.guardrails.pii import PIIGuardrails
from src.nlu.guardrails.result import CompositeGuardrailResult, GuardrailAction, GuardrailResult, RiskLevel


class GuardrailManager:
    """Orquestador de los tres tipos de guardrails.

    Usalo como punto de entrada unico para evaluar prompts y workflows.
    """

    def __init__(self, lang: str = "es"):
        self.lang = lang
        self.content = ContentGuardrails(lang)
        self.execution = ExecutionGuardrails(lang)
        self.pii = PIIGuardrails(lang)

    def check_prompt(self, text: str) -> CompositeGuardrailResult:
        """Evalua un prompt del usuario contra todas las capas."""
        checks: dict[str, GuardrailResult] = {
            "content": self.content.check_prompt(text),
        }
        return self._aggregate(checks)

    def check_workflow(self, workflow: dict) -> CompositeGuardrailResult:
        """Evalua un workflow completo contra todas las capas."""
        checks: dict[str, GuardrailResult] = {
            "execution": self.execution.check_workflow_definition(workflow),
            "pii": self.pii.check_workflow_for_pii(workflow),
        }
        return self._aggregate(checks)

    def check_all(self, prompt: str, workflow: dict) -> CompositeGuardrailResult:
        """Evalua prompt + workflow contra todas las capas."""
        checks: dict[str, GuardrailResult] = {
            "content": self.content.check_prompt(prompt),
            "execution": self.execution.check_workflow_definition(workflow),
            "pii": self.pii.check_workflow_for_pii(workflow),
        }
        return self._aggregate(checks)

    def _aggregate(self, checks: dict[str, GuardrailResult]) -> CompositeGuardrailResult:
        """Agrega multiples resultados de guardrail en uno compuesto."""
        blocks = [r for r in checks.values() if r.action == GuardrailAction.BLOCK]
        warnings = [r for r in checks.values() if r.action == GuardrailAction.WARN and r.passed]
        risks = [r.risk for r in checks.values()]

        # Prioridad de riesgo
        risk_order = [RiskLevel.CRITICAL, RiskLevel.HIGH, RiskLevel.MEDIUM, RiskLevel.LOW]
        max_risk = RiskLevel.LOW
        for risk in risk_order:
            if risk in risks:
                max_risk = risk
                break

        if blocks:
            return CompositeGuardrailResult(
                overall_passed=False,
                overall_action=GuardrailAction.BLOCK,
                checks=checks,
                risk=max_risk,
            )

        if warnings:
            return CompositeGuardrailResult(
                overall_passed=True,
                overall_action=GuardrailAction.WARN,
                checks=checks,
                risk=max_risk,
            )

        return CompositeGuardrailResult(
            overall_passed=True,
            overall_action=GuardrailAction.ALLOW,
            checks=checks,
            risk=RiskLevel.LOW,
        )
