"""
Workflow Determinista — Data Layer
==================================

Modulos de persistencia y servicios de datos:
- DatabaseManager: Singleton SQLite (core: conexion, transacciones, schema)
- UserRepository: CRUD de usuarios
- SettingsRepository: Gestion de settings clave-valor
- AuditRepository: Registro de auditoria
- MongoDBService: Singleton async MongoDB (Motor)
- MongoRepository: Clase base generica para repositorios MongoDB
- RedisService: Singleton sync Redis
- BackupEngine: Backups automaticos
"""

from src.data.audit_repository import AuditRepository
from src.data.backup_engine import BackupEngine
from src.data.database_manager import DatabaseManager
from src.data.mongodb_repository import MongoRepository
from src.data.mongodb_service import MongoDBService
from src.data.redis_service import RedisService
from src.data.settings_repository import SettingsRepository
from src.data.user_repository import UserRepository

__all__ = [
    "AuditRepository",
    "BackupEngine",
    "DatabaseManager",
    "MongoDBService",
    "MongoRepository",
    "RedisService",
    "SettingsRepository",
    "UserRepository",
]
