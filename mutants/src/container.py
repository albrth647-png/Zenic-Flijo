"""
Sprint 6 (Fase 6) — IoC Container ligero.
=========================================

Resuelve BUG-ARCH-01 (singletonitis) introduciendo un patrón de registro
y resolución de dependencias que convive con los singletons existentes.

Estrategia gradual (sin breaking changes):
1. Los singletons actuales siguen funcionando como están.
2. Los servicios NUEVOS pueden registrarse en el container y resolverse
   vía type hints o por nombre.
3. Los tests pueden overridear dependencias sin tocar _instance.

Uso:
    from src.container import container

    # Registrar
    container.register("db", DatabaseManager)
    container.register_factory("event_bus", lambda: EventBus())

    # Resolver
    db = container.resolve("db")
    event_bus = container.resolve("event_bus")

    # Override para tests
    container.override("db", mock_db)
    db = container.resolve("db")  # retorna mock_db

    # Reset overrides
    container.reset_overrides()

El container es sí mismo un singleton (única instancia global), pero
actúa como punto único de configuración en lugar de tener 15+ singletons
dispersos por el código.
"""
from __future__ import annotations

import threading
from collections.abc import Callable
from typing import Any, TypeVar

T = TypeVar("T")


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class ContainerError(Exception):
    """Error del IoC container."""
mutants_xǁContainerǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁContainerǁregister__mutmut: MutantDict = {}  # type: ignore
mutants_xǁContainerǁregister_factory__mutmut: MutantDict = {}  # type: ignore
mutants_xǁContainerǁregister_instance__mutmut: MutantDict = {}  # type: ignore
mutants_xǁContainerǁresolve__mutmut: MutantDict = {}  # type: ignore
mutants_xǁContainerǁhas__mutmut: MutantDict = {}  # type: ignore
mutants_xǁContainerǁlist_registered__mutmut: MutantDict = {}  # type: ignore
mutants_xǁContainerǁoverride__mutmut: MutantDict = {}  # type: ignore
mutants_xǁContainerǁget_info__mutmut: MutantDict = {}  # type: ignore


