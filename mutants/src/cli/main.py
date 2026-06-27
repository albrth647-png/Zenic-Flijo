"""
Zenic CLI — Punto de Entrada Principal
========================================

Interfaz de linea de comandos para el desarrollo de conectores Zenic-Flijo.

Uso:
    python -m src.cli.main init <name> [--category ...] [--auth-type ...]
    python -m src.cli.main test <path> [--action ...] [--input ...]
    python -m src.cli.main validate <path>
    python -m src.cli.main publish <path> [--registry ...]
    python -m src.cli.main version <path> [--bump major|minor|patch]
    python -m src.cli.main list
    python -m src.cli.main info <name>
"""

from __future__ import annotations

import sys

from src.cli.commands import COMMAND_MAP, build_parser
from src.core.logging import setup_logging

logger = setup_logging(__name__)

CLI_VERSION = "1.0.0"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_main__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_main__mutmut)
def main(argv: list[str] | None = None) -> int:
    """
    Punto de entrada principal del CLI.

    Parsea los argumentos de linea de comandos y despacha al
    subcomando correspondiente usando COMMAND_MAP.

    Args:
        argv: Lista de argumentos (default: sys.argv[1:])

    Retorna:
        Codigo de salida (0 = exito, 1 = error)
    """
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    handler = COMMAND_MAP.get(args.command)
    if handler is None:
        print(f"Error: Comando desconocido '{args.command}'", file=sys.stderr)
        return 1

    try:
        return handler(args)
    except KeyboardInterrupt:
        print("\nOperacion cancelada por el usuario", file=sys.stderr)
        return 130
    except Exception as exc:
        print(f"Error inesperado: {exc}", file=sys.stderr)
        logger.error(f"Error en comando '{args.command}': {exc}", exc_info=True)
        return 1


def x_main__mutmut_orig(argv: list[str] | None = None) -> int:
    """
    Punto de entrada principal del CLI.

    Parsea los argumentos de linea de comandos y despacha al
    subcomando correspondiente usando COMMAND_MAP.

    Args:
        argv: Lista de argumentos (default: sys.argv[1:])

    Retorna:
        Codigo de salida (0 = exito, 1 = error)
    """
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    handler = COMMAND_MAP.get(args.command)
    if handler is None:
        print(f"Error: Comando desconocido '{args.command}'", file=sys.stderr)
        return 1

    try:
        return handler(args)
    except KeyboardInterrupt:
        print("\nOperacion cancelada por el usuario", file=sys.stderr)
        return 130
    except Exception as exc:
        print(f"Error inesperado: {exc}", file=sys.stderr)
        logger.error(f"Error en comando '{args.command}': {exc}", exc_info=True)
        return 1


def x_main__mutmut_1(argv: list[str] | None = None) -> int:
    """
    Punto de entrada principal del CLI.

    Parsea los argumentos de linea de comandos y despacha al
    subcomando correspondiente usando COMMAND_MAP.

    Args:
        argv: Lista de argumentos (default: sys.argv[1:])

    Retorna:
        Codigo de salida (0 = exito, 1 = error)
    """
    parser = None
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    handler = COMMAND_MAP.get(args.command)
    if handler is None:
        print(f"Error: Comando desconocido '{args.command}'", file=sys.stderr)
        return 1

    try:
        return handler(args)
    except KeyboardInterrupt:
        print("\nOperacion cancelada por el usuario", file=sys.stderr)
        return 130
    except Exception as exc:
        print(f"Error inesperado: {exc}", file=sys.stderr)
        logger.error(f"Error en comando '{args.command}': {exc}", exc_info=True)
        return 1


def x_main__mutmut_2(argv: list[str] | None = None) -> int:
    """
    Punto de entrada principal del CLI.

    Parsea los argumentos de linea de comandos y despacha al
    subcomando correspondiente usando COMMAND_MAP.

    Args:
        argv: Lista de argumentos (default: sys.argv[1:])

    Retorna:
        Codigo de salida (0 = exito, 1 = error)
    """
    parser = build_parser()
    args = None

    if args.command is None:
        parser.print_help()
        return 0

    handler = COMMAND_MAP.get(args.command)
    if handler is None:
        print(f"Error: Comando desconocido '{args.command}'", file=sys.stderr)
        return 1

    try:
        return handler(args)
    except KeyboardInterrupt:
        print("\nOperacion cancelada por el usuario", file=sys.stderr)
        return 130
    except Exception as exc:
        print(f"Error inesperado: {exc}", file=sys.stderr)
        logger.error(f"Error en comando '{args.command}': {exc}", exc_info=True)
        return 1


