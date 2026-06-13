"""DDE v3 — NLU Package (Fase 3).

Componentes del pipeline NLU determinista + IA:
- Pipeline orquestador con smart_compile (guardrails + fallback hierarchy)
- Intent Classifier TF-IDF, Slot Filler, Entity Extractor
- WorkflowCompiler, Validator, Explainer
- AI Generator con guardrails de contenido, ejecución y PII
- Guardrails de IA: ContentGuardrails, ExecutionGuardrails, PIIGuardrails
- Fallback Hierarchy: determinista → orbital → IA → template genérico
"""

from src.nlu.ai_generator import AIGenerationResult, WorkflowAIGenerator, generate_workflow_from_text
from src.nlu.compiler import WorkflowCompiler
from src.nlu.disambiguator import Disambiguator
from src.nlu.explainer import Explainer
from src.nlu.fallback import FallbackConfig, FallbackLevel, FallbackOrchestrator, FallbackResult, get_fallback_message
from src.nlu.guardrails import (
    CompositeGuardrailResult,
    ContentGuardrails,
    ExecutionGuardrails,
    GuardrailAction,
    GuardrailManager,
    GuardrailResult,
    PIIGuardrails,
    RiskLevel,
)
from src.nlu.intent_classifier import IntentClassifier
from src.nlu.language_router import LanguageRouter
from src.nlu.normalizer import normalize
from src.nlu.pipeline import Pipeline, compile_workflow, simulate_workflow, understand
from src.nlu.slot_filler import SlotFiller
from src.nlu.tokenizer import tokenize
from src.nlu.validator import WorkflowValidator

__all__ = [
    # Case-insensitive sorted
    "AIGenerationResult",
    "CompositeGuardrailResult",
    "ContentGuardrails",
    "Disambiguator",
    "ExecutionGuardrails",
    "Explainer",
    "FallbackConfig",
    "FallbackLevel",
    "FallbackOrchestrator",
    "FallbackResult",
    "GuardrailAction",
    "GuardrailManager",
    "GuardrailResult",
    "IntentClassifier",
    "LanguageRouter",
    "PIIGuardrails",
    "Pipeline",
    "RiskLevel",
    "SlotFiller",
    "WorkflowAIGenerator",
    "WorkflowCompiler",
    "WorkflowValidator",
    "compile_workflow",
    "generate_workflow_from_text",
    "get_fallback_message",
    "normalize",
    "simulate_workflow",
    "tokenize",
    "understand",
]