class Container:
    """
    IoC container thread-safe con soporte para:
    - Registro por clase (singleton lazy)
    - Registro por factory (función que retorna la instancia)
    - Registro por instancia (ya construida)
    - Overrides para tests
    - Scopes (pendiente para v2.1)
    """

    @_mutmut_mutated(mutants_xǁContainerǁ__init____mutmut)
    def __init__(self) -> None:
        self._lock = threading.RLock()
        self._factories: dict[str, Callable[[], Any]] = {}
        self._instances: dict[str, Any] = {}
        self._overrides: dict[str, Any] = {}
        self._singletons: set[str] = set()

    def xǁContainerǁ__init____mutmut_orig(self) -> None:
        self._lock = threading.RLock()
        self._factories: dict[str, Callable[[], Any]] = {}
        self._instances: dict[str, Any] = {}
        self._overrides: dict[str, Any] = {}
        self._singletons: set[str] = set()

    def xǁContainerǁ__init____mutmut_1(self) -> None:
        self._lock = None
        self._factories: dict[str, Callable[[], Any]] = {}
        self._instances: dict[str, Any] = {}
        self._overrides: dict[str, Any] = {}
        self._singletons: set[str] = set()

    def xǁContainerǁ__init____mutmut_2(self) -> None:
        self._lock = threading.RLock()
        self._factories: dict[str, Callable[[], Any]] = None
        self._instances: dict[str, Any] = {}
        self._overrides: dict[str, Any] = {}
        self._singletons: set[str] = set()

    def xǁContainerǁ__init____mutmut_3(self) -> None:
        self._lock = threading.RLock()
        self._factories: dict[str, Callable[[], Any]] = {}
        self._instances: dict[str, Any] = None
        self._overrides: dict[str, Any] = {}
        self._singletons: set[str] = set()

    def xǁContainerǁ__init____mutmut_4(self) -> None:
        self._lock = threading.RLock()
        self._factories: dict[str, Callable[[], Any]] = {}
        self._instances: dict[str, Any] = {}
        self._overrides: dict[str, Any] = None
        self._singletons: set[str] = set()

    def xǁContainerǁ__init____mutmut_5(self) -> None:
        self._lock = threading.RLock()
        self._factories: dict[str, Callable[[], Any]] = {}
        self._instances: dict[str, Any] = {}
        self._overrides: dict[str, Any] = {}
        self._singletons: set[str] = None

    # ── Registro ──────────────────────────────────────────────

    @_mutmut_mutated(mutants_xǁContainerǁregister__mutmut)
    def register(
        self,
        name: str,
        factory: Callable[[], Any] | type,
        singleton: bool = True,
    ) -> None:
        """
        Registra una dependencia.

        Args:
            name: Nombre único de la dependencia.
            factory: Función factory o clase a instanciar.
            singleton: Si True, la instancia se cachea tras la primera resolución.
        """
        with self._lock:
            if isinstance(factory, type):
                # Si es una clase, crear factory que instancia
                cls = factory
                self._factories[name] = cls
            else:
                self._factories[name] = factory

            if singleton:
                self._singletons.add(name)

            # Invalidar instancia cacheada si se re-registra
            self._instances.pop(name, None)

    # ── Registro ──────────────────────────────────────────────

    def xǁContainerǁregister__mutmut_orig(
        self,
        name: str,
        factory: Callable[[], Any] | type,
        singleton: bool = True,
    ) -> None:
        """
        Registra una dependencia.

        Args:
            name: Nombre único de la dependencia.
            factory: Función factory o clase a instanciar.
            singleton: Si True, la instancia se cachea tras la primera resolución.
        """
        with self._lock:
            if isinstance(factory, type):
                # Si es una clase, crear factory que instancia
                cls = factory
                self._factories[name] = cls
            else:
                self._factories[name] = factory

            if singleton:
                self._singletons.add(name)

            # Invalidar instancia cacheada si se re-registra
            self._instances.pop(name, None)

    # ── Registro ──────────────────────────────────────────────

    def xǁContainerǁregister__mutmut_1(
        self,
        name: str,
        factory: Callable[[], Any] | type,
        singleton: bool = False,
    ) -> None:
        """
        Registra una dependencia.

        Args:
            name: Nombre único de la dependencia.
            factory: Función factory o clase a instanciar.
            singleton: Si True, la instancia se cachea tras la primera resolución.
        """
        with self._lock:
            if isinstance(factory, type):
                # Si es una clase, crear factory que instancia
                cls = factory
                self._factories[name] = cls
            else:
                self._factories[name] = factory

            if singleton:
                self._singletons.add(name)

            # Invalidar instancia cacheada si se re-registra
            self._instances.pop(name, None)

    # ── Registro ──────────────────────────────────────────────

    def xǁContainerǁregister__mutmut_2(
        self,
        name: str,
        factory: Callable[[], Any] | type,
        singleton: bool = True,
    ) -> None:
        """
        Registra una dependencia.

        Args:
            name: Nombre único de la dependencia.
            factory: Función factory o clase a instanciar.
            singleton: Si True, la instancia se cachea tras la primera resolución.
        """
        with self._lock:
            if isinstance(factory, type):
                # Si es una clase, crear factory que instancia
                cls = None
                self._factories[name] = cls
            else:
                self._factories[name] = factory

            if singleton:
                self._singletons.add(name)

            # Invalidar instancia cacheada si se re-registra
            self._instances.pop(name, None)

    # ── Registro ──────────────────────────────────────────────

    def xǁContainerǁregister__mutmut_3(
        self,
        name: str,
        factory: Callable[[], Any] | type,
        singleton: bool = True,
    ) -> None:
        """
        Registra una dependencia.

        Args:
            name: Nombre único de la dependencia.
            factory: Función factory o clase a instanciar.
            singleton: Si True, la instancia se cachea tras la primera resolución.
        """
        with self._lock:
            if isinstance(factory, type):
                # Si es una clase, crear factory que instancia
                cls = factory
                self._factories[name] = None
            else:
                self._factories[name] = factory

            if singleton:
                self._singletons.add(name)

            # Invalidar instancia cacheada si se re-registra
            self._instances.pop(name, None)

    # ── Registro ──────────────────────────────────────────────

    def xǁContainerǁregister__mutmut_4(
        self,
        name: str,
        factory: Callable[[], Any] | type,
        singleton: bool = True,
    ) -> None:
        """
        Registra una dependencia.

        Args:
            name: Nombre único de la dependencia.
            factory: Función factory o clase a instanciar.
            singleton: Si True, la instancia se cachea tras la primera resolución.
        """
        with self._lock:
            if isinstance(factory, type):
                # Si es una clase, crear factory que instancia
                cls = factory
                self._factories[name] = cls
            else:
                self._factories[name] = None

            if singleton:
                self._singletons.add(name)

            # Invalidar instancia cacheada si se re-registra
            self._instances.pop(name, None)

    # ── Registro ──────────────────────────────────────────────

    def xǁContainerǁregister__mutmut_5(
        self,
        name: str,
        factory: Callable[[], Any] | type,
        singleton: bool = True,
    ) -> None:
        """
        Registra una dependencia.

        Args:
            name: Nombre único de la dependencia.
            factory: Función factory o clase a instanciar.
            singleton: Si True, la instancia se cachea tras la primera resolución.
        """
        with self._lock:
            if isinstance(factory, type):
                # Si es una clase, crear factory que instancia
                cls = factory
                self._factories[name] = cls
            else:
                self._factories[name] = factory

            if singleton:
                self._singletons.add(None)

            # Invalidar instancia cacheada si se re-registra
            self._instances.pop(name, None)

    # ── Registro ──────────────────────────────────────────────

    def xǁContainerǁregister__mutmut_6(
        self,
        name: str,
        factory: Callable[[], Any] | type,
        singleton: bool = True,
    ) -> None:
        """
        Registra una dependencia.

        Args:
            name: Nombre único de la dependencia.
            factory: Función factory o clase a instanciar.
            singleton: Si True, la instancia se cachea tras la primera resolución.
        """
        with self._lock:
            if isinstance(factory, type):
                # Si es una clase, crear factory que instancia
                cls = factory
                self._factories[name] = cls
            else:
                self._factories[name] = factory

            if singleton:
                self._singletons.add(name)

            # Invalidar instancia cacheada si se re-registra
            self._instances.pop(None, None)

    # ── Registro ──────────────────────────────────────────────

    def xǁContainerǁregister__mutmut_7(
        self,
        name: str,
        factory: Callable[[], Any] | type,
        singleton: bool = True,
    ) -> None:
        """
        Registra una dependencia.

        Args:
            name: Nombre único de la dependencia.
            factory: Función factory o clase a instanciar.
            singleton: Si True, la instancia se cachea tras la primera resolución.
        """
        with self._lock:
            if isinstance(factory, type):
                # Si es una clase, crear factory que instancia
                cls = factory
                self._factories[name] = cls
            else:
                self._factories[name] = factory

            if singleton:
                self._singletons.add(name)

            # Invalidar instancia cacheada si se re-registra
            self._instances.pop(None)

    # ── Registro ──────────────────────────────────────────────

    def xǁContainerǁregister__mutmut_8(
        self,
        name: str,
        factory: Callable[[], Any] | type,
        singleton: bool = True,
    ) -> None:
        """
        Registra una dependencia.

        Args:
            name: Nombre único de la dependencia.
            factory: Función factory o clase a instanciar.
            singleton: Si True, la instancia se cachea tras la primera resolución.
        """
        with self._lock:
            if isinstance(factory, type):
                # Si es una clase, crear factory que instancia
                cls = factory
                self._factories[name] = cls
            else:
                self._factories[name] = factory

            if singleton:
                self._singletons.add(name)

            # Invalidar instancia cacheada si se re-registra
            self._instances.pop(name, )

    @_mutmut_mutated(mutants_xǁContainerǁregister_factory__mutmut)
    def register_factory(self, name: str, factory: Callable[[], Any]) -> None:
        """Alias para register con factory function."""
        self.register(name, factory, singleton=True)

    def xǁContainerǁregister_factory__mutmut_orig(self, name: str, factory: Callable[[], Any]) -> None:
        """Alias para register con factory function."""
        self.register(name, factory, singleton=True)

    def xǁContainerǁregister_factory__mutmut_1(self, name: str, factory: Callable[[], Any]) -> None:
        """Alias para register con factory function."""
        self.register(None, factory, singleton=True)

    def xǁContainerǁregister_factory__mutmut_2(self, name: str, factory: Callable[[], Any]) -> None:
        """Alias para register con factory function."""
        self.register(name, None, singleton=True)

    def xǁContainerǁregister_factory__mutmut_3(self, name: str, factory: Callable[[], Any]) -> None:
        """Alias para register con factory function."""
        self.register(name, factory, singleton=None)

    def xǁContainerǁregister_factory__mutmut_4(self, name: str, factory: Callable[[], Any]) -> None:
        """Alias para register con factory function."""
        self.register(factory, singleton=True)

    def xǁContainerǁregister_factory__mutmut_5(self, name: str, factory: Callable[[], Any]) -> None:
        """Alias para register con factory function."""
        self.register(name, singleton=True)

    def xǁContainerǁregister_factory__mutmut_6(self, name: str, factory: Callable[[], Any]) -> None:
        """Alias para register con factory function."""
        self.register(name, factory, )

    def xǁContainerǁregister_factory__mutmut_7(self, name: str, factory: Callable[[], Any]) -> None:
        """Alias para register con factory function."""
        self.register(name, factory, singleton=False)

    @_mutmut_mutated(mutants_xǁContainerǁregister_instance__mutmut)
    def register_instance(self, name: str, instance: Any) -> None:
        """Registra una instancia ya construida (singleton inmediato)."""
        with self._lock:
            self._instances[name] = instance
            self._singletons.add(name)
            # No necesita factory porque la instancia ya está construida

    def xǁContainerǁregister_instance__mutmut_orig(self, name: str, instance: Any) -> None:
        """Registra una instancia ya construida (singleton inmediato)."""
        with self._lock:
            self._instances[name] = instance
            self._singletons.add(name)
            # No necesita factory porque la instancia ya está construida

    def xǁContainerǁregister_instance__mutmut_1(self, name: str, instance: Any) -> None:
        """Registra una instancia ya construida (singleton inmediato)."""
        with self._lock:
            self._instances[name] = None
            self._singletons.add(name)
            # No necesita factory porque la instancia ya está construida

    def xǁContainerǁregister_instance__mutmut_2(self, name: str, instance: Any) -> None:
        """Registra una instancia ya construida (singleton inmediato)."""
        with self._lock:
            self._instances[name] = instance
            self._singletons.add(None)
            # No necesita factory porque la instancia ya está construida

    # ── Resolución ────────────────────────────────────────────

    @_mutmut_mutated(mutants_xǁContainerǁresolve__mutmut)
    def resolve(self, name: str) -> Any:
        """
        Resuelve una dependencia por nombre.
        Lanza ContainerError si no está registrada.
        """
        with self._lock:
            # 1. Override tiene prioridad (para tests)
            if name in self._overrides:
                return self._overrides[name]

            # 2. Instancia cacheada (singleton)
            if name in self._instances:
                return self._instances[name]

            # 3. Factory
            if name not in self._factories:
                raise ContainerError(
                    f"Dependencia no registrada: {name!r}. "
                    f"Disponibles: {list(self._factories.keys())}"
                )

            factory = self._factories[name]
            instance = factory()

            # Cachear si es singleton
            if name in self._singletons:
                self._instances[name] = instance

            return instance

    # ── Resolución ────────────────────────────────────────────

    def xǁContainerǁresolve__mutmut_orig(self, name: str) -> Any:
        """
        Resuelve una dependencia por nombre.
        Lanza ContainerError si no está registrada.
        """
        with self._lock:
            # 1. Override tiene prioridad (para tests)
            if name in self._overrides:
                return self._overrides[name]

            # 2. Instancia cacheada (singleton)
            if name in self._instances:
                return self._instances[name]

            # 3. Factory
            if name not in self._factories:
                raise ContainerError(
                    f"Dependencia no registrada: {name!r}. "
                    f"Disponibles: {list(self._factories.keys())}"
                )

            factory = self._factories[name]
            instance = factory()

            # Cachear si es singleton
            if name in self._singletons:
                self._instances[name] = instance

            return instance

    # ── Resolución ────────────────────────────────────────────

    def xǁContainerǁresolve__mutmut_1(self, name: str) -> Any:
        """
        Resuelve una dependencia por nombre.
        Lanza ContainerError si no está registrada.
        """
        with self._lock:
            # 1. Override tiene prioridad (para tests)
            if name not in self._overrides:
                return self._overrides[name]

            # 2. Instancia cacheada (singleton)
            if name in self._instances:
                return self._instances[name]

            # 3. Factory
            if name not in self._factories:
                raise ContainerError(
                    f"Dependencia no registrada: {name!r}. "
                    f"Disponibles: {list(self._factories.keys())}"
                )

            factory = self._factories[name]
            instance = factory()

            # Cachear si es singleton
            if name in self._singletons:
                self._instances[name] = instance

            return instance

    # ── Resolución ────────────────────────────────────────────

    def xǁContainerǁresolve__mutmut_2(self, name: str) -> Any:
        """
        Resuelve una dependencia por nombre.
        Lanza ContainerError si no está registrada.
        """
        with self._lock:
            # 1. Override tiene prioridad (para tests)
            if name in self._overrides:
                return self._overrides[name]

            # 2. Instancia cacheada (singleton)
            if name not in self._instances:
                return self._instances[name]

            # 3. Factory
            if name not in self._factories:
                raise ContainerError(
                    f"Dependencia no registrada: {name!r}. "
                    f"Disponibles: {list(self._factories.keys())}"
                )

            factory = self._factories[name]
            instance = factory()

            # Cachear si es singleton
            if name in self._singletons:
                self._instances[name] = instance

            return instance

    # ── Resolución ────────────────────────────────────────────

    def xǁContainerǁresolve__mutmut_3(self, name: str) -> Any:
        """
        Resuelve una dependencia por nombre.
        Lanza ContainerError si no está registrada.
        """
        with self._lock:
            # 1. Override tiene prioridad (para tests)
            if name in self._overrides:
                return self._overrides[name]

            # 2. Instancia cacheada (singleton)
            if name in self._instances:
                return self._instances[name]

            # 3. Factory
            if name in self._factories:
                raise ContainerError(
                    f"Dependencia no registrada: {name!r}. "
                    f"Disponibles: {list(self._factories.keys())}"
                )

            factory = self._factories[name]
            instance = factory()

            # Cachear si es singleton
            if name in self._singletons:
                self._instances[name] = instance

            return instance

    # ── Resolución ────────────────────────────────────────────

    def xǁContainerǁresolve__mutmut_4(self, name: str) -> Any:
        """
        Resuelve una dependencia por nombre.
        Lanza ContainerError si no está registrada.
        """
        with self._lock:
            # 1. Override tiene prioridad (para tests)
            if name in self._overrides:
                return self._overrides[name]

            # 2. Instancia cacheada (singleton)
            if name in self._instances:
                return self._instances[name]

            # 3. Factory
            if name not in self._factories:
                raise ContainerError(
                    None
                )

            factory = self._factories[name]
            instance = factory()

            # Cachear si es singleton
            if name in self._singletons:
                self._instances[name] = instance

            return instance

    # ── Resolución ────────────────────────────────────────────

    def xǁContainerǁresolve__mutmut_5(self, name: str) -> Any:
        """
        Resuelve una dependencia por nombre.
        Lanza ContainerError si no está registrada.
        """
        with self._lock:
            # 1. Override tiene prioridad (para tests)
            if name in self._overrides:
                return self._overrides[name]

            # 2. Instancia cacheada (singleton)
            if name in self._instances:
                return self._instances[name]

            # 3. Factory
            if name not in self._factories:
                raise ContainerError(
                    f"Dependencia no registrada: {name!r}. "
                    f"Disponibles: {list(None)}"
                )

            factory = self._factories[name]
            instance = factory()

            # Cachear si es singleton
            if name in self._singletons:
                self._instances[name] = instance

            return instance

    # ── Resolución ────────────────────────────────────────────

    def xǁContainerǁresolve__mutmut_6(self, name: str) -> Any:
        """
        Resuelve una dependencia por nombre.
        Lanza ContainerError si no está registrada.
        """
        with self._lock:
            # 1. Override tiene prioridad (para tests)
            if name in self._overrides:
                return self._overrides[name]

            # 2. Instancia cacheada (singleton)
            if name in self._instances:
                return self._instances[name]

            # 3. Factory
            if name not in self._factories:
                raise ContainerError(
                    f"Dependencia no registrada: {name!r}. "
                    f"Disponibles: {list(self._factories.keys())}"
                )

            factory = None
            instance = factory()

            # Cachear si es singleton
            if name in self._singletons:
                self._instances[name] = instance

            return instance

    # ── Resolución ────────────────────────────────────────────

    def xǁContainerǁresolve__mutmut_7(self, name: str) -> Any:
        """
        Resuelve una dependencia por nombre.
        Lanza ContainerError si no está registrada.
        """
        with self._lock:
            # 1. Override tiene prioridad (para tests)
            if name in self._overrides:
                return self._overrides[name]

            # 2. Instancia cacheada (singleton)
            if name in self._instances:
                return self._instances[name]

            # 3. Factory
            if name not in self._factories:
                raise ContainerError(
                    f"Dependencia no registrada: {name!r}. "
                    f"Disponibles: {list(self._factories.keys())}"
                )

            factory = self._factories[name]
            instance = None

            # Cachear si es singleton
            if name in self._singletons:
                self._instances[name] = instance

            return instance

    # ── Resolución ────────────────────────────────────────────

    def xǁContainerǁresolve__mutmut_8(self, name: str) -> Any:
        """
        Resuelve una dependencia por nombre.
        Lanza ContainerError si no está registrada.
        """
        with self._lock:
            # 1. Override tiene prioridad (para tests)
            if name in self._overrides:
                return self._overrides[name]

            # 2. Instancia cacheada (singleton)
            if name in self._instances:
                return self._instances[name]

            # 3. Factory
            if name not in self._factories:
                raise ContainerError(
                    f"Dependencia no registrada: {name!r}. "
                    f"Disponibles: {list(self._factories.keys())}"
                )

            factory = self._factories[name]
            instance = factory()

            # Cachear si es singleton
            if name not in self._singletons:
                self._instances[name] = instance

            return instance

    # ── Resolución ────────────────────────────────────────────

    def xǁContainerǁresolve__mutmut_9(self, name: str) -> Any:
        """
        Resuelve una dependencia por nombre.
        Lanza ContainerError si no está registrada.
        """
        with self._lock:
            # 1. Override tiene prioridad (para tests)
            if name in self._overrides:
                return self._overrides[name]

            # 2. Instancia cacheada (singleton)
            if name in self._instances:
                return self._instances[name]

            # 3. Factory
            if name not in self._factories:
                raise ContainerError(
                    f"Dependencia no registrada: {name!r}. "
                    f"Disponibles: {list(self._factories.keys())}"
                )

            factory = self._factories[name]
            instance = factory()

            # Cachear si es singleton
            if name in self._singletons:
                self._instances[name] = None

            return instance

    @_mutmut_mutated(mutants_xǁContainerǁhas__mutmut)
    def has(self, name: str) -> bool:
        """True si la dependencia está registrada."""
        with self._lock:
            return name in self._factories or name in self._instances

    def xǁContainerǁhas__mutmut_orig(self, name: str) -> bool:
        """True si la dependencia está registrada."""
        with self._lock:
            return name in self._factories or name in self._instances

    def xǁContainerǁhas__mutmut_1(self, name: str) -> bool:
        """True si la dependencia está registrada."""
        with self._lock:
            return name in self._factories and name in self._instances

    def xǁContainerǁhas__mutmut_2(self, name: str) -> bool:
        """True si la dependencia está registrada."""
        with self._lock:
            return name not in self._factories or name in self._instances

    def xǁContainerǁhas__mutmut_3(self, name: str) -> bool:
        """True si la dependencia está registrada."""
        with self._lock:
            return name in self._factories or name not in self._instances

    @_mutmut_mutated(mutants_xǁContainerǁlist_registered__mutmut)
    def list_registered(self) -> list[str]:
        """Lista todas las dependencias registradas."""
        with self._lock:
            names = set(self._factories.keys()) | set(self._instances.keys())
            return sorted(names)

    def xǁContainerǁlist_registered__mutmut_orig(self) -> list[str]:
        """Lista todas las dependencias registradas."""
        with self._lock:
            names = set(self._factories.keys()) | set(self._instances.keys())
            return sorted(names)

    def xǁContainerǁlist_registered__mutmut_1(self) -> list[str]:
        """Lista todas las dependencias registradas."""
        with self._lock:
            names = None
            return sorted(names)

    def xǁContainerǁlist_registered__mutmut_2(self) -> list[str]:
        """Lista todas las dependencias registradas."""
        with self._lock:
            names = set(self._factories.keys()) & set(self._instances.keys())
            return sorted(names)

    def xǁContainerǁlist_registered__mutmut_3(self) -> list[str]:
        """Lista todas las dependencias registradas."""
        with self._lock:
            names = set(None) | set(self._instances.keys())
            return sorted(names)

    def xǁContainerǁlist_registered__mutmut_4(self) -> list[str]:
        """Lista todas las dependencias registradas."""
        with self._lock:
            names = set(self._factories.keys()) | set(None)
            return sorted(names)

    def xǁContainerǁlist_registered__mutmut_5(self) -> list[str]:
        """Lista todas las dependencias registradas."""
        with self._lock:
            names = set(self._factories.keys()) | set(self._instances.keys())
            return sorted(None)

    # ── Overrides para tests ──────────────────────────────────

    @_mutmut_mutated(mutants_xǁContainerǁoverride__mutmut)
    def override(self, name: str, instance: Any) -> None:
        """
        Reemplaza una dependencia con un mock/stub para tests.
        El override tiene prioridad sobre la instancia cacheada.
        """
        with self._lock:
            self._overrides[name] = instance

    # ── Overrides para tests ──────────────────────────────────

    def xǁContainerǁoverride__mutmut_orig(self, name: str, instance: Any) -> None:
        """
        Reemplaza una dependencia con un mock/stub para tests.
        El override tiene prioridad sobre la instancia cacheada.
        """
        with self._lock:
            self._overrides[name] = instance

    # ── Overrides para tests ──────────────────────────────────

    def xǁContainerǁoverride__mutmut_1(self, name: str, instance: Any) -> None:
        """
        Reemplaza una dependencia con un mock/stub para tests.
        El override tiene prioridad sobre la instancia cacheada.
        """
        with self._lock:
            self._overrides[name] = None

    def reset_overrides(self) -> None:
        """Elimina todos los overrides (restaura comportamiento normal)."""
        with self._lock:
            self._overrides.clear()

    # ── Limpieza ──────────────────────────────────────────────

    def clear(self) -> None:
        """Elimina todos los registros (útil para reset entre tests)."""
        with self._lock:
            self._factories.clear()
            self._instances.clear()
            self._overrides.clear()
            self._singletons.clear()

    def clear_instances(self) -> None:
        """Solo limpia instancias cacheadas (mantiene factories). Útil para
        forzar re-construcción de singletons."""
        with self._lock:
            self._instances.clear()

    # ── Introspección ─────────────────────────────────────────

    @_mutmut_mutated(mutants_xǁContainerǁget_info__mutmut)
    def get_info(self) -> dict[str, Any]:
        """Retorna info del container para debugging."""
        with self._lock:
            return {
                "registered": self.list_registered(),
                "singletons": sorted(self._singletons),
                "cached_instances": sorted(self._instances.keys()),
                "overrides": sorted(self._overrides.keys()),
            }

    # ── Introspección ─────────────────────────────────────────

    def xǁContainerǁget_info__mutmut_orig(self) -> dict[str, Any]:
        """Retorna info del container para debugging."""
        with self._lock:
            return {
                "registered": self.list_registered(),
                "singletons": sorted(self._singletons),
                "cached_instances": sorted(self._instances.keys()),
                "overrides": sorted(self._overrides.keys()),
            }

    # ── Introspección ─────────────────────────────────────────

    def xǁContainerǁget_info__mutmut_1(self) -> dict[str, Any]:
        """Retorna info del container para debugging."""
        with self._lock:
            return {
                "XXregisteredXX": self.list_registered(),
                "singletons": sorted(self._singletons),
                "cached_instances": sorted(self._instances.keys()),
                "overrides": sorted(self._overrides.keys()),
            }

    # ── Introspección ─────────────────────────────────────────

    def xǁContainerǁget_info__mutmut_2(self) -> dict[str, Any]:
        """Retorna info del container para debugging."""
        with self._lock:
            return {
                "REGISTERED": self.list_registered(),
                "singletons": sorted(self._singletons),
                "cached_instances": sorted(self._instances.keys()),
                "overrides": sorted(self._overrides.keys()),
            }

    # ── Introspección ─────────────────────────────────────────

    def xǁContainerǁget_info__mutmut_3(self) -> dict[str, Any]:
        """Retorna info del container para debugging."""
        with self._lock:
            return {
                "registered": self.list_registered(),
                "XXsingletonsXX": sorted(self._singletons),
                "cached_instances": sorted(self._instances.keys()),
                "overrides": sorted(self._overrides.keys()),
            }

    # ── Introspección ─────────────────────────────────────────

    def xǁContainerǁget_info__mutmut_4(self) -> dict[str, Any]:
        """Retorna info del container para debugging."""
        with self._lock:
            return {
                "registered": self.list_registered(),
                "SINGLETONS": sorted(self._singletons),
                "cached_instances": sorted(self._instances.keys()),
                "overrides": sorted(self._overrides.keys()),
            }

    # ── Introspección ─────────────────────────────────────────

    def xǁContainerǁget_info__mutmut_5(self) -> dict[str, Any]:
        """Retorna info del container para debugging."""
        with self._lock:
            return {
                "registered": self.list_registered(),
                "singletons": sorted(None),
                "cached_instances": sorted(self._instances.keys()),
                "overrides": sorted(self._overrides.keys()),
            }

    # ── Introspección ─────────────────────────────────────────

    def xǁContainerǁget_info__mutmut_6(self) -> dict[str, Any]:
        """Retorna info del container para debugging."""
        with self._lock:
            return {
                "registered": self.list_registered(),
                "singletons": sorted(self._singletons),
                "XXcached_instancesXX": sorted(self._instances.keys()),
                "overrides": sorted(self._overrides.keys()),
            }

    # ── Introspección ─────────────────────────────────────────

    def xǁContainerǁget_info__mutmut_7(self) -> dict[str, Any]:
        """Retorna info del container para debugging."""
        with self._lock:
            return {
                "registered": self.list_registered(),
                "singletons": sorted(self._singletons),
                "CACHED_INSTANCES": sorted(self._instances.keys()),
                "overrides": sorted(self._overrides.keys()),
            }

    # ── Introspección ─────────────────────────────────────────

    def xǁContainerǁget_info__mutmut_8(self) -> dict[str, Any]:
        """Retorna info del container para debugging."""
        with self._lock:
            return {
                "registered": self.list_registered(),
                "singletons": sorted(self._singletons),
                "cached_instances": sorted(None),
                "overrides": sorted(self._overrides.keys()),
            }

    # ── Introspección ─────────────────────────────────────────

    def xǁContainerǁget_info__mutmut_9(self) -> dict[str, Any]:
        """Retorna info del container para debugging."""
        with self._lock:
            return {
                "registered": self.list_registered(),
                "singletons": sorted(self._singletons),
                "cached_instances": sorted(self._instances.keys()),
                "XXoverridesXX": sorted(self._overrides.keys()),
            }

    # ── Introspección ─────────────────────────────────────────

    def xǁContainerǁget_info__mutmut_10(self) -> dict[str, Any]:
        """Retorna info del container para debugging."""
        with self._lock:
            return {
                "registered": self.list_registered(),
                "singletons": sorted(self._singletons),
                "cached_instances": sorted(self._instances.keys()),
                "OVERRIDES": sorted(self._overrides.keys()),
            }

    # ── Introspección ─────────────────────────────────────────

    def xǁContainerǁget_info__mutmut_11(self) -> dict[str, Any]:
        """Retorna info del container para debugging."""
        with self._lock:
            return {
                "registered": self.list_registered(),
                "singletons": sorted(self._singletons),
                "cached_instances": sorted(self._instances.keys()),
                "overrides": sorted(None),
            }

