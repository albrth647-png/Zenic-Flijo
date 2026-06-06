"""
Workflow Determinista — DatabaseTrigger
Detecta cambios en tablas SQLite y emite eventos correspondientes.
"""
import json
from typing import Any

from src.data.database_manager import DatabaseManager
from src.events.bus import EventBus
from src.utils.logger import setup_logging

logger = setup_logging(__name__)


class DatabaseTrigger:
    """
    Detecta cambios en tablas SQLite y emite eventos.
    
    Los triggers SQL se instalan al inicializar la base de datos
    y emiten eventos cuando se insertan, actualizan o eliminan registros.
    """

    # Mapeo de tablas a eventos
    TABLE_EVENTS: dict[str, dict[str, str]] = {
        "leads": {
            "insert": "crm.lead.created",
            "update": "crm.lead.updated",
            "delete": "crm.lead.deleted",
        },
        "invoices": {
            "insert": "invoice.created",
            "update": "invoice.updated",
            "delete": "invoice.deleted",
        },
        "products": {
            "insert": "inventory.product.created",
            "update": "inventory.product.updated",
            "delete": "inventory.product.deleted",
        },
        "workflow_executions": {
            "insert": "workflow.execution.created",
            "update": "workflow.execution.updated",
        },
    }

    def __init__(self):
        self._db = DatabaseManager()
        self._event_bus = EventBus()
        self._snapshots: dict[str, dict[int, dict]] = {}

    def install_triggers(self) -> None:
        """Instala triggers SQL en la base de datos."""
        conn = self._db.get_connection()
        cursor = conn.cursor()

        for table, events in self.TABLE_EVENTS.items():
            for action, event_name in events.items():
                trigger_name = f"trg_{table}_{action}"

                # Verificar si el trigger ya existe
                cursor.execute(
                    "SELECT name FROM sqlite_master WHERE type='trigger' AND name=?",
                    (trigger_name,),
                )
                if cursor.fetchone():
                    continue

                # Crear trigger
                if action == "insert":
                    sql = f"""
                    CREATE TRIGGER IF NOT EXISTS {trigger_name}
                    AFTER INSERT ON {table}
                    BEGIN
                        INSERT INTO event_queue (event_type, event_data, status)
                        VALUES ('{event_name}', json_object('id', NEW.id), 'pending');
                    END;
                    """
                elif action == "update":
                    sql = f"""
                    CREATE TRIGGER IF NOT EXISTS {trigger_name}
                    AFTER UPDATE ON {table}
                    BEGIN
                        INSERT INTO event_queue (event_type, event_data, status)
                        VALUES ('{event_name}', json_object('id', NEW.id), 'pending');
                    END;
                    """
                elif action == "delete":
                    sql = f"""
                    CREATE TRIGGER IF NOT EXISTS {trigger_name}
                    AFTER DELETE ON {table}
                    BEGIN
                        INSERT INTO event_queue (event_type, event_data, status)
                        VALUES ('{event_name}', json_object('id', OLD.id), 'pending');
                    END;
                    """

                cursor.execute(sql)
                logger.debug(f"Trigger SQL instalado: {trigger_name}")

        conn.commit()
        logger.info("Triggers SQL instalados correctamente")

    def poll_changes(self) -> list[dict]:
        """
        Lee eventos pendientes generados por triggers y los publica en el EventBus.
        Útil como alternativa a los triggers SQL directos.
        """
        pending = self._db.fetchall(
            "SELECT * FROM event_queue WHERE status = 'pending' ORDER BY created_at LIMIT 50"
        )

        results = []
        for event in pending:
            try:
                event_data = json.loads(event["event_data"]) if event.get("event_data") else {}
                self._event_bus.publish(event["event_type"], event_data)

                self._db.execute(
                    "UPDATE event_queue SET status = 'completed', processed_at = CURRENT_TIMESTAMP WHERE id = ?",
                    (event["id"],),
                )
                self._db.commit()
                results.append({"event_id": event["id"], "status": "processed"})

            except Exception as e:
                logger.error(f"Error procesando evento DB {event['id']}: {e}")
                self._db.execute(
                    "UPDATE event_queue SET status = 'failed' WHERE id = ?",
                    (event["id"],),
                )
                self._db.commit()
                results.append({"event_id": event["id"], "status": "failed"})

        return results
