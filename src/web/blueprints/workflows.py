"""
Blueprints — Workflows CRUD, Historial y Export/Import
"""

from flask import Blueprint, jsonify, request, session

from src.events.bus import EventBus
from src.web.helpers import _sanitize, check_free_tier, login_required, repo, require_role
from src.workflow.repository import WorkflowDefinition

bp = Blueprint("workflows", __name__)


@bp.route("/api/workflows", methods=["GET"])
@login_required
def api_list_workflows():
    status = request.args.get("status")
    workflows = repo.list_all(status)
    return jsonify([w.to_dict() for w in workflows])


@bp.route("/api/workflows", methods=["POST"])
@login_required
@require_role("editor")
@check_free_tier()
def api_create_workflow():
    data = request.get_json() or {}
    try:
        wf = WorkflowDefinition(
            name=_sanitize(data.get("name", "")),
            description=_sanitize(data.get("description", "")),
            trigger_type=data.get("trigger_type", "manual"),
            trigger_config=data.get("trigger_config", {}),
            steps=data.get("steps", []),
        )
        created = repo.create(wf, user_id=session.get("user_id"))

        event_bus = EventBus()
        if created.trigger_type == "event":
            event_config = created.trigger_config
            event_type = event_config.get("event", "")
            if event_type:
                event_bus.subscribe(event_type, created.id)
        elif created.trigger_type == "webhook":
            event_bus.subscribe("webhook.received", created.id)

        return jsonify(created.to_dict()), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@bp.route("/api/workflows/<int:wf_id>", methods=["GET"])
@login_required
def api_get_workflow(wf_id):
    wf = repo.get(wf_id)
    if not wf:
        return jsonify({"error": "Workflow no encontrado"}), 404
    return jsonify(wf.to_dict())


@bp.route("/api/workflows/<int:wf_id>", methods=["PUT"])
@login_required
@require_role("editor")
def api_update_workflow(wf_id):
    data = request.get_json() or {}
    updated = repo.update(wf_id, data)
    if not updated:
        return jsonify({"error": "Workflow no encontrado"}), 404
    return jsonify(updated.to_dict())


@bp.route("/api/workflows/<int:wf_id>", methods=["DELETE"])
@login_required
@require_role("editor")
def api_delete_workflow(wf_id):
    from src.workflow.engine import WorkflowEngine
    engine = WorkflowEngine()
    engine.pause(wf_id)
    repo.delete(wf_id)
    return jsonify({"status": "deleted"})


@bp.route("/api/workflows/<int:wf_id>/activate", methods=["POST"])
@login_required
@require_role("editor")
def api_activate_workflow(wf_id):
    from src.workflow.engine import WorkflowEngine
    engine = WorkflowEngine()
    result = engine.resume(wf_id)
    return jsonify({"status": "active" if result else "error"})


@bp.route("/api/workflows/<int:wf_id>/pause", methods=["POST"])
@login_required
@require_role("editor")
def api_pause_workflow(wf_id):
    from src.workflow.engine import WorkflowEngine
    engine = WorkflowEngine()
    result = engine.pause(wf_id)
    return jsonify({"status": "paused" if result else "error"})


@bp.route("/api/workflows/<int:wf_id>/<action>", methods=["POST"])
@login_required
@require_role("editor")
def api_workflow_action(wf_id, action):
    """Endpoint genérico para activate/pause - compatible con frontend actual."""
    from src.workflow.engine import WorkflowEngine
    engine = WorkflowEngine()

    if action == "activate":
        result = engine.resume(wf_id)
        status = "active" if result else "error"
    elif action == "pause":
        result = engine.pause(wf_id)
        status = "paused" if result else "error"
    else:
        return jsonify({"error": "Acción inválida. Use 'activate' o 'pause'"}), 400

    if status == "error":
        return jsonify({"error": f"No se pudo {action} el workflow"}), 400
    return jsonify({"status": status})


@bp.route("/api/workflows/<int:wf_id>/history", methods=["GET"])
@login_required
def api_workflow_history(wf_id):
    limit = int(request.args.get("limit", 50))
    executions = repo.list_executions(wf_id, limit)
    return jsonify([e.to_dict() for e in executions])


@bp.route("/api/workflows/<int:wf_id>/history/<int:exec_id>", methods=["GET"])
@login_required
def api_execution_detail(wf_id, exec_id):
    execution = repo.get_execution(exec_id)
    if not execution or execution.workflow_id != wf_id:
        return jsonify({"error": "Ejecución no encontrada"}), 404
    logs = repo.get_step_logs(exec_id)
    return jsonify({"execution": execution.to_dict(), "logs": logs})


@bp.route("/api/workflows/<int:wf_id>/export", methods=["GET"])
@login_required
def api_export_workflow(wf_id):
    exported = repo.export_workflow(wf_id)
    if not exported:
        return jsonify({"error": "Workflow no encontrado"}), 404
    return jsonify(exported)


@bp.route("/api/workflows/import", methods=["POST"])
@login_required
def api_import_workflow():
    data = request.get_json() or {}
    try:
        imported = repo.import_workflow(data)
        return jsonify(imported.to_dict()), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@bp.route("/api/workflows/<int:wf_id>/retry", methods=["POST"])
@login_required
@require_role("editor")
def api_retry_workflow(wf_id):
    from src.workflow.engine import WorkflowEngine
    engine = WorkflowEngine()
    try:
        result = engine.execute(wf_id)
        return jsonify(result.to_dict())
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
