"""Research gap detection heuristics for the ScholarGraph AI prototype."""

from __future__ import annotations

from typing import List

GAP_RULES = {
    "small sample": "Potential limitation: small sample size may reduce generalizability.",
    "limited dataset": "Potential limitation: dataset coverage appears limited.",
    "single dataset": "Potential gap: evaluation on multiple datasets may be needed.",
    "future work": "The abstract mentions future work, which may indicate an unresolved direction.",
    "limitation": "The paper explicitly signals limitations that should be inspected.",
    "english": "Possible gap: multilingual or cross-cultural evaluation may be underexplored.",
    "benchmark": "Possible gap: benchmark dependence may limit real-world validity.",
    "explainability": "Possible gap: human-centered explanation evaluation may be needed.",
    "privacy": "Possible gap: privacy, governance, and ethical risk analysis may be needed.",
    "bias": "Possible gap: fairness and bias evaluation may require deeper study.",
}

DEFAULT_GAPS = [
    "Compare the proposed approach across more diverse datasets or domains.",
    "Investigate external validity beyond the original experimental setting.",
    "Add reproducibility evidence, ablation studies, or transparent evaluation protocols.",
]


def detect_gap_signals(title: str, abstract: str, keywords: List[str]) -> List[str]:
    """Return transparent candidate gap signals based on text patterns."""

    text = f"{title} {abstract} {' '.join(keywords)}".lower()
    gaps = [message for trigger, message in GAP_RULES.items() if trigger in text]
    return gaps or DEFAULT_GAPS


def generate_research_questions(themes: List[str], gaps: List[str]) -> List[str]:
    """Generate defensible research-question templates from themes and gaps."""

    primary_theme = themes[0] if themes else "the selected research domain"
    questions = [
        f"How can {primary_theme} be improved through more transparent and reproducible evaluation?",
        f"What methodological limitations currently restrict progress in {primary_theme}?",
        f"How can evidence from existing studies be synthesized into a reliable research agenda for {primary_theme}?",
    ]
    if gaps:
        questions.append(f"To what extent does this gap affect the validity of current findings: {gaps[0]}")
    return questions[:4]


def thesis_relevance_score(themes: List[str], gaps: List[str], methodology_signals: List[str]) -> float:
    """Score whether the paper appears useful for thesis-level planning."""

    score = 0.25
    score += min(len(themes), 6) * 0.06
    score += min(len(gaps), 4) * 0.08
    score += min(len(methodology_signals), 3) * 0.05
    return round(min(score, 1.0), 2)