mutants_xǁContainerǁ__init____mutmut['_mutmut_orig'] = Container.xǁContainerǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁContainerǁ__init____mutmut['xǁContainerǁ__init____mutmut_1'] = Container.xǁContainerǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁContainerǁ__init____mutmut['xǁContainerǁ__init____mutmut_2'] = Container.xǁContainerǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁContainerǁ__init____mutmut['xǁContainerǁ__init____mutmut_3'] = Container.xǁContainerǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁContainerǁ__init____mutmut['xǁContainerǁ__init____mutmut_4'] = Container.xǁContainerǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁContainerǁ__init____mutmut['xǁContainerǁ__init____mutmut_5'] = Container.xǁContainerǁ__init____mutmut_5 # type: ignore # mutmut generated

mutants_xǁContainerǁregister__mutmut['_mutmut_orig'] = Container.xǁContainerǁregister__mutmut_orig # type: ignore # mutmut generated
mutants_xǁContainerǁregister__mutmut['xǁContainerǁregister__mutmut_1'] = Container.xǁContainerǁregister__mutmut_1 # type: ignore # mutmut generated
mutants_xǁContainerǁregister__mutmut['xǁContainerǁregister__mutmut_2'] = Container.xǁContainerǁregister__mutmut_2 # type: ignore # mutmut generated
mutants_xǁContainerǁregister__mutmut['xǁContainerǁregister__mutmut_3'] = Container.xǁContainerǁregister__mutmut_3 # type: ignore # mutmut generated
mutants_xǁContainerǁregister__mutmut['xǁContainerǁregister__mutmut_4'] = Container.xǁContainerǁregister__mutmut_4 # type: ignore # mutmut generated
mutants_xǁContainerǁregister__mutmut['xǁContainerǁregister__mutmut_5'] = Container.xǁContainerǁregister__mutmut_5 # type: ignore # mutmut generated
mutants_xǁContainerǁregister__mutmut['xǁContainerǁregister__mutmut_6'] = Container.xǁContainerǁregister__mutmut_6 # type: ignore # mutmut generated
mutants_xǁContainerǁregister__mutmut['xǁContainerǁregister__mutmut_7'] = Container.xǁContainerǁregister__mutmut_7 # type: ignore # mutmut generated
mutants_xǁContainerǁregister__mutmut['xǁContainerǁregister__mutmut_8'] = Container.xǁContainerǁregister__mutmut_8 # type: ignore # mutmut generated

