"""
Workflow Determinista — LogicGate Service
"""
from src.workflow.condition_evaluator import ConditionEvaluator
from src.utils.logger import setup_logging

logger = setup_logging(__name__)


class LogicGateService:
    def __init__(self):
        self._evaluator = ConditionEvaluator()

    def evaluate_rule(self, rule: str, context: dict) -> bool:
        return self._evaluator.evaluate(rule, context)

    def validate_expression(self, expression: str) -> dict:
        return self._evaluator.validate_expression(expression)
