"""
Blueprints — Admin: Users, Dead Letter Queue y Work Queue
"""

from flask import Blueprint, jsonify, request, session

from src.data.audit_repository import AuditRepository
from src.data.user_repository import UserRepository
from src.web.helpers import login_required, require_role

users = UserRepository()
audit = AuditRepository()

bp = Blueprint("admin", __name__)


# ── API: Users Management (RBAC) ───────────────────────────

@bp.route("/api/users", methods=["GET"])
@login_required
@require_role("admin")
def api_list_users():
    user_list = users.list_users()
    return jsonify(user_list)


@bp.route("/api/users", methods=["POST"])
@login_required
@require_role("admin")
def api_create_user():
    data = request.get_json() or {}
    username = data.get("username", "")
    password = data.get("password", "")
    role = data.get("role", "editor")
    allowed_roles = {"admin", "editor", "viewer"}
    if role not in allowed_roles:
        return jsonify({"error": f"Rol inválido. Roles válidos: {', '.join(sorted(allowed_roles))}"}), 400
    if not username or len(username) < 3:
        return jsonify({"error": "Usuario debe tener al menos 3 caracteres"}), 400
    if len(password) < 6:
        return jsonify({"error": "Contraseña debe tener al menos 6 caracteres"}), 400
    existing = users.get_user_by_username(username)
    if existing:
        return jsonify({"error": "El usuario ya existe"}), 400
    new_user = users.create_user(
        username=username,
        password=password,
        role=role,
        display_name=data.get("display_name", ""),
        email=data.get("email", ""),
    )
    audit.log("user.created", f"Usuario creado: {username}", request.remote_addr, session.get("user_id"))
    return jsonify(new_user), 201


@bp.route("/api/users/<int:user_id>", methods=["PUT"])
@login_required
@require_role("admin")
def api_update_user(user_id):
    data = request.get_json() or {}
    allowed = {"role", "display_name", "email", "is_active"}
    updates = {k: v for k, v in data.items() if k in allowed}
    if not updates:
        return jsonify({"error": "Sin campos válidos para actualizar"}), 400
    users.update_user(user_id, updates)
    audit.log("user.updated", f"Usuario {user_id} actualizado", request.remote_addr, session.get("user_id"))
    return jsonify({"status": "updated"})


@bp.route("/api/users/<int:user_id>", methods=["DELETE"])
@login_required
@require_role("admin")
def api_delete_user(user_id):
    if user_id == session.get("user_id"):
        return jsonify({"error": "No puedes eliminarte a ti mismo"}), 400
    users.delete_user(user_id)
    audit.log("user.deleted", f"Usuario {user_id} desactivado", request.remote_addr, session.get("user_id"))
    return jsonify({"status": "deleted"})


# ── API: Dead Letter Queue (Sprint 4) ─────────────────────

@bp.route("/api/dead-letter", methods=["GET"])
@login_required
def api_dead_letter_list():
    from src.workflow.dead_letter import DeadLetterManager
    dl = DeadLetterManager()
    status = request.args.get("status")
    workflow_id = request.args.get("workflow_id", type=int)
    limit = int(request.args.get("limit", 50))
    offset = int(request.args.get("offset", 0))
    entries = dl.list(status=status, workflow_id=workflow_id, limit=limit, offset=offset)
    return jsonify({"entries": [e.to_dict() for e in entries], "stats": dl.get_stats()})


@bp.route("/api/dead-letter/stats", methods=["GET"])
@login_required
def api_dead_letter_stats():
    from src.workflow.dead_letter import DeadLetterManager
    dl = DeadLetterManager()
    return jsonify(dl.get_stats())


@bp.route("/api/dead-letter/<int:entry_id>/retry", methods=["POST"])
@login_required
@require_role("editor")
def api_dead_letter_retry(entry_id):
    from src.workflow.dead_letter import DeadLetterManager
    dl = DeadLetterManager()
    result = dl.retry(entry_id)
    return jsonify(result)


@bp.route("/api/dead-letter/<int:entry_id>/discard", methods=["POST"])
@login_required
@require_role("editor")
def api_dead_letter_discard(entry_id):
    from src.workflow.dead_letter import DeadLetterManager
    dl = DeadLetterManager()
    success = dl.discard(entry_id)
    return jsonify({"status": "discarded" if success else "not_found"})


@bp.route("/api/dead-letter/retry-all", methods=["POST"])
@login_required
@require_role("editor")
def api_dead_letter_retry_all():
    from src.workflow.dead_letter import DeadLetterManager
    dl = DeadLetterManager()
    results = dl.retry_all()
    return jsonify(results)


@bp.route("/api/dead-letter/discard-all", methods=["POST"])
@login_required
@require_role("editor")
def api_dead_letter_discard_all():
    from src.workflow.dead_letter import DeadLetterManager
    dl = DeadLetterManager()
    count = dl.discard_all()
    return jsonify({"discarded": count})


@bp.route("/api/dead-letter/notify/<int:entry_id>", methods=["POST"])
@login_required
@require_role("editor")
def api_dead_letter_notify(entry_id):
    from src.workflow.dead_letter import DeadLetterManager
    dl = DeadLetterManager()
    result = dl.notify_dead_letter(entry_id)
    return jsonify({"notified": result})


# ── API: Work Queue + Workers (Sprint 7-8) ─────────────────

@bp.route("/api/queue/status")
@login_required
def api_queue_status():
    from src.events.work_queue import WorkQueue
    queue = WorkQueue()
    metrics = queue.get_metrics()
    peek = queue.peek(limit=10)
    return jsonify({"metrics": metrics, "next_items": [item.to_dict() for item in peek]})


@bp.route("/api/queue/workers")
@login_required
def api_queue_workers():
    from src.events.worker_manager import WorkerManager
    mgr = WorkerManager()
    return jsonify(mgr.get_metrics())


@bp.route("/api/queue/enqueue", methods=["POST"])
@login_required
@require_role("editor")
def api_queue_enqueue():
    data = request.get_json() or {}
    workflow_id = data.get("workflow_id")
    if not workflow_id:
        return jsonify({"error": "workflow_id es requerido"}), 400
    from src.workflow.engine import WorkflowEngine
    engine = WorkflowEngine()
    try:
        result = engine.execute_async(
            workflow_id=workflow_id,
            trigger_data=data.get("trigger_data"),
            priority=data.get("priority", 0),
        )
        return jsonify(result), 202
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@bp.route("/api/queue/<int:item_id>/retry", methods=["POST"])
@login_required
@require_role("editor")
def api_queue_retry(item_id):
    from src.events.work_queue import WorkQueue
    queue = WorkQueue()
    result = queue.retry_failed(max_items=1)
    return jsonify({"retried": result})


@bp.route("/api/queue/cleanup", methods=["POST"])
@login_required
@require_role("admin")
def api_queue_cleanup():
    data = request.get_json() or {}
    max_age = int(data.get("max_age_hours", 24))
    from src.events.work_queue import WorkQueue
    queue = WorkQueue()
    deleted = queue.cleanup(max_age_hours=max_age)
    return jsonify({"deleted": deleted})
