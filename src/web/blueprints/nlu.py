"""
Blueprints — NLP Chat, AI Generation y NLU endpoints
"""

from flask import Blueprint, jsonify, request

from src.nlu.ai_config import get_ai_config
from src.nlu.intent_classifier import IntentClassifier
from src.nlu.pipeline import Pipeline
from src.nlu.templates import TEMPLATES
from src.web.helpers import login_required

bp = Blueprint("nlu", __name__)


@bp.route("/api/nlu/understand", methods=["POST"])
@login_required
def api_nlu_understand():
    """Endpoint NLU completo: análisis + compilación + simulación."""
    data = request.get_json() or {}
    text = data.get("text", "")
    mode = data.get("mode", "compile")
    lang = data.get("lang")
    context = data.get("context")

    if not text:
        return jsonify({"error": "text es requerido"}), 400

    pipeline = Pipeline()

    if mode == "analyze":
        result = pipeline.process(text, lang)
        return jsonify({
            "status": "analyzed",
            "lang": result.lang,
            "confidence": result.confidence,
            "intents": [{"intent": i.intent, "score": i.score, "evidence": i.evidence} for i in result.intents[:5]],
            "entities": [{"type": e.type, "value": str(e.value), "raw": e.raw} for e in result.entities],
            "slots": [{"name": s.name, "required": s.required, "filled": s.filled, "value": s.value} for s in result.slots],
            "trace": list(result.trace),
        })

    elif mode == "simulate":
        result = pipeline.simulate(text, lang, context)
        return jsonify({
            "status": "simulated",
            "workflow_name": result.workflow_name,
            "trigger_type": result.trigger_type,
            "total_steps": result.total_steps,
            "would_succeed": result.steps_that_would_succeed,
            "would_fail": result.steps_that_would_fail,
            "feasible": result.overall_feasible,
            "warnings": list(result.warnings),
            "summary": result.summary,
            "steps": [{"id": s.step_id, "tool": s.tool, "action": s.action, "ok": s.would_succeed} for s in result.steps],
        })

    else:  # compile (default)
        result = pipeline.compile(text, lang)
        return jsonify({
            "status": result.status,
            "explanation": result.explanation,
            "workflow": result.workflow,
            "missing_slots": list(result.missing_slots),
        })


@bp.route("/api/workflows/chat", methods=["POST"])
@login_required
def api_chat():
    """Chat endpoint — usa HATRouter (Nivel 1) para procesar mensajes."""
    data = request.get_json() or {}
    message = data.get("message", data.get("text", "")).strip()
    if not message:
        return jsonify({"error": "Message is required"}), 400

    # M8: Usar HATRouter (sistema HAT de 5 niveles)
    from src.hat import get_hat_router
    try:
        hat_router = get_hat_router()
        result = hat_router.handle(
            user_id=str(session.get("user_id", "1")),
            session_id=str(session.get("session_id", "default")),
            message=message,
        )
        return jsonify(result)
    except Exception as exc:
        logger.error("HAT chat error: %s", exc)
        return jsonify({"error": str(exc), "status": "failed"}), 500


@bp.route("/api/nlu/ai-generate", methods=["POST"])
@login_required
def api_nlu_ai_generate():
    """Genera un workflow usando IA.
    Modos:
    - ai: Genera workflow con LLM
    - hybrid: Intenta determinista primero, fallback a IA
    - deterministic: Solo usa el compilador determinista
    """
    data = request.get_json() or {}
    text = data.get("text", "")
    mode = data.get("mode", "hybrid")
    lang = data.get("lang", "es")

    if not text:
        return jsonify({"error": "text es requerido"}), 400

    pipeline = Pipeline()
    ai_config = get_ai_config()

    if mode == "deterministic":
        result = pipeline.compile(text, lang)
        return jsonify({
            "status": result.status,
            "source": "deterministic",
            "explanation": result.explanation,
            "workflow": result.workflow,
            "missing_slots": list(result.missing_slots),
            "ai_provider": "none",
        })

    if mode == "ai":
        if not ai_config.is_ai_available():
            return jsonify({
                "error": "No hay proveedor de IA configurado. "
                "Activa Ollama, OpenAI o Anthropic en Configuración.",
                "status": "no_provider",
                "available_providers": ai_config.get_status(),
            }), 400
        ai_result = pipeline.ai_generate(text, lang)
        return jsonify({
            "status": "ready" if ai_result.validated else "validation_error",
            "source": "ai",
            "explanation": ai_result.explanation,
            "workflow": ai_result.workflow,
            "ai_provider": ai_result.provider,
            "ai_model": ai_result.model,
            "validated": ai_result.validated,
            "validation_errors": ai_result.validation_errors,
        })

    # ── Modo hybrid ─────────────────────────────────────────
    det_result = pipeline.compile(text, lang)
    if det_result.status == "ready" and det_result.workflow:
        return jsonify({
            "status": det_result.status,
            "source": "deterministic",
            "explanation": det_result.explanation,
            "workflow": det_result.workflow,
            "missing_slots": list(det_result.missing_slots),
            "ai_provider": "none",
        })

    if ai_config.is_ai_available():
        ai_result = pipeline.ai_generate(text, lang)
        if ai_result.validated and ai_result.workflow:
            return jsonify({
                "status": "ready",
                "source": "ai_fallback",
                "explanation": ai_result.explanation,
                "workflow": ai_result.workflow,
                "ai_provider": ai_result.provider,
                "ai_model": ai_result.model,
                "validated": True,
            })

    return jsonify({
        "status": det_result.status,
        "source": "deterministic",
        "explanation": det_result.explanation or "No pude generar un workflow para tu solicitud.",
        "workflow": {},
        "missing_slots": list(det_result.missing_slots),
        "ai_provider": ai_config.active_provider.value if ai_config.is_ai_available() else "none",
    })