def x_main__mutmut_3(argv: list[str] | None = None) -> int:
    """
    Punto de entrada principal del CLI.

    Parsea los argumentos de linea de comandos y despacha al
    subcomando correspondiente usando COMMAND_MAP.

    Args:
        argv: Lista de argumentos (default: sys.argv[1:])

    Retorna:
        Codigo de salida (0 = exito, 1 = error)
    """
    parser = build_parser()
    args = parser.parse_args(None)

    if args.command is None:
        parser.print_help()
        return 0

    handler = COMMAND_MAP.get(args.command)
    if handler is None:
        print(f"Error: Comando desconocido '{args.command}'", file=sys.stderr)
        return 1

    try:
        return handler(args)
    except KeyboardInterrupt:
        print("\nOperacion cancelada por el usuario", file=sys.stderr)
        return 130
    except Exception as exc:
        print(f"Error inesperado: {exc}", file=sys.stderr)
        logger.error(f"Error en comando '{args.command}': {exc}", exc_info=True)
        return 1


def x_main__mutmut_4(argv: list[str] | None = None) -> int:
    """
    Punto de entrada principal del CLI.

    Parsea los argumentos de linea de comandos y despacha al
    subcomando correspondiente usando COMMAND_MAP.

    Args:
        argv: Lista de argumentos (default: sys.argv[1:])

    Retorna:
        Codigo de salida (0 = exito, 1 = error)
    """
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command is not None:
        parser.print_help()
        return 0

    handler = COMMAND_MAP.get(args.command)
    if handler is None:
        print(f"Error: Comando desconocido '{args.command}'", file=sys.stderr)
        return 1

    try:
        return handler(args)
    except KeyboardInterrupt:
        print("\nOperacion cancelada por el usuario", file=sys.stderr)
        return 130
    except Exception as exc:
        print(f"Error inesperado: {exc}", file=sys.stderr)
        logger.error(f"Error en comando '{args.command}': {exc}", exc_info=True)
        return 1


def x_main__mutmut_5(argv: list[str] | None = None) -> int:
    """
    Punto de entrada principal del CLI.

    Parsea los argumentos de linea de comandos y despacha al
    subcomando correspondiente usando COMMAND_MAP.

    Args:
        argv: Lista de argumentos (default: sys.argv[1:])

    Retorna:
        Codigo de salida (0 = exito, 1 = error)
    """
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 1

    handler = COMMAND_MAP.get(args.command)
    if handler is None:
        print(f"Error: Comando desconocido '{args.command}'", file=sys.stderr)
        return 1

    try:
        return handler(args)
    except KeyboardInterrupt:
        print("\nOperacion cancelada por el usuario", file=sys.stderr)
        return 130
    except Exception as exc:
        print(f"Error inesperado: {exc}", file=sys.stderr)
        logger.error(f"Error en comando '{args.command}': {exc}", exc_info=True)
        return 1


def x_main__mutmut_6(argv: list[str] | None = None) -> int:
    """
    Punto de entrada principal del CLI.

    Parsea los argumentos de linea de comandos y despacha al
    subcomando correspondiente usando COMMAND_MAP.

    Args:
        argv: Lista de argumentos (default: sys.argv[1:])

    Retorna:
        Codigo de salida (0 = exito, 1 = error)
    """
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    handler = None
    if handler is None:
        print(f"Error: Comando desconocido '{args.command}'", file=sys.stderr)
        return 1

    try:
        return handler(args)
    except KeyboardInterrupt:
        print("\nOperacion cancelada por el usuario", file=sys.stderr)
        return 130
    except Exception as exc:
        print(f"Error inesperado: {exc}", file=sys.stderr)
        logger.error(f"Error en comando '{args.command}': {exc}", exc_info=True)
        return 1


