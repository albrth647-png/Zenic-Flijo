"""
Blueprints — Reportes (CSV/PDF)
"""

from flask import Blueprint, current_app, jsonify

from src.web.helpers import login_required

bp = Blueprint("reports", __name__)


@bp.route("/api/reports/workflows/<fmt>")
@login_required
def api_report_workflows(fmt):
    from src.web.reports import ReportGenerator
    gen = ReportGenerator()
    if fmt == "csv":
        content = gen.workflows_csv()
        mimetype = "text/csv"
    elif fmt == "pdf":
        content = gen.workflows_pdf()
        mimetype = "application/pdf"
    else:
        return jsonify({"error": "Formato no soportado. Usa csv o pdf."}), 400
    response = current_app.response_class(response=content, mimetype=mimetype)
    response.headers["Content-Disposition"] = f'attachment; filename="{gen.filename("workflows", fmt)}"'
    return response


@bp.route("/api/reports/crm/<fmt>")
@login_required
def api_report_crm(fmt):
    from src.web.reports import ReportGenerator
    gen = ReportGenerator()
    if fmt == "csv":
        content = gen.crm_leads_csv()
        mimetype = "text/csv"
    elif fmt == "pdf":
        content = gen.crm_leads_pdf()
        mimetype = "application/pdf"
    else:
        return jsonify({"error": "Formato no soportado. Usa csv o pdf."}), 400
    response = current_app.response_class(response=content, mimetype=mimetype)
    response.headers["Content-Disposition"] = f'attachment; filename="{gen.filename("crm_leads", fmt)}"'
    return response


@bp.route("/api/reports/inventory/<fmt>")
@login_required
def api_report_inventory(fmt):
    from src.web.reports import ReportGenerator
    gen = ReportGenerator()
    if fmt == "csv":
        content = gen.inventory_csv()
        mimetype = "text/csv"
    elif fmt == "pdf":
        content = gen.inventory_pdf()
        mimetype = "application/pdf"
    else:
        return jsonify({"error": "Formato no soportado. Usa csv o pdf."}), 400
    response = current_app.response_class(response=content, mimetype=mimetype)
    response.headers["Content-Disposition"] = f'attachment; filename="{gen.filename("inventory", fmt)}"'
    return response


@bp.route("/api/reports/invoices/<fmt>")
@login_required
def api_report_invoices(fmt):
    from src.web.reports import ReportGenerator
    gen = ReportGenerator()
    if fmt == "csv":
        content = gen.invoices_csv()
        mimetype = "text/csv"
    elif fmt == "pdf":
        content = gen.invoices_pdf()
        mimetype = "application/pdf"
    else:
        return jsonify({"error": "Formato no soportado. Usa csv o pdf."}), 400
    response = current_app.response_class(response=content, mimetype=mimetype)
    response.headers["Content-Disposition"] = f'attachment; filename="{gen.filename("invoices", fmt)}"'
    return response