mutants_xǁContainerǁregister_factory__mutmut['_mutmut_orig'] = Container.xǁContainerǁregister_factory__mutmut_orig # type: ignore # mutmut generated
mutants_xǁContainerǁregister_factory__mutmut['xǁContainerǁregister_factory__mutmut_1'] = Container.xǁContainerǁregister_factory__mutmut_1 # type: ignore # mutmut generated
mutants_xǁContainerǁregister_factory__mutmut['xǁContainerǁregister_factory__mutmut_2'] = Container.xǁContainerǁregister_factory__mutmut_2 # type: ignore # mutmut generated
mutants_xǁContainerǁregister_factory__mutmut['xǁContainerǁregister_factory__mutmut_3'] = Container.xǁContainerǁregister_factory__mutmut_3 # type: ignore # mutmut generated
mutants_xǁContainerǁregister_factory__mutmut['xǁContainerǁregister_factory__mutmut_4'] = Container.xǁContainerǁregister_factory__mutmut_4 # type: ignore # mutmut generated
mutants_xǁContainerǁregister_factory__mutmut['xǁContainerǁregister_factory__mutmut_5'] = Container.xǁContainerǁregister_factory__mutmut_5 # type: ignore # mutmut generated
mutants_xǁContainerǁregister_factory__mutmut['xǁContainerǁregister_factory__mutmut_6'] = Container.xǁContainerǁregister_factory__mutmut_6 # type: ignore # mutmut generated
mutants_xǁContainerǁregister_factory__mutmut['xǁContainerǁregister_factory__mutmut_7'] = Container.xǁContainerǁregister_factory__mutmut_7 # type: ignore # mutmut generated