def x_main__mutmut_7(argv: list[str] | None = None) -> int:
    """
    Punto de entrada principal del CLI.

    Parsea los argumentos de linea de comandos y despacha al
    subcomando correspondiente usando COMMAND_MAP.

    Args:
        argv: Lista de argumentos (default: sys.argv[1:])

    Retorna:
        Codigo de salida (0 = exito, 1 = error)
    """
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    handler = COMMAND_MAP.get(None)
    if handler is None:
        print(f"Error: Comando desconocido '{args.command}'", file=sys.stderr)
        return 1

    try:
        return handler(args)
    except KeyboardInterrupt:
        print("\nOperacion cancelada por el usuario", file=sys.stderr)
        return 130
    except Exception as exc:
        print(f"Error inesperado: {exc}", file=sys.stderr)
        logger.error(f"Error en comando '{args.command}': {exc}", exc_info=True)
        return 1


def x_main__mutmut_8(argv: list[str] | None = None) -> int:
    """
    Punto de entrada principal del CLI.

    Parsea los argumentos de linea de comandos y despacha al
    subcomando correspondiente usando COMMAND_MAP.

    Args:
        argv: Lista de argumentos (default: sys.argv[1:])

    Retorna:
        Codigo de salida (0 = exito, 1 = error)
    """
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    handler = COMMAND_MAP.get(args.command)
    if handler is not None:
        print(f"Error: Comando desconocido '{args.command}'", file=sys.stderr)
        return 1

    try:
        return handler(args)
    except KeyboardInterrupt:
        print("\nOperacion cancelada por el usuario", file=sys.stderr)
        return 130
    except Exception as exc:
        print(f"Error inesperado: {exc}", file=sys.stderr)
        logger.error(f"Error en comando '{args.command}': {exc}", exc_info=True)
        return 1


def x_main__mutmut_9(argv: list[str] | None = None) -> int:
    """
    Punto de entrada principal del CLI.

    Parsea los argumentos de linea de comandos y despacha al
    subcomando correspondiente usando COMMAND_MAP.

    Args:
        argv: Lista de argumentos (default: sys.argv[1:])

    Retorna:
        Codigo de salida (0 = exito, 1 = error)
    """
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    handler = COMMAND_MAP.get(args.command)
    if handler is None:
        print(None, file=sys.stderr)
        return 1

    try:
        return handler(args)
    except KeyboardInterrupt:
        print("\nOperacion cancelada por el usuario", file=sys.stderr)
        return 130
    except Exception as exc:
        print(f"Error inesperado: {exc}", file=sys.stderr)
        logger.error(f"Error en comando '{args.command}': {exc}", exc_info=True)
        return 1


def x_main__mutmut_10(argv: list[str] | None = None) -> int:
    """
    Punto de entrada principal del CLI.

    Parsea los argumentos de linea de comandos y despacha al
    subcomando correspondiente usando COMMAND_MAP.

    Args:
        argv: Lista de argumentos (default: sys.argv[1:])

    Retorna:
        Codigo de salida (0 = exito, 1 = error)
    """
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    handler = COMMAND_MAP.get(args.command)
    if handler is None:
        print(f"Error: Comando desconocido '{args.command}'", file=None)
        return 1

    try:
        return handler(args)
    except KeyboardInterrupt:
        print("\nOperacion cancelada por el usuario", file=sys.stderr)
        return 130
    except Exception as exc:
        print(f"Error inesperado: {exc}", file=sys.stderr)
        logger.error(f"Error en comando '{args.command}': {exc}", exc_info=True)
        return 1


def x_main__mutmut_11(argv: list[str] | None = None) -> int:
    """
    Punto de entrada principal del CLI.

    Parsea los argumentos de linea de comandos y despacha al
    subcomando correspondiente usando COMMAND_MAP.

    Args:
        argv: Lista de argumentos (default: sys.argv[1:])

    Retorna:
        Codigo de salida (0 = exito, 1 = error)
    """
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    handler = COMMAND_MAP.get(args.command)
    if handler is None:
        print(file=sys.stderr)
        return 1

    try:
        return handler(args)
    except KeyboardInterrupt:
        print("\nOperacion cancelada por el usuario", file=sys.stderr)
        return 130
    except Exception as exc:
        print(f"Error inesperado: {exc}", file=sys.stderr)
        logger.error(f"Error en comando '{args.command}': {exc}", exc_info=True)
        return 1


