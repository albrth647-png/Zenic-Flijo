"""
Zenic-Flijo — Tests del EventBus (Pub/Sub Puro)
=================================================

Tests para el bus de eventos simple en memoria.
Cubre: subscribe, unsubscribe, publish, handlers, sistema de eventos.
"""

from unittest.mock import MagicMock


class TestEventBus:
    """Tests para el EventBus pub/sub puro."""

    def test_publish_calls_handler(self):
        """Test: publish llama al handler suscrito."""
        from src.events.bus import EventBus

        bus = EventBus()
        handler = MagicMock()

        bus.subscribe("test.event", handler)
        bus.publish("test.event", {"key": "value"})

        handler.assert_called_once_with({"key": "value"})

    def test_publish_no_handlers(self):
        """Test: publish sin handlers no falla."""
        from src.events.bus import EventBus

        bus = EventBus()
        bus.publish("test.none", {"data": "test"})  # No debe lanzar excepción

    def test_publish_multiple_handlers(self):
        """Test: publish llama a todos los handlers suscritos al mismo evento."""
        from src.events.bus import EventBus

        bus = EventBus()
        handler1 = MagicMock()
        handler2 = MagicMock()

        bus.subscribe("test.multi", handler1)
        bus.subscribe("test.multi", handler2)
        bus.publish("test.multi", {"msg": "hello"})

        handler1.assert_called_once_with({"msg": "hello"})
        handler2.assert_called_once_with({"msg": "hello"})

    def test_unsubscribe_removes_handler(self):
        """Test: unsubscribe elimina un handler previamente registrado."""
        from src.events.bus import EventBus

        bus = EventBus()
        handler = MagicMock()

        bus.subscribe("test.unsub", handler)
        bus.unsubscribe("test.unsub", handler)
        bus.publish("test.unsub", {"test": True})

        handler.assert_not_called()

    def test_subscribe_multiple_event_types(self):
        """Test: un handler puede suscribirse a múltiples tipos de evento."""
        from src.events.bus import EventBus

        bus = EventBus()
        handler = MagicMock()

        bus.subscribe("type.a", handler)
        bus.subscribe("type.b", handler)

        bus.publish("type.a", {"from": "a"})
        bus.publish("type.b", {"from": "b"})

        assert handler.call_count == 2

    def test_handler_error_does_not_affect_others(self):
        """Test: un error en un handler no impide que otros handlers se ejecuten."""
        from src.events.bus import EventBus

        bus = EventBus()
        handler_ok = MagicMock()

        def failing_handler(data):
            raise ValueError("Error simulado")

        bus.subscribe("test.error", failing_handler)
        bus.subscribe("test.error", handler_ok)
        bus.publish("test.error", {"data": "test"})

        handler_ok.assert_called_once_with({"data": "test"})

    def test_get_system_events(self):
        """Test: get_system_events retorna la lista de eventos del sistema."""
        from src.events.bus import EventBus

        events = EventBus.get_system_events()
        assert isinstance(events, list)
        assert len(events) >= 10
        event_names = [e["event"] for e in events]
        assert "crm.lead.created" in event_names
        assert "workflow.completed" in event_names
        assert "email.received" in event_names

    def test_independent_instances(self):
        """Test: instancias separadas tienen handlers separados."""
        from src.events.bus import EventBus

        bus1 = EventBus()
        bus2 = EventBus()

        handler = MagicMock()
        bus1.subscribe("test.event", handler)

        bus1.publish("test.event", {"data": 1})
        handler.assert_called_once()

        handler.reset_mock()
        bus2.publish("test.event", {"data": 2})
        handler.assert_not_called()  # bus2 no tiene handlers