mutants_xǁContainerǁregister_instance__mutmut['_mutmut_orig'] = Container.xǁContainerǁregister_instance__mutmut_orig # type: ignore # mutmut generated
mutants_xǁContainerǁregister_instance__mutmut['xǁContainerǁregister_instance__mutmut_1'] = Container.xǁContainerǁregister_instance__mutmut_1 # type: ignore # mutmut generated
mutants_xǁContainerǁregister_instance__mutmut['xǁContainerǁregister_instance__mutmut_2'] = Container.xǁContainerǁregister_instance__mutmut_2 # type: ignore # mutmut generated

mutants_xǁContainerǁresolve__mutmut['_mutmut_orig'] = Container.xǁContainerǁresolve__mutmut_orig # type: ignore # mutmut generated
mutants_xǁContainerǁresolve__mutmut['xǁContainerǁresolve__mutmut_1'] = Container.xǁContainerǁresolve__mutmut_1 # type: ignore # mutmut generated
mutants_xǁContainerǁresolve__mutmut['xǁContainerǁresolve__mutmut_2'] = Container.xǁContainerǁresolve__mutmut_2 # type: ignore # mutmut generated
mutants_xǁContainerǁresolve__mutmut['xǁContainerǁresolve__mutmut_3'] = Container.xǁContainerǁresolve__mutmut_3 # type: ignore # mutmut generated
mutants_xǁContainerǁresolve__mutmut['xǁContainerǁresolve__mutmut_4'] = Container.xǁContainerǁresolve__mutmut_4 # type: ignore # mutmut generated
mutants_xǁContainerǁresolve__mutmut['xǁContainerǁresolve__mutmut_5'] = Container.xǁContainerǁresolve__mutmut_5 # type: ignore # mutmut generated
mutants_xǁContainerǁresolve__mutmut['xǁContainerǁresolve__mutmut_6'] = Container.xǁContainerǁresolve__mutmut_6 # type: ignore # mutmut generated
mutants_xǁContainerǁresolve__mutmut['xǁContainerǁresolve__mutmut_7'] = Container.xǁContainerǁresolve__mutmut_7 # type: ignore # mutmut generated
mutants_xǁContainerǁresolve__mutmut['xǁContainerǁresolve__mutmut_8'] = Container.xǁContainerǁresolve__mutmut_8 # type: ignore # mutmut generated
mutants_xǁContainerǁresolve__mutmut['xǁContainerǁresolve__mutmut_9'] = Container.xǁContainerǁresolve__mutmut_9 # type: ignore # mutmut generated

