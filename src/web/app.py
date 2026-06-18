"""
Workflow Determinista — Web App (Flask)
Fábrica de aplicación que registra todos los blueprints.
"""

from pathlib import Path

from flask import Flask, jsonify

from src.config import SESSION_COOKIE_SECURE, SESSION_EXPIRY_HOURS, SESSION_SECRET
from src.utils.logger import setup_logging
from src.web.blueprints import register_blueprints
from src.web.helpers import (
    _check_rate_limit,
    _login_attempts,
    _register_failed_login,
    _sanitize,
    check_free_tier,
    check_trial,
    login_required,
    require_role,
)

logger = setup_logging(__name__)

# Re-export shared state and helpers for backward compatibility.
# Fix Sprint 3 bug #26: tests preexistentes (test_security_fase3, test_security_redteam)
# asumían que _sanitize, _check_rate_limit y _login_attempts estaban en app.py,
# pero viven en helpers.py. Re-exportar mantiene compatibilidad sin duplicar lógica.
__all__ = [
    "_sanitize",
    "_check_rate_limit",
    "_register_failed_login",
    "_login_attempts",
    "login_required",
    "require_role",
    "check_trial",
    "check_free_tier",
    "create_app",
]


def create_app() -> Flask:
    """Crea y configura la aplicación Flask registrando todos los blueprints."""
    app = Flask(
        __name__,
        template_folder=str(Path(__file__).parent / "templates"),
        static_folder=str(Path(__file__).parent / "static"),
    )
    app.secret_key = SESSION_SECRET
    app.config["SESSION_COOKIE_SECURE"] = SESSION_COOKIE_SECURE
    app.config["SESSION_COOKIE_HTTPONLY"] = True
    app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
    app.config["PERMANENT_SESSION_LIFETIME"] = SESSION_EXPIRY_HOURS * 3600

    # Registrar todos los blueprints
    register_blueprints(app)

    # ── SPA: React frontend ──────────────────────────────────

    @app.route("/app/<path:path>")
    @app.route("/app")
    def spa_serve(path="index.html"):
        spa_path = Path(__file__).parent / "static" / "spa" / "index.html"
        if spa_path.exists():
            return app.send_static_file("spa/index.html")
        return jsonify({"error": "SPA not built yet. Run: cd frontend && npm run build"}), 503

    return app
