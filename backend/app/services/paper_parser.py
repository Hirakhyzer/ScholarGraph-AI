"""Simple paper parsing utilities.

This module intentionally avoids paid APIs and heavy model dependencies so the
prototype can run immediately after installation. The logic can be replaced by
PDF parsers, embedding models, or LLM-backed extraction later.
"""

from __future__ import annotations

import hashlib
import re
from typing import Iterable, List

ACADEMIC_STOPWORDS = {
    "paper",
    "study",
    "research",
    "method",
    "result",
    "approach",
    "analysis",
    "using",
    "based",
    "system",
    "model",
    "data",
    "results",
    "proposed",
}

METHOD_TERMS = {
    "transformer",
    "bert",
    "llm",
    "knowledge graph",
    "graph neural network",
    "survey",
    "experiment",
    "case study",
    "mixed method",
    "regression",
    "classification",
    "clustering",
    "deep learning",
    "machine learning",
}


def stable_paper_id(title: str) -> str:
    """Create a stable short identifier from a paper title."""

    digest = hashlib.sha1(title.lower().encode("utf-8")).hexdigest()[:10]
    return f"paper_{digest}"


def normalize_terms(terms: Iterable[str]) -> List[str]:
    """Clean and deduplicate user or parser supplied terms."""

    seen: set[str] = set()
    normalized: List[str] = []
    for term in terms:
        clean = re.sub(r"\s+", " ", term.strip().lower())
        if len(clean) < 3 or clean in ACADEMIC_STOPWORDS or clean in seen:
            continue
        seen.add(clean)
        normalized.append(clean)
    return normalized


def extract_candidate_themes(title: str, abstract: str, keywords: List[str]) -> List[str]:
    """Extract lightweight theme candidates from title, abstract, and keywords."""

    keyword_terms = normalize_terms(keywords)
    text = f"{title} {abstract}".lower()
    phrase_candidates = re.findall(r"\b[a-z][a-z\-]+(?:\s+[a-z][a-z\-]+){0,2}\b", text)
    candidates = normalize_terms(keyword_terms + phrase_candidates)
    return candidates[:10]


def detect_methodology_signals(text: str) -> List[str]:
    """Detect methodology terms using a transparent keyword list."""

    lowered = text.lower()
    signals = [term for term in METHOD_TERMS if term in lowered]
    return sorted(signals) or ["methodology not explicit in provided text"]