mutants_xǁContainerǁhas__mutmut['_mutmut_orig'] = Container.xǁContainerǁhas__mutmut_orig # type: ignore # mutmut generated
mutants_xǁContainerǁhas__mutmut['xǁContainerǁhas__mutmut_1'] = Container.xǁContainerǁhas__mutmut_1 # type: ignore # mutmut generated
mutants_xǁContainerǁhas__mutmut['xǁContainerǁhas__mutmut_2'] = Container.xǁContainerǁhas__mutmut_2 # type: ignore # mutmut generated
mutants_xǁContainerǁhas__mutmut['xǁContainerǁhas__mutmut_3'] = Container.xǁContainerǁhas__mutmut_3 # type: ignore # mutmut generated

mutants_xǁContainerǁlist_registered__mutmut['_mutmut_orig'] = Container.xǁContainerǁlist_registered__mutmut_orig # type: ignore # mutmut generated
mutants_xǁContainerǁlist_registered__mutmut['xǁContainerǁlist_registered__mutmut_1'] = Container.xǁContainerǁlist_registered__mutmut_1 # type: ignore # mutmut generated
mutants_xǁContainerǁlist_registered__mutmut['xǁContainerǁlist_registered__mutmut_2'] = Container.xǁContainerǁlist_registered__mutmut_2 # type: ignore # mutmut generated
mutants_xǁContainerǁlist_registered__mutmut['xǁContainerǁlist_registered__mutmut_3'] = Container.xǁContainerǁlist_registered__mutmut_3 # type: ignore # mutmut generated
mutants_xǁContainerǁlist_registered__mutmut['xǁContainerǁlist_registered__mutmut_4'] = Container.xǁContainerǁlist_registered__mutmut_4 # type: ignore # mutmut generated
mutants_xǁContainerǁlist_registered__mutmut['xǁContainerǁlist_registered__mutmut_5'] = Container.xǁContainerǁlist_registered__mutmut_5 # type: ignore # mutmut generated

