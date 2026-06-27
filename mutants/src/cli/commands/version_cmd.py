"""
Zenic CLI — Comando: version
Gestiona la version de un conector siguiendo semver.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from src.cli.commands.helpers import _bump_version, _read_version, _update_version_in_files


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_cmd_version__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_cmd_version__mutmut)
def cmd_version(args: argparse.Namespace) -> int:
    """
    Gestiona la version de un conector siguiendo semver.

    Si se especifica --bump, incrementa la version segun el tipo:
    - major: Incrementa la version mayor (X.0.0) - cambios incompatibles
    - minor: Incrementa la version menor (0.X.0) - nueva funcionalidad compatible
    - patch: Incrementa la version de parche (0.0.X) - correcciones de bugs

    Si no se especifica --bump, muestra la version actual.

    Args:
        args: Argumentos parseados con 'connector_path', 'bump'

    Retorna:
        0 si la operacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    bump_type = getattr(args, "bump", None)

    current_version = _read_version(connector_path)
    if current_version is None:
        print(f"Error: No se pudo determinar la version del conector en {connector_path}", file=sys.stderr)
        return 1

    if bump_type is None:
        print(f"Conector: {connector_path.name}")
        print(f"Version actual: {current_version}")
        return 0

    new_version = _bump_version(current_version, bump_type)
    if new_version is None:
        print(f"Error: No se pudo calcular la nueva version. Version actual: {current_version}", file=sys.stderr)
        return 1

    updated_files = _update_version_in_files(connector_path, current_version, new_version)

    print(f"Version actualizada: {current_version} -> {new_version}")
    print(f"Bump: {bump_type}")
    print()
    print("Archivos actualizados:")
    for filepath in updated_files:
        print(f"  - {filepath}")

    return 0


def x_cmd_version__mutmut_orig(args: argparse.Namespace) -> int:
    """
    Gestiona la version de un conector siguiendo semver.

    Si se especifica --bump, incrementa la version segun el tipo:
    - major: Incrementa la version mayor (X.0.0) - cambios incompatibles
    - minor: Incrementa la version menor (0.X.0) - nueva funcionalidad compatible
    - patch: Incrementa la version de parche (0.0.X) - correcciones de bugs

    Si no se especifica --bump, muestra la version actual.

    Args:
        args: Argumentos parseados con 'connector_path', 'bump'

    Retorna:
        0 si la operacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    bump_type = getattr(args, "bump", None)

    current_version = _read_version(connector_path)
    if current_version is None:
        print(f"Error: No se pudo determinar la version del conector en {connector_path}", file=sys.stderr)
        return 1

    if bump_type is None:
        print(f"Conector: {connector_path.name}")
        print(f"Version actual: {current_version}")
        return 0

    new_version = _bump_version(current_version, bump_type)
    if new_version is None:
        print(f"Error: No se pudo calcular la nueva version. Version actual: {current_version}", file=sys.stderr)
        return 1

    updated_files = _update_version_in_files(connector_path, current_version, new_version)

    print(f"Version actualizada: {current_version} -> {new_version}")
    print(f"Bump: {bump_type}")
    print()
    print("Archivos actualizados:")
    for filepath in updated_files:
        print(f"  - {filepath}")

    return 0


def x_cmd_version__mutmut_1(args: argparse.Namespace) -> int:
    """
    Gestiona la version de un conector siguiendo semver.

    Si se especifica --bump, incrementa la version segun el tipo:
    - major: Incrementa la version mayor (X.0.0) - cambios incompatibles
    - minor: Incrementa la version menor (0.X.0) - nueva funcionalidad compatible
    - patch: Incrementa la version de parche (0.0.X) - correcciones de bugs

    Si no se especifica --bump, muestra la version actual.

    Args:
        args: Argumentos parseados con 'connector_path', 'bump'

    Retorna:
        0 si la operacion fue exitosa, 1 si hubo errores
    """
    connector_path = None
    bump_type = getattr(args, "bump", None)

    current_version = _read_version(connector_path)
    if current_version is None:
        print(f"Error: No se pudo determinar la version del conector en {connector_path}", file=sys.stderr)
        return 1

    if bump_type is None:
        print(f"Conector: {connector_path.name}")
        print(f"Version actual: {current_version}")
        return 0

    new_version = _bump_version(current_version, bump_type)
    if new_version is None:
        print(f"Error: No se pudo calcular la nueva version. Version actual: {current_version}", file=sys.stderr)
        return 1

    updated_files = _update_version_in_files(connector_path, current_version, new_version)

    print(f"Version actualizada: {current_version} -> {new_version}")
    print(f"Bump: {bump_type}")
    print()
    print("Archivos actualizados:")
    for filepath in updated_files:
        print(f"  - {filepath}")

    return 0


def x_cmd_version__mutmut_2(args: argparse.Namespace) -> int:
    """
    Gestiona la version de un conector siguiendo semver.

    Si se especifica --bump, incrementa la version segun el tipo:
    - major: Incrementa la version mayor (X.0.0) - cambios incompatibles
    - minor: Incrementa la version menor (0.X.0) - nueva funcionalidad compatible
    - patch: Incrementa la version de parche (0.0.X) - correcciones de bugs

    Si no se especifica --bump, muestra la version actual.

    Args:
        args: Argumentos parseados con 'connector_path', 'bump'

    Retorna:
        0 si la operacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(None)
    bump_type = getattr(args, "bump", None)

    current_version = _read_version(connector_path)
    if current_version is None:
        print(f"Error: No se pudo determinar la version del conector en {connector_path}", file=sys.stderr)
        return 1

    if bump_type is None:
        print(f"Conector: {connector_path.name}")
        print(f"Version actual: {current_version}")
        return 0

    new_version = _bump_version(current_version, bump_type)
    if new_version is None:
        print(f"Error: No se pudo calcular la nueva version. Version actual: {current_version}", file=sys.stderr)
        return 1

    updated_files = _update_version_in_files(connector_path, current_version, new_version)

    print(f"Version actualizada: {current_version} -> {new_version}")
    print(f"Bump: {bump_type}")
    print()
    print("Archivos actualizados:")
    for filepath in updated_files:
        print(f"  - {filepath}")

    return 0


def x_cmd_version__mutmut_3(args: argparse.Namespace) -> int:
    """
    Gestiona la version de un conector siguiendo semver.

    Si se especifica --bump, incrementa la version segun el tipo:
    - major: Incrementa la version mayor (X.0.0) - cambios incompatibles
    - minor: Incrementa la version menor (0.X.0) - nueva funcionalidad compatible
    - patch: Incrementa la version de parche (0.0.X) - correcciones de bugs

    Si no se especifica --bump, muestra la version actual.

    Args:
        args: Argumentos parseados con 'connector_path', 'bump'

    Retorna:
        0 si la operacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    bump_type = None

    current_version = _read_version(connector_path)
    if current_version is None:
        print(f"Error: No se pudo determinar la version del conector en {connector_path}", file=sys.stderr)
        return 1

    if bump_type is None:
        print(f"Conector: {connector_path.name}")
        print(f"Version actual: {current_version}")
        return 0

    new_version = _bump_version(current_version, bump_type)
    if new_version is None:
        print(f"Error: No se pudo calcular la nueva version. Version actual: {current_version}", file=sys.stderr)
        return 1

    updated_files = _update_version_in_files(connector_path, current_version, new_version)

    print(f"Version actualizada: {current_version} -> {new_version}")
    print(f"Bump: {bump_type}")
    print()
    print("Archivos actualizados:")
    for filepath in updated_files:
        print(f"  - {filepath}")

    return 0


def x_cmd_version__mutmut_4(args: argparse.Namespace) -> int:
    """
    Gestiona la version de un conector siguiendo semver.

    Si se especifica --bump, incrementa la version segun el tipo:
    - major: Incrementa la version mayor (X.0.0) - cambios incompatibles
    - minor: Incrementa la version menor (0.X.0) - nueva funcionalidad compatible
    - patch: Incrementa la version de parche (0.0.X) - correcciones de bugs

    Si no se especifica --bump, muestra la version actual.

    Args:
        args: Argumentos parseados con 'connector_path', 'bump'

    Retorna:
        0 si la operacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    bump_type = getattr(None, "bump", None)

    current_version = _read_version(connector_path)
    if current_version is None:
        print(f"Error: No se pudo determinar la version del conector en {connector_path}", file=sys.stderr)
        return 1

    if bump_type is None:
        print(f"Conector: {connector_path.name}")
        print(f"Version actual: {current_version}")
        return 0

    new_version = _bump_version(current_version, bump_type)
    if new_version is None:
        print(f"Error: No se pudo calcular la nueva version. Version actual: {current_version}", file=sys.stderr)
        return 1

    updated_files = _update_version_in_files(connector_path, current_version, new_version)

    print(f"Version actualizada: {current_version} -> {new_version}")
    print(f"Bump: {bump_type}")
    print()
    print("Archivos actualizados:")
    for filepath in updated_files:
        print(f"  - {filepath}")

    return 0