def x_main__mutmut_12(argv: list[str] | None = None) -> int:
    """
    Punto de entrada principal del CLI.

    Parsea los argumentos de linea de comandos y despacha al
    subcomando correspondiente usando COMMAND_MAP.

    Args:
        argv: Lista de argumentos (default: sys.argv[1:])

    Retorna:
        Codigo de salida (0 = exito, 1 = error)
    """
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    handler = COMMAND_MAP.get(args.command)
    if handler is None:
        print(f"Error: Comando desconocido '{args.command}'", )
        return 1

    try:
        return handler(args)
    except KeyboardInterrupt:
        print("\nOperacion cancelada por el usuario", file=sys.stderr)
        return 130
    except Exception as exc:
        print(f"Error inesperado: {exc}", file=sys.stderr)
        logger.error(f"Error en comando '{args.command}': {exc}", exc_info=True)
        return 1


def x_main__mutmut_13(argv: list[str] | None = None) -> int:
    """
    Punto de entrada principal del CLI.

    Parsea los argumentos de linea de comandos y despacha al
    subcomando correspondiente usando COMMAND_MAP.

    Args:
        argv: Lista de argumentos (default: sys.argv[1:])

    Retorna:
        Codigo de salida (0 = exito, 1 = error)
    """
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    handler = COMMAND_MAP.get(args.command)
    if handler is None:
        print(f"Error: Comando desconocido '{args.command}'", file=sys.stderr)
        return 2

    try:
        return handler(args)
    except KeyboardInterrupt:
        print("\nOperacion cancelada por el usuario", file=sys.stderr)
        return 130
    except Exception as exc:
        print(f"Error inesperado: {exc}", file=sys.stderr)
        logger.error(f"Error en comando '{args.command}': {exc}", exc_info=True)
        return 1


def x_main__mutmut_14(argv: list[str] | None = None) -> int:
    """
    Punto de entrada principal del CLI.

    Parsea los argumentos de linea de comandos y despacha al
    subcomando correspondiente usando COMMAND_MAP.

    Args:
        argv: Lista de argumentos (default: sys.argv[1:])

    Retorna:
        Codigo de salida (0 = exito, 1 = error)
    """
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    handler = COMMAND_MAP.get(args.command)
    if handler is None:
        print(f"Error: Comando desconocido '{args.command}'", file=sys.stderr)
        return 1

    try:
        return handler(None)
    except KeyboardInterrupt:
        print("\nOperacion cancelada por el usuario", file=sys.stderr)
        return 130
    except Exception as exc:
        print(f"Error inesperado: {exc}", file=sys.stderr)
        logger.error(f"Error en comando '{args.command}': {exc}", exc_info=True)
        return 1


def x_main__mutmut_15(argv: list[str] | None = None) -> int:
    """
    Punto de entrada principal del CLI.

    Parsea los argumentos de linea de comandos y despacha al
    subcomando correspondiente usando COMMAND_MAP.

    Args:
        argv: Lista de argumentos (default: sys.argv[1:])

    Retorna:
        Codigo de salida (0 = exito, 1 = error)
    """
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    handler = COMMAND_MAP.get(args.command)
    if handler is None:
        print(f"Error: Comando desconocido '{args.command}'", file=sys.stderr)
        return 1

    try:
        return handler(args)
    except KeyboardInterrupt:
        print(None, file=sys.stderr)
        return 130
    except Exception as exc:
        print(f"Error inesperado: {exc}", file=sys.stderr)
        logger.error(f"Error en comando '{args.command}': {exc}", exc_info=True)
        return 1


def x_main__mutmut_16(argv: list[str] | None = None) -> int:
    """
    Punto de entrada principal del CLI.

    Parsea los argumentos de linea de comandos y despacha al
    subcomando correspondiente usando COMMAND_MAP.

    Args:
        argv: Lista de argumentos (default: sys.argv[1:])

    Retorna:
        Codigo de salida (0 = exito, 1 = error)
    """
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    handler = COMMAND_MAP.get(args.command)
    if handler is None:
        print(f"Error: Comando desconocido '{args.command}'", file=sys.stderr)
        return 1

    try:
        return handler(args)
    except KeyboardInterrupt:
        print("\nOperacion cancelada por el usuario", file=None)
        return 130
    except Exception as exc:
        print(f"Error inesperado: {exc}", file=sys.stderr)
        logger.error(f"Error en comando '{args.command}': {exc}", exc_info=True)
        return 1


def x_main__mutmut_17(argv: list[str] | None = None) -> int:
    """
    Punto de entrada principal del CLI.

    Parsea los argumentos de linea de comandos y despacha al
    subcomando correspondiente usando COMMAND_MAP.

    Args:
        argv: Lista de argumentos (default: sys.argv[1:])

    Retorna:
        Codigo de salida (0 = exito, 1 = error)
    """
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    handler = COMMAND_MAP.get(args.command)
    if handler is None:
        print(f"Error: Comando desconocido '{args.command}'", file=sys.stderr)
        return 1

    try:
        return handler(args)
    except KeyboardInterrupt:
        print(file=sys.stderr)
        return 130
    except Exception as exc:
        print(f"Error inesperado: {exc}", file=sys.stderr)
        logger.error(f"Error en comando '{args.command}': {exc}", exc_info=True)
        return 1


def x_main__mutmut_18(argv: list[str] | None = None) -> int:
    """
    Punto de entrada principal del CLI.

    Parsea los argumentos de linea de comandos y despacha al
    subcomando correspondiente usando COMMAND_MAP.

    Args:
        argv: Lista de argumentos (default: sys.argv[1:])

    Retorna:
        Codigo de salida (0 = exito, 1 = error)
    """
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    handler = COMMAND_MAP.get(args.command)
    if handler is None:
        print(f"Error: Comando desconocido '{args.command}'", file=sys.stderr)
        return 1

    try:
        return handler(args)
    except KeyboardInterrupt:
        print("\nOperacion cancelada por el usuario", )
        return 130
    except Exception as exc:
        print(f"Error inesperado: {exc}", file=sys.stderr)
        logger.error(f"Error en comando '{args.command}': {exc}", exc_info=True)
        return 1


def x_main__mutmut_19(argv: list[str] | None = None) -> int:
    """
    Punto de entrada principal del CLI.

    Parsea los argumentos de linea de comandos y despacha al
    subcomando correspondiente usando COMMAND_MAP.

    Args:
        argv: Lista de argumentos (default: sys.argv[1:])

    Retorna:
        Codigo de salida (0 = exito, 1 = error)
    """
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    handler = COMMAND_MAP.get(args.command)
    if handler is None:
        print(f"Error: Comando desconocido '{args.command}'", file=sys.stderr)
        return 1

    try:
        return handler(args)
    except KeyboardInterrupt:
        print("XX\nOperacion cancelada por el usuarioXX", file=sys.stderr)
        return 130
    except Exception as exc:
        print(f"Error inesperado: {exc}", file=sys.stderr)
        logger.error(f"Error en comando '{args.command}': {exc}", exc_info=True)
        return 1


def x_main__mutmut_20(argv: list[str] | None = None) -> int:
    """
    Punto de entrada principal del CLI.

    Parsea los argumentos de linea de comandos y despacha al
    subcomando correspondiente usando COMMAND_MAP.

    Args:
        argv: Lista de argumentos (default: sys.argv[1:])

    Retorna:
        Codigo de salida (0 = exito, 1 = error)
    """
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    handler = COMMAND_MAP.get(args.command)
    if handler is None:
        print(f"Error: Comando desconocido '{args.command}'", file=sys.stderr)
        return 1

    try:
        return handler(args)
    except KeyboardInterrupt:
        print("\noperacion cancelada por el usuario", file=sys.stderr)
        return 130
    except Exception as exc:
        print(f"Error inesperado: {exc}", file=sys.stderr)
        logger.error(f"Error en comando '{args.command}': {exc}", exc_info=True)
        return 1


def x_main__mutmut_21(argv: list[str] | None = None) -> int:
    """
    Punto de entrada principal del CLI.

    Parsea los argumentos de linea de comandos y despacha al
    subcomando correspondiente usando COMMAND_MAP.

    Args:
        argv: Lista de argumentos (default: sys.argv[1:])

    Retorna:
        Codigo de salida (0 = exito, 1 = error)
    """
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    handler = COMMAND_MAP.get(args.command)
    if handler is None:
        print(f"Error: Comando desconocido '{args.command}'", file=sys.stderr)
        return 1

    try:
        return handler(args)
    except KeyboardInterrupt:
        print("\nOPERACION CANCELADA POR EL USUARIO", file=sys.stderr)
        return 130
    except Exception as exc:
        print(f"Error inesperado: {exc}", file=sys.stderr)
        logger.error(f"Error en comando '{args.command}': {exc}", exc_info=True)
        return 1


def x_main__mutmut_22(argv: list[str] | None = None) -> int:
    """
    Punto de entrada principal del CLI.

    Parsea los argumentos de linea de comandos y despacha al
    subcomando correspondiente usando COMMAND_MAP.

    Args:
        argv: Lista de argumentos (default: sys.argv[1:])

    Retorna:
        Codigo de salida (0 = exito, 1 = error)
    """
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    handler = COMMAND_MAP.get(args.command)
    if handler is None:
        print(f"Error: Comando desconocido '{args.command}'", file=sys.stderr)
        return 1

    try:
        return handler(args)
    except KeyboardInterrupt:
        print("\nOperacion cancelada por el usuario", file=sys.stderr)
        return 131
    except Exception as exc:
        print(f"Error inesperado: {exc}", file=sys.stderr)
        logger.error(f"Error en comando '{args.command}': {exc}", exc_info=True)
        return 1


def x_main__mutmut_23(argv: list[str] | None = None) -> int:
    """
    Punto de entrada principal del CLI.

    Parsea los argumentos de linea de comandos y despacha al
    subcomando correspondiente usando COMMAND_MAP.

    Args:
        argv: Lista de argumentos (default: sys.argv[1:])

    Retorna:
        Codigo de salida (0 = exito, 1 = error)
    """
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    handler = COMMAND_MAP.get(args.command)
    if handler is None:
        print(f"Error: Comando desconocido '{args.command}'", file=sys.stderr)
        return 1

    try:
        return handler(args)
    except KeyboardInterrupt:
        print("\nOperacion cancelada por el usuario", file=sys.stderr)
        return 130
    except Exception as exc:
        print(None, file=sys.stderr)
        logger.error(f"Error en comando '{args.command}': {exc}", exc_info=True)
        return 1


def x_main__mutmut_24(argv: list[str] | None = None) -> int:
    """
    Punto de entrada principal del CLI.

    Parsea los argumentos de linea de comandos y despacha al
    subcomando correspondiente usando COMMAND_MAP.

    Args:
        argv: Lista de argumentos (default: sys.argv[1:])

    Retorna:
        Codigo de salida (0 = exito, 1 = error)
    """
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    handler = COMMAND_MAP.get(args.command)
    if handler is None:
        print(f"Error: Comando desconocido '{args.command}'", file=sys.stderr)
        return 1

    try:
        return handler(args)
    except KeyboardInterrupt:
        print("\nOperacion cancelada por el usuario", file=sys.stderr)
        return 130
    except Exception as exc:
        print(f"Error inesperado: {exc}", file=None)
        logger.error(f"Error en comando '{args.command}': {exc}", exc_info=True)
        return 1


def x_main__mutmut_25(argv: list[str] | None = None) -> int:
    """
    Punto de entrada principal del CLI.

    Parsea los argumentos de linea de comandos y despacha al
    subcomando correspondiente usando COMMAND_MAP.

    Args:
        argv: Lista de argumentos (default: sys.argv[1:])

    Retorna:
        Codigo de salida (0 = exito, 1 = error)
    """
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    handler = COMMAND_MAP.get(args.command)
    if handler is None:
        print(f"Error: Comando desconocido '{args.command}'", file=sys.stderr)
        return 1

    try:
        return handler(args)
    except KeyboardInterrupt:
        print("\nOperacion cancelada por el usuario", file=sys.stderr)
        return 130
    except Exception as exc:
        print(file=sys.stderr)
        logger.error(f"Error en comando '{args.command}': {exc}", exc_info=True)
        return 1


def x_main__mutmut_26(argv: list[str] | None = None) -> int:
    """
    Punto de entrada principal del CLI.

    Parsea los argumentos de linea de comandos y despacha al
    subcomando correspondiente usando COMMAND_MAP.

    Args:
        argv: Lista de argumentos (default: sys.argv[1:])

    Retorna:
        Codigo de salida (0 = exito, 1 = error)
    """
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    handler = COMMAND_MAP.get(args.command)
    if handler is None:
        print(f"Error: Comando desconocido '{args.command}'", file=sys.stderr)
        return 1

    try:
        return handler(args)
    except KeyboardInterrupt:
        print("\nOperacion cancelada por el usuario", file=sys.stderr)
        return 130
    except Exception as exc:
        print(f"Error inesperado: {exc}", )
        logger.error(f"Error en comando '{args.command}': {exc}", exc_info=True)
        return 1


def x_main__mutmut_27(argv: list[str] | None = None) -> int:
    """
    Punto de entrada principal del CLI.

    Parsea los argumentos de linea de comandos y despacha al
    subcomando correspondiente usando COMMAND_MAP.

    Args:
        argv: Lista de argumentos (default: sys.argv[1:])

    Retorna:
        Codigo de salida (0 = exito, 1 = error)
    """
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    handler = COMMAND_MAP.get(args.command)
    if handler is None:
        print(f"Error: Comando desconocido '{args.command}'", file=sys.stderr)
        return 1

    try:
        return handler(args)
    except KeyboardInterrupt:
        print("\nOperacion cancelada por el usuario", file=sys.stderr)
        return 130
    except Exception as exc:
        print(f"Error inesperado: {exc}", file=sys.stderr)
        logger.error(None, exc_info=True)
        return 1


def x_main__mutmut_28(argv: list[str] | None = None) -> int:
    """
    Punto de entrada principal del CLI.

    Parsea los argumentos de linea de comandos y despacha al
    subcomando correspondiente usando COMMAND_MAP.

    Args:
        argv: Lista de argumentos (default: sys.argv[1:])

    Retorna:
        Codigo de salida (0 = exito, 1 = error)
    """
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    handler = COMMAND_MAP.get(args.command)
    if handler is None:
        print(f"Error: Comando desconocido '{args.command}'", file=sys.stderr)
        return 1

    try:
        return handler(args)
    except KeyboardInterrupt:
        print("\nOperacion cancelada por el usuario", file=sys.stderr)
        return 130
    except Exception as exc:
        print(f"Error inesperado: {exc}", file=sys.stderr)
        logger.error(f"Error en comando '{args.command}': {exc}", exc_info=None)
        return 1


def x_main__mutmut_29(argv: list[str] | None = None) -> int:
    """
    Punto de entrada principal del CLI.

    Parsea los argumentos de linea de comandos y despacha al
    subcomando correspondiente usando COMMAND_MAP.

    Args:
        argv: Lista de argumentos (default: sys.argv[1:])

    Retorna:
        Codigo de salida (0 = exito, 1 = error)
    """
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    handler = COMMAND_MAP.get(args.command)
    if handler is None:
        print(f"Error: Comando desconocido '{args.command}'", file=sys.stderr)
        return 1

    try:
        return handler(args)
    except KeyboardInterrupt:
        print("\nOperacion cancelada por el usuario", file=sys.stderr)
        return 130
    except Exception as exc:
        print(f"Error inesperado: {exc}", file=sys.stderr)
        logger.error(exc_info=True)
        return 1