mutants_xǁContainerǁoverride__mutmut['_mutmut_orig'] = Container.xǁContainerǁoverride__mutmut_orig # type: ignore # mutmut generated
mutants_xǁContainerǁoverride__mutmut['xǁContainerǁoverride__mutmut_1'] = Container.xǁContainerǁoverride__mutmut_1 # type: ignore # mutmut generated

mutants_xǁContainerǁget_info__mutmut['_mutmut_orig'] = Container.xǁContainerǁget_info__mutmut_orig # type: ignore # mutmut generated
mutants_xǁContainerǁget_info__mutmut['xǁContainerǁget_info__mutmut_1'] = Container.xǁContainerǁget_info__mutmut_1 # type: ignore # mutmut generated
mutants_xǁContainerǁget_info__mutmut['xǁContainerǁget_info__mutmut_2'] = Container.xǁContainerǁget_info__mutmut_2 # type: ignore # mutmut generated
mutants_xǁContainerǁget_info__mutmut['xǁContainerǁget_info__mutmut_3'] = Container.xǁContainerǁget_info__mutmut_3 # type: ignore # mutmut generated
mutants_xǁContainerǁget_info__mutmut['xǁContainerǁget_info__mutmut_4'] = Container.xǁContainerǁget_info__mutmut_4 # type: ignore # mutmut generated
mutants_xǁContainerǁget_info__mutmut['xǁContainerǁget_info__mutmut_5'] = Container.xǁContainerǁget_info__mutmut_5 # type: ignore # mutmut generated
mutants_xǁContainerǁget_info__mutmut['xǁContainerǁget_info__mutmut_6'] = Container.xǁContainerǁget_info__mutmut_6 # type: ignore # mutmut generated
mutants_xǁContainerǁget_info__mutmut['xǁContainerǁget_info__mutmut_7'] = Container.xǁContainerǁget_info__mutmut_7 # type: ignore # mutmut generated
mutants_xǁContainerǁget_info__mutmut['xǁContainerǁget_info__mutmut_8'] = Container.xǁContainerǁget_info__mutmut_8 # type: ignore # mutmut generated
mutants_xǁContainerǁget_info__mutmut['xǁContainerǁget_info__mutmut_9'] = Container.xǁContainerǁget_info__mutmut_9 # type: ignore # mutmut generated
mutants_xǁContainerǁget_info__mutmut['xǁContainerǁget_info__mutmut_10'] = Container.xǁContainerǁget_info__mutmut_10 # type: ignore # mutmut generated
mutants_xǁContainerǁget_info__mutmut['xǁContainerǁget_info__mutmut_11'] = Container.xǁContainerǁget_info__mutmut_11 # type: ignore # mutmut generated


# ─── Instancia global (singleton del container) ─────────────────────────