def x_cmd_version__mutmut_5(args: argparse.Namespace) -> int:
    """
    Gestiona la version de un conector siguiendo semver.

    Si se especifica --bump, incrementa la version segun el tipo:
    - major: Incrementa la version mayor (X.0.0) - cambios incompatibles
    - minor: Incrementa la version menor (0.X.0) - nueva funcionalidad compatible
    - patch: Incrementa la version de parche (0.0.X) - correcciones de bugs

    Si no se especifica --bump, muestra la version actual.

    Args:
        args: Argumentos parseados con 'connector_path', 'bump'

    Retorna:
        0 si la operacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    bump_type = getattr(args, None, None)

    current_version = _read_version(connector_path)
    if current_version is None:
        print(f"Error: No se pudo determinar la version del conector en {connector_path}", file=sys.stderr)
        return 1

    if bump_type is None:
        print(f"Conector: {connector_path.name}")
        print(f"Version actual: {current_version}")
        return 0

    new_version = _bump_version(current_version, bump_type)
    if new_version is None:
        print(f"Error: No se pudo calcular la nueva version. Version actual: {current_version}", file=sys.stderr)
        return 1

    updated_files = _update_version_in_files(connector_path, current_version, new_version)

    print(f"Version actualizada: {current_version} -> {new_version}")
    print(f"Bump: {bump_type}")
    print()
    print("Archivos actualizados:")
    for filepath in updated_files:
        print(f"  - {filepath}")

    return 0


def x_cmd_version__mutmut_6(args: argparse.Namespace) -> int:
    """
    Gestiona la version de un conector siguiendo semver.

    Si se especifica --bump, incrementa la version segun el tipo:
    - major: Incrementa la version mayor (X.0.0) - cambios incompatibles
    - minor: Incrementa la version menor (0.X.0) - nueva funcionalidad compatible
    - patch: Incrementa la version de parche (0.0.X) - correcciones de bugs

    Si no se especifica --bump, muestra la version actual.

    Args:
        args: Argumentos parseados con 'connector_path', 'bump'

    Retorna:
        0 si la operacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    bump_type = getattr("bump", None)

    current_version = _read_version(connector_path)
    if current_version is None:
        print(f"Error: No se pudo determinar la version del conector en {connector_path}", file=sys.stderr)
        return 1

    if bump_type is None:
        print(f"Conector: {connector_path.name}")
        print(f"Version actual: {current_version}")
        return 0

    new_version = _bump_version(current_version, bump_type)
    if new_version is None:
        print(f"Error: No se pudo calcular la nueva version. Version actual: {current_version}", file=sys.stderr)
        return 1

    updated_files = _update_version_in_files(connector_path, current_version, new_version)

    print(f"Version actualizada: {current_version} -> {new_version}")
    print(f"Bump: {bump_type}")
    print()
    print("Archivos actualizados:")
    for filepath in updated_files:
        print(f"  - {filepath}")

    return 0


def x_cmd_version__mutmut_7(args: argparse.Namespace) -> int:
    """
    Gestiona la version de un conector siguiendo semver.

    Si se especifica --bump, incrementa la version segun el tipo:
    - major: Incrementa la version mayor (X.0.0) - cambios incompatibles
    - minor: Incrementa la version menor (0.X.0) - nueva funcionalidad compatible
    - patch: Incrementa la version de parche (0.0.X) - correcciones de bugs

    Si no se especifica --bump, muestra la version actual.

    Args:
        args: Argumentos parseados con 'connector_path', 'bump'

    Retorna:
        0 si la operacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    bump_type = getattr(args, None)

    current_version = _read_version(connector_path)
    if current_version is None:
        print(f"Error: No se pudo determinar la version del conector en {connector_path}", file=sys.stderr)
        return 1

    if bump_type is None:
        print(f"Conector: {connector_path.name}")
        print(f"Version actual: {current_version}")
        return 0

    new_version = _bump_version(current_version, bump_type)
    if new_version is None:
        print(f"Error: No se pudo calcular la nueva version. Version actual: {current_version}", file=sys.stderr)
        return 1

    updated_files = _update_version_in_files(connector_path, current_version, new_version)

    print(f"Version actualizada: {current_version} -> {new_version}")
    print(f"Bump: {bump_type}")
    print()
    print("Archivos actualizados:")
    for filepath in updated_files:
        print(f"  - {filepath}")

    return 0


def x_cmd_version__mutmut_8(args: argparse.Namespace) -> int:
    """
    Gestiona la version de un conector siguiendo semver.

    Si se especifica --bump, incrementa la version segun el tipo:
    - major: Incrementa la version mayor (X.0.0) - cambios incompatibles
    - minor: Incrementa la version menor (0.X.0) - nueva funcionalidad compatible
    - patch: Incrementa la version de parche (0.0.X) - correcciones de bugs

    Si no se especifica --bump, muestra la version actual.

    Args:
        args: Argumentos parseados con 'connector_path', 'bump'

    Retorna:
        0 si la operacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    bump_type = getattr(args, "bump", )

    current_version = _read_version(connector_path)
    if current_version is None:
        print(f"Error: No se pudo determinar la version del conector en {connector_path}", file=sys.stderr)
        return 1

    if bump_type is None:
        print(f"Conector: {connector_path.name}")
        print(f"Version actual: {current_version}")
        return 0

    new_version = _bump_version(current_version, bump_type)
    if new_version is None:
        print(f"Error: No se pudo calcular la nueva version. Version actual: {current_version}", file=sys.stderr)
        return 1

    updated_files = _update_version_in_files(connector_path, current_version, new_version)

    print(f"Version actualizada: {current_version} -> {new_version}")
    print(f"Bump: {bump_type}")
    print()
    print("Archivos actualizados:")
    for filepath in updated_files:
        print(f"  - {filepath}")

    return 0


def x_cmd_version__mutmut_9(args: argparse.Namespace) -> int:
    """
    Gestiona la version de un conector siguiendo semver.

    Si se especifica --bump, incrementa la version segun el tipo:
    - major: Incrementa la version mayor (X.0.0) - cambios incompatibles
    - minor: Incrementa la version menor (0.X.0) - nueva funcionalidad compatible
    - patch: Incrementa la version de parche (0.0.X) - correcciones de bugs

    Si no se especifica --bump, muestra la version actual.

    Args:
        args: Argumentos parseados con 'connector_path', 'bump'

    Retorna:
        0 si la operacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    bump_type = getattr(args, "XXbumpXX", None)

    current_version = _read_version(connector_path)
    if current_version is None:
        print(f"Error: No se pudo determinar la version del conector en {connector_path}", file=sys.stderr)
        return 1

    if bump_type is None:
        print(f"Conector: {connector_path.name}")
        print(f"Version actual: {current_version}")
        return 0

    new_version = _bump_version(current_version, bump_type)
    if new_version is None:
        print(f"Error: No se pudo calcular la nueva version. Version actual: {current_version}", file=sys.stderr)
        return 1

    updated_files = _update_version_in_files(connector_path, current_version, new_version)

    print(f"Version actualizada: {current_version} -> {new_version}")
    print(f"Bump: {bump_type}")
    print()
    print("Archivos actualizados:")
    for filepath in updated_files:
        print(f"  - {filepath}")

    return 0


def x_cmd_version__mutmut_10(args: argparse.Namespace) -> int:
    """
    Gestiona la version de un conector siguiendo semver.

    Si se especifica --bump, incrementa la version segun el tipo:
    - major: Incrementa la version mayor (X.0.0) - cambios incompatibles
    - minor: Incrementa la version menor (0.X.0) - nueva funcionalidad compatible
    - patch: Incrementa la version de parche (0.0.X) - correcciones de bugs

    Si no se especifica --bump, muestra la version actual.

    Args:
        args: Argumentos parseados con 'connector_path', 'bump'

    Retorna:
        0 si la operacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    bump_type = getattr(args, "BUMP", None)

    current_version = _read_version(connector_path)
    if current_version is None:
        print(f"Error: No se pudo determinar la version del conector en {connector_path}", file=sys.stderr)
        return 1

    if bump_type is None:
        print(f"Conector: {connector_path.name}")
        print(f"Version actual: {current_version}")
        return 0

    new_version = _bump_version(current_version, bump_type)
    if new_version is None:
        print(f"Error: No se pudo calcular la nueva version. Version actual: {current_version}", file=sys.stderr)
        return 1

    updated_files = _update_version_in_files(connector_path, current_version, new_version)

    print(f"Version actualizada: {current_version} -> {new_version}")
    print(f"Bump: {bump_type}")
    print()
    print("Archivos actualizados:")
    for filepath in updated_files:
        print(f"  - {filepath}")

    return 0


def x_cmd_version__mutmut_11(args: argparse.Namespace) -> int:
    """
    Gestiona la version de un conector siguiendo semver.

    Si se especifica --bump, incrementa la version segun el tipo:
    - major: Incrementa la version mayor (X.0.0) - cambios incompatibles
    - minor: Incrementa la version menor (0.X.0) - nueva funcionalidad compatible
    - patch: Incrementa la version de parche (0.0.X) - correcciones de bugs

    Si no se especifica --bump, muestra la version actual.

    Args:
        args: Argumentos parseados con 'connector_path', 'bump'

    Retorna:
        0 si la operacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    bump_type = getattr(args, "bump", None)

    current_version = None
    if current_version is None:
        print(f"Error: No se pudo determinar la version del conector en {connector_path}", file=sys.stderr)
        return 1

    if bump_type is None:
        print(f"Conector: {connector_path.name}")
        print(f"Version actual: {current_version}")
        return 0

    new_version = _bump_version(current_version, bump_type)
    if new_version is None:
        print(f"Error: No se pudo calcular la nueva version. Version actual: {current_version}", file=sys.stderr)
        return 1

    updated_files = _update_version_in_files(connector_path, current_version, new_version)

    print(f"Version actualizada: {current_version} -> {new_version}")
    print(f"Bump: {bump_type}")
    print()
    print("Archivos actualizados:")
    for filepath in updated_files:
        print(f"  - {filepath}")

    return 0


def x_cmd_version__mutmut_12(args: argparse.Namespace) -> int:
    """
    Gestiona la version de un conector siguiendo semver.

    Si se especifica --bump, incrementa la version segun el tipo:
    - major: Incrementa la version mayor (X.0.0) - cambios incompatibles
    - minor: Incrementa la version menor (0.X.0) - nueva funcionalidad compatible
    - patch: Incrementa la version de parche (0.0.X) - correcciones de bugs

    Si no se especifica --bump, muestra la version actual.

    Args:
        args: Argumentos parseados con 'connector_path', 'bump'

    Retorna:
        0 si la operacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    bump_type = getattr(args, "bump", None)

    current_version = _read_version(None)
    if current_version is None:
        print(f"Error: No se pudo determinar la version del conector en {connector_path}", file=sys.stderr)
        return 1

    if bump_type is None:
        print(f"Conector: {connector_path.name}")
        print(f"Version actual: {current_version}")
        return 0

    new_version = _bump_version(current_version, bump_type)
    if new_version is None:
        print(f"Error: No se pudo calcular la nueva version. Version actual: {current_version}", file=sys.stderr)
        return 1

    updated_files = _update_version_in_files(connector_path, current_version, new_version)

    print(f"Version actualizada: {current_version} -> {new_version}")
    print(f"Bump: {bump_type}")
    print()
    print("Archivos actualizados:")
    for filepath in updated_files:
        print(f"  - {filepath}")

    return 0


