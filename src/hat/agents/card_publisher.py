"""
HAT-ORBITAL Nivel 2-3 — Card Publisher Mixin.

Mixin que añade a cualquier BaseAgent la capacidad de publicar su AgentCard
en el Ledger (DB hat_agent_cards) y como variable OVC para resonancia RCC.

Uso:
    class MySpecialist(BaseAgent, CardPublisherMixin):
        def get_card(self) -> AgentCard:
            return AgentCard(agent_id="my_specialist", ...)

    agent = MySpecialist(config)
    agent.publish_card()  # persiste en DB + inyecta en OVC

Implementado en F0-D6 siguiendo HAT_ORBITAL_PLAN.md §5.3.
"""

from __future__ import annotations

import hashlib

from src.hat.agents.cards import AgentCard
from src.hat.ledger.repository import LedgerRepository
from src.orbital.context import OrbitalContext
from src.orbital.models import TWO_PI
from src.utils.logger import setup_logging

logger = setup_logging(__name__)

# Prefijo para variables OVC de Agent Cards.
_CARD_VAR_PREFIX = "card_"


class CardPublisherMixin:
    """Mixin para publicar AgentCards en DB + OVC.

    Debe combinarse con BaseAgent (que provee `self.config` y `self.agent_id`).
    La subclase debe implementar get_card() -> AgentCard.
    """

    def get_card(self) -> AgentCard:
        """Retorna la AgentCard que describe a este agente.

        Subclases deben sobreescribir este método.
        """
        raise NotImplementedError(
            f"{type(self).__name__} debe implementar get_card() -> AgentCard"
        )

    def publish_card(
        self,
        repo: LedgerRepository | None = None,
        ctx: OrbitalContext | None = None,
    ) -> AgentCard:
        """Publica la AgentCard en DB (hat_agent_cards) + OVC.

        Idempotente: si la variable OVC ya existe, se skip (no duplica).
        La DB usa ON CONFLICT(agent_id) DO UPDATE → actualiza si existe.

        Args:
            repo: LedgerRepository. None → crea uno nuevo (usa DatabaseManager singleton).
            ctx: OrbitalContext. None → usa el singleton existente.

        Returns:
            La AgentCard publicada (la misma que retorna get_card()).
        """
        card = self.get_card()
        repository = repo if repo is not None else LedgerRepository()
        context = ctx if ctx is not None else OrbitalContext()  # type: ignore[no-untyped-call]

        # 1. Persistir en hat_agent_cards
        self._persist_card_to_db(card, repository)

        # 2. Inyectar como variable OVC
        self._inject_card_to_ovc(card, context)

        logger.info(
            "CardPublisher: card %s publicada (domain=%s, tier=%s, %d keywords)",
            card.agent_id, card.domain, card.tier, len(card.orbital_keywords),
        )
        return card

    @staticmethod
    def _persist_card_to_db(card: AgentCard, repo: LedgerRepository) -> None:
        """Persiste la AgentCard en hat_agent_cards (upsert)."""
        repo.upsert_agent_card(
            agent_id=card.agent_id,
            agent_name=card.agent_name,
            domain=card.domain,
            tier=card.tier,
            capabilities=card.capabilities,
            orbital_keywords=card.orbital_keywords,
            cost_per_call=card.cost_per_call,
            avg_latency_ms=card.avg_latency_ms,
            orbital_amplitude=card.orbital_amplitude,
            orbital_velocity=card.orbital_velocity,
        )

    @staticmethod
    def _inject_card_to_ovc(card: AgentCard, ctx: OrbitalContext) -> None:
        """Inyecta la AgentCard como variable OVC. Idempotente."""
        var_name = f"{_CARD_VAR_PREFIX}{card.agent_id}"
        theta = CardPublisherMixin._deterministic_theta(card.orbital_keywords)
        try:
            ctx.ovc.create_variable(
                name=var_name,
                theta=theta,
                amplitude=card.orbital_amplitude,
                velocity=card.orbital_velocity,
                orbit_group=f"hat_cards_{card.domain}",
                metadata=card.to_ovc_metadata(),
            )
        except ValueError:
            # Variable ya existe (idempotente) — skip silencioso.
            logger.debug(
                "CardPublisher: variable OVC %s ya existe — skip", var_name
            )

    @staticmethod
    def _deterministic_theta(keywords: list[str]) -> float:
        """Genera una fase θ determinista a partir de keywords (hash MD5).

        Args:
            keywords: Lista de keywords (ej: ["buscar", "info"]).

        Returns:
            θ en [0, 2π) derivada deterministamente. Misma lista → misma θ.
        """
        joined = "|".join(keywords)
        hash_val = int(
            hashlib.md5(joined.encode(), usedforsecurity=False).hexdigest()[:8], 16
        )
        return (hash_val % 10000) / 10000.0 * TWO_PI

    @staticmethod
    def make_card_var_name(agent_id: str) -> str:
        """Genera el nombre canónico de la variable OVC para una card.

        Args:
            agent_id: ID del agente.

        Returns:
            Nombre en formato "card_<agent_id>".
        """
        return f"{_CARD_VAR_PREFIX}{agent_id}"
