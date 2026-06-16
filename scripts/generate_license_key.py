#!/usr/bin/env python3
"""
Workflow Determinista — Generar License Key
Uso: python scripts/generate_license_key.py --type individual --client "Cliente Demo"
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from src.license.generator import LicenseGenerator


def main():
    parser = argparse.ArgumentParser(description="Generar License Key para Workflow Determinista")
    parser.add_argument(
        "--type", choices=["individual", "reseller", "enterprise"], default="individual", help="Tipo de licencia"
    )
    parser.add_argument("--client", default="", help="Nombre del cliente")
    parser.add_argument("--days", type=int, default=365, help="Días de validez")
    parser.add_argument(
        "--password", default="",
        help="Contraseña de administrador para descifrar clave privada Ed25519. "
             "Si no se proporciona, se solicitará interactivamente."
    )
    args = parser.parse_args()

    admin_password = args.password
    if not admin_password:
        import getpass
        admin_password = getpass.getpass("Contraseña de administrador: ")

    gen = LicenseGenerator()
    key = gen.generate(admin_password=admin_password, license_type=args.type, client_name=args.client, days_valid=args.days)
    print("\n⚙️  License Key Generada")
    print(f"{'=' * 40}")
    print(f"  {key}")
    print(f"{'=' * 40}")
    print(f"  Tipo:     {args.type}")
    print(f"  Cliente:  {args.client or '(sin especificar)'}")
    print(f"  Validez:  {args.days} días")
    print(f"  Firma:    {gen.last_signature_b64[:20]}... (almacenada para activación)")
    print()
    print("Para activar esta licencia, use:")
    print(f"  activate_key('{key}', signature_b64='{gen.last_signature_b64}')")
    print()


if __name__ == "__main__":
    main()
