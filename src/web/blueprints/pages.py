"""
Blueprints — Páginas (rutas de templates HTML)
"""

from flask import Blueprint, redirect, render_template, session, url_for

from src.license.validator import LicenseValidator
from src.web.helpers import check_trial, login_required

bp = Blueprint("pages", __name__)


@bp.route("/")
@login_required
def index():
    return redirect(url_for("pages.dashboard_page"))


@bp.route("/login")
def login_page():
    if "user" in session:
        return redirect(url_for("pages.dashboard_page"))
    trial = LicenseValidator().get_trial_status()
    return render_template("login.html", trial=trial)


@bp.route("/dashboard")
@login_required
def dashboard_page():
    if check_trial():
        return render_template("login.html", trial={"status": "expired"})
    return render_template("dashboard.html")


@bp.route("/chat")
@login_required
def chat_page():
    if check_trial():
        return render_template("login.html", trial={"status": "expired"})
    return render_template("chat.html")


@bp.route("/editor")
@login_required
def editor_page():
    if check_trial():
        return render_template("login.html", trial={"status": "expired"})
    return render_template("editor.html")


@bp.route("/workflows")
@login_required
def workflow_list_page():
    if check_trial():
        return render_template("login.html", trial={"status": "expired"})
    return render_template("workflow_list.html")


@bp.route("/workflows/<int:workflow_id>")
@login_required
def workflow_detail_page(workflow_id):
    if check_trial():
        return render_template("login.html", trial={"status": "expired"})
    return render_template("workflow_detail.html", workflow_id=workflow_id)


@bp.route("/settings")
@login_required
def settings_page():
    if check_trial():
        return render_template("login.html", trial={"status": "expired"})
    return render_template("settings.html")


@bp.route("/dead-letter")
@login_required
def dead_letter_page():
    if check_trial():
        return render_template("login.html", trial={"status": "expired"})
    return render_template("dead_letter.html")


@bp.route("/compliance")
@login_required
def compliance_page():
    if check_trial():
        return render_template("login.html", trial={"status": "expired"})
    return render_template("compliance.html")


@bp.route("/airgap")
@login_required
def airgap_page():
    if check_trial():
        return render_template("login.html", trial={"status": "expired"})
    return render_template("airgap.html")


@bp.route("/partners")
@login_required
def partners_page():
    if check_trial():
        return render_template("login.html", trial={"status": "expired"})
    return render_template("partners.html")


@bp.route("/orbital")
@login_required
def orbital_page():
    if check_trial():
        return render_template("login.html", trial={"status": "expired"})
    return render_template("orbital.html")