def x_cmd_version__mutmut_13(args: argparse.Namespace) -> int:
    """
    Gestiona la version de un conector siguiendo semver.

    Si se especifica --bump, incrementa la version segun el tipo:
    - major: Incrementa la version mayor (X.0.0) - cambios incompatibles
    - minor: Incrementa la version menor (0.X.0) - nueva funcionalidad compatible
    - patch: Incrementa la version de parche (0.0.X) - correcciones de bugs

    Si no se especifica --bump, muestra la version actual.

    Args:
        args: Argumentos parseados con 'connector_path', 'bump'

    Retorna:
        0 si la operacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    bump_type = getattr(args, "bump", None)

    current_version = _read_version(connector_path)
    if current_version is not None:
        print(f"Error: No se pudo determinar la version del conector en {connector_path}", file=sys.stderr)
        return 1

    if bump_type is None:
        print(f"Conector: {connector_path.name}")
        print(f"Version actual: {current_version}")
        return 0

    new_version = _bump_version(current_version, bump_type)
    if new_version is None:
        print(f"Error: No se pudo calcular la nueva version. Version actual: {current_version}", file=sys.stderr)
        return 1

    updated_files = _update_version_in_files(connector_path, current_version, new_version)

    print(f"Version actualizada: {current_version} -> {new_version}")
    print(f"Bump: {bump_type}")
    print()
    print("Archivos actualizados:")
    for filepath in updated_files:
        print(f"  - {filepath}")

    return 0


def x_cmd_version__mutmut_14(args: argparse.Namespace) -> int:
    """
    Gestiona la version de un conector siguiendo semver.

    Si se especifica --bump, incrementa la version segun el tipo:
    - major: Incrementa la version mayor (X.0.0) - cambios incompatibles
    - minor: Incrementa la version menor (0.X.0) - nueva funcionalidad compatible
    - patch: Incrementa la version de parche (0.0.X) - correcciones de bugs

    Si no se especifica --bump, muestra la version actual.

    Args:
        args: Argumentos parseados con 'connector_path', 'bump'

    Retorna:
        0 si la operacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    bump_type = getattr(args, "bump", None)

    current_version = _read_version(connector_path)
    if current_version is None:
        print(None, file=sys.stderr)
        return 1

    if bump_type is None:
        print(f"Conector: {connector_path.name}")
        print(f"Version actual: {current_version}")
        return 0

    new_version = _bump_version(current_version, bump_type)
    if new_version is None:
        print(f"Error: No se pudo calcular la nueva version. Version actual: {current_version}", file=sys.stderr)
        return 1

    updated_files = _update_version_in_files(connector_path, current_version, new_version)

    print(f"Version actualizada: {current_version} -> {new_version}")
    print(f"Bump: {bump_type}")
    print()
    print("Archivos actualizados:")
    for filepath in updated_files:
        print(f"  - {filepath}")

    return 0


def x_cmd_version__mutmut_15(args: argparse.Namespace) -> int:
    """
    Gestiona la version de un conector siguiendo semver.

    Si se especifica --bump, incrementa la version segun el tipo:
    - major: Incrementa la version mayor (X.0.0) - cambios incompatibles
    - minor: Incrementa la version menor (0.X.0) - nueva funcionalidad compatible
    - patch: Incrementa la version de parche (0.0.X) - correcciones de bugs

    Si no se especifica --bump, muestra la version actual.

    Args:
        args: Argumentos parseados con 'connector_path', 'bump'

    Retorna:
        0 si la operacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    bump_type = getattr(args, "bump", None)

    current_version = _read_version(connector_path)
    if current_version is None:
        print(f"Error: No se pudo determinar la version del conector en {connector_path}", file=None)
        return 1

    if bump_type is None:
        print(f"Conector: {connector_path.name}")
        print(f"Version actual: {current_version}")
        return 0

    new_version = _bump_version(current_version, bump_type)
    if new_version is None:
        print(f"Error: No se pudo calcular la nueva version. Version actual: {current_version}", file=sys.stderr)
        return 1

    updated_files = _update_version_in_files(connector_path, current_version, new_version)

    print(f"Version actualizada: {current_version} -> {new_version}")
    print(f"Bump: {bump_type}")
    print()
    print("Archivos actualizados:")
    for filepath in updated_files:
        print(f"  - {filepath}")

    return 0


def x_cmd_version__mutmut_16(args: argparse.Namespace) -> int:
    """
    Gestiona la version de un conector siguiendo semver.

    Si se especifica --bump, incrementa la version segun el tipo:
    - major: Incrementa la version mayor (X.0.0) - cambios incompatibles
    - minor: Incrementa la version menor (0.X.0) - nueva funcionalidad compatible
    - patch: Incrementa la version de parche (0.0.X) - correcciones de bugs

    Si no se especifica --bump, muestra la version actual.

    Args:
        args: Argumentos parseados con 'connector_path', 'bump'

    Retorna:
        0 si la operacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    bump_type = getattr(args, "bump", None)

    current_version = _read_version(connector_path)
    if current_version is None:
        print(file=sys.stderr)
        return 1

    if bump_type is None:
        print(f"Conector: {connector_path.name}")
        print(f"Version actual: {current_version}")
        return 0

    new_version = _bump_version(current_version, bump_type)
    if new_version is None:
        print(f"Error: No se pudo calcular la nueva version. Version actual: {current_version}", file=sys.stderr)
        return 1

    updated_files = _update_version_in_files(connector_path, current_version, new_version)

    print(f"Version actualizada: {current_version} -> {new_version}")
    print(f"Bump: {bump_type}")
    print()
    print("Archivos actualizados:")
    for filepath in updated_files:
        print(f"  - {filepath}")

    return 0


def x_cmd_version__mutmut_17(args: argparse.Namespace) -> int:
    """
    Gestiona la version de un conector siguiendo semver.

    Si se especifica --bump, incrementa la version segun el tipo:
    - major: Incrementa la version mayor (X.0.0) - cambios incompatibles
    - minor: Incrementa la version menor (0.X.0) - nueva funcionalidad compatible
    - patch: Incrementa la version de parche (0.0.X) - correcciones de bugs

    Si no se especifica --bump, muestra la version actual.

    Args:
        args: Argumentos parseados con 'connector_path', 'bump'

    Retorna:
        0 si la operacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    bump_type = getattr(args, "bump", None)

    current_version = _read_version(connector_path)
    if current_version is None:
        print(f"Error: No se pudo determinar la version del conector en {connector_path}", )
        return 1

    if bump_type is None:
        print(f"Conector: {connector_path.name}")
        print(f"Version actual: {current_version}")
        return 0

    new_version = _bump_version(current_version, bump_type)
    if new_version is None:
        print(f"Error: No se pudo calcular la nueva version. Version actual: {current_version}", file=sys.stderr)
        return 1

    updated_files = _update_version_in_files(connector_path, current_version, new_version)

    print(f"Version actualizada: {current_version} -> {new_version}")
    print(f"Bump: {bump_type}")
    print()
    print("Archivos actualizados:")
    for filepath in updated_files:
        print(f"  - {filepath}")

    return 0


def x_cmd_version__mutmut_18(args: argparse.Namespace) -> int:
    """
    Gestiona la version de un conector siguiendo semver.

    Si se especifica --bump, incrementa la version segun el tipo:
    - major: Incrementa la version mayor (X.0.0) - cambios incompatibles
    - minor: Incrementa la version menor (0.X.0) - nueva funcionalidad compatible
    - patch: Incrementa la version de parche (0.0.X) - correcciones de bugs

    Si no se especifica --bump, muestra la version actual.

    Args:
        args: Argumentos parseados con 'connector_path', 'bump'

    Retorna:
        0 si la operacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    bump_type = getattr(args, "bump", None)

    current_version = _read_version(connector_path)
    if current_version is None:
        print(f"Error: No se pudo determinar la version del conector en {connector_path}", file=sys.stderr)
        return 2

    if bump_type is None:
        print(f"Conector: {connector_path.name}")
        print(f"Version actual: {current_version}")
        return 0

    new_version = _bump_version(current_version, bump_type)
    if new_version is None:
        print(f"Error: No se pudo calcular la nueva version. Version actual: {current_version}", file=sys.stderr)
        return 1

    updated_files = _update_version_in_files(connector_path, current_version, new_version)

    print(f"Version actualizada: {current_version} -> {new_version}")
    print(f"Bump: {bump_type}")
    print()
    print("Archivos actualizados:")
    for filepath in updated_files:
        print(f"  - {filepath}")

    return 0


