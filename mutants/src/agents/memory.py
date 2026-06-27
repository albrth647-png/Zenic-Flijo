"""Agent Memory — Short-term and long-term memory with vector similarity.

Provides persistent memory for agents with:
- Short-term memory: Recent observations and actions (sliding window)
- Long-term memory: Persistent knowledge with semantic search
- Vector similarity: Cosine similarity for semantic recall
- Memory consolidation: Automatic transfer from short-term to long-term
"""

from __future__ import annotations

import math
import sqlite3
import threading
import time
import uuid
from dataclasses import dataclass, field
from typing import Any

from src.utils.logger import get_logger

logger = get_logger("agent.memory")


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class MemoryEntry:
    """A single memory entry with metadata and optional embedding."""

    entry_id: str = ""
    agent_id: str = ""
    content: str = ""
    entry_type: str = "observation"  # observation, action, decision, knowledge
    importance: float = 0.5  # 0.0 to 1.0
    embedding: list[float] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)
    timestamp: float = field(default_factory=time.time)
    access_count: int = 0
    last_accessed: float = field(default_factory=time.time)

    def __post_init__(self) -> None:
        if not self.entry_id:
            self.entry_id = f"mem-{uuid.uuid4().hex[:8]}"
mutants_x__cosine_similarity__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__cosine_similarity__mutmut)
def _cosine_similarity(a: list[float], b: list[float]) -> float:
    """Compute cosine similarity between two vectors."""
    if not a or not b or len(a) != len(b):
        return 0.0
    dot = sum(x * y for x, y in zip(a, b, strict=False))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(x * x for x in b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def x__cosine_similarity__mutmut_orig(a: list[float], b: list[float]) -> float:
    """Compute cosine similarity between two vectors."""
    if not a or not b or len(a) != len(b):
        return 0.0
    dot = sum(x * y for x, y in zip(a, b, strict=False))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(x * x for x in b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def x__cosine_similarity__mutmut_1(a: list[float], b: list[float]) -> float:
    """Compute cosine similarity between two vectors."""
    if not a or not b and len(a) != len(b):
        return 0.0
    dot = sum(x * y for x, y in zip(a, b, strict=False))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(x * x for x in b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def x__cosine_similarity__mutmut_2(a: list[float], b: list[float]) -> float:
    """Compute cosine similarity between two vectors."""
    if not a and not b or len(a) != len(b):
        return 0.0
    dot = sum(x * y for x, y in zip(a, b, strict=False))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(x * x for x in b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def x__cosine_similarity__mutmut_3(a: list[float], b: list[float]) -> float:
    """Compute cosine similarity between two vectors."""
    if a or not b or len(a) != len(b):
        return 0.0
    dot = sum(x * y for x, y in zip(a, b, strict=False))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(x * x for x in b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def x__cosine_similarity__mutmut_4(a: list[float], b: list[float]) -> float:
    """Compute cosine similarity between two vectors."""
    if not a or b or len(a) != len(b):
        return 0.0
    dot = sum(x * y for x, y in zip(a, b, strict=False))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(x * x for x in b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def x__cosine_similarity__mutmut_5(a: list[float], b: list[float]) -> float:
    """Compute cosine similarity between two vectors."""
    if not a or not b or len(a) == len(b):
        return 0.0
    dot = sum(x * y for x, y in zip(a, b, strict=False))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(x * x for x in b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def x__cosine_similarity__mutmut_6(a: list[float], b: list[float]) -> float:
    """Compute cosine similarity between two vectors."""
    if not a or not b or len(a) != len(b):
        return 1.0
    dot = sum(x * y for x, y in zip(a, b, strict=False))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(x * x for x in b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def x__cosine_similarity__mutmut_7(a: list[float], b: list[float]) -> float:
    """Compute cosine similarity between two vectors."""
    if not a or not b or len(a) != len(b):
        return 0.0
    dot = None
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(x * x for x in b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def x__cosine_similarity__mutmut_8(a: list[float], b: list[float]) -> float:
    """Compute cosine similarity between two vectors."""
    if not a or not b or len(a) != len(b):
        return 0.0
    dot = sum(None)
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(x * x for x in b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def x__cosine_similarity__mutmut_9(a: list[float], b: list[float]) -> float:
    """Compute cosine similarity between two vectors."""
    if not a or not b or len(a) != len(b):
        return 0.0
    dot = sum(x / y for x, y in zip(a, b, strict=False))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(x * x for x in b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def x__cosine_similarity__mutmut_10(a: list[float], b: list[float]) -> float:
    """Compute cosine similarity between two vectors."""
    if not a or not b or len(a) != len(b):
        return 0.0
    dot = sum(x * y for x, y in zip(None, b, strict=False))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(x * x for x in b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def x__cosine_similarity__mutmut_11(a: list[float], b: list[float]) -> float:
    """Compute cosine similarity between two vectors."""
    if not a or not b or len(a) != len(b):
        return 0.0
    dot = sum(x * y for x, y in zip(a, None, strict=False))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(x * x for x in b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def x__cosine_similarity__mutmut_12(a: list[float], b: list[float]) -> float:
    """Compute cosine similarity between two vectors."""
    if not a or not b or len(a) != len(b):
        return 0.0
    dot = sum(x * y for x, y in zip(a, b, strict=None))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(x * x for x in b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def x__cosine_similarity__mutmut_13(a: list[float], b: list[float]) -> float:
    """Compute cosine similarity between two vectors."""
    if not a or not b or len(a) != len(b):
        return 0.0
    dot = sum(x * y for x, y in zip(b, strict=False))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(x * x for x in b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def x__cosine_similarity__mutmut_14(a: list[float], b: list[float]) -> float:
    """Compute cosine similarity between two vectors."""
    if not a or not b or len(a) != len(b):
        return 0.0
    dot = sum(x * y for x, y in zip(a, strict=False))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(x * x for x in b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def x__cosine_similarity__mutmut_15(a: list[float], b: list[float]) -> float:
    """Compute cosine similarity between two vectors."""
    if not a or not b or len(a) != len(b):
        return 0.0
    dot = sum(x * y for x, y in zip(a, b, ))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(x * x for x in b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def x__cosine_similarity__mutmut_16(a: list[float], b: list[float]) -> float:
    """Compute cosine similarity between two vectors."""
    if not a or not b or len(a) != len(b):
        return 0.0
    dot = sum(x * y for x, y in zip(a, b, strict=True))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(x * x for x in b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def x__cosine_similarity__mutmut_17(a: list[float], b: list[float]) -> float:
    """Compute cosine similarity between two vectors."""
    if not a or not b or len(a) != len(b):
        return 0.0
    dot = sum(x * y for x, y in zip(a, b, strict=False))
    norm_a = None
    norm_b = math.sqrt(sum(x * x for x in b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def x__cosine_similarity__mutmut_18(a: list[float], b: list[float]) -> float:
    """Compute cosine similarity between two vectors."""
    if not a or not b or len(a) != len(b):
        return 0.0
    dot = sum(x * y for x, y in zip(a, b, strict=False))
    norm_a = math.sqrt(None)
    norm_b = math.sqrt(sum(x * x for x in b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def x__cosine_similarity__mutmut_19(a: list[float], b: list[float]) -> float:
    """Compute cosine similarity between two vectors."""
    if not a or not b or len(a) != len(b):
        return 0.0
    dot = sum(x * y for x, y in zip(a, b, strict=False))
    norm_a = math.sqrt(sum(None))
    norm_b = math.sqrt(sum(x * x for x in b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def x__cosine_similarity__mutmut_20(a: list[float], b: list[float]) -> float:
    """Compute cosine similarity between two vectors."""
    if not a or not b or len(a) != len(b):
        return 0.0
    dot = sum(x * y for x, y in zip(a, b, strict=False))
    norm_a = math.sqrt(sum(x / x for x in a))
    norm_b = math.sqrt(sum(x * x for x in b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def x__cosine_similarity__mutmut_21(a: list[float], b: list[float]) -> float:
    """Compute cosine similarity between two vectors."""
    if not a or not b or len(a) != len(b):
        return 0.0
    dot = sum(x * y for x, y in zip(a, b, strict=False))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = None
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def x__cosine_similarity__mutmut_22(a: list[float], b: list[float]) -> float:
    """Compute cosine similarity between two vectors."""
    if not a or not b or len(a) != len(b):
        return 0.0
    dot = sum(x * y for x, y in zip(a, b, strict=False))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(None)
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def x__cosine_similarity__mutmut_23(a: list[float], b: list[float]) -> float:
    """Compute cosine similarity between two vectors."""
    if not a or not b or len(a) != len(b):
        return 0.0
    dot = sum(x * y for x, y in zip(a, b, strict=False))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(None))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def x__cosine_similarity__mutmut_24(a: list[float], b: list[float]) -> float:
    """Compute cosine similarity between two vectors."""
    if not a or not b or len(a) != len(b):
        return 0.0
    dot = sum(x * y for x, y in zip(a, b, strict=False))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(x / x for x in b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def x__cosine_similarity__mutmut_25(a: list[float], b: list[float]) -> float:
    """Compute cosine similarity between two vectors."""
    if not a or not b or len(a) != len(b):
        return 0.0
    dot = sum(x * y for x, y in zip(a, b, strict=False))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(x * x for x in b))
    if norm_a == 0 and norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def x__cosine_similarity__mutmut_26(a: list[float], b: list[float]) -> float:
    """Compute cosine similarity between two vectors."""
    if not a or not b or len(a) != len(b):
        return 0.0
    dot = sum(x * y for x, y in zip(a, b, strict=False))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(x * x for x in b))
    if norm_a != 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def x__cosine_similarity__mutmut_27(a: list[float], b: list[float]) -> float:
    """Compute cosine similarity between two vectors."""
    if not a or not b or len(a) != len(b):
        return 0.0
    dot = sum(x * y for x, y in zip(a, b, strict=False))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(x * x for x in b))
    if norm_a == 1 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def x__cosine_similarity__mutmut_28(a: list[float], b: list[float]) -> float:
    """Compute cosine similarity between two vectors."""
    if not a or not b or len(a) != len(b):
        return 0.0
    dot = sum(x * y for x, y in zip(a, b, strict=False))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(x * x for x in b))
    if norm_a == 0 or norm_b != 0:
        return 0.0
    return dot / (norm_a * norm_b)


def x__cosine_similarity__mutmut_29(a: list[float], b: list[float]) -> float:
    """Compute cosine similarity between two vectors."""
    if not a or not b or len(a) != len(b):
        return 0.0
    dot = sum(x * y for x, y in zip(a, b, strict=False))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(x * x for x in b))
    if norm_a == 0 or norm_b == 1:
        return 0.0
    return dot / (norm_a * norm_b)


def x__cosine_similarity__mutmut_30(a: list[float], b: list[float]) -> float:
    """Compute cosine similarity between two vectors."""
    if not a or not b or len(a) != len(b):
        return 0.0
    dot = sum(x * y for x, y in zip(a, b, strict=False))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(x * x for x in b))
    if norm_a == 0 or norm_b == 0:
        return 1.0
    return dot / (norm_a * norm_b)


def x__cosine_similarity__mutmut_31(a: list[float], b: list[float]) -> float:
    """Compute cosine similarity between two vectors."""
    if not a or not b or len(a) != len(b):
        return 0.0
    dot = sum(x * y for x, y in zip(a, b, strict=False))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(x * x for x in b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot * (norm_a * norm_b)


def x__cosine_similarity__mutmut_32(a: list[float], b: list[float]) -> float:
    """Compute cosine similarity between two vectors."""
    if not a or not b or len(a) != len(b):
        return 0.0
    dot = sum(x * y for x, y in zip(a, b, strict=False))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(x * x for x in b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a / norm_b)

mutants_x__cosine_similarity__mutmut['_mutmut_orig'] = x__cosine_similarity__mutmut_orig # type: ignore # mutmut generated
mutants_x__cosine_similarity__mutmut['x__cosine_similarity__mutmut_1'] = x__cosine_similarity__mutmut_1 # type: ignore # mutmut generated
mutants_x__cosine_similarity__mutmut['x__cosine_similarity__mutmut_2'] = x__cosine_similarity__mutmut_2 # type: ignore # mutmut generated
mutants_x__cosine_similarity__mutmut['x__cosine_similarity__mutmut_3'] = x__cosine_similarity__mutmut_3 # type: ignore # mutmut generated
mutants_x__cosine_similarity__mutmut['x__cosine_similarity__mutmut_4'] = x__cosine_similarity__mutmut_4 # type: ignore # mutmut generated
mutants_x__cosine_similarity__mutmut['x__cosine_similarity__mutmut_5'] = x__cosine_similarity__mutmut_5 # type: ignore # mutmut generated
mutants_x__cosine_similarity__mutmut['x__cosine_similarity__mutmut_6'] = x__cosine_similarity__mutmut_6 # type: ignore # mutmut generated
mutants_x__cosine_similarity__mutmut['x__cosine_similarity__mutmut_7'] = x__cosine_similarity__mutmut_7 # type: ignore # mutmut generated
mutants_x__cosine_similarity__mutmut['x__cosine_similarity__mutmut_8'] = x__cosine_similarity__mutmut_8 # type: ignore # mutmut generated
mutants_x__cosine_similarity__mutmut['x__cosine_similarity__mutmut_9'] = x__cosine_similarity__mutmut_9 # type: ignore # mutmut generated
mutants_x__cosine_similarity__mutmut['x__cosine_similarity__mutmut_10'] = x__cosine_similarity__mutmut_10 # type: ignore # mutmut generated
mutants_x__cosine_similarity__mutmut['x__cosine_similarity__mutmut_11'] = x__cosine_similarity__mutmut_11 # type: ignore # mutmut generated
mutants_x__cosine_similarity__mutmut['x__cosine_similarity__mutmut_12'] = x__cosine_similarity__mutmut_12 # type: ignore # mutmut generated
mutants_x__cosine_similarity__mutmut['x__cosine_similarity__mutmut_13'] = x__cosine_similarity__mutmut_13 # type: ignore # mutmut generated
mutants_x__cosine_similarity__mutmut['x__cosine_similarity__mutmut_14'] = x__cosine_similarity__mutmut_14 # type: ignore # mutmut generated
mutants_x__cosine_similarity__mutmut['x__cosine_similarity__mutmut_15'] = x__cosine_similarity__mutmut_15 # type: ignore # mutmut generated
mutants_x__cosine_similarity__mutmut['x__cosine_similarity__mutmut_16'] = x__cosine_similarity__mutmut_16 # type: ignore # mutmut generated
mutants_x__cosine_similarity__mutmut['x__cosine_similarity__mutmut_17'] = x__cosine_similarity__mutmut_17 # type: ignore # mutmut generated
mutants_x__cosine_similarity__mutmut['x__cosine_similarity__mutmut_18'] = x__cosine_similarity__mutmut_18 # type: ignore # mutmut generated
mutants_x__cosine_similarity__mutmut['x__cosine_similarity__mutmut_19'] = x__cosine_similarity__mutmut_19 # type: ignore # mutmut generated
mutants_x__cosine_similarity__mutmut['x__cosine_similarity__mutmut_20'] = x__cosine_similarity__mutmut_20 # type: ignore # mutmut generated
mutants_x__cosine_similarity__mutmut['x__cosine_similarity__mutmut_21'] = x__cosine_similarity__mutmut_21 # type: ignore # mutmut generated
mutants_x__cosine_similarity__mutmut['x__cosine_similarity__mutmut_22'] = x__cosine_similarity__mutmut_22 # type: ignore # mutmut generated
mutants_x__cosine_similarity__mutmut['x__cosine_similarity__mutmut_23'] = x__cosine_similarity__mutmut_23 # type: ignore # mutmut generated
mutants_x__cosine_similarity__mutmut['x__cosine_similarity__mutmut_24'] = x__cosine_similarity__mutmut_24 # type: ignore # mutmut generated
mutants_x__cosine_similarity__mutmut['x__cosine_similarity__mutmut_25'] = x__cosine_similarity__mutmut_25 # type: ignore # mutmut generated
mutants_x__cosine_similarity__mutmut['x__cosine_similarity__mutmut_26'] = x__cosine_similarity__mutmut_26 # type: ignore # mutmut generated
mutants_x__cosine_similarity__mutmut['x__cosine_similarity__mutmut_27'] = x__cosine_similarity__mutmut_27 # type: ignore # mutmut generated
mutants_x__cosine_similarity__mutmut['x__cosine_similarity__mutmut_28'] = x__cosine_similarity__mutmut_28 # type: ignore # mutmut generated
mutants_x__cosine_similarity__mutmut['x__cosine_similarity__mutmut_29'] = x__cosine_similarity__mutmut_29 # type: ignore # mutmut generated
mutants_x__cosine_similarity__mutmut['x__cosine_similarity__mutmut_30'] = x__cosine_similarity__mutmut_30 # type: ignore # mutmut generated
mutants_x__cosine_similarity__mutmut['x__cosine_similarity__mutmut_31'] = x__cosine_similarity__mutmut_31 # type: ignore # mutmut generated
mutants_x__cosine_similarity__mutmut['x__cosine_similarity__mutmut_32'] = x__cosine_similarity__mutmut_32 # type: ignore # mutmut generated
mutants_x__simple_embedding__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__simple_embedding__mutmut)
def _simple_embedding(text: str, dim: int = 64) -> list[float]:
    """Simple hash-based embedding for demo/fallback.

    Production agents should use real embeddings (OpenAI, HuggingFace, etc.)
    This uses a deterministic character-based hash projection.
    """
    embedding = [0.0] * dim
    if not text:
        return embedding
    for i, char in enumerate(text):
        idx = i % dim
        embedding[idx] += (ord(char) * 0.01)
    # Normalize
    norm = math.sqrt(sum(x * x for x in embedding))
    if norm > 0:
        embedding = [x / norm for x in embedding]
    return embedding


def x__simple_embedding__mutmut_orig(text: str, dim: int = 64) -> list[float]:
    """Simple hash-based embedding for demo/fallback.

    Production agents should use real embeddings (OpenAI, HuggingFace, etc.)
    This uses a deterministic character-based hash projection.
    """
    embedding = [0.0] * dim
    if not text:
        return embedding
    for i, char in enumerate(text):
        idx = i % dim
        embedding[idx] += (ord(char) * 0.01)
    # Normalize
    norm = math.sqrt(sum(x * x for x in embedding))
    if norm > 0:
        embedding = [x / norm for x in embedding]
    return embedding


def x__simple_embedding__mutmut_1(text: str, dim: int = 65) -> list[float]:
    """Simple hash-based embedding for demo/fallback.

    Production agents should use real embeddings (OpenAI, HuggingFace, etc.)
    This uses a deterministic character-based hash projection.
    """
    embedding = [0.0] * dim
    if not text:
        return embedding
    for i, char in enumerate(text):
        idx = i % dim
        embedding[idx] += (ord(char) * 0.01)
    # Normalize
    norm = math.sqrt(sum(x * x for x in embedding))
    if norm > 0:
        embedding = [x / norm for x in embedding]
    return embedding


def x__simple_embedding__mutmut_2(text: str, dim: int = 64) -> list[float]:
    """Simple hash-based embedding for demo/fallback.

    Production agents should use real embeddings (OpenAI, HuggingFace, etc.)
    This uses a deterministic character-based hash projection.
    """
    embedding = None
    if not text:
        return embedding
    for i, char in enumerate(text):
        idx = i % dim
        embedding[idx] += (ord(char) * 0.01)
    # Normalize
    norm = math.sqrt(sum(x * x for x in embedding))
    if norm > 0:
        embedding = [x / norm for x in embedding]
    return embedding


def x__simple_embedding__mutmut_3(text: str, dim: int = 64) -> list[float]:
    """Simple hash-based embedding for demo/fallback.

    Production agents should use real embeddings (OpenAI, HuggingFace, etc.)
    This uses a deterministic character-based hash projection.
    """
    embedding = [0.0] / dim
    if not text:
        return embedding
    for i, char in enumerate(text):
        idx = i % dim
        embedding[idx] += (ord(char) * 0.01)
    # Normalize
    norm = math.sqrt(sum(x * x for x in embedding))
    if norm > 0:
        embedding = [x / norm for x in embedding]
    return embedding


def x__simple_embedding__mutmut_4(text: str, dim: int = 64) -> list[float]:
    """Simple hash-based embedding for demo/fallback.

    Production agents should use real embeddings (OpenAI, HuggingFace, etc.)
    This uses a deterministic character-based hash projection.
    """
    embedding = [1.0] * dim
    if not text:
        return embedding
    for i, char in enumerate(text):
        idx = i % dim
        embedding[idx] += (ord(char) * 0.01)
    # Normalize
    norm = math.sqrt(sum(x * x for x in embedding))
    if norm > 0:
        embedding = [x / norm for x in embedding]
    return embedding


def x__simple_embedding__mutmut_5(text: str, dim: int = 64) -> list[float]:
    """Simple hash-based embedding for demo/fallback.

    Production agents should use real embeddings (OpenAI, HuggingFace, etc.)
    This uses a deterministic character-based hash projection.
    """
    embedding = [0.0] * dim
    if text:
        return embedding
    for i, char in enumerate(text):
        idx = i % dim
        embedding[idx] += (ord(char) * 0.01)
    # Normalize
    norm = math.sqrt(sum(x * x for x in embedding))
    if norm > 0:
        embedding = [x / norm for x in embedding]
    return embedding


def x__simple_embedding__mutmut_6(text: str, dim: int = 64) -> list[float]:
    """Simple hash-based embedding for demo/fallback.

    Production agents should use real embeddings (OpenAI, HuggingFace, etc.)
    This uses a deterministic character-based hash projection.
    """
    embedding = [0.0] * dim
    if not text:
        return embedding
    for i, char in enumerate(None):
        idx = i % dim
        embedding[idx] += (ord(char) * 0.01)
    # Normalize
    norm = math.sqrt(sum(x * x for x in embedding))
    if norm > 0:
        embedding = [x / norm for x in embedding]
    return embedding


def x__simple_embedding__mutmut_7(text: str, dim: int = 64) -> list[float]:
    """Simple hash-based embedding for demo/fallback.

    Production agents should use real embeddings (OpenAI, HuggingFace, etc.)
    This uses a deterministic character-based hash projection.
    """
    embedding = [0.0] * dim
    if not text:
        return embedding
    for i, char in enumerate(text):
        idx = None
        embedding[idx] += (ord(char) * 0.01)
    # Normalize
    norm = math.sqrt(sum(x * x for x in embedding))
    if norm > 0:
        embedding = [x / norm for x in embedding]
    return embedding


def x__simple_embedding__mutmut_8(text: str, dim: int = 64) -> list[float]:
    """Simple hash-based embedding for demo/fallback.

    Production agents should use real embeddings (OpenAI, HuggingFace, etc.)
    This uses a deterministic character-based hash projection.
    """
    embedding = [0.0] * dim
    if not text:
        return embedding
    for i, char in enumerate(text):
        idx = i / dim
        embedding[idx] += (ord(char) * 0.01)
    # Normalize
    norm = math.sqrt(sum(x * x for x in embedding))
    if norm > 0:
        embedding = [x / norm for x in embedding]
    return embedding


def x__simple_embedding__mutmut_9(text: str, dim: int = 64) -> list[float]:
    """Simple hash-based embedding for demo/fallback.

    Production agents should use real embeddings (OpenAI, HuggingFace, etc.)
    This uses a deterministic character-based hash projection.
    """
    embedding = [0.0] * dim
    if not text:
        return embedding
    for i, char in enumerate(text):
        idx = i % dim
        embedding[idx] = (ord(char) * 0.01)
    # Normalize
    norm = math.sqrt(sum(x * x for x in embedding))
    if norm > 0:
        embedding = [x / norm for x in embedding]
    return embedding


def x__simple_embedding__mutmut_10(text: str, dim: int = 64) -> list[float]:
    """Simple hash-based embedding for demo/fallback.

    Production agents should use real embeddings (OpenAI, HuggingFace, etc.)
    This uses a deterministic character-based hash projection.
    """
    embedding = [0.0] * dim
    if not text:
        return embedding
    for i, char in enumerate(text):
        idx = i % dim
        embedding[idx] -= (ord(char) * 0.01)
    # Normalize
    norm = math.sqrt(sum(x * x for x in embedding))
    if norm > 0:
        embedding = [x / norm for x in embedding]
    return embedding


def x__simple_embedding__mutmut_11(text: str, dim: int = 64) -> list[float]:
    """Simple hash-based embedding for demo/fallback.

    Production agents should use real embeddings (OpenAI, HuggingFace, etc.)
    This uses a deterministic character-based hash projection.
    """
    embedding = [0.0] * dim
    if not text:
        return embedding
    for i, char in enumerate(text):
        idx = i % dim
        embedding[idx] += (ord(char) / 0.01)
    # Normalize
    norm = math.sqrt(sum(x * x for x in embedding))
    if norm > 0:
        embedding = [x / norm for x in embedding]
    return embedding


def x__simple_embedding__mutmut_12(text: str, dim: int = 64) -> list[float]:
    """Simple hash-based embedding for demo/fallback.

    Production agents should use real embeddings (OpenAI, HuggingFace, etc.)
    This uses a deterministic character-based hash projection.
    """
    embedding = [0.0] * dim
    if not text:
        return embedding
    for i, char in enumerate(text):
        idx = i % dim
        embedding[idx] += (ord(None) * 0.01)
    # Normalize
    norm = math.sqrt(sum(x * x for x in embedding))
    if norm > 0:
        embedding = [x / norm for x in embedding]
    return embedding


def x__simple_embedding__mutmut_13(text: str, dim: int = 64) -> list[float]:
    """Simple hash-based embedding for demo/fallback.

    Production agents should use real embeddings (OpenAI, HuggingFace, etc.)
    This uses a deterministic character-based hash projection.
    """
    embedding = [0.0] * dim
    if not text:
        return embedding
    for i, char in enumerate(text):
        idx = i % dim
        embedding[idx] += (ord(char) * 1.01)
    # Normalize
    norm = math.sqrt(sum(x * x for x in embedding))
    if norm > 0:
        embedding = [x / norm for x in embedding]
    return embedding


def x__simple_embedding__mutmut_14(text: str, dim: int = 64) -> list[float]:
    """Simple hash-based embedding for demo/fallback.

    Production agents should use real embeddings (OpenAI, HuggingFace, etc.)
    This uses a deterministic character-based hash projection.
    """
    embedding = [0.0] * dim
    if not text:
        return embedding
    for i, char in enumerate(text):
        idx = i % dim
        embedding[idx] += (ord(char) * 0.01)
    # Normalize
    norm = None
    if norm > 0:
        embedding = [x / norm for x in embedding]
    return embedding


def x__simple_embedding__mutmut_15(text: str, dim: int = 64) -> list[float]:
    """Simple hash-based embedding for demo/fallback.

    Production agents should use real embeddings (OpenAI, HuggingFace, etc.)
    This uses a deterministic character-based hash projection.
    """
    embedding = [0.0] * dim
    if not text:
        return embedding
    for i, char in enumerate(text):
        idx = i % dim
        embedding[idx] += (ord(char) * 0.01)
    # Normalize
    norm = math.sqrt(None)
    if norm > 0:
        embedding = [x / norm for x in embedding]
    return embedding


def x__simple_embedding__mutmut_16(text: str, dim: int = 64) -> list[float]:
    """Simple hash-based embedding for demo/fallback.

    Production agents should use real embeddings (OpenAI, HuggingFace, etc.)
    This uses a deterministic character-based hash projection.
    """
    embedding = [0.0] * dim
    if not text:
        return embedding
    for i, char in enumerate(text):
        idx = i % dim
        embedding[idx] += (ord(char) * 0.01)
    # Normalize
    norm = math.sqrt(sum(None))
    if norm > 0:
        embedding = [x / norm for x in embedding]
    return embedding


def x__simple_embedding__mutmut_17(text: str, dim: int = 64) -> list[float]:
    """Simple hash-based embedding for demo/fallback.

    Production agents should use real embeddings (OpenAI, HuggingFace, etc.)
    This uses a deterministic character-based hash projection.
    """
    embedding = [0.0] * dim
    if not text:
        return embedding
    for i, char in enumerate(text):
        idx = i % dim
        embedding[idx] += (ord(char) * 0.01)
    # Normalize
    norm = math.sqrt(sum(x / x for x in embedding))
    if norm > 0:
        embedding = [x / norm for x in embedding]
    return embedding


def x__simple_embedding__mutmut_18(text: str, dim: int = 64) -> list[float]:
    """Simple hash-based embedding for demo/fallback.

    Production agents should use real embeddings (OpenAI, HuggingFace, etc.)
    This uses a deterministic character-based hash projection.
    """
    embedding = [0.0] * dim
    if not text:
        return embedding
    for i, char in enumerate(text):
        idx = i % dim
        embedding[idx] += (ord(char) * 0.01)
    # Normalize
    norm = math.sqrt(sum(x * x for x in embedding))
    if norm >= 0:
        embedding = [x / norm for x in embedding]
    return embedding


def x__simple_embedding__mutmut_19(text: str, dim: int = 64) -> list[float]:
    """Simple hash-based embedding for demo/fallback.

    Production agents should use real embeddings (OpenAI, HuggingFace, etc.)
    This uses a deterministic character-based hash projection.
    """
    embedding = [0.0] * dim
    if not text:
        return embedding
    for i, char in enumerate(text):
        idx = i % dim
        embedding[idx] += (ord(char) * 0.01)
    # Normalize
    norm = math.sqrt(sum(x * x for x in embedding))
    if norm > 1:
        embedding = [x / norm for x in embedding]
    return embedding


def x__simple_embedding__mutmut_20(text: str, dim: int = 64) -> list[float]:
    """Simple hash-based embedding for demo/fallback.

    Production agents should use real embeddings (OpenAI, HuggingFace, etc.)
    This uses a deterministic character-based hash projection.
    """
    embedding = [0.0] * dim
    if not text:
        return embedding
    for i, char in enumerate(text):
        idx = i % dim
        embedding[idx] += (ord(char) * 0.01)
    # Normalize
    norm = math.sqrt(sum(x * x for x in embedding))
    if norm > 0:
        embedding = None
    return embedding


def x__simple_embedding__mutmut_21(text: str, dim: int = 64) -> list[float]:
    """Simple hash-based embedding for demo/fallback.

    Production agents should use real embeddings (OpenAI, HuggingFace, etc.)
    This uses a deterministic character-based hash projection.
    """
    embedding = [0.0] * dim
    if not text:
        return embedding
    for i, char in enumerate(text):
        idx = i % dim
        embedding[idx] += (ord(char) * 0.01)
    # Normalize
    norm = math.sqrt(sum(x * x for x in embedding))
    if norm > 0:
        embedding = [x * norm for x in embedding]
    return embedding

mutants_x__simple_embedding__mutmut['_mutmut_orig'] = x__simple_embedding__mutmut_orig # type: ignore # mutmut generated
mutants_x__simple_embedding__mutmut['x__simple_embedding__mutmut_1'] = x__simple_embedding__mutmut_1 # type: ignore # mutmut generated
mutants_x__simple_embedding__mutmut['x__simple_embedding__mutmut_2'] = x__simple_embedding__mutmut_2 # type: ignore # mutmut generated
mutants_x__simple_embedding__mutmut['x__simple_embedding__mutmut_3'] = x__simple_embedding__mutmut_3 # type: ignore # mutmut generated
mutants_x__simple_embedding__mutmut['x__simple_embedding__mutmut_4'] = x__simple_embedding__mutmut_4 # type: ignore # mutmut generated
mutants_x__simple_embedding__mutmut['x__simple_embedding__mutmut_5'] = x__simple_embedding__mutmut_5 # type: ignore # mutmut generated
mutants_x__simple_embedding__mutmut['x__simple_embedding__mutmut_6'] = x__simple_embedding__mutmut_6 # type: ignore # mutmut generated
mutants_x__simple_embedding__mutmut['x__simple_embedding__mutmut_7'] = x__simple_embedding__mutmut_7 # type: ignore # mutmut generated
mutants_x__simple_embedding__mutmut['x__simple_embedding__mutmut_8'] = x__simple_embedding__mutmut_8 # type: ignore # mutmut generated
mutants_x__simple_embedding__mutmut['x__simple_embedding__mutmut_9'] = x__simple_embedding__mutmut_9 # type: ignore # mutmut generated
mutants_x__simple_embedding__mutmut['x__simple_embedding__mutmut_10'] = x__simple_embedding__mutmut_10 # type: ignore # mutmut generated
mutants_x__simple_embedding__mutmut['x__simple_embedding__mutmut_11'] = x__simple_embedding__mutmut_11 # type: ignore # mutmut generated
mutants_x__simple_embedding__mutmut['x__simple_embedding__mutmut_12'] = x__simple_embedding__mutmut_12 # type: ignore # mutmut generated
mutants_x__simple_embedding__mutmut['x__simple_embedding__mutmut_13'] = x__simple_embedding__mutmut_13 # type: ignore # mutmut generated
mutants_x__simple_embedding__mutmut['x__simple_embedding__mutmut_14'] = x__simple_embedding__mutmut_14 # type: ignore # mutmut generated
mutants_x__simple_embedding__mutmut['x__simple_embedding__mutmut_15'] = x__simple_embedding__mutmut_15 # type: ignore # mutmut generated
mutants_x__simple_embedding__mutmut['x__simple_embedding__mutmut_16'] = x__simple_embedding__mutmut_16 # type: ignore # mutmut generated
mutants_x__simple_embedding__mutmut['x__simple_embedding__mutmut_17'] = x__simple_embedding__mutmut_17 # type: ignore # mutmut generated
mutants_x__simple_embedding__mutmut['x__simple_embedding__mutmut_18'] = x__simple_embedding__mutmut_18 # type: ignore # mutmut generated
mutants_x__simple_embedding__mutmut['x__simple_embedding__mutmut_19'] = x__simple_embedding__mutmut_19 # type: ignore # mutmut generated
mutants_x__simple_embedding__mutmut['x__simple_embedding__mutmut_20'] = x__simple_embedding__mutmut_20 # type: ignore # mutmut generated
mutants_x__simple_embedding__mutmut['x__simple_embedding__mutmut_21'] = x__simple_embedding__mutmut_21 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁAgentMemoryǁ_init_db__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAgentMemoryǁstore__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAgentMemoryǁ_persist_entry__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAgentMemoryǁrecall__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAgentMemoryǁ_search_entries__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAgentMemoryǁ_search_db__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAgentMemoryǁ_row_to_entry__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAgentMemoryǁconsolidate__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAgentMemoryǁforget__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAgentMemoryǁclear__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAgentMemoryǁget_stats__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAgentMemoryǁclose__mutmut: MutantDict = {}  # type: ignore


class AgentMemory:
    """Agent memory system with short-term and long-term storage.

    Short-term memory is a sliding window of recent entries.
    Long-term memory is persisted in SQLite with vector similarity search.

    Usage:
        memory = AgentMemory(agent_id="agent-1", db_path=":memory:")
        memory.store("User asked about invoices", entry_type="observation")
        results = memory.recall("invoices", limit=5)
    """

    @_mutmut_mutated(mutants_xǁAgentMemoryǁ__init____mutmut)
    def __init__(
        self,
        agent_id: str,
        db_path: str = "agent_memory.db",
        short_term_limit: int = 100,
        embedding_fn: Any | None = None,
    ) -> None:
        self.agent_id = agent_id
        self._db_path = db_path
        self._short_term_limit = short_term_limit
        self._embedding_fn = embedding_fn or _simple_embedding
        self._short_term: list[MemoryEntry] = []
        self._lock = threading.Lock()
        self._conn: sqlite3.Connection | None = None
        self._init_db()

    def xǁAgentMemoryǁ__init____mutmut_orig(
        self,
        agent_id: str,
        db_path: str = "agent_memory.db",
        short_term_limit: int = 100,
        embedding_fn: Any | None = None,
    ) -> None:
        self.agent_id = agent_id
        self._db_path = db_path
        self._short_term_limit = short_term_limit
        self._embedding_fn = embedding_fn or _simple_embedding
        self._short_term: list[MemoryEntry] = []
        self._lock = threading.Lock()
        self._conn: sqlite3.Connection | None = None
        self._init_db()

    def xǁAgentMemoryǁ__init____mutmut_1(
        self,
        agent_id: str,
        db_path: str = "XXagent_memory.dbXX",
        short_term_limit: int = 100,
        embedding_fn: Any | None = None,
    ) -> None:
        self.agent_id = agent_id
        self._db_path = db_path
        self._short_term_limit = short_term_limit
        self._embedding_fn = embedding_fn or _simple_embedding
        self._short_term: list[MemoryEntry] = []
        self._lock = threading.Lock()
        self._conn: sqlite3.Connection | None = None
        self._init_db()

    def xǁAgentMemoryǁ__init____mutmut_2(
        self,
        agent_id: str,
        db_path: str = "AGENT_MEMORY.DB",
        short_term_limit: int = 100,
        embedding_fn: Any | None = None,
    ) -> None:
        self.agent_id = agent_id
        self._db_path = db_path
        self._short_term_limit = short_term_limit
        self._embedding_fn = embedding_fn or _simple_embedding
        self._short_term: list[MemoryEntry] = []
        self._lock = threading.Lock()
        self._conn: sqlite3.Connection | None = None
        self._init_db()

    def xǁAgentMemoryǁ__init____mutmut_3(
        self,
        agent_id: str,
        db_path: str = "agent_memory.db",
        short_term_limit: int = 101,
        embedding_fn: Any | None = None,
    ) -> None:
        self.agent_id = agent_id
        self._db_path = db_path
        self._short_term_limit = short_term_limit
        self._embedding_fn = embedding_fn or _simple_embedding
        self._short_term: list[MemoryEntry] = []
        self._lock = threading.Lock()
        self._conn: sqlite3.Connection | None = None
        self._init_db()

    def xǁAgentMemoryǁ__init____mutmut_4(
        self,
        agent_id: str,
        db_path: str = "agent_memory.db",
        short_term_limit: int = 100,
        embedding_fn: Any | None = None,
    ) -> None:
        self.agent_id = None
        self._db_path = db_path
        self._short_term_limit = short_term_limit
        self._embedding_fn = embedding_fn or _simple_embedding
        self._short_term: list[MemoryEntry] = []
        self._lock = threading.Lock()
        self._conn: sqlite3.Connection | None = None
        self._init_db()

    def xǁAgentMemoryǁ__init____mutmut_5(
        self,
        agent_id: str,
        db_path: str = "agent_memory.db",
        short_term_limit: int = 100,
        embedding_fn: Any | None = None,
    ) -> None:
        self.agent_id = agent_id
        self._db_path = None
        self._short_term_limit = short_term_limit
        self._embedding_fn = embedding_fn or _simple_embedding
        self._short_term: list[MemoryEntry] = []
        self._lock = threading.Lock()
        self._conn: sqlite3.Connection | None = None
        self._init_db()

    def xǁAgentMemoryǁ__init____mutmut_6(
        self,
        agent_id: str,
        db_path: str = "agent_memory.db",
        short_term_limit: int = 100,
        embedding_fn: Any | None = None,
    ) -> None:
        self.agent_id = agent_id
        self._db_path = db_path
        self._short_term_limit = None
        self._embedding_fn = embedding_fn or _simple_embedding
        self._short_term: list[MemoryEntry] = []
        self._lock = threading.Lock()
        self._conn: sqlite3.Connection | None = None
        self._init_db()

    def xǁAgentMemoryǁ__init____mutmut_7(
        self,
        agent_id: str,
        db_path: str = "agent_memory.db",
        short_term_limit: int = 100,
        embedding_fn: Any | None = None,
    ) -> None:
        self.agent_id = agent_id
        self._db_path = db_path
        self._short_term_limit = short_term_limit
        self._embedding_fn = None
        self._short_term: list[MemoryEntry] = []
        self._lock = threading.Lock()
        self._conn: sqlite3.Connection | None = None
        self._init_db()

    def xǁAgentMemoryǁ__init____mutmut_8(
        self,
        agent_id: str,
        db_path: str = "agent_memory.db",
        short_term_limit: int = 100,
        embedding_fn: Any | None = None,
    ) -> None:
        self.agent_id = agent_id
        self._db_path = db_path
        self._short_term_limit = short_term_limit
        self._embedding_fn = embedding_fn and _simple_embedding
        self._short_term: list[MemoryEntry] = []
        self._lock = threading.Lock()
        self._conn: sqlite3.Connection | None = None
        self._init_db()

    def xǁAgentMemoryǁ__init____mutmut_9(
        self,
        agent_id: str,
        db_path: str = "agent_memory.db",
        short_term_limit: int = 100,
        embedding_fn: Any | None = None,
    ) -> None:
        self.agent_id = agent_id
        self._db_path = db_path
        self._short_term_limit = short_term_limit
        self._embedding_fn = embedding_fn or _simple_embedding
        self._short_term: list[MemoryEntry] = None
        self._lock = threading.Lock()
        self._conn: sqlite3.Connection | None = None
        self._init_db()

    def xǁAgentMemoryǁ__init____mutmut_10(
        self,
        agent_id: str,
        db_path: str = "agent_memory.db",
        short_term_limit: int = 100,
        embedding_fn: Any | None = None,
    ) -> None:
        self.agent_id = agent_id
        self._db_path = db_path
        self._short_term_limit = short_term_limit
        self._embedding_fn = embedding_fn or _simple_embedding
        self._short_term: list[MemoryEntry] = []
        self._lock = None
        self._conn: sqlite3.Connection | None = None
        self._init_db()

    def xǁAgentMemoryǁ__init____mutmut_11(
        self,
        agent_id: str,
        db_path: str = "agent_memory.db",
        short_term_limit: int = 100,
        embedding_fn: Any | None = None,
    ) -> None:
        self.agent_id = agent_id
        self._db_path = db_path
        self._short_term_limit = short_term_limit
        self._embedding_fn = embedding_fn or _simple_embedding
        self._short_term: list[MemoryEntry] = []
        self._lock = threading.Lock()
        self._conn: sqlite3.Connection | None = ""
        self._init_db()

    @_mutmut_mutated(mutants_xǁAgentMemoryǁ_init_db__mutmut)
    def _init_db(self) -> None:
        """Initialize SQLite storage for long-term memory."""
        self._conn = sqlite3.connect(self._db_path, check_same_thread=False)
        self._conn.execute("""
            CREATE TABLE IF NOT EXISTS agent_memory (
                entry_id TEXT PRIMARY KEY,
                agent_id TEXT NOT NULL,
                content TEXT NOT NULL,
                entry_type TEXT NOT NULL DEFAULT 'observation',
                importance REAL NOT NULL DEFAULT 0.5,
                embedding TEXT NOT NULL DEFAULT '',
                metadata TEXT NOT NULL DEFAULT '{}',
                timestamp REAL NOT NULL,
                access_count INTEGER NOT NULL DEFAULT 0,
                last_accessed REAL NOT NULL
            )
        """)
        self._conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_memory_agent ON agent_memory(agent_id)"
        )
        self._conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_memory_type ON agent_memory(agent_id, entry_type)"
        )
        self._conn.commit()

    def xǁAgentMemoryǁ_init_db__mutmut_orig(self) -> None:
        """Initialize SQLite storage for long-term memory."""
        self._conn = sqlite3.connect(self._db_path, check_same_thread=False)
        self._conn.execute("""
            CREATE TABLE IF NOT EXISTS agent_memory (
                entry_id TEXT PRIMARY KEY,
                agent_id TEXT NOT NULL,
                content TEXT NOT NULL,
                entry_type TEXT NOT NULL DEFAULT 'observation',
                importance REAL NOT NULL DEFAULT 0.5,
                embedding TEXT NOT NULL DEFAULT '',
                metadata TEXT NOT NULL DEFAULT '{}',
                timestamp REAL NOT NULL,
                access_count INTEGER NOT NULL DEFAULT 0,
                last_accessed REAL NOT NULL
            )
        """)
        self._conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_memory_agent ON agent_memory(agent_id)"
        )
        self._conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_memory_type ON agent_memory(agent_id, entry_type)"
        )
        self._conn.commit()

    def xǁAgentMemoryǁ_init_db__mutmut_1(self) -> None:
        """Initialize SQLite storage for long-term memory."""
        self._conn = None
        self._conn.execute("""
            CREATE TABLE IF NOT EXISTS agent_memory (
                entry_id TEXT PRIMARY KEY,
                agent_id TEXT NOT NULL,
                content TEXT NOT NULL,
                entry_type TEXT NOT NULL DEFAULT 'observation',
                importance REAL NOT NULL DEFAULT 0.5,
                embedding TEXT NOT NULL DEFAULT '',
                metadata TEXT NOT NULL DEFAULT '{}',
                timestamp REAL NOT NULL,
                access_count INTEGER NOT NULL DEFAULT 0,
                last_accessed REAL NOT NULL
            )
        """)
        self._conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_memory_agent ON agent_memory(agent_id)"
        )
        self._conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_memory_type ON agent_memory(agent_id, entry_type)"
        )
        self._conn.commit()

    def xǁAgentMemoryǁ_init_db__mutmut_2(self) -> None:
        """Initialize SQLite storage for long-term memory."""
        self._conn = sqlite3.connect(None, check_same_thread=False)
        self._conn.execute("""
            CREATE TABLE IF NOT EXISTS agent_memory (
                entry_id TEXT PRIMARY KEY,
                agent_id TEXT NOT NULL,
                content TEXT NOT NULL,
                entry_type TEXT NOT NULL DEFAULT 'observation',
                importance REAL NOT NULL DEFAULT 0.5,
                embedding TEXT NOT NULL DEFAULT '',
                metadata TEXT NOT NULL DEFAULT '{}',
                timestamp REAL NOT NULL,
                access_count INTEGER NOT NULL DEFAULT 0,
                last_accessed REAL NOT NULL
            )
        """)
        self._conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_memory_agent ON agent_memory(agent_id)"
        )
        self._conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_memory_type ON agent_memory(agent_id, entry_type)"
        )
        self._conn.commit()

    def xǁAgentMemoryǁ_init_db__mutmut_3(self) -> None:
        """Initialize SQLite storage for long-term memory."""
        self._conn = sqlite3.connect(self._db_path, check_same_thread=None)
        self._conn.execute("""
            CREATE TABLE IF NOT EXISTS agent_memory (
                entry_id TEXT PRIMARY KEY,
                agent_id TEXT NOT NULL,
                content TEXT NOT NULL,
                entry_type TEXT NOT NULL DEFAULT 'observation',
                importance REAL NOT NULL DEFAULT 0.5,
                embedding TEXT NOT NULL DEFAULT '',
                metadata TEXT NOT NULL DEFAULT '{}',
                timestamp REAL NOT NULL,
                access_count INTEGER NOT NULL DEFAULT 0,
                last_accessed REAL NOT NULL
            )
        """)
        self._conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_memory_agent ON agent_memory(agent_id)"
        )
        self._conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_memory_type ON agent_memory(agent_id, entry_type)"
        )
        self._conn.commit()

    def xǁAgentMemoryǁ_init_db__mutmut_4(self) -> None:
        """Initialize SQLite storage for long-term memory."""
        self._conn = sqlite3.connect(check_same_thread=False)
        self._conn.execute("""
            CREATE TABLE IF NOT EXISTS agent_memory (
                entry_id TEXT PRIMARY KEY,
                agent_id TEXT NOT NULL,
                content TEXT NOT NULL,
                entry_type TEXT NOT NULL DEFAULT 'observation',
                importance REAL NOT NULL DEFAULT 0.5,
                embedding TEXT NOT NULL DEFAULT '',
                metadata TEXT NOT NULL DEFAULT '{}',
                timestamp REAL NOT NULL,
                access_count INTEGER NOT NULL DEFAULT 0,
                last_accessed REAL NOT NULL
            )
        """)
        self._conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_memory_agent ON agent_memory(agent_id)"
        )
        self._conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_memory_type ON agent_memory(agent_id, entry_type)"
        )
        self._conn.commit()

    def xǁAgentMemoryǁ_init_db__mutmut_5(self) -> None:
        """Initialize SQLite storage for long-term memory."""
        self._conn = sqlite3.connect(self._db_path, )
        self._conn.execute("""
            CREATE TABLE IF NOT EXISTS agent_memory (
                entry_id TEXT PRIMARY KEY,
                agent_id TEXT NOT NULL,
                content TEXT NOT NULL,
                entry_type TEXT NOT NULL DEFAULT 'observation',
                importance REAL NOT NULL DEFAULT 0.5,
                embedding TEXT NOT NULL DEFAULT '',
                metadata TEXT NOT NULL DEFAULT '{}',
                timestamp REAL NOT NULL,
                access_count INTEGER NOT NULL DEFAULT 0,
                last_accessed REAL NOT NULL
            )
        """)
        self._conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_memory_agent ON agent_memory(agent_id)"
        )
        self._conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_memory_type ON agent_memory(agent_id, entry_type)"
        )
        self._conn.commit()

    def xǁAgentMemoryǁ_init_db__mutmut_6(self) -> None:
        """Initialize SQLite storage for long-term memory."""
        self._conn = sqlite3.connect(self._db_path, check_same_thread=True)
        self._conn.execute("""
            CREATE TABLE IF NOT EXISTS agent_memory (
                entry_id TEXT PRIMARY KEY,
                agent_id TEXT NOT NULL,
                content TEXT NOT NULL,
                entry_type TEXT NOT NULL DEFAULT 'observation',
                importance REAL NOT NULL DEFAULT 0.5,
                embedding TEXT NOT NULL DEFAULT '',
                metadata TEXT NOT NULL DEFAULT '{}',
                timestamp REAL NOT NULL,
                access_count INTEGER NOT NULL DEFAULT 0,
                last_accessed REAL NOT NULL
            )
        """)
        self._conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_memory_agent ON agent_memory(agent_id)"
        )
        self._conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_memory_type ON agent_memory(agent_id, entry_type)"
        )
        self._conn.commit()

    def xǁAgentMemoryǁ_init_db__mutmut_7(self) -> None:
        """Initialize SQLite storage for long-term memory."""
        self._conn = sqlite3.connect(self._db_path, check_same_thread=False)
        self._conn.execute(None)
        self._conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_memory_agent ON agent_memory(agent_id)"
        )
        self._conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_memory_type ON agent_memory(agent_id, entry_type)"
        )
        self._conn.commit()

    def xǁAgentMemoryǁ_init_db__mutmut_8(self) -> None:
        """Initialize SQLite storage for long-term memory."""
        self._conn = sqlite3.connect(self._db_path, check_same_thread=False)
        self._conn.execute("""
            CREATE TABLE IF NOT EXISTS agent_memory (
                entry_id TEXT PRIMARY KEY,
                agent_id TEXT NOT NULL,
                content TEXT NOT NULL,
                entry_type TEXT NOT NULL DEFAULT 'observation',
                importance REAL NOT NULL DEFAULT 0.5,
                embedding TEXT NOT NULL DEFAULT '',
                metadata TEXT NOT NULL DEFAULT '{}',
                timestamp REAL NOT NULL,
                access_count INTEGER NOT NULL DEFAULT 0,
                last_accessed REAL NOT NULL
            )
        """)
        self._conn.execute(
            None
        )
        self._conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_memory_type ON agent_memory(agent_id, entry_type)"
        )
        self._conn.commit()

    def xǁAgentMemoryǁ_init_db__mutmut_9(self) -> None:
        """Initialize SQLite storage for long-term memory."""
        self._conn = sqlite3.connect(self._db_path, check_same_thread=False)
        self._conn.execute("""
            CREATE TABLE IF NOT EXISTS agent_memory (
                entry_id TEXT PRIMARY KEY,
                agent_id TEXT NOT NULL,
                content TEXT NOT NULL,
                entry_type TEXT NOT NULL DEFAULT 'observation',
                importance REAL NOT NULL DEFAULT 0.5,
                embedding TEXT NOT NULL DEFAULT '',
                metadata TEXT NOT NULL DEFAULT '{}',
                timestamp REAL NOT NULL,
                access_count INTEGER NOT NULL DEFAULT 0,
                last_accessed REAL NOT NULL
            )
        """)
        self._conn.execute(
            "XXCREATE INDEX IF NOT EXISTS idx_memory_agent ON agent_memory(agent_id)XX"
        )
        self._conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_memory_type ON agent_memory(agent_id, entry_type)"
        )
        self._conn.commit()

    def xǁAgentMemoryǁ_init_db__mutmut_10(self) -> None:
        """Initialize SQLite storage for long-term memory."""
        self._conn = sqlite3.connect(self._db_path, check_same_thread=False)
        self._conn.execute("""
            CREATE TABLE IF NOT EXISTS agent_memory (
                entry_id TEXT PRIMARY KEY,
                agent_id TEXT NOT NULL,
                content TEXT NOT NULL,
                entry_type TEXT NOT NULL DEFAULT 'observation',
                importance REAL NOT NULL DEFAULT 0.5,
                embedding TEXT NOT NULL DEFAULT '',
                metadata TEXT NOT NULL DEFAULT '{}',
                timestamp REAL NOT NULL,
                access_count INTEGER NOT NULL DEFAULT 0,
                last_accessed REAL NOT NULL
            )
        """)
        self._conn.execute(
            "create index if not exists idx_memory_agent on agent_memory(agent_id)"
        )
        self._conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_memory_type ON agent_memory(agent_id, entry_type)"
        )
        self._conn.commit()

    def xǁAgentMemoryǁ_init_db__mutmut_11(self) -> None:
        """Initialize SQLite storage for long-term memory."""
        self._conn = sqlite3.connect(self._db_path, check_same_thread=False)
        self._conn.execute("""
            CREATE TABLE IF NOT EXISTS agent_memory (
                entry_id TEXT PRIMARY KEY,
                agent_id TEXT NOT NULL,
                content TEXT NOT NULL,
                entry_type TEXT NOT NULL DEFAULT 'observation',
                importance REAL NOT NULL DEFAULT 0.5,
                embedding TEXT NOT NULL DEFAULT '',
                metadata TEXT NOT NULL DEFAULT '{}',
                timestamp REAL NOT NULL,
                access_count INTEGER NOT NULL DEFAULT 0,
                last_accessed REAL NOT NULL
            )
        """)
        self._conn.execute(
            "CREATE INDEX IF NOT EXISTS IDX_MEMORY_AGENT ON AGENT_MEMORY(AGENT_ID)"
        )
        self._conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_memory_type ON agent_memory(agent_id, entry_type)"
        )
        self._conn.commit()

    def xǁAgentMemoryǁ_init_db__mutmut_12(self) -> None:
        """Initialize SQLite storage for long-term memory."""
        self._conn = sqlite3.connect(self._db_path, check_same_thread=False)
        self._conn.execute("""
            CREATE TABLE IF NOT EXISTS agent_memory (
                entry_id TEXT PRIMARY KEY,
                agent_id TEXT NOT NULL,
                content TEXT NOT NULL,
                entry_type TEXT NOT NULL DEFAULT 'observation',
                importance REAL NOT NULL DEFAULT 0.5,
                embedding TEXT NOT NULL DEFAULT '',
                metadata TEXT NOT NULL DEFAULT '{}',
                timestamp REAL NOT NULL,
                access_count INTEGER NOT NULL DEFAULT 0,
                last_accessed REAL NOT NULL
            )
        """)
        self._conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_memory_agent ON agent_memory(agent_id)"
        )
        self._conn.execute(
            None
        )
        self._conn.commit()

    def xǁAgentMemoryǁ_init_db__mutmut_13(self) -> None:
        """Initialize SQLite storage for long-term memory."""
        self._conn = sqlite3.connect(self._db_path, check_same_thread=False)
        self._conn.execute("""
            CREATE TABLE IF NOT EXISTS agent_memory (
                entry_id TEXT PRIMARY KEY,
                agent_id TEXT NOT NULL,
                content TEXT NOT NULL,
                entry_type TEXT NOT NULL DEFAULT 'observation',
                importance REAL NOT NULL DEFAULT 0.5,
                embedding TEXT NOT NULL DEFAULT '',
                metadata TEXT NOT NULL DEFAULT '{}',
                timestamp REAL NOT NULL,
                access_count INTEGER NOT NULL DEFAULT 0,
                last_accessed REAL NOT NULL
            )
        """)
        self._conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_memory_agent ON agent_memory(agent_id)"
        )
        self._conn.execute(
            "XXCREATE INDEX IF NOT EXISTS idx_memory_type ON agent_memory(agent_id, entry_type)XX"
        )
        self._conn.commit()

    def xǁAgentMemoryǁ_init_db__mutmut_14(self) -> None:
        """Initialize SQLite storage for long-term memory."""
        self._conn = sqlite3.connect(self._db_path, check_same_thread=False)
        self._conn.execute("""
            CREATE TABLE IF NOT EXISTS agent_memory (
                entry_id TEXT PRIMARY KEY,
                agent_id TEXT NOT NULL,
                content TEXT NOT NULL,
                entry_type TEXT NOT NULL DEFAULT 'observation',
                importance REAL NOT NULL DEFAULT 0.5,
                embedding TEXT NOT NULL DEFAULT '',
                metadata TEXT NOT NULL DEFAULT '{}',
                timestamp REAL NOT NULL,
                access_count INTEGER NOT NULL DEFAULT 0,
                last_accessed REAL NOT NULL
            )
        """)
        self._conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_memory_agent ON agent_memory(agent_id)"
        )
        self._conn.execute(
            "create index if not exists idx_memory_type on agent_memory(agent_id, entry_type)"
        )
        self._conn.commit()

    def xǁAgentMemoryǁ_init_db__mutmut_15(self) -> None:
        """Initialize SQLite storage for long-term memory."""
        self._conn = sqlite3.connect(self._db_path, check_same_thread=False)
        self._conn.execute("""
            CREATE TABLE IF NOT EXISTS agent_memory (
                entry_id TEXT PRIMARY KEY,
                agent_id TEXT NOT NULL,
                content TEXT NOT NULL,
                entry_type TEXT NOT NULL DEFAULT 'observation',
                importance REAL NOT NULL DEFAULT 0.5,
                embedding TEXT NOT NULL DEFAULT '',
                metadata TEXT NOT NULL DEFAULT '{}',
                timestamp REAL NOT NULL,
                access_count INTEGER NOT NULL DEFAULT 0,
                last_accessed REAL NOT NULL
            )
        """)
        self._conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_memory_agent ON agent_memory(agent_id)"
        )
        self._conn.execute(
            "CREATE INDEX IF NOT EXISTS IDX_MEMORY_TYPE ON AGENT_MEMORY(AGENT_ID, ENTRY_TYPE)"
        )
        self._conn.commit()

    # ── Store ───────────────────────────────────────────────

    @_mutmut_mutated(mutants_xǁAgentMemoryǁstore__mutmut)
    def store(
        self,
        content: str,
        entry_type: str = "observation",
        importance: float = 0.5,
        metadata: dict[str, Any] | None = None,
    ) -> MemoryEntry:
        """Store a new memory entry in both short-term and long-term memory.

        Args:
            content: The memory content text.
            entry_type: Type of memory (observation, action, decision, knowledge).
            importance: Importance score 0.0-1.0.
            metadata: Optional metadata dict.

        Returns:
            The created MemoryEntry.
        """
        embedding = self._embedding_fn(content)
        entry = MemoryEntry(
            agent_id=self.agent_id,
            content=content,
            entry_type=entry_type,
            importance=max(0.0, min(1.0, importance)),
            embedding=embedding,
            metadata=metadata or {},
        )

        with self._lock:
            # Short-term
            self._short_term.append(entry)
            if len(self._short_term) > self._short_term_limit:
                self._short_term = self._short_term[-self._short_term_limit:]

            # Long-term (SQLite)
            self._persist_entry(entry)

        return entry

    # ── Store ───────────────────────────────────────────────

    def xǁAgentMemoryǁstore__mutmut_orig(
        self,
        content: str,
        entry_type: str = "observation",
        importance: float = 0.5,
        metadata: dict[str, Any] | None = None,
    ) -> MemoryEntry:
        """Store a new memory entry in both short-term and long-term memory.

        Args:
            content: The memory content text.
            entry_type: Type of memory (observation, action, decision, knowledge).
            importance: Importance score 0.0-1.0.
            metadata: Optional metadata dict.

        Returns:
            The created MemoryEntry.
        """
        embedding = self._embedding_fn(content)
        entry = MemoryEntry(
            agent_id=self.agent_id,
            content=content,
            entry_type=entry_type,
            importance=max(0.0, min(1.0, importance)),
            embedding=embedding,
            metadata=metadata or {},
        )

        with self._lock:
            # Short-term
            self._short_term.append(entry)
            if len(self._short_term) > self._short_term_limit:
                self._short_term = self._short_term[-self._short_term_limit:]

            # Long-term (SQLite)
            self._persist_entry(entry)

        return entry

    # ── Store ───────────────────────────────────────────────

    def xǁAgentMemoryǁstore__mutmut_1(
        self,
        content: str,
        entry_type: str = "XXobservationXX",
        importance: float = 0.5,
        metadata: dict[str, Any] | None = None,
    ) -> MemoryEntry:
        """Store a new memory entry in both short-term and long-term memory.

        Args:
            content: The memory content text.
            entry_type: Type of memory (observation, action, decision, knowledge).
            importance: Importance score 0.0-1.0.
            metadata: Optional metadata dict.

        Returns:
            The created MemoryEntry.
        """
        embedding = self._embedding_fn(content)
        entry = MemoryEntry(
            agent_id=self.agent_id,
            content=content,
            entry_type=entry_type,
            importance=max(0.0, min(1.0, importance)),
            embedding=embedding,
            metadata=metadata or {},
        )

        with self._lock:
            # Short-term
            self._short_term.append(entry)
            if len(self._short_term) > self._short_term_limit:
                self._short_term = self._short_term[-self._short_term_limit:]

            # Long-term (SQLite)
            self._persist_entry(entry)

        return entry

    # ── Store ───────────────────────────────────────────────

    def xǁAgentMemoryǁstore__mutmut_2(
        self,
        content: str,
        entry_type: str = "OBSERVATION",
        importance: float = 0.5,
        metadata: dict[str, Any] | None = None,
    ) -> MemoryEntry:
        """Store a new memory entry in both short-term and long-term memory.

        Args:
            content: The memory content text.
            entry_type: Type of memory (observation, action, decision, knowledge).
            importance: Importance score 0.0-1.0.
            metadata: Optional metadata dict.

        Returns:
            The created MemoryEntry.
        """
        embedding = self._embedding_fn(content)
        entry = MemoryEntry(
            agent_id=self.agent_id,
            content=content,
            entry_type=entry_type,
            importance=max(0.0, min(1.0, importance)),
            embedding=embedding,
            metadata=metadata or {},
        )

        with self._lock:
            # Short-term
            self._short_term.append(entry)
            if len(self._short_term) > self._short_term_limit:
                self._short_term = self._short_term[-self._short_term_limit:]

            # Long-term (SQLite)
            self._persist_entry(entry)

        return entry

    # ── Store ───────────────────────────────────────────────

    def xǁAgentMemoryǁstore__mutmut_3(
        self,
        content: str,
        entry_type: str = "observation",
        importance: float = 1.5,
        metadata: dict[str, Any] | None = None,
    ) -> MemoryEntry:
        """Store a new memory entry in both short-term and long-term memory.

        Args:
            content: The memory content text.
            entry_type: Type of memory (observation, action, decision, knowledge).
            importance: Importance score 0.0-1.0.
            metadata: Optional metadata dict.

        Returns:
            The created MemoryEntry.
        """
        embedding = self._embedding_fn(content)
        entry = MemoryEntry(
            agent_id=self.agent_id,
            content=content,
            entry_type=entry_type,
            importance=max(0.0, min(1.0, importance)),
            embedding=embedding,
            metadata=metadata or {},
        )

        with self._lock:
            # Short-term
            self._short_term.append(entry)
            if len(self._short_term) > self._short_term_limit:
                self._short_term = self._short_term[-self._short_term_limit:]

            # Long-term (SQLite)
            self._persist_entry(entry)

        return entry

    # ── Store ───────────────────────────────────────────────

    def xǁAgentMemoryǁstore__mutmut_4(
        self,
        content: str,
        entry_type: str = "observation",
        importance: float = 0.5,
        metadata: dict[str, Any] | None = None,
    ) -> MemoryEntry:
        """Store a new memory entry in both short-term and long-term memory.

        Args:
            content: The memory content text.
            entry_type: Type of memory (observation, action, decision, knowledge).
            importance: Importance score 0.0-1.0.
            metadata: Optional metadata dict.

        Returns:
            The created MemoryEntry.
        """
        embedding = None
        entry = MemoryEntry(
            agent_id=self.agent_id,
            content=content,
            entry_type=entry_type,
            importance=max(0.0, min(1.0, importance)),
            embedding=embedding,
            metadata=metadata or {},
        )

        with self._lock:
            # Short-term
            self._short_term.append(entry)
            if len(self._short_term) > self._short_term_limit:
                self._short_term = self._short_term[-self._short_term_limit:]

            # Long-term (SQLite)
            self._persist_entry(entry)

        return entry

    # ── Store ───────────────────────────────────────────────

    def xǁAgentMemoryǁstore__mutmut_5(
        self,
        content: str,
        entry_type: str = "observation",
        importance: float = 0.5,
        metadata: dict[str, Any] | None = None,
    ) -> MemoryEntry:
        """Store a new memory entry in both short-term and long-term memory.

        Args:
            content: The memory content text.
            entry_type: Type of memory (observation, action, decision, knowledge).
            importance: Importance score 0.0-1.0.
            metadata: Optional metadata dict.

        Returns:
            The created MemoryEntry.
        """
        embedding = self._embedding_fn(None)
        entry = MemoryEntry(
            agent_id=self.agent_id,
            content=content,
            entry_type=entry_type,
            importance=max(0.0, min(1.0, importance)),
            embedding=embedding,
            metadata=metadata or {},
        )

        with self._lock:
            # Short-term
            self._short_term.append(entry)
            if len(self._short_term) > self._short_term_limit:
                self._short_term = self._short_term[-self._short_term_limit:]

            # Long-term (SQLite)
            self._persist_entry(entry)

        return entry

    # ── Store ───────────────────────────────────────────────

    def xǁAgentMemoryǁstore__mutmut_6(
        self,
        content: str,
        entry_type: str = "observation",
        importance: float = 0.5,
        metadata: dict[str, Any] | None = None,
    ) -> MemoryEntry:
        """Store a new memory entry in both short-term and long-term memory.

        Args:
            content: The memory content text.
            entry_type: Type of memory (observation, action, decision, knowledge).
            importance: Importance score 0.0-1.0.
            metadata: Optional metadata dict.

        Returns:
            The created MemoryEntry.
        """
        embedding = self._embedding_fn(content)
        entry = None

        with self._lock:
            # Short-term
            self._short_term.append(entry)
            if len(self._short_term) > self._short_term_limit:
                self._short_term = self._short_term[-self._short_term_limit:]

            # Long-term (SQLite)
            self._persist_entry(entry)

        return entry

    # ── Store ───────────────────────────────────────────────

    def xǁAgentMemoryǁstore__mutmut_7(
        self,
        content: str,
        entry_type: str = "observation",
        importance: float = 0.5,
        metadata: dict[str, Any] | None = None,
    ) -> MemoryEntry:
        """Store a new memory entry in both short-term and long-term memory.

        Args:
            content: The memory content text.
            entry_type: Type of memory (observation, action, decision, knowledge).
            importance: Importance score 0.0-1.0.
            metadata: Optional metadata dict.

        Returns:
            The created MemoryEntry.
        """
        embedding = self._embedding_fn(content)
        entry = MemoryEntry(
            agent_id=None,
            content=content,
            entry_type=entry_type,
            importance=max(0.0, min(1.0, importance)),
            embedding=embedding,
            metadata=metadata or {},
        )

        with self._lock:
            # Short-term
            self._short_term.append(entry)
            if len(self._short_term) > self._short_term_limit:
                self._short_term = self._short_term[-self._short_term_limit:]

            # Long-term (SQLite)
            self._persist_entry(entry)

        return entry

    # ── Store ───────────────────────────────────────────────

    def xǁAgentMemoryǁstore__mutmut_8(
        self,
        content: str,
        entry_type: str = "observation",
        importance: float = 0.5,
        metadata: dict[str, Any] | None = None,
    ) -> MemoryEntry:
        """Store a new memory entry in both short-term and long-term memory.

        Args:
            content: The memory content text.
            entry_type: Type of memory (observation, action, decision, knowledge).
            importance: Importance score 0.0-1.0.
            metadata: Optional metadata dict.

        Returns:
            The created MemoryEntry.
        """
        embedding = self._embedding_fn(content)
        entry = MemoryEntry(
            agent_id=self.agent_id,
            content=None,
            entry_type=entry_type,
            importance=max(0.0, min(1.0, importance)),
            embedding=embedding,
            metadata=metadata or {},
        )

        with self._lock:
            # Short-term
            self._short_term.append(entry)
            if len(self._short_term) > self._short_term_limit:
                self._short_term = self._short_term[-self._short_term_limit:]

            # Long-term (SQLite)
            self._persist_entry(entry)

        return entry

    # ── Store ───────────────────────────────────────────────

    def xǁAgentMemoryǁstore__mutmut_9(
        self,
        content: str,
        entry_type: str = "observation",
        importance: float = 0.5,
        metadata: dict[str, Any] | None = None,
    ) -> MemoryEntry:
        """Store a new memory entry in both short-term and long-term memory.

        Args:
            content: The memory content text.
            entry_type: Type of memory (observation, action, decision, knowledge).
            importance: Importance score 0.0-1.0.
            metadata: Optional metadata dict.

        Returns:
            The created MemoryEntry.
        """
        embedding = self._embedding_fn(content)
        entry = MemoryEntry(
            agent_id=self.agent_id,
            content=content,
            entry_type=None,
            importance=max(0.0, min(1.0, importance)),
            embedding=embedding,
            metadata=metadata or {},
        )

        with self._lock:
            # Short-term
            self._short_term.append(entry)
            if len(self._short_term) > self._short_term_limit:
                self._short_term = self._short_term[-self._short_term_limit:]

            # Long-term (SQLite)
            self._persist_entry(entry)

        return entry

    # ── Store ───────────────────────────────────────────────

    def xǁAgentMemoryǁstore__mutmut_10(
        self,
        content: str,
        entry_type: str = "observation",
        importance: float = 0.5,
        metadata: dict[str, Any] | None = None,
    ) -> MemoryEntry:
        """Store a new memory entry in both short-term and long-term memory.

        Args:
            content: The memory content text.
            entry_type: Type of memory (observation, action, decision, knowledge).
            importance: Importance score 0.0-1.0.
            metadata: Optional metadata dict.

        Returns:
            The created MemoryEntry.
        """
        embedding = self._embedding_fn(content)
        entry = MemoryEntry(
            agent_id=self.agent_id,
            content=content,
            entry_type=entry_type,
            importance=None,
            embedding=embedding,
            metadata=metadata or {},
        )

        with self._lock:
            # Short-term
            self._short_term.append(entry)
            if len(self._short_term) > self._short_term_limit:
                self._short_term = self._short_term[-self._short_term_limit:]

            # Long-term (SQLite)
            self._persist_entry(entry)

        return entry

    # ── Store ───────────────────────────────────────────────

    def xǁAgentMemoryǁstore__mutmut_11(
        self,
        content: str,
        entry_type: str = "observation",
        importance: float = 0.5,
        metadata: dict[str, Any] | None = None,
    ) -> MemoryEntry:
        """Store a new memory entry in both short-term and long-term memory.

        Args:
            content: The memory content text.
            entry_type: Type of memory (observation, action, decision, knowledge).
            importance: Importance score 0.0-1.0.
            metadata: Optional metadata dict.

        Returns:
            The created MemoryEntry.
        """
        embedding = self._embedding_fn(content)
        entry = MemoryEntry(
            agent_id=self.agent_id,
            content=content,
            entry_type=entry_type,
            importance=max(0.0, min(1.0, importance)),
            embedding=None,
            metadata=metadata or {},
        )

        with self._lock:
            # Short-term
            self._short_term.append(entry)
            if len(self._short_term) > self._short_term_limit:
                self._short_term = self._short_term[-self._short_term_limit:]

            # Long-term (SQLite)
            self._persist_entry(entry)

        return entry

    # ── Store ───────────────────────────────────────────────

    def xǁAgentMemoryǁstore__mutmut_12(
        self,
        content: str,
        entry_type: str = "observation",
        importance: float = 0.5,
        metadata: dict[str, Any] | None = None,
    ) -> MemoryEntry:
        """Store a new memory entry in both short-term and long-term memory.

        Args:
            content: The memory content text.
            entry_type: Type of memory (observation, action, decision, knowledge).
            importance: Importance score 0.0-1.0.
            metadata: Optional metadata dict.

        Returns:
            The created MemoryEntry.
        """
        embedding = self._embedding_fn(content)
        entry = MemoryEntry(
            agent_id=self.agent_id,
            content=content,
            entry_type=entry_type,
            importance=max(0.0, min(1.0, importance)),
            embedding=embedding,
            metadata=None,
        )

        with self._lock:
            # Short-term
            self._short_term.append(entry)
            if len(self._short_term) > self._short_term_limit:
                self._short_term = self._short_term[-self._short_term_limit:]

            # Long-term (SQLite)
            self._persist_entry(entry)

        return entry

    # ── Store ───────────────────────────────────────────────

    def xǁAgentMemoryǁstore__mutmut_13(
        self,
        content: str,
        entry_type: str = "observation",
        importance: float = 0.5,
        metadata: dict[str, Any] | None = None,
    ) -> MemoryEntry:
        """Store a new memory entry in both short-term and long-term memory.

        Args:
            content: The memory content text.
            entry_type: Type of memory (observation, action, decision, knowledge).
            importance: Importance score 0.0-1.0.
            metadata: Optional metadata dict.

        Returns:
            The created MemoryEntry.
        """
        embedding = self._embedding_fn(content)
        entry = MemoryEntry(
            content=content,
            entry_type=entry_type,
            importance=max(0.0, min(1.0, importance)),
            embedding=embedding,
            metadata=metadata or {},
        )

        with self._lock:
            # Short-term
            self._short_term.append(entry)
            if len(self._short_term) > self._short_term_limit:
                self._short_term = self._short_term[-self._short_term_limit:]

            # Long-term (SQLite)
            self._persist_entry(entry)

        return entry

    # ── Store ───────────────────────────────────────────────

    def xǁAgentMemoryǁstore__mutmut_14(
        self,
        content: str,
        entry_type: str = "observation",
        importance: float = 0.5,
        metadata: dict[str, Any] | None = None,
    ) -> MemoryEntry:
        """Store a new memory entry in both short-term and long-term memory.

        Args:
            content: The memory content text.
            entry_type: Type of memory (observation, action, decision, knowledge).
            importance: Importance score 0.0-1.0.
            metadata: Optional metadata dict.

        Returns:
            The created MemoryEntry.
        """
        embedding = self._embedding_fn(content)
        entry = MemoryEntry(
            agent_id=self.agent_id,
            entry_type=entry_type,
            importance=max(0.0, min(1.0, importance)),
            embedding=embedding,
            metadata=metadata or {},
        )

        with self._lock:
            # Short-term
            self._short_term.append(entry)
            if len(self._short_term) > self._short_term_limit:
                self._short_term = self._short_term[-self._short_term_limit:]

            # Long-term (SQLite)
            self._persist_entry(entry)

        return entry

    # ── Store ───────────────────────────────────────────────

    def xǁAgentMemoryǁstore__mutmut_15(
        self,
        content: str,
        entry_type: str = "observation",
        importance: float = 0.5,
        metadata: dict[str, Any] | None = None,
    ) -> MemoryEntry:
        """Store a new memory entry in both short-term and long-term memory.

        Args:
            content: The memory content text.
            entry_type: Type of memory (observation, action, decision, knowledge).
            importance: Importance score 0.0-1.0.
            metadata: Optional metadata dict.

        Returns:
            The created MemoryEntry.
        """
        embedding = self._embedding_fn(content)
        entry = MemoryEntry(
            agent_id=self.agent_id,
            content=content,
            importance=max(0.0, min(1.0, importance)),
            embedding=embedding,
            metadata=metadata or {},
        )

        with self._lock:
            # Short-term
            self._short_term.append(entry)
            if len(self._short_term) > self._short_term_limit:
                self._short_term = self._short_term[-self._short_term_limit:]

            # Long-term (SQLite)
            self._persist_entry(entry)

        return entry

    # ── Store ───────────────────────────────────────────────

    def xǁAgentMemoryǁstore__mutmut_16(
        self,
        content: str,
        entry_type: str = "observation",
        importance: float = 0.5,
        metadata: dict[str, Any] | None = None,
    ) -> MemoryEntry:
        """Store a new memory entry in both short-term and long-term memory.

        Args:
            content: The memory content text.
            entry_type: Type of memory (observation, action, decision, knowledge).
            importance: Importance score 0.0-1.0.
            metadata: Optional metadata dict.

        Returns:
            The created MemoryEntry.
        """
        embedding = self._embedding_fn(content)
        entry = MemoryEntry(
            agent_id=self.agent_id,
            content=content,
            entry_type=entry_type,
            embedding=embedding,
            metadata=metadata or {},
        )

        with self._lock:
            # Short-term
            self._short_term.append(entry)
            if len(self._short_term) > self._short_term_limit:
                self._short_term = self._short_term[-self._short_term_limit:]

            # Long-term (SQLite)
            self._persist_entry(entry)

        return entry

    # ── Store ───────────────────────────────────────────────

    def xǁAgentMemoryǁstore__mutmut_17(
        self,
        content: str,
        entry_type: str = "observation",
        importance: float = 0.5,
        metadata: dict[str, Any] | None = None,
    ) -> MemoryEntry:
        """Store a new memory entry in both short-term and long-term memory.

        Args:
            content: The memory content text.
            entry_type: Type of memory (observation, action, decision, knowledge).
            importance: Importance score 0.0-1.0.
            metadata: Optional metadata dict.

        Returns:
            The created MemoryEntry.
        """
        embedding = self._embedding_fn(content)
        entry = MemoryEntry(
            agent_id=self.agent_id,
            content=content,
            entry_type=entry_type,
            importance=max(0.0, min(1.0, importance)),
            metadata=metadata or {},
        )

        with self._lock:
            # Short-term
            self._short_term.append(entry)
            if len(self._short_term) > self._short_term_limit:
                self._short_term = self._short_term[-self._short_term_limit:]

            # Long-term (SQLite)
            self._persist_entry(entry)

        return entry

    # ── Store ───────────────────────────────────────────────

    def xǁAgentMemoryǁstore__mutmut_18(
        self,
        content: str,
        entry_type: str = "observation",
        importance: float = 0.5,
        metadata: dict[str, Any] | None = None,
    ) -> MemoryEntry:
        """Store a new memory entry in both short-term and long-term memory.

        Args:
            content: The memory content text.
            entry_type: Type of memory (observation, action, decision, knowledge).
            importance: Importance score 0.0-1.0.
            metadata: Optional metadata dict.

        Returns:
            The created MemoryEntry.
        """
        embedding = self._embedding_fn(content)
        entry = MemoryEntry(
            agent_id=self.agent_id,
            content=content,
            entry_type=entry_type,
            importance=max(0.0, min(1.0, importance)),
            embedding=embedding,
            )

        with self._lock:
            # Short-term
            self._short_term.append(entry)
            if len(self._short_term) > self._short_term_limit:
                self._short_term = self._short_term[-self._short_term_limit:]

            # Long-term (SQLite)
            self._persist_entry(entry)

        return entry

    # ── Store ───────────────────────────────────────────────

    def xǁAgentMemoryǁstore__mutmut_19(
        self,
        content: str,
        entry_type: str = "observation",
        importance: float = 0.5,
        metadata: dict[str, Any] | None = None,
    ) -> MemoryEntry:
        """Store a new memory entry in both short-term and long-term memory.

        Args:
            content: The memory content text.
            entry_type: Type of memory (observation, action, decision, knowledge).
            importance: Importance score 0.0-1.0.
            metadata: Optional metadata dict.

        Returns:
            The created MemoryEntry.
        """
        embedding = self._embedding_fn(content)
        entry = MemoryEntry(
            agent_id=self.agent_id,
            content=content,
            entry_type=entry_type,
            importance=max(None, min(1.0, importance)),
            embedding=embedding,
            metadata=metadata or {},
        )

        with self._lock:
            # Short-term
            self._short_term.append(entry)
            if len(self._short_term) > self._short_term_limit:
                self._short_term = self._short_term[-self._short_term_limit:]

            # Long-term (SQLite)
            self._persist_entry(entry)

        return entry

    # ── Store ───────────────────────────────────────────────

    def xǁAgentMemoryǁstore__mutmut_20(
        self,
        content: str,
        entry_type: str = "observation",
        importance: float = 0.5,
        metadata: dict[str, Any] | None = None,
    ) -> MemoryEntry:
        """Store a new memory entry in both short-term and long-term memory.

        Args:
            content: The memory content text.
            entry_type: Type of memory (observation, action, decision, knowledge).
            importance: Importance score 0.0-1.0.
            metadata: Optional metadata dict.

        Returns:
            The created MemoryEntry.
        """
        embedding = self._embedding_fn(content)
        entry = MemoryEntry(
            agent_id=self.agent_id,
            content=content,
            entry_type=entry_type,
            importance=max(0.0, None),
            embedding=embedding,
            metadata=metadata or {},
        )

        with self._lock:
            # Short-term
            self._short_term.append(entry)
            if len(self._short_term) > self._short_term_limit:
                self._short_term = self._short_term[-self._short_term_limit:]

            # Long-term (SQLite)
            self._persist_entry(entry)

        return entry

    # ── Store ───────────────────────────────────────────────

    def xǁAgentMemoryǁstore__mutmut_21(
        self,
        content: str,
        entry_type: str = "observation",
        importance: float = 0.5,
        metadata: dict[str, Any] | None = None,
    ) -> MemoryEntry:
        """Store a new memory entry in both short-term and long-term memory.

        Args:
            content: The memory content text.
            entry_type: Type of memory (observation, action, decision, knowledge).
            importance: Importance score 0.0-1.0.
            metadata: Optional metadata dict.

        Returns:
            The created MemoryEntry.
        """
        embedding = self._embedding_fn(content)
        entry = MemoryEntry(
            agent_id=self.agent_id,
            content=content,
            entry_type=entry_type,
            importance=max(min(1.0, importance)),
            embedding=embedding,
            metadata=metadata or {},
        )

        with self._lock:
            # Short-term
            self._short_term.append(entry)
            if len(self._short_term) > self._short_term_limit:
                self._short_term = self._short_term[-self._short_term_limit:]

            # Long-term (SQLite)
            self._persist_entry(entry)

        return entry

    # ── Store ───────────────────────────────────────────────

    def xǁAgentMemoryǁstore__mutmut_22(
        self,
        content: str,
        entry_type: str = "observation",
        importance: float = 0.5,
        metadata: dict[str, Any] | None = None,
    ) -> MemoryEntry:
        """Store a new memory entry in both short-term and long-term memory.

        Args:
            content: The memory content text.
            entry_type: Type of memory (observation, action, decision, knowledge).
            importance: Importance score 0.0-1.0.
            metadata: Optional metadata dict.

        Returns:
            The created MemoryEntry.
        """
        embedding = self._embedding_fn(content)
        entry = MemoryEntry(
            agent_id=self.agent_id,
            content=content,
            entry_type=entry_type,
            importance=max(0.0, ),
            embedding=embedding,
            metadata=metadata or {},
        )

        with self._lock:
            # Short-term
            self._short_term.append(entry)
            if len(self._short_term) > self._short_term_limit:
                self._short_term = self._short_term[-self._short_term_limit:]

            # Long-term (SQLite)
            self._persist_entry(entry)

        return entry

    # ── Store ───────────────────────────────────────────────

    def xǁAgentMemoryǁstore__mutmut_23(
        self,
        content: str,
        entry_type: str = "observation",
        importance: float = 0.5,
        metadata: dict[str, Any] | None = None,
    ) -> MemoryEntry:
        """Store a new memory entry in both short-term and long-term memory.

        Args:
            content: The memory content text.
            entry_type: Type of memory (observation, action, decision, knowledge).
            importance: Importance score 0.0-1.0.
            metadata: Optional metadata dict.

        Returns:
            The created MemoryEntry.
        """
        embedding = self._embedding_fn(content)
        entry = MemoryEntry(
            agent_id=self.agent_id,
            content=content,
            entry_type=entry_type,
            importance=max(1.0, min(1.0, importance)),
            embedding=embedding,
            metadata=metadata or {},
        )

        with self._lock:
            # Short-term
            self._short_term.append(entry)
            if len(self._short_term) > self._short_term_limit:
                self._short_term = self._short_term[-self._short_term_limit:]

            # Long-term (SQLite)
            self._persist_entry(entry)

        return entry

    # ── Store ───────────────────────────────────────────────

    def xǁAgentMemoryǁstore__mutmut_24(
        self,
        content: str,
        entry_type: str = "observation",
        importance: float = 0.5,
        metadata: dict[str, Any] | None = None,
    ) -> MemoryEntry:
        """Store a new memory entry in both short-term and long-term memory.

        Args:
            content: The memory content text.
            entry_type: Type of memory (observation, action, decision, knowledge).
            importance: Importance score 0.0-1.0.
            metadata: Optional metadata dict.

        Returns:
            The created MemoryEntry.
        """
        embedding = self._embedding_fn(content)
        entry = MemoryEntry(
            agent_id=self.agent_id,
            content=content,
            entry_type=entry_type,
            importance=max(0.0, min(None, importance)),
            embedding=embedding,
            metadata=metadata or {},
        )

        with self._lock:
            # Short-term
            self._short_term.append(entry)
            if len(self._short_term) > self._short_term_limit:
                self._short_term = self._short_term[-self._short_term_limit:]

            # Long-term (SQLite)
            self._persist_entry(entry)

        return entry

    # ── Store ───────────────────────────────────────────────

    def xǁAgentMemoryǁstore__mutmut_25(
        self,
        content: str,
        entry_type: str = "observation",
        importance: float = 0.5,
        metadata: dict[str, Any] | None = None,
    ) -> MemoryEntry:
        """Store a new memory entry in both short-term and long-term memory.

        Args:
            content: The memory content text.
            entry_type: Type of memory (observation, action, decision, knowledge).
            importance: Importance score 0.0-1.0.
            metadata: Optional metadata dict.

        Returns:
            The created MemoryEntry.
        """
        embedding = self._embedding_fn(content)
        entry = MemoryEntry(
            agent_id=self.agent_id,
            content=content,
            entry_type=entry_type,
            importance=max(0.0, min(1.0, None)),
            embedding=embedding,
            metadata=metadata or {},
        )

        with self._lock:
            # Short-term
            self._short_term.append(entry)
            if len(self._short_term) > self._short_term_limit:
                self._short_term = self._short_term[-self._short_term_limit:]

            # Long-term (SQLite)
            self._persist_entry(entry)

        return entry

    # ── Store ───────────────────────────────────────────────

    def xǁAgentMemoryǁstore__mutmut_26(
        self,
        content: str,
        entry_type: str = "observation",
        importance: float = 0.5,
        metadata: dict[str, Any] | None = None,
    ) -> MemoryEntry:
        """Store a new memory entry in both short-term and long-term memory.

        Args:
            content: The memory content text.
            entry_type: Type of memory (observation, action, decision, knowledge).
            importance: Importance score 0.0-1.0.
            metadata: Optional metadata dict.

        Returns:
            The created MemoryEntry.
        """
        embedding = self._embedding_fn(content)
        entry = MemoryEntry(
            agent_id=self.agent_id,
            content=content,
            entry_type=entry_type,
            importance=max(0.0, min(importance)),
            embedding=embedding,
            metadata=metadata or {},
        )

        with self._lock:
            # Short-term
            self._short_term.append(entry)
            if len(self._short_term) > self._short_term_limit:
                self._short_term = self._short_term[-self._short_term_limit:]

            # Long-term (SQLite)
            self._persist_entry(entry)

        return entry

    # ── Store ───────────────────────────────────────────────

    def xǁAgentMemoryǁstore__mutmut_27(
        self,
        content: str,
        entry_type: str = "observation",
        importance: float = 0.5,
        metadata: dict[str, Any] | None = None,
    ) -> MemoryEntry:
        """Store a new memory entry in both short-term and long-term memory.

        Args:
            content: The memory content text.
            entry_type: Type of memory (observation, action, decision, knowledge).
            importance: Importance score 0.0-1.0.
            metadata: Optional metadata dict.

        Returns:
            The created MemoryEntry.
        """
        embedding = self._embedding_fn(content)
        entry = MemoryEntry(
            agent_id=self.agent_id,
            content=content,
            entry_type=entry_type,
            importance=max(0.0, min(1.0, )),
            embedding=embedding,
            metadata=metadata or {},
        )

        with self._lock:
            # Short-term
            self._short_term.append(entry)
            if len(self._short_term) > self._short_term_limit:
                self._short_term = self._short_term[-self._short_term_limit:]

            # Long-term (SQLite)
            self._persist_entry(entry)

        return entry

    # ── Store ───────────────────────────────────────────────

    def xǁAgentMemoryǁstore__mutmut_28(
        self,
        content: str,
        entry_type: str = "observation",
        importance: float = 0.5,
        metadata: dict[str, Any] | None = None,
    ) -> MemoryEntry:
        """Store a new memory entry in both short-term and long-term memory.

        Args:
            content: The memory content text.
            entry_type: Type of memory (observation, action, decision, knowledge).
            importance: Importance score 0.0-1.0.
            metadata: Optional metadata dict.

        Returns:
            The created MemoryEntry.
        """
        embedding = self._embedding_fn(content)
        entry = MemoryEntry(
            agent_id=self.agent_id,
            content=content,
            entry_type=entry_type,
            importance=max(0.0, min(2.0, importance)),
            embedding=embedding,
            metadata=metadata or {},
        )

        with self._lock:
            # Short-term
            self._short_term.append(entry)
            if len(self._short_term) > self._short_term_limit:
                self._short_term = self._short_term[-self._short_term_limit:]

            # Long-term (SQLite)
            self._persist_entry(entry)

        return entry

    # ── Store ───────────────────────────────────────────────

    def xǁAgentMemoryǁstore__mutmut_29(
        self,
        content: str,
        entry_type: str = "observation",
        importance: float = 0.5,
        metadata: dict[str, Any] | None = None,
    ) -> MemoryEntry:
        """Store a new memory entry in both short-term and long-term memory.

        Args:
            content: The memory content text.
            entry_type: Type of memory (observation, action, decision, knowledge).
            importance: Importance score 0.0-1.0.
            metadata: Optional metadata dict.

        Returns:
            The created MemoryEntry.
        """
        embedding = self._embedding_fn(content)
        entry = MemoryEntry(
            agent_id=self.agent_id,
            content=content,
            entry_type=entry_type,
            importance=max(0.0, min(1.0, importance)),
            embedding=embedding,
            metadata=metadata and {},
        )

        with self._lock:
            # Short-term
            self._short_term.append(entry)
            if len(self._short_term) > self._short_term_limit:
                self._short_term = self._short_term[-self._short_term_limit:]

            # Long-term (SQLite)
            self._persist_entry(entry)

        return entry

    # ── Store ───────────────────────────────────────────────

    def xǁAgentMemoryǁstore__mutmut_30(
        self,
        content: str,
        entry_type: str = "observation",
        importance: float = 0.5,
        metadata: dict[str, Any] | None = None,
    ) -> MemoryEntry:
        """Store a new memory entry in both short-term and long-term memory.

        Args:
            content: The memory content text.
            entry_type: Type of memory (observation, action, decision, knowledge).
            importance: Importance score 0.0-1.0.
            metadata: Optional metadata dict.

        Returns:
            The created MemoryEntry.
        """
        embedding = self._embedding_fn(content)
        entry = MemoryEntry(
            agent_id=self.agent_id,
            content=content,
            entry_type=entry_type,
            importance=max(0.0, min(1.0, importance)),
            embedding=embedding,
            metadata=metadata or {},
        )

        with self._lock:
            # Short-term
            self._short_term.append(None)
            if len(self._short_term) > self._short_term_limit:
                self._short_term = self._short_term[-self._short_term_limit:]

            # Long-term (SQLite)
            self._persist_entry(entry)

        return entry

    # ── Store ───────────────────────────────────────────────

    def xǁAgentMemoryǁstore__mutmut_31(
        self,
        content: str,
        entry_type: str = "observation",
        importance: float = 0.5,
        metadata: dict[str, Any] | None = None,
    ) -> MemoryEntry:
        """Store a new memory entry in both short-term and long-term memory.

        Args:
            content: The memory content text.
            entry_type: Type of memory (observation, action, decision, knowledge).
            importance: Importance score 0.0-1.0.
            metadata: Optional metadata dict.

        Returns:
            The created MemoryEntry.
        """
        embedding = self._embedding_fn(content)
        entry = MemoryEntry(
            agent_id=self.agent_id,
            content=content,
            entry_type=entry_type,
            importance=max(0.0, min(1.0, importance)),
            embedding=embedding,
            metadata=metadata or {},
        )

        with self._lock:
            # Short-term
            self._short_term.append(entry)
            if len(self._short_term) >= self._short_term_limit:
                self._short_term = self._short_term[-self._short_term_limit:]

            # Long-term (SQLite)
            self._persist_entry(entry)

        return entry

    # ── Store ───────────────────────────────────────────────

    def xǁAgentMemoryǁstore__mutmut_32(
        self,
        content: str,
        entry_type: str = "observation",
        importance: float = 0.5,
        metadata: dict[str, Any] | None = None,
    ) -> MemoryEntry:
        """Store a new memory entry in both short-term and long-term memory.

        Args:
            content: The memory content text.
            entry_type: Type of memory (observation, action, decision, knowledge).
            importance: Importance score 0.0-1.0.
            metadata: Optional metadata dict.

        Returns:
            The created MemoryEntry.
        """
        embedding = self._embedding_fn(content)
        entry = MemoryEntry(
            agent_id=self.agent_id,
            content=content,
            entry_type=entry_type,
            importance=max(0.0, min(1.0, importance)),
            embedding=embedding,
            metadata=metadata or {},
        )

        with self._lock:
            # Short-term
            self._short_term.append(entry)
            if len(self._short_term) > self._short_term_limit:
                self._short_term = None

            # Long-term (SQLite)
            self._persist_entry(entry)

        return entry

    # ── Store ───────────────────────────────────────────────

    def xǁAgentMemoryǁstore__mutmut_33(
        self,
        content: str,
        entry_type: str = "observation",
        importance: float = 0.5,
        metadata: dict[str, Any] | None = None,
    ) -> MemoryEntry:
        """Store a new memory entry in both short-term and long-term memory.

        Args:
            content: The memory content text.
            entry_type: Type of memory (observation, action, decision, knowledge).
            importance: Importance score 0.0-1.0.
            metadata: Optional metadata dict.

        Returns:
            The created MemoryEntry.
        """
        embedding = self._embedding_fn(content)
        entry = MemoryEntry(
            agent_id=self.agent_id,
            content=content,
            entry_type=entry_type,
            importance=max(0.0, min(1.0, importance)),
            embedding=embedding,
            metadata=metadata or {},
        )

        with self._lock:
            # Short-term
            self._short_term.append(entry)
            if len(self._short_term) > self._short_term_limit:
                self._short_term = self._short_term[+self._short_term_limit:]

            # Long-term (SQLite)
            self._persist_entry(entry)

        return entry

    # ── Store ───────────────────────────────────────────────

    def xǁAgentMemoryǁstore__mutmut_34(
        self,
        content: str,
        entry_type: str = "observation",
        importance: float = 0.5,
        metadata: dict[str, Any] | None = None,
    ) -> MemoryEntry:
        """Store a new memory entry in both short-term and long-term memory.

        Args:
            content: The memory content text.
            entry_type: Type of memory (observation, action, decision, knowledge).
            importance: Importance score 0.0-1.0.
            metadata: Optional metadata dict.

        Returns:
            The created MemoryEntry.
        """
        embedding = self._embedding_fn(content)
        entry = MemoryEntry(
            agent_id=self.agent_id,
            content=content,
            entry_type=entry_type,
            importance=max(0.0, min(1.0, importance)),
            embedding=embedding,
            metadata=metadata or {},
        )

        with self._lock:
            # Short-term
            self._short_term.append(entry)
            if len(self._short_term) > self._short_term_limit:
                self._short_term = self._short_term[-self._short_term_limit:]

            # Long-term (SQLite)
            self._persist_entry(None)

        return entry

    @_mutmut_mutated(mutants_xǁAgentMemoryǁ_persist_entry__mutmut)
    def _persist_entry(self, entry: MemoryEntry) -> None:
        """Persist a memory entry to SQLite."""
        if self._conn is None:
            return
        self._conn.execute(
            """INSERT OR REPLACE INTO agent_memory
               (entry_id, agent_id, content, entry_type, importance, embedding, metadata,
                timestamp, access_count, last_accessed)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                entry.entry_id,
                entry.agent_id,
                entry.content,
                entry.entry_type,
                entry.importance,
                ",".join(str(v) for v in entry.embedding),
                str(entry.metadata),
                entry.timestamp,
                entry.access_count,
                entry.last_accessed,
            ),
        )
        self._conn.commit()

    def xǁAgentMemoryǁ_persist_entry__mutmut_orig(self, entry: MemoryEntry) -> None:
        """Persist a memory entry to SQLite."""
        if self._conn is None:
            return
        self._conn.execute(
            """INSERT OR REPLACE INTO agent_memory
               (entry_id, agent_id, content, entry_type, importance, embedding, metadata,
                timestamp, access_count, last_accessed)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                entry.entry_id,
                entry.agent_id,
                entry.content,
                entry.entry_type,
                entry.importance,
                ",".join(str(v) for v in entry.embedding),
                str(entry.metadata),
                entry.timestamp,
                entry.access_count,
                entry.last_accessed,
            ),
        )
        self._conn.commit()

    def xǁAgentMemoryǁ_persist_entry__mutmut_1(self, entry: MemoryEntry) -> None:
        """Persist a memory entry to SQLite."""
        if self._conn is not None:
            return
        self._conn.execute(
            """INSERT OR REPLACE INTO agent_memory
               (entry_id, agent_id, content, entry_type, importance, embedding, metadata,
                timestamp, access_count, last_accessed)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                entry.entry_id,
                entry.agent_id,
                entry.content,
                entry.entry_type,
                entry.importance,
                ",".join(str(v) for v in entry.embedding),
                str(entry.metadata),
                entry.timestamp,
                entry.access_count,
                entry.last_accessed,
            ),
        )
        self._conn.commit()

    def xǁAgentMemoryǁ_persist_entry__mutmut_2(self, entry: MemoryEntry) -> None:
        """Persist a memory entry to SQLite."""
        if self._conn is None:
            return
        self._conn.execute(
            None,
            (
                entry.entry_id,
                entry.agent_id,
                entry.content,
                entry.entry_type,
                entry.importance,
                ",".join(str(v) for v in entry.embedding),
                str(entry.metadata),
                entry.timestamp,
                entry.access_count,
                entry.last_accessed,
            ),
        )
        self._conn.commit()

    def xǁAgentMemoryǁ_persist_entry__mutmut_3(self, entry: MemoryEntry) -> None:
        """Persist a memory entry to SQLite."""
        if self._conn is None:
            return
        self._conn.execute(
            """INSERT OR REPLACE INTO agent_memory
               (entry_id, agent_id, content, entry_type, importance, embedding, metadata,
                timestamp, access_count, last_accessed)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            None,
        )
        self._conn.commit()

    def xǁAgentMemoryǁ_persist_entry__mutmut_4(self, entry: MemoryEntry) -> None:
        """Persist a memory entry to SQLite."""
        if self._conn is None:
            return
        self._conn.execute(
            (
                entry.entry_id,
                entry.agent_id,
                entry.content,
                entry.entry_type,
                entry.importance,
                ",".join(str(v) for v in entry.embedding),
                str(entry.metadata),
                entry.timestamp,
                entry.access_count,
                entry.last_accessed,
            ),
        )
        self._conn.commit()

    def xǁAgentMemoryǁ_persist_entry__mutmut_5(self, entry: MemoryEntry) -> None:
        """Persist a memory entry to SQLite."""
        if self._conn is None:
            return
        self._conn.execute(
            """INSERT OR REPLACE INTO agent_memory
               (entry_id, agent_id, content, entry_type, importance, embedding, metadata,
                timestamp, access_count, last_accessed)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            )
        self._conn.commit()

    def xǁAgentMemoryǁ_persist_entry__mutmut_6(self, entry: MemoryEntry) -> None:
        """Persist a memory entry to SQLite."""
        if self._conn is None:
            return
        self._conn.execute(
            """INSERT OR REPLACE INTO agent_memory
               (entry_id, agent_id, content, entry_type, importance, embedding, metadata,
                timestamp, access_count, last_accessed)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                entry.entry_id,
                entry.agent_id,
                entry.content,
                entry.entry_type,
                entry.importance,
                ",".join(None),
                str(entry.metadata),
                entry.timestamp,
                entry.access_count,
                entry.last_accessed,
            ),
        )
        self._conn.commit()

    def xǁAgentMemoryǁ_persist_entry__mutmut_7(self, entry: MemoryEntry) -> None:
        """Persist a memory entry to SQLite."""
        if self._conn is None:
            return
        self._conn.execute(
            """INSERT OR REPLACE INTO agent_memory
               (entry_id, agent_id, content, entry_type, importance, embedding, metadata,
                timestamp, access_count, last_accessed)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                entry.entry_id,
                entry.agent_id,
                entry.content,
                entry.entry_type,
                entry.importance,
                "XX,XX".join(str(v) for v in entry.embedding),
                str(entry.metadata),
                entry.timestamp,
                entry.access_count,
                entry.last_accessed,
            ),
        )
        self._conn.commit()

    def xǁAgentMemoryǁ_persist_entry__mutmut_8(self, entry: MemoryEntry) -> None:
        """Persist a memory entry to SQLite."""
        if self._conn is None:
            return
        self._conn.execute(
            """INSERT OR REPLACE INTO agent_memory
               (entry_id, agent_id, content, entry_type, importance, embedding, metadata,
                timestamp, access_count, last_accessed)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                entry.entry_id,
                entry.agent_id,
                entry.content,
                entry.entry_type,
                entry.importance,
                ",".join(str(None) for v in entry.embedding),
                str(entry.metadata),
                entry.timestamp,
                entry.access_count,
                entry.last_accessed,
            ),
        )
        self._conn.commit()

    def xǁAgentMemoryǁ_persist_entry__mutmut_9(self, entry: MemoryEntry) -> None:
        """Persist a memory entry to SQLite."""
        if self._conn is None:
            return
        self._conn.execute(
            """INSERT OR REPLACE INTO agent_memory
               (entry_id, agent_id, content, entry_type, importance, embedding, metadata,
                timestamp, access_count, last_accessed)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                entry.entry_id,
                entry.agent_id,
                entry.content,
                entry.entry_type,
                entry.importance,
                ",".join(str(v) for v in entry.embedding),
                str(None),
                entry.timestamp,
                entry.access_count,
                entry.last_accessed,
            ),
        )
        self._conn.commit()

    # ── Recall ──────────────────────────────────────────────

    @_mutmut_mutated(mutants_xǁAgentMemoryǁrecall__mutmut)
    def recall(
        self,
        query: str,
        limit: int = 10,
        entry_type: str | None = None,
        min_importance: float = 0.0,
        use_similarity: bool = True,
    ) -> list[MemoryEntry]:
        """Recall memories matching a query.

        Uses vector similarity search if use_similarity is True,
        otherwise falls back to keyword matching.

        Args:
            query: The search query.
            limit: Maximum number of results.
            entry_type: Filter by entry type.
            min_importance: Minimum importance threshold.
            use_similarity: Whether to use semantic similarity.

        Returns:
            List of matching MemoryEntry objects, ranked by relevance.
        """
        query_embedding = self._embedding_fn(query) if use_similarity else []

        with self._lock:
            # Search short-term first
            short_results = self._search_entries(
                self._short_term, query_embedding, entry_type, min_importance
            )

            # Search long-term
            long_results = self._search_db(query_embedding, entry_type, min_importance)

        # Merge, deduplicate, and rank
        seen_ids: set[str] = set()
        all_results: list[MemoryEntry] = []

        for entry in short_results + long_results:
            if entry.entry_id not in seen_ids:
                seen_ids.add(entry.entry_id)
                all_results.append(entry)

        # Sort by relevance (similarity score or importance)
        if use_similarity and query_embedding:
            all_results.sort(
                key=lambda e: _cosine_similarity(query_embedding, e.embedding),
                reverse=True,
            )
        else:
            all_results.sort(key=lambda e: e.importance, reverse=True)

        return all_results[:limit]

    # ── Recall ──────────────────────────────────────────────

    def xǁAgentMemoryǁrecall__mutmut_orig(
        self,
        query: str,
        limit: int = 10,
        entry_type: str | None = None,
        min_importance: float = 0.0,
        use_similarity: bool = True,
    ) -> list[MemoryEntry]:
        """Recall memories matching a query.

        Uses vector similarity search if use_similarity is True,
        otherwise falls back to keyword matching.

        Args:
            query: The search query.
            limit: Maximum number of results.
            entry_type: Filter by entry type.
            min_importance: Minimum importance threshold.
            use_similarity: Whether to use semantic similarity.

        Returns:
            List of matching MemoryEntry objects, ranked by relevance.
        """
        query_embedding = self._embedding_fn(query) if use_similarity else []

        with self._lock:
            # Search short-term first
            short_results = self._search_entries(
                self._short_term, query_embedding, entry_type, min_importance
            )

            # Search long-term
            long_results = self._search_db(query_embedding, entry_type, min_importance)

        # Merge, deduplicate, and rank
        seen_ids: set[str] = set()
        all_results: list[MemoryEntry] = []

        for entry in short_results + long_results:
            if entry.entry_id not in seen_ids:
                seen_ids.add(entry.entry_id)
                all_results.append(entry)

        # Sort by relevance (similarity score or importance)
        if use_similarity and query_embedding:
            all_results.sort(
                key=lambda e: _cosine_similarity(query_embedding, e.embedding),
                reverse=True,
            )
        else:
            all_results.sort(key=lambda e: e.importance, reverse=True)

        return all_results[:limit]

    # ── Recall ──────────────────────────────────────────────

    def xǁAgentMemoryǁrecall__mutmut_1(
        self,
        query: str,
        limit: int = 11,
        entry_type: str | None = None,
        min_importance: float = 0.0,
        use_similarity: bool = True,
    ) -> list[MemoryEntry]:
        """Recall memories matching a query.

        Uses vector similarity search if use_similarity is True,
        otherwise falls back to keyword matching.

        Args:
            query: The search query.
            limit: Maximum number of results.
            entry_type: Filter by entry type.
            min_importance: Minimum importance threshold.
            use_similarity: Whether to use semantic similarity.

        Returns:
            List of matching MemoryEntry objects, ranked by relevance.
        """
        query_embedding = self._embedding_fn(query) if use_similarity else []

        with self._lock:
            # Search short-term first
            short_results = self._search_entries(
                self._short_term, query_embedding, entry_type, min_importance
            )

            # Search long-term
            long_results = self._search_db(query_embedding, entry_type, min_importance)

        # Merge, deduplicate, and rank
        seen_ids: set[str] = set()
        all_results: list[MemoryEntry] = []

        for entry in short_results + long_results:
            if entry.entry_id not in seen_ids:
                seen_ids.add(entry.entry_id)
                all_results.append(entry)

        # Sort by relevance (similarity score or importance)
        if use_similarity and query_embedding:
            all_results.sort(
                key=lambda e: _cosine_similarity(query_embedding, e.embedding),
                reverse=True,
            )
        else:
            all_results.sort(key=lambda e: e.importance, reverse=True)

        return all_results[:limit]

    # ── Recall ──────────────────────────────────────────────

    def xǁAgentMemoryǁrecall__mutmut_2(
        self,
        query: str,
        limit: int = 10,
        entry_type: str | None = None,
        min_importance: float = 1.0,
        use_similarity: bool = True,
    ) -> list[MemoryEntry]:
        """Recall memories matching a query.

        Uses vector similarity search if use_similarity is True,
        otherwise falls back to keyword matching.

        Args:
            query: The search query.
            limit: Maximum number of results.
            entry_type: Filter by entry type.
            min_importance: Minimum importance threshold.
            use_similarity: Whether to use semantic similarity.

        Returns:
            List of matching MemoryEntry objects, ranked by relevance.
        """
        query_embedding = self._embedding_fn(query) if use_similarity else []

        with self._lock:
            # Search short-term first
            short_results = self._search_entries(
                self._short_term, query_embedding, entry_type, min_importance
            )

            # Search long-term
            long_results = self._search_db(query_embedding, entry_type, min_importance)

        # Merge, deduplicate, and rank
        seen_ids: set[str] = set()
        all_results: list[MemoryEntry] = []

        for entry in short_results + long_results:
            if entry.entry_id not in seen_ids:
                seen_ids.add(entry.entry_id)
                all_results.append(entry)

        # Sort by relevance (similarity score or importance)
        if use_similarity and query_embedding:
            all_results.sort(
                key=lambda e: _cosine_similarity(query_embedding, e.embedding),
                reverse=True,
            )
        else:
            all_results.sort(key=lambda e: e.importance, reverse=True)

        return all_results[:limit]

    # ── Recall ──────────────────────────────────────────────

    def xǁAgentMemoryǁrecall__mutmut_3(
        self,
        query: str,
        limit: int = 10,
        entry_type: str | None = None,
        min_importance: float = 0.0,
        use_similarity: bool = False,
    ) -> list[MemoryEntry]:
        """Recall memories matching a query.

        Uses vector similarity search if use_similarity is True,
        otherwise falls back to keyword matching.

        Args:
            query: The search query.
            limit: Maximum number of results.
            entry_type: Filter by entry type.
            min_importance: Minimum importance threshold.
            use_similarity: Whether to use semantic similarity.

        Returns:
            List of matching MemoryEntry objects, ranked by relevance.
        """
        query_embedding = self._embedding_fn(query) if use_similarity else []

        with self._lock:
            # Search short-term first
            short_results = self._search_entries(
                self._short_term, query_embedding, entry_type, min_importance
            )

            # Search long-term
            long_results = self._search_db(query_embedding, entry_type, min_importance)

        # Merge, deduplicate, and rank
        seen_ids: set[str] = set()
        all_results: list[MemoryEntry] = []

        for entry in short_results + long_results:
            if entry.entry_id not in seen_ids:
                seen_ids.add(entry.entry_id)
                all_results.append(entry)

        # Sort by relevance (similarity score or importance)
        if use_similarity and query_embedding:
            all_results.sort(
                key=lambda e: _cosine_similarity(query_embedding, e.embedding),
                reverse=True,
            )
        else:
            all_results.sort(key=lambda e: e.importance, reverse=True)

        return all_results[:limit]

    # ── Recall ──────────────────────────────────────────────

    def xǁAgentMemoryǁrecall__mutmut_4(
        self,
        query: str,
        limit: int = 10,
        entry_type: str | None = None,
        min_importance: float = 0.0,
        use_similarity: bool = True,
    ) -> list[MemoryEntry]:
        """Recall memories matching a query.

        Uses vector similarity search if use_similarity is True,
        otherwise falls back to keyword matching.

        Args:
            query: The search query.
            limit: Maximum number of results.
            entry_type: Filter by entry type.
            min_importance: Minimum importance threshold.
            use_similarity: Whether to use semantic similarity.

        Returns:
            List of matching MemoryEntry objects, ranked by relevance.
        """
        query_embedding = None

        with self._lock:
            # Search short-term first
            short_results = self._search_entries(
                self._short_term, query_embedding, entry_type, min_importance
            )

            # Search long-term
            long_results = self._search_db(query_embedding, entry_type, min_importance)

        # Merge, deduplicate, and rank
        seen_ids: set[str] = set()
        all_results: list[MemoryEntry] = []

        for entry in short_results + long_results:
            if entry.entry_id not in seen_ids:
                seen_ids.add(entry.entry_id)
                all_results.append(entry)

        # Sort by relevance (similarity score or importance)
        if use_similarity and query_embedding:
            all_results.sort(
                key=lambda e: _cosine_similarity(query_embedding, e.embedding),
                reverse=True,
            )
        else:
            all_results.sort(key=lambda e: e.importance, reverse=True)

        return all_results[:limit]

    # ── Recall ──────────────────────────────────────────────

    def xǁAgentMemoryǁrecall__mutmut_5(
        self,
        query: str,
        limit: int = 10,
        entry_type: str | None = None,
        min_importance: float = 0.0,
        use_similarity: bool = True,
    ) -> list[MemoryEntry]:
        """Recall memories matching a query.

        Uses vector similarity search if use_similarity is True,
        otherwise falls back to keyword matching.

        Args:
            query: The search query.
            limit: Maximum number of results.
            entry_type: Filter by entry type.
            min_importance: Minimum importance threshold.
            use_similarity: Whether to use semantic similarity.

        Returns:
            List of matching MemoryEntry objects, ranked by relevance.
        """
        query_embedding = self._embedding_fn(None) if use_similarity else []

        with self._lock:
            # Search short-term first
            short_results = self._search_entries(
                self._short_term, query_embedding, entry_type, min_importance
            )

            # Search long-term
            long_results = self._search_db(query_embedding, entry_type, min_importance)

        # Merge, deduplicate, and rank
        seen_ids: set[str] = set()
        all_results: list[MemoryEntry] = []

        for entry in short_results + long_results:
            if entry.entry_id not in seen_ids:
                seen_ids.add(entry.entry_id)
                all_results.append(entry)

        # Sort by relevance (similarity score or importance)
        if use_similarity and query_embedding:
            all_results.sort(
                key=lambda e: _cosine_similarity(query_embedding, e.embedding),
                reverse=True,
            )
        else:
            all_results.sort(key=lambda e: e.importance, reverse=True)

        return all_results[:limit]

    # ── Recall ──────────────────────────────────────────────

    def xǁAgentMemoryǁrecall__mutmut_6(
        self,
        query: str,
        limit: int = 10,
        entry_type: str | None = None,
        min_importance: float = 0.0,
        use_similarity: bool = True,
    ) -> list[MemoryEntry]:
        """Recall memories matching a query.

        Uses vector similarity search if use_similarity is True,
        otherwise falls back to keyword matching.

        Args:
            query: The search query.
            limit: Maximum number of results.
            entry_type: Filter by entry type.
            min_importance: Minimum importance threshold.
            use_similarity: Whether to use semantic similarity.

        Returns:
            List of matching MemoryEntry objects, ranked by relevance.
        """
        query_embedding = self._embedding_fn(query) if use_similarity else []

        with self._lock:
            # Search short-term first
            short_results = None

            # Search long-term
            long_results = self._search_db(query_embedding, entry_type, min_importance)

        # Merge, deduplicate, and rank
        seen_ids: set[str] = set()
        all_results: list[MemoryEntry] = []

        for entry in short_results + long_results:
            if entry.entry_id not in seen_ids:
                seen_ids.add(entry.entry_id)
                all_results.append(entry)

        # Sort by relevance (similarity score or importance)
        if use_similarity and query_embedding:
            all_results.sort(
                key=lambda e: _cosine_similarity(query_embedding, e.embedding),
                reverse=True,
            )
        else:
            all_results.sort(key=lambda e: e.importance, reverse=True)

        return all_results[:limit]

    # ── Recall ──────────────────────────────────────────────

    def xǁAgentMemoryǁrecall__mutmut_7(
        self,
        query: str,
        limit: int = 10,
        entry_type: str | None = None,
        min_importance: float = 0.0,
        use_similarity: bool = True,
    ) -> list[MemoryEntry]:
        """Recall memories matching a query.

        Uses vector similarity search if use_similarity is True,
        otherwise falls back to keyword matching.

        Args:
            query: The search query.
            limit: Maximum number of results.
            entry_type: Filter by entry type.
            min_importance: Minimum importance threshold.
            use_similarity: Whether to use semantic similarity.

        Returns:
            List of matching MemoryEntry objects, ranked by relevance.
        """
        query_embedding = self._embedding_fn(query) if use_similarity else []

        with self._lock:
            # Search short-term first
            short_results = self._search_entries(
                None, query_embedding, entry_type, min_importance
            )

            # Search long-term
            long_results = self._search_db(query_embedding, entry_type, min_importance)

        # Merge, deduplicate, and rank
        seen_ids: set[str] = set()
        all_results: list[MemoryEntry] = []

        for entry in short_results + long_results:
            if entry.entry_id not in seen_ids:
                seen_ids.add(entry.entry_id)
                all_results.append(entry)

        # Sort by relevance (similarity score or importance)
        if use_similarity and query_embedding:
            all_results.sort(
                key=lambda e: _cosine_similarity(query_embedding, e.embedding),
                reverse=True,
            )
        else:
            all_results.sort(key=lambda e: e.importance, reverse=True)

        return all_results[:limit]

    # ── Recall ──────────────────────────────────────────────

    def xǁAgentMemoryǁrecall__mutmut_8(
        self,
        query: str,
        limit: int = 10,
        entry_type: str | None = None,
        min_importance: float = 0.0,
        use_similarity: bool = True,
    ) -> list[MemoryEntry]:
        """Recall memories matching a query.

        Uses vector similarity search if use_similarity is True,
        otherwise falls back to keyword matching.

        Args:
            query: The search query.
            limit: Maximum number of results.
            entry_type: Filter by entry type.
            min_importance: Minimum importance threshold.
            use_similarity: Whether to use semantic similarity.

        Returns:
            List of matching MemoryEntry objects, ranked by relevance.
        """
        query_embedding = self._embedding_fn(query) if use_similarity else []

        with self._lock:
            # Search short-term first
            short_results = self._search_entries(
                self._short_term, None, entry_type, min_importance
            )

            # Search long-term
            long_results = self._search_db(query_embedding, entry_type, min_importance)

        # Merge, deduplicate, and rank
        seen_ids: set[str] = set()
        all_results: list[MemoryEntry] = []

        for entry in short_results + long_results:
            if entry.entry_id not in seen_ids:
                seen_ids.add(entry.entry_id)
                all_results.append(entry)

        # Sort by relevance (similarity score or importance)
        if use_similarity and query_embedding:
            all_results.sort(
                key=lambda e: _cosine_similarity(query_embedding, e.embedding),
                reverse=True,
            )
        else:
            all_results.sort(key=lambda e: e.importance, reverse=True)

        return all_results[:limit]

    # ── Recall ──────────────────────────────────────────────

    def xǁAgentMemoryǁrecall__mutmut_9(
        self,
        query: str,
        limit: int = 10,
        entry_type: str | None = None,
        min_importance: float = 0.0,
        use_similarity: bool = True,
    ) -> list[MemoryEntry]:
        """Recall memories matching a query.

        Uses vector similarity search if use_similarity is True,
        otherwise falls back to keyword matching.

        Args:
            query: The search query.
            limit: Maximum number of results.
            entry_type: Filter by entry type.
            min_importance: Minimum importance threshold.
            use_similarity: Whether to use semantic similarity.

        Returns:
            List of matching MemoryEntry objects, ranked by relevance.
        """
        query_embedding = self._embedding_fn(query) if use_similarity else []

        with self._lock:
            # Search short-term first
            short_results = self._search_entries(
                self._short_term, query_embedding, None, min_importance
            )

            # Search long-term
            long_results = self._search_db(query_embedding, entry_type, min_importance)

        # Merge, deduplicate, and rank
        seen_ids: set[str] = set()
        all_results: list[MemoryEntry] = []

        for entry in short_results + long_results:
            if entry.entry_id not in seen_ids:
                seen_ids.add(entry.entry_id)
                all_results.append(entry)

        # Sort by relevance (similarity score or importance)
        if use_similarity and query_embedding:
            all_results.sort(
                key=lambda e: _cosine_similarity(query_embedding, e.embedding),
                reverse=True,
            )
        else:
            all_results.sort(key=lambda e: e.importance, reverse=True)

        return all_results[:limit]

    # ── Recall ──────────────────────────────────────────────

    def xǁAgentMemoryǁrecall__mutmut_10(
        self,
        query: str,
        limit: int = 10,
        entry_type: str | None = None,
        min_importance: float = 0.0,
        use_similarity: bool = True,
    ) -> list[MemoryEntry]:
        """Recall memories matching a query.

        Uses vector similarity search if use_similarity is True,
        otherwise falls back to keyword matching.

        Args:
            query: The search query.
            limit: Maximum number of results.
            entry_type: Filter by entry type.
            min_importance: Minimum importance threshold.
            use_similarity: Whether to use semantic similarity.

        Returns:
            List of matching MemoryEntry objects, ranked by relevance.
        """
        query_embedding = self._embedding_fn(query) if use_similarity else []

        with self._lock:
            # Search short-term first
            short_results = self._search_entries(
                self._short_term, query_embedding, entry_type, None
            )

            # Search long-term
            long_results = self._search_db(query_embedding, entry_type, min_importance)

        # Merge, deduplicate, and rank
        seen_ids: set[str] = set()
        all_results: list[MemoryEntry] = []

        for entry in short_results + long_results:
            if entry.entry_id not in seen_ids:
                seen_ids.add(entry.entry_id)
                all_results.append(entry)

        # Sort by relevance (similarity score or importance)
        if use_similarity and query_embedding:
            all_results.sort(
                key=lambda e: _cosine_similarity(query_embedding, e.embedding),
                reverse=True,
            )
        else:
            all_results.sort(key=lambda e: e.importance, reverse=True)

        return all_results[:limit]

    # ── Recall ──────────────────────────────────────────────

    def xǁAgentMemoryǁrecall__mutmut_11(
        self,
        query: str,
        limit: int = 10,
        entry_type: str | None = None,
        min_importance: float = 0.0,
        use_similarity: bool = True,
    ) -> list[MemoryEntry]:
        """Recall memories matching a query.

        Uses vector similarity search if use_similarity is True,
        otherwise falls back to keyword matching.

        Args:
            query: The search query.
            limit: Maximum number of results.
            entry_type: Filter by entry type.
            min_importance: Minimum importance threshold.
            use_similarity: Whether to use semantic similarity.

        Returns:
            List of matching MemoryEntry objects, ranked by relevance.
        """
        query_embedding = self._embedding_fn(query) if use_similarity else []

        with self._lock:
            # Search short-term first
            short_results = self._search_entries(
                query_embedding, entry_type, min_importance
            )

            # Search long-term
            long_results = self._search_db(query_embedding, entry_type, min_importance)

        # Merge, deduplicate, and rank
        seen_ids: set[str] = set()
        all_results: list[MemoryEntry] = []

        for entry in short_results + long_results:
            if entry.entry_id not in seen_ids:
                seen_ids.add(entry.entry_id)
                all_results.append(entry)

        # Sort by relevance (similarity score or importance)
        if use_similarity and query_embedding:
            all_results.sort(
                key=lambda e: _cosine_similarity(query_embedding, e.embedding),
                reverse=True,
            )
        else:
            all_results.sort(key=lambda e: e.importance, reverse=True)

        return all_results[:limit]

    # ── Recall ──────────────────────────────────────────────

    def xǁAgentMemoryǁrecall__mutmut_12(
        self,
        query: str,
        limit: int = 10,
        entry_type: str | None = None,
        min_importance: float = 0.0,
        use_similarity: bool = True,
    ) -> list[MemoryEntry]:
        """Recall memories matching a query.

        Uses vector similarity search if use_similarity is True,
        otherwise falls back to keyword matching.

        Args:
            query: The search query.
            limit: Maximum number of results.
            entry_type: Filter by entry type.
            min_importance: Minimum importance threshold.
            use_similarity: Whether to use semantic similarity.

        Returns:
            List of matching MemoryEntry objects, ranked by relevance.
        """
        query_embedding = self._embedding_fn(query) if use_similarity else []

        with self._lock:
            # Search short-term first
            short_results = self._search_entries(
                self._short_term, entry_type, min_importance
            )

            # Search long-term
            long_results = self._search_db(query_embedding, entry_type, min_importance)

        # Merge, deduplicate, and rank
        seen_ids: set[str] = set()
        all_results: list[MemoryEntry] = []

        for entry in short_results + long_results:
            if entry.entry_id not in seen_ids:
                seen_ids.add(entry.entry_id)
                all_results.append(entry)

        # Sort by relevance (similarity score or importance)
        if use_similarity and query_embedding:
            all_results.sort(
                key=lambda e: _cosine_similarity(query_embedding, e.embedding),
                reverse=True,
            )
        else:
            all_results.sort(key=lambda e: e.importance, reverse=True)

        return all_results[:limit]

    # ── Recall ──────────────────────────────────────────────

    def xǁAgentMemoryǁrecall__mutmut_13(
        self,
        query: str,
        limit: int = 10,
        entry_type: str | None = None,
        min_importance: float = 0.0,
        use_similarity: bool = True,
    ) -> list[MemoryEntry]:
        """Recall memories matching a query.

        Uses vector similarity search if use_similarity is True,
        otherwise falls back to keyword matching.

        Args:
            query: The search query.
            limit: Maximum number of results.
            entry_type: Filter by entry type.
            min_importance: Minimum importance threshold.
            use_similarity: Whether to use semantic similarity.

        Returns:
            List of matching MemoryEntry objects, ranked by relevance.
        """
        query_embedding = self._embedding_fn(query) if use_similarity else []

        with self._lock:
            # Search short-term first
            short_results = self._search_entries(
                self._short_term, query_embedding, min_importance
            )

            # Search long-term
            long_results = self._search_db(query_embedding, entry_type, min_importance)

        # Merge, deduplicate, and rank
        seen_ids: set[str] = set()
        all_results: list[MemoryEntry] = []

        for entry in short_results + long_results:
            if entry.entry_id not in seen_ids:
                seen_ids.add(entry.entry_id)
                all_results.append(entry)

        # Sort by relevance (similarity score or importance)
        if use_similarity and query_embedding:
            all_results.sort(
                key=lambda e: _cosine_similarity(query_embedding, e.embedding),
                reverse=True,
            )
        else:
            all_results.sort(key=lambda e: e.importance, reverse=True)

        return all_results[:limit]

    # ── Recall ──────────────────────────────────────────────

    def xǁAgentMemoryǁrecall__mutmut_14(
        self,
        query: str,
        limit: int = 10,
        entry_type: str | None = None,
        min_importance: float = 0.0,
        use_similarity: bool = True,
    ) -> list[MemoryEntry]:
        """Recall memories matching a query.

        Uses vector similarity search if use_similarity is True,
        otherwise falls back to keyword matching.

        Args:
            query: The search query.
            limit: Maximum number of results.
            entry_type: Filter by entry type.
            min_importance: Minimum importance threshold.
            use_similarity: Whether to use semantic similarity.

        Returns:
            List of matching MemoryEntry objects, ranked by relevance.
        """
        query_embedding = self._embedding_fn(query) if use_similarity else []

        with self._lock:
            # Search short-term first
            short_results = self._search_entries(
                self._short_term, query_embedding, entry_type, )

            # Search long-term
            long_results = self._search_db(query_embedding, entry_type, min_importance)

        # Merge, deduplicate, and rank
        seen_ids: set[str] = set()
        all_results: list[MemoryEntry] = []

        for entry in short_results + long_results:
            if entry.entry_id not in seen_ids:
                seen_ids.add(entry.entry_id)
                all_results.append(entry)

        # Sort by relevance (similarity score or importance)
        if use_similarity and query_embedding:
            all_results.sort(
                key=lambda e: _cosine_similarity(query_embedding, e.embedding),
                reverse=True,
            )
        else:
            all_results.sort(key=lambda e: e.importance, reverse=True)

        return all_results[:limit]

    # ── Recall ──────────────────────────────────────────────

    def xǁAgentMemoryǁrecall__mutmut_15(
        self,
        query: str,
        limit: int = 10,
        entry_type: str | None = None,
        min_importance: float = 0.0,
        use_similarity: bool = True,
    ) -> list[MemoryEntry]:
        """Recall memories matching a query.

        Uses vector similarity search if use_similarity is True,
        otherwise falls back to keyword matching.

        Args:
            query: The search query.
            limit: Maximum number of results.
            entry_type: Filter by entry type.
            min_importance: Minimum importance threshold.
            use_similarity: Whether to use semantic similarity.

        Returns:
            List of matching MemoryEntry objects, ranked by relevance.
        """
        query_embedding = self._embedding_fn(query) if use_similarity else []

        with self._lock:
            # Search short-term first
            short_results = self._search_entries(
                self._short_term, query_embedding, entry_type, min_importance
            )

            # Search long-term
            long_results = None

        # Merge, deduplicate, and rank
        seen_ids: set[str] = set()
        all_results: list[MemoryEntry] = []

        for entry in short_results + long_results:
            if entry.entry_id not in seen_ids:
                seen_ids.add(entry.entry_id)
                all_results.append(entry)

        # Sort by relevance (similarity score or importance)
        if use_similarity and query_embedding:
            all_results.sort(
                key=lambda e: _cosine_similarity(query_embedding, e.embedding),
                reverse=True,
            )
        else:
            all_results.sort(key=lambda e: e.importance, reverse=True)

        return all_results[:limit]

    # ── Recall ──────────────────────────────────────────────

    def xǁAgentMemoryǁrecall__mutmut_16(
        self,
        query: str,
        limit: int = 10,
        entry_type: str | None = None,
        min_importance: float = 0.0,
        use_similarity: bool = True,
    ) -> list[MemoryEntry]:
        """Recall memories matching a query.

        Uses vector similarity search if use_similarity is True,
        otherwise falls back to keyword matching.

        Args:
            query: The search query.
            limit: Maximum number of results.
            entry_type: Filter by entry type.
            min_importance: Minimum importance threshold.
            use_similarity: Whether to use semantic similarity.

        Returns:
            List of matching MemoryEntry objects, ranked by relevance.
        """
        query_embedding = self._embedding_fn(query) if use_similarity else []

        with self._lock:
            # Search short-term first
            short_results = self._search_entries(
                self._short_term, query_embedding, entry_type, min_importance
            )

            # Search long-term
            long_results = self._search_db(None, entry_type, min_importance)

        # Merge, deduplicate, and rank
        seen_ids: set[str] = set()
        all_results: list[MemoryEntry] = []

        for entry in short_results + long_results:
            if entry.entry_id not in seen_ids:
                seen_ids.add(entry.entry_id)
                all_results.append(entry)

        # Sort by relevance (similarity score or importance)
        if use_similarity and query_embedding:
            all_results.sort(
                key=lambda e: _cosine_similarity(query_embedding, e.embedding),
                reverse=True,
            )
        else:
            all_results.sort(key=lambda e: e.importance, reverse=True)

        return all_results[:limit]

    # ── Recall ──────────────────────────────────────────────

    def xǁAgentMemoryǁrecall__mutmut_17(
        self,
        query: str,
        limit: int = 10,
        entry_type: str | None = None,
        min_importance: float = 0.0,
        use_similarity: bool = True,
    ) -> list[MemoryEntry]:
        """Recall memories matching a query.

        Uses vector similarity search if use_similarity is True,
        otherwise falls back to keyword matching.

        Args:
            query: The search query.
            limit: Maximum number of results.
            entry_type: Filter by entry type.
            min_importance: Minimum importance threshold.
            use_similarity: Whether to use semantic similarity.

        Returns:
            List of matching MemoryEntry objects, ranked by relevance.
        """
        query_embedding = self._embedding_fn(query) if use_similarity else []

        with self._lock:
            # Search short-term first
            short_results = self._search_entries(
                self._short_term, query_embedding, entry_type, min_importance
            )

            # Search long-term
            long_results = self._search_db(query_embedding, None, min_importance)

        # Merge, deduplicate, and rank
        seen_ids: set[str] = set()
        all_results: list[MemoryEntry] = []

        for entry in short_results + long_results:
            if entry.entry_id not in seen_ids:
                seen_ids.add(entry.entry_id)
                all_results.append(entry)

        # Sort by relevance (similarity score or importance)
        if use_similarity and query_embedding:
            all_results.sort(
                key=lambda e: _cosine_similarity(query_embedding, e.embedding),
                reverse=True,
            )
        else:
            all_results.sort(key=lambda e: e.importance, reverse=True)

        return all_results[:limit]

    # ── Recall ──────────────────────────────────────────────

    def xǁAgentMemoryǁrecall__mutmut_18(
        self,
        query: str,
        limit: int = 10,
        entry_type: str | None = None,
        min_importance: float = 0.0,
        use_similarity: bool = True,
    ) -> list[MemoryEntry]:
        """Recall memories matching a query.

        Uses vector similarity search if use_similarity is True,
        otherwise falls back to keyword matching.

        Args:
            query: The search query.
            limit: Maximum number of results.
            entry_type: Filter by entry type.
            min_importance: Minimum importance threshold.
            use_similarity: Whether to use semantic similarity.

        Returns:
            List of matching MemoryEntry objects, ranked by relevance.
        """
        query_embedding = self._embedding_fn(query) if use_similarity else []

        with self._lock:
            # Search short-term first
            short_results = self._search_entries(
                self._short_term, query_embedding, entry_type, min_importance
            )

            # Search long-term
            long_results = self._search_db(query_embedding, entry_type, None)

        # Merge, deduplicate, and rank
        seen_ids: set[str] = set()
        all_results: list[MemoryEntry] = []

        for entry in short_results + long_results:
            if entry.entry_id not in seen_ids:
                seen_ids.add(entry.entry_id)
                all_results.append(entry)

        # Sort by relevance (similarity score or importance)
        if use_similarity and query_embedding:
            all_results.sort(
                key=lambda e: _cosine_similarity(query_embedding, e.embedding),
                reverse=True,
            )
        else:
            all_results.sort(key=lambda e: e.importance, reverse=True)

        return all_results[:limit]

    # ── Recall ──────────────────────────────────────────────

    def xǁAgentMemoryǁrecall__mutmut_19(
        self,
        query: str,
        limit: int = 10,
        entry_type: str | None = None,
        min_importance: float = 0.0,
        use_similarity: bool = True,
    ) -> list[MemoryEntry]:
        """Recall memories matching a query.

        Uses vector similarity search if use_similarity is True,
        otherwise falls back to keyword matching.

        Args:
            query: The search query.
            limit: Maximum number of results.
            entry_type: Filter by entry type.
            min_importance: Minimum importance threshold.
            use_similarity: Whether to use semantic similarity.

        Returns:
            List of matching MemoryEntry objects, ranked by relevance.
        """
        query_embedding = self._embedding_fn(query) if use_similarity else []

        with self._lock:
            # Search short-term first
            short_results = self._search_entries(
                self._short_term, query_embedding, entry_type, min_importance
            )

            # Search long-term
            long_results = self._search_db(entry_type, min_importance)

        # Merge, deduplicate, and rank
        seen_ids: set[str] = set()
        all_results: list[MemoryEntry] = []

        for entry in short_results + long_results:
            if entry.entry_id not in seen_ids:
                seen_ids.add(entry.entry_id)
                all_results.append(entry)

        # Sort by relevance (similarity score or importance)
        if use_similarity and query_embedding:
            all_results.sort(
                key=lambda e: _cosine_similarity(query_embedding, e.embedding),
                reverse=True,
            )
        else:
            all_results.sort(key=lambda e: e.importance, reverse=True)

        return all_results[:limit]

    # ── Recall ──────────────────────────────────────────────

    def xǁAgentMemoryǁrecall__mutmut_20(
        self,
        query: str,
        limit: int = 10,
        entry_type: str | None = None,
        min_importance: float = 0.0,
        use_similarity: bool = True,
    ) -> list[MemoryEntry]:
        """Recall memories matching a query.

        Uses vector similarity search if use_similarity is True,
        otherwise falls back to keyword matching.

        Args:
            query: The search query.
            limit: Maximum number of results.
            entry_type: Filter by entry type.
            min_importance: Minimum importance threshold.
            use_similarity: Whether to use semantic similarity.

        Returns:
            List of matching MemoryEntry objects, ranked by relevance.
        """
        query_embedding = self._embedding_fn(query) if use_similarity else []

        with self._lock:
            # Search short-term first
            short_results = self._search_entries(
                self._short_term, query_embedding, entry_type, min_importance
            )

            # Search long-term
            long_results = self._search_db(query_embedding, min_importance)

        # Merge, deduplicate, and rank
        seen_ids: set[str] = set()
        all_results: list[MemoryEntry] = []

        for entry in short_results + long_results:
            if entry.entry_id not in seen_ids:
                seen_ids.add(entry.entry_id)
                all_results.append(entry)

        # Sort by relevance (similarity score or importance)
        if use_similarity and query_embedding:
            all_results.sort(
                key=lambda e: _cosine_similarity(query_embedding, e.embedding),
                reverse=True,
            )
        else:
            all_results.sort(key=lambda e: e.importance, reverse=True)

        return all_results[:limit]

    # ── Recall ──────────────────────────────────────────────

    def xǁAgentMemoryǁrecall__mutmut_21(
        self,
        query: str,
        limit: int = 10,
        entry_type: str | None = None,
        min_importance: float = 0.0,
        use_similarity: bool = True,
    ) -> list[MemoryEntry]:
        """Recall memories matching a query.

        Uses vector similarity search if use_similarity is True,
        otherwise falls back to keyword matching.

        Args:
            query: The search query.
            limit: Maximum number of results.
            entry_type: Filter by entry type.
            min_importance: Minimum importance threshold.
            use_similarity: Whether to use semantic similarity.

        Returns:
            List of matching MemoryEntry objects, ranked by relevance.
        """
        query_embedding = self._embedding_fn(query) if use_similarity else []

        with self._lock:
            # Search short-term first
            short_results = self._search_entries(
                self._short_term, query_embedding, entry_type, min_importance
            )

            # Search long-term
            long_results = self._search_db(query_embedding, entry_type, )

        # Merge, deduplicate, and rank
        seen_ids: set[str] = set()
        all_results: list[MemoryEntry] = []

        for entry in short_results + long_results:
            if entry.entry_id not in seen_ids:
                seen_ids.add(entry.entry_id)
                all_results.append(entry)

        # Sort by relevance (similarity score or importance)
        if use_similarity and query_embedding:
            all_results.sort(
                key=lambda e: _cosine_similarity(query_embedding, e.embedding),
                reverse=True,
            )
        else:
            all_results.sort(key=lambda e: e.importance, reverse=True)

        return all_results[:limit]

    # ── Recall ──────────────────────────────────────────────

    def xǁAgentMemoryǁrecall__mutmut_22(
        self,
        query: str,
        limit: int = 10,
        entry_type: str | None = None,
        min_importance: float = 0.0,
        use_similarity: bool = True,
    ) -> list[MemoryEntry]:
        """Recall memories matching a query.

        Uses vector similarity search if use_similarity is True,
        otherwise falls back to keyword matching.

        Args:
            query: The search query.
            limit: Maximum number of results.
            entry_type: Filter by entry type.
            min_importance: Minimum importance threshold.
            use_similarity: Whether to use semantic similarity.

        Returns:
            List of matching MemoryEntry objects, ranked by relevance.
        """
        query_embedding = self._embedding_fn(query) if use_similarity else []

        with self._lock:
            # Search short-term first
            short_results = self._search_entries(
                self._short_term, query_embedding, entry_type, min_importance
            )

            # Search long-term
            long_results = self._search_db(query_embedding, entry_type, min_importance)

        # Merge, deduplicate, and rank
        seen_ids: set[str] = None
        all_results: list[MemoryEntry] = []

        for entry in short_results + long_results:
            if entry.entry_id not in seen_ids:
                seen_ids.add(entry.entry_id)
                all_results.append(entry)

        # Sort by relevance (similarity score or importance)
        if use_similarity and query_embedding:
            all_results.sort(
                key=lambda e: _cosine_similarity(query_embedding, e.embedding),
                reverse=True,
            )
        else:
            all_results.sort(key=lambda e: e.importance, reverse=True)

        return all_results[:limit]

    # ── Recall ──────────────────────────────────────────────

    def xǁAgentMemoryǁrecall__mutmut_23(
        self,
        query: str,
        limit: int = 10,
        entry_type: str | None = None,
        min_importance: float = 0.0,
        use_similarity: bool = True,
    ) -> list[MemoryEntry]:
        """Recall memories matching a query.

        Uses vector similarity search if use_similarity is True,
        otherwise falls back to keyword matching.

        Args:
            query: The search query.
            limit: Maximum number of results.
            entry_type: Filter by entry type.
            min_importance: Minimum importance threshold.
            use_similarity: Whether to use semantic similarity.

        Returns:
            List of matching MemoryEntry objects, ranked by relevance.
        """
        query_embedding = self._embedding_fn(query) if use_similarity else []

        with self._lock:
            # Search short-term first
            short_results = self._search_entries(
                self._short_term, query_embedding, entry_type, min_importance
            )

            # Search long-term
            long_results = self._search_db(query_embedding, entry_type, min_importance)

        # Merge, deduplicate, and rank
        seen_ids: set[str] = set()
        all_results: list[MemoryEntry] = None

        for entry in short_results + long_results:
            if entry.entry_id not in seen_ids:
                seen_ids.add(entry.entry_id)
                all_results.append(entry)

        # Sort by relevance (similarity score or importance)
        if use_similarity and query_embedding:
            all_results.sort(
                key=lambda e: _cosine_similarity(query_embedding, e.embedding),
                reverse=True,
            )
        else:
            all_results.sort(key=lambda e: e.importance, reverse=True)

        return all_results[:limit]

    # ── Recall ──────────────────────────────────────────────

    def xǁAgentMemoryǁrecall__mutmut_24(
        self,
        query: str,
        limit: int = 10,
        entry_type: str | None = None,
        min_importance: float = 0.0,
        use_similarity: bool = True,
    ) -> list[MemoryEntry]:
        """Recall memories matching a query.

        Uses vector similarity search if use_similarity is True,
        otherwise falls back to keyword matching.

        Args:
            query: The search query.
            limit: Maximum number of results.
            entry_type: Filter by entry type.
            min_importance: Minimum importance threshold.
            use_similarity: Whether to use semantic similarity.

        Returns:
            List of matching MemoryEntry objects, ranked by relevance.
        """
        query_embedding = self._embedding_fn(query) if use_similarity else []

        with self._lock:
            # Search short-term first
            short_results = self._search_entries(
                self._short_term, query_embedding, entry_type, min_importance
            )

            # Search long-term
            long_results = self._search_db(query_embedding, entry_type, min_importance)

        # Merge, deduplicate, and rank
        seen_ids: set[str] = set()
        all_results: list[MemoryEntry] = []

        for entry in short_results - long_results:
            if entry.entry_id not in seen_ids:
                seen_ids.add(entry.entry_id)
                all_results.append(entry)

        # Sort by relevance (similarity score or importance)
        if use_similarity and query_embedding:
            all_results.sort(
                key=lambda e: _cosine_similarity(query_embedding, e.embedding),
                reverse=True,
            )
        else:
            all_results.sort(key=lambda e: e.importance, reverse=True)

        return all_results[:limit]

    # ── Recall ──────────────────────────────────────────────

    def xǁAgentMemoryǁrecall__mutmut_25(
        self,
        query: str,
        limit: int = 10,
        entry_type: str | None = None,
        min_importance: float = 0.0,
        use_similarity: bool = True,
    ) -> list[MemoryEntry]:
        """Recall memories matching a query.

        Uses vector similarity search if use_similarity is True,
        otherwise falls back to keyword matching.

        Args:
            query: The search query.
            limit: Maximum number of results.
            entry_type: Filter by entry type.
            min_importance: Minimum importance threshold.
            use_similarity: Whether to use semantic similarity.

        Returns:
            List of matching MemoryEntry objects, ranked by relevance.
        """
        query_embedding = self._embedding_fn(query) if use_similarity else []

        with self._lock:
            # Search short-term first
            short_results = self._search_entries(
                self._short_term, query_embedding, entry_type, min_importance
            )

            # Search long-term
            long_results = self._search_db(query_embedding, entry_type, min_importance)

        # Merge, deduplicate, and rank
        seen_ids: set[str] = set()
        all_results: list[MemoryEntry] = []

        for entry in short_results + long_results:
            if entry.entry_id in seen_ids:
                seen_ids.add(entry.entry_id)
                all_results.append(entry)

        # Sort by relevance (similarity score or importance)
        if use_similarity and query_embedding:
            all_results.sort(
                key=lambda e: _cosine_similarity(query_embedding, e.embedding),
                reverse=True,
            )
        else:
            all_results.sort(key=lambda e: e.importance, reverse=True)

        return all_results[:limit]

    # ── Recall ──────────────────────────────────────────────

    def xǁAgentMemoryǁrecall__mutmut_26(
        self,
        query: str,
        limit: int = 10,
        entry_type: str | None = None,
        min_importance: float = 0.0,
        use_similarity: bool = True,
    ) -> list[MemoryEntry]:
        """Recall memories matching a query.

        Uses vector similarity search if use_similarity is True,
        otherwise falls back to keyword matching.

        Args:
            query: The search query.
            limit: Maximum number of results.
            entry_type: Filter by entry type.
            min_importance: Minimum importance threshold.
            use_similarity: Whether to use semantic similarity.

        Returns:
            List of matching MemoryEntry objects, ranked by relevance.
        """
        query_embedding = self._embedding_fn(query) if use_similarity else []

        with self._lock:
            # Search short-term first
            short_results = self._search_entries(
                self._short_term, query_embedding, entry_type, min_importance
            )

            # Search long-term
            long_results = self._search_db(query_embedding, entry_type, min_importance)

        # Merge, deduplicate, and rank
        seen_ids: set[str] = set()
        all_results: list[MemoryEntry] = []

        for entry in short_results + long_results:
            if entry.entry_id not in seen_ids:
                seen_ids.add(None)
                all_results.append(entry)

        # Sort by relevance (similarity score or importance)
        if use_similarity and query_embedding:
            all_results.sort(
                key=lambda e: _cosine_similarity(query_embedding, e.embedding),
                reverse=True,
            )
        else:
            all_results.sort(key=lambda e: e.importance, reverse=True)

        return all_results[:limit]

    # ── Recall ──────────────────────────────────────────────

    def xǁAgentMemoryǁrecall__mutmut_27(
        self,
        query: str,
        limit: int = 10,
        entry_type: str | None = None,
        min_importance: float = 0.0,
        use_similarity: bool = True,
    ) -> list[MemoryEntry]:
        """Recall memories matching a query.

        Uses vector similarity search if use_similarity is True,
        otherwise falls back to keyword matching.

        Args:
            query: The search query.
            limit: Maximum number of results.
            entry_type: Filter by entry type.
            min_importance: Minimum importance threshold.
            use_similarity: Whether to use semantic similarity.

        Returns:
            List of matching MemoryEntry objects, ranked by relevance.
        """
        query_embedding = self._embedding_fn(query) if use_similarity else []

        with self._lock:
            # Search short-term first
            short_results = self._search_entries(
                self._short_term, query_embedding, entry_type, min_importance
            )

            # Search long-term
            long_results = self._search_db(query_embedding, entry_type, min_importance)

        # Merge, deduplicate, and rank
        seen_ids: set[str] = set()
        all_results: list[MemoryEntry] = []

        for entry in short_results + long_results:
            if entry.entry_id not in seen_ids:
                seen_ids.add(entry.entry_id)
                all_results.append(None)

        # Sort by relevance (similarity score or importance)
        if use_similarity and query_embedding:
            all_results.sort(
                key=lambda e: _cosine_similarity(query_embedding, e.embedding),
                reverse=True,
            )
        else:
            all_results.sort(key=lambda e: e.importance, reverse=True)

        return all_results[:limit]

    # ── Recall ──────────────────────────────────────────────

    def xǁAgentMemoryǁrecall__mutmut_28(
        self,
        query: str,
        limit: int = 10,
        entry_type: str | None = None,
        min_importance: float = 0.0,
        use_similarity: bool = True,
    ) -> list[MemoryEntry]:
        """Recall memories matching a query.

        Uses vector similarity search if use_similarity is True,
        otherwise falls back to keyword matching.

        Args:
            query: The search query.
            limit: Maximum number of results.
            entry_type: Filter by entry type.
            min_importance: Minimum importance threshold.
            use_similarity: Whether to use semantic similarity.

        Returns:
            List of matching MemoryEntry objects, ranked by relevance.
        """
        query_embedding = self._embedding_fn(query) if use_similarity else []

        with self._lock:
            # Search short-term first
            short_results = self._search_entries(
                self._short_term, query_embedding, entry_type, min_importance
            )

            # Search long-term
            long_results = self._search_db(query_embedding, entry_type, min_importance)

        # Merge, deduplicate, and rank
        seen_ids: set[str] = set()
        all_results: list[MemoryEntry] = []

        for entry in short_results + long_results:
            if entry.entry_id not in seen_ids:
                seen_ids.add(entry.entry_id)
                all_results.append(entry)

        # Sort by relevance (similarity score or importance)
        if use_similarity or query_embedding:
            all_results.sort(
                key=lambda e: _cosine_similarity(query_embedding, e.embedding),
                reverse=True,
            )
        else:
            all_results.sort(key=lambda e: e.importance, reverse=True)

        return all_results[:limit]

    # ── Recall ──────────────────────────────────────────────

    def xǁAgentMemoryǁrecall__mutmut_29(
        self,
        query: str,
        limit: int = 10,
        entry_type: str | None = None,
        min_importance: float = 0.0,
        use_similarity: bool = True,
    ) -> list[MemoryEntry]:
        """Recall memories matching a query.

        Uses vector similarity search if use_similarity is True,
        otherwise falls back to keyword matching.

        Args:
            query: The search query.
            limit: Maximum number of results.
            entry_type: Filter by entry type.
            min_importance: Minimum importance threshold.
            use_similarity: Whether to use semantic similarity.

        Returns:
            List of matching MemoryEntry objects, ranked by relevance.
        """
        query_embedding = self._embedding_fn(query) if use_similarity else []

        with self._lock:
            # Search short-term first
            short_results = self._search_entries(
                self._short_term, query_embedding, entry_type, min_importance
            )

            # Search long-term
            long_results = self._search_db(query_embedding, entry_type, min_importance)

        # Merge, deduplicate, and rank
        seen_ids: set[str] = set()
        all_results: list[MemoryEntry] = []

        for entry in short_results + long_results:
            if entry.entry_id not in seen_ids:
                seen_ids.add(entry.entry_id)
                all_results.append(entry)

        # Sort by relevance (similarity score or importance)
        if use_similarity and query_embedding:
            all_results.sort(
                key=None,
                reverse=True,
            )
        else:
            all_results.sort(key=lambda e: e.importance, reverse=True)

        return all_results[:limit]

    # ── Recall ──────────────────────────────────────────────

    def xǁAgentMemoryǁrecall__mutmut_30(
        self,
        query: str,
        limit: int = 10,
        entry_type: str | None = None,
        min_importance: float = 0.0,
        use_similarity: bool = True,
    ) -> list[MemoryEntry]:
        """Recall memories matching a query.

        Uses vector similarity search if use_similarity is True,
        otherwise falls back to keyword matching.

        Args:
            query: The search query.
            limit: Maximum number of results.
            entry_type: Filter by entry type.
            min_importance: Minimum importance threshold.
            use_similarity: Whether to use semantic similarity.

        Returns:
            List of matching MemoryEntry objects, ranked by relevance.
        """
        query_embedding = self._embedding_fn(query) if use_similarity else []

        with self._lock:
            # Search short-term first
            short_results = self._search_entries(
                self._short_term, query_embedding, entry_type, min_importance
            )

            # Search long-term
            long_results = self._search_db(query_embedding, entry_type, min_importance)

        # Merge, deduplicate, and rank
        seen_ids: set[str] = set()
        all_results: list[MemoryEntry] = []

        for entry in short_results + long_results:
            if entry.entry_id not in seen_ids:
                seen_ids.add(entry.entry_id)
                all_results.append(entry)

        # Sort by relevance (similarity score or importance)
        if use_similarity and query_embedding:
            all_results.sort(
                key=lambda e: _cosine_similarity(query_embedding, e.embedding),
                reverse=None,
            )
        else:
            all_results.sort(key=lambda e: e.importance, reverse=True)

        return all_results[:limit]

    # ── Recall ──────────────────────────────────────────────

    def xǁAgentMemoryǁrecall__mutmut_31(
        self,
        query: str,
        limit: int = 10,
        entry_type: str | None = None,
        min_importance: float = 0.0,
        use_similarity: bool = True,
    ) -> list[MemoryEntry]:
        """Recall memories matching a query.

        Uses vector similarity search if use_similarity is True,
        otherwise falls back to keyword matching.

        Args:
            query: The search query.
            limit: Maximum number of results.
            entry_type: Filter by entry type.
            min_importance: Minimum importance threshold.
            use_similarity: Whether to use semantic similarity.

        Returns:
            List of matching MemoryEntry objects, ranked by relevance.
        """
        query_embedding = self._embedding_fn(query) if use_similarity else []

        with self._lock:
            # Search short-term first
            short_results = self._search_entries(
                self._short_term, query_embedding, entry_type, min_importance
            )

            # Search long-term
            long_results = self._search_db(query_embedding, entry_type, min_importance)

        # Merge, deduplicate, and rank
        seen_ids: set[str] = set()
        all_results: list[MemoryEntry] = []

        for entry in short_results + long_results:
            if entry.entry_id not in seen_ids:
                seen_ids.add(entry.entry_id)
                all_results.append(entry)

        # Sort by relevance (similarity score or importance)
        if use_similarity and query_embedding:
            all_results.sort(
                reverse=True,
            )
        else:
            all_results.sort(key=lambda e: e.importance, reverse=True)

        return all_results[:limit]

    # ── Recall ──────────────────────────────────────────────

    def xǁAgentMemoryǁrecall__mutmut_32(
        self,
        query: str,
        limit: int = 10,
        entry_type: str | None = None,
        min_importance: float = 0.0,
        use_similarity: bool = True,
    ) -> list[MemoryEntry]:
        """Recall memories matching a query.

        Uses vector similarity search if use_similarity is True,
        otherwise falls back to keyword matching.

        Args:
            query: The search query.
            limit: Maximum number of results.
            entry_type: Filter by entry type.
            min_importance: Minimum importance threshold.
            use_similarity: Whether to use semantic similarity.

        Returns:
            List of matching MemoryEntry objects, ranked by relevance.
        """
        query_embedding = self._embedding_fn(query) if use_similarity else []

        with self._lock:
            # Search short-term first
            short_results = self._search_entries(
                self._short_term, query_embedding, entry_type, min_importance
            )

            # Search long-term
            long_results = self._search_db(query_embedding, entry_type, min_importance)

        # Merge, deduplicate, and rank
        seen_ids: set[str] = set()
        all_results: list[MemoryEntry] = []

        for entry in short_results + long_results:
            if entry.entry_id not in seen_ids:
                seen_ids.add(entry.entry_id)
                all_results.append(entry)

        # Sort by relevance (similarity score or importance)
        if use_similarity and query_embedding:
            all_results.sort(
                key=lambda e: _cosine_similarity(query_embedding, e.embedding),
                )
        else:
            all_results.sort(key=lambda e: e.importance, reverse=True)

        return all_results[:limit]

    # ── Recall ──────────────────────────────────────────────

    def xǁAgentMemoryǁrecall__mutmut_33(
        self,
        query: str,
        limit: int = 10,
        entry_type: str | None = None,
        min_importance: float = 0.0,
        use_similarity: bool = True,
    ) -> list[MemoryEntry]:
        """Recall memories matching a query.

        Uses vector similarity search if use_similarity is True,
        otherwise falls back to keyword matching.

        Args:
            query: The search query.
            limit: Maximum number of results.
            entry_type: Filter by entry type.
            min_importance: Minimum importance threshold.
            use_similarity: Whether to use semantic similarity.

        Returns:
            List of matching MemoryEntry objects, ranked by relevance.
        """
        query_embedding = self._embedding_fn(query) if use_similarity else []

        with self._lock:
            # Search short-term first
            short_results = self._search_entries(
                self._short_term, query_embedding, entry_type, min_importance
            )

            # Search long-term
            long_results = self._search_db(query_embedding, entry_type, min_importance)

        # Merge, deduplicate, and rank
        seen_ids: set[str] = set()
        all_results: list[MemoryEntry] = []

        for entry in short_results + long_results:
            if entry.entry_id not in seen_ids:
                seen_ids.add(entry.entry_id)
                all_results.append(entry)

        # Sort by relevance (similarity score or importance)
        if use_similarity and query_embedding:
            all_results.sort(
                key=lambda e: None,
                reverse=True,
            )
        else:
            all_results.sort(key=lambda e: e.importance, reverse=True)

        return all_results[:limit]

    # ── Recall ──────────────────────────────────────────────

    def xǁAgentMemoryǁrecall__mutmut_34(
        self,
        query: str,
        limit: int = 10,
        entry_type: str | None = None,
        min_importance: float = 0.0,
        use_similarity: bool = True,
    ) -> list[MemoryEntry]:
        """Recall memories matching a query.

        Uses vector similarity search if use_similarity is True,
        otherwise falls back to keyword matching.

        Args:
            query: The search query.
            limit: Maximum number of results.
            entry_type: Filter by entry type.
            min_importance: Minimum importance threshold.
            use_similarity: Whether to use semantic similarity.

        Returns:
            List of matching MemoryEntry objects, ranked by relevance.
        """
        query_embedding = self._embedding_fn(query) if use_similarity else []

        with self._lock:
            # Search short-term first
            short_results = self._search_entries(
                self._short_term, query_embedding, entry_type, min_importance
            )

            # Search long-term
            long_results = self._search_db(query_embedding, entry_type, min_importance)

        # Merge, deduplicate, and rank
        seen_ids: set[str] = set()
        all_results: list[MemoryEntry] = []

        for entry in short_results + long_results:
            if entry.entry_id not in seen_ids:
                seen_ids.add(entry.entry_id)
                all_results.append(entry)

        # Sort by relevance (similarity score or importance)
        if use_similarity and query_embedding:
            all_results.sort(
                key=lambda e: _cosine_similarity(None, e.embedding),
                reverse=True,
            )
        else:
            all_results.sort(key=lambda e: e.importance, reverse=True)

        return all_results[:limit]

    # ── Recall ──────────────────────────────────────────────

    def xǁAgentMemoryǁrecall__mutmut_35(
        self,
        query: str,
        limit: int = 10,
        entry_type: str | None = None,
        min_importance: float = 0.0,
        use_similarity: bool = True,
    ) -> list[MemoryEntry]:
        """Recall memories matching a query.

        Uses vector similarity search if use_similarity is True,
        otherwise falls back to keyword matching.

        Args:
            query: The search query.
            limit: Maximum number of results.
            entry_type: Filter by entry type.
            min_importance: Minimum importance threshold.
            use_similarity: Whether to use semantic similarity.

        Returns:
            List of matching MemoryEntry objects, ranked by relevance.
        """
        query_embedding = self._embedding_fn(query) if use_similarity else []

        with self._lock:
            # Search short-term first
            short_results = self._search_entries(
                self._short_term, query_embedding, entry_type, min_importance
            )

            # Search long-term
            long_results = self._search_db(query_embedding, entry_type, min_importance)

        # Merge, deduplicate, and rank
        seen_ids: set[str] = set()
        all_results: list[MemoryEntry] = []

        for entry in short_results + long_results:
            if entry.entry_id not in seen_ids:
                seen_ids.add(entry.entry_id)
                all_results.append(entry)

        # Sort by relevance (similarity score or importance)
        if use_similarity and query_embedding:
            all_results.sort(
                key=lambda e: _cosine_similarity(query_embedding, None),
                reverse=True,
            )
        else:
            all_results.sort(key=lambda e: e.importance, reverse=True)

        return all_results[:limit]

    # ── Recall ──────────────────────────────────────────────

    def xǁAgentMemoryǁrecall__mutmut_36(
        self,
        query: str,
        limit: int = 10,
        entry_type: str | None = None,
        min_importance: float = 0.0,
        use_similarity: bool = True,
    ) -> list[MemoryEntry]:
        """Recall memories matching a query.

        Uses vector similarity search if use_similarity is True,
        otherwise falls back to keyword matching.

        Args:
            query: The search query.
            limit: Maximum number of results.
            entry_type: Filter by entry type.
            min_importance: Minimum importance threshold.
            use_similarity: Whether to use semantic similarity.

        Returns:
            List of matching MemoryEntry objects, ranked by relevance.
        """
        query_embedding = self._embedding_fn(query) if use_similarity else []

        with self._lock:
            # Search short-term first
            short_results = self._search_entries(
                self._short_term, query_embedding, entry_type, min_importance
            )

            # Search long-term
            long_results = self._search_db(query_embedding, entry_type, min_importance)

        # Merge, deduplicate, and rank
        seen_ids: set[str] = set()
        all_results: list[MemoryEntry] = []

        for entry in short_results + long_results:
            if entry.entry_id not in seen_ids:
                seen_ids.add(entry.entry_id)
                all_results.append(entry)

        # Sort by relevance (similarity score or importance)
        if use_similarity and query_embedding:
            all_results.sort(
                key=lambda e: _cosine_similarity(e.embedding),
                reverse=True,
            )
        else:
            all_results.sort(key=lambda e: e.importance, reverse=True)

        return all_results[:limit]

    # ── Recall ──────────────────────────────────────────────

    def xǁAgentMemoryǁrecall__mutmut_37(
        self,
        query: str,
        limit: int = 10,
        entry_type: str | None = None,
        min_importance: float = 0.0,
        use_similarity: bool = True,
    ) -> list[MemoryEntry]:
        """Recall memories matching a query.

        Uses vector similarity search if use_similarity is True,
        otherwise falls back to keyword matching.

        Args:
            query: The search query.
            limit: Maximum number of results.
            entry_type: Filter by entry type.
            min_importance: Minimum importance threshold.
            use_similarity: Whether to use semantic similarity.

        Returns:
            List of matching MemoryEntry objects, ranked by relevance.
        """
        query_embedding = self._embedding_fn(query) if use_similarity else []

        with self._lock:
            # Search short-term first
            short_results = self._search_entries(
                self._short_term, query_embedding, entry_type, min_importance
            )

            # Search long-term
            long_results = self._search_db(query_embedding, entry_type, min_importance)

        # Merge, deduplicate, and rank
        seen_ids: set[str] = set()
        all_results: list[MemoryEntry] = []

        for entry in short_results + long_results:
            if entry.entry_id not in seen_ids:
                seen_ids.add(entry.entry_id)
                all_results.append(entry)

        # Sort by relevance (similarity score or importance)
        if use_similarity and query_embedding:
            all_results.sort(
                key=lambda e: _cosine_similarity(query_embedding, ),
                reverse=True,
            )
        else:
            all_results.sort(key=lambda e: e.importance, reverse=True)

        return all_results[:limit]

    # ── Recall ──────────────────────────────────────────────

    def xǁAgentMemoryǁrecall__mutmut_38(
        self,
        query: str,
        limit: int = 10,
        entry_type: str | None = None,
        min_importance: float = 0.0,
        use_similarity: bool = True,
    ) -> list[MemoryEntry]:
        """Recall memories matching a query.

        Uses vector similarity search if use_similarity is True,
        otherwise falls back to keyword matching.

        Args:
            query: The search query.
            limit: Maximum number of results.
            entry_type: Filter by entry type.
            min_importance: Minimum importance threshold.
            use_similarity: Whether to use semantic similarity.

        Returns:
            List of matching MemoryEntry objects, ranked by relevance.
        """
        query_embedding = self._embedding_fn(query) if use_similarity else []

        with self._lock:
            # Search short-term first
            short_results = self._search_entries(
                self._short_term, query_embedding, entry_type, min_importance
            )

            # Search long-term
            long_results = self._search_db(query_embedding, entry_type, min_importance)

        # Merge, deduplicate, and rank
        seen_ids: set[str] = set()
        all_results: list[MemoryEntry] = []

        for entry in short_results + long_results:
            if entry.entry_id not in seen_ids:
                seen_ids.add(entry.entry_id)
                all_results.append(entry)

        # Sort by relevance (similarity score or importance)
        if use_similarity and query_embedding:
            all_results.sort(
                key=lambda e: _cosine_similarity(query_embedding, e.embedding),
                reverse=False,
            )
        else:
            all_results.sort(key=lambda e: e.importance, reverse=True)

        return all_results[:limit]

    # ── Recall ──────────────────────────────────────────────

    def xǁAgentMemoryǁrecall__mutmut_39(
        self,
        query: str,
        limit: int = 10,
        entry_type: str | None = None,
        min_importance: float = 0.0,
        use_similarity: bool = True,
    ) -> list[MemoryEntry]:
        """Recall memories matching a query.

        Uses vector similarity search if use_similarity is True,
        otherwise falls back to keyword matching.

        Args:
            query: The search query.
            limit: Maximum number of results.
            entry_type: Filter by entry type.
            min_importance: Minimum importance threshold.
            use_similarity: Whether to use semantic similarity.

        Returns:
            List of matching MemoryEntry objects, ranked by relevance.
        """
        query_embedding = self._embedding_fn(query) if use_similarity else []

        with self._lock:
            # Search short-term first
            short_results = self._search_entries(
                self._short_term, query_embedding, entry_type, min_importance
            )

            # Search long-term
            long_results = self._search_db(query_embedding, entry_type, min_importance)

        # Merge, deduplicate, and rank
        seen_ids: set[str] = set()
        all_results: list[MemoryEntry] = []

        for entry in short_results + long_results:
            if entry.entry_id not in seen_ids:
                seen_ids.add(entry.entry_id)
                all_results.append(entry)

        # Sort by relevance (similarity score or importance)
        if use_similarity and query_embedding:
            all_results.sort(
                key=lambda e: _cosine_similarity(query_embedding, e.embedding),
                reverse=True,
            )
        else:
            all_results.sort(key=None, reverse=True)

        return all_results[:limit]

    # ── Recall ──────────────────────────────────────────────

    def xǁAgentMemoryǁrecall__mutmut_40(
        self,
        query: str,
        limit: int = 10,
        entry_type: str | None = None,
        min_importance: float = 0.0,
        use_similarity: bool = True,
    ) -> list[MemoryEntry]:
        """Recall memories matching a query.

        Uses vector similarity search if use_similarity is True,
        otherwise falls back to keyword matching.

        Args:
            query: The search query.
            limit: Maximum number of results.
            entry_type: Filter by entry type.
            min_importance: Minimum importance threshold.
            use_similarity: Whether to use semantic similarity.

        Returns:
            List of matching MemoryEntry objects, ranked by relevance.
        """
        query_embedding = self._embedding_fn(query) if use_similarity else []

        with self._lock:
            # Search short-term first
            short_results = self._search_entries(
                self._short_term, query_embedding, entry_type, min_importance
            )

            # Search long-term
            long_results = self._search_db(query_embedding, entry_type, min_importance)

        # Merge, deduplicate, and rank
        seen_ids: set[str] = set()
        all_results: list[MemoryEntry] = []

        for entry in short_results + long_results:
            if entry.entry_id not in seen_ids:
                seen_ids.add(entry.entry_id)
                all_results.append(entry)

        # Sort by relevance (similarity score or importance)
        if use_similarity and query_embedding:
            all_results.sort(
                key=lambda e: _cosine_similarity(query_embedding, e.embedding),
                reverse=True,
            )
        else:
            all_results.sort(key=lambda e: e.importance, reverse=None)

        return all_results[:limit]

    # ── Recall ──────────────────────────────────────────────

    def xǁAgentMemoryǁrecall__mutmut_41(
        self,
        query: str,
        limit: int = 10,
        entry_type: str | None = None,
        min_importance: float = 0.0,
        use_similarity: bool = True,
    ) -> list[MemoryEntry]:
        """Recall memories matching a query.

        Uses vector similarity search if use_similarity is True,
        otherwise falls back to keyword matching.

        Args:
            query: The search query.
            limit: Maximum number of results.
            entry_type: Filter by entry type.
            min_importance: Minimum importance threshold.
            use_similarity: Whether to use semantic similarity.

        Returns:
            List of matching MemoryEntry objects, ranked by relevance.
        """
        query_embedding = self._embedding_fn(query) if use_similarity else []

        with self._lock:
            # Search short-term first
            short_results = self._search_entries(
                self._short_term, query_embedding, entry_type, min_importance
            )

            # Search long-term
            long_results = self._search_db(query_embedding, entry_type, min_importance)

        # Merge, deduplicate, and rank
        seen_ids: set[str] = set()
        all_results: list[MemoryEntry] = []

        for entry in short_results + long_results:
            if entry.entry_id not in seen_ids:
                seen_ids.add(entry.entry_id)
                all_results.append(entry)

        # Sort by relevance (similarity score or importance)
        if use_similarity and query_embedding:
            all_results.sort(
                key=lambda e: _cosine_similarity(query_embedding, e.embedding),
                reverse=True,
            )
        else:
            all_results.sort(reverse=True)

        return all_results[:limit]

    # ── Recall ──────────────────────────────────────────────

    def xǁAgentMemoryǁrecall__mutmut_42(
        self,
        query: str,
        limit: int = 10,
        entry_type: str | None = None,
        min_importance: float = 0.0,
        use_similarity: bool = True,
    ) -> list[MemoryEntry]:
        """Recall memories matching a query.

        Uses vector similarity search if use_similarity is True,
        otherwise falls back to keyword matching.

        Args:
            query: The search query.
            limit: Maximum number of results.
            entry_type: Filter by entry type.
            min_importance: Minimum importance threshold.
            use_similarity: Whether to use semantic similarity.

        Returns:
            List of matching MemoryEntry objects, ranked by relevance.
        """
        query_embedding = self._embedding_fn(query) if use_similarity else []

        with self._lock:
            # Search short-term first
            short_results = self._search_entries(
                self._short_term, query_embedding, entry_type, min_importance
            )

            # Search long-term
            long_results = self._search_db(query_embedding, entry_type, min_importance)

        # Merge, deduplicate, and rank
        seen_ids: set[str] = set()
        all_results: list[MemoryEntry] = []

        for entry in short_results + long_results:
            if entry.entry_id not in seen_ids:
                seen_ids.add(entry.entry_id)
                all_results.append(entry)

        # Sort by relevance (similarity score or importance)
        if use_similarity and query_embedding:
            all_results.sort(
                key=lambda e: _cosine_similarity(query_embedding, e.embedding),
                reverse=True,
            )
        else:
            all_results.sort(key=lambda e: e.importance, )

        return all_results[:limit]

    # ── Recall ──────────────────────────────────────────────

    def xǁAgentMemoryǁrecall__mutmut_43(
        self,
        query: str,
        limit: int = 10,
        entry_type: str | None = None,
        min_importance: float = 0.0,
        use_similarity: bool = True,
    ) -> list[MemoryEntry]:
        """Recall memories matching a query.

        Uses vector similarity search if use_similarity is True,
        otherwise falls back to keyword matching.

        Args:
            query: The search query.
            limit: Maximum number of results.
            entry_type: Filter by entry type.
            min_importance: Minimum importance threshold.
            use_similarity: Whether to use semantic similarity.

        Returns:
            List of matching MemoryEntry objects, ranked by relevance.
        """
        query_embedding = self._embedding_fn(query) if use_similarity else []

        with self._lock:
            # Search short-term first
            short_results = self._search_entries(
                self._short_term, query_embedding, entry_type, min_importance
            )

            # Search long-term
            long_results = self._search_db(query_embedding, entry_type, min_importance)

        # Merge, deduplicate, and rank
        seen_ids: set[str] = set()
        all_results: list[MemoryEntry] = []

        for entry in short_results + long_results:
            if entry.entry_id not in seen_ids:
                seen_ids.add(entry.entry_id)
                all_results.append(entry)

        # Sort by relevance (similarity score or importance)
        if use_similarity and query_embedding:
            all_results.sort(
                key=lambda e: _cosine_similarity(query_embedding, e.embedding),
                reverse=True,
            )
        else:
            all_results.sort(key=lambda e: None, reverse=True)

        return all_results[:limit]

    # ── Recall ──────────────────────────────────────────────

    def xǁAgentMemoryǁrecall__mutmut_44(
        self,
        query: str,
        limit: int = 10,
        entry_type: str | None = None,
        min_importance: float = 0.0,
        use_similarity: bool = True,
    ) -> list[MemoryEntry]:
        """Recall memories matching a query.

        Uses vector similarity search if use_similarity is True,
        otherwise falls back to keyword matching.

        Args:
            query: The search query.
            limit: Maximum number of results.
            entry_type: Filter by entry type.
            min_importance: Minimum importance threshold.
            use_similarity: Whether to use semantic similarity.

        Returns:
            List of matching MemoryEntry objects, ranked by relevance.
        """
        query_embedding = self._embedding_fn(query) if use_similarity else []

        with self._lock:
            # Search short-term first
            short_results = self._search_entries(
                self._short_term, query_embedding, entry_type, min_importance
            )

            # Search long-term
            long_results = self._search_db(query_embedding, entry_type, min_importance)

        # Merge, deduplicate, and rank
        seen_ids: set[str] = set()
        all_results: list[MemoryEntry] = []

        for entry in short_results + long_results:
            if entry.entry_id not in seen_ids:
                seen_ids.add(entry.entry_id)
                all_results.append(entry)

        # Sort by relevance (similarity score or importance)
        if use_similarity and query_embedding:
            all_results.sort(
                key=lambda e: _cosine_similarity(query_embedding, e.embedding),
                reverse=True,
            )
        else:
            all_results.sort(key=lambda e: e.importance, reverse=False)

        return all_results[:limit]

    @_mutmut_mutated(mutants_xǁAgentMemoryǁ_search_entries__mutmut)
    def _search_entries(
        self,
        entries: list[MemoryEntry],
        query_embedding: list[float],
        entry_type: str | None,
        min_importance: float,
    ) -> list[MemoryEntry]:
        """Filter entries by type and importance, optionally compute similarity."""
        results = []
        for entry in entries:
            if entry_type and entry.entry_type != entry_type:
                continue
            if entry.importance < min_importance:
                continue
            results.append(entry)
        return results

    def xǁAgentMemoryǁ_search_entries__mutmut_orig(
        self,
        entries: list[MemoryEntry],
        query_embedding: list[float],
        entry_type: str | None,
        min_importance: float,
    ) -> list[MemoryEntry]:
        """Filter entries by type and importance, optionally compute similarity."""
        results = []
        for entry in entries:
            if entry_type and entry.entry_type != entry_type:
                continue
            if entry.importance < min_importance:
                continue
            results.append(entry)
        return results

    def xǁAgentMemoryǁ_search_entries__mutmut_1(
        self,
        entries: list[MemoryEntry],
        query_embedding: list[float],
        entry_type: str | None,
        min_importance: float,
    ) -> list[MemoryEntry]:
        """Filter entries by type and importance, optionally compute similarity."""
        results = None
        for entry in entries:
            if entry_type and entry.entry_type != entry_type:
                continue
            if entry.importance < min_importance:
                continue
            results.append(entry)
        return results

    def xǁAgentMemoryǁ_search_entries__mutmut_2(
        self,
        entries: list[MemoryEntry],
        query_embedding: list[float],
        entry_type: str | None,
        min_importance: float,
    ) -> list[MemoryEntry]:
        """Filter entries by type and importance, optionally compute similarity."""
        results = []
        for entry in entries:
            if entry_type or entry.entry_type != entry_type:
                continue
            if entry.importance < min_importance:
                continue
            results.append(entry)
        return results

    def xǁAgentMemoryǁ_search_entries__mutmut_3(
        self,
        entries: list[MemoryEntry],
        query_embedding: list[float],
        entry_type: str | None,
        min_importance: float,
    ) -> list[MemoryEntry]:
        """Filter entries by type and importance, optionally compute similarity."""
        results = []
        for entry in entries:
            if entry_type and entry.entry_type == entry_type:
                continue
            if entry.importance < min_importance:
                continue
            results.append(entry)
        return results

    def xǁAgentMemoryǁ_search_entries__mutmut_4(
        self,
        entries: list[MemoryEntry],
        query_embedding: list[float],
        entry_type: str | None,
        min_importance: float,
    ) -> list[MemoryEntry]:
        """Filter entries by type and importance, optionally compute similarity."""
        results = []
        for entry in entries:
            if entry_type and entry.entry_type != entry_type:
                break
            if entry.importance < min_importance:
                continue
            results.append(entry)
        return results

    def xǁAgentMemoryǁ_search_entries__mutmut_5(
        self,
        entries: list[MemoryEntry],
        query_embedding: list[float],
        entry_type: str | None,
        min_importance: float,
    ) -> list[MemoryEntry]:
        """Filter entries by type and importance, optionally compute similarity."""
        results = []
        for entry in entries:
            if entry_type and entry.entry_type != entry_type:
                continue
            if entry.importance <= min_importance:
                continue
            results.append(entry)
        return results

    def xǁAgentMemoryǁ_search_entries__mutmut_6(
        self,
        entries: list[MemoryEntry],
        query_embedding: list[float],
        entry_type: str | None,
        min_importance: float,
    ) -> list[MemoryEntry]:
        """Filter entries by type and importance, optionally compute similarity."""
        results = []
        for entry in entries:
            if entry_type and entry.entry_type != entry_type:
                continue
            if entry.importance < min_importance:
                break
            results.append(entry)
        return results

    def xǁAgentMemoryǁ_search_entries__mutmut_7(
        self,
        entries: list[MemoryEntry],
        query_embedding: list[float],
        entry_type: str | None,
        min_importance: float,
    ) -> list[MemoryEntry]:
        """Filter entries by type and importance, optionally compute similarity."""
        results = []
        for entry in entries:
            if entry_type and entry.entry_type != entry_type:
                continue
            if entry.importance < min_importance:
                continue
            results.append(None)
        return results

    @_mutmut_mutated(mutants_xǁAgentMemoryǁ_search_db__mutmut)
    def _search_db(
        self,
        query_embedding: list[float],
        entry_type: str | None,
        min_importance: float,
    ) -> list[MemoryEntry]:
        """Search long-term memory in SQLite."""
        if self._conn is None:
            return []

        query = "SELECT * FROM agent_memory WHERE agent_id = ? AND importance >= ?"
        params: list[Any] = [self.agent_id, min_importance]

        if entry_type:
            query += " AND entry_type = ?"
            params.append(entry_type)

        query += " ORDER BY importance DESC, timestamp DESC LIMIT 200"

        try:
            cursor = self._conn.execute(query, params)
            rows = cursor.fetchall()
        except sqlite3.Error:
            return []

        results = []
        for row in rows:
            entry = self._row_to_entry(row)
            results.append(entry)
        return results

    def xǁAgentMemoryǁ_search_db__mutmut_orig(
        self,
        query_embedding: list[float],
        entry_type: str | None,
        min_importance: float,
    ) -> list[MemoryEntry]:
        """Search long-term memory in SQLite."""
        if self._conn is None:
            return []

        query = "SELECT * FROM agent_memory WHERE agent_id = ? AND importance >= ?"
        params: list[Any] = [self.agent_id, min_importance]

        if entry_type:
            query += " AND entry_type = ?"
            params.append(entry_type)

        query += " ORDER BY importance DESC, timestamp DESC LIMIT 200"

        try:
            cursor = self._conn.execute(query, params)
            rows = cursor.fetchall()
        except sqlite3.Error:
            return []

        results = []
        for row in rows:
            entry = self._row_to_entry(row)
            results.append(entry)
        return results

    def xǁAgentMemoryǁ_search_db__mutmut_1(
        self,
        query_embedding: list[float],
        entry_type: str | None,
        min_importance: float,
    ) -> list[MemoryEntry]:
        """Search long-term memory in SQLite."""
        if self._conn is not None:
            return []

        query = "SELECT * FROM agent_memory WHERE agent_id = ? AND importance >= ?"
        params: list[Any] = [self.agent_id, min_importance]

        if entry_type:
            query += " AND entry_type = ?"
            params.append(entry_type)

        query += " ORDER BY importance DESC, timestamp DESC LIMIT 200"

        try:
            cursor = self._conn.execute(query, params)
            rows = cursor.fetchall()
        except sqlite3.Error:
            return []

        results = []
        for row in rows:
            entry = self._row_to_entry(row)
            results.append(entry)
        return results

    def xǁAgentMemoryǁ_search_db__mutmut_2(
        self,
        query_embedding: list[float],
        entry_type: str | None,
        min_importance: float,
    ) -> list[MemoryEntry]:
        """Search long-term memory in SQLite."""
        if self._conn is None:
            return []

        query = None
        params: list[Any] = [self.agent_id, min_importance]

        if entry_type:
            query += " AND entry_type = ?"
            params.append(entry_type)

        query += " ORDER BY importance DESC, timestamp DESC LIMIT 200"

        try:
            cursor = self._conn.execute(query, params)
            rows = cursor.fetchall()
        except sqlite3.Error:
            return []

        results = []
        for row in rows:
            entry = self._row_to_entry(row)
            results.append(entry)
        return results

    def xǁAgentMemoryǁ_search_db__mutmut_3(
        self,
        query_embedding: list[float],
        entry_type: str | None,
        min_importance: float,
    ) -> list[MemoryEntry]:
        """Search long-term memory in SQLite."""
        if self._conn is None:
            return []

        query = "XXSELECT * FROM agent_memory WHERE agent_id = ? AND importance >= ?XX"
        params: list[Any] = [self.agent_id, min_importance]

        if entry_type:
            query += " AND entry_type = ?"
            params.append(entry_type)

        query += " ORDER BY importance DESC, timestamp DESC LIMIT 200"

        try:
            cursor = self._conn.execute(query, params)
            rows = cursor.fetchall()
        except sqlite3.Error:
            return []

        results = []
        for row in rows:
            entry = self._row_to_entry(row)
            results.append(entry)
        return results

    def xǁAgentMemoryǁ_search_db__mutmut_4(
        self,
        query_embedding: list[float],
        entry_type: str | None,
        min_importance: float,
    ) -> list[MemoryEntry]:
        """Search long-term memory in SQLite."""
        if self._conn is None:
            return []

        query = "select * from agent_memory where agent_id = ? and importance >= ?"
        params: list[Any] = [self.agent_id, min_importance]

        if entry_type:
            query += " AND entry_type = ?"
            params.append(entry_type)

        query += " ORDER BY importance DESC, timestamp DESC LIMIT 200"

        try:
            cursor = self._conn.execute(query, params)
            rows = cursor.fetchall()
        except sqlite3.Error:
            return []

        results = []
        for row in rows:
            entry = self._row_to_entry(row)
            results.append(entry)
        return results

    def xǁAgentMemoryǁ_search_db__mutmut_5(
        self,
        query_embedding: list[float],
        entry_type: str | None,
        min_importance: float,
    ) -> list[MemoryEntry]:
        """Search long-term memory in SQLite."""
        if self._conn is None:
            return []

        query = "SELECT * FROM AGENT_MEMORY WHERE AGENT_ID = ? AND IMPORTANCE >= ?"
        params: list[Any] = [self.agent_id, min_importance]

        if entry_type:
            query += " AND entry_type = ?"
            params.append(entry_type)

        query += " ORDER BY importance DESC, timestamp DESC LIMIT 200"

        try:
            cursor = self._conn.execute(query, params)
            rows = cursor.fetchall()
        except sqlite3.Error:
            return []

        results = []
        for row in rows:
            entry = self._row_to_entry(row)
            results.append(entry)
        return results

    def xǁAgentMemoryǁ_search_db__mutmut_6(
        self,
        query_embedding: list[float],
        entry_type: str | None,
        min_importance: float,
    ) -> list[MemoryEntry]:
        """Search long-term memory in SQLite."""
        if self._conn is None:
            return []

        query = "SELECT * FROM agent_memory WHERE agent_id = ? AND importance >= ?"
        params: list[Any] = None

        if entry_type:
            query += " AND entry_type = ?"
            params.append(entry_type)

        query += " ORDER BY importance DESC, timestamp DESC LIMIT 200"

        try:
            cursor = self._conn.execute(query, params)
            rows = cursor.fetchall()
        except sqlite3.Error:
            return []

        results = []
        for row in rows:
            entry = self._row_to_entry(row)
            results.append(entry)
        return results

    def xǁAgentMemoryǁ_search_db__mutmut_7(
        self,
        query_embedding: list[float],
        entry_type: str | None,
        min_importance: float,
    ) -> list[MemoryEntry]:
        """Search long-term memory in SQLite."""
        if self._conn is None:
            return []

        query = "SELECT * FROM agent_memory WHERE agent_id = ? AND importance >= ?"
        params: list[Any] = [self.agent_id, min_importance]

        if entry_type:
            query = " AND entry_type = ?"
            params.append(entry_type)

        query += " ORDER BY importance DESC, timestamp DESC LIMIT 200"

        try:
            cursor = self._conn.execute(query, params)
            rows = cursor.fetchall()
        except sqlite3.Error:
            return []

        results = []
        for row in rows:
            entry = self._row_to_entry(row)
            results.append(entry)
        return results

    def xǁAgentMemoryǁ_search_db__mutmut_8(
        self,
        query_embedding: list[float],
        entry_type: str | None,
        min_importance: float,
    ) -> list[MemoryEntry]:
        """Search long-term memory in SQLite."""
        if self._conn is None:
            return []

        query = "SELECT * FROM agent_memory WHERE agent_id = ? AND importance >= ?"
        params: list[Any] = [self.agent_id, min_importance]

        if entry_type:
            query -= " AND entry_type = ?"
            params.append(entry_type)

        query += " ORDER BY importance DESC, timestamp DESC LIMIT 200"

        try:
            cursor = self._conn.execute(query, params)
            rows = cursor.fetchall()
        except sqlite3.Error:
            return []

        results = []
        for row in rows:
            entry = self._row_to_entry(row)
            results.append(entry)
        return results

    def xǁAgentMemoryǁ_search_db__mutmut_9(
        self,
        query_embedding: list[float],
        entry_type: str | None,
        min_importance: float,
    ) -> list[MemoryEntry]:
        """Search long-term memory in SQLite."""
        if self._conn is None:
            return []

        query = "SELECT * FROM agent_memory WHERE agent_id = ? AND importance >= ?"
        params: list[Any] = [self.agent_id, min_importance]

        if entry_type:
            query += "XX AND entry_type = ?XX"
            params.append(entry_type)

        query += " ORDER BY importance DESC, timestamp DESC LIMIT 200"

        try:
            cursor = self._conn.execute(query, params)
            rows = cursor.fetchall()
        except sqlite3.Error:
            return []

        results = []
        for row in rows:
            entry = self._row_to_entry(row)
            results.append(entry)
        return results

    def xǁAgentMemoryǁ_search_db__mutmut_10(
        self,
        query_embedding: list[float],
        entry_type: str | None,
        min_importance: float,
    ) -> list[MemoryEntry]:
        """Search long-term memory in SQLite."""
        if self._conn is None:
            return []

        query = "SELECT * FROM agent_memory WHERE agent_id = ? AND importance >= ?"
        params: list[Any] = [self.agent_id, min_importance]

        if entry_type:
            query += " and entry_type = ?"
            params.append(entry_type)

        query += " ORDER BY importance DESC, timestamp DESC LIMIT 200"

        try:
            cursor = self._conn.execute(query, params)
            rows = cursor.fetchall()
        except sqlite3.Error:
            return []

        results = []
        for row in rows:
            entry = self._row_to_entry(row)
            results.append(entry)
        return results

    def xǁAgentMemoryǁ_search_db__mutmut_11(
        self,
        query_embedding: list[float],
        entry_type: str | None,
        min_importance: float,
    ) -> list[MemoryEntry]:
        """Search long-term memory in SQLite."""
        if self._conn is None:
            return []

        query = "SELECT * FROM agent_memory WHERE agent_id = ? AND importance >= ?"
        params: list[Any] = [self.agent_id, min_importance]

        if entry_type:
            query += " AND ENTRY_TYPE = ?"
            params.append(entry_type)

        query += " ORDER BY importance DESC, timestamp DESC LIMIT 200"

        try:
            cursor = self._conn.execute(query, params)
            rows = cursor.fetchall()
        except sqlite3.Error:
            return []

        results = []
        for row in rows:
            entry = self._row_to_entry(row)
            results.append(entry)
        return results

    def xǁAgentMemoryǁ_search_db__mutmut_12(
        self,
        query_embedding: list[float],
        entry_type: str | None,
        min_importance: float,
    ) -> list[MemoryEntry]:
        """Search long-term memory in SQLite."""
        if self._conn is None:
            return []

        query = "SELECT * FROM agent_memory WHERE agent_id = ? AND importance >= ?"
        params: list[Any] = [self.agent_id, min_importance]

        if entry_type:
            query += " AND entry_type = ?"
            params.append(None)

        query += " ORDER BY importance DESC, timestamp DESC LIMIT 200"

        try:
            cursor = self._conn.execute(query, params)
            rows = cursor.fetchall()
        except sqlite3.Error:
            return []

        results = []
        for row in rows:
            entry = self._row_to_entry(row)
            results.append(entry)
        return results

    def xǁAgentMemoryǁ_search_db__mutmut_13(
        self,
        query_embedding: list[float],
        entry_type: str | None,
        min_importance: float,
    ) -> list[MemoryEntry]:
        """Search long-term memory in SQLite."""
        if self._conn is None:
            return []

        query = "SELECT * FROM agent_memory WHERE agent_id = ? AND importance >= ?"
        params: list[Any] = [self.agent_id, min_importance]

        if entry_type:
            query += " AND entry_type = ?"
            params.append(entry_type)

        query = " ORDER BY importance DESC, timestamp DESC LIMIT 200"

        try:
            cursor = self._conn.execute(query, params)
            rows = cursor.fetchall()
        except sqlite3.Error:
            return []

        results = []
        for row in rows:
            entry = self._row_to_entry(row)
            results.append(entry)
        return results

    def xǁAgentMemoryǁ_search_db__mutmut_14(
        self,
        query_embedding: list[float],
        entry_type: str | None,
        min_importance: float,
    ) -> list[MemoryEntry]:
        """Search long-term memory in SQLite."""
        if self._conn is None:
            return []

        query = "SELECT * FROM agent_memory WHERE agent_id = ? AND importance >= ?"
        params: list[Any] = [self.agent_id, min_importance]

        if entry_type:
            query += " AND entry_type = ?"
            params.append(entry_type)

        query -= " ORDER BY importance DESC, timestamp DESC LIMIT 200"

        try:
            cursor = self._conn.execute(query, params)
            rows = cursor.fetchall()
        except sqlite3.Error:
            return []

        results = []
        for row in rows:
            entry = self._row_to_entry(row)
            results.append(entry)
        return results

    def xǁAgentMemoryǁ_search_db__mutmut_15(
        self,
        query_embedding: list[float],
        entry_type: str | None,
        min_importance: float,
    ) -> list[MemoryEntry]:
        """Search long-term memory in SQLite."""
        if self._conn is None:
            return []

        query = "SELECT * FROM agent_memory WHERE agent_id = ? AND importance >= ?"
        params: list[Any] = [self.agent_id, min_importance]

        if entry_type:
            query += " AND entry_type = ?"
            params.append(entry_type)

        query += "XX ORDER BY importance DESC, timestamp DESC LIMIT 200XX"

        try:
            cursor = self._conn.execute(query, params)
            rows = cursor.fetchall()
        except sqlite3.Error:
            return []

        results = []
        for row in rows:
            entry = self._row_to_entry(row)
            results.append(entry)
        return results

    def xǁAgentMemoryǁ_search_db__mutmut_16(
        self,
        query_embedding: list[float],
        entry_type: str | None,
        min_importance: float,
    ) -> list[MemoryEntry]:
        """Search long-term memory in SQLite."""
        if self._conn is None:
            return []

        query = "SELECT * FROM agent_memory WHERE agent_id = ? AND importance >= ?"
        params: list[Any] = [self.agent_id, min_importance]

        if entry_type:
            query += " AND entry_type = ?"
            params.append(entry_type)

        query += " order by importance desc, timestamp desc limit 200"

        try:
            cursor = self._conn.execute(query, params)
            rows = cursor.fetchall()
        except sqlite3.Error:
            return []

        results = []
        for row in rows:
            entry = self._row_to_entry(row)
            results.append(entry)
        return results

    def xǁAgentMemoryǁ_search_db__mutmut_17(
        self,
        query_embedding: list[float],
        entry_type: str | None,
        min_importance: float,
    ) -> list[MemoryEntry]:
        """Search long-term memory in SQLite."""
        if self._conn is None:
            return []

        query = "SELECT * FROM agent_memory WHERE agent_id = ? AND importance >= ?"
        params: list[Any] = [self.agent_id, min_importance]

        if entry_type:
            query += " AND entry_type = ?"
            params.append(entry_type)

        query += " ORDER BY IMPORTANCE DESC, TIMESTAMP DESC LIMIT 200"

        try:
            cursor = self._conn.execute(query, params)
            rows = cursor.fetchall()
        except sqlite3.Error:
            return []

        results = []
        for row in rows:
            entry = self._row_to_entry(row)
            results.append(entry)
        return results

    def xǁAgentMemoryǁ_search_db__mutmut_18(
        self,
        query_embedding: list[float],
        entry_type: str | None,
        min_importance: float,
    ) -> list[MemoryEntry]:
        """Search long-term memory in SQLite."""
        if self._conn is None:
            return []

        query = "SELECT * FROM agent_memory WHERE agent_id = ? AND importance >= ?"
        params: list[Any] = [self.agent_id, min_importance]

        if entry_type:
            query += " AND entry_type = ?"
            params.append(entry_type)

        query += " ORDER BY importance DESC, timestamp DESC LIMIT 200"

        try:
            cursor = None
            rows = cursor.fetchall()
        except sqlite3.Error:
            return []

        results = []
        for row in rows:
            entry = self._row_to_entry(row)
            results.append(entry)
        return results

    def xǁAgentMemoryǁ_search_db__mutmut_19(
        self,
        query_embedding: list[float],
        entry_type: str | None,
        min_importance: float,
    ) -> list[MemoryEntry]:
        """Search long-term memory in SQLite."""
        if self._conn is None:
            return []

        query = "SELECT * FROM agent_memory WHERE agent_id = ? AND importance >= ?"
        params: list[Any] = [self.agent_id, min_importance]

        if entry_type:
            query += " AND entry_type = ?"
            params.append(entry_type)

        query += " ORDER BY importance DESC, timestamp DESC LIMIT 200"

        try:
            cursor = self._conn.execute(None, params)
            rows = cursor.fetchall()
        except sqlite3.Error:
            return []

        results = []
        for row in rows:
            entry = self._row_to_entry(row)
            results.append(entry)
        return results

    def xǁAgentMemoryǁ_search_db__mutmut_20(
        self,
        query_embedding: list[float],
        entry_type: str | None,
        min_importance: float,
    ) -> list[MemoryEntry]:
        """Search long-term memory in SQLite."""
        if self._conn is None:
            return []

        query = "SELECT * FROM agent_memory WHERE agent_id = ? AND importance >= ?"
        params: list[Any] = [self.agent_id, min_importance]

        if entry_type:
            query += " AND entry_type = ?"
            params.append(entry_type)

        query += " ORDER BY importance DESC, timestamp DESC LIMIT 200"

        try:
            cursor = self._conn.execute(query, None)
            rows = cursor.fetchall()
        except sqlite3.Error:
            return []

        results = []
        for row in rows:
            entry = self._row_to_entry(row)
            results.append(entry)
        return results

    def xǁAgentMemoryǁ_search_db__mutmut_21(
        self,
        query_embedding: list[float],
        entry_type: str | None,
        min_importance: float,
    ) -> list[MemoryEntry]:
        """Search long-term memory in SQLite."""
        if self._conn is None:
            return []

        query = "SELECT * FROM agent_memory WHERE agent_id = ? AND importance >= ?"
        params: list[Any] = [self.agent_id, min_importance]

        if entry_type:
            query += " AND entry_type = ?"
            params.append(entry_type)

        query += " ORDER BY importance DESC, timestamp DESC LIMIT 200"

        try:
            cursor = self._conn.execute(params)
            rows = cursor.fetchall()
        except sqlite3.Error:
            return []

        results = []
        for row in rows:
            entry = self._row_to_entry(row)
            results.append(entry)
        return results

    def xǁAgentMemoryǁ_search_db__mutmut_22(
        self,
        query_embedding: list[float],
        entry_type: str | None,
        min_importance: float,
    ) -> list[MemoryEntry]:
        """Search long-term memory in SQLite."""
        if self._conn is None:
            return []

        query = "SELECT * FROM agent_memory WHERE agent_id = ? AND importance >= ?"
        params: list[Any] = [self.agent_id, min_importance]

        if entry_type:
            query += " AND entry_type = ?"
            params.append(entry_type)

        query += " ORDER BY importance DESC, timestamp DESC LIMIT 200"

        try:
            cursor = self._conn.execute(query, )
            rows = cursor.fetchall()
        except sqlite3.Error:
            return []

        results = []
        for row in rows:
            entry = self._row_to_entry(row)
            results.append(entry)
        return results

    def xǁAgentMemoryǁ_search_db__mutmut_23(
        self,
        query_embedding: list[float],
        entry_type: str | None,
        min_importance: float,
    ) -> list[MemoryEntry]:
        """Search long-term memory in SQLite."""
        if self._conn is None:
            return []

        query = "SELECT * FROM agent_memory WHERE agent_id = ? AND importance >= ?"
        params: list[Any] = [self.agent_id, min_importance]

        if entry_type:
            query += " AND entry_type = ?"
            params.append(entry_type)

        query += " ORDER BY importance DESC, timestamp DESC LIMIT 200"

        try:
            cursor = self._conn.execute(query, params)
            rows = None
        except sqlite3.Error:
            return []

        results = []
        for row in rows:
            entry = self._row_to_entry(row)
            results.append(entry)
        return results

    def xǁAgentMemoryǁ_search_db__mutmut_24(
        self,
        query_embedding: list[float],
        entry_type: str | None,
        min_importance: float,
    ) -> list[MemoryEntry]:
        """Search long-term memory in SQLite."""
        if self._conn is None:
            return []

        query = "SELECT * FROM agent_memory WHERE agent_id = ? AND importance >= ?"
        params: list[Any] = [self.agent_id, min_importance]

        if entry_type:
            query += " AND entry_type = ?"
            params.append(entry_type)

        query += " ORDER BY importance DESC, timestamp DESC LIMIT 200"

        try:
            cursor = self._conn.execute(query, params)
            rows = cursor.fetchall()
        except sqlite3.Error:
            return []

        results = None
        for row in rows:
            entry = self._row_to_entry(row)
            results.append(entry)
        return results

    def xǁAgentMemoryǁ_search_db__mutmut_25(
        self,
        query_embedding: list[float],
        entry_type: str | None,
        min_importance: float,
    ) -> list[MemoryEntry]:
        """Search long-term memory in SQLite."""
        if self._conn is None:
            return []

        query = "SELECT * FROM agent_memory WHERE agent_id = ? AND importance >= ?"
        params: list[Any] = [self.agent_id, min_importance]

        if entry_type:
            query += " AND entry_type = ?"
            params.append(entry_type)

        query += " ORDER BY importance DESC, timestamp DESC LIMIT 200"

        try:
            cursor = self._conn.execute(query, params)
            rows = cursor.fetchall()
        except sqlite3.Error:
            return []

        results = []
        for row in rows:
            entry = None
            results.append(entry)
        return results

    def xǁAgentMemoryǁ_search_db__mutmut_26(
        self,
        query_embedding: list[float],
        entry_type: str | None,
        min_importance: float,
    ) -> list[MemoryEntry]:
        """Search long-term memory in SQLite."""
        if self._conn is None:
            return []

        query = "SELECT * FROM agent_memory WHERE agent_id = ? AND importance >= ?"
        params: list[Any] = [self.agent_id, min_importance]

        if entry_type:
            query += " AND entry_type = ?"
            params.append(entry_type)

        query += " ORDER BY importance DESC, timestamp DESC LIMIT 200"

        try:
            cursor = self._conn.execute(query, params)
            rows = cursor.fetchall()
        except sqlite3.Error:
            return []

        results = []
        for row in rows:
            entry = self._row_to_entry(None)
            results.append(entry)
        return results

    def xǁAgentMemoryǁ_search_db__mutmut_27(
        self,
        query_embedding: list[float],
        entry_type: str | None,
        min_importance: float,
    ) -> list[MemoryEntry]:
        """Search long-term memory in SQLite."""
        if self._conn is None:
            return []

        query = "SELECT * FROM agent_memory WHERE agent_id = ? AND importance >= ?"
        params: list[Any] = [self.agent_id, min_importance]

        if entry_type:
            query += " AND entry_type = ?"
            params.append(entry_type)

        query += " ORDER BY importance DESC, timestamp DESC LIMIT 200"

        try:
            cursor = self._conn.execute(query, params)
            rows = cursor.fetchall()
        except sqlite3.Error:
            return []

        results = []
        for row in rows:
            entry = self._row_to_entry(row)
            results.append(None)
        return results

    @_mutmut_mutated(mutants_xǁAgentMemoryǁ_row_to_entry__mutmut)
    def _row_to_entry(self, row: tuple) -> MemoryEntry:
        """Convert a database row to a MemoryEntry."""
        embedding_str = row[5] if len(row) > 5 else ""
        embedding = [float(v) for v in embedding_str.split(",") if v] if embedding_str else []

        import json

        return MemoryEntry(
            entry_id=row[0],
            agent_id=row[1],
            content=row[2],
            entry_type=row[3],
            importance=row[4],
            embedding=embedding,
            metadata=json.loads(row[6]) if len(row) > 6 and row[6] else {},
            timestamp=row[7],
            access_count=row[8] if len(row) > 8 else 0,
            last_accessed=row[9] if len(row) > 9 else 0.0,
        )

    def xǁAgentMemoryǁ_row_to_entry__mutmut_orig(self, row: tuple) -> MemoryEntry:
        """Convert a database row to a MemoryEntry."""
        embedding_str = row[5] if len(row) > 5 else ""
        embedding = [float(v) for v in embedding_str.split(",") if v] if embedding_str else []

        import json

        return MemoryEntry(
            entry_id=row[0],
            agent_id=row[1],
            content=row[2],
            entry_type=row[3],
            importance=row[4],
            embedding=embedding,
            metadata=json.loads(row[6]) if len(row) > 6 and row[6] else {},
            timestamp=row[7],
            access_count=row[8] if len(row) > 8 else 0,
            last_accessed=row[9] if len(row) > 9 else 0.0,
        )

    def xǁAgentMemoryǁ_row_to_entry__mutmut_1(self, row: tuple) -> MemoryEntry:
        """Convert a database row to a MemoryEntry."""
        embedding_str = None
        embedding = [float(v) for v in embedding_str.split(",") if v] if embedding_str else []

        import json

        return MemoryEntry(
            entry_id=row[0],
            agent_id=row[1],
            content=row[2],
            entry_type=row[3],
            importance=row[4],
            embedding=embedding,
            metadata=json.loads(row[6]) if len(row) > 6 and row[6] else {},
            timestamp=row[7],
            access_count=row[8] if len(row) > 8 else 0,
            last_accessed=row[9] if len(row) > 9 else 0.0,
        )

    def xǁAgentMemoryǁ_row_to_entry__mutmut_2(self, row: tuple) -> MemoryEntry:
        """Convert a database row to a MemoryEntry."""
        embedding_str = row[6] if len(row) > 5 else ""
        embedding = [float(v) for v in embedding_str.split(",") if v] if embedding_str else []

        import json

        return MemoryEntry(
            entry_id=row[0],
            agent_id=row[1],
            content=row[2],
            entry_type=row[3],
            importance=row[4],
            embedding=embedding,
            metadata=json.loads(row[6]) if len(row) > 6 and row[6] else {},
            timestamp=row[7],
            access_count=row[8] if len(row) > 8 else 0,
            last_accessed=row[9] if len(row) > 9 else 0.0,
        )

    def xǁAgentMemoryǁ_row_to_entry__mutmut_3(self, row: tuple) -> MemoryEntry:
        """Convert a database row to a MemoryEntry."""
        embedding_str = row[5] if len(row) >= 5 else ""
        embedding = [float(v) for v in embedding_str.split(",") if v] if embedding_str else []

        import json

        return MemoryEntry(
            entry_id=row[0],
            agent_id=row[1],
            content=row[2],
            entry_type=row[3],
            importance=row[4],
            embedding=embedding,
            metadata=json.loads(row[6]) if len(row) > 6 and row[6] else {},
            timestamp=row[7],
            access_count=row[8] if len(row) > 8 else 0,
            last_accessed=row[9] if len(row) > 9 else 0.0,
        )

    def xǁAgentMemoryǁ_row_to_entry__mutmut_4(self, row: tuple) -> MemoryEntry:
        """Convert a database row to a MemoryEntry."""
        embedding_str = row[5] if len(row) > 6 else ""
        embedding = [float(v) for v in embedding_str.split(",") if v] if embedding_str else []

        import json

        return MemoryEntry(
            entry_id=row[0],
            agent_id=row[1],
            content=row[2],
            entry_type=row[3],
            importance=row[4],
            embedding=embedding,
            metadata=json.loads(row[6]) if len(row) > 6 and row[6] else {},
            timestamp=row[7],
            access_count=row[8] if len(row) > 8 else 0,
            last_accessed=row[9] if len(row) > 9 else 0.0,
        )

    def xǁAgentMemoryǁ_row_to_entry__mutmut_5(self, row: tuple) -> MemoryEntry:
        """Convert a database row to a MemoryEntry."""
        embedding_str = row[5] if len(row) > 5 else "XXXX"
        embedding = [float(v) for v in embedding_str.split(",") if v] if embedding_str else []

        import json

        return MemoryEntry(
            entry_id=row[0],
            agent_id=row[1],
            content=row[2],
            entry_type=row[3],
            importance=row[4],
            embedding=embedding,
            metadata=json.loads(row[6]) if len(row) > 6 and row[6] else {},
            timestamp=row[7],
            access_count=row[8] if len(row) > 8 else 0,
            last_accessed=row[9] if len(row) > 9 else 0.0,
        )

    def xǁAgentMemoryǁ_row_to_entry__mutmut_6(self, row: tuple) -> MemoryEntry:
        """Convert a database row to a MemoryEntry."""
        embedding_str = row[5] if len(row) > 5 else ""
        embedding = None

        import json

        return MemoryEntry(
            entry_id=row[0],
            agent_id=row[1],
            content=row[2],
            entry_type=row[3],
            importance=row[4],
            embedding=embedding,
            metadata=json.loads(row[6]) if len(row) > 6 and row[6] else {},
            timestamp=row[7],
            access_count=row[8] if len(row) > 8 else 0,
            last_accessed=row[9] if len(row) > 9 else 0.0,
        )

    def xǁAgentMemoryǁ_row_to_entry__mutmut_7(self, row: tuple) -> MemoryEntry:
        """Convert a database row to a MemoryEntry."""
        embedding_str = row[5] if len(row) > 5 else ""
        embedding = [float(None) for v in embedding_str.split(",") if v] if embedding_str else []

        import json

        return MemoryEntry(
            entry_id=row[0],
            agent_id=row[1],
            content=row[2],
            entry_type=row[3],
            importance=row[4],
            embedding=embedding,
            metadata=json.loads(row[6]) if len(row) > 6 and row[6] else {},
            timestamp=row[7],
            access_count=row[8] if len(row) > 8 else 0,
            last_accessed=row[9] if len(row) > 9 else 0.0,
        )

    def xǁAgentMemoryǁ_row_to_entry__mutmut_8(self, row: tuple) -> MemoryEntry:
        """Convert a database row to a MemoryEntry."""
        embedding_str = row[5] if len(row) > 5 else ""
        embedding = [float(v) for v in embedding_str.split(None) if v] if embedding_str else []

        import json

        return MemoryEntry(
            entry_id=row[0],
            agent_id=row[1],
            content=row[2],
            entry_type=row[3],
            importance=row[4],
            embedding=embedding,
            metadata=json.loads(row[6]) if len(row) > 6 and row[6] else {},
            timestamp=row[7],
            access_count=row[8] if len(row) > 8 else 0,
            last_accessed=row[9] if len(row) > 9 else 0.0,
        )

    def xǁAgentMemoryǁ_row_to_entry__mutmut_9(self, row: tuple) -> MemoryEntry:
        """Convert a database row to a MemoryEntry."""
        embedding_str = row[5] if len(row) > 5 else ""
        embedding = [float(v) for v in embedding_str.split("XX,XX") if v] if embedding_str else []

        import json

        return MemoryEntry(
            entry_id=row[0],
            agent_id=row[1],
            content=row[2],
            entry_type=row[3],
            importance=row[4],
            embedding=embedding,
            metadata=json.loads(row[6]) if len(row) > 6 and row[6] else {},
            timestamp=row[7],
            access_count=row[8] if len(row) > 8 else 0,
            last_accessed=row[9] if len(row) > 9 else 0.0,
        )

    def xǁAgentMemoryǁ_row_to_entry__mutmut_10(self, row: tuple) -> MemoryEntry:
        """Convert a database row to a MemoryEntry."""
        embedding_str = row[5] if len(row) > 5 else ""
        embedding = [float(v) for v in embedding_str.split(",") if v] if embedding_str else []

        import json

        return MemoryEntry(
            entry_id=None,
            agent_id=row[1],
            content=row[2],
            entry_type=row[3],
            importance=row[4],
            embedding=embedding,
            metadata=json.loads(row[6]) if len(row) > 6 and row[6] else {},
            timestamp=row[7],
            access_count=row[8] if len(row) > 8 else 0,
            last_accessed=row[9] if len(row) > 9 else 0.0,
        )

    def xǁAgentMemoryǁ_row_to_entry__mutmut_11(self, row: tuple) -> MemoryEntry:
        """Convert a database row to a MemoryEntry."""
        embedding_str = row[5] if len(row) > 5 else ""
        embedding = [float(v) for v in embedding_str.split(",") if v] if embedding_str else []

        import json

        return MemoryEntry(
            entry_id=row[0],
            agent_id=None,
            content=row[2],
            entry_type=row[3],
            importance=row[4],
            embedding=embedding,
            metadata=json.loads(row[6]) if len(row) > 6 and row[6] else {},
            timestamp=row[7],
            access_count=row[8] if len(row) > 8 else 0,
            last_accessed=row[9] if len(row) > 9 else 0.0,
        )

    def xǁAgentMemoryǁ_row_to_entry__mutmut_12(self, row: tuple) -> MemoryEntry:
        """Convert a database row to a MemoryEntry."""
        embedding_str = row[5] if len(row) > 5 else ""
        embedding = [float(v) for v in embedding_str.split(",") if v] if embedding_str else []

        import json

        return MemoryEntry(
            entry_id=row[0],
            agent_id=row[1],
            content=None,
            entry_type=row[3],
            importance=row[4],
            embedding=embedding,
            metadata=json.loads(row[6]) if len(row) > 6 and row[6] else {},
            timestamp=row[7],
            access_count=row[8] if len(row) > 8 else 0,
            last_accessed=row[9] if len(row) > 9 else 0.0,
        )

    def xǁAgentMemoryǁ_row_to_entry__mutmut_13(self, row: tuple) -> MemoryEntry:
        """Convert a database row to a MemoryEntry."""
        embedding_str = row[5] if len(row) > 5 else ""
        embedding = [float(v) for v in embedding_str.split(",") if v] if embedding_str else []

        import json

        return MemoryEntry(
            entry_id=row[0],
            agent_id=row[1],
            content=row[2],
            entry_type=None,
            importance=row[4],
            embedding=embedding,
            metadata=json.loads(row[6]) if len(row) > 6 and row[6] else {},
            timestamp=row[7],
            access_count=row[8] if len(row) > 8 else 0,
            last_accessed=row[9] if len(row) > 9 else 0.0,
        )

    def xǁAgentMemoryǁ_row_to_entry__mutmut_14(self, row: tuple) -> MemoryEntry:
        """Convert a database row to a MemoryEntry."""
        embedding_str = row[5] if len(row) > 5 else ""
        embedding = [float(v) for v in embedding_str.split(",") if v] if embedding_str else []

        import json

        return MemoryEntry(
            entry_id=row[0],
            agent_id=row[1],
            content=row[2],
            entry_type=row[3],
            importance=None,
            embedding=embedding,
            metadata=json.loads(row[6]) if len(row) > 6 and row[6] else {},
            timestamp=row[7],
            access_count=row[8] if len(row) > 8 else 0,
            last_accessed=row[9] if len(row) > 9 else 0.0,
        )

    def xǁAgentMemoryǁ_row_to_entry__mutmut_15(self, row: tuple) -> MemoryEntry:
        """Convert a database row to a MemoryEntry."""
        embedding_str = row[5] if len(row) > 5 else ""
        embedding = [float(v) for v in embedding_str.split(",") if v] if embedding_str else []

        import json

        return MemoryEntry(
            entry_id=row[0],
            agent_id=row[1],
            content=row[2],
            entry_type=row[3],
            importance=row[4],
            embedding=None,
            metadata=json.loads(row[6]) if len(row) > 6 and row[6] else {},
            timestamp=row[7],
            access_count=row[8] if len(row) > 8 else 0,
            last_accessed=row[9] if len(row) > 9 else 0.0,
        )

    def xǁAgentMemoryǁ_row_to_entry__mutmut_16(self, row: tuple) -> MemoryEntry:
        """Convert a database row to a MemoryEntry."""
        embedding_str = row[5] if len(row) > 5 else ""
        embedding = [float(v) for v in embedding_str.split(",") if v] if embedding_str else []

        import json

        return MemoryEntry(
            entry_id=row[0],
            agent_id=row[1],
            content=row[2],
            entry_type=row[3],
            importance=row[4],
            embedding=embedding,
            metadata=None,
            timestamp=row[7],
            access_count=row[8] if len(row) > 8 else 0,
            last_accessed=row[9] if len(row) > 9 else 0.0,
        )

    def xǁAgentMemoryǁ_row_to_entry__mutmut_17(self, row: tuple) -> MemoryEntry:
        """Convert a database row to a MemoryEntry."""
        embedding_str = row[5] if len(row) > 5 else ""
        embedding = [float(v) for v in embedding_str.split(",") if v] if embedding_str else []

        import json

        return MemoryEntry(
            entry_id=row[0],
            agent_id=row[1],
            content=row[2],
            entry_type=row[3],
            importance=row[4],
            embedding=embedding,
            metadata=json.loads(row[6]) if len(row) > 6 and row[6] else {},
            timestamp=None,
            access_count=row[8] if len(row) > 8 else 0,
            last_accessed=row[9] if len(row) > 9 else 0.0,
        )

    def xǁAgentMemoryǁ_row_to_entry__mutmut_18(self, row: tuple) -> MemoryEntry:
        """Convert a database row to a MemoryEntry."""
        embedding_str = row[5] if len(row) > 5 else ""
        embedding = [float(v) for v in embedding_str.split(",") if v] if embedding_str else []

        import json

        return MemoryEntry(
            entry_id=row[0],
            agent_id=row[1],
            content=row[2],
            entry_type=row[3],
            importance=row[4],
            embedding=embedding,
            metadata=json.loads(row[6]) if len(row) > 6 and row[6] else {},
            timestamp=row[7],
            access_count=None,
            last_accessed=row[9] if len(row) > 9 else 0.0,
        )

    def xǁAgentMemoryǁ_row_to_entry__mutmut_19(self, row: tuple) -> MemoryEntry:
        """Convert a database row to a MemoryEntry."""
        embedding_str = row[5] if len(row) > 5 else ""
        embedding = [float(v) for v in embedding_str.split(",") if v] if embedding_str else []

        import json

        return MemoryEntry(
            entry_id=row[0],
            agent_id=row[1],
            content=row[2],
            entry_type=row[3],
            importance=row[4],
            embedding=embedding,
            metadata=json.loads(row[6]) if len(row) > 6 and row[6] else {},
            timestamp=row[7],
            access_count=row[8] if len(row) > 8 else 0,
            last_accessed=None,
        )

    def xǁAgentMemoryǁ_row_to_entry__mutmut_20(self, row: tuple) -> MemoryEntry:
        """Convert a database row to a MemoryEntry."""
        embedding_str = row[5] if len(row) > 5 else ""
        embedding = [float(v) for v in embedding_str.split(",") if v] if embedding_str else []

        import json

        return MemoryEntry(
            agent_id=row[1],
            content=row[2],
            entry_type=row[3],
            importance=row[4],
            embedding=embedding,
            metadata=json.loads(row[6]) if len(row) > 6 and row[6] else {},
            timestamp=row[7],
            access_count=row[8] if len(row) > 8 else 0,
            last_accessed=row[9] if len(row) > 9 else 0.0,
        )

    def xǁAgentMemoryǁ_row_to_entry__mutmut_21(self, row: tuple) -> MemoryEntry:
        """Convert a database row to a MemoryEntry."""
        embedding_str = row[5] if len(row) > 5 else ""
        embedding = [float(v) for v in embedding_str.split(",") if v] if embedding_str else []

        import json

        return MemoryEntry(
            entry_id=row[0],
            content=row[2],
            entry_type=row[3],
            importance=row[4],
            embedding=embedding,
            metadata=json.loads(row[6]) if len(row) > 6 and row[6] else {},
            timestamp=row[7],
            access_count=row[8] if len(row) > 8 else 0,
            last_accessed=row[9] if len(row) > 9 else 0.0,
        )

    def xǁAgentMemoryǁ_row_to_entry__mutmut_22(self, row: tuple) -> MemoryEntry:
        """Convert a database row to a MemoryEntry."""
        embedding_str = row[5] if len(row) > 5 else ""
        embedding = [float(v) for v in embedding_str.split(",") if v] if embedding_str else []

        import json

        return MemoryEntry(
            entry_id=row[0],
            agent_id=row[1],
            entry_type=row[3],
            importance=row[4],
            embedding=embedding,
            metadata=json.loads(row[6]) if len(row) > 6 and row[6] else {},
            timestamp=row[7],
            access_count=row[8] if len(row) > 8 else 0,
            last_accessed=row[9] if len(row) > 9 else 0.0,
        )

    def xǁAgentMemoryǁ_row_to_entry__mutmut_23(self, row: tuple) -> MemoryEntry:
        """Convert a database row to a MemoryEntry."""
        embedding_str = row[5] if len(row) > 5 else ""
        embedding = [float(v) for v in embedding_str.split(",") if v] if embedding_str else []

        import json

        return MemoryEntry(
            entry_id=row[0],
            agent_id=row[1],
            content=row[2],
            importance=row[4],
            embedding=embedding,
            metadata=json.loads(row[6]) if len(row) > 6 and row[6] else {},
            timestamp=row[7],
            access_count=row[8] if len(row) > 8 else 0,
            last_accessed=row[9] if len(row) > 9 else 0.0,
        )

    def xǁAgentMemoryǁ_row_to_entry__mutmut_24(self, row: tuple) -> MemoryEntry:
        """Convert a database row to a MemoryEntry."""
        embedding_str = row[5] if len(row) > 5 else ""
        embedding = [float(v) for v in embedding_str.split(",") if v] if embedding_str else []

        import json

        return MemoryEntry(
            entry_id=row[0],
            agent_id=row[1],
            content=row[2],
            entry_type=row[3],
            embedding=embedding,
            metadata=json.loads(row[6]) if len(row) > 6 and row[6] else {},
            timestamp=row[7],
            access_count=row[8] if len(row) > 8 else 0,
            last_accessed=row[9] if len(row) > 9 else 0.0,
        )

    def xǁAgentMemoryǁ_row_to_entry__mutmut_25(self, row: tuple) -> MemoryEntry:
        """Convert a database row to a MemoryEntry."""
        embedding_str = row[5] if len(row) > 5 else ""
        embedding = [float(v) for v in embedding_str.split(",") if v] if embedding_str else []

        import json

        return MemoryEntry(
            entry_id=row[0],
            agent_id=row[1],
            content=row[2],
            entry_type=row[3],
            importance=row[4],
            metadata=json.loads(row[6]) if len(row) > 6 and row[6] else {},
            timestamp=row[7],
            access_count=row[8] if len(row) > 8 else 0,
            last_accessed=row[9] if len(row) > 9 else 0.0,
        )

    def xǁAgentMemoryǁ_row_to_entry__mutmut_26(self, row: tuple) -> MemoryEntry:
        """Convert a database row to a MemoryEntry."""
        embedding_str = row[5] if len(row) > 5 else ""
        embedding = [float(v) for v in embedding_str.split(",") if v] if embedding_str else []

        import json

        return MemoryEntry(
            entry_id=row[0],
            agent_id=row[1],
            content=row[2],
            entry_type=row[3],
            importance=row[4],
            embedding=embedding,
            timestamp=row[7],
            access_count=row[8] if len(row) > 8 else 0,
            last_accessed=row[9] if len(row) > 9 else 0.0,
        )

    def xǁAgentMemoryǁ_row_to_entry__mutmut_27(self, row: tuple) -> MemoryEntry:
        """Convert a database row to a MemoryEntry."""
        embedding_str = row[5] if len(row) > 5 else ""
        embedding = [float(v) for v in embedding_str.split(",") if v] if embedding_str else []

        import json

        return MemoryEntry(
            entry_id=row[0],
            agent_id=row[1],
            content=row[2],
            entry_type=row[3],
            importance=row[4],
            embedding=embedding,
            metadata=json.loads(row[6]) if len(row) > 6 and row[6] else {},
            access_count=row[8] if len(row) > 8 else 0,
            last_accessed=row[9] if len(row) > 9 else 0.0,
        )

    def xǁAgentMemoryǁ_row_to_entry__mutmut_28(self, row: tuple) -> MemoryEntry:
        """Convert a database row to a MemoryEntry."""
        embedding_str = row[5] if len(row) > 5 else ""
        embedding = [float(v) for v in embedding_str.split(",") if v] if embedding_str else []

        import json

        return MemoryEntry(
            entry_id=row[0],
            agent_id=row[1],
            content=row[2],
            entry_type=row[3],
            importance=row[4],
            embedding=embedding,
            metadata=json.loads(row[6]) if len(row) > 6 and row[6] else {},
            timestamp=row[7],
            last_accessed=row[9] if len(row) > 9 else 0.0,
        )

    def xǁAgentMemoryǁ_row_to_entry__mutmut_29(self, row: tuple) -> MemoryEntry:
        """Convert a database row to a MemoryEntry."""
        embedding_str = row[5] if len(row) > 5 else ""
        embedding = [float(v) for v in embedding_str.split(",") if v] if embedding_str else []

        import json

        return MemoryEntry(
            entry_id=row[0],
            agent_id=row[1],
            content=row[2],
            entry_type=row[3],
            importance=row[4],
            embedding=embedding,
            metadata=json.loads(row[6]) if len(row) > 6 and row[6] else {},
            timestamp=row[7],
            access_count=row[8] if len(row) > 8 else 0,
            )

    def xǁAgentMemoryǁ_row_to_entry__mutmut_30(self, row: tuple) -> MemoryEntry:
        """Convert a database row to a MemoryEntry."""
        embedding_str = row[5] if len(row) > 5 else ""
        embedding = [float(v) for v in embedding_str.split(",") if v] if embedding_str else []

        import json

        return MemoryEntry(
            entry_id=row[1],
            agent_id=row[1],
            content=row[2],
            entry_type=row[3],
            importance=row[4],
            embedding=embedding,
            metadata=json.loads(row[6]) if len(row) > 6 and row[6] else {},
            timestamp=row[7],
            access_count=row[8] if len(row) > 8 else 0,
            last_accessed=row[9] if len(row) > 9 else 0.0,
        )

    def xǁAgentMemoryǁ_row_to_entry__mutmut_31(self, row: tuple) -> MemoryEntry:
        """Convert a database row to a MemoryEntry."""
        embedding_str = row[5] if len(row) > 5 else ""
        embedding = [float(v) for v in embedding_str.split(",") if v] if embedding_str else []

        import json

        return MemoryEntry(
            entry_id=row[0],
            agent_id=row[2],
            content=row[2],
            entry_type=row[3],
            importance=row[4],
            embedding=embedding,
            metadata=json.loads(row[6]) if len(row) > 6 and row[6] else {},
            timestamp=row[7],
            access_count=row[8] if len(row) > 8 else 0,
            last_accessed=row[9] if len(row) > 9 else 0.0,
        )

    def xǁAgentMemoryǁ_row_to_entry__mutmut_32(self, row: tuple) -> MemoryEntry:
        """Convert a database row to a MemoryEntry."""
        embedding_str = row[5] if len(row) > 5 else ""
        embedding = [float(v) for v in embedding_str.split(",") if v] if embedding_str else []

        import json

        return MemoryEntry(
            entry_id=row[0],
            agent_id=row[1],
            content=row[3],
            entry_type=row[3],
            importance=row[4],
            embedding=embedding,
            metadata=json.loads(row[6]) if len(row) > 6 and row[6] else {},
            timestamp=row[7],
            access_count=row[8] if len(row) > 8 else 0,
            last_accessed=row[9] if len(row) > 9 else 0.0,
        )

    def xǁAgentMemoryǁ_row_to_entry__mutmut_33(self, row: tuple) -> MemoryEntry:
        """Convert a database row to a MemoryEntry."""
        embedding_str = row[5] if len(row) > 5 else ""
        embedding = [float(v) for v in embedding_str.split(",") if v] if embedding_str else []

        import json

        return MemoryEntry(
            entry_id=row[0],
            agent_id=row[1],
            content=row[2],
            entry_type=row[4],
            importance=row[4],
            embedding=embedding,
            metadata=json.loads(row[6]) if len(row) > 6 and row[6] else {},
            timestamp=row[7],
            access_count=row[8] if len(row) > 8 else 0,
            last_accessed=row[9] if len(row) > 9 else 0.0,
        )

    def xǁAgentMemoryǁ_row_to_entry__mutmut_34(self, row: tuple) -> MemoryEntry:
        """Convert a database row to a MemoryEntry."""
        embedding_str = row[5] if len(row) > 5 else ""
        embedding = [float(v) for v in embedding_str.split(",") if v] if embedding_str else []

        import json

        return MemoryEntry(
            entry_id=row[0],
            agent_id=row[1],
            content=row[2],
            entry_type=row[3],
            importance=row[5],
            embedding=embedding,
            metadata=json.loads(row[6]) if len(row) > 6 and row[6] else {},
            timestamp=row[7],
            access_count=row[8] if len(row) > 8 else 0,
            last_accessed=row[9] if len(row) > 9 else 0.0,
        )

    def xǁAgentMemoryǁ_row_to_entry__mutmut_35(self, row: tuple) -> MemoryEntry:
        """Convert a database row to a MemoryEntry."""
        embedding_str = row[5] if len(row) > 5 else ""
        embedding = [float(v) for v in embedding_str.split(",") if v] if embedding_str else []

        import json

        return MemoryEntry(
            entry_id=row[0],
            agent_id=row[1],
            content=row[2],
            entry_type=row[3],
            importance=row[4],
            embedding=embedding,
            metadata=json.loads(None) if len(row) > 6 and row[6] else {},
            timestamp=row[7],
            access_count=row[8] if len(row) > 8 else 0,
            last_accessed=row[9] if len(row) > 9 else 0.0,
        )

    def xǁAgentMemoryǁ_row_to_entry__mutmut_36(self, row: tuple) -> MemoryEntry:
        """Convert a database row to a MemoryEntry."""
        embedding_str = row[5] if len(row) > 5 else ""
        embedding = [float(v) for v in embedding_str.split(",") if v] if embedding_str else []

        import json

        return MemoryEntry(
            entry_id=row[0],
            agent_id=row[1],
            content=row[2],
            entry_type=row[3],
            importance=row[4],
            embedding=embedding,
            metadata=json.loads(row[7]) if len(row) > 6 and row[6] else {},
            timestamp=row[7],
            access_count=row[8] if len(row) > 8 else 0,
            last_accessed=row[9] if len(row) > 9 else 0.0,
        )

    def xǁAgentMemoryǁ_row_to_entry__mutmut_37(self, row: tuple) -> MemoryEntry:
        """Convert a database row to a MemoryEntry."""
        embedding_str = row[5] if len(row) > 5 else ""
        embedding = [float(v) for v in embedding_str.split(",") if v] if embedding_str else []

        import json

        return MemoryEntry(
            entry_id=row[0],
            agent_id=row[1],
            content=row[2],
            entry_type=row[3],
            importance=row[4],
            embedding=embedding,
            metadata=json.loads(row[6]) if len(row) > 6 or row[6] else {},
            timestamp=row[7],
            access_count=row[8] if len(row) > 8 else 0,
            last_accessed=row[9] if len(row) > 9 else 0.0,
        )

    def xǁAgentMemoryǁ_row_to_entry__mutmut_38(self, row: tuple) -> MemoryEntry:
        """Convert a database row to a MemoryEntry."""
        embedding_str = row[5] if len(row) > 5 else ""
        embedding = [float(v) for v in embedding_str.split(",") if v] if embedding_str else []

        import json

        return MemoryEntry(
            entry_id=row[0],
            agent_id=row[1],
            content=row[2],
            entry_type=row[3],
            importance=row[4],
            embedding=embedding,
            metadata=json.loads(row[6]) if len(row) >= 6 and row[6] else {},
            timestamp=row[7],
            access_count=row[8] if len(row) > 8 else 0,
            last_accessed=row[9] if len(row) > 9 else 0.0,
        )

    def xǁAgentMemoryǁ_row_to_entry__mutmut_39(self, row: tuple) -> MemoryEntry:
        """Convert a database row to a MemoryEntry."""
        embedding_str = row[5] if len(row) > 5 else ""
        embedding = [float(v) for v in embedding_str.split(",") if v] if embedding_str else []

        import json

        return MemoryEntry(
            entry_id=row[0],
            agent_id=row[1],
            content=row[2],
            entry_type=row[3],
            importance=row[4],
            embedding=embedding,
            metadata=json.loads(row[6]) if len(row) > 7 and row[6] else {},
            timestamp=row[7],
            access_count=row[8] if len(row) > 8 else 0,
            last_accessed=row[9] if len(row) > 9 else 0.0,
        )

    def xǁAgentMemoryǁ_row_to_entry__mutmut_40(self, row: tuple) -> MemoryEntry:
        """Convert a database row to a MemoryEntry."""
        embedding_str = row[5] if len(row) > 5 else ""
        embedding = [float(v) for v in embedding_str.split(",") if v] if embedding_str else []

        import json

        return MemoryEntry(
            entry_id=row[0],
            agent_id=row[1],
            content=row[2],
            entry_type=row[3],
            importance=row[4],
            embedding=embedding,
            metadata=json.loads(row[6]) if len(row) > 6 and row[7] else {},
            timestamp=row[7],
            access_count=row[8] if len(row) > 8 else 0,
            last_accessed=row[9] if len(row) > 9 else 0.0,
        )

    def xǁAgentMemoryǁ_row_to_entry__mutmut_41(self, row: tuple) -> MemoryEntry:
        """Convert a database row to a MemoryEntry."""
        embedding_str = row[5] if len(row) > 5 else ""
        embedding = [float(v) for v in embedding_str.split(",") if v] if embedding_str else []

        import json

        return MemoryEntry(
            entry_id=row[0],
            agent_id=row[1],
            content=row[2],
            entry_type=row[3],
            importance=row[4],
            embedding=embedding,
            metadata=json.loads(row[6]) if len(row) > 6 and row[6] else {},
            timestamp=row[8],
            access_count=row[8] if len(row) > 8 else 0,
            last_accessed=row[9] if len(row) > 9 else 0.0,
        )

    def xǁAgentMemoryǁ_row_to_entry__mutmut_42(self, row: tuple) -> MemoryEntry:
        """Convert a database row to a MemoryEntry."""
        embedding_str = row[5] if len(row) > 5 else ""
        embedding = [float(v) for v in embedding_str.split(",") if v] if embedding_str else []

        import json

        return MemoryEntry(
            entry_id=row[0],
            agent_id=row[1],
            content=row[2],
            entry_type=row[3],
            importance=row[4],
            embedding=embedding,
            metadata=json.loads(row[6]) if len(row) > 6 and row[6] else {},
            timestamp=row[7],
            access_count=row[9] if len(row) > 8 else 0,
            last_accessed=row[9] if len(row) > 9 else 0.0,
        )

    def xǁAgentMemoryǁ_row_to_entry__mutmut_43(self, row: tuple) -> MemoryEntry:
        """Convert a database row to a MemoryEntry."""
        embedding_str = row[5] if len(row) > 5 else ""
        embedding = [float(v) for v in embedding_str.split(",") if v] if embedding_str else []

        import json

        return MemoryEntry(
            entry_id=row[0],
            agent_id=row[1],
            content=row[2],
            entry_type=row[3],
            importance=row[4],
            embedding=embedding,
            metadata=json.loads(row[6]) if len(row) > 6 and row[6] else {},
            timestamp=row[7],
            access_count=row[8] if len(row) >= 8 else 0,
            last_accessed=row[9] if len(row) > 9 else 0.0,
        )

    def xǁAgentMemoryǁ_row_to_entry__mutmut_44(self, row: tuple) -> MemoryEntry:
        """Convert a database row to a MemoryEntry."""
        embedding_str = row[5] if len(row) > 5 else ""
        embedding = [float(v) for v in embedding_str.split(",") if v] if embedding_str else []

        import json

        return MemoryEntry(
            entry_id=row[0],
            agent_id=row[1],
            content=row[2],
            entry_type=row[3],
            importance=row[4],
            embedding=embedding,
            metadata=json.loads(row[6]) if len(row) > 6 and row[6] else {},
            timestamp=row[7],
            access_count=row[8] if len(row) > 9 else 0,
            last_accessed=row[9] if len(row) > 9 else 0.0,
        )

    def xǁAgentMemoryǁ_row_to_entry__mutmut_45(self, row: tuple) -> MemoryEntry:
        """Convert a database row to a MemoryEntry."""
        embedding_str = row[5] if len(row) > 5 else ""
        embedding = [float(v) for v in embedding_str.split(",") if v] if embedding_str else []

        import json

        return MemoryEntry(
            entry_id=row[0],
            agent_id=row[1],
            content=row[2],
            entry_type=row[3],
            importance=row[4],
            embedding=embedding,
            metadata=json.loads(row[6]) if len(row) > 6 and row[6] else {},
            timestamp=row[7],
            access_count=row[8] if len(row) > 8 else 1,
            last_accessed=row[9] if len(row) > 9 else 0.0,
        )

    def xǁAgentMemoryǁ_row_to_entry__mutmut_46(self, row: tuple) -> MemoryEntry:
        """Convert a database row to a MemoryEntry."""
        embedding_str = row[5] if len(row) > 5 else ""
        embedding = [float(v) for v in embedding_str.split(",") if v] if embedding_str else []

        import json

        return MemoryEntry(
            entry_id=row[0],
            agent_id=row[1],
            content=row[2],
            entry_type=row[3],
            importance=row[4],
            embedding=embedding,
            metadata=json.loads(row[6]) if len(row) > 6 and row[6] else {},
            timestamp=row[7],
            access_count=row[8] if len(row) > 8 else 0,
            last_accessed=row[10] if len(row) > 9 else 0.0,
        )

    def xǁAgentMemoryǁ_row_to_entry__mutmut_47(self, row: tuple) -> MemoryEntry:
        """Convert a database row to a MemoryEntry."""
        embedding_str = row[5] if len(row) > 5 else ""
        embedding = [float(v) for v in embedding_str.split(",") if v] if embedding_str else []

        import json

        return MemoryEntry(
            entry_id=row[0],
            agent_id=row[1],
            content=row[2],
            entry_type=row[3],
            importance=row[4],
            embedding=embedding,
            metadata=json.loads(row[6]) if len(row) > 6 and row[6] else {},
            timestamp=row[7],
            access_count=row[8] if len(row) > 8 else 0,
            last_accessed=row[9] if len(row) >= 9 else 0.0,
        )

    def xǁAgentMemoryǁ_row_to_entry__mutmut_48(self, row: tuple) -> MemoryEntry:
        """Convert a database row to a MemoryEntry."""
        embedding_str = row[5] if len(row) > 5 else ""
        embedding = [float(v) for v in embedding_str.split(",") if v] if embedding_str else []

        import json

        return MemoryEntry(
            entry_id=row[0],
            agent_id=row[1],
            content=row[2],
            entry_type=row[3],
            importance=row[4],
            embedding=embedding,
            metadata=json.loads(row[6]) if len(row) > 6 and row[6] else {},
            timestamp=row[7],
            access_count=row[8] if len(row) > 8 else 0,
            last_accessed=row[9] if len(row) > 10 else 0.0,
        )

    def xǁAgentMemoryǁ_row_to_entry__mutmut_49(self, row: tuple) -> MemoryEntry:
        """Convert a database row to a MemoryEntry."""
        embedding_str = row[5] if len(row) > 5 else ""
        embedding = [float(v) for v in embedding_str.split(",") if v] if embedding_str else []

        import json

        return MemoryEntry(
            entry_id=row[0],
            agent_id=row[1],
            content=row[2],
            entry_type=row[3],
            importance=row[4],
            embedding=embedding,
            metadata=json.loads(row[6]) if len(row) > 6 and row[6] else {},
            timestamp=row[7],
            access_count=row[8] if len(row) > 8 else 0,
            last_accessed=row[9] if len(row) > 9 else 1.0,
        )

    # ── Consolidation ───────────────────────────────────────

    @_mutmut_mutated(mutants_xǁAgentMemoryǁconsolidate__mutmut)
    def consolidate(self, importance_threshold: float = 0.7) -> int:
        """Move important short-term memories to long-term with enhanced embedding.

        This simulates the cognitive process of memory consolidation during sleep.
        Only memories above the importance threshold are consolidated.

        Returns:
            Number of memories consolidated.
        """
        consolidated = 0
        with self._lock:
            for entry in self._short_term:
                if entry.importance >= importance_threshold:
                    # Boost importance slightly during consolidation
                    entry.importance = min(1.0, entry.importance * 1.1)
                    self._persist_entry(entry)
                    consolidated += 1

        if consolidated > 0:
            logger.info("Consolidated %d memories for agent %s", consolidated, self.agent_id)
        return consolidated

    # ── Consolidation ───────────────────────────────────────

    def xǁAgentMemoryǁconsolidate__mutmut_orig(self, importance_threshold: float = 0.7) -> int:
        """Move important short-term memories to long-term with enhanced embedding.

        This simulates the cognitive process of memory consolidation during sleep.
        Only memories above the importance threshold are consolidated.

        Returns:
            Number of memories consolidated.
        """
        consolidated = 0
        with self._lock:
            for entry in self._short_term:
                if entry.importance >= importance_threshold:
                    # Boost importance slightly during consolidation
                    entry.importance = min(1.0, entry.importance * 1.1)
                    self._persist_entry(entry)
                    consolidated += 1

        if consolidated > 0:
            logger.info("Consolidated %d memories for agent %s", consolidated, self.agent_id)
        return consolidated

    # ── Consolidation ───────────────────────────────────────

    def xǁAgentMemoryǁconsolidate__mutmut_1(self, importance_threshold: float = 1.7) -> int:
        """Move important short-term memories to long-term with enhanced embedding.

        This simulates the cognitive process of memory consolidation during sleep.
        Only memories above the importance threshold are consolidated.

        Returns:
            Number of memories consolidated.
        """
        consolidated = 0
        with self._lock:
            for entry in self._short_term:
                if entry.importance >= importance_threshold:
                    # Boost importance slightly during consolidation
                    entry.importance = min(1.0, entry.importance * 1.1)
                    self._persist_entry(entry)
                    consolidated += 1

        if consolidated > 0:
            logger.info("Consolidated %d memories for agent %s", consolidated, self.agent_id)
        return consolidated

    # ── Consolidation ───────────────────────────────────────

    def xǁAgentMemoryǁconsolidate__mutmut_2(self, importance_threshold: float = 0.7) -> int:
        """Move important short-term memories to long-term with enhanced embedding.

        This simulates the cognitive process of memory consolidation during sleep.
        Only memories above the importance threshold are consolidated.

        Returns:
            Number of memories consolidated.
        """
        consolidated = None
        with self._lock:
            for entry in self._short_term:
                if entry.importance >= importance_threshold:
                    # Boost importance slightly during consolidation
                    entry.importance = min(1.0, entry.importance * 1.1)
                    self._persist_entry(entry)
                    consolidated += 1

        if consolidated > 0:
            logger.info("Consolidated %d memories for agent %s", consolidated, self.agent_id)
        return consolidated

    # ── Consolidation ───────────────────────────────────────

    def xǁAgentMemoryǁconsolidate__mutmut_3(self, importance_threshold: float = 0.7) -> int:
        """Move important short-term memories to long-term with enhanced embedding.

        This simulates the cognitive process of memory consolidation during sleep.
        Only memories above the importance threshold are consolidated.

        Returns:
            Number of memories consolidated.
        """
        consolidated = 1
        with self._lock:
            for entry in self._short_term:
                if entry.importance >= importance_threshold:
                    # Boost importance slightly during consolidation
                    entry.importance = min(1.0, entry.importance * 1.1)
                    self._persist_entry(entry)
                    consolidated += 1

        if consolidated > 0:
            logger.info("Consolidated %d memories for agent %s", consolidated, self.agent_id)
        return consolidated

    # ── Consolidation ───────────────────────────────────────

    def xǁAgentMemoryǁconsolidate__mutmut_4(self, importance_threshold: float = 0.7) -> int:
        """Move important short-term memories to long-term with enhanced embedding.

        This simulates the cognitive process of memory consolidation during sleep.
        Only memories above the importance threshold are consolidated.

        Returns:
            Number of memories consolidated.
        """
        consolidated = 0
        with self._lock:
            for entry in self._short_term:
                if entry.importance > importance_threshold:
                    # Boost importance slightly during consolidation
                    entry.importance = min(1.0, entry.importance * 1.1)
                    self._persist_entry(entry)
                    consolidated += 1

        if consolidated > 0:
            logger.info("Consolidated %d memories for agent %s", consolidated, self.agent_id)
        return consolidated

    # ── Consolidation ───────────────────────────────────────

    def xǁAgentMemoryǁconsolidate__mutmut_5(self, importance_threshold: float = 0.7) -> int:
        """Move important short-term memories to long-term with enhanced embedding.

        This simulates the cognitive process of memory consolidation during sleep.
        Only memories above the importance threshold are consolidated.

        Returns:
            Number of memories consolidated.
        """
        consolidated = 0
        with self._lock:
            for entry in self._short_term:
                if entry.importance >= importance_threshold:
                    # Boost importance slightly during consolidation
                    entry.importance = None
                    self._persist_entry(entry)
                    consolidated += 1

        if consolidated > 0:
            logger.info("Consolidated %d memories for agent %s", consolidated, self.agent_id)
        return consolidated

    # ── Consolidation ───────────────────────────────────────

    def xǁAgentMemoryǁconsolidate__mutmut_6(self, importance_threshold: float = 0.7) -> int:
        """Move important short-term memories to long-term with enhanced embedding.

        This simulates the cognitive process of memory consolidation during sleep.
        Only memories above the importance threshold are consolidated.

        Returns:
            Number of memories consolidated.
        """
        consolidated = 0
        with self._lock:
            for entry in self._short_term:
                if entry.importance >= importance_threshold:
                    # Boost importance slightly during consolidation
                    entry.importance = min(None, entry.importance * 1.1)
                    self._persist_entry(entry)
                    consolidated += 1

        if consolidated > 0:
            logger.info("Consolidated %d memories for agent %s", consolidated, self.agent_id)
        return consolidated

    # ── Consolidation ───────────────────────────────────────

    def xǁAgentMemoryǁconsolidate__mutmut_7(self, importance_threshold: float = 0.7) -> int:
        """Move important short-term memories to long-term with enhanced embedding.

        This simulates the cognitive process of memory consolidation during sleep.
        Only memories above the importance threshold are consolidated.

        Returns:
            Number of memories consolidated.
        """
        consolidated = 0
        with self._lock:
            for entry in self._short_term:
                if entry.importance >= importance_threshold:
                    # Boost importance slightly during consolidation
                    entry.importance = min(1.0, None)
                    self._persist_entry(entry)
                    consolidated += 1

        if consolidated > 0:
            logger.info("Consolidated %d memories for agent %s", consolidated, self.agent_id)
        return consolidated

    # ── Consolidation ───────────────────────────────────────

    def xǁAgentMemoryǁconsolidate__mutmut_8(self, importance_threshold: float = 0.7) -> int:
        """Move important short-term memories to long-term with enhanced embedding.

        This simulates the cognitive process of memory consolidation during sleep.
        Only memories above the importance threshold are consolidated.

        Returns:
            Number of memories consolidated.
        """
        consolidated = 0
        with self._lock:
            for entry in self._short_term:
                if entry.importance >= importance_threshold:
                    # Boost importance slightly during consolidation
                    entry.importance = min(entry.importance * 1.1)
                    self._persist_entry(entry)
                    consolidated += 1

        if consolidated > 0:
            logger.info("Consolidated %d memories for agent %s", consolidated, self.agent_id)
        return consolidated

    # ── Consolidation ───────────────────────────────────────

    def xǁAgentMemoryǁconsolidate__mutmut_9(self, importance_threshold: float = 0.7) -> int:
        """Move important short-term memories to long-term with enhanced embedding.

        This simulates the cognitive process of memory consolidation during sleep.
        Only memories above the importance threshold are consolidated.

        Returns:
            Number of memories consolidated.
        """
        consolidated = 0
        with self._lock:
            for entry in self._short_term:
                if entry.importance >= importance_threshold:
                    # Boost importance slightly during consolidation
                    entry.importance = min(1.0, )
                    self._persist_entry(entry)
                    consolidated += 1

        if consolidated > 0:
            logger.info("Consolidated %d memories for agent %s", consolidated, self.agent_id)
        return consolidated

    # ── Consolidation ───────────────────────────────────────

    def xǁAgentMemoryǁconsolidate__mutmut_10(self, importance_threshold: float = 0.7) -> int:
        """Move important short-term memories to long-term with enhanced embedding.

        This simulates the cognitive process of memory consolidation during sleep.
        Only memories above the importance threshold are consolidated.

        Returns:
            Number of memories consolidated.
        """
        consolidated = 0
        with self._lock:
            for entry in self._short_term:
                if entry.importance >= importance_threshold:
                    # Boost importance slightly during consolidation
                    entry.importance = min(2.0, entry.importance * 1.1)
                    self._persist_entry(entry)
                    consolidated += 1

        if consolidated > 0:
            logger.info("Consolidated %d memories for agent %s", consolidated, self.agent_id)
        return consolidated

    # ── Consolidation ───────────────────────────────────────

    def xǁAgentMemoryǁconsolidate__mutmut_11(self, importance_threshold: float = 0.7) -> int:
        """Move important short-term memories to long-term with enhanced embedding.

        This simulates the cognitive process of memory consolidation during sleep.
        Only memories above the importance threshold are consolidated.

        Returns:
            Number of memories consolidated.
        """
        consolidated = 0
        with self._lock:
            for entry in self._short_term:
                if entry.importance >= importance_threshold:
                    # Boost importance slightly during consolidation
                    entry.importance = min(1.0, entry.importance / 1.1)
                    self._persist_entry(entry)
                    consolidated += 1

        if consolidated > 0:
            logger.info("Consolidated %d memories for agent %s", consolidated, self.agent_id)
        return consolidated

    # ── Consolidation ───────────────────────────────────────

    def xǁAgentMemoryǁconsolidate__mutmut_12(self, importance_threshold: float = 0.7) -> int:
        """Move important short-term memories to long-term with enhanced embedding.

        This simulates the cognitive process of memory consolidation during sleep.
        Only memories above the importance threshold are consolidated.

        Returns:
            Number of memories consolidated.
        """
        consolidated = 0
        with self._lock:
            for entry in self._short_term:
                if entry.importance >= importance_threshold:
                    # Boost importance slightly during consolidation
                    entry.importance = min(1.0, entry.importance * 2.1)
                    self._persist_entry(entry)
                    consolidated += 1

        if consolidated > 0:
            logger.info("Consolidated %d memories for agent %s", consolidated, self.agent_id)
        return consolidated

    # ── Consolidation ───────────────────────────────────────

    def xǁAgentMemoryǁconsolidate__mutmut_13(self, importance_threshold: float = 0.7) -> int:
        """Move important short-term memories to long-term with enhanced embedding.

        This simulates the cognitive process of memory consolidation during sleep.
        Only memories above the importance threshold are consolidated.

        Returns:
            Number of memories consolidated.
        """
        consolidated = 0
        with self._lock:
            for entry in self._short_term:
                if entry.importance >= importance_threshold:
                    # Boost importance slightly during consolidation
                    entry.importance = min(1.0, entry.importance * 1.1)
                    self._persist_entry(None)
                    consolidated += 1

        if consolidated > 0:
            logger.info("Consolidated %d memories for agent %s", consolidated, self.agent_id)
        return consolidated

    # ── Consolidation ───────────────────────────────────────

    def xǁAgentMemoryǁconsolidate__mutmut_14(self, importance_threshold: float = 0.7) -> int:
        """Move important short-term memories to long-term with enhanced embedding.

        This simulates the cognitive process of memory consolidation during sleep.
        Only memories above the importance threshold are consolidated.

        Returns:
            Number of memories consolidated.
        """
        consolidated = 0
        with self._lock:
            for entry in self._short_term:
                if entry.importance >= importance_threshold:
                    # Boost importance slightly during consolidation
                    entry.importance = min(1.0, entry.importance * 1.1)
                    self._persist_entry(entry)
                    consolidated = 1

        if consolidated > 0:
            logger.info("Consolidated %d memories for agent %s", consolidated, self.agent_id)
        return consolidated

    # ── Consolidation ───────────────────────────────────────

    def xǁAgentMemoryǁconsolidate__mutmut_15(self, importance_threshold: float = 0.7) -> int:
        """Move important short-term memories to long-term with enhanced embedding.

        This simulates the cognitive process of memory consolidation during sleep.
        Only memories above the importance threshold are consolidated.

        Returns:
            Number of memories consolidated.
        """
        consolidated = 0
        with self._lock:
            for entry in self._short_term:
                if entry.importance >= importance_threshold:
                    # Boost importance slightly during consolidation
                    entry.importance = min(1.0, entry.importance * 1.1)
                    self._persist_entry(entry)
                    consolidated -= 1

        if consolidated > 0:
            logger.info("Consolidated %d memories for agent %s", consolidated, self.agent_id)
        return consolidated

    # ── Consolidation ───────────────────────────────────────

    def xǁAgentMemoryǁconsolidate__mutmut_16(self, importance_threshold: float = 0.7) -> int:
        """Move important short-term memories to long-term with enhanced embedding.

        This simulates the cognitive process of memory consolidation during sleep.
        Only memories above the importance threshold are consolidated.

        Returns:
            Number of memories consolidated.
        """
        consolidated = 0
        with self._lock:
            for entry in self._short_term:
                if entry.importance >= importance_threshold:
                    # Boost importance slightly during consolidation
                    entry.importance = min(1.0, entry.importance * 1.1)
                    self._persist_entry(entry)
                    consolidated += 2

        if consolidated > 0:
            logger.info("Consolidated %d memories for agent %s", consolidated, self.agent_id)
        return consolidated

    # ── Consolidation ───────────────────────────────────────

    def xǁAgentMemoryǁconsolidate__mutmut_17(self, importance_threshold: float = 0.7) -> int:
        """Move important short-term memories to long-term with enhanced embedding.

        This simulates the cognitive process of memory consolidation during sleep.
        Only memories above the importance threshold are consolidated.

        Returns:
            Number of memories consolidated.
        """
        consolidated = 0
        with self._lock:
            for entry in self._short_term:
                if entry.importance >= importance_threshold:
                    # Boost importance slightly during consolidation
                    entry.importance = min(1.0, entry.importance * 1.1)
                    self._persist_entry(entry)
                    consolidated += 1

        if consolidated >= 0:
            logger.info("Consolidated %d memories for agent %s", consolidated, self.agent_id)
        return consolidated

    # ── Consolidation ───────────────────────────────────────

    def xǁAgentMemoryǁconsolidate__mutmut_18(self, importance_threshold: float = 0.7) -> int:
        """Move important short-term memories to long-term with enhanced embedding.

        This simulates the cognitive process of memory consolidation during sleep.
        Only memories above the importance threshold are consolidated.

        Returns:
            Number of memories consolidated.
        """
        consolidated = 0
        with self._lock:
            for entry in self._short_term:
                if entry.importance >= importance_threshold:
                    # Boost importance slightly during consolidation
                    entry.importance = min(1.0, entry.importance * 1.1)
                    self._persist_entry(entry)
                    consolidated += 1

        if consolidated > 1:
            logger.info("Consolidated %d memories for agent %s", consolidated, self.agent_id)
        return consolidated

    # ── Consolidation ───────────────────────────────────────

    def xǁAgentMemoryǁconsolidate__mutmut_19(self, importance_threshold: float = 0.7) -> int:
        """Move important short-term memories to long-term with enhanced embedding.

        This simulates the cognitive process of memory consolidation during sleep.
        Only memories above the importance threshold are consolidated.

        Returns:
            Number of memories consolidated.
        """
        consolidated = 0
        with self._lock:
            for entry in self._short_term:
                if entry.importance >= importance_threshold:
                    # Boost importance slightly during consolidation
                    entry.importance = min(1.0, entry.importance * 1.1)
                    self._persist_entry(entry)
                    consolidated += 1

        if consolidated > 0:
            logger.info(None, consolidated, self.agent_id)
        return consolidated

    # ── Consolidation ───────────────────────────────────────

    def xǁAgentMemoryǁconsolidate__mutmut_20(self, importance_threshold: float = 0.7) -> int:
        """Move important short-term memories to long-term with enhanced embedding.

        This simulates the cognitive process of memory consolidation during sleep.
        Only memories above the importance threshold are consolidated.

        Returns:
            Number of memories consolidated.
        """
        consolidated = 0
        with self._lock:
            for entry in self._short_term:
                if entry.importance >= importance_threshold:
                    # Boost importance slightly during consolidation
                    entry.importance = min(1.0, entry.importance * 1.1)
                    self._persist_entry(entry)
                    consolidated += 1

        if consolidated > 0:
            logger.info("Consolidated %d memories for agent %s", None, self.agent_id)
        return consolidated

    # ── Consolidation ───────────────────────────────────────

    def xǁAgentMemoryǁconsolidate__mutmut_21(self, importance_threshold: float = 0.7) -> int:
        """Move important short-term memories to long-term with enhanced embedding.

        This simulates the cognitive process of memory consolidation during sleep.
        Only memories above the importance threshold are consolidated.

        Returns:
            Number of memories consolidated.
        """
        consolidated = 0
        with self._lock:
            for entry in self._short_term:
                if entry.importance >= importance_threshold:
                    # Boost importance slightly during consolidation
                    entry.importance = min(1.0, entry.importance * 1.1)
                    self._persist_entry(entry)
                    consolidated += 1

        if consolidated > 0:
            logger.info("Consolidated %d memories for agent %s", consolidated, None)
        return consolidated

    # ── Consolidation ───────────────────────────────────────

    def xǁAgentMemoryǁconsolidate__mutmut_22(self, importance_threshold: float = 0.7) -> int:
        """Move important short-term memories to long-term with enhanced embedding.

        This simulates the cognitive process of memory consolidation during sleep.
        Only memories above the importance threshold are consolidated.

        Returns:
            Number of memories consolidated.
        """
        consolidated = 0
        with self._lock:
            for entry in self._short_term:
                if entry.importance >= importance_threshold:
                    # Boost importance slightly during consolidation
                    entry.importance = min(1.0, entry.importance * 1.1)
                    self._persist_entry(entry)
                    consolidated += 1

        if consolidated > 0:
            logger.info(consolidated, self.agent_id)
        return consolidated

    # ── Consolidation ───────────────────────────────────────

    def xǁAgentMemoryǁconsolidate__mutmut_23(self, importance_threshold: float = 0.7) -> int:
        """Move important short-term memories to long-term with enhanced embedding.

        This simulates the cognitive process of memory consolidation during sleep.
        Only memories above the importance threshold are consolidated.

        Returns:
            Number of memories consolidated.
        """
        consolidated = 0
        with self._lock:
            for entry in self._short_term:
                if entry.importance >= importance_threshold:
                    # Boost importance slightly during consolidation
                    entry.importance = min(1.0, entry.importance * 1.1)
                    self._persist_entry(entry)
                    consolidated += 1

        if consolidated > 0:
            logger.info("Consolidated %d memories for agent %s", self.agent_id)
        return consolidated

    # ── Consolidation ───────────────────────────────────────

    def xǁAgentMemoryǁconsolidate__mutmut_24(self, importance_threshold: float = 0.7) -> int:
        """Move important short-term memories to long-term with enhanced embedding.

        This simulates the cognitive process of memory consolidation during sleep.
        Only memories above the importance threshold are consolidated.

        Returns:
            Number of memories consolidated.
        """
        consolidated = 0
        with self._lock:
            for entry in self._short_term:
                if entry.importance >= importance_threshold:
                    # Boost importance slightly during consolidation
                    entry.importance = min(1.0, entry.importance * 1.1)
                    self._persist_entry(entry)
                    consolidated += 1

        if consolidated > 0:
            logger.info("Consolidated %d memories for agent %s", consolidated, )
        return consolidated

    # ── Consolidation ───────────────────────────────────────

    def xǁAgentMemoryǁconsolidate__mutmut_25(self, importance_threshold: float = 0.7) -> int:
        """Move important short-term memories to long-term with enhanced embedding.

        This simulates the cognitive process of memory consolidation during sleep.
        Only memories above the importance threshold are consolidated.

        Returns:
            Number of memories consolidated.
        """
        consolidated = 0
        with self._lock:
            for entry in self._short_term:
                if entry.importance >= importance_threshold:
                    # Boost importance slightly during consolidation
                    entry.importance = min(1.0, entry.importance * 1.1)
                    self._persist_entry(entry)
                    consolidated += 1

        if consolidated > 0:
            logger.info("XXConsolidated %d memories for agent %sXX", consolidated, self.agent_id)
        return consolidated

    # ── Consolidation ───────────────────────────────────────

    def xǁAgentMemoryǁconsolidate__mutmut_26(self, importance_threshold: float = 0.7) -> int:
        """Move important short-term memories to long-term with enhanced embedding.

        This simulates the cognitive process of memory consolidation during sleep.
        Only memories above the importance threshold are consolidated.

        Returns:
            Number of memories consolidated.
        """
        consolidated = 0
        with self._lock:
            for entry in self._short_term:
                if entry.importance >= importance_threshold:
                    # Boost importance slightly during consolidation
                    entry.importance = min(1.0, entry.importance * 1.1)
                    self._persist_entry(entry)
                    consolidated += 1

        if consolidated > 0:
            logger.info("consolidated %d memories for agent %s", consolidated, self.agent_id)
        return consolidated

    # ── Consolidation ───────────────────────────────────────

    def xǁAgentMemoryǁconsolidate__mutmut_27(self, importance_threshold: float = 0.7) -> int:
        """Move important short-term memories to long-term with enhanced embedding.

        This simulates the cognitive process of memory consolidation during sleep.
        Only memories above the importance threshold are consolidated.

        Returns:
            Number of memories consolidated.
        """
        consolidated = 0
        with self._lock:
            for entry in self._short_term:
                if entry.importance >= importance_threshold:
                    # Boost importance slightly during consolidation
                    entry.importance = min(1.0, entry.importance * 1.1)
                    self._persist_entry(entry)
                    consolidated += 1

        if consolidated > 0:
            logger.info("CONSOLIDATED %D MEMORIES FOR AGENT %S", consolidated, self.agent_id)
        return consolidated

    # ── Management ──────────────────────────────────────────

    @_mutmut_mutated(mutants_xǁAgentMemoryǁforget__mutmut)
    def forget(self, entry_id: str) -> bool:
        """Remove a specific memory entry.

        Returns:
            True if the entry was found and removed.
        """
        with self._lock:
            # Remove from short-term
            self._short_term = [e for e in self._short_term if e.entry_id != entry_id]

            # Remove from long-term
            if self._conn is not None:
                self._conn.execute(
                    "DELETE FROM agent_memory WHERE entry_id = ? AND agent_id = ?",
                    (entry_id, self.agent_id),
                )
                self._conn.commit()
        return True

    # ── Management ──────────────────────────────────────────

    def xǁAgentMemoryǁforget__mutmut_orig(self, entry_id: str) -> bool:
        """Remove a specific memory entry.

        Returns:
            True if the entry was found and removed.
        """
        with self._lock:
            # Remove from short-term
            self._short_term = [e for e in self._short_term if e.entry_id != entry_id]

            # Remove from long-term
            if self._conn is not None:
                self._conn.execute(
                    "DELETE FROM agent_memory WHERE entry_id = ? AND agent_id = ?",
                    (entry_id, self.agent_id),
                )
                self._conn.commit()
        return True

    # ── Management ──────────────────────────────────────────

    def xǁAgentMemoryǁforget__mutmut_1(self, entry_id: str) -> bool:
        """Remove a specific memory entry.

        Returns:
            True if the entry was found and removed.
        """
        with self._lock:
            # Remove from short-term
            self._short_term = None

            # Remove from long-term
            if self._conn is not None:
                self._conn.execute(
                    "DELETE FROM agent_memory WHERE entry_id = ? AND agent_id = ?",
                    (entry_id, self.agent_id),
                )
                self._conn.commit()
        return True

    # ── Management ──────────────────────────────────────────

    def xǁAgentMemoryǁforget__mutmut_2(self, entry_id: str) -> bool:
        """Remove a specific memory entry.

        Returns:
            True if the entry was found and removed.
        """
        with self._lock:
            # Remove from short-term
            self._short_term = [e for e in self._short_term if e.entry_id == entry_id]

            # Remove from long-term
            if self._conn is not None:
                self._conn.execute(
                    "DELETE FROM agent_memory WHERE entry_id = ? AND agent_id = ?",
                    (entry_id, self.agent_id),
                )
                self._conn.commit()
        return True

    # ── Management ──────────────────────────────────────────

    def xǁAgentMemoryǁforget__mutmut_3(self, entry_id: str) -> bool:
        """Remove a specific memory entry.

        Returns:
            True if the entry was found and removed.
        """
        with self._lock:
            # Remove from short-term
            self._short_term = [e for e in self._short_term if e.entry_id != entry_id]

            # Remove from long-term
            if self._conn is None:
                self._conn.execute(
                    "DELETE FROM agent_memory WHERE entry_id = ? AND agent_id = ?",
                    (entry_id, self.agent_id),
                )
                self._conn.commit()
        return True

    # ── Management ──────────────────────────────────────────

    def xǁAgentMemoryǁforget__mutmut_4(self, entry_id: str) -> bool:
        """Remove a specific memory entry.

        Returns:
            True if the entry was found and removed.
        """
        with self._lock:
            # Remove from short-term
            self._short_term = [e for e in self._short_term if e.entry_id != entry_id]

            # Remove from long-term
            if self._conn is not None:
                self._conn.execute(
                    None,
                    (entry_id, self.agent_id),
                )
                self._conn.commit()
        return True

    # ── Management ──────────────────────────────────────────

    def xǁAgentMemoryǁforget__mutmut_5(self, entry_id: str) -> bool:
        """Remove a specific memory entry.

        Returns:
            True if the entry was found and removed.
        """
        with self._lock:
            # Remove from short-term
            self._short_term = [e for e in self._short_term if e.entry_id != entry_id]

            # Remove from long-term
            if self._conn is not None:
                self._conn.execute(
                    "DELETE FROM agent_memory WHERE entry_id = ? AND agent_id = ?",
                    None,
                )
                self._conn.commit()
        return True

    # ── Management ──────────────────────────────────────────

    def xǁAgentMemoryǁforget__mutmut_6(self, entry_id: str) -> bool:
        """Remove a specific memory entry.

        Returns:
            True if the entry was found and removed.
        """
        with self._lock:
            # Remove from short-term
            self._short_term = [e for e in self._short_term if e.entry_id != entry_id]

            # Remove from long-term
            if self._conn is not None:
                self._conn.execute(
                    (entry_id, self.agent_id),
                )
                self._conn.commit()
        return True

    # ── Management ──────────────────────────────────────────

    def xǁAgentMemoryǁforget__mutmut_7(self, entry_id: str) -> bool:
        """Remove a specific memory entry.

        Returns:
            True if the entry was found and removed.
        """
        with self._lock:
            # Remove from short-term
            self._short_term = [e for e in self._short_term if e.entry_id != entry_id]

            # Remove from long-term
            if self._conn is not None:
                self._conn.execute(
                    "DELETE FROM agent_memory WHERE entry_id = ? AND agent_id = ?",
                    )
                self._conn.commit()
        return True

    # ── Management ──────────────────────────────────────────

    def xǁAgentMemoryǁforget__mutmut_8(self, entry_id: str) -> bool:
        """Remove a specific memory entry.

        Returns:
            True if the entry was found and removed.
        """
        with self._lock:
            # Remove from short-term
            self._short_term = [e for e in self._short_term if e.entry_id != entry_id]

            # Remove from long-term
            if self._conn is not None:
                self._conn.execute(
                    "XXDELETE FROM agent_memory WHERE entry_id = ? AND agent_id = ?XX",
                    (entry_id, self.agent_id),
                )
                self._conn.commit()
        return True

    # ── Management ──────────────────────────────────────────

    def xǁAgentMemoryǁforget__mutmut_9(self, entry_id: str) -> bool:
        """Remove a specific memory entry.

        Returns:
            True if the entry was found and removed.
        """
        with self._lock:
            # Remove from short-term
            self._short_term = [e for e in self._short_term if e.entry_id != entry_id]

            # Remove from long-term
            if self._conn is not None:
                self._conn.execute(
                    "delete from agent_memory where entry_id = ? and agent_id = ?",
                    (entry_id, self.agent_id),
                )
                self._conn.commit()
        return True

    # ── Management ──────────────────────────────────────────

    def xǁAgentMemoryǁforget__mutmut_10(self, entry_id: str) -> bool:
        """Remove a specific memory entry.

        Returns:
            True if the entry was found and removed.
        """
        with self._lock:
            # Remove from short-term
            self._short_term = [e for e in self._short_term if e.entry_id != entry_id]

            # Remove from long-term
            if self._conn is not None:
                self._conn.execute(
                    "DELETE FROM AGENT_MEMORY WHERE ENTRY_ID = ? AND AGENT_ID = ?",
                    (entry_id, self.agent_id),
                )
                self._conn.commit()
        return True

    # ── Management ──────────────────────────────────────────

    def xǁAgentMemoryǁforget__mutmut_11(self, entry_id: str) -> bool:
        """Remove a specific memory entry.

        Returns:
            True if the entry was found and removed.
        """
        with self._lock:
            # Remove from short-term
            self._short_term = [e for e in self._short_term if e.entry_id != entry_id]

            # Remove from long-term
            if self._conn is not None:
                self._conn.execute(
                    "DELETE FROM agent_memory WHERE entry_id = ? AND agent_id = ?",
                    (entry_id, self.agent_id),
                )
                self._conn.commit()
        return False

    @_mutmut_mutated(mutants_xǁAgentMemoryǁclear__mutmut)
    def clear(self, entry_type: str | None = None) -> int:
        """Clear memories, optionally filtered by type.

        Returns:
            Number of entries cleared.
        """
        with self._lock:
            if entry_type:
                count = sum(1 for e in self._short_term if e.entry_type == entry_type)
                self._short_term = [e for e in self._short_term if e.entry_type != entry_type]
            else:
                count = len(self._short_term)
                self._short_term = []

            if self._conn is not None:
                if entry_type:
                    self._conn.execute(
                        "DELETE FROM agent_memory WHERE agent_id = ? AND entry_type = ?",
                        (self.agent_id, entry_type),
                    )
                else:
                    self._conn.execute(
                        "DELETE FROM agent_memory WHERE agent_id = ?",
                        (self.agent_id,),
                    )
                self._conn.commit()

        return count

    def xǁAgentMemoryǁclear__mutmut_orig(self, entry_type: str | None = None) -> int:
        """Clear memories, optionally filtered by type.

        Returns:
            Number of entries cleared.
        """
        with self._lock:
            if entry_type:
                count = sum(1 for e in self._short_term if e.entry_type == entry_type)
                self._short_term = [e for e in self._short_term if e.entry_type != entry_type]
            else:
                count = len(self._short_term)
                self._short_term = []

            if self._conn is not None:
                if entry_type:
                    self._conn.execute(
                        "DELETE FROM agent_memory WHERE agent_id = ? AND entry_type = ?",
                        (self.agent_id, entry_type),
                    )
                else:
                    self._conn.execute(
                        "DELETE FROM agent_memory WHERE agent_id = ?",
                        (self.agent_id,),
                    )
                self._conn.commit()

        return count

    def xǁAgentMemoryǁclear__mutmut_1(self, entry_type: str | None = None) -> int:
        """Clear memories, optionally filtered by type.

        Returns:
            Number of entries cleared.
        """
        with self._lock:
            if entry_type:
                count = None
                self._short_term = [e for e in self._short_term if e.entry_type != entry_type]
            else:
                count = len(self._short_term)
                self._short_term = []

            if self._conn is not None:
                if entry_type:
                    self._conn.execute(
                        "DELETE FROM agent_memory WHERE agent_id = ? AND entry_type = ?",
                        (self.agent_id, entry_type),
                    )
                else:
                    self._conn.execute(
                        "DELETE FROM agent_memory WHERE agent_id = ?",
                        (self.agent_id,),
                    )
                self._conn.commit()

        return count

    def xǁAgentMemoryǁclear__mutmut_2(self, entry_type: str | None = None) -> int:
        """Clear memories, optionally filtered by type.

        Returns:
            Number of entries cleared.
        """
        with self._lock:
            if entry_type:
                count = sum(None)
                self._short_term = [e for e in self._short_term if e.entry_type != entry_type]
            else:
                count = len(self._short_term)
                self._short_term = []

            if self._conn is not None:
                if entry_type:
                    self._conn.execute(
                        "DELETE FROM agent_memory WHERE agent_id = ? AND entry_type = ?",
                        (self.agent_id, entry_type),
                    )
                else:
                    self._conn.execute(
                        "DELETE FROM agent_memory WHERE agent_id = ?",
                        (self.agent_id,),
                    )
                self._conn.commit()

        return count

    def xǁAgentMemoryǁclear__mutmut_3(self, entry_type: str | None = None) -> int:
        """Clear memories, optionally filtered by type.

        Returns:
            Number of entries cleared.
        """
        with self._lock:
            if entry_type:
                count = sum(2 for e in self._short_term if e.entry_type == entry_type)
                self._short_term = [e for e in self._short_term if e.entry_type != entry_type]
            else:
                count = len(self._short_term)
                self._short_term = []

            if self._conn is not None:
                if entry_type:
                    self._conn.execute(
                        "DELETE FROM agent_memory WHERE agent_id = ? AND entry_type = ?",
                        (self.agent_id, entry_type),
                    )
                else:
                    self._conn.execute(
                        "DELETE FROM agent_memory WHERE agent_id = ?",
                        (self.agent_id,),
                    )
                self._conn.commit()

        return count

    def xǁAgentMemoryǁclear__mutmut_4(self, entry_type: str | None = None) -> int:
        """Clear memories, optionally filtered by type.

        Returns:
            Number of entries cleared.
        """
        with self._lock:
            if entry_type:
                count = sum(1 for e in self._short_term if e.entry_type != entry_type)
                self._short_term = [e for e in self._short_term if e.entry_type != entry_type]
            else:
                count = len(self._short_term)
                self._short_term = []

            if self._conn is not None:
                if entry_type:
                    self._conn.execute(
                        "DELETE FROM agent_memory WHERE agent_id = ? AND entry_type = ?",
                        (self.agent_id, entry_type),
                    )
                else:
                    self._conn.execute(
                        "DELETE FROM agent_memory WHERE agent_id = ?",
                        (self.agent_id,),
                    )
                self._conn.commit()

        return count

    def xǁAgentMemoryǁclear__mutmut_5(self, entry_type: str | None = None) -> int:
        """Clear memories, optionally filtered by type.

        Returns:
            Number of entries cleared.
        """
        with self._lock:
            if entry_type:
                count = sum(1 for e in self._short_term if e.entry_type == entry_type)
                self._short_term = None
            else:
                count = len(self._short_term)
                self._short_term = []

            if self._conn is not None:
                if entry_type:
                    self._conn.execute(
                        "DELETE FROM agent_memory WHERE agent_id = ? AND entry_type = ?",
                        (self.agent_id, entry_type),
                    )
                else:
                    self._conn.execute(
                        "DELETE FROM agent_memory WHERE agent_id = ?",
                        (self.agent_id,),
                    )
                self._conn.commit()

        return count

    def xǁAgentMemoryǁclear__mutmut_6(self, entry_type: str | None = None) -> int:
        """Clear memories, optionally filtered by type.

        Returns:
            Number of entries cleared.
        """
        with self._lock:
            if entry_type:
                count = sum(1 for e in self._short_term if e.entry_type == entry_type)
                self._short_term = [e for e in self._short_term if e.entry_type == entry_type]
            else:
                count = len(self._short_term)
                self._short_term = []

            if self._conn is not None:
                if entry_type:
                    self._conn.execute(
                        "DELETE FROM agent_memory WHERE agent_id = ? AND entry_type = ?",
                        (self.agent_id, entry_type),
                    )
                else:
                    self._conn.execute(
                        "DELETE FROM agent_memory WHERE agent_id = ?",
                        (self.agent_id,),
                    )
                self._conn.commit()

        return count

    def xǁAgentMemoryǁclear__mutmut_7(self, entry_type: str | None = None) -> int:
        """Clear memories, optionally filtered by type.

        Returns:
            Number of entries cleared.
        """
        with self._lock:
            if entry_type:
                count = sum(1 for e in self._short_term if e.entry_type == entry_type)
                self._short_term = [e for e in self._short_term if e.entry_type != entry_type]
            else:
                count = None
                self._short_term = []

            if self._conn is not None:
                if entry_type:
                    self._conn.execute(
                        "DELETE FROM agent_memory WHERE agent_id = ? AND entry_type = ?",
                        (self.agent_id, entry_type),
                    )
                else:
                    self._conn.execute(
                        "DELETE FROM agent_memory WHERE agent_id = ?",
                        (self.agent_id,),
                    )
                self._conn.commit()

        return count

    def xǁAgentMemoryǁclear__mutmut_8(self, entry_type: str | None = None) -> int:
        """Clear memories, optionally filtered by type.

        Returns:
            Number of entries cleared.
        """
        with self._lock:
            if entry_type:
                count = sum(1 for e in self._short_term if e.entry_type == entry_type)
                self._short_term = [e for e in self._short_term if e.entry_type != entry_type]
            else:
                count = len(self._short_term)
                self._short_term = None

            if self._conn is not None:
                if entry_type:
                    self._conn.execute(
                        "DELETE FROM agent_memory WHERE agent_id = ? AND entry_type = ?",
                        (self.agent_id, entry_type),
                    )
                else:
                    self._conn.execute(
                        "DELETE FROM agent_memory WHERE agent_id = ?",
                        (self.agent_id,),
                    )
                self._conn.commit()

        return count

    def xǁAgentMemoryǁclear__mutmut_9(self, entry_type: str | None = None) -> int:
        """Clear memories, optionally filtered by type.

        Returns:
            Number of entries cleared.
        """
        with self._lock:
            if entry_type:
                count = sum(1 for e in self._short_term if e.entry_type == entry_type)
                self._short_term = [e for e in self._short_term if e.entry_type != entry_type]
            else:
                count = len(self._short_term)
                self._short_term = []

            if self._conn is None:
                if entry_type:
                    self._conn.execute(
                        "DELETE FROM agent_memory WHERE agent_id = ? AND entry_type = ?",
                        (self.agent_id, entry_type),
                    )
                else:
                    self._conn.execute(
                        "DELETE FROM agent_memory WHERE agent_id = ?",
                        (self.agent_id,),
                    )
                self._conn.commit()

        return count

    def xǁAgentMemoryǁclear__mutmut_10(self, entry_type: str | None = None) -> int:
        """Clear memories, optionally filtered by type.

        Returns:
            Number of entries cleared.
        """
        with self._lock:
            if entry_type:
                count = sum(1 for e in self._short_term if e.entry_type == entry_type)
                self._short_term = [e for e in self._short_term if e.entry_type != entry_type]
            else:
                count = len(self._short_term)
                self._short_term = []

            if self._conn is not None:
                if entry_type:
                    self._conn.execute(
                        None,
                        (self.agent_id, entry_type),
                    )
                else:
                    self._conn.execute(
                        "DELETE FROM agent_memory WHERE agent_id = ?",
                        (self.agent_id,),
                    )
                self._conn.commit()

        return count

    def xǁAgentMemoryǁclear__mutmut_11(self, entry_type: str | None = None) -> int:
        """Clear memories, optionally filtered by type.

        Returns:
            Number of entries cleared.
        """
        with self._lock:
            if entry_type:
                count = sum(1 for e in self._short_term if e.entry_type == entry_type)
                self._short_term = [e for e in self._short_term if e.entry_type != entry_type]
            else:
                count = len(self._short_term)
                self._short_term = []

            if self._conn is not None:
                if entry_type:
                    self._conn.execute(
                        "DELETE FROM agent_memory WHERE agent_id = ? AND entry_type = ?",
                        None,
                    )
                else:
                    self._conn.execute(
                        "DELETE FROM agent_memory WHERE agent_id = ?",
                        (self.agent_id,),
                    )
                self._conn.commit()

        return count

    def xǁAgentMemoryǁclear__mutmut_12(self, entry_type: str | None = None) -> int:
        """Clear memories, optionally filtered by type.

        Returns:
            Number of entries cleared.
        """
        with self._lock:
            if entry_type:
                count = sum(1 for e in self._short_term if e.entry_type == entry_type)
                self._short_term = [e for e in self._short_term if e.entry_type != entry_type]
            else:
                count = len(self._short_term)
                self._short_term = []

            if self._conn is not None:
                if entry_type:
                    self._conn.execute(
                        (self.agent_id, entry_type),
                    )
                else:
                    self._conn.execute(
                        "DELETE FROM agent_memory WHERE agent_id = ?",
                        (self.agent_id,),
                    )
                self._conn.commit()

        return count

    def xǁAgentMemoryǁclear__mutmut_13(self, entry_type: str | None = None) -> int:
        """Clear memories, optionally filtered by type.

        Returns:
            Number of entries cleared.
        """
        with self._lock:
            if entry_type:
                count = sum(1 for e in self._short_term if e.entry_type == entry_type)
                self._short_term = [e for e in self._short_term if e.entry_type != entry_type]
            else:
                count = len(self._short_term)
                self._short_term = []

            if self._conn is not None:
                if entry_type:
                    self._conn.execute(
                        "DELETE FROM agent_memory WHERE agent_id = ? AND entry_type = ?",
                        )
                else:
                    self._conn.execute(
                        "DELETE FROM agent_memory WHERE agent_id = ?",
                        (self.agent_id,),
                    )
                self._conn.commit()

        return count

    def xǁAgentMemoryǁclear__mutmut_14(self, entry_type: str | None = None) -> int:
        """Clear memories, optionally filtered by type.

        Returns:
            Number of entries cleared.
        """
        with self._lock:
            if entry_type:
                count = sum(1 for e in self._short_term if e.entry_type == entry_type)
                self._short_term = [e for e in self._short_term if e.entry_type != entry_type]
            else:
                count = len(self._short_term)
                self._short_term = []

            if self._conn is not None:
                if entry_type:
                    self._conn.execute(
                        "XXDELETE FROM agent_memory WHERE agent_id = ? AND entry_type = ?XX",
                        (self.agent_id, entry_type),
                    )
                else:
                    self._conn.execute(
                        "DELETE FROM agent_memory WHERE agent_id = ?",
                        (self.agent_id,),
                    )
                self._conn.commit()

        return count

    def xǁAgentMemoryǁclear__mutmut_15(self, entry_type: str | None = None) -> int:
        """Clear memories, optionally filtered by type.

        Returns:
            Number of entries cleared.
        """
        with self._lock:
            if entry_type:
                count = sum(1 for e in self._short_term if e.entry_type == entry_type)
                self._short_term = [e for e in self._short_term if e.entry_type != entry_type]
            else:
                count = len(self._short_term)
                self._short_term = []

            if self._conn is not None:
                if entry_type:
                    self._conn.execute(
                        "delete from agent_memory where agent_id = ? and entry_type = ?",
                        (self.agent_id, entry_type),
                    )
                else:
                    self._conn.execute(
                        "DELETE FROM agent_memory WHERE agent_id = ?",
                        (self.agent_id,),
                    )
                self._conn.commit()

        return count

    def xǁAgentMemoryǁclear__mutmut_16(self, entry_type: str | None = None) -> int:
        """Clear memories, optionally filtered by type.

        Returns:
            Number of entries cleared.
        """
        with self._lock:
            if entry_type:
                count = sum(1 for e in self._short_term if e.entry_type == entry_type)
                self._short_term = [e for e in self._short_term if e.entry_type != entry_type]
            else:
                count = len(self._short_term)
                self._short_term = []

            if self._conn is not None:
                if entry_type:
                    self._conn.execute(
                        "DELETE FROM AGENT_MEMORY WHERE AGENT_ID = ? AND ENTRY_TYPE = ?",
                        (self.agent_id, entry_type),
                    )
                else:
                    self._conn.execute(
                        "DELETE FROM agent_memory WHERE agent_id = ?",
                        (self.agent_id,),
                    )
                self._conn.commit()

        return count

    def xǁAgentMemoryǁclear__mutmut_17(self, entry_type: str | None = None) -> int:
        """Clear memories, optionally filtered by type.

        Returns:
            Number of entries cleared.
        """
        with self._lock:
            if entry_type:
                count = sum(1 for e in self._short_term if e.entry_type == entry_type)
                self._short_term = [e for e in self._short_term if e.entry_type != entry_type]
            else:
                count = len(self._short_term)
                self._short_term = []

            if self._conn is not None:
                if entry_type:
                    self._conn.execute(
                        "DELETE FROM agent_memory WHERE agent_id = ? AND entry_type = ?",
                        (self.agent_id, entry_type),
                    )
                else:
                    self._conn.execute(
                        None,
                        (self.agent_id,),
                    )
                self._conn.commit()

        return count

    def xǁAgentMemoryǁclear__mutmut_18(self, entry_type: str | None = None) -> int:
        """Clear memories, optionally filtered by type.

        Returns:
            Number of entries cleared.
        """
        with self._lock:
            if entry_type:
                count = sum(1 for e in self._short_term if e.entry_type == entry_type)
                self._short_term = [e for e in self._short_term if e.entry_type != entry_type]
            else:
                count = len(self._short_term)
                self._short_term = []

            if self._conn is not None:
                if entry_type:
                    self._conn.execute(
                        "DELETE FROM agent_memory WHERE agent_id = ? AND entry_type = ?",
                        (self.agent_id, entry_type),
                    )
                else:
                    self._conn.execute(
                        "DELETE FROM agent_memory WHERE agent_id = ?",
                        None,
                    )
                self._conn.commit()

        return count

    def xǁAgentMemoryǁclear__mutmut_19(self, entry_type: str | None = None) -> int:
        """Clear memories, optionally filtered by type.

        Returns:
            Number of entries cleared.
        """
        with self._lock:
            if entry_type:
                count = sum(1 for e in self._short_term if e.entry_type == entry_type)
                self._short_term = [e for e in self._short_term if e.entry_type != entry_type]
            else:
                count = len(self._short_term)
                self._short_term = []

            if self._conn is not None:
                if entry_type:
                    self._conn.execute(
                        "DELETE FROM agent_memory WHERE agent_id = ? AND entry_type = ?",
                        (self.agent_id, entry_type),
                    )
                else:
                    self._conn.execute(
                        (self.agent_id,),
                    )
                self._conn.commit()

        return count

    def xǁAgentMemoryǁclear__mutmut_20(self, entry_type: str | None = None) -> int:
        """Clear memories, optionally filtered by type.

        Returns:
            Number of entries cleared.
        """
        with self._lock:
            if entry_type:
                count = sum(1 for e in self._short_term if e.entry_type == entry_type)
                self._short_term = [e for e in self._short_term if e.entry_type != entry_type]
            else:
                count = len(self._short_term)
                self._short_term = []

            if self._conn is not None:
                if entry_type:
                    self._conn.execute(
                        "DELETE FROM agent_memory WHERE agent_id = ? AND entry_type = ?",
                        (self.agent_id, entry_type),
                    )
                else:
                    self._conn.execute(
                        "DELETE FROM agent_memory WHERE agent_id = ?",
                        )
                self._conn.commit()

        return count

    def xǁAgentMemoryǁclear__mutmut_21(self, entry_type: str | None = None) -> int:
        """Clear memories, optionally filtered by type.

        Returns:
            Number of entries cleared.
        """
        with self._lock:
            if entry_type:
                count = sum(1 for e in self._short_term if e.entry_type == entry_type)
                self._short_term = [e for e in self._short_term if e.entry_type != entry_type]
            else:
                count = len(self._short_term)
                self._short_term = []

            if self._conn is not None:
                if entry_type:
                    self._conn.execute(
                        "DELETE FROM agent_memory WHERE agent_id = ? AND entry_type = ?",
                        (self.agent_id, entry_type),
                    )
                else:
                    self._conn.execute(
                        "XXDELETE FROM agent_memory WHERE agent_id = ?XX",
                        (self.agent_id,),
                    )
                self._conn.commit()

        return count

    def xǁAgentMemoryǁclear__mutmut_22(self, entry_type: str | None = None) -> int:
        """Clear memories, optionally filtered by type.

        Returns:
            Number of entries cleared.
        """
        with self._lock:
            if entry_type:
                count = sum(1 for e in self._short_term if e.entry_type == entry_type)
                self._short_term = [e for e in self._short_term if e.entry_type != entry_type]
            else:
                count = len(self._short_term)
                self._short_term = []

            if self._conn is not None:
                if entry_type:
                    self._conn.execute(
                        "DELETE FROM agent_memory WHERE agent_id = ? AND entry_type = ?",
                        (self.agent_id, entry_type),
                    )
                else:
                    self._conn.execute(
                        "delete from agent_memory where agent_id = ?",
                        (self.agent_id,),
                    )
                self._conn.commit()

        return count

    def xǁAgentMemoryǁclear__mutmut_23(self, entry_type: str | None = None) -> int:
        """Clear memories, optionally filtered by type.

        Returns:
            Number of entries cleared.
        """
        with self._lock:
            if entry_type:
                count = sum(1 for e in self._short_term if e.entry_type == entry_type)
                self._short_term = [e for e in self._short_term if e.entry_type != entry_type]
            else:
                count = len(self._short_term)
                self._short_term = []

            if self._conn is not None:
                if entry_type:
                    self._conn.execute(
                        "DELETE FROM agent_memory WHERE agent_id = ? AND entry_type = ?",
                        (self.agent_id, entry_type),
                    )
                else:
                    self._conn.execute(
                        "DELETE FROM AGENT_MEMORY WHERE AGENT_ID = ?",
                        (self.agent_id,),
                    )
                self._conn.commit()

        return count

    @_mutmut_mutated(mutants_xǁAgentMemoryǁget_stats__mutmut)
    def get_stats(self) -> dict[str, Any]:
        """Get memory statistics."""
        with self._lock:
            short_term_count = len(self._short_term)
            type_counts: dict[str, int] = {}
            for entry in self._short_term:
                type_counts[entry.entry_type] = type_counts.get(entry.entry_type, 0) + 1

        long_term_count = 0
        if self._conn is not None:
            cursor = self._conn.execute(
                "SELECT COUNT(*) FROM agent_memory WHERE agent_id = ?",
                (self.agent_id,),
            )
            long_term_count = cursor.fetchone()[0]

        return {
            "agent_id": self.agent_id,
            "short_term_count": short_term_count,
            "long_term_count": long_term_count,
            "type_counts": type_counts,
            "short_term_limit": self._short_term_limit,
        }

    def xǁAgentMemoryǁget_stats__mutmut_orig(self) -> dict[str, Any]:
        """Get memory statistics."""
        with self._lock:
            short_term_count = len(self._short_term)
            type_counts: dict[str, int] = {}
            for entry in self._short_term:
                type_counts[entry.entry_type] = type_counts.get(entry.entry_type, 0) + 1

        long_term_count = 0
        if self._conn is not None:
            cursor = self._conn.execute(
                "SELECT COUNT(*) FROM agent_memory WHERE agent_id = ?",
                (self.agent_id,),
            )
            long_term_count = cursor.fetchone()[0]

        return {
            "agent_id": self.agent_id,
            "short_term_count": short_term_count,
            "long_term_count": long_term_count,
            "type_counts": type_counts,
            "short_term_limit": self._short_term_limit,
        }

    def xǁAgentMemoryǁget_stats__mutmut_1(self) -> dict[str, Any]:
        """Get memory statistics."""
        with self._lock:
            short_term_count = None
            type_counts: dict[str, int] = {}
            for entry in self._short_term:
                type_counts[entry.entry_type] = type_counts.get(entry.entry_type, 0) + 1

        long_term_count = 0
        if self._conn is not None:
            cursor = self._conn.execute(
                "SELECT COUNT(*) FROM agent_memory WHERE agent_id = ?",
                (self.agent_id,),
            )
            long_term_count = cursor.fetchone()[0]

        return {
            "agent_id": self.agent_id,
            "short_term_count": short_term_count,
            "long_term_count": long_term_count,
            "type_counts": type_counts,
            "short_term_limit": self._short_term_limit,
        }

    def xǁAgentMemoryǁget_stats__mutmut_2(self) -> dict[str, Any]:
        """Get memory statistics."""
        with self._lock:
            short_term_count = len(self._short_term)
            type_counts: dict[str, int] = None
            for entry in self._short_term:
                type_counts[entry.entry_type] = type_counts.get(entry.entry_type, 0) + 1

        long_term_count = 0
        if self._conn is not None:
            cursor = self._conn.execute(
                "SELECT COUNT(*) FROM agent_memory WHERE agent_id = ?",
                (self.agent_id,),
            )
            long_term_count = cursor.fetchone()[0]

        return {
            "agent_id": self.agent_id,
            "short_term_count": short_term_count,
            "long_term_count": long_term_count,
            "type_counts": type_counts,
            "short_term_limit": self._short_term_limit,
        }

    def xǁAgentMemoryǁget_stats__mutmut_3(self) -> dict[str, Any]:
        """Get memory statistics."""
        with self._lock:
            short_term_count = len(self._short_term)
            type_counts: dict[str, int] = {}
            for entry in self._short_term:
                type_counts[entry.entry_type] = None

        long_term_count = 0
        if self._conn is not None:
            cursor = self._conn.execute(
                "SELECT COUNT(*) FROM agent_memory WHERE agent_id = ?",
                (self.agent_id,),
            )
            long_term_count = cursor.fetchone()[0]

        return {
            "agent_id": self.agent_id,
            "short_term_count": short_term_count,
            "long_term_count": long_term_count,
            "type_counts": type_counts,
            "short_term_limit": self._short_term_limit,
        }

    def xǁAgentMemoryǁget_stats__mutmut_4(self) -> dict[str, Any]:
        """Get memory statistics."""
        with self._lock:
            short_term_count = len(self._short_term)
            type_counts: dict[str, int] = {}
            for entry in self._short_term:
                type_counts[entry.entry_type] = type_counts.get(entry.entry_type, 0) - 1

        long_term_count = 0
        if self._conn is not None:
            cursor = self._conn.execute(
                "SELECT COUNT(*) FROM agent_memory WHERE agent_id = ?",
                (self.agent_id,),
            )
            long_term_count = cursor.fetchone()[0]

        return {
            "agent_id": self.agent_id,
            "short_term_count": short_term_count,
            "long_term_count": long_term_count,
            "type_counts": type_counts,
            "short_term_limit": self._short_term_limit,
        }

    def xǁAgentMemoryǁget_stats__mutmut_5(self) -> dict[str, Any]:
        """Get memory statistics."""
        with self._lock:
            short_term_count = len(self._short_term)
            type_counts: dict[str, int] = {}
            for entry in self._short_term:
                type_counts[entry.entry_type] = type_counts.get(None, 0) + 1

        long_term_count = 0
        if self._conn is not None:
            cursor = self._conn.execute(
                "SELECT COUNT(*) FROM agent_memory WHERE agent_id = ?",
                (self.agent_id,),
            )
            long_term_count = cursor.fetchone()[0]

        return {
            "agent_id": self.agent_id,
            "short_term_count": short_term_count,
            "long_term_count": long_term_count,
            "type_counts": type_counts,
            "short_term_limit": self._short_term_limit,
        }

    def xǁAgentMemoryǁget_stats__mutmut_6(self) -> dict[str, Any]:
        """Get memory statistics."""
        with self._lock:
            short_term_count = len(self._short_term)
            type_counts: dict[str, int] = {}
            for entry in self._short_term:
                type_counts[entry.entry_type] = type_counts.get(entry.entry_type, None) + 1

        long_term_count = 0
        if self._conn is not None:
            cursor = self._conn.execute(
                "SELECT COUNT(*) FROM agent_memory WHERE agent_id = ?",
                (self.agent_id,),
            )
            long_term_count = cursor.fetchone()[0]

        return {
            "agent_id": self.agent_id,
            "short_term_count": short_term_count,
            "long_term_count": long_term_count,
            "type_counts": type_counts,
            "short_term_limit": self._short_term_limit,
        }

    def xǁAgentMemoryǁget_stats__mutmut_7(self) -> dict[str, Any]:
        """Get memory statistics."""
        with self._lock:
            short_term_count = len(self._short_term)
            type_counts: dict[str, int] = {}
            for entry in self._short_term:
                type_counts[entry.entry_type] = type_counts.get(0) + 1

        long_term_count = 0
        if self._conn is not None:
            cursor = self._conn.execute(
                "SELECT COUNT(*) FROM agent_memory WHERE agent_id = ?",
                (self.agent_id,),
            )
            long_term_count = cursor.fetchone()[0]

        return {
            "agent_id": self.agent_id,
            "short_term_count": short_term_count,
            "long_term_count": long_term_count,
            "type_counts": type_counts,
            "short_term_limit": self._short_term_limit,
        }

    def xǁAgentMemoryǁget_stats__mutmut_8(self) -> dict[str, Any]:
        """Get memory statistics."""
        with self._lock:
            short_term_count = len(self._short_term)
            type_counts: dict[str, int] = {}
            for entry in self._short_term:
                type_counts[entry.entry_type] = type_counts.get(entry.entry_type, ) + 1

        long_term_count = 0
        if self._conn is not None:
            cursor = self._conn.execute(
                "SELECT COUNT(*) FROM agent_memory WHERE agent_id = ?",
                (self.agent_id,),
            )
            long_term_count = cursor.fetchone()[0]

        return {
            "agent_id": self.agent_id,
            "short_term_count": short_term_count,
            "long_term_count": long_term_count,
            "type_counts": type_counts,
            "short_term_limit": self._short_term_limit,
        }

    def xǁAgentMemoryǁget_stats__mutmut_9(self) -> dict[str, Any]:
        """Get memory statistics."""
        with self._lock:
            short_term_count = len(self._short_term)
            type_counts: dict[str, int] = {}
            for entry in self._short_term:
                type_counts[entry.entry_type] = type_counts.get(entry.entry_type, 1) + 1

        long_term_count = 0
        if self._conn is not None:
            cursor = self._conn.execute(
                "SELECT COUNT(*) FROM agent_memory WHERE agent_id = ?",
                (self.agent_id,),
            )
            long_term_count = cursor.fetchone()[0]

        return {
            "agent_id": self.agent_id,
            "short_term_count": short_term_count,
            "long_term_count": long_term_count,
            "type_counts": type_counts,
            "short_term_limit": self._short_term_limit,
        }

    def xǁAgentMemoryǁget_stats__mutmut_10(self) -> dict[str, Any]:
        """Get memory statistics."""
        with self._lock:
            short_term_count = len(self._short_term)
            type_counts: dict[str, int] = {}
            for entry in self._short_term:
                type_counts[entry.entry_type] = type_counts.get(entry.entry_type, 0) + 2

        long_term_count = 0
        if self._conn is not None:
            cursor = self._conn.execute(
                "SELECT COUNT(*) FROM agent_memory WHERE agent_id = ?",
                (self.agent_id,),
            )
            long_term_count = cursor.fetchone()[0]

        return {
            "agent_id": self.agent_id,
            "short_term_count": short_term_count,
            "long_term_count": long_term_count,
            "type_counts": type_counts,
            "short_term_limit": self._short_term_limit,
        }

    def xǁAgentMemoryǁget_stats__mutmut_11(self) -> dict[str, Any]:
        """Get memory statistics."""
        with self._lock:
            short_term_count = len(self._short_term)
            type_counts: dict[str, int] = {}
            for entry in self._short_term:
                type_counts[entry.entry_type] = type_counts.get(entry.entry_type, 0) + 1

        long_term_count = None
        if self._conn is not None:
            cursor = self._conn.execute(
                "SELECT COUNT(*) FROM agent_memory WHERE agent_id = ?",
                (self.agent_id,),
            )
            long_term_count = cursor.fetchone()[0]

        return {
            "agent_id": self.agent_id,
            "short_term_count": short_term_count,
            "long_term_count": long_term_count,
            "type_counts": type_counts,
            "short_term_limit": self._short_term_limit,
        }

    def xǁAgentMemoryǁget_stats__mutmut_12(self) -> dict[str, Any]:
        """Get memory statistics."""
        with self._lock:
            short_term_count = len(self._short_term)
            type_counts: dict[str, int] = {}
            for entry in self._short_term:
                type_counts[entry.entry_type] = type_counts.get(entry.entry_type, 0) + 1

        long_term_count = 1
        if self._conn is not None:
            cursor = self._conn.execute(
                "SELECT COUNT(*) FROM agent_memory WHERE agent_id = ?",
                (self.agent_id,),
            )
            long_term_count = cursor.fetchone()[0]

        return {
            "agent_id": self.agent_id,
            "short_term_count": short_term_count,
            "long_term_count": long_term_count,
            "type_counts": type_counts,
            "short_term_limit": self._short_term_limit,
        }

    def xǁAgentMemoryǁget_stats__mutmut_13(self) -> dict[str, Any]:
        """Get memory statistics."""
        with self._lock:
            short_term_count = len(self._short_term)
            type_counts: dict[str, int] = {}
            for entry in self._short_term:
                type_counts[entry.entry_type] = type_counts.get(entry.entry_type, 0) + 1

        long_term_count = 0
        if self._conn is None:
            cursor = self._conn.execute(
                "SELECT COUNT(*) FROM agent_memory WHERE agent_id = ?",
                (self.agent_id,),
            )
            long_term_count = cursor.fetchone()[0]

        return {
            "agent_id": self.agent_id,
            "short_term_count": short_term_count,
            "long_term_count": long_term_count,
            "type_counts": type_counts,
            "short_term_limit": self._short_term_limit,
        }

    def xǁAgentMemoryǁget_stats__mutmut_14(self) -> dict[str, Any]:
        """Get memory statistics."""
        with self._lock:
            short_term_count = len(self._short_term)
            type_counts: dict[str, int] = {}
            for entry in self._short_term:
                type_counts[entry.entry_type] = type_counts.get(entry.entry_type, 0) + 1

        long_term_count = 0
        if self._conn is not None:
            cursor = None
            long_term_count = cursor.fetchone()[0]

        return {
            "agent_id": self.agent_id,
            "short_term_count": short_term_count,
            "long_term_count": long_term_count,
            "type_counts": type_counts,
            "short_term_limit": self._short_term_limit,
        }

    def xǁAgentMemoryǁget_stats__mutmut_15(self) -> dict[str, Any]:
        """Get memory statistics."""
        with self._lock:
            short_term_count = len(self._short_term)
            type_counts: dict[str, int] = {}
            for entry in self._short_term:
                type_counts[entry.entry_type] = type_counts.get(entry.entry_type, 0) + 1

        long_term_count = 0
        if self._conn is not None:
            cursor = self._conn.execute(
                None,
                (self.agent_id,),
            )
            long_term_count = cursor.fetchone()[0]

        return {
            "agent_id": self.agent_id,
            "short_term_count": short_term_count,
            "long_term_count": long_term_count,
            "type_counts": type_counts,
            "short_term_limit": self._short_term_limit,
        }

    def xǁAgentMemoryǁget_stats__mutmut_16(self) -> dict[str, Any]:
        """Get memory statistics."""
        with self._lock:
            short_term_count = len(self._short_term)
            type_counts: dict[str, int] = {}
            for entry in self._short_term:
                type_counts[entry.entry_type] = type_counts.get(entry.entry_type, 0) + 1

        long_term_count = 0
        if self._conn is not None:
            cursor = self._conn.execute(
                "SELECT COUNT(*) FROM agent_memory WHERE agent_id = ?",
                None,
            )
            long_term_count = cursor.fetchone()[0]

        return {
            "agent_id": self.agent_id,
            "short_term_count": short_term_count,
            "long_term_count": long_term_count,
            "type_counts": type_counts,
            "short_term_limit": self._short_term_limit,
        }

    def xǁAgentMemoryǁget_stats__mutmut_17(self) -> dict[str, Any]:
        """Get memory statistics."""
        with self._lock:
            short_term_count = len(self._short_term)
            type_counts: dict[str, int] = {}
            for entry in self._short_term:
                type_counts[entry.entry_type] = type_counts.get(entry.entry_type, 0) + 1

        long_term_count = 0
        if self._conn is not None:
            cursor = self._conn.execute(
                (self.agent_id,),
            )
            long_term_count = cursor.fetchone()[0]

        return {
            "agent_id": self.agent_id,
            "short_term_count": short_term_count,
            "long_term_count": long_term_count,
            "type_counts": type_counts,
            "short_term_limit": self._short_term_limit,
        }

    def xǁAgentMemoryǁget_stats__mutmut_18(self) -> dict[str, Any]:
        """Get memory statistics."""
        with self._lock:
            short_term_count = len(self._short_term)
            type_counts: dict[str, int] = {}
            for entry in self._short_term:
                type_counts[entry.entry_type] = type_counts.get(entry.entry_type, 0) + 1

        long_term_count = 0
        if self._conn is not None:
            cursor = self._conn.execute(
                "SELECT COUNT(*) FROM agent_memory WHERE agent_id = ?",
                )
            long_term_count = cursor.fetchone()[0]

        return {
            "agent_id": self.agent_id,
            "short_term_count": short_term_count,
            "long_term_count": long_term_count,
            "type_counts": type_counts,
            "short_term_limit": self._short_term_limit,
        }

    def xǁAgentMemoryǁget_stats__mutmut_19(self) -> dict[str, Any]:
        """Get memory statistics."""
        with self._lock:
            short_term_count = len(self._short_term)
            type_counts: dict[str, int] = {}
            for entry in self._short_term:
                type_counts[entry.entry_type] = type_counts.get(entry.entry_type, 0) + 1

        long_term_count = 0
        if self._conn is not None:
            cursor = self._conn.execute(
                "XXSELECT COUNT(*) FROM agent_memory WHERE agent_id = ?XX",
                (self.agent_id,),
            )
            long_term_count = cursor.fetchone()[0]

        return {
            "agent_id": self.agent_id,
            "short_term_count": short_term_count,
            "long_term_count": long_term_count,
            "type_counts": type_counts,
            "short_term_limit": self._short_term_limit,
        }

    def xǁAgentMemoryǁget_stats__mutmut_20(self) -> dict[str, Any]:
        """Get memory statistics."""
        with self._lock:
            short_term_count = len(self._short_term)
            type_counts: dict[str, int] = {}
            for entry in self._short_term:
                type_counts[entry.entry_type] = type_counts.get(entry.entry_type, 0) + 1

        long_term_count = 0
        if self._conn is not None:
            cursor = self._conn.execute(
                "select count(*) from agent_memory where agent_id = ?",
                (self.agent_id,),
            )
            long_term_count = cursor.fetchone()[0]

        return {
            "agent_id": self.agent_id,
            "short_term_count": short_term_count,
            "long_term_count": long_term_count,
            "type_counts": type_counts,
            "short_term_limit": self._short_term_limit,
        }

    def xǁAgentMemoryǁget_stats__mutmut_21(self) -> dict[str, Any]:
        """Get memory statistics."""
        with self._lock:
            short_term_count = len(self._short_term)
            type_counts: dict[str, int] = {}
            for entry in self._short_term:
                type_counts[entry.entry_type] = type_counts.get(entry.entry_type, 0) + 1

        long_term_count = 0
        if self._conn is not None:
            cursor = self._conn.execute(
                "SELECT COUNT(*) FROM AGENT_MEMORY WHERE AGENT_ID = ?",
                (self.agent_id,),
            )
            long_term_count = cursor.fetchone()[0]

        return {
            "agent_id": self.agent_id,
            "short_term_count": short_term_count,
            "long_term_count": long_term_count,
            "type_counts": type_counts,
            "short_term_limit": self._short_term_limit,
        }

    def xǁAgentMemoryǁget_stats__mutmut_22(self) -> dict[str, Any]:
        """Get memory statistics."""
        with self._lock:
            short_term_count = len(self._short_term)
            type_counts: dict[str, int] = {}
            for entry in self._short_term:
                type_counts[entry.entry_type] = type_counts.get(entry.entry_type, 0) + 1

        long_term_count = 0
        if self._conn is not None:
            cursor = self._conn.execute(
                "SELECT COUNT(*) FROM agent_memory WHERE agent_id = ?",
                (self.agent_id,),
            )
            long_term_count = None

        return {
            "agent_id": self.agent_id,
            "short_term_count": short_term_count,
            "long_term_count": long_term_count,
            "type_counts": type_counts,
            "short_term_limit": self._short_term_limit,
        }

    def xǁAgentMemoryǁget_stats__mutmut_23(self) -> dict[str, Any]:
        """Get memory statistics."""
        with self._lock:
            short_term_count = len(self._short_term)
            type_counts: dict[str, int] = {}
            for entry in self._short_term:
                type_counts[entry.entry_type] = type_counts.get(entry.entry_type, 0) + 1

        long_term_count = 0
        if self._conn is not None:
            cursor = self._conn.execute(
                "SELECT COUNT(*) FROM agent_memory WHERE agent_id = ?",
                (self.agent_id,),
            )
            long_term_count = cursor.fetchone()[1]

        return {
            "agent_id": self.agent_id,
            "short_term_count": short_term_count,
            "long_term_count": long_term_count,
            "type_counts": type_counts,
            "short_term_limit": self._short_term_limit,
        }

    def xǁAgentMemoryǁget_stats__mutmut_24(self) -> dict[str, Any]:
        """Get memory statistics."""
        with self._lock:
            short_term_count = len(self._short_term)
            type_counts: dict[str, int] = {}
            for entry in self._short_term:
                type_counts[entry.entry_type] = type_counts.get(entry.entry_type, 0) + 1

        long_term_count = 0
        if self._conn is not None:
            cursor = self._conn.execute(
                "SELECT COUNT(*) FROM agent_memory WHERE agent_id = ?",
                (self.agent_id,),
            )
            long_term_count = cursor.fetchone()[0]

        return {
            "XXagent_idXX": self.agent_id,
            "short_term_count": short_term_count,
            "long_term_count": long_term_count,
            "type_counts": type_counts,
            "short_term_limit": self._short_term_limit,
        }

    def xǁAgentMemoryǁget_stats__mutmut_25(self) -> dict[str, Any]:
        """Get memory statistics."""
        with self._lock:
            short_term_count = len(self._short_term)
            type_counts: dict[str, int] = {}
            for entry in self._short_term:
                type_counts[entry.entry_type] = type_counts.get(entry.entry_type, 0) + 1

        long_term_count = 0
        if self._conn is not None:
            cursor = self._conn.execute(
                "SELECT COUNT(*) FROM agent_memory WHERE agent_id = ?",
                (self.agent_id,),
            )
            long_term_count = cursor.fetchone()[0]

        return {
            "AGENT_ID": self.agent_id,
            "short_term_count": short_term_count,
            "long_term_count": long_term_count,
            "type_counts": type_counts,
            "short_term_limit": self._short_term_limit,
        }

    def xǁAgentMemoryǁget_stats__mutmut_26(self) -> dict[str, Any]:
        """Get memory statistics."""
        with self._lock:
            short_term_count = len(self._short_term)
            type_counts: dict[str, int] = {}
            for entry in self._short_term:
                type_counts[entry.entry_type] = type_counts.get(entry.entry_type, 0) + 1

        long_term_count = 0
        if self._conn is not None:
            cursor = self._conn.execute(
                "SELECT COUNT(*) FROM agent_memory WHERE agent_id = ?",
                (self.agent_id,),
            )
            long_term_count = cursor.fetchone()[0]

        return {
            "agent_id": self.agent_id,
            "XXshort_term_countXX": short_term_count,
            "long_term_count": long_term_count,
            "type_counts": type_counts,
            "short_term_limit": self._short_term_limit,
        }

    def xǁAgentMemoryǁget_stats__mutmut_27(self) -> dict[str, Any]:
        """Get memory statistics."""
        with self._lock:
            short_term_count = len(self._short_term)
            type_counts: dict[str, int] = {}
            for entry in self._short_term:
                type_counts[entry.entry_type] = type_counts.get(entry.entry_type, 0) + 1

        long_term_count = 0
        if self._conn is not None:
            cursor = self._conn.execute(
                "SELECT COUNT(*) FROM agent_memory WHERE agent_id = ?",
                (self.agent_id,),
            )
            long_term_count = cursor.fetchone()[0]

        return {
            "agent_id": self.agent_id,
            "SHORT_TERM_COUNT": short_term_count,
            "long_term_count": long_term_count,
            "type_counts": type_counts,
            "short_term_limit": self._short_term_limit,
        }

    def xǁAgentMemoryǁget_stats__mutmut_28(self) -> dict[str, Any]:
        """Get memory statistics."""
        with self._lock:
            short_term_count = len(self._short_term)
            type_counts: dict[str, int] = {}
            for entry in self._short_term:
                type_counts[entry.entry_type] = type_counts.get(entry.entry_type, 0) + 1

        long_term_count = 0
        if self._conn is not None:
            cursor = self._conn.execute(
                "SELECT COUNT(*) FROM agent_memory WHERE agent_id = ?",
                (self.agent_id,),
            )
            long_term_count = cursor.fetchone()[0]

        return {
            "agent_id": self.agent_id,
            "short_term_count": short_term_count,
            "XXlong_term_countXX": long_term_count,
            "type_counts": type_counts,
            "short_term_limit": self._short_term_limit,
        }

    def xǁAgentMemoryǁget_stats__mutmut_29(self) -> dict[str, Any]:
        """Get memory statistics."""
        with self._lock:
            short_term_count = len(self._short_term)
            type_counts: dict[str, int] = {}
            for entry in self._short_term:
                type_counts[entry.entry_type] = type_counts.get(entry.entry_type, 0) + 1

        long_term_count = 0
        if self._conn is not None:
            cursor = self._conn.execute(
                "SELECT COUNT(*) FROM agent_memory WHERE agent_id = ?",
                (self.agent_id,),
            )
            long_term_count = cursor.fetchone()[0]

        return {
            "agent_id": self.agent_id,
            "short_term_count": short_term_count,
            "LONG_TERM_COUNT": long_term_count,
            "type_counts": type_counts,
            "short_term_limit": self._short_term_limit,
        }

    def xǁAgentMemoryǁget_stats__mutmut_30(self) -> dict[str, Any]:
        """Get memory statistics."""
        with self._lock:
            short_term_count = len(self._short_term)
            type_counts: dict[str, int] = {}
            for entry in self._short_term:
                type_counts[entry.entry_type] = type_counts.get(entry.entry_type, 0) + 1

        long_term_count = 0
        if self._conn is not None:
            cursor = self._conn.execute(
                "SELECT COUNT(*) FROM agent_memory WHERE agent_id = ?",
                (self.agent_id,),
            )
            long_term_count = cursor.fetchone()[0]

        return {
            "agent_id": self.agent_id,
            "short_term_count": short_term_count,
            "long_term_count": long_term_count,
            "XXtype_countsXX": type_counts,
            "short_term_limit": self._short_term_limit,
        }

    def xǁAgentMemoryǁget_stats__mutmut_31(self) -> dict[str, Any]:
        """Get memory statistics."""
        with self._lock:
            short_term_count = len(self._short_term)
            type_counts: dict[str, int] = {}
            for entry in self._short_term:
                type_counts[entry.entry_type] = type_counts.get(entry.entry_type, 0) + 1

        long_term_count = 0
        if self._conn is not None:
            cursor = self._conn.execute(
                "SELECT COUNT(*) FROM agent_memory WHERE agent_id = ?",
                (self.agent_id,),
            )
            long_term_count = cursor.fetchone()[0]

        return {
            "agent_id": self.agent_id,
            "short_term_count": short_term_count,
            "long_term_count": long_term_count,
            "TYPE_COUNTS": type_counts,
            "short_term_limit": self._short_term_limit,
        }

    def xǁAgentMemoryǁget_stats__mutmut_32(self) -> dict[str, Any]:
        """Get memory statistics."""
        with self._lock:
            short_term_count = len(self._short_term)
            type_counts: dict[str, int] = {}
            for entry in self._short_term:
                type_counts[entry.entry_type] = type_counts.get(entry.entry_type, 0) + 1

        long_term_count = 0
        if self._conn is not None:
            cursor = self._conn.execute(
                "SELECT COUNT(*) FROM agent_memory WHERE agent_id = ?",
                (self.agent_id,),
            )
            long_term_count = cursor.fetchone()[0]

        return {
            "agent_id": self.agent_id,
            "short_term_count": short_term_count,
            "long_term_count": long_term_count,
            "type_counts": type_counts,
            "XXshort_term_limitXX": self._short_term_limit,
        }

    def xǁAgentMemoryǁget_stats__mutmut_33(self) -> dict[str, Any]:
        """Get memory statistics."""
        with self._lock:
            short_term_count = len(self._short_term)
            type_counts: dict[str, int] = {}
            for entry in self._short_term:
                type_counts[entry.entry_type] = type_counts.get(entry.entry_type, 0) + 1

        long_term_count = 0
        if self._conn is not None:
            cursor = self._conn.execute(
                "SELECT COUNT(*) FROM agent_memory WHERE agent_id = ?",
                (self.agent_id,),
            )
            long_term_count = cursor.fetchone()[0]

        return {
            "agent_id": self.agent_id,
            "short_term_count": short_term_count,
            "long_term_count": long_term_count,
            "type_counts": type_counts,
            "SHORT_TERM_LIMIT": self._short_term_limit,
        }

    @_mutmut_mutated(mutants_xǁAgentMemoryǁclose__mutmut)
    def close(self) -> None:
        """Close the database connection."""
        if self._conn is not None:
            self._conn.close()
            self._conn = None

    def xǁAgentMemoryǁclose__mutmut_orig(self) -> None:
        """Close the database connection."""
        if self._conn is not None:
            self._conn.close()
            self._conn = None

    def xǁAgentMemoryǁclose__mutmut_1(self) -> None:
        """Close the database connection."""
        if self._conn is None:
            self._conn.close()
            self._conn = None

    def xǁAgentMemoryǁclose__mutmut_2(self) -> None:
        """Close the database connection."""
        if self._conn is not None:
            self._conn.close()
            self._conn = ""

mutants_xǁAgentMemoryǁ__init____mutmut['_mutmut_orig'] = AgentMemory.xǁAgentMemoryǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ__init____mutmut['xǁAgentMemoryǁ__init____mutmut_1'] = AgentMemory.xǁAgentMemoryǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ__init____mutmut['xǁAgentMemoryǁ__init____mutmut_2'] = AgentMemory.xǁAgentMemoryǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ__init____mutmut['xǁAgentMemoryǁ__init____mutmut_3'] = AgentMemory.xǁAgentMemoryǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ__init____mutmut['xǁAgentMemoryǁ__init____mutmut_4'] = AgentMemory.xǁAgentMemoryǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ__init____mutmut['xǁAgentMemoryǁ__init____mutmut_5'] = AgentMemory.xǁAgentMemoryǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ__init____mutmut['xǁAgentMemoryǁ__init____mutmut_6'] = AgentMemory.xǁAgentMemoryǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ__init____mutmut['xǁAgentMemoryǁ__init____mutmut_7'] = AgentMemory.xǁAgentMemoryǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ__init____mutmut['xǁAgentMemoryǁ__init____mutmut_8'] = AgentMemory.xǁAgentMemoryǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ__init____mutmut['xǁAgentMemoryǁ__init____mutmut_9'] = AgentMemory.xǁAgentMemoryǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ__init____mutmut['xǁAgentMemoryǁ__init____mutmut_10'] = AgentMemory.xǁAgentMemoryǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ__init____mutmut['xǁAgentMemoryǁ__init____mutmut_11'] = AgentMemory.xǁAgentMemoryǁ__init____mutmut_11 # type: ignore # mutmut generated

mutants_xǁAgentMemoryǁ_init_db__mutmut['_mutmut_orig'] = AgentMemory.xǁAgentMemoryǁ_init_db__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_init_db__mutmut['xǁAgentMemoryǁ_init_db__mutmut_1'] = AgentMemory.xǁAgentMemoryǁ_init_db__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_init_db__mutmut['xǁAgentMemoryǁ_init_db__mutmut_2'] = AgentMemory.xǁAgentMemoryǁ_init_db__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_init_db__mutmut['xǁAgentMemoryǁ_init_db__mutmut_3'] = AgentMemory.xǁAgentMemoryǁ_init_db__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_init_db__mutmut['xǁAgentMemoryǁ_init_db__mutmut_4'] = AgentMemory.xǁAgentMemoryǁ_init_db__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_init_db__mutmut['xǁAgentMemoryǁ_init_db__mutmut_5'] = AgentMemory.xǁAgentMemoryǁ_init_db__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_init_db__mutmut['xǁAgentMemoryǁ_init_db__mutmut_6'] = AgentMemory.xǁAgentMemoryǁ_init_db__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_init_db__mutmut['xǁAgentMemoryǁ_init_db__mutmut_7'] = AgentMemory.xǁAgentMemoryǁ_init_db__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_init_db__mutmut['xǁAgentMemoryǁ_init_db__mutmut_8'] = AgentMemory.xǁAgentMemoryǁ_init_db__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_init_db__mutmut['xǁAgentMemoryǁ_init_db__mutmut_9'] = AgentMemory.xǁAgentMemoryǁ_init_db__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_init_db__mutmut['xǁAgentMemoryǁ_init_db__mutmut_10'] = AgentMemory.xǁAgentMemoryǁ_init_db__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_init_db__mutmut['xǁAgentMemoryǁ_init_db__mutmut_11'] = AgentMemory.xǁAgentMemoryǁ_init_db__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_init_db__mutmut['xǁAgentMemoryǁ_init_db__mutmut_12'] = AgentMemory.xǁAgentMemoryǁ_init_db__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_init_db__mutmut['xǁAgentMemoryǁ_init_db__mutmut_13'] = AgentMemory.xǁAgentMemoryǁ_init_db__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_init_db__mutmut['xǁAgentMemoryǁ_init_db__mutmut_14'] = AgentMemory.xǁAgentMemoryǁ_init_db__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_init_db__mutmut['xǁAgentMemoryǁ_init_db__mutmut_15'] = AgentMemory.xǁAgentMemoryǁ_init_db__mutmut_15 # type: ignore # mutmut generated

mutants_xǁAgentMemoryǁstore__mutmut['_mutmut_orig'] = AgentMemory.xǁAgentMemoryǁstore__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁstore__mutmut['xǁAgentMemoryǁstore__mutmut_1'] = AgentMemory.xǁAgentMemoryǁstore__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁstore__mutmut['xǁAgentMemoryǁstore__mutmut_2'] = AgentMemory.xǁAgentMemoryǁstore__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁstore__mutmut['xǁAgentMemoryǁstore__mutmut_3'] = AgentMemory.xǁAgentMemoryǁstore__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁstore__mutmut['xǁAgentMemoryǁstore__mutmut_4'] = AgentMemory.xǁAgentMemoryǁstore__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁstore__mutmut['xǁAgentMemoryǁstore__mutmut_5'] = AgentMemory.xǁAgentMemoryǁstore__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁstore__mutmut['xǁAgentMemoryǁstore__mutmut_6'] = AgentMemory.xǁAgentMemoryǁstore__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁstore__mutmut['xǁAgentMemoryǁstore__mutmut_7'] = AgentMemory.xǁAgentMemoryǁstore__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁstore__mutmut['xǁAgentMemoryǁstore__mutmut_8'] = AgentMemory.xǁAgentMemoryǁstore__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁstore__mutmut['xǁAgentMemoryǁstore__mutmut_9'] = AgentMemory.xǁAgentMemoryǁstore__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁstore__mutmut['xǁAgentMemoryǁstore__mutmut_10'] = AgentMemory.xǁAgentMemoryǁstore__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁstore__mutmut['xǁAgentMemoryǁstore__mutmut_11'] = AgentMemory.xǁAgentMemoryǁstore__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁstore__mutmut['xǁAgentMemoryǁstore__mutmut_12'] = AgentMemory.xǁAgentMemoryǁstore__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁstore__mutmut['xǁAgentMemoryǁstore__mutmut_13'] = AgentMemory.xǁAgentMemoryǁstore__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁstore__mutmut['xǁAgentMemoryǁstore__mutmut_14'] = AgentMemory.xǁAgentMemoryǁstore__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁstore__mutmut['xǁAgentMemoryǁstore__mutmut_15'] = AgentMemory.xǁAgentMemoryǁstore__mutmut_15 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁstore__mutmut['xǁAgentMemoryǁstore__mutmut_16'] = AgentMemory.xǁAgentMemoryǁstore__mutmut_16 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁstore__mutmut['xǁAgentMemoryǁstore__mutmut_17'] = AgentMemory.xǁAgentMemoryǁstore__mutmut_17 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁstore__mutmut['xǁAgentMemoryǁstore__mutmut_18'] = AgentMemory.xǁAgentMemoryǁstore__mutmut_18 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁstore__mutmut['xǁAgentMemoryǁstore__mutmut_19'] = AgentMemory.xǁAgentMemoryǁstore__mutmut_19 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁstore__mutmut['xǁAgentMemoryǁstore__mutmut_20'] = AgentMemory.xǁAgentMemoryǁstore__mutmut_20 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁstore__mutmut['xǁAgentMemoryǁstore__mutmut_21'] = AgentMemory.xǁAgentMemoryǁstore__mutmut_21 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁstore__mutmut['xǁAgentMemoryǁstore__mutmut_22'] = AgentMemory.xǁAgentMemoryǁstore__mutmut_22 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁstore__mutmut['xǁAgentMemoryǁstore__mutmut_23'] = AgentMemory.xǁAgentMemoryǁstore__mutmut_23 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁstore__mutmut['xǁAgentMemoryǁstore__mutmut_24'] = AgentMemory.xǁAgentMemoryǁstore__mutmut_24 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁstore__mutmut['xǁAgentMemoryǁstore__mutmut_25'] = AgentMemory.xǁAgentMemoryǁstore__mutmut_25 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁstore__mutmut['xǁAgentMemoryǁstore__mutmut_26'] = AgentMemory.xǁAgentMemoryǁstore__mutmut_26 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁstore__mutmut['xǁAgentMemoryǁstore__mutmut_27'] = AgentMemory.xǁAgentMemoryǁstore__mutmut_27 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁstore__mutmut['xǁAgentMemoryǁstore__mutmut_28'] = AgentMemory.xǁAgentMemoryǁstore__mutmut_28 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁstore__mutmut['xǁAgentMemoryǁstore__mutmut_29'] = AgentMemory.xǁAgentMemoryǁstore__mutmut_29 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁstore__mutmut['xǁAgentMemoryǁstore__mutmut_30'] = AgentMemory.xǁAgentMemoryǁstore__mutmut_30 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁstore__mutmut['xǁAgentMemoryǁstore__mutmut_31'] = AgentMemory.xǁAgentMemoryǁstore__mutmut_31 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁstore__mutmut['xǁAgentMemoryǁstore__mutmut_32'] = AgentMemory.xǁAgentMemoryǁstore__mutmut_32 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁstore__mutmut['xǁAgentMemoryǁstore__mutmut_33'] = AgentMemory.xǁAgentMemoryǁstore__mutmut_33 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁstore__mutmut['xǁAgentMemoryǁstore__mutmut_34'] = AgentMemory.xǁAgentMemoryǁstore__mutmut_34 # type: ignore # mutmut generated

mutants_xǁAgentMemoryǁ_persist_entry__mutmut['_mutmut_orig'] = AgentMemory.xǁAgentMemoryǁ_persist_entry__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_persist_entry__mutmut['xǁAgentMemoryǁ_persist_entry__mutmut_1'] = AgentMemory.xǁAgentMemoryǁ_persist_entry__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_persist_entry__mutmut['xǁAgentMemoryǁ_persist_entry__mutmut_2'] = AgentMemory.xǁAgentMemoryǁ_persist_entry__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_persist_entry__mutmut['xǁAgentMemoryǁ_persist_entry__mutmut_3'] = AgentMemory.xǁAgentMemoryǁ_persist_entry__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_persist_entry__mutmut['xǁAgentMemoryǁ_persist_entry__mutmut_4'] = AgentMemory.xǁAgentMemoryǁ_persist_entry__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_persist_entry__mutmut['xǁAgentMemoryǁ_persist_entry__mutmut_5'] = AgentMemory.xǁAgentMemoryǁ_persist_entry__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_persist_entry__mutmut['xǁAgentMemoryǁ_persist_entry__mutmut_6'] = AgentMemory.xǁAgentMemoryǁ_persist_entry__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_persist_entry__mutmut['xǁAgentMemoryǁ_persist_entry__mutmut_7'] = AgentMemory.xǁAgentMemoryǁ_persist_entry__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_persist_entry__mutmut['xǁAgentMemoryǁ_persist_entry__mutmut_8'] = AgentMemory.xǁAgentMemoryǁ_persist_entry__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_persist_entry__mutmut['xǁAgentMemoryǁ_persist_entry__mutmut_9'] = AgentMemory.xǁAgentMemoryǁ_persist_entry__mutmut_9 # type: ignore # mutmut generated

mutants_xǁAgentMemoryǁrecall__mutmut['_mutmut_orig'] = AgentMemory.xǁAgentMemoryǁrecall__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁrecall__mutmut['xǁAgentMemoryǁrecall__mutmut_1'] = AgentMemory.xǁAgentMemoryǁrecall__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁrecall__mutmut['xǁAgentMemoryǁrecall__mutmut_2'] = AgentMemory.xǁAgentMemoryǁrecall__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁrecall__mutmut['xǁAgentMemoryǁrecall__mutmut_3'] = AgentMemory.xǁAgentMemoryǁrecall__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁrecall__mutmut['xǁAgentMemoryǁrecall__mutmut_4'] = AgentMemory.xǁAgentMemoryǁrecall__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁrecall__mutmut['xǁAgentMemoryǁrecall__mutmut_5'] = AgentMemory.xǁAgentMemoryǁrecall__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁrecall__mutmut['xǁAgentMemoryǁrecall__mutmut_6'] = AgentMemory.xǁAgentMemoryǁrecall__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁrecall__mutmut['xǁAgentMemoryǁrecall__mutmut_7'] = AgentMemory.xǁAgentMemoryǁrecall__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁrecall__mutmut['xǁAgentMemoryǁrecall__mutmut_8'] = AgentMemory.xǁAgentMemoryǁrecall__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁrecall__mutmut['xǁAgentMemoryǁrecall__mutmut_9'] = AgentMemory.xǁAgentMemoryǁrecall__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁrecall__mutmut['xǁAgentMemoryǁrecall__mutmut_10'] = AgentMemory.xǁAgentMemoryǁrecall__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁrecall__mutmut['xǁAgentMemoryǁrecall__mutmut_11'] = AgentMemory.xǁAgentMemoryǁrecall__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁrecall__mutmut['xǁAgentMemoryǁrecall__mutmut_12'] = AgentMemory.xǁAgentMemoryǁrecall__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁrecall__mutmut['xǁAgentMemoryǁrecall__mutmut_13'] = AgentMemory.xǁAgentMemoryǁrecall__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁrecall__mutmut['xǁAgentMemoryǁrecall__mutmut_14'] = AgentMemory.xǁAgentMemoryǁrecall__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁrecall__mutmut['xǁAgentMemoryǁrecall__mutmut_15'] = AgentMemory.xǁAgentMemoryǁrecall__mutmut_15 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁrecall__mutmut['xǁAgentMemoryǁrecall__mutmut_16'] = AgentMemory.xǁAgentMemoryǁrecall__mutmut_16 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁrecall__mutmut['xǁAgentMemoryǁrecall__mutmut_17'] = AgentMemory.xǁAgentMemoryǁrecall__mutmut_17 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁrecall__mutmut['xǁAgentMemoryǁrecall__mutmut_18'] = AgentMemory.xǁAgentMemoryǁrecall__mutmut_18 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁrecall__mutmut['xǁAgentMemoryǁrecall__mutmut_19'] = AgentMemory.xǁAgentMemoryǁrecall__mutmut_19 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁrecall__mutmut['xǁAgentMemoryǁrecall__mutmut_20'] = AgentMemory.xǁAgentMemoryǁrecall__mutmut_20 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁrecall__mutmut['xǁAgentMemoryǁrecall__mutmut_21'] = AgentMemory.xǁAgentMemoryǁrecall__mutmut_21 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁrecall__mutmut['xǁAgentMemoryǁrecall__mutmut_22'] = AgentMemory.xǁAgentMemoryǁrecall__mutmut_22 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁrecall__mutmut['xǁAgentMemoryǁrecall__mutmut_23'] = AgentMemory.xǁAgentMemoryǁrecall__mutmut_23 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁrecall__mutmut['xǁAgentMemoryǁrecall__mutmut_24'] = AgentMemory.xǁAgentMemoryǁrecall__mutmut_24 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁrecall__mutmut['xǁAgentMemoryǁrecall__mutmut_25'] = AgentMemory.xǁAgentMemoryǁrecall__mutmut_25 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁrecall__mutmut['xǁAgentMemoryǁrecall__mutmut_26'] = AgentMemory.xǁAgentMemoryǁrecall__mutmut_26 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁrecall__mutmut['xǁAgentMemoryǁrecall__mutmut_27'] = AgentMemory.xǁAgentMemoryǁrecall__mutmut_27 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁrecall__mutmut['xǁAgentMemoryǁrecall__mutmut_28'] = AgentMemory.xǁAgentMemoryǁrecall__mutmut_28 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁrecall__mutmut['xǁAgentMemoryǁrecall__mutmut_29'] = AgentMemory.xǁAgentMemoryǁrecall__mutmut_29 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁrecall__mutmut['xǁAgentMemoryǁrecall__mutmut_30'] = AgentMemory.xǁAgentMemoryǁrecall__mutmut_30 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁrecall__mutmut['xǁAgentMemoryǁrecall__mutmut_31'] = AgentMemory.xǁAgentMemoryǁrecall__mutmut_31 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁrecall__mutmut['xǁAgentMemoryǁrecall__mutmut_32'] = AgentMemory.xǁAgentMemoryǁrecall__mutmut_32 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁrecall__mutmut['xǁAgentMemoryǁrecall__mutmut_33'] = AgentMemory.xǁAgentMemoryǁrecall__mutmut_33 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁrecall__mutmut['xǁAgentMemoryǁrecall__mutmut_34'] = AgentMemory.xǁAgentMemoryǁrecall__mutmut_34 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁrecall__mutmut['xǁAgentMemoryǁrecall__mutmut_35'] = AgentMemory.xǁAgentMemoryǁrecall__mutmut_35 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁrecall__mutmut['xǁAgentMemoryǁrecall__mutmut_36'] = AgentMemory.xǁAgentMemoryǁrecall__mutmut_36 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁrecall__mutmut['xǁAgentMemoryǁrecall__mutmut_37'] = AgentMemory.xǁAgentMemoryǁrecall__mutmut_37 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁrecall__mutmut['xǁAgentMemoryǁrecall__mutmut_38'] = AgentMemory.xǁAgentMemoryǁrecall__mutmut_38 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁrecall__mutmut['xǁAgentMemoryǁrecall__mutmut_39'] = AgentMemory.xǁAgentMemoryǁrecall__mutmut_39 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁrecall__mutmut['xǁAgentMemoryǁrecall__mutmut_40'] = AgentMemory.xǁAgentMemoryǁrecall__mutmut_40 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁrecall__mutmut['xǁAgentMemoryǁrecall__mutmut_41'] = AgentMemory.xǁAgentMemoryǁrecall__mutmut_41 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁrecall__mutmut['xǁAgentMemoryǁrecall__mutmut_42'] = AgentMemory.xǁAgentMemoryǁrecall__mutmut_42 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁrecall__mutmut['xǁAgentMemoryǁrecall__mutmut_43'] = AgentMemory.xǁAgentMemoryǁrecall__mutmut_43 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁrecall__mutmut['xǁAgentMemoryǁrecall__mutmut_44'] = AgentMemory.xǁAgentMemoryǁrecall__mutmut_44 # type: ignore # mutmut generated

mutants_xǁAgentMemoryǁ_search_entries__mutmut['_mutmut_orig'] = AgentMemory.xǁAgentMemoryǁ_search_entries__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_search_entries__mutmut['xǁAgentMemoryǁ_search_entries__mutmut_1'] = AgentMemory.xǁAgentMemoryǁ_search_entries__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_search_entries__mutmut['xǁAgentMemoryǁ_search_entries__mutmut_2'] = AgentMemory.xǁAgentMemoryǁ_search_entries__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_search_entries__mutmut['xǁAgentMemoryǁ_search_entries__mutmut_3'] = AgentMemory.xǁAgentMemoryǁ_search_entries__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_search_entries__mutmut['xǁAgentMemoryǁ_search_entries__mutmut_4'] = AgentMemory.xǁAgentMemoryǁ_search_entries__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_search_entries__mutmut['xǁAgentMemoryǁ_search_entries__mutmut_5'] = AgentMemory.xǁAgentMemoryǁ_search_entries__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_search_entries__mutmut['xǁAgentMemoryǁ_search_entries__mutmut_6'] = AgentMemory.xǁAgentMemoryǁ_search_entries__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_search_entries__mutmut['xǁAgentMemoryǁ_search_entries__mutmut_7'] = AgentMemory.xǁAgentMemoryǁ_search_entries__mutmut_7 # type: ignore # mutmut generated

mutants_xǁAgentMemoryǁ_search_db__mutmut['_mutmut_orig'] = AgentMemory.xǁAgentMemoryǁ_search_db__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_search_db__mutmut['xǁAgentMemoryǁ_search_db__mutmut_1'] = AgentMemory.xǁAgentMemoryǁ_search_db__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_search_db__mutmut['xǁAgentMemoryǁ_search_db__mutmut_2'] = AgentMemory.xǁAgentMemoryǁ_search_db__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_search_db__mutmut['xǁAgentMemoryǁ_search_db__mutmut_3'] = AgentMemory.xǁAgentMemoryǁ_search_db__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_search_db__mutmut['xǁAgentMemoryǁ_search_db__mutmut_4'] = AgentMemory.xǁAgentMemoryǁ_search_db__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_search_db__mutmut['xǁAgentMemoryǁ_search_db__mutmut_5'] = AgentMemory.xǁAgentMemoryǁ_search_db__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_search_db__mutmut['xǁAgentMemoryǁ_search_db__mutmut_6'] = AgentMemory.xǁAgentMemoryǁ_search_db__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_search_db__mutmut['xǁAgentMemoryǁ_search_db__mutmut_7'] = AgentMemory.xǁAgentMemoryǁ_search_db__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_search_db__mutmut['xǁAgentMemoryǁ_search_db__mutmut_8'] = AgentMemory.xǁAgentMemoryǁ_search_db__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_search_db__mutmut['xǁAgentMemoryǁ_search_db__mutmut_9'] = AgentMemory.xǁAgentMemoryǁ_search_db__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_search_db__mutmut['xǁAgentMemoryǁ_search_db__mutmut_10'] = AgentMemory.xǁAgentMemoryǁ_search_db__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_search_db__mutmut['xǁAgentMemoryǁ_search_db__mutmut_11'] = AgentMemory.xǁAgentMemoryǁ_search_db__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_search_db__mutmut['xǁAgentMemoryǁ_search_db__mutmut_12'] = AgentMemory.xǁAgentMemoryǁ_search_db__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_search_db__mutmut['xǁAgentMemoryǁ_search_db__mutmut_13'] = AgentMemory.xǁAgentMemoryǁ_search_db__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_search_db__mutmut['xǁAgentMemoryǁ_search_db__mutmut_14'] = AgentMemory.xǁAgentMemoryǁ_search_db__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_search_db__mutmut['xǁAgentMemoryǁ_search_db__mutmut_15'] = AgentMemory.xǁAgentMemoryǁ_search_db__mutmut_15 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_search_db__mutmut['xǁAgentMemoryǁ_search_db__mutmut_16'] = AgentMemory.xǁAgentMemoryǁ_search_db__mutmut_16 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_search_db__mutmut['xǁAgentMemoryǁ_search_db__mutmut_17'] = AgentMemory.xǁAgentMemoryǁ_search_db__mutmut_17 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_search_db__mutmut['xǁAgentMemoryǁ_search_db__mutmut_18'] = AgentMemory.xǁAgentMemoryǁ_search_db__mutmut_18 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_search_db__mutmut['xǁAgentMemoryǁ_search_db__mutmut_19'] = AgentMemory.xǁAgentMemoryǁ_search_db__mutmut_19 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_search_db__mutmut['xǁAgentMemoryǁ_search_db__mutmut_20'] = AgentMemory.xǁAgentMemoryǁ_search_db__mutmut_20 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_search_db__mutmut['xǁAgentMemoryǁ_search_db__mutmut_21'] = AgentMemory.xǁAgentMemoryǁ_search_db__mutmut_21 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_search_db__mutmut['xǁAgentMemoryǁ_search_db__mutmut_22'] = AgentMemory.xǁAgentMemoryǁ_search_db__mutmut_22 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_search_db__mutmut['xǁAgentMemoryǁ_search_db__mutmut_23'] = AgentMemory.xǁAgentMemoryǁ_search_db__mutmut_23 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_search_db__mutmut['xǁAgentMemoryǁ_search_db__mutmut_24'] = AgentMemory.xǁAgentMemoryǁ_search_db__mutmut_24 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_search_db__mutmut['xǁAgentMemoryǁ_search_db__mutmut_25'] = AgentMemory.xǁAgentMemoryǁ_search_db__mutmut_25 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_search_db__mutmut['xǁAgentMemoryǁ_search_db__mutmut_26'] = AgentMemory.xǁAgentMemoryǁ_search_db__mutmut_26 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_search_db__mutmut['xǁAgentMemoryǁ_search_db__mutmut_27'] = AgentMemory.xǁAgentMemoryǁ_search_db__mutmut_27 # type: ignore # mutmut generated

mutants_xǁAgentMemoryǁ_row_to_entry__mutmut['_mutmut_orig'] = AgentMemory.xǁAgentMemoryǁ_row_to_entry__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_row_to_entry__mutmut['xǁAgentMemoryǁ_row_to_entry__mutmut_1'] = AgentMemory.xǁAgentMemoryǁ_row_to_entry__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_row_to_entry__mutmut['xǁAgentMemoryǁ_row_to_entry__mutmut_2'] = AgentMemory.xǁAgentMemoryǁ_row_to_entry__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_row_to_entry__mutmut['xǁAgentMemoryǁ_row_to_entry__mutmut_3'] = AgentMemory.xǁAgentMemoryǁ_row_to_entry__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_row_to_entry__mutmut['xǁAgentMemoryǁ_row_to_entry__mutmut_4'] = AgentMemory.xǁAgentMemoryǁ_row_to_entry__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_row_to_entry__mutmut['xǁAgentMemoryǁ_row_to_entry__mutmut_5'] = AgentMemory.xǁAgentMemoryǁ_row_to_entry__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_row_to_entry__mutmut['xǁAgentMemoryǁ_row_to_entry__mutmut_6'] = AgentMemory.xǁAgentMemoryǁ_row_to_entry__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_row_to_entry__mutmut['xǁAgentMemoryǁ_row_to_entry__mutmut_7'] = AgentMemory.xǁAgentMemoryǁ_row_to_entry__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_row_to_entry__mutmut['xǁAgentMemoryǁ_row_to_entry__mutmut_8'] = AgentMemory.xǁAgentMemoryǁ_row_to_entry__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_row_to_entry__mutmut['xǁAgentMemoryǁ_row_to_entry__mutmut_9'] = AgentMemory.xǁAgentMemoryǁ_row_to_entry__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_row_to_entry__mutmut['xǁAgentMemoryǁ_row_to_entry__mutmut_10'] = AgentMemory.xǁAgentMemoryǁ_row_to_entry__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_row_to_entry__mutmut['xǁAgentMemoryǁ_row_to_entry__mutmut_11'] = AgentMemory.xǁAgentMemoryǁ_row_to_entry__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_row_to_entry__mutmut['xǁAgentMemoryǁ_row_to_entry__mutmut_12'] = AgentMemory.xǁAgentMemoryǁ_row_to_entry__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_row_to_entry__mutmut['xǁAgentMemoryǁ_row_to_entry__mutmut_13'] = AgentMemory.xǁAgentMemoryǁ_row_to_entry__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_row_to_entry__mutmut['xǁAgentMemoryǁ_row_to_entry__mutmut_14'] = AgentMemory.xǁAgentMemoryǁ_row_to_entry__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_row_to_entry__mutmut['xǁAgentMemoryǁ_row_to_entry__mutmut_15'] = AgentMemory.xǁAgentMemoryǁ_row_to_entry__mutmut_15 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_row_to_entry__mutmut['xǁAgentMemoryǁ_row_to_entry__mutmut_16'] = AgentMemory.xǁAgentMemoryǁ_row_to_entry__mutmut_16 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_row_to_entry__mutmut['xǁAgentMemoryǁ_row_to_entry__mutmut_17'] = AgentMemory.xǁAgentMemoryǁ_row_to_entry__mutmut_17 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_row_to_entry__mutmut['xǁAgentMemoryǁ_row_to_entry__mutmut_18'] = AgentMemory.xǁAgentMemoryǁ_row_to_entry__mutmut_18 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_row_to_entry__mutmut['xǁAgentMemoryǁ_row_to_entry__mutmut_19'] = AgentMemory.xǁAgentMemoryǁ_row_to_entry__mutmut_19 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_row_to_entry__mutmut['xǁAgentMemoryǁ_row_to_entry__mutmut_20'] = AgentMemory.xǁAgentMemoryǁ_row_to_entry__mutmut_20 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_row_to_entry__mutmut['xǁAgentMemoryǁ_row_to_entry__mutmut_21'] = AgentMemory.xǁAgentMemoryǁ_row_to_entry__mutmut_21 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_row_to_entry__mutmut['xǁAgentMemoryǁ_row_to_entry__mutmut_22'] = AgentMemory.xǁAgentMemoryǁ_row_to_entry__mutmut_22 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_row_to_entry__mutmut['xǁAgentMemoryǁ_row_to_entry__mutmut_23'] = AgentMemory.xǁAgentMemoryǁ_row_to_entry__mutmut_23 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_row_to_entry__mutmut['xǁAgentMemoryǁ_row_to_entry__mutmut_24'] = AgentMemory.xǁAgentMemoryǁ_row_to_entry__mutmut_24 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_row_to_entry__mutmut['xǁAgentMemoryǁ_row_to_entry__mutmut_25'] = AgentMemory.xǁAgentMemoryǁ_row_to_entry__mutmut_25 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_row_to_entry__mutmut['xǁAgentMemoryǁ_row_to_entry__mutmut_26'] = AgentMemory.xǁAgentMemoryǁ_row_to_entry__mutmut_26 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_row_to_entry__mutmut['xǁAgentMemoryǁ_row_to_entry__mutmut_27'] = AgentMemory.xǁAgentMemoryǁ_row_to_entry__mutmut_27 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_row_to_entry__mutmut['xǁAgentMemoryǁ_row_to_entry__mutmut_28'] = AgentMemory.xǁAgentMemoryǁ_row_to_entry__mutmut_28 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_row_to_entry__mutmut['xǁAgentMemoryǁ_row_to_entry__mutmut_29'] = AgentMemory.xǁAgentMemoryǁ_row_to_entry__mutmut_29 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_row_to_entry__mutmut['xǁAgentMemoryǁ_row_to_entry__mutmut_30'] = AgentMemory.xǁAgentMemoryǁ_row_to_entry__mutmut_30 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_row_to_entry__mutmut['xǁAgentMemoryǁ_row_to_entry__mutmut_31'] = AgentMemory.xǁAgentMemoryǁ_row_to_entry__mutmut_31 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_row_to_entry__mutmut['xǁAgentMemoryǁ_row_to_entry__mutmut_32'] = AgentMemory.xǁAgentMemoryǁ_row_to_entry__mutmut_32 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_row_to_entry__mutmut['xǁAgentMemoryǁ_row_to_entry__mutmut_33'] = AgentMemory.xǁAgentMemoryǁ_row_to_entry__mutmut_33 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_row_to_entry__mutmut['xǁAgentMemoryǁ_row_to_entry__mutmut_34'] = AgentMemory.xǁAgentMemoryǁ_row_to_entry__mutmut_34 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_row_to_entry__mutmut['xǁAgentMemoryǁ_row_to_entry__mutmut_35'] = AgentMemory.xǁAgentMemoryǁ_row_to_entry__mutmut_35 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_row_to_entry__mutmut['xǁAgentMemoryǁ_row_to_entry__mutmut_36'] = AgentMemory.xǁAgentMemoryǁ_row_to_entry__mutmut_36 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_row_to_entry__mutmut['xǁAgentMemoryǁ_row_to_entry__mutmut_37'] = AgentMemory.xǁAgentMemoryǁ_row_to_entry__mutmut_37 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_row_to_entry__mutmut['xǁAgentMemoryǁ_row_to_entry__mutmut_38'] = AgentMemory.xǁAgentMemoryǁ_row_to_entry__mutmut_38 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_row_to_entry__mutmut['xǁAgentMemoryǁ_row_to_entry__mutmut_39'] = AgentMemory.xǁAgentMemoryǁ_row_to_entry__mutmut_39 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_row_to_entry__mutmut['xǁAgentMemoryǁ_row_to_entry__mutmut_40'] = AgentMemory.xǁAgentMemoryǁ_row_to_entry__mutmut_40 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_row_to_entry__mutmut['xǁAgentMemoryǁ_row_to_entry__mutmut_41'] = AgentMemory.xǁAgentMemoryǁ_row_to_entry__mutmut_41 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_row_to_entry__mutmut['xǁAgentMemoryǁ_row_to_entry__mutmut_42'] = AgentMemory.xǁAgentMemoryǁ_row_to_entry__mutmut_42 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_row_to_entry__mutmut['xǁAgentMemoryǁ_row_to_entry__mutmut_43'] = AgentMemory.xǁAgentMemoryǁ_row_to_entry__mutmut_43 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_row_to_entry__mutmut['xǁAgentMemoryǁ_row_to_entry__mutmut_44'] = AgentMemory.xǁAgentMemoryǁ_row_to_entry__mutmut_44 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_row_to_entry__mutmut['xǁAgentMemoryǁ_row_to_entry__mutmut_45'] = AgentMemory.xǁAgentMemoryǁ_row_to_entry__mutmut_45 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_row_to_entry__mutmut['xǁAgentMemoryǁ_row_to_entry__mutmut_46'] = AgentMemory.xǁAgentMemoryǁ_row_to_entry__mutmut_46 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_row_to_entry__mutmut['xǁAgentMemoryǁ_row_to_entry__mutmut_47'] = AgentMemory.xǁAgentMemoryǁ_row_to_entry__mutmut_47 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_row_to_entry__mutmut['xǁAgentMemoryǁ_row_to_entry__mutmut_48'] = AgentMemory.xǁAgentMemoryǁ_row_to_entry__mutmut_48 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁ_row_to_entry__mutmut['xǁAgentMemoryǁ_row_to_entry__mutmut_49'] = AgentMemory.xǁAgentMemoryǁ_row_to_entry__mutmut_49 # type: ignore # mutmut generated

mutants_xǁAgentMemoryǁconsolidate__mutmut['_mutmut_orig'] = AgentMemory.xǁAgentMemoryǁconsolidate__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁconsolidate__mutmut['xǁAgentMemoryǁconsolidate__mutmut_1'] = AgentMemory.xǁAgentMemoryǁconsolidate__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁconsolidate__mutmut['xǁAgentMemoryǁconsolidate__mutmut_2'] = AgentMemory.xǁAgentMemoryǁconsolidate__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁconsolidate__mutmut['xǁAgentMemoryǁconsolidate__mutmut_3'] = AgentMemory.xǁAgentMemoryǁconsolidate__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁconsolidate__mutmut['xǁAgentMemoryǁconsolidate__mutmut_4'] = AgentMemory.xǁAgentMemoryǁconsolidate__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁconsolidate__mutmut['xǁAgentMemoryǁconsolidate__mutmut_5'] = AgentMemory.xǁAgentMemoryǁconsolidate__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁconsolidate__mutmut['xǁAgentMemoryǁconsolidate__mutmut_6'] = AgentMemory.xǁAgentMemoryǁconsolidate__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁconsolidate__mutmut['xǁAgentMemoryǁconsolidate__mutmut_7'] = AgentMemory.xǁAgentMemoryǁconsolidate__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁconsolidate__mutmut['xǁAgentMemoryǁconsolidate__mutmut_8'] = AgentMemory.xǁAgentMemoryǁconsolidate__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁconsolidate__mutmut['xǁAgentMemoryǁconsolidate__mutmut_9'] = AgentMemory.xǁAgentMemoryǁconsolidate__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁconsolidate__mutmut['xǁAgentMemoryǁconsolidate__mutmut_10'] = AgentMemory.xǁAgentMemoryǁconsolidate__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁconsolidate__mutmut['xǁAgentMemoryǁconsolidate__mutmut_11'] = AgentMemory.xǁAgentMemoryǁconsolidate__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁconsolidate__mutmut['xǁAgentMemoryǁconsolidate__mutmut_12'] = AgentMemory.xǁAgentMemoryǁconsolidate__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁconsolidate__mutmut['xǁAgentMemoryǁconsolidate__mutmut_13'] = AgentMemory.xǁAgentMemoryǁconsolidate__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁconsolidate__mutmut['xǁAgentMemoryǁconsolidate__mutmut_14'] = AgentMemory.xǁAgentMemoryǁconsolidate__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁconsolidate__mutmut['xǁAgentMemoryǁconsolidate__mutmut_15'] = AgentMemory.xǁAgentMemoryǁconsolidate__mutmut_15 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁconsolidate__mutmut['xǁAgentMemoryǁconsolidate__mutmut_16'] = AgentMemory.xǁAgentMemoryǁconsolidate__mutmut_16 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁconsolidate__mutmut['xǁAgentMemoryǁconsolidate__mutmut_17'] = AgentMemory.xǁAgentMemoryǁconsolidate__mutmut_17 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁconsolidate__mutmut['xǁAgentMemoryǁconsolidate__mutmut_18'] = AgentMemory.xǁAgentMemoryǁconsolidate__mutmut_18 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁconsolidate__mutmut['xǁAgentMemoryǁconsolidate__mutmut_19'] = AgentMemory.xǁAgentMemoryǁconsolidate__mutmut_19 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁconsolidate__mutmut['xǁAgentMemoryǁconsolidate__mutmut_20'] = AgentMemory.xǁAgentMemoryǁconsolidate__mutmut_20 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁconsolidate__mutmut['xǁAgentMemoryǁconsolidate__mutmut_21'] = AgentMemory.xǁAgentMemoryǁconsolidate__mutmut_21 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁconsolidate__mutmut['xǁAgentMemoryǁconsolidate__mutmut_22'] = AgentMemory.xǁAgentMemoryǁconsolidate__mutmut_22 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁconsolidate__mutmut['xǁAgentMemoryǁconsolidate__mutmut_23'] = AgentMemory.xǁAgentMemoryǁconsolidate__mutmut_23 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁconsolidate__mutmut['xǁAgentMemoryǁconsolidate__mutmut_24'] = AgentMemory.xǁAgentMemoryǁconsolidate__mutmut_24 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁconsolidate__mutmut['xǁAgentMemoryǁconsolidate__mutmut_25'] = AgentMemory.xǁAgentMemoryǁconsolidate__mutmut_25 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁconsolidate__mutmut['xǁAgentMemoryǁconsolidate__mutmut_26'] = AgentMemory.xǁAgentMemoryǁconsolidate__mutmut_26 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁconsolidate__mutmut['xǁAgentMemoryǁconsolidate__mutmut_27'] = AgentMemory.xǁAgentMemoryǁconsolidate__mutmut_27 # type: ignore # mutmut generated

mutants_xǁAgentMemoryǁforget__mutmut['_mutmut_orig'] = AgentMemory.xǁAgentMemoryǁforget__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁforget__mutmut['xǁAgentMemoryǁforget__mutmut_1'] = AgentMemory.xǁAgentMemoryǁforget__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁforget__mutmut['xǁAgentMemoryǁforget__mutmut_2'] = AgentMemory.xǁAgentMemoryǁforget__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁforget__mutmut['xǁAgentMemoryǁforget__mutmut_3'] = AgentMemory.xǁAgentMemoryǁforget__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁforget__mutmut['xǁAgentMemoryǁforget__mutmut_4'] = AgentMemory.xǁAgentMemoryǁforget__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁforget__mutmut['xǁAgentMemoryǁforget__mutmut_5'] = AgentMemory.xǁAgentMemoryǁforget__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁforget__mutmut['xǁAgentMemoryǁforget__mutmut_6'] = AgentMemory.xǁAgentMemoryǁforget__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁforget__mutmut['xǁAgentMemoryǁforget__mutmut_7'] = AgentMemory.xǁAgentMemoryǁforget__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁforget__mutmut['xǁAgentMemoryǁforget__mutmut_8'] = AgentMemory.xǁAgentMemoryǁforget__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁforget__mutmut['xǁAgentMemoryǁforget__mutmut_9'] = AgentMemory.xǁAgentMemoryǁforget__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁforget__mutmut['xǁAgentMemoryǁforget__mutmut_10'] = AgentMemory.xǁAgentMemoryǁforget__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁforget__mutmut['xǁAgentMemoryǁforget__mutmut_11'] = AgentMemory.xǁAgentMemoryǁforget__mutmut_11 # type: ignore # mutmut generated

mutants_xǁAgentMemoryǁclear__mutmut['_mutmut_orig'] = AgentMemory.xǁAgentMemoryǁclear__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁclear__mutmut['xǁAgentMemoryǁclear__mutmut_1'] = AgentMemory.xǁAgentMemoryǁclear__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁclear__mutmut['xǁAgentMemoryǁclear__mutmut_2'] = AgentMemory.xǁAgentMemoryǁclear__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁclear__mutmut['xǁAgentMemoryǁclear__mutmut_3'] = AgentMemory.xǁAgentMemoryǁclear__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁclear__mutmut['xǁAgentMemoryǁclear__mutmut_4'] = AgentMemory.xǁAgentMemoryǁclear__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁclear__mutmut['xǁAgentMemoryǁclear__mutmut_5'] = AgentMemory.xǁAgentMemoryǁclear__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁclear__mutmut['xǁAgentMemoryǁclear__mutmut_6'] = AgentMemory.xǁAgentMemoryǁclear__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁclear__mutmut['xǁAgentMemoryǁclear__mutmut_7'] = AgentMemory.xǁAgentMemoryǁclear__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁclear__mutmut['xǁAgentMemoryǁclear__mutmut_8'] = AgentMemory.xǁAgentMemoryǁclear__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁclear__mutmut['xǁAgentMemoryǁclear__mutmut_9'] = AgentMemory.xǁAgentMemoryǁclear__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁclear__mutmut['xǁAgentMemoryǁclear__mutmut_10'] = AgentMemory.xǁAgentMemoryǁclear__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁclear__mutmut['xǁAgentMemoryǁclear__mutmut_11'] = AgentMemory.xǁAgentMemoryǁclear__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁclear__mutmut['xǁAgentMemoryǁclear__mutmut_12'] = AgentMemory.xǁAgentMemoryǁclear__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁclear__mutmut['xǁAgentMemoryǁclear__mutmut_13'] = AgentMemory.xǁAgentMemoryǁclear__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁclear__mutmut['xǁAgentMemoryǁclear__mutmut_14'] = AgentMemory.xǁAgentMemoryǁclear__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁclear__mutmut['xǁAgentMemoryǁclear__mutmut_15'] = AgentMemory.xǁAgentMemoryǁclear__mutmut_15 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁclear__mutmut['xǁAgentMemoryǁclear__mutmut_16'] = AgentMemory.xǁAgentMemoryǁclear__mutmut_16 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁclear__mutmut['xǁAgentMemoryǁclear__mutmut_17'] = AgentMemory.xǁAgentMemoryǁclear__mutmut_17 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁclear__mutmut['xǁAgentMemoryǁclear__mutmut_18'] = AgentMemory.xǁAgentMemoryǁclear__mutmut_18 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁclear__mutmut['xǁAgentMemoryǁclear__mutmut_19'] = AgentMemory.xǁAgentMemoryǁclear__mutmut_19 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁclear__mutmut['xǁAgentMemoryǁclear__mutmut_20'] = AgentMemory.xǁAgentMemoryǁclear__mutmut_20 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁclear__mutmut['xǁAgentMemoryǁclear__mutmut_21'] = AgentMemory.xǁAgentMemoryǁclear__mutmut_21 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁclear__mutmut['xǁAgentMemoryǁclear__mutmut_22'] = AgentMemory.xǁAgentMemoryǁclear__mutmut_22 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁclear__mutmut['xǁAgentMemoryǁclear__mutmut_23'] = AgentMemory.xǁAgentMemoryǁclear__mutmut_23 # type: ignore # mutmut generated

mutants_xǁAgentMemoryǁget_stats__mutmut['_mutmut_orig'] = AgentMemory.xǁAgentMemoryǁget_stats__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁget_stats__mutmut['xǁAgentMemoryǁget_stats__mutmut_1'] = AgentMemory.xǁAgentMemoryǁget_stats__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁget_stats__mutmut['xǁAgentMemoryǁget_stats__mutmut_2'] = AgentMemory.xǁAgentMemoryǁget_stats__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁget_stats__mutmut['xǁAgentMemoryǁget_stats__mutmut_3'] = AgentMemory.xǁAgentMemoryǁget_stats__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁget_stats__mutmut['xǁAgentMemoryǁget_stats__mutmut_4'] = AgentMemory.xǁAgentMemoryǁget_stats__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁget_stats__mutmut['xǁAgentMemoryǁget_stats__mutmut_5'] = AgentMemory.xǁAgentMemoryǁget_stats__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁget_stats__mutmut['xǁAgentMemoryǁget_stats__mutmut_6'] = AgentMemory.xǁAgentMemoryǁget_stats__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁget_stats__mutmut['xǁAgentMemoryǁget_stats__mutmut_7'] = AgentMemory.xǁAgentMemoryǁget_stats__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁget_stats__mutmut['xǁAgentMemoryǁget_stats__mutmut_8'] = AgentMemory.xǁAgentMemoryǁget_stats__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁget_stats__mutmut['xǁAgentMemoryǁget_stats__mutmut_9'] = AgentMemory.xǁAgentMemoryǁget_stats__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁget_stats__mutmut['xǁAgentMemoryǁget_stats__mutmut_10'] = AgentMemory.xǁAgentMemoryǁget_stats__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁget_stats__mutmut['xǁAgentMemoryǁget_stats__mutmut_11'] = AgentMemory.xǁAgentMemoryǁget_stats__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁget_stats__mutmut['xǁAgentMemoryǁget_stats__mutmut_12'] = AgentMemory.xǁAgentMemoryǁget_stats__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁget_stats__mutmut['xǁAgentMemoryǁget_stats__mutmut_13'] = AgentMemory.xǁAgentMemoryǁget_stats__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁget_stats__mutmut['xǁAgentMemoryǁget_stats__mutmut_14'] = AgentMemory.xǁAgentMemoryǁget_stats__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁget_stats__mutmut['xǁAgentMemoryǁget_stats__mutmut_15'] = AgentMemory.xǁAgentMemoryǁget_stats__mutmut_15 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁget_stats__mutmut['xǁAgentMemoryǁget_stats__mutmut_16'] = AgentMemory.xǁAgentMemoryǁget_stats__mutmut_16 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁget_stats__mutmut['xǁAgentMemoryǁget_stats__mutmut_17'] = AgentMemory.xǁAgentMemoryǁget_stats__mutmut_17 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁget_stats__mutmut['xǁAgentMemoryǁget_stats__mutmut_18'] = AgentMemory.xǁAgentMemoryǁget_stats__mutmut_18 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁget_stats__mutmut['xǁAgentMemoryǁget_stats__mutmut_19'] = AgentMemory.xǁAgentMemoryǁget_stats__mutmut_19 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁget_stats__mutmut['xǁAgentMemoryǁget_stats__mutmut_20'] = AgentMemory.xǁAgentMemoryǁget_stats__mutmut_20 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁget_stats__mutmut['xǁAgentMemoryǁget_stats__mutmut_21'] = AgentMemory.xǁAgentMemoryǁget_stats__mutmut_21 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁget_stats__mutmut['xǁAgentMemoryǁget_stats__mutmut_22'] = AgentMemory.xǁAgentMemoryǁget_stats__mutmut_22 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁget_stats__mutmut['xǁAgentMemoryǁget_stats__mutmut_23'] = AgentMemory.xǁAgentMemoryǁget_stats__mutmut_23 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁget_stats__mutmut['xǁAgentMemoryǁget_stats__mutmut_24'] = AgentMemory.xǁAgentMemoryǁget_stats__mutmut_24 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁget_stats__mutmut['xǁAgentMemoryǁget_stats__mutmut_25'] = AgentMemory.xǁAgentMemoryǁget_stats__mutmut_25 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁget_stats__mutmut['xǁAgentMemoryǁget_stats__mutmut_26'] = AgentMemory.xǁAgentMemoryǁget_stats__mutmut_26 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁget_stats__mutmut['xǁAgentMemoryǁget_stats__mutmut_27'] = AgentMemory.xǁAgentMemoryǁget_stats__mutmut_27 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁget_stats__mutmut['xǁAgentMemoryǁget_stats__mutmut_28'] = AgentMemory.xǁAgentMemoryǁget_stats__mutmut_28 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁget_stats__mutmut['xǁAgentMemoryǁget_stats__mutmut_29'] = AgentMemory.xǁAgentMemoryǁget_stats__mutmut_29 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁget_stats__mutmut['xǁAgentMemoryǁget_stats__mutmut_30'] = AgentMemory.xǁAgentMemoryǁget_stats__mutmut_30 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁget_stats__mutmut['xǁAgentMemoryǁget_stats__mutmut_31'] = AgentMemory.xǁAgentMemoryǁget_stats__mutmut_31 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁget_stats__mutmut['xǁAgentMemoryǁget_stats__mutmut_32'] = AgentMemory.xǁAgentMemoryǁget_stats__mutmut_32 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁget_stats__mutmut['xǁAgentMemoryǁget_stats__mutmut_33'] = AgentMemory.xǁAgentMemoryǁget_stats__mutmut_33 # type: ignore # mutmut generated

mutants_xǁAgentMemoryǁclose__mutmut['_mutmut_orig'] = AgentMemory.xǁAgentMemoryǁclose__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁclose__mutmut['xǁAgentMemoryǁclose__mutmut_1'] = AgentMemory.xǁAgentMemoryǁclose__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAgentMemoryǁclose__mutmut['xǁAgentMemoryǁclose__mutmut_2'] = AgentMemory.xǁAgentMemoryǁclose__mutmut_2 # type: ignore # mutmut generated
