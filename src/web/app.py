"""
Workflow Determinista — Web App (Flask)
Servidor web con todas las rutas de la API REST.
"""
import json
import os
from functools import wraps
from pathlib import Path

from flask import (
    Flask, render_template, request, jsonify, session,
    redirect, url_for, send_from_directory,
)

from src.config import WEB_HOST, WEB_PORT, SESSION_SECRET, SESSION_EXPIRY_HOURS, LOGIN_MAX_ATTEMPTS, LOGIN_WINDOW_MINUTES
from src.data.database_manager import DatabaseManager
from src.utils.logger import setup_logging
from src.license.validator import LicenseValidator
from src.workflow.repository import WorkflowRepository, WorkflowDefinition
from src.events.bus import EventBus

logger = setup_logging(__name__)

# ── Helpers ────────────────────────────────────────────────

db = DatabaseManager()
repo = WorkflowRepository()
event_bus = EventBus()

# Rate limiting state
_login_attempts: dict[str, list[float]] = {}


def _check_rate_limit(ip: str) -> bool:
    """Verifica rate limiting: 10 intentos cada 15 minutos por IP."""
    import time
    now = time.time()
    window = LOGIN_WINDOW_MINUTES * 60
    if ip not in _login_attempts:
        _login_attempts[ip] = []
    _login_attempts[ip] = [t for t in _login_attempts[ip] if now - t < window]
    if len(_login_attempts[ip]) >= LOGIN_MAX_ATTEMPTS:
        return False
    _login_attempts[ip].append(now)
    return True


def login_required(f):
    """Decorador: requiere sesión iniciada."""
    @wraps(f)
    def decorated(*args, **kwargs):
        if "user" not in session:
            return redirect(url_for("login_page"))
        return f(*args, **kwargs)
    return decorated


def check_trial():
    """Verifica si el trial ha expirado."""
    validator = LicenseValidator()
    status = validator.get_trial_status()
    return status["status"] == "expired" and status.get("is_trial", False)