def x_cmd_version__mutmut_19(args: argparse.Namespace) -> int:
    """
    Gestiona la version de un conector siguiendo semver.

    Si se especifica --bump, incrementa la version segun el tipo:
    - major: Incrementa la version mayor (X.0.0) - cambios incompatibles
    - minor: Incrementa la version menor (0.X.0) - nueva funcionalidad compatible
    - patch: Incrementa la version de parche (0.0.X) - correcciones de bugs

    Si no se especifica --bump, muestra la version actual.

    Args:
        args: Argumentos parseados con 'connector_path', 'bump'

    Retorna:
        0 si la operacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    bump_type = getattr(args, "bump", None)

    current_version = _read_version(connector_path)
    if current_version is None:
        print(f"Error: No se pudo determinar la version del conector en {connector_path}", file=sys.stderr)
        return 1

    if bump_type is not None:
        print(f"Conector: {connector_path.name}")
        print(f"Version actual: {current_version}")
        return 0

    new_version = _bump_version(current_version, bump_type)
    if new_version is None:
        print(f"Error: No se pudo calcular la nueva version. Version actual: {current_version}", file=sys.stderr)
        return 1

    updated_files = _update_version_in_files(connector_path, current_version, new_version)

    print(f"Version actualizada: {current_version} -> {new_version}")
    print(f"Bump: {bump_type}")
    print()
    print("Archivos actualizados:")
    for filepath in updated_files:
        print(f"  - {filepath}")

    return 0


def x_cmd_version__mutmut_20(args: argparse.Namespace) -> int:
    """
    Gestiona la version de un conector siguiendo semver.

    Si se especifica --bump, incrementa la version segun el tipo:
    - major: Incrementa la version mayor (X.0.0) - cambios incompatibles
    - minor: Incrementa la version menor (0.X.0) - nueva funcionalidad compatible
    - patch: Incrementa la version de parche (0.0.X) - correcciones de bugs

    Si no se especifica --bump, muestra la version actual.

    Args:
        args: Argumentos parseados con 'connector_path', 'bump'

    Retorna:
        0 si la operacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    bump_type = getattr(args, "bump", None)

    current_version = _read_version(connector_path)
    if current_version is None:
        print(f"Error: No se pudo determinar la version del conector en {connector_path}", file=sys.stderr)
        return 1

    if bump_type is None:
        print(None)
        print(f"Version actual: {current_version}")
        return 0

    new_version = _bump_version(current_version, bump_type)
    if new_version is None:
        print(f"Error: No se pudo calcular la nueva version. Version actual: {current_version}", file=sys.stderr)
        return 1

    updated_files = _update_version_in_files(connector_path, current_version, new_version)

    print(f"Version actualizada: {current_version} -> {new_version}")
    print(f"Bump: {bump_type}")
    print()
    print("Archivos actualizados:")
    for filepath in updated_files:
        print(f"  - {filepath}")

    return 0


def x_cmd_version__mutmut_21(args: argparse.Namespace) -> int:
    """
    Gestiona la version de un conector siguiendo semver.

    Si se especifica --bump, incrementa la version segun el tipo:
    - major: Incrementa la version mayor (X.0.0) - cambios incompatibles
    - minor: Incrementa la version menor (0.X.0) - nueva funcionalidad compatible
    - patch: Incrementa la version de parche (0.0.X) - correcciones de bugs

    Si no se especifica --bump, muestra la version actual.

    Args:
        args: Argumentos parseados con 'connector_path', 'bump'

    Retorna:
        0 si la operacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    bump_type = getattr(args, "bump", None)

    current_version = _read_version(connector_path)
    if current_version is None:
        print(f"Error: No se pudo determinar la version del conector en {connector_path}", file=sys.stderr)
        return 1

    if bump_type is None:
        print(f"Conector: {connector_path.name}")
        print(None)
        return 0

    new_version = _bump_version(current_version, bump_type)
    if new_version is None:
        print(f"Error: No se pudo calcular la nueva version. Version actual: {current_version}", file=sys.stderr)
        return 1

    updated_files = _update_version_in_files(connector_path, current_version, new_version)

    print(f"Version actualizada: {current_version} -> {new_version}")
    print(f"Bump: {bump_type}")
    print()
    print("Archivos actualizados:")
    for filepath in updated_files:
        print(f"  - {filepath}")

    return 0


def x_cmd_version__mutmut_22(args: argparse.Namespace) -> int:
    """
    Gestiona la version de un conector siguiendo semver.

    Si se especifica --bump, incrementa la version segun el tipo:
    - major: Incrementa la version mayor (X.0.0) - cambios incompatibles
    - minor: Incrementa la version menor (0.X.0) - nueva funcionalidad compatible
    - patch: Incrementa la version de parche (0.0.X) - correcciones de bugs

    Si no se especifica --bump, muestra la version actual.

    Args:
        args: Argumentos parseados con 'connector_path', 'bump'

    Retorna:
        0 si la operacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    bump_type = getattr(args, "bump", None)

    current_version = _read_version(connector_path)
    if current_version is None:
        print(f"Error: No se pudo determinar la version del conector en {connector_path}", file=sys.stderr)
        return 1

    if bump_type is None:
        print(f"Conector: {connector_path.name}")
        print(f"Version actual: {current_version}")
        return 1

    new_version = _bump_version(current_version, bump_type)
    if new_version is None:
        print(f"Error: No se pudo calcular la nueva version. Version actual: {current_version}", file=sys.stderr)
        return 1

    updated_files = _update_version_in_files(connector_path, current_version, new_version)

    print(f"Version actualizada: {current_version} -> {new_version}")
    print(f"Bump: {bump_type}")
    print()
    print("Archivos actualizados:")
    for filepath in updated_files:
        print(f"  - {filepath}")

    return 0


def x_cmd_version__mutmut_23(args: argparse.Namespace) -> int:
    """
    Gestiona la version de un conector siguiendo semver.

    Si se especifica --bump, incrementa la version segun el tipo:
    - major: Incrementa la version mayor (X.0.0) - cambios incompatibles
    - minor: Incrementa la version menor (0.X.0) - nueva funcionalidad compatible
    - patch: Incrementa la version de parche (0.0.X) - correcciones de bugs

    Si no se especifica --bump, muestra la version actual.

    Args:
        args: Argumentos parseados con 'connector_path', 'bump'

    Retorna:
        0 si la operacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    bump_type = getattr(args, "bump", None)

    current_version = _read_version(connector_path)
    if current_version is None:
        print(f"Error: No se pudo determinar la version del conector en {connector_path}", file=sys.stderr)
        return 1

    if bump_type is None:
        print(f"Conector: {connector_path.name}")
        print(f"Version actual: {current_version}")
        return 0

    new_version = None
    if new_version is None:
        print(f"Error: No se pudo calcular la nueva version. Version actual: {current_version}", file=sys.stderr)
        return 1

    updated_files = _update_version_in_files(connector_path, current_version, new_version)

    print(f"Version actualizada: {current_version} -> {new_version}")
    print(f"Bump: {bump_type}")
    print()
    print("Archivos actualizados:")
    for filepath in updated_files:
        print(f"  - {filepath}")

    return 0


def x_cmd_version__mutmut_24(args: argparse.Namespace) -> int:
    """
    Gestiona la version de un conector siguiendo semver.

    Si se especifica --bump, incrementa la version segun el tipo:
    - major: Incrementa la version mayor (X.0.0) - cambios incompatibles
    - minor: Incrementa la version menor (0.X.0) - nueva funcionalidad compatible
    - patch: Incrementa la version de parche (0.0.X) - correcciones de bugs

    Si no se especifica --bump, muestra la version actual.

    Args:
        args: Argumentos parseados con 'connector_path', 'bump'

    Retorna:
        0 si la operacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    bump_type = getattr(args, "bump", None)

    current_version = _read_version(connector_path)
    if current_version is None:
        print(f"Error: No se pudo determinar la version del conector en {connector_path}", file=sys.stderr)
        return 1

    if bump_type is None:
        print(f"Conector: {connector_path.name}")
        print(f"Version actual: {current_version}")
        return 0

    new_version = _bump_version(None, bump_type)
    if new_version is None:
        print(f"Error: No se pudo calcular la nueva version. Version actual: {current_version}", file=sys.stderr)
        return 1

    updated_files = _update_version_in_files(connector_path, current_version, new_version)

    print(f"Version actualizada: {current_version} -> {new_version}")
    print(f"Bump: {bump_type}")
    print()
    print("Archivos actualizados:")
    for filepath in updated_files:
        print(f"  - {filepath}")

    return 0


def x_cmd_version__mutmut_25(args: argparse.Namespace) -> int:
    """
    Gestiona la version de un conector siguiendo semver.

    Si se especifica --bump, incrementa la version segun el tipo:
    - major: Incrementa la version mayor (X.0.0) - cambios incompatibles
    - minor: Incrementa la version menor (0.X.0) - nueva funcionalidad compatible
    - patch: Incrementa la version de parche (0.0.X) - correcciones de bugs

    Si no se especifica --bump, muestra la version actual.

    Args:
        args: Argumentos parseados con 'connector_path', 'bump'

    Retorna:
        0 si la operacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    bump_type = getattr(args, "bump", None)

    current_version = _read_version(connector_path)
    if current_version is None:
        print(f"Error: No se pudo determinar la version del conector en {connector_path}", file=sys.stderr)
        return 1

    if bump_type is None:
        print(f"Conector: {connector_path.name}")
        print(f"Version actual: {current_version}")
        return 0

    new_version = _bump_version(current_version, None)
    if new_version is None:
        print(f"Error: No se pudo calcular la nueva version. Version actual: {current_version}", file=sys.stderr)
        return 1

    updated_files = _update_version_in_files(connector_path, current_version, new_version)

    print(f"Version actualizada: {current_version} -> {new_version}")
    print(f"Bump: {bump_type}")
    print()
    print("Archivos actualizados:")
    for filepath in updated_files:
        print(f"  - {filepath}")

    return 0


def x_cmd_version__mutmut_26(args: argparse.Namespace) -> int:
    """
    Gestiona la version de un conector siguiendo semver.

    Si se especifica --bump, incrementa la version segun el tipo:
    - major: Incrementa la version mayor (X.0.0) - cambios incompatibles
    - minor: Incrementa la version menor (0.X.0) - nueva funcionalidad compatible
    - patch: Incrementa la version de parche (0.0.X) - correcciones de bugs

    Si no se especifica --bump, muestra la version actual.

    Args:
        args: Argumentos parseados con 'connector_path', 'bump'

    Retorna:
        0 si la operacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    bump_type = getattr(args, "bump", None)

    current_version = _read_version(connector_path)
    if current_version is None:
        print(f"Error: No se pudo determinar la version del conector en {connector_path}", file=sys.stderr)
        return 1

    if bump_type is None:
        print(f"Conector: {connector_path.name}")
        print(f"Version actual: {current_version}")
        return 0

    new_version = _bump_version(bump_type)
    if new_version is None:
        print(f"Error: No se pudo calcular la nueva version. Version actual: {current_version}", file=sys.stderr)
        return 1

    updated_files = _update_version_in_files(connector_path, current_version, new_version)

    print(f"Version actualizada: {current_version} -> {new_version}")
    print(f"Bump: {bump_type}")
    print()
    print("Archivos actualizados:")
    for filepath in updated_files:
        print(f"  - {filepath}")

    return 0


def x_cmd_version__mutmut_27(args: argparse.Namespace) -> int:
    """
    Gestiona la version de un conector siguiendo semver.

    Si se especifica --bump, incrementa la version segun el tipo:
    - major: Incrementa la version mayor (X.0.0) - cambios incompatibles
    - minor: Incrementa la version menor (0.X.0) - nueva funcionalidad compatible
    - patch: Incrementa la version de parche (0.0.X) - correcciones de bugs

    Si no se especifica --bump, muestra la version actual.

    Args:
        args: Argumentos parseados con 'connector_path', 'bump'

    Retorna:
        0 si la operacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    bump_type = getattr(args, "bump", None)

    current_version = _read_version(connector_path)
    if current_version is None:
        print(f"Error: No se pudo determinar la version del conector en {connector_path}", file=sys.stderr)
        return 1

    if bump_type is None:
        print(f"Conector: {connector_path.name}")
        print(f"Version actual: {current_version}")
        return 0

    new_version = _bump_version(current_version, )
    if new_version is None:
        print(f"Error: No se pudo calcular la nueva version. Version actual: {current_version}", file=sys.stderr)
        return 1

    updated_files = _update_version_in_files(connector_path, current_version, new_version)

    print(f"Version actualizada: {current_version} -> {new_version}")
    print(f"Bump: {bump_type}")
    print()
    print("Archivos actualizados:")
    for filepath in updated_files:
        print(f"  - {filepath}")

    return 0


def x_cmd_version__mutmut_28(args: argparse.Namespace) -> int:
    """
    Gestiona la version de un conector siguiendo semver.

    Si se especifica --bump, incrementa la version segun el tipo:
    - major: Incrementa la version mayor (X.0.0) - cambios incompatibles
    - minor: Incrementa la version menor (0.X.0) - nueva funcionalidad compatible
    - patch: Incrementa la version de parche (0.0.X) - correcciones de bugs

    Si no se especifica --bump, muestra la version actual.

    Args:
        args: Argumentos parseados con 'connector_path', 'bump'

    Retorna:
        0 si la operacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    bump_type = getattr(args, "bump", None)

    current_version = _read_version(connector_path)
    if current_version is None:
        print(f"Error: No se pudo determinar la version del conector en {connector_path}", file=sys.stderr)
        return 1

    if bump_type is None:
        print(f"Conector: {connector_path.name}")
        print(f"Version actual: {current_version}")
        return 0

    new_version = _bump_version(current_version, bump_type)
    if new_version is not None:
        print(f"Error: No se pudo calcular la nueva version. Version actual: {current_version}", file=sys.stderr)
        return 1

    updated_files = _update_version_in_files(connector_path, current_version, new_version)

    print(f"Version actualizada: {current_version} -> {new_version}")
    print(f"Bump: {bump_type}")
    print()
    print("Archivos actualizados:")
    for filepath in updated_files:
        print(f"  - {filepath}")

    return 0


def x_cmd_version__mutmut_29(args: argparse.Namespace) -> int:
    """
    Gestiona la version de un conector siguiendo semver.

    Si se especifica --bump, incrementa la version segun el tipo:
    - major: Incrementa la version mayor (X.0.0) - cambios incompatibles
    - minor: Incrementa la version menor (0.X.0) - nueva funcionalidad compatible
    - patch: Incrementa la version de parche (0.0.X) - correcciones de bugs

    Si no se especifica --bump, muestra la version actual.

    Args:
        args: Argumentos parseados con 'connector_path', 'bump'

    Retorna:
        0 si la operacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    bump_type = getattr(args, "bump", None)

    current_version = _read_version(connector_path)
    if current_version is None:
        print(f"Error: No se pudo determinar la version del conector en {connector_path}", file=sys.stderr)
        return 1

    if bump_type is None:
        print(f"Conector: {connector_path.name}")
        print(f"Version actual: {current_version}")
        return 0

    new_version = _bump_version(current_version, bump_type)
    if new_version is None:
        print(None, file=sys.stderr)
        return 1

    updated_files = _update_version_in_files(connector_path, current_version, new_version)

    print(f"Version actualizada: {current_version} -> {new_version}")
    print(f"Bump: {bump_type}")
    print()
    print("Archivos actualizados:")
    for filepath in updated_files:
        print(f"  - {filepath}")

    return 0


def x_cmd_version__mutmut_30(args: argparse.Namespace) -> int:
    """
    Gestiona la version de un conector siguiendo semver.

    Si se especifica --bump, incrementa la version segun el tipo:
    - major: Incrementa la version mayor (X.0.0) - cambios incompatibles
    - minor: Incrementa la version menor (0.X.0) - nueva funcionalidad compatible
    - patch: Incrementa la version de parche (0.0.X) - correcciones de bugs

    Si no se especifica --bump, muestra la version actual.

    Args:
        args: Argumentos parseados con 'connector_path', 'bump'

    Retorna:
        0 si la operacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    bump_type = getattr(args, "bump", None)

    current_version = _read_version(connector_path)
    if current_version is None:
        print(f"Error: No se pudo determinar la version del conector en {connector_path}", file=sys.stderr)
        return 1

    if bump_type is None:
        print(f"Conector: {connector_path.name}")
        print(f"Version actual: {current_version}")
        return 0

    new_version = _bump_version(current_version, bump_type)
    if new_version is None:
        print(f"Error: No se pudo calcular la nueva version. Version actual: {current_version}", file=None)
        return 1

    updated_files = _update_version_in_files(connector_path, current_version, new_version)

    print(f"Version actualizada: {current_version} -> {new_version}")
    print(f"Bump: {bump_type}")
    print()
    print("Archivos actualizados:")
    for filepath in updated_files:
        print(f"  - {filepath}")

    return 0


def x_cmd_version__mutmut_31(args: argparse.Namespace) -> int:
    """
    Gestiona la version de un conector siguiendo semver.

    Si se especifica --bump, incrementa la version segun el tipo:
    - major: Incrementa la version mayor (X.0.0) - cambios incompatibles
    - minor: Incrementa la version menor (0.X.0) - nueva funcionalidad compatible
    - patch: Incrementa la version de parche (0.0.X) - correcciones de bugs

    Si no se especifica --bump, muestra la version actual.

    Args:
        args: Argumentos parseados con 'connector_path', 'bump'

    Retorna:
        0 si la operacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    bump_type = getattr(args, "bump", None)

    current_version = _read_version(connector_path)
    if current_version is None:
        print(f"Error: No se pudo determinar la version del conector en {connector_path}", file=sys.stderr)
        return 1

    if bump_type is None:
        print(f"Conector: {connector_path.name}")
        print(f"Version actual: {current_version}")
        return 0

    new_version = _bump_version(current_version, bump_type)
    if new_version is None:
        print(file=sys.stderr)
        return 1

    updated_files = _update_version_in_files(connector_path, current_version, new_version)

    print(f"Version actualizada: {current_version} -> {new_version}")
    print(f"Bump: {bump_type}")
    print()
    print("Archivos actualizados:")
    for filepath in updated_files:
        print(f"  - {filepath}")

    return 0


def x_cmd_version__mutmut_32(args: argparse.Namespace) -> int:
    """
    Gestiona la version de un conector siguiendo semver.

    Si se especifica --bump, incrementa la version segun el tipo:
    - major: Incrementa la version mayor (X.0.0) - cambios incompatibles
    - minor: Incrementa la version menor (0.X.0) - nueva funcionalidad compatible
    - patch: Incrementa la version de parche (0.0.X) - correcciones de bugs

    Si no se especifica --bump, muestra la version actual.

    Args:
        args: Argumentos parseados con 'connector_path', 'bump'

    Retorna:
        0 si la operacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    bump_type = getattr(args, "bump", None)

    current_version = _read_version(connector_path)
    if current_version is None:
        print(f"Error: No se pudo determinar la version del conector en {connector_path}", file=sys.stderr)
        return 1

    if bump_type is None:
        print(f"Conector: {connector_path.name}")
        print(f"Version actual: {current_version}")
        return 0

    new_version = _bump_version(current_version, bump_type)
    if new_version is None:
        print(f"Error: No se pudo calcular la nueva version. Version actual: {current_version}", )
        return 1

    updated_files = _update_version_in_files(connector_path, current_version, new_version)

    print(f"Version actualizada: {current_version} -> {new_version}")
    print(f"Bump: {bump_type}")
    print()
    print("Archivos actualizados:")
    for filepath in updated_files:
        print(f"  - {filepath}")

    return 0


def x_cmd_version__mutmut_33(args: argparse.Namespace) -> int:
    """
    Gestiona la version de un conector siguiendo semver.

    Si se especifica --bump, incrementa la version segun el tipo:
    - major: Incrementa la version mayor (X.0.0) - cambios incompatibles
    - minor: Incrementa la version menor (0.X.0) - nueva funcionalidad compatible
    - patch: Incrementa la version de parche (0.0.X) - correcciones de bugs

    Si no se especifica --bump, muestra la version actual.

    Args:
        args: Argumentos parseados con 'connector_path', 'bump'

    Retorna:
        0 si la operacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    bump_type = getattr(args, "bump", None)

    current_version = _read_version(connector_path)
    if current_version is None:
        print(f"Error: No se pudo determinar la version del conector en {connector_path}", file=sys.stderr)
        return 1

    if bump_type is None:
        print(f"Conector: {connector_path.name}")
        print(f"Version actual: {current_version}")
        return 0

    new_version = _bump_version(current_version, bump_type)
    if new_version is None:
        print(f"Error: No se pudo calcular la nueva version. Version actual: {current_version}", file=sys.stderr)
        return 2

    updated_files = _update_version_in_files(connector_path, current_version, new_version)

    print(f"Version actualizada: {current_version} -> {new_version}")
    print(f"Bump: {bump_type}")
    print()
    print("Archivos actualizados:")
    for filepath in updated_files:
        print(f"  - {filepath}")

    return 0


def x_cmd_version__mutmut_34(args: argparse.Namespace) -> int:
    """
    Gestiona la version de un conector siguiendo semver.

    Si se especifica --bump, incrementa la version segun el tipo:
    - major: Incrementa la version mayor (X.0.0) - cambios incompatibles
    - minor: Incrementa la version menor (0.X.0) - nueva funcionalidad compatible
    - patch: Incrementa la version de parche (0.0.X) - correcciones de bugs

    Si no se especifica --bump, muestra la version actual.

    Args:
        args: Argumentos parseados con 'connector_path', 'bump'

    Retorna:
        0 si la operacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    bump_type = getattr(args, "bump", None)

    current_version = _read_version(connector_path)
    if current_version is None:
        print(f"Error: No se pudo determinar la version del conector en {connector_path}", file=sys.stderr)
        return 1

    if bump_type is None:
        print(f"Conector: {connector_path.name}")
        print(f"Version actual: {current_version}")
        return 0

    new_version = _bump_version(current_version, bump_type)
    if new_version is None:
        print(f"Error: No se pudo calcular la nueva version. Version actual: {current_version}", file=sys.stderr)
        return 1

    updated_files = None

    print(f"Version actualizada: {current_version} -> {new_version}")
    print(f"Bump: {bump_type}")
    print()
    print("Archivos actualizados:")
    for filepath in updated_files:
        print(f"  - {filepath}")

    return 0


def x_cmd_version__mutmut_35(args: argparse.Namespace) -> int:
    """
    Gestiona la version de un conector siguiendo semver.

    Si se especifica --bump, incrementa la version segun el tipo:
    - major: Incrementa la version mayor (X.0.0) - cambios incompatibles
    - minor: Incrementa la version menor (0.X.0) - nueva funcionalidad compatible
    - patch: Incrementa la version de parche (0.0.X) - correcciones de bugs

    Si no se especifica --bump, muestra la version actual.

    Args:
        args: Argumentos parseados con 'connector_path', 'bump'

    Retorna:
        0 si la operacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    bump_type = getattr(args, "bump", None)

    current_version = _read_version(connector_path)
    if current_version is None:
        print(f"Error: No se pudo determinar la version del conector en {connector_path}", file=sys.stderr)
        return 1

    if bump_type is None:
        print(f"Conector: {connector_path.name}")
        print(f"Version actual: {current_version}")
        return 0

    new_version = _bump_version(current_version, bump_type)
    if new_version is None:
        print(f"Error: No se pudo calcular la nueva version. Version actual: {current_version}", file=sys.stderr)
        return 1

    updated_files = _update_version_in_files(None, current_version, new_version)

    print(f"Version actualizada: {current_version} -> {new_version}")
    print(f"Bump: {bump_type}")
    print()
    print("Archivos actualizados:")
    for filepath in updated_files:
        print(f"  - {filepath}")

    return 0


def x_cmd_version__mutmut_36(args: argparse.Namespace) -> int:
    """
    Gestiona la version de un conector siguiendo semver.

    Si se especifica --bump, incrementa la version segun el tipo:
    - major: Incrementa la version mayor (X.0.0) - cambios incompatibles
    - minor: Incrementa la version menor (0.X.0) - nueva funcionalidad compatible
    - patch: Incrementa la version de parche (0.0.X) - correcciones de bugs

    Si no se especifica --bump, muestra la version actual.

    Args:
        args: Argumentos parseados con 'connector_path', 'bump'

    Retorna:
        0 si la operacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    bump_type = getattr(args, "bump", None)

    current_version = _read_version(connector_path)
    if current_version is None:
        print(f"Error: No se pudo determinar la version del conector en {connector_path}", file=sys.stderr)
        return 1

    if bump_type is None:
        print(f"Conector: {connector_path.name}")
        print(f"Version actual: {current_version}")
        return 0

    new_version = _bump_version(current_version, bump_type)
    if new_version is None:
        print(f"Error: No se pudo calcular la nueva version. Version actual: {current_version}", file=sys.stderr)
        return 1

    updated_files = _update_version_in_files(connector_path, None, new_version)

    print(f"Version actualizada: {current_version} -> {new_version}")
    print(f"Bump: {bump_type}")
    print()
    print("Archivos actualizados:")
    for filepath in updated_files:
        print(f"  - {filepath}")

    return 0


def x_cmd_version__mutmut_37(args: argparse.Namespace) -> int:
    """
    Gestiona la version de un conector siguiendo semver.

    Si se especifica --bump, incrementa la version segun el tipo:
    - major: Incrementa la version mayor (X.0.0) - cambios incompatibles
    - minor: Incrementa la version menor (0.X.0) - nueva funcionalidad compatible
    - patch: Incrementa la version de parche (0.0.X) - correcciones de bugs

    Si no se especifica --bump, muestra la version actual.

    Args:
        args: Argumentos parseados con 'connector_path', 'bump'

    Retorna:
        0 si la operacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    bump_type = getattr(args, "bump", None)

    current_version = _read_version(connector_path)
    if current_version is None:
        print(f"Error: No se pudo determinar la version del conector en {connector_path}", file=sys.stderr)
        return 1

    if bump_type is None:
        print(f"Conector: {connector_path.name}")
        print(f"Version actual: {current_version}")
        return 0

    new_version = _bump_version(current_version, bump_type)
    if new_version is None:
        print(f"Error: No se pudo calcular la nueva version. Version actual: {current_version}", file=sys.stderr)
        return 1

    updated_files = _update_version_in_files(connector_path, current_version, None)

    print(f"Version actualizada: {current_version} -> {new_version}")
    print(f"Bump: {bump_type}")
    print()
    print("Archivos actualizados:")
    for filepath in updated_files:
        print(f"  - {filepath}")

    return 0


def x_cmd_version__mutmut_38(args: argparse.Namespace) -> int:
    """
    Gestiona la version de un conector siguiendo semver.

    Si se especifica --bump, incrementa la version segun el tipo:
    - major: Incrementa la version mayor (X.0.0) - cambios incompatibles
    - minor: Incrementa la version menor (0.X.0) - nueva funcionalidad compatible
    - patch: Incrementa la version de parche (0.0.X) - correcciones de bugs

    Si no se especifica --bump, muestra la version actual.

    Args:
        args: Argumentos parseados con 'connector_path', 'bump'

    Retorna:
        0 si la operacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    bump_type = getattr(args, "bump", None)

    current_version = _read_version(connector_path)
    if current_version is None:
        print(f"Error: No se pudo determinar la version del conector en {connector_path}", file=sys.stderr)
        return 1

    if bump_type is None:
        print(f"Conector: {connector_path.name}")
        print(f"Version actual: {current_version}")
        return 0

    new_version = _bump_version(current_version, bump_type)
    if new_version is None:
        print(f"Error: No se pudo calcular la nueva version. Version actual: {current_version}", file=sys.stderr)
        return 1

    updated_files = _update_version_in_files(current_version, new_version)

    print(f"Version actualizada: {current_version} -> {new_version}")
    print(f"Bump: {bump_type}")
    print()
    print("Archivos actualizados:")
    for filepath in updated_files:
        print(f"  - {filepath}")

    return 0


def x_cmd_version__mutmut_39(args: argparse.Namespace) -> int:
    """
    Gestiona la version de un conector siguiendo semver.

    Si se especifica --bump, incrementa la version segun el tipo:
    - major: Incrementa la version mayor (X.0.0) - cambios incompatibles
    - minor: Incrementa la version menor (0.X.0) - nueva funcionalidad compatible
    - patch: Incrementa la version de parche (0.0.X) - correcciones de bugs

    Si no se especifica --bump, muestra la version actual.

    Args:
        args: Argumentos parseados con 'connector_path', 'bump'

    Retorna:
        0 si la operacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    bump_type = getattr(args, "bump", None)

    current_version = _read_version(connector_path)
    if current_version is None:
        print(f"Error: No se pudo determinar la version del conector en {connector_path}", file=sys.stderr)
        return 1

    if bump_type is None:
        print(f"Conector: {connector_path.name}")
        print(f"Version actual: {current_version}")
        return 0

    new_version = _bump_version(current_version, bump_type)
    if new_version is None:
        print(f"Error: No se pudo calcular la nueva version. Version actual: {current_version}", file=sys.stderr)
        return 1

    updated_files = _update_version_in_files(connector_path, new_version)

    print(f"Version actualizada: {current_version} -> {new_version}")
    print(f"Bump: {bump_type}")
    print()
    print("Archivos actualizados:")
    for filepath in updated_files:
        print(f"  - {filepath}")

    return 0


def x_cmd_version__mutmut_40(args: argparse.Namespace) -> int:
    """
    Gestiona la version de un conector siguiendo semver.

    Si se especifica --bump, incrementa la version segun el tipo:
    - major: Incrementa la version mayor (X.0.0) - cambios incompatibles
    - minor: Incrementa la version menor (0.X.0) - nueva funcionalidad compatible
    - patch: Incrementa la version de parche (0.0.X) - correcciones de bugs

    Si no se especifica --bump, muestra la version actual.

    Args:
        args: Argumentos parseados con 'connector_path', 'bump'

    Retorna:
        0 si la operacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    bump_type = getattr(args, "bump", None)

    current_version = _read_version(connector_path)
    if current_version is None:
        print(f"Error: No se pudo determinar la version del conector en {connector_path}", file=sys.stderr)
        return 1

    if bump_type is None:
        print(f"Conector: {connector_path.name}")
        print(f"Version actual: {current_version}")
        return 0

    new_version = _bump_version(current_version, bump_type)
    if new_version is None:
        print(f"Error: No se pudo calcular la nueva version. Version actual: {current_version}", file=sys.stderr)
        return 1

    updated_files = _update_version_in_files(connector_path, current_version, )

    print(f"Version actualizada: {current_version} -> {new_version}")
    print(f"Bump: {bump_type}")
    print()
    print("Archivos actualizados:")
    for filepath in updated_files:
        print(f"  - {filepath}")

    return 0


