"""
HAT-ORBITAL API v2 — Routes.

Endpoint FastAPI v2 para HAT. Recibe requests del usuario y delega al
HATRouter del Nivel 0.

Implementado en F0-D7.
"""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from src.hat.orbital_n0.tick_router import HATRouter

router = APIRouter(prefix="/api/hat", tags=["hat"])


class HATRequest(BaseModel):
    """Request del endpoint /chat."""

    user_id: str = Field(..., description="ID del usuario", min_length=1)
    session_id: str = Field(..., description="ID de la sesión", min_length=1)
    message: str = Field(..., description="Mensaje del usuario", min_length=1)
    context: dict[str, Any] = Field(
        default_factory=dict, description="Contexto adicional opcional",
    )


class HATResponse(BaseModel):
    """Response del endpoint /chat."""

    dispatch_id: str = Field(..., description="ID único del despacho")
    domain: str = Field(..., description="Dominio ganador (research/build/operate/clarify)")
    response: str = Field(..., description="Texto de respuesta al usuario")
    orbital_resonance: float = Field(..., description="Resonancia ORBITAL final [0, 1]")
    anti_dup_layer_hit: str = Field(..., description="Capa anti-doble-llamada activada")
    duration_ms: int = Field(..., description="Duración total en ms")
    facts_updated: list[str] = Field(
        default_factory=list, description="Facts actualizados en el Ledger",
    )
    status: str = Field(..., description="Estado final (completed/failed/clarify)")


@router.post("/chat", response_model=HATResponse)
async def chat(request: HATRequest) -> HATResponse:
    """Endpoint principal HAT.

    Procesa el mensaje del usuario a través del HATRouter:
    1. Calcula intent_hash (anti-doble capa 1+2)
    2. Carga sesión del Ledger
    3. Ruteo por resonancia ORBITAL
    4. FSM desambiguación si necesario
    5. Despacha al supervisor del dominio ganador
    6. Persiste + sintetiza respuesta

    Args:
        request: HATRequest con user_id, session_id, message y context opcional.

    Returns:
        HATResponse con la respuesta sintetizada.

    Raises:
        HTTPException 500: Si el HATRouter falla internamente.
    """
    try:
        router_instance = HATRouter()
        result = router_instance.handle(
            user_id=request.user_id,
            session_id=request.session_id,
            message=request.message,
            context=request.context,
        )
        return HATResponse(**result)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Error interno HAT: {exc}",
        ) from exc


@router.get("/health")
async def health() -> dict[str, str]:
    """Health check del endpoint HAT."""
    return {"status": "ok", "module": "hat", "version": "f0-d7"}