def x_main__mutmut_30(argv: list[str] | None = None) -> int:
    """
    Punto de entrada principal del CLI.

    Parsea los argumentos de linea de comandos y despacha al
    subcomando correspondiente usando COMMAND_MAP.

    Args:
        argv: Lista de argumentos (default: sys.argv[1:])

    Retorna:
        Codigo de salida (0 = exito, 1 = error)
    """
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    handler = COMMAND_MAP.get(args.command)
    if handler is None:
        print(f"Error: Comando desconocido '{args.command}'", file=sys.stderr)
        return 1

    try:
        return handler(args)
    except KeyboardInterrupt:
        print("\nOperacion cancelada por el usuario", file=sys.stderr)
        return 130
    except Exception as exc:
        print(f"Error inesperado: {exc}", file=sys.stderr)
        logger.error(f"Error en comando '{args.command}': {exc}", )
        return 1


def x_main__mutmut_31(argv: list[str] | None = None) -> int:
    """
    Punto de entrada principal del CLI.

    Parsea los argumentos de linea de comandos y despacha al
    subcomando correspondiente usando COMMAND_MAP.

    Args:
        argv: Lista de argumentos (default: sys.argv[1:])

    Retorna:
        Codigo de salida (0 = exito, 1 = error)
    """
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    handler = COMMAND_MAP.get(args.command)
    if handler is None:
        print(f"Error: Comando desconocido '{args.command}'", file=sys.stderr)
        return 1

    try:
        return handler(args)
    except KeyboardInterrupt:
        print("\nOperacion cancelada por el usuario", file=sys.stderr)
        return 130
    except Exception as exc:
        print(f"Error inesperado: {exc}", file=sys.stderr)
        logger.error(f"Error en comando '{args.command}': {exc}", exc_info=False)
        return 1


def x_main__mutmut_32(argv: list[str] | None = None) -> int:
    """
    Punto de entrada principal del CLI.

    Parsea los argumentos de linea de comandos y despacha al
    subcomando correspondiente usando COMMAND_MAP.

    Args:
        argv: Lista de argumentos (default: sys.argv[1:])

    Retorna:
        Codigo de salida (0 = exito, 1 = error)
    """
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    handler = COMMAND_MAP.get(args.command)
    if handler is None:
        print(f"Error: Comando desconocido '{args.command}'", file=sys.stderr)
        return 1

    try:
        return handler(args)
    except KeyboardInterrupt:
        print("\nOperacion cancelada por el usuario", file=sys.stderr)
        return 130
    except Exception as exc:
        print(f"Error inesperado: {exc}", file=sys.stderr)
        logger.error(f"Error en comando '{args.command}': {exc}", exc_info=True)
        return 2

mutants_x_main__mutmut['_mutmut_orig'] = x_main__mutmut_orig # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_1'] = x_main__mutmut_1 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_2'] = x_main__mutmut_2 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_3'] = x_main__mutmut_3 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_4'] = x_main__mutmut_4 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_5'] = x_main__mutmut_5 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_6'] = x_main__mutmut_6 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_7'] = x_main__mutmut_7 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_8'] = x_main__mutmut_8 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_9'] = x_main__mutmut_9 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_10'] = x_main__mutmut_10 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_11'] = x_main__mutmut_11 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_12'] = x_main__mutmut_12 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_13'] = x_main__mutmut_13 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_14'] = x_main__mutmut_14 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_15'] = x_main__mutmut_15 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_16'] = x_main__mutmut_16 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_17'] = x_main__mutmut_17 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_18'] = x_main__mutmut_18 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_19'] = x_main__mutmut_19 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_20'] = x_main__mutmut_20 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_21'] = x_main__mutmut_21 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_22'] = x_main__mutmut_22 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_23'] = x_main__mutmut_23 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_24'] = x_main__mutmut_24 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_25'] = x_main__mutmut_25 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_26'] = x_main__mutmut_26 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_27'] = x_main__mutmut_27 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_28'] = x_main__mutmut_28 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_29'] = x_main__mutmut_29 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_30'] = x_main__mutmut_30 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_31'] = x_main__mutmut_31 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_32'] = x_main__mutmut_32 # type: ignore # mutmut generated


if __name__ == "__main__":
    sys.exit(main())