def x_cmd_version__mutmut_41(args: argparse.Namespace) -> int:
    """
    Gestiona la version de un conector siguiendo semver.

    Si se especifica --bump, incrementa la version segun el tipo:
    - major: Incrementa la version mayor (X.0.0) - cambios incompatibles
    - minor: Incrementa la version menor (0.X.0) - nueva funcionalidad compatible
    - patch: Incrementa la version de parche (0.0.X) - correcciones de bugs

    Si no se especifica --bump, muestra la version actual.

    Args:
        args: Argumentos parseados con 'connector_path', 'bump'

    Retorna:
        0 si la operacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    bump_type = getattr(args, "bump", None)

    current_version = _read_version(connector_path)
    if current_version is None:
        print(f"Error: No se pudo determinar la version del conector en {connector_path}", file=sys.stderr)
        return 1

    if bump_type is None:
        print(f"Conector: {connector_path.name}")
        print(f"Version actual: {current_version}")
        return 0

    new_version = _bump_version(current_version, bump_type)
    if new_version is None:
        print(f"Error: No se pudo calcular la nueva version. Version actual: {current_version}", file=sys.stderr)
        return 1

    updated_files = _update_version_in_files(connector_path, current_version, new_version)

    print(None)
    print(f"Bump: {bump_type}")
    print()
    print("Archivos actualizados:")
    for filepath in updated_files:
        print(f"  - {filepath}")

    return 0


def x_cmd_version__mutmut_42(args: argparse.Namespace) -> int:
    """
    Gestiona la version de un conector siguiendo semver.

    Si se especifica --bump, incrementa la version segun el tipo:
    - major: Incrementa la version mayor (X.0.0) - cambios incompatibles
    - minor: Incrementa la version menor (0.X.0) - nueva funcionalidad compatible
    - patch: Incrementa la version de parche (0.0.X) - correcciones de bugs

    Si no se especifica --bump, muestra la version actual.

    Args:
        args: Argumentos parseados con 'connector_path', 'bump'

    Retorna:
        0 si la operacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    bump_type = getattr(args, "bump", None)

    current_version = _read_version(connector_path)
    if current_version is None:
        print(f"Error: No se pudo determinar la version del conector en {connector_path}", file=sys.stderr)
        return 1

    if bump_type is None:
        print(f"Conector: {connector_path.name}")
        print(f"Version actual: {current_version}")
        return 0

    new_version = _bump_version(current_version, bump_type)
    if new_version is None:
        print(f"Error: No se pudo calcular la nueva version. Version actual: {current_version}", file=sys.stderr)
        return 1

    updated_files = _update_version_in_files(connector_path, current_version, new_version)

    print(f"Version actualizada: {current_version} -> {new_version}")
    print(None)
    print()
    print("Archivos actualizados:")
    for filepath in updated_files:
        print(f"  - {filepath}")

    return 0


def x_cmd_version__mutmut_43(args: argparse.Namespace) -> int:
    """
    Gestiona la version de un conector siguiendo semver.

    Si se especifica --bump, incrementa la version segun el tipo:
    - major: Incrementa la version mayor (X.0.0) - cambios incompatibles
    - minor: Incrementa la version menor (0.X.0) - nueva funcionalidad compatible
    - patch: Incrementa la version de parche (0.0.X) - correcciones de bugs

    Si no se especifica --bump, muestra la version actual.

    Args:
        args: Argumentos parseados con 'connector_path', 'bump'

    Retorna:
        0 si la operacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    bump_type = getattr(args, "bump", None)

    current_version = _read_version(connector_path)
    if current_version is None:
        print(f"Error: No se pudo determinar la version del conector en {connector_path}", file=sys.stderr)
        return 1

    if bump_type is None:
        print(f"Conector: {connector_path.name}")
        print(f"Version actual: {current_version}")
        return 0

    new_version = _bump_version(current_version, bump_type)
    if new_version is None:
        print(f"Error: No se pudo calcular la nueva version. Version actual: {current_version}", file=sys.stderr)
        return 1

    updated_files = _update_version_in_files(connector_path, current_version, new_version)

    print(f"Version actualizada: {current_version} -> {new_version}")
    print(f"Bump: {bump_type}")
    print()
    print(None)
    for filepath in updated_files:
        print(f"  - {filepath}")

    return 0


def x_cmd_version__mutmut_44(args: argparse.Namespace) -> int:
    """
    Gestiona la version de un conector siguiendo semver.

    Si se especifica --bump, incrementa la version segun el tipo:
    - major: Incrementa la version mayor (X.0.0) - cambios incompatibles
    - minor: Incrementa la version menor (0.X.0) - nueva funcionalidad compatible
    - patch: Incrementa la version de parche (0.0.X) - correcciones de bugs

    Si no se especifica --bump, muestra la version actual.

    Args:
        args: Argumentos parseados con 'connector_path', 'bump'

    Retorna:
        0 si la operacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    bump_type = getattr(args, "bump", None)

    current_version = _read_version(connector_path)
    if current_version is None:
        print(f"Error: No se pudo determinar la version del conector en {connector_path}", file=sys.stderr)
        return 1

    if bump_type is None:
        print(f"Conector: {connector_path.name}")
        print(f"Version actual: {current_version}")
        return 0

    new_version = _bump_version(current_version, bump_type)
    if new_version is None:
        print(f"Error: No se pudo calcular la nueva version. Version actual: {current_version}", file=sys.stderr)
        return 1

    updated_files = _update_version_in_files(connector_path, current_version, new_version)

    print(f"Version actualizada: {current_version} -> {new_version}")
    print(f"Bump: {bump_type}")
    print()
    print("XXArchivos actualizados:XX")
    for filepath in updated_files:
        print(f"  - {filepath}")

    return 0


def x_cmd_version__mutmut_45(args: argparse.Namespace) -> int:
    """
    Gestiona la version de un conector siguiendo semver.

    Si se especifica --bump, incrementa la version segun el tipo:
    - major: Incrementa la version mayor (X.0.0) - cambios incompatibles
    - minor: Incrementa la version menor (0.X.0) - nueva funcionalidad compatible
    - patch: Incrementa la version de parche (0.0.X) - correcciones de bugs

    Si no se especifica --bump, muestra la version actual.

    Args:
        args: Argumentos parseados con 'connector_path', 'bump'

    Retorna:
        0 si la operacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    bump_type = getattr(args, "bump", None)

    current_version = _read_version(connector_path)
    if current_version is None:
        print(f"Error: No se pudo determinar la version del conector en {connector_path}", file=sys.stderr)
        return 1

    if bump_type is None:
        print(f"Conector: {connector_path.name}")
        print(f"Version actual: {current_version}")
        return 0

    new_version = _bump_version(current_version, bump_type)
    if new_version is None:
        print(f"Error: No se pudo calcular la nueva version. Version actual: {current_version}", file=sys.stderr)
        return 1

    updated_files = _update_version_in_files(connector_path, current_version, new_version)

    print(f"Version actualizada: {current_version} -> {new_version}")
    print(f"Bump: {bump_type}")
    print()
    print("archivos actualizados:")
    for filepath in updated_files:
        print(f"  - {filepath}")

    return 0


def x_cmd_version__mutmut_46(args: argparse.Namespace) -> int:
    """
    Gestiona la version de un conector siguiendo semver.

    Si se especifica --bump, incrementa la version segun el tipo:
    - major: Incrementa la version mayor (X.0.0) - cambios incompatibles
    - minor: Incrementa la version menor (0.X.0) - nueva funcionalidad compatible
    - patch: Incrementa la version de parche (0.0.X) - correcciones de bugs

    Si no se especifica --bump, muestra la version actual.

    Args:
        args: Argumentos parseados con 'connector_path', 'bump'

    Retorna:
        0 si la operacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    bump_type = getattr(args, "bump", None)

    current_version = _read_version(connector_path)
    if current_version is None:
        print(f"Error: No se pudo determinar la version del conector en {connector_path}", file=sys.stderr)
        return 1

    if bump_type is None:
        print(f"Conector: {connector_path.name}")
        print(f"Version actual: {current_version}")
        return 0

    new_version = _bump_version(current_version, bump_type)
    if new_version is None:
        print(f"Error: No se pudo calcular la nueva version. Version actual: {current_version}", file=sys.stderr)
        return 1

    updated_files = _update_version_in_files(connector_path, current_version, new_version)

    print(f"Version actualizada: {current_version} -> {new_version}")
    print(f"Bump: {bump_type}")
    print()
    print("ARCHIVOS ACTUALIZADOS:")
    for filepath in updated_files:
        print(f"  - {filepath}")

    return 0


