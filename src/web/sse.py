"""
SSE — Server-Sent Events para tiempo real.
"""

import json
import queue
import threading
import time as _time
from datetime import datetime as _dt

from flask import Blueprint, current_app

from src.web.helpers import login_required
from src.workflow.repository import WorkflowRepository

sse_bp = Blueprint("sse", __name__, url_prefix="/api/events")

_sse_clients: list[queue.Queue] = []
_sse_lock = threading.Lock()


def _broadcast_sse(event_type: str, data: dict):
    """Envía un evento SSE a todos los clientes conectados."""
    payload = f"event: {event_type}\ndata: {json.dumps(data)}\n\n"
    with _sse_lock:
        dead = []
        for q in _sse_clients:
            try:
                q.put_nowait(payload)
            except Exception:
                dead.append(q)
        for q in dead:
            _sse_clients.remove(q)


def _patch_engine_for_sse():
    """Parchea WorkflowEngine.execute para emitir eventos SSE."""
    from src.workflow.engine import WorkflowEngine

    repo = WorkflowRepository()
    original_execute = WorkflowEngine.execute

    def patched_execute(self, workflow_id, *args, **kwargs):
        now = _dt.now()
        wf = repo.get(workflow_id)
        _broadcast_sse("execution.started", {
            "workflow_id": workflow_id,
            "name": wf.name if wf else f"Workflow #{workflow_id}",
            "timestamp": now.isoformat(),
        })

        try:
            result = original_execute(self, workflow_id, *args, **kwargs)
            duration_ms = getattr(result, 'duration_ms', 0)
            _broadcast_sse("execution.completed", {
                "workflow_id": workflow_id,
                "name": wf.name if wf else f"Workflow #{workflow_id}",
                "status": "completed",
                "duration_ms": duration_ms,
                "timestamp": now.isoformat(),
            })
            return result
        except Exception as e:
            _broadcast_sse("execution.failed", {
                "workflow_id": workflow_id,
                "name": wf.name if wf else f"Workflow #{workflow_id}",
                "status": "failed",
                "error": str(e),
                "timestamp": now.isoformat(),
            })
            raise

    WorkflowEngine.execute = patched_execute


@sse_bp.route("/stream")
@login_required
def api_events_stream():
    """SSE endpoint: emite eventos en tiempo real al dashboard.
    Eventos:
    - execution.started: cuando un workflow empieza a ejecutarse
    - execution.completed: cuando un workflow termina
    - execution.failed: cuando un workflow falla
    - stats.update: cuando las estadísticas cambian
    """
    def event_stream():
        q: queue.Queue = queue.Queue(maxsize=100)
        with _sse_lock:
            _sse_clients.append(q)
        try:
            last_heartbeat = _time.time()
            while True:
                try:
                    msg = q.get(timeout=5)
                    yield msg
                except queue.Empty:
                    if _time.time() - last_heartbeat > 25:
                        yield ": heartbeat\n\n"
                        last_heartbeat = _time.time()
                    continue
        except GeneratorExit:
            pass
        finally:
            with _sse_lock:
                if q in _sse_clients:
                    _sse_clients.remove(q)

    return current_app.response_class(
        event_stream(),
        mimetype="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )
