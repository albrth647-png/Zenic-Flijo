"""
Code-Forge CLI v1.0
===================
Entry point for `python -m forge <command>`.

Commands:
  init            Inicializa ledger en directorio actual
  verify          Corre 12 gates sobre el proyecto
  check-module    Gates sobre un módulo específico
  report          Genera reporte de estado
  self-test       Ejecuta auto-test de gates en directorio temporal
"""

import argparse
import sys
from pathlib import Path


def cmd_init(args):
    """Inicializa ledger vacío en el directorio actual."""
    from forge import RunLedger

    target = Path(args.dir).resolve()
    ledger = RunLedger(target)
    ledger_path = target / "run_ledger.json"
    action = ledger._append_action
    ledger._actions = []
    ledger._persist()
    print(f"Ledger initialized at {ledger_path}")


def cmd_verify(args):
    """Corre todos los gates sobre el proyecto."""
    from forge import GateRunner

    root = Path(args.dir).resolve()
    runner = GateRunner(root)
    exclude = set(runner.EXPENSIVE_GATES) if args.quick else set()
    report = runner.run_all(exclude=exclude)
    runner.print_report()
    return 0 if report["overall"]["passed"] else 1


def cmd_check_module(args):
    """Corre gates sobre un módulo específico."""
    from forge import GateRunner

    root = Path(args.dir).resolve()
    module_path = Path(args.module)
    if not module_path.exists():
        print(f"Module not found: {module_path}", file=sys.stderr)
        return 1

    runner = GateRunner(root)
    py_files = list(module_path.rglob("*.py"))
    ts_files = list(module_path.rglob("*.ts")) + list(module_path.rglob("*.tsx"))
    stacks = []
    if py_files:
        stacks.append("python")
    if ts_files:
        stacks.append("typescript")
    if not stacks:
        print(f"No Python or TypeScript files found in {module_path}", file=sys.stderr)
        return 1

    report = runner.run_all(stacks=stacks, exclude=set(runner.EXPENSIVE_GATES))
    runner.print_report()
    return 0 if report["overall"]["passed"] else 1


def cmd_report(args):
    """Genera reporte de estado del proyecto."""
    from forge import GateRunner

    root = Path(args.dir).resolve()
    runner = GateRunner(root)
    exclude = set(runner.EXPENSIVE_GATES) if args.quick else set()
    report = runner.run_all(exclude=exclude)
    runner.print_report()
    print()
    print("  Summary:")
    print(f"    Hard gates: {report['hard_gates']['count']}")
    print(f"    Soft score: {report['soft_goals']['score']:.1f}/{report['soft_goals']['threshold']}")
    print(f"    Overall:    {'PASS' if report['overall']['passed'] else 'FAIL'}")
    return 0 if report["overall"]["passed"] else 1


def cmd_self_test(args):
    """Ejecuta self-test en directorio temporal."""
    from forge.gates import self_test

    report = self_test()
    return 0 if report["overall"]["passed"] else 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m forge",
        description="Code-Forge v1.0 — Framework de ingeniería para agentes de IA",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_init = sub.add_parser("init", help="Inicializa ledger en directorio")
    p_init.add_argument("--dir", default=".", help="Directorio del proyecto")

    p_verify = sub.add_parser("verify", help="Corre 12 gates sobre el proyecto")
    p_verify.add_argument("--dir", default=".", help="Directorio del proyecto")
    p_verify.add_argument("--quick", action="store_true", help="Skip expensive gates (mutation, coverage)")

    p_module = sub.add_parser("check-module", help="Gates sobre un módulo específico")
    p_module.add_argument("module", help="Ruta del módulo (ej: src/hat/)")
    p_module.add_argument("--dir", default=".", help="Directorio del proyecto")

    p_report = sub.add_parser("report", help="Genera reporte de estado")
    p_report.add_argument("--dir", default=".", help="Directorio del proyecto")
    p_report.add_argument("--quick", action="store_true", help="Skip expensive gates")

    sub.add_parser("self-test", help="Ejecuta auto-test de gates en directorio temporal")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    dispatch = {
        "init": cmd_init,
        "verify": cmd_verify,
        "check-module": cmd_check_module,
        "report": cmd_report,
        "self-test": cmd_self_test,
    }

    handler = dispatch.get(args.command)
    if handler:
        return handler(args)
    parser.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
