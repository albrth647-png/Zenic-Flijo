"""
HAT-ORBITAL Nivel 0 — Intent Hasher.

Genera hashes deterministas para anti-doble-llamada (capa 1 Exact Match
y capa 2 Idempotency Lock del F1).

Hash = sha256(user_id + session_id + normalized_intent + sorted(params))
El mismo input siempre produce el mismo hash → permite detectar duplicados
sin necesidad de LLM ni comparaciones semánticas.

Implementado en F0-D7.
"""

from __future__ import annotations

import hashlib
import json
import re
from typing import Any

# Regex para normalizar: lowercase, sin acentos, sin puntuación extraña.
_ACCENT_MAP = {
    "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u",
    "ñ": "n", "ü": "u",
}
_NON_ALNUM_SPACE = re.compile(r"[^a-z0-9 ]")


def normalize_intent(text: str) -> str:
    """Normaliza texto del usuario para hashing determinista.

    Pasos:
    1. lowercase
    2. strip
    3. reemplazar acentos (á→a, é→e, ...)
    4. colapsar espacios múltiples
    5. eliminar puntuación (mantener solo alfanum + espacio)

    Args:
        text: Texto crudo del usuario.

    Returns:
        Texto normalizado listo para hashing. Vacío si el input es inválido.
    """
    if not isinstance(text, str):
        return ""
    lowered = text.lower().strip()
    # Reemplazar acentos
    for accented, plain in _ACCENT_MAP.items():
        lowered = lowered.replace(accented, plain)
    # Eliminar puntuación
    lowered = _NON_ALNUM_SPACE.sub(" ", lowered)
    # Colapsar espacios
    return " ".join(lowered.split())


def compute_intent_hash(
    user_id: str,
    session_id: str,
    intent: str,
    params: dict[str, Any] | None = None,
) -> str:
    """Calcula el hash determinista de un intent del usuario.

    El hash es sha256 de:
        user_id + "|" + session_id + "|" + normalize_intent(intent) + "|" + sorted(params)

    Args:
        user_id: ID del usuario.
        session_id: ID de la sesión.
        intent: Texto del usuario (se normaliza antes de hashear).
        params: Parámetros adicionales (se serializan como JSON con keys sorted).

    Returns:
        Hex string de 64 caracteres (sha256).

    Raises:
        TypeError: Si user_id o session_id no son strings.
    """
    if not isinstance(user_id, str):
        raise TypeError(f"user_id debe ser str, no {type(user_id).__name__}")
    if not isinstance(session_id, str):
        raise TypeError(f"session_id debe ser str, no {type(session_id).__name__}")

    normalized = normalize_intent(intent)
    params = params or {}
    params_json = json.dumps(params, sort_keys=True, ensure_ascii=False, default=str)

    payload = f"{user_id}|{session_id}|{normalized}|{params_json}"
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()
