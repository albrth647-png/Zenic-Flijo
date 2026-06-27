"""
Zenic CLI — Comando: publish
Empaqueta y publica un conector al marketplace.
"""

from __future__ import annotations

import argparse
import os
import sys
from contextlib import suppress
from pathlib import Path

from src.cli.commands.helpers import _format_validation_report, _package_connector, _run_validation, _upload_connector


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_cmd_publish__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_cmd_publish__mutmut)
def cmd_publish(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_orig(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_1(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = None
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_2(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(None)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_3(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = None

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_4(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) and "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_5(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(None, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_6(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, None, None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_7(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr("registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_8(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_9(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", ) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_10(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "XXregistryXX", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_11(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "REGISTRY", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_12(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "XXhttps://marketplace.zenic-flijo.io/api/v1/connectorsXX"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_13(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "HTTPS://MARKETPLACE.ZENIC-FLIJO.IO/API/V1/CONNECTORS"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_14(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print(None)
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_15(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("XXPublicando conector...XX")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_16(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_17(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("PUBLICANDO CONECTOR...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_18(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(None)
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_19(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(None)
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_20(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print(None)
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_21(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("XXPaso 1/3: Validando conector...XX")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_22(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("paso 1/3: validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_23(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("PASO 1/3: VALIDANDO CONECTOR...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_24(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = None
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_25(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(None)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_26(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_27(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["XXpassedXX"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_28(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["PASSED"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_29(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print(None, file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_30(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=None)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_31(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print(file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_32(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", )
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_33(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("XX  Validacion FALLIDA. Corrija los errores antes de publicar.XX", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_34(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  validacion fallida. corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_35(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  VALIDACION FALLIDA. CORRIJA LOS ERRORES ANTES DE PUBLICAR.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_36(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(None)
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_37(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(None))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_38(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 2
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_39(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(None)
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_40(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['XXpassed_checksXX']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_41(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['PASSED_CHECKS']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_42(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['XXtotal_checksXX']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_43(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['TOTAL_CHECKS']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_44(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print(None)
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_45(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("XXPaso 2/3: Empaquetando conector...XX")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_46(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("paso 2/3: empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_47(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("PASO 2/3: EMPAQUETANDO CONECTOR...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_48(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = None
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_49(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(None)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_50(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is not None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_51(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print(None, file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_52(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=None)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_53(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print(file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_54(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", )
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_55(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("XX  Error: No se pudo empaquetar el conectorXX", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_56(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  error: no se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_57(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  ERROR: NO SE PUDO EMPAQUETAR EL CONECTOR", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_58(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 2
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_59(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = None
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_60(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) * 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_61(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(None) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_62(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1025
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_63(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(None)
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_64(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print(None)
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_65(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("XXPaso 3/3: Subiendo al marketplace...XX")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_66(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("paso 3/3: subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_67(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("PASO 3/3: SUBIENDO AL MARKETPLACE...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_68(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = None
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_69(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(None, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_70(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, None)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_71(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_72(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, )
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_73(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print(None)
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_74(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("XX  Publicacion exitosa!XX")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_75(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_76(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  PUBLICACION EXITOSA!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_77(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print(None, file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_78(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=None)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_79(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print(file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_80(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", )
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_81(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("XX  Error: No se pudo subir al marketplaceXX", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_82(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  error: no se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_83(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  ERROR: NO SE PUDO SUBIR AL MARKETPLACE", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_84(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print(None)
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_85(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("XX  Nota: Verifique su ZENIC_API_KEY y la conectividad al registroXX")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_86(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  nota: verifique su zenic_api_key y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_87(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  NOTA: VERIFIQUE SU ZENIC_API_KEY Y LA CONECTIVIDAD AL REGISTRO")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_88(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 2

    with suppress(OSError):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_89(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(None):
        os.remove(zip_path)

    return 0


def x_cmd_publish__mutmut_90(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(None)

    return 0


def x_cmd_publish__mutmut_91(args: argparse.Namespace) -> int:
    """
    Empaqueta y publica un conector al marketplace.

    El proceso realiza los siguientes pasos:
    1. Valida el conector (ejecuta validate internamente)
    2. Empaqueta el conector como archivo .zip con manifest.json
    3. Sube al registro del marketplace (HTTP POST con API key)
    4. Muestra el estado de la publicacion

    Args:
        args: Argumentos parseados con 'connector_path', 'registry'

    Retorna:
        0 si la publicacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    registry_url = getattr(args, "registry", None) or "https://marketplace.zenic-flijo.io/api/v1/connectors"

    print("Publicando conector...")
    print(f"  Ruta:     {connector_path}")
    print(f"  Registro: {registry_url}")
    print()

    # Paso 1: Validar
    print("Paso 1/3: Validando conector...")
    validation = _run_validation(connector_path)
    if not validation["passed"]:
        print("  Validacion FALLIDA. Corrija los errores antes de publicar.", file=sys.stderr)
        print()
        print(_format_validation_report(validation))
        return 1
    print(f"  Validacion OK ({validation['passed_checks']}/{validation['total_checks']} checks)")
    print()

    # Paso 2: Empaquetar
    print("Paso 2/3: Empaquetando conector...")
    zip_path = _package_connector(connector_path)
    if zip_path is None:
        print("  Error: No se pudo empaquetar el conector", file=sys.stderr)
        return 1
    zip_size_kb = os.path.getsize(zip_path) / 1024
    print(f"  Paquete creado: {zip_path} ({zip_size_kb:.1f} KB)")
    print()

    # Paso 3: Subir
    print("Paso 3/3: Subiendo al marketplace...")
    success = _upload_connector(zip_path, registry_url)
    if success:
        print("  Publicacion exitosa!")
    else:
        print("  Error: No se pudo subir al marketplace", file=sys.stderr)
        print("  Nota: Verifique su ZENIC_API_KEY y la conectividad al registro")
        return 1

    with suppress(OSError):
        os.remove(zip_path)

    return 1

mutants_x_cmd_publish__mutmut['_mutmut_orig'] = x_cmd_publish__mutmut_orig # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_1'] = x_cmd_publish__mutmut_1 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_2'] = x_cmd_publish__mutmut_2 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_3'] = x_cmd_publish__mutmut_3 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_4'] = x_cmd_publish__mutmut_4 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_5'] = x_cmd_publish__mutmut_5 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_6'] = x_cmd_publish__mutmut_6 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_7'] = x_cmd_publish__mutmut_7 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_8'] = x_cmd_publish__mutmut_8 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_9'] = x_cmd_publish__mutmut_9 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_10'] = x_cmd_publish__mutmut_10 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_11'] = x_cmd_publish__mutmut_11 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_12'] = x_cmd_publish__mutmut_12 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_13'] = x_cmd_publish__mutmut_13 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_14'] = x_cmd_publish__mutmut_14 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_15'] = x_cmd_publish__mutmut_15 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_16'] = x_cmd_publish__mutmut_16 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_17'] = x_cmd_publish__mutmut_17 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_18'] = x_cmd_publish__mutmut_18 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_19'] = x_cmd_publish__mutmut_19 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_20'] = x_cmd_publish__mutmut_20 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_21'] = x_cmd_publish__mutmut_21 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_22'] = x_cmd_publish__mutmut_22 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_23'] = x_cmd_publish__mutmut_23 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_24'] = x_cmd_publish__mutmut_24 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_25'] = x_cmd_publish__mutmut_25 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_26'] = x_cmd_publish__mutmut_26 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_27'] = x_cmd_publish__mutmut_27 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_28'] = x_cmd_publish__mutmut_28 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_29'] = x_cmd_publish__mutmut_29 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_30'] = x_cmd_publish__mutmut_30 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_31'] = x_cmd_publish__mutmut_31 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_32'] = x_cmd_publish__mutmut_32 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_33'] = x_cmd_publish__mutmut_33 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_34'] = x_cmd_publish__mutmut_34 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_35'] = x_cmd_publish__mutmut_35 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_36'] = x_cmd_publish__mutmut_36 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_37'] = x_cmd_publish__mutmut_37 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_38'] = x_cmd_publish__mutmut_38 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_39'] = x_cmd_publish__mutmut_39 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_40'] = x_cmd_publish__mutmut_40 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_41'] = x_cmd_publish__mutmut_41 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_42'] = x_cmd_publish__mutmut_42 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_43'] = x_cmd_publish__mutmut_43 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_44'] = x_cmd_publish__mutmut_44 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_45'] = x_cmd_publish__mutmut_45 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_46'] = x_cmd_publish__mutmut_46 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_47'] = x_cmd_publish__mutmut_47 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_48'] = x_cmd_publish__mutmut_48 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_49'] = x_cmd_publish__mutmut_49 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_50'] = x_cmd_publish__mutmut_50 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_51'] = x_cmd_publish__mutmut_51 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_52'] = x_cmd_publish__mutmut_52 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_53'] = x_cmd_publish__mutmut_53 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_54'] = x_cmd_publish__mutmut_54 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_55'] = x_cmd_publish__mutmut_55 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_56'] = x_cmd_publish__mutmut_56 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_57'] = x_cmd_publish__mutmut_57 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_58'] = x_cmd_publish__mutmut_58 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_59'] = x_cmd_publish__mutmut_59 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_60'] = x_cmd_publish__mutmut_60 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_61'] = x_cmd_publish__mutmut_61 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_62'] = x_cmd_publish__mutmut_62 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_63'] = x_cmd_publish__mutmut_63 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_64'] = x_cmd_publish__mutmut_64 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_65'] = x_cmd_publish__mutmut_65 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_66'] = x_cmd_publish__mutmut_66 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_67'] = x_cmd_publish__mutmut_67 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_68'] = x_cmd_publish__mutmut_68 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_69'] = x_cmd_publish__mutmut_69 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_70'] = x_cmd_publish__mutmut_70 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_71'] = x_cmd_publish__mutmut_71 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_72'] = x_cmd_publish__mutmut_72 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_73'] = x_cmd_publish__mutmut_73 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_74'] = x_cmd_publish__mutmut_74 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_75'] = x_cmd_publish__mutmut_75 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_76'] = x_cmd_publish__mutmut_76 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_77'] = x_cmd_publish__mutmut_77 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_78'] = x_cmd_publish__mutmut_78 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_79'] = x_cmd_publish__mutmut_79 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_80'] = x_cmd_publish__mutmut_80 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_81'] = x_cmd_publish__mutmut_81 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_82'] = x_cmd_publish__mutmut_82 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_83'] = x_cmd_publish__mutmut_83 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_84'] = x_cmd_publish__mutmut_84 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_85'] = x_cmd_publish__mutmut_85 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_86'] = x_cmd_publish__mutmut_86 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_87'] = x_cmd_publish__mutmut_87 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_88'] = x_cmd_publish__mutmut_88 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_89'] = x_cmd_publish__mutmut_89 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_90'] = x_cmd_publish__mutmut_90 # type: ignore # mutmut generated
mutants_x_cmd_publish__mutmut['x_cmd_publish__mutmut_91'] = x_cmd_publish__mutmut_91 # type: ignore # mutmut generated