def create_app() -> Flask:
    """Crea y configura la aplicación Flask."""
    app = Flask(
        __name__,
        template_folder=str(Path(__file__).parent / "templates"),
        static_folder=str(Path(__file__).parent / "static"),
    )
    app.secret_key = SESSION_SECRET
    app.config["SESSION_COOKIE_HTTPONLY"] = True
    app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
    app.config["PERMANENT_SESSION_LIFETIME"] = SESSION_EXPIRY_HOURS * 3600

    # ── Rutas de páginas ──────────────────────────────────

    @app.route("/")
    @login_required
    def index():
        return redirect(url_for("dashboard_page"))

    @app.route("/login")
    def login_page():
        if "user" in session:
            return redirect(url_for("dashboard_page"))
        trial = LicenseValidator().get_trial_status()
        return render_template("login.html", trial=trial)

    @app.route("/dashboard")
    @login_required
    def dashboard_page():
        if check_trial():
            return render_template("login.html", trial={"status": "expired"})
        return render_template("dashboard.html")

    @app.route("/chat")
    @login_required
    def chat_page():
        if check_trial():
            return render_template("login.html", trial={"status": "expired"})
        return render_template("chat.html")

    @app.route("/editor")
    @login_required
    def editor_page():
        if check_trial():
            return render_template("login.html", trial={"status": "expired"})
        return render_template("editor.html")

    @app.route("/workflows")
    @login_required
    def workflow_list_page():
        if check_trial():
            return render_template("login.html", trial={"status": "expired"})
        return render_template("workflow_list.html")

    @app.route("/workflows/<int:workflow_id>")
    @login_required
    def workflow_detail_page(workflow_id):
        if check_trial():
            return render_template("login.html", trial={"status": "expired"})
        return render_template("workflow_detail.html", workflow_id=workflow_id)

    @app.route("/settings")
    @login_required
    def settings_page():
        if check_trial():
            return render_template("login.html", trial={"status": "expired"})
        return render_template("settings.html")

    # ── API: Auth ──────────────────────────────────────────

    @app.route("/api/auth/login", methods=["POST"])
    def api_login():
        ip = request.remote_addr or "unknown"
        if not _check_rate_limit(ip):
            return jsonify({"error": "Demasiados intentos. Espera 15 minutos."}), 429
        data = request.get_json() or {}
        username = data.get("username", "")
        password = data.get("password", "")

        import bcrypt
        stored_hash = db.get_setting("admin_password_hash")
        if not stored_hash:
            return jsonify({"error": "No hay usuario configurado"}), 401

        if isinstance(stored_hash, str):
            try:
                valid = bcrypt.checkpw(password.encode(), stored_hash.encode())
            except Exception:
                valid = False
        else:
            valid = False

        if not valid:
            ip = request.remote_addr or "unknown"
            db.audit("login.failed", f"Intento fallido para {username}", ip)
            return jsonify({"error": "Credenciales inválidas"}), 401

        session["user"] = username
        session.permanent = True
        db.audit("login.success", f"Login exitoso: {username}", request.remote_addr)
        return jsonify({"status": "ok", "user": username})

    @app.route("/api/auth/logout", methods=["POST"])
    def api_logout():
        session.pop("user", None)
        return jsonify({"status": "ok"})

    @app.route("/api/auth/status")
    def api_auth_status():
        return jsonify({"authenticated": "user" in session})

    # ── API: Dashboard ─────────────────────────────────────

    @app.route("/api/dashboard/stats")
    @login_required
    def api_dashboard_stats():
        stats = repo.get_stats()
        trial = LicenseValidator().get_trial_status()
        return jsonify({"stats": stats, "trial": trial})

    # ── API: Workflows ─────────────────────────────────────

    @app.route("/api/workflows", methods=["GET"])
    @login_required
    def api_list_workflows():
        status = request.args.get("status")
        workflows = repo.list_all(status)
        return jsonify([w.to_dict() for w in workflows])

    @app.route("/api/workflows", methods=["POST"])
    @login_required
    def api_create_workflow():
        data = request.get_json() or {}
        try:
            wf = WorkflowDefinition(
                name=data.get("name", ""),
                description=data.get("description", ""),
                trigger_type=data.get("trigger_type", "manual"),
                trigger_config=data.get("trigger_config", {}),
                steps=data.get("steps", []),
            )
            created = repo.create(wf)

            # Suscribir a eventos si es necesario
            if created.trigger_type == "event":
                event_config = created.trigger_config
                event_type = event_config.get("event", "")
                if event_type:
                    event_bus.subscribe(event_type, created.id)

            return jsonify(created.to_dict()), 201
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    @app.route("/api/workflows/<int:wf_id>", methods=["GET"])
    @login_required
    def api_get_workflow(wf_id):
        wf = repo.get(wf_id)
        if not wf:
            return jsonify({"error": "Workflow no encontrado"}), 404
        return jsonify(wf.to_dict())

    @app.route("/api/workflows/<int:wf_id>", methods=["PUT"])
    @login_required
    def api_update_workflow(wf_id):
        data = request.get_json() or {}
        updated = repo.update(wf_id, data)
        if not updated:
            return jsonify({"error": "Workflow no encontrado"}), 404
        return jsonify(updated.to_dict())

    @app.route("/api/workflows/<int:wf_id>", methods=["DELETE"])
    @login_required
    def api_delete_workflow(wf_id):
        from src.workflow.engine import WorkflowEngine
        engine = WorkflowEngine()
        engine.pause(wf_id)
        repo.delete(wf_id)
        return jsonify({"status": "deleted"})

    @app.route("/api/workflows/<int:wf_id>/activate", methods=["POST"])
    @login_required
    def api_activate_workflow(wf_id):
        from src.workflow.engine import WorkflowEngine
        engine = WorkflowEngine()
        result = engine.resume(wf_id)
        return jsonify({"status": "active" if result else "error"})

    @app.route("/api/workflows/<int:wf_id>/pause", methods=["POST"])
    @login_required
    def api_pause_workflow(wf_id):
        from src.workflow.engine import WorkflowEngine
        engine = WorkflowEngine()
        result = engine.pause(wf_id)
        return jsonify({"status": "paused" if result else "error"})

    @app.route("/api/workflows/<int:wf_id>/history", methods=["GET"])
    @login_required
    def api_workflow_history(wf_id):
        limit = int(request.args.get("limit", 50))
        executions = repo.list_executions(wf_id, limit)
        return jsonify([e.to_dict() for e in executions])

    @app.route("/api/workflows/<int:wf_id>/history/<int:exec_id>", methods=["GET"])
    @login_required
    def api_execution_detail(wf_id, exec_id):
        execution = repo.get_execution(exec_id)
        if not execution or execution.workflow_id != wf_id:
            return jsonify({"error": "Ejecución no encontrada"}), 404
        logs = repo.get_step_logs(exec_id)
        return jsonify({"execution": execution.to_dict(), "logs": logs})

    @app.route("/api/workflows/<int:wf_id>/retry", methods=["POST"])
    @login_required
    def api_retry_workflow(wf_id):
        from src.workflow.engine import WorkflowEngine
        engine = WorkflowEngine()
        try:
            result = engine.execute(wf_id)
            return jsonify(result.to_dict())
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    # ── API: NLP Chat ───────────────────────────────────────

    @app.route("/api/workflows/chat", methods=["POST"])
    @login_required
    def api_chat():
        data = request.get_json() or {}
        text = data.get("text", "")

        from src.nlp.intent_classifier import IntentClassifier
        classifier = IntentClassifier()
        intents = classifier.classify(text)

        if not intents:
            return jsonify({"suggestions": [], "message": "No entendí tu solicitud. Intenta describir qué quieres automatizar."})

        return jsonify({
            "suggestions": intents,
            "message": f"Encontré {len(intents)} sugerencias para tu solicitud.",
        })

    # ── API: Tools ──────────────────────────────────────────

    @app.route("/api/tools/crm/leads", methods=["GET"])
    @login_required
    def api_list_leads():
        from src.tools.crm.service import CRMService
        crm = CRMService()
        stage = request.args.get("stage")
        leads = crm.list_leads(stage)
        return jsonify(leads)

    @app.route("/api/tools/crm/leads", methods=["POST"])
    @login_required
    def api_create_lead():
        from src.tools.crm.service import CRMService
        crm = CRMService()
        data = request.get_json() or {}
        lead = crm.create_lead(
            name=data.get("name", ""),
            email=data.get("email"),
            phone=data.get("phone"),
            company=data.get("company"),
            source=data.get("source", "web_form"),
            notes=data.get("notes"),
        )
        return jsonify(lead), 201

    @app.route("/api/tools/inventory/products", methods=["GET"])
    @login_required
    def api_list_products():
        from src.tools.inventory.service import InventoryService
        inv = InventoryService()
        low_stock = request.args.get("low_stock", "false").lower() == "true"
        products = inv.list_products(low_stock_only=low_stock)
        return jsonify(products)

    @app.route("/api/tools/inventory/low-stock", methods=["GET"])
    @login_required
    def api_low_stock():
        from src.tools.inventory.service import InventoryService
        inv = InventoryService()
        return jsonify(inv.get_low_stock_products())

    @app.route("/api/tools/invoice/list", methods=["GET"])
    @login_required
    def api_list_invoices():
        from src.tools.invoice.service import InvoiceService
        inv = InvoiceService()
        status = request.args.get("status")
        invoices = inv.list_invoices(status)
        return jsonify(invoices)

    # ── API: Settings ───────────────────────────────────────

    @app.route("/api/settings", methods=["GET"])
    @login_required
    def api_get_settings():
        return jsonify({
            "smtp_server": db.get_setting("smtp_server", ""),
            "smtp_port": db.get_setting("smtp_port", "587"),
            "email_user": db.get_setting("email_user", ""),
            "webhook_api_key": db.get_setting("webhook_api_key", ""),
        })

    @app.route("/api/settings", methods=["PUT"])
    @login_required
    def api_update_settings():
        data = request.get_json() or {}
        for key in ["smtp_server", "smtp_port", "email_user", "email_password",
                     "webhook_api_key", "imap_server", "imap_port"]:
            if key in data:
                db.set_setting(key, str(data[key]))
        return jsonify({"status": "saved"})

    @app.route("/api/settings/change-password", methods=["POST"])
    @login_required
    def api_change_password():
        import bcrypt
        data = request.get_json() or {}
        current = data.get("current_password", "")
        new_pass = data.get("new_password", "")

        stored_hash = db.get_setting("admin_password_hash")
        if stored_hash:
            if isinstance(stored_hash, str):
                try:
                    if not bcrypt.checkpw(current.encode(), stored_hash.encode()):
                        return jsonify({"error": "Contraseña actual incorrecta"}), 400
                except Exception:
                    return jsonify({"error": "Error verificando contraseña"}), 400

        if len(new_pass) < 6:
            return jsonify({"error": "La nueva contraseña debe tener al menos 6 caracteres"}), 400

        new_hash = bcrypt.hashpw(new_pass.encode(), bcrypt.gensalt(rounds=12)).decode()
        db.set_setting("admin_password_hash", new_hash)
        db.audit("password.changed", "Contraseña cambiada", request.remote_addr)
        return jsonify({"status": "ok"})

    @app.route("/api/settings/test-email", methods=["POST"])
    @login_required
    def api_test_email():
        from src.tools.notification.service import NotificationService
        ns = NotificationService()
        result = ns.test_connection()
        return jsonify(result)

    # ── API: License ────────────────────────────────────────

    @app.route("/api/license/validate", methods=["POST"])
    def api_validate_license():
        data = request.get_json() or {}
        key = data.get("key", "")
        validator = LicenseValidator()
        result = validator.validate(key)
        if result["valid"]:
            validator.activate_key(key, result.get("type", "individual"),
                                    result.get("client_name", ""))
        return jsonify(result)

    @app.route("/api/license/info")
    def api_license_info():
        validator = LicenseValidator()
        return jsonify(validator.get_license_info())

    # ── API: System ─────────────────────────────────────────

    @app.route("/api/system/backup", methods=["POST"])
    @login_required
    def api_system_backup():
        from src.data.backup_engine import BackupEngine
        be = BackupEngine()
        path = be.backup_now()
        return jsonify({"path": path, "status": "completed"})

    @app.route("/api/system/status")
    def api_system_status():
        return jsonify({
            "version": "1.0.0",
            "status": "running",
            "db_path": str(db._db_path),
        })

    return app