container = Container()
"""Container global único. Importar y usar directamente."""
mutants_x_setup_default_container__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_setup_default_container__mutmut)
def setup_default_container() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_orig() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_1() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has(None):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_2() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("XXdbXX"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_3() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("DB"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_4() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register(None, lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_5() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", None)

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_6() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register(lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_7() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", )

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_8() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("XXdbXX", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_9() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("DB", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_10() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: None)

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_11() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register(None, lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_12() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", None)

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_13() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register(lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_14() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", )

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_15() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("XXredisXX", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_16() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("REDIS", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_17() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: None)

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_18() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register(None, lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_19() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", None)

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_20() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register(lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_21() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", )

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_22() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("XXevent_busXX", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_23() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("EVENT_BUS", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_24() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: None)

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_25() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register(None, lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_26() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", None)

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_27() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register(lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_28() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", )

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_29() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("XXworkflow_engineXX", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_30() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("WORKFLOW_ENGINE", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_31() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: None)

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_32() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register(None, lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_33() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", None)

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_34() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register(lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_35() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", )

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_36() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("XXworkflow_repositoryXX", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_37() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("WORKFLOW_REPOSITORY", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_38() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: None)

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_39() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register(None, lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_40() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", None)
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_41() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register(lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_42() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", )
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_43() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("XXversion_repositoryXX", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_44() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("VERSION_REPOSITORY", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_45() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: None)
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_46() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register(None, lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_47() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", None)
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_48() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register(lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_49() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", )
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_50() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("XXenvironment_serviceXX", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_51() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("ENVIRONMENT_SERVICE", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_52() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: None)
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_53() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register(None, lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_54() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", None)

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_55() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register(lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_56() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", )

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_57() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("XXpromotion_serviceXX", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_58() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("PROMOTION_SERVICE", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_59() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: None)

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_60() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register(None, lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_61() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", None)

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_62() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register(lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_63() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", )

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_64() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("XXalert_serviceXX", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_65() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("ALERT_SERVICE", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_66() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: None)

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: RBACManager())


def x_setup_default_container__mutmut_67() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register(None, lambda: RBACManager())


def x_setup_default_container__mutmut_68() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", None)


def x_setup_default_container__mutmut_69() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register(lambda: RBACManager())


def x_setup_default_container__mutmut_70() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", )


def x_setup_default_container__mutmut_71() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("XXrbac_managerXX", lambda: RBACManager())


def x_setup_default_container__mutmut_72() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("RBAC_MANAGER", lambda: RBACManager())


def x_setup_default_container__mutmut_73() -> None:
    """
    Registra las dependencias por defecto del proyecto en el container global.
    Es idempotente: si ya están registradas, no hace nada.

    Esta función debe llamarse al inicio de main.py (junto con el resto de
    inicialización del sistema). Los servicios siguen siendo singletons
    internamente, pero ahora son accesibles vía container.resolve().
    """
    if container.has("db"):
        return  # Ya inicializado

    # ── Data layer ────────────────────────────────────────────
    from src.core.db import DatabaseManager

    container.register("db", lambda: DatabaseManager())

    from src.core.db import RedisService

    container.register("redis", lambda: RedisService())

    # ── Events ────────────────────────────────────────────────
    from src.events.bus import EventBus

    container.register("event_bus", lambda: EventBus())

    # ── Workflow ──────────────────────────────────────────────
    from src.workflow.engine import WorkflowEngine

    container.register("workflow_engine", lambda: WorkflowEngine())

    from src.workflow.repository import WorkflowRepository

    container.register("workflow_repository", lambda: WorkflowRepository())

    # ── Versioning (Sprint 9) ─────────────────────────────────
    from src.workflow.versioning import (
        EnvironmentService,
        PromotionService,
        WorkflowVersionRepository,
    )

    container.register("version_repository", lambda: WorkflowVersionRepository())
    container.register("environment_service", lambda: EnvironmentService())
    container.register("promotion_service", lambda: PromotionService())

    # ── Observability (Sprint 11) ─────────────────────────────
    from src.core.observability.alerts import AlertService

    container.register("alert_service", lambda: AlertService())

    # ── Security ──────────────────────────────────────────────
    from src.core.security.rbac import RBACManager

    container.register("rbac_manager", lambda: None)

mutants_x_setup_default_container__mutmut['_mutmut_orig'] = x_setup_default_container__mutmut_orig # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_1'] = x_setup_default_container__mutmut_1 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_2'] = x_setup_default_container__mutmut_2 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_3'] = x_setup_default_container__mutmut_3 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_4'] = x_setup_default_container__mutmut_4 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_5'] = x_setup_default_container__mutmut_5 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_6'] = x_setup_default_container__mutmut_6 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_7'] = x_setup_default_container__mutmut_7 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_8'] = x_setup_default_container__mutmut_8 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_9'] = x_setup_default_container__mutmut_9 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_10'] = x_setup_default_container__mutmut_10 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_11'] = x_setup_default_container__mutmut_11 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_12'] = x_setup_default_container__mutmut_12 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_13'] = x_setup_default_container__mutmut_13 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_14'] = x_setup_default_container__mutmut_14 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_15'] = x_setup_default_container__mutmut_15 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_16'] = x_setup_default_container__mutmut_16 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_17'] = x_setup_default_container__mutmut_17 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_18'] = x_setup_default_container__mutmut_18 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_19'] = x_setup_default_container__mutmut_19 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_20'] = x_setup_default_container__mutmut_20 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_21'] = x_setup_default_container__mutmut_21 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_22'] = x_setup_default_container__mutmut_22 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_23'] = x_setup_default_container__mutmut_23 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_24'] = x_setup_default_container__mutmut_24 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_25'] = x_setup_default_container__mutmut_25 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_26'] = x_setup_default_container__mutmut_26 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_27'] = x_setup_default_container__mutmut_27 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_28'] = x_setup_default_container__mutmut_28 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_29'] = x_setup_default_container__mutmut_29 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_30'] = x_setup_default_container__mutmut_30 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_31'] = x_setup_default_container__mutmut_31 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_32'] = x_setup_default_container__mutmut_32 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_33'] = x_setup_default_container__mutmut_33 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_34'] = x_setup_default_container__mutmut_34 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_35'] = x_setup_default_container__mutmut_35 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_36'] = x_setup_default_container__mutmut_36 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_37'] = x_setup_default_container__mutmut_37 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_38'] = x_setup_default_container__mutmut_38 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_39'] = x_setup_default_container__mutmut_39 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_40'] = x_setup_default_container__mutmut_40 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_41'] = x_setup_default_container__mutmut_41 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_42'] = x_setup_default_container__mutmut_42 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_43'] = x_setup_default_container__mutmut_43 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_44'] = x_setup_default_container__mutmut_44 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_45'] = x_setup_default_container__mutmut_45 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_46'] = x_setup_default_container__mutmut_46 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_47'] = x_setup_default_container__mutmut_47 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_48'] = x_setup_default_container__mutmut_48 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_49'] = x_setup_default_container__mutmut_49 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_50'] = x_setup_default_container__mutmut_50 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_51'] = x_setup_default_container__mutmut_51 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_52'] = x_setup_default_container__mutmut_52 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_53'] = x_setup_default_container__mutmut_53 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_54'] = x_setup_default_container__mutmut_54 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_55'] = x_setup_default_container__mutmut_55 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_56'] = x_setup_default_container__mutmut_56 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_57'] = x_setup_default_container__mutmut_57 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_58'] = x_setup_default_container__mutmut_58 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_59'] = x_setup_default_container__mutmut_59 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_60'] = x_setup_default_container__mutmut_60 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_61'] = x_setup_default_container__mutmut_61 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_62'] = x_setup_default_container__mutmut_62 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_63'] = x_setup_default_container__mutmut_63 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_64'] = x_setup_default_container__mutmut_64 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_65'] = x_setup_default_container__mutmut_65 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_66'] = x_setup_default_container__mutmut_66 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_67'] = x_setup_default_container__mutmut_67 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_68'] = x_setup_default_container__mutmut_68 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_69'] = x_setup_default_container__mutmut_69 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_70'] = x_setup_default_container__mutmut_70 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_71'] = x_setup_default_container__mutmut_71 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_72'] = x_setup_default_container__mutmut_72 # type: ignore # mutmut generated
mutants_x_setup_default_container__mutmut['x_setup_default_container__mutmut_73'] = x_setup_default_container__mutmut_73 # type: ignore # mutmut generated
