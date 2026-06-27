"""
Zenic CLI — Comando: info
Muestra informacion detallada de un conector.
"""

from __future__ import annotations

import argparse
from contextlib import suppress


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_cmd_info__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_cmd_info__mutmut)
def cmd_info(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_orig(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_1(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = None
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_2(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = None

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_3(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() != 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_4(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 1:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_5(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(None):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_6(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover(None)
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_7(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("XXsrc.connectorsXX")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_8(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("SRC.CONNECTORS")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_9(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(None):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_10(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover(None)

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_11(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("XXsrc.tools.integrationsXX")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_12(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("SRC.TOOLS.INTEGRATIONS")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_13(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = None
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_14(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(None)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_15(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = None

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_16(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(None)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_17(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None and connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_18(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is not None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_19(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is not None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_20(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(None)
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_21(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print(None)
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_22(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("XXConectores disponibles:XX")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_23(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_24(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("CONECTORES DISPONIBLES:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_25(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(None)
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_26(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 2

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_27(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print(None)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_28(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" / 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_29(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("XX=XX" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_30(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 61)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_31(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(None)
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_32(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print(None)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_33(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" / 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_34(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("XX=XX" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_35(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 61)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_36(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print(None)
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_37(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("XX  Metadata:XX")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_38(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_39(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  METADATA:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_40(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(None)
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_41(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get(None, connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_42(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', None)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_43(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get(connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_44(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', )}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_45(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('XXnameXX', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_46(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('NAME', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_47(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(None)
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_48(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get(None, 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_49(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', None)}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_50(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_51(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', )}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_52(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('XXversionXX', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_53(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('VERSION', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_54(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'XXN/AXX')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_55(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'n/a')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_56(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(None)
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_57(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get(None, 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_58(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', None)}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_59(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_60(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', )}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_61(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('XXdescriptionXX', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_62(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('DESCRIPTION', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_63(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'XXSin descripcionXX')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_64(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_65(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'SIN DESCRIPCION')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_66(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(None)
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_67(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get(None, 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_68(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', None)}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_69(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_70(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', )}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_71(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('XXcategoryXX', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_72(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('CATEGORY', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_73(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'XXgeneralXX')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_74(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'GENERAL')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_75(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(None)
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_76(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get(None, 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_77(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', None)}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_78(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_79(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', )}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_80(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('XXiconXX', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_81(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('ICON', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_82(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'XXplugXX')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_83(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'PLUG')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_84(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(None)
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_85(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get(None, 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_86(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', None)}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_87(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_88(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', )}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_89(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('XXauthorXX', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_90(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('AUTHOR', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_91(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'XXDesconocidoXX')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_92(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_93(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'DESCONOCIDO')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_94(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(None)
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_95(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get(None, 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_96(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', None)}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_97(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_98(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', )}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_99(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('XXregistered_atXX', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_100(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('REGISTERED_AT', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_101(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'XXN/AXX')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_102(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'n/a')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_103(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch(None), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_104(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("XXsrc.sdk.base.RedisServiceXX"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_105(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.redisservice"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_106(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("SRC.SDK.BASE.REDISSERVICE"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_107(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch(None):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_108(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("XXsrc.sdk.base.TelemetryServiceXX"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_109(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.telemetryservice"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_110(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("SRC.SDK.BASE.TELEMETRYSERVICE"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_111(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = None

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_112(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = None
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_113(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print(None)
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_114(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("XX  Acciones disponibles:XX")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_115(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_116(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  ACCIONES DISPONIBLES:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_117(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(None)
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_118(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print(None)
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_119(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("XX    (Sin acciones definidas)XX")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_120(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_121(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (SIN ACCIONES DEFINIDAS)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_122(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = None
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_123(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = None
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_124(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get(None, False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_125(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", None)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_126(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get(False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_127(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", )
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_128(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("XXhas_authXX", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_129(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("HAS_AUTH", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_130(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", True)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_131(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = None
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_132(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get(None, "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_133(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", None)
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_134(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_135(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", )
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_136(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("XXauth_typeXX", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_137(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("AUTH_TYPE", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_138(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "XXnoneXX")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_139(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "NONE")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_140(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print(None)
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_141(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("XX  Autenticacion:XX")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_142(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_143(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  AUTENTICACION:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_144(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(None)
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_145(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'XXSiXX' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_146(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_147(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'SI' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_148(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'XXNoXX'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_149(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'no'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_150(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'NO'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_151(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(None)
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_152(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type and 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_153(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'XXN/AXX'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_154(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'n/a'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_155(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = None
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_156(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print(None)
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_157(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("XX  Esquema:XX")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_158(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_159(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  ESQUEMA:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_160(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(None)
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_161(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(None)
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_162(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(None)
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_163(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(None)
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_164(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(None)
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_165(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(None) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_166(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {'XX, XX'.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_167(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'XXNingunoXX'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_168(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_169(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'NINGUNO'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_170(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print(None)
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_171(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("XX    Detalles de autenticacion:XX")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_172(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_173(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    DETALLES DE AUTENTICACION:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_174(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = None
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_175(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(None) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_176(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = "XX, XX".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_177(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "XXNingunoXX"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_178(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_179(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "NINGUNO"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_180(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = None
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_181(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(None) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_182(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = "XX, XX".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_183(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "XXNingunoXX"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_184(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_185(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "NINGUNO"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_186(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(None)
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_187(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(None)
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_188(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(None)
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_189(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(None)
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_190(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print(None)

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_191(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("XX  Esquema: No definidoXX")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_192(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  esquema: no definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_193(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  ESQUEMA: NO DEFINIDO")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_194(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(None)

    print()
    print("=" * 60)

    return 0


def x_cmd_info__mutmut_195(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print(None)

    return 0


def x_cmd_info__mutmut_196(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" / 60)

    return 0


def x_cmd_info__mutmut_197(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("XX=XX" * 60)

    return 0


def x_cmd_info__mutmut_198(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 61)

    return 0


def x_cmd_info__mutmut_199(args: argparse.Namespace) -> int:
    """
    Muestra informacion detallada de un conector.

    Busca el conector por nombre en el registro y muestra:
    - Metadata (nombre, version, descripcion, categoria, autor)
    - Acciones disponibles
    - Requisitos de autenticacion
    - Esquema del conector

    Args:
        args: Argumentos parseados con 'connector_name'

    Retorna:
        0 si se encontro el conector, 1 si no existe
    """
    from src.sdk.registry import ConnectorRegistry

    connector_name = args.connector_name
    registry = ConnectorRegistry()

    if registry.count() == 0:
        with suppress(Exception):
            registry.auto_discover("src.connectors")
        with suppress(Exception):
            registry.auto_discover("src.tools.integrations")

    metadata = registry.get_metadata(connector_name)
    connector_class = registry.get(connector_name)

    if metadata is None or connector_class is None:
        print(f"Conector '{connector_name}' no encontrado.")
        print()
        print("Conectores disponibles:")
        for name in registry.list_names():
            print(f"  - {name}")
        return 1

    print("=" * 60)
    print(f"  INFORMACION DEL CONECTOR: {connector_name}")
    print("=" * 60)
    print()

    print("  Metadata:")
    print(f"    Nombre:        {metadata.get('name', connector_name)}")
    print(f"    Version:       {metadata.get('version', 'N/A')}")
    print(f"    Descripcion:   {metadata.get('description', 'Sin descripcion')}")
    print(f"    Categoria:     {metadata.get('category', 'general')}")
    print(f"    Icono:         {metadata.get('icon', 'plug')}")
    print(f"    Autor:         {metadata.get('author', 'Desconocido')}")
    print(f"    Registrado:    {metadata.get('registered_at', 'N/A')}")
    print()

    try:
        from unittest.mock import patch
        with patch("src.sdk.base.RedisService"), patch("src.sdk.base.TelemetryService"):
            instance = connector_class()

        actions = instance.get_action_names()
        print("  Acciones disponibles:")
        if actions:
            for action in actions:
                print(f"    - {action}")
        else:
            print("    (Sin acciones definidas)")
        print()

        status = instance.get_status()
        has_auth = status.get("has_auth", False)
        auth_type = status.get("auth_type", "none")
        print("  Autenticacion:")
        print(f"    Requiere auth: {'Si' if has_auth else 'No'}")
        print(f"    Tipo:          {auth_type or 'N/A'}")
        print()

        schema = instance.get_schema()
        if schema:
            print("  Esquema:")
            print(f"    Nombre:           {schema.name}")
            print(f"    Version:          {schema.version}")
            print(f"    Acciones:         {len(schema.actions)}")
            print(f"    Requisitos auth:  {len(schema.auth_requirements)}")
            print(f"    Tags:             {', '.join(schema.tags) if schema.tags else 'Ninguno'}")
            if schema.auth_requirements:
                print()
                print("    Detalles de autenticacion:")
                for req in schema.auth_requirements:
                    required = ", ".join(req.required_fields) if req.required_fields else "Ninguno"
                    optional = ", ".join(req.optional_fields) if req.optional_fields else "Ninguno"
                    print(f"      - Tipo: {req.auth_type}")
                    print(f"        Campos requeridos: {required}")
                    print(f"        Campos opcionales: {optional}")
                    if req.description:
                        print(f"        Descripcion: {req.description}")
        else:
            print("  Esquema: No definido")

    except Exception as exc:
        print(f"  (No se pudo obtener informacion detallada: {exc})")

    print()
    print("=" * 60)

    return 1

mutants_x_cmd_info__mutmut['_mutmut_orig'] = x_cmd_info__mutmut_orig # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_1'] = x_cmd_info__mutmut_1 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_2'] = x_cmd_info__mutmut_2 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_3'] = x_cmd_info__mutmut_3 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_4'] = x_cmd_info__mutmut_4 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_5'] = x_cmd_info__mutmut_5 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_6'] = x_cmd_info__mutmut_6 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_7'] = x_cmd_info__mutmut_7 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_8'] = x_cmd_info__mutmut_8 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_9'] = x_cmd_info__mutmut_9 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_10'] = x_cmd_info__mutmut_10 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_11'] = x_cmd_info__mutmut_11 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_12'] = x_cmd_info__mutmut_12 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_13'] = x_cmd_info__mutmut_13 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_14'] = x_cmd_info__mutmut_14 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_15'] = x_cmd_info__mutmut_15 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_16'] = x_cmd_info__mutmut_16 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_17'] = x_cmd_info__mutmut_17 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_18'] = x_cmd_info__mutmut_18 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_19'] = x_cmd_info__mutmut_19 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_20'] = x_cmd_info__mutmut_20 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_21'] = x_cmd_info__mutmut_21 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_22'] = x_cmd_info__mutmut_22 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_23'] = x_cmd_info__mutmut_23 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_24'] = x_cmd_info__mutmut_24 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_25'] = x_cmd_info__mutmut_25 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_26'] = x_cmd_info__mutmut_26 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_27'] = x_cmd_info__mutmut_27 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_28'] = x_cmd_info__mutmut_28 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_29'] = x_cmd_info__mutmut_29 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_30'] = x_cmd_info__mutmut_30 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_31'] = x_cmd_info__mutmut_31 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_32'] = x_cmd_info__mutmut_32 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_33'] = x_cmd_info__mutmut_33 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_34'] = x_cmd_info__mutmut_34 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_35'] = x_cmd_info__mutmut_35 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_36'] = x_cmd_info__mutmut_36 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_37'] = x_cmd_info__mutmut_37 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_38'] = x_cmd_info__mutmut_38 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_39'] = x_cmd_info__mutmut_39 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_40'] = x_cmd_info__mutmut_40 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_41'] = x_cmd_info__mutmut_41 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_42'] = x_cmd_info__mutmut_42 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_43'] = x_cmd_info__mutmut_43 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_44'] = x_cmd_info__mutmut_44 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_45'] = x_cmd_info__mutmut_45 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_46'] = x_cmd_info__mutmut_46 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_47'] = x_cmd_info__mutmut_47 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_48'] = x_cmd_info__mutmut_48 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_49'] = x_cmd_info__mutmut_49 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_50'] = x_cmd_info__mutmut_50 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_51'] = x_cmd_info__mutmut_51 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_52'] = x_cmd_info__mutmut_52 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_53'] = x_cmd_info__mutmut_53 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_54'] = x_cmd_info__mutmut_54 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_55'] = x_cmd_info__mutmut_55 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_56'] = x_cmd_info__mutmut_56 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_57'] = x_cmd_info__mutmut_57 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_58'] = x_cmd_info__mutmut_58 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_59'] = x_cmd_info__mutmut_59 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_60'] = x_cmd_info__mutmut_60 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_61'] = x_cmd_info__mutmut_61 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_62'] = x_cmd_info__mutmut_62 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_63'] = x_cmd_info__mutmut_63 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_64'] = x_cmd_info__mutmut_64 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_65'] = x_cmd_info__mutmut_65 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_66'] = x_cmd_info__mutmut_66 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_67'] = x_cmd_info__mutmut_67 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_68'] = x_cmd_info__mutmut_68 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_69'] = x_cmd_info__mutmut_69 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_70'] = x_cmd_info__mutmut_70 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_71'] = x_cmd_info__mutmut_71 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_72'] = x_cmd_info__mutmut_72 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_73'] = x_cmd_info__mutmut_73 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_74'] = x_cmd_info__mutmut_74 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_75'] = x_cmd_info__mutmut_75 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_76'] = x_cmd_info__mutmut_76 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_77'] = x_cmd_info__mutmut_77 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_78'] = x_cmd_info__mutmut_78 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_79'] = x_cmd_info__mutmut_79 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_80'] = x_cmd_info__mutmut_80 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_81'] = x_cmd_info__mutmut_81 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_82'] = x_cmd_info__mutmut_82 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_83'] = x_cmd_info__mutmut_83 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_84'] = x_cmd_info__mutmut_84 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_85'] = x_cmd_info__mutmut_85 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_86'] = x_cmd_info__mutmut_86 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_87'] = x_cmd_info__mutmut_87 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_88'] = x_cmd_info__mutmut_88 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_89'] = x_cmd_info__mutmut_89 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_90'] = x_cmd_info__mutmut_90 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_91'] = x_cmd_info__mutmut_91 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_92'] = x_cmd_info__mutmut_92 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_93'] = x_cmd_info__mutmut_93 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_94'] = x_cmd_info__mutmut_94 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_95'] = x_cmd_info__mutmut_95 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_96'] = x_cmd_info__mutmut_96 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_97'] = x_cmd_info__mutmut_97 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_98'] = x_cmd_info__mutmut_98 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_99'] = x_cmd_info__mutmut_99 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_100'] = x_cmd_info__mutmut_100 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_101'] = x_cmd_info__mutmut_101 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_102'] = x_cmd_info__mutmut_102 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_103'] = x_cmd_info__mutmut_103 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_104'] = x_cmd_info__mutmut_104 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_105'] = x_cmd_info__mutmut_105 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_106'] = x_cmd_info__mutmut_106 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_107'] = x_cmd_info__mutmut_107 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_108'] = x_cmd_info__mutmut_108 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_109'] = x_cmd_info__mutmut_109 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_110'] = x_cmd_info__mutmut_110 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_111'] = x_cmd_info__mutmut_111 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_112'] = x_cmd_info__mutmut_112 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_113'] = x_cmd_info__mutmut_113 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_114'] = x_cmd_info__mutmut_114 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_115'] = x_cmd_info__mutmut_115 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_116'] = x_cmd_info__mutmut_116 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_117'] = x_cmd_info__mutmut_117 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_118'] = x_cmd_info__mutmut_118 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_119'] = x_cmd_info__mutmut_119 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_120'] = x_cmd_info__mutmut_120 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_121'] = x_cmd_info__mutmut_121 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_122'] = x_cmd_info__mutmut_122 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_123'] = x_cmd_info__mutmut_123 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_124'] = x_cmd_info__mutmut_124 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_125'] = x_cmd_info__mutmut_125 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_126'] = x_cmd_info__mutmut_126 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_127'] = x_cmd_info__mutmut_127 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_128'] = x_cmd_info__mutmut_128 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_129'] = x_cmd_info__mutmut_129 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_130'] = x_cmd_info__mutmut_130 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_131'] = x_cmd_info__mutmut_131 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_132'] = x_cmd_info__mutmut_132 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_133'] = x_cmd_info__mutmut_133 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_134'] = x_cmd_info__mutmut_134 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_135'] = x_cmd_info__mutmut_135 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_136'] = x_cmd_info__mutmut_136 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_137'] = x_cmd_info__mutmut_137 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_138'] = x_cmd_info__mutmut_138 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_139'] = x_cmd_info__mutmut_139 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_140'] = x_cmd_info__mutmut_140 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_141'] = x_cmd_info__mutmut_141 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_142'] = x_cmd_info__mutmut_142 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_143'] = x_cmd_info__mutmut_143 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_144'] = x_cmd_info__mutmut_144 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_145'] = x_cmd_info__mutmut_145 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_146'] = x_cmd_info__mutmut_146 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_147'] = x_cmd_info__mutmut_147 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_148'] = x_cmd_info__mutmut_148 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_149'] = x_cmd_info__mutmut_149 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_150'] = x_cmd_info__mutmut_150 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_151'] = x_cmd_info__mutmut_151 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_152'] = x_cmd_info__mutmut_152 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_153'] = x_cmd_info__mutmut_153 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_154'] = x_cmd_info__mutmut_154 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_155'] = x_cmd_info__mutmut_155 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_156'] = x_cmd_info__mutmut_156 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_157'] = x_cmd_info__mutmut_157 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_158'] = x_cmd_info__mutmut_158 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_159'] = x_cmd_info__mutmut_159 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_160'] = x_cmd_info__mutmut_160 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_161'] = x_cmd_info__mutmut_161 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_162'] = x_cmd_info__mutmut_162 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_163'] = x_cmd_info__mutmut_163 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_164'] = x_cmd_info__mutmut_164 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_165'] = x_cmd_info__mutmut_165 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_166'] = x_cmd_info__mutmut_166 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_167'] = x_cmd_info__mutmut_167 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_168'] = x_cmd_info__mutmut_168 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_169'] = x_cmd_info__mutmut_169 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_170'] = x_cmd_info__mutmut_170 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_171'] = x_cmd_info__mutmut_171 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_172'] = x_cmd_info__mutmut_172 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_173'] = x_cmd_info__mutmut_173 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_174'] = x_cmd_info__mutmut_174 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_175'] = x_cmd_info__mutmut_175 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_176'] = x_cmd_info__mutmut_176 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_177'] = x_cmd_info__mutmut_177 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_178'] = x_cmd_info__mutmut_178 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_179'] = x_cmd_info__mutmut_179 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_180'] = x_cmd_info__mutmut_180 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_181'] = x_cmd_info__mutmut_181 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_182'] = x_cmd_info__mutmut_182 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_183'] = x_cmd_info__mutmut_183 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_184'] = x_cmd_info__mutmut_184 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_185'] = x_cmd_info__mutmut_185 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_186'] = x_cmd_info__mutmut_186 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_187'] = x_cmd_info__mutmut_187 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_188'] = x_cmd_info__mutmut_188 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_189'] = x_cmd_info__mutmut_189 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_190'] = x_cmd_info__mutmut_190 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_191'] = x_cmd_info__mutmut_191 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_192'] = x_cmd_info__mutmut_192 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_193'] = x_cmd_info__mutmut_193 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_194'] = x_cmd_info__mutmut_194 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_195'] = x_cmd_info__mutmut_195 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_196'] = x_cmd_info__mutmut_196 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_197'] = x_cmd_info__mutmut_197 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_198'] = x_cmd_info__mutmut_198 # type: ignore # mutmut generated
mutants_x_cmd_info__mutmut['x_cmd_info__mutmut_199'] = x_cmd_info__mutmut_199 # type: ignore # mutmut generated