def x_cmd_version__mutmut_47(args: argparse.Namespace) -> int:
    """
    Gestiona la version de un conector siguiendo semver.

    Si se especifica --bump, incrementa la version segun el tipo:
    - major: Incrementa la version mayor (X.0.0) - cambios incompatibles
    - minor: Incrementa la version menor (0.X.0) - nueva funcionalidad compatible
    - patch: Incrementa la version de parche (0.0.X) - correcciones de bugs

    Si no se especifica --bump, muestra la version actual.

    Args:
        args: Argumentos parseados con 'connector_path', 'bump'

    Retorna:
        0 si la operacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    bump_type = getattr(args, "bump", None)

    current_version = _read_version(connector_path)
    if current_version is None:
        print(f"Error: No se pudo determinar la version del conector en {connector_path}", file=sys.stderr)
        return 1

    if bump_type is None:
        print(f"Conector: {connector_path.name}")
        print(f"Version actual: {current_version}")
        return 0

    new_version = _bump_version(current_version, bump_type)
    if new_version is None:
        print(f"Error: No se pudo calcular la nueva version. Version actual: {current_version}", file=sys.stderr)
        return 1

    updated_files = _update_version_in_files(connector_path, current_version, new_version)

    print(f"Version actualizada: {current_version} -> {new_version}")
    print(f"Bump: {bump_type}")
    print()
    print("Archivos actualizados:")
    for filepath in updated_files:
        print(None)

    return 0


def x_cmd_version__mutmut_48(args: argparse.Namespace) -> int:
    """
    Gestiona la version de un conector siguiendo semver.

    Si se especifica --bump, incrementa la version segun el tipo:
    - major: Incrementa la version mayor (X.0.0) - cambios incompatibles
    - minor: Incrementa la version menor (0.X.0) - nueva funcionalidad compatible
    - patch: Incrementa la version de parche (0.0.X) - correcciones de bugs

    Si no se especifica --bump, muestra la version actual.

    Args:
        args: Argumentos parseados con 'connector_path', 'bump'

    Retorna:
        0 si la operacion fue exitosa, 1 si hubo errores
    """
    connector_path = Path(args.connector_path)
    bump_type = getattr(args, "bump", None)

    current_version = _read_version(connector_path)
    if current_version is None:
        print(f"Error: No se pudo determinar la version del conector en {connector_path}", file=sys.stderr)
        return 1

    if bump_type is None:
        print(f"Conector: {connector_path.name}")
        print(f"Version actual: {current_version}")
        return 0

    new_version = _bump_version(current_version, bump_type)
    if new_version is None:
        print(f"Error: No se pudo calcular la nueva version. Version actual: {current_version}", file=sys.stderr)
        return 1

    updated_files = _update_version_in_files(connector_path, current_version, new_version)

    print(f"Version actualizada: {current_version} -> {new_version}")
    print(f"Bump: {bump_type}")
    print()
    print("Archivos actualizados:")
    for filepath in updated_files:
        print(f"  - {filepath}")

    return 1

mutants_x_cmd_version__mutmut['_mutmut_orig'] = x_cmd_version__mutmut_orig # type: ignore # mutmut generated
mutants_x_cmd_version__mutmut['x_cmd_version__mutmut_1'] = x_cmd_version__mutmut_1 # type: ignore # mutmut generated
mutants_x_cmd_version__mutmut['x_cmd_version__mutmut_2'] = x_cmd_version__mutmut_2 # type: ignore # mutmut generated
mutants_x_cmd_version__mutmut['x_cmd_version__mutmut_3'] = x_cmd_version__mutmut_3 # type: ignore # mutmut generated
mutants_x_cmd_version__mutmut['x_cmd_version__mutmut_4'] = x_cmd_version__mutmut_4 # type: ignore # mutmut generated
mutants_x_cmd_version__mutmut['x_cmd_version__mutmut_5'] = x_cmd_version__mutmut_5 # type: ignore # mutmut generated
mutants_x_cmd_version__mutmut['x_cmd_version__mutmut_6'] = x_cmd_version__mutmut_6 # type: ignore # mutmut generated
mutants_x_cmd_version__mutmut['x_cmd_version__mutmut_7'] = x_cmd_version__mutmut_7 # type: ignore # mutmut generated
mutants_x_cmd_version__mutmut['x_cmd_version__mutmut_8'] = x_cmd_version__mutmut_8 # type: ignore # mutmut generated
mutants_x_cmd_version__mutmut['x_cmd_version__mutmut_9'] = x_cmd_version__mutmut_9 # type: ignore # mutmut generated
mutants_x_cmd_version__mutmut['x_cmd_version__mutmut_10'] = x_cmd_version__mutmut_10 # type: ignore # mutmut generated
mutants_x_cmd_version__mutmut['x_cmd_version__mutmut_11'] = x_cmd_version__mutmut_11 # type: ignore # mutmut generated
mutants_x_cmd_version__mutmut['x_cmd_version__mutmut_12'] = x_cmd_version__mutmut_12 # type: ignore # mutmut generated
mutants_x_cmd_version__mutmut['x_cmd_version__mutmut_13'] = x_cmd_version__mutmut_13 # type: ignore # mutmut generated
mutants_x_cmd_version__mutmut['x_cmd_version__mutmut_14'] = x_cmd_version__mutmut_14 # type: ignore # mutmut generated
mutants_x_cmd_version__mutmut['x_cmd_version__mutmut_15'] = x_cmd_version__mutmut_15 # type: ignore # mutmut generated
mutants_x_cmd_version__mutmut['x_cmd_version__mutmut_16'] = x_cmd_version__mutmut_16 # type: ignore # mutmut generated
mutants_x_cmd_version__mutmut['x_cmd_version__mutmut_17'] = x_cmd_version__mutmut_17 # type: ignore # mutmut generated
mutants_x_cmd_version__mutmut['x_cmd_version__mutmut_18'] = x_cmd_version__mutmut_18 # type: ignore # mutmut generated
mutants_x_cmd_version__mutmut['x_cmd_version__mutmut_19'] = x_cmd_version__mutmut_19 # type: ignore # mutmut generated
mutants_x_cmd_version__mutmut['x_cmd_version__mutmut_20'] = x_cmd_version__mutmut_20 # type: ignore # mutmut generated
mutants_x_cmd_version__mutmut['x_cmd_version__mutmut_21'] = x_cmd_version__mutmut_21 # type: ignore # mutmut generated
mutants_x_cmd_version__mutmut['x_cmd_version__mutmut_22'] = x_cmd_version__mutmut_22 # type: ignore # mutmut generated
mutants_x_cmd_version__mutmut['x_cmd_version__mutmut_23'] = x_cmd_version__mutmut_23 # type: ignore # mutmut generated
mutants_x_cmd_version__mutmut['x_cmd_version__mutmut_24'] = x_cmd_version__mutmut_24 # type: ignore # mutmut generated
mutants_x_cmd_version__mutmut['x_cmd_version__mutmut_25'] = x_cmd_version__mutmut_25 # type: ignore # mutmut generated
mutants_x_cmd_version__mutmut['x_cmd_version__mutmut_26'] = x_cmd_version__mutmut_26 # type: ignore # mutmut generated
mutants_x_cmd_version__mutmut['x_cmd_version__mutmut_27'] = x_cmd_version__mutmut_27 # type: ignore # mutmut generated
mutants_x_cmd_version__mutmut['x_cmd_version__mutmut_28'] = x_cmd_version__mutmut_28 # type: ignore # mutmut generated
mutants_x_cmd_version__mutmut['x_cmd_version__mutmut_29'] = x_cmd_version__mutmut_29 # type: ignore # mutmut generated
mutants_x_cmd_version__mutmut['x_cmd_version__mutmut_30'] = x_cmd_version__mutmut_30 # type: ignore # mutmut generated
mutants_x_cmd_version__mutmut['x_cmd_version__mutmut_31'] = x_cmd_version__mutmut_31 # type: ignore # mutmut generated
mutants_x_cmd_version__mutmut['x_cmd_version__mutmut_32'] = x_cmd_version__mutmut_32 # type: ignore # mutmut generated
mutants_x_cmd_version__mutmut['x_cmd_version__mutmut_33'] = x_cmd_version__mutmut_33 # type: ignore # mutmut generated
mutants_x_cmd_version__mutmut['x_cmd_version__mutmut_34'] = x_cmd_version__mutmut_34 # type: ignore # mutmut generated
mutants_x_cmd_version__mutmut['x_cmd_version__mutmut_35'] = x_cmd_version__mutmut_35 # type: ignore # mutmut generated
mutants_x_cmd_version__mutmut['x_cmd_version__mutmut_36'] = x_cmd_version__mutmut_36 # type: ignore # mutmut generated
mutants_x_cmd_version__mutmut['x_cmd_version__mutmut_37'] = x_cmd_version__mutmut_37 # type: ignore # mutmut generated
mutants_x_cmd_version__mutmut['x_cmd_version__mutmut_38'] = x_cmd_version__mutmut_38 # type: ignore # mutmut generated
mutants_x_cmd_version__mutmut['x_cmd_version__mutmut_39'] = x_cmd_version__mutmut_39 # type: ignore # mutmut generated
mutants_x_cmd_version__mutmut['x_cmd_version__mutmut_40'] = x_cmd_version__mutmut_40 # type: ignore # mutmut generated
mutants_x_cmd_version__mutmut['x_cmd_version__mutmut_41'] = x_cmd_version__mutmut_41 # type: ignore # mutmut generated
mutants_x_cmd_version__mutmut['x_cmd_version__mutmut_42'] = x_cmd_version__mutmut_42 # type: ignore # mutmut generated
mutants_x_cmd_version__mutmut['x_cmd_version__mutmut_43'] = x_cmd_version__mutmut_43 # type: ignore # mutmut generated
mutants_x_cmd_version__mutmut['x_cmd_version__mutmut_44'] = x_cmd_version__mutmut_44 # type: ignore # mutmut generated
mutants_x_cmd_version__mutmut['x_cmd_version__mutmut_45'] = x_cmd_version__mutmut_45 # type: ignore # mutmut generated
mutants_x_cmd_version__mutmut['x_cmd_version__mutmut_46'] = x_cmd_version__mutmut_46 # type: ignore # mutmut generated
mutants_x_cmd_version__mutmut['x_cmd_version__mutmut_47'] = x_cmd_version__mutmut_47 # type: ignore # mutmut generated
mutants_x_cmd_version__mutmut['x_cmd_version__mutmut_48'] = x_cmd_version__mutmut_48 # type: ignore # mutmut generated
