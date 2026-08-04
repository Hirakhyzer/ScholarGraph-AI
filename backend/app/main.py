"""ScholarGraph AI FastAPI application."""

from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.models import LiteratureMatrixRow, PaperAnalysis, PaperInput
from app.services.gap_detector import (
    detect_gap_signals,
    generate_research_questions,
    thesis_relevance_score,
)
from app.services.graph_builder import build_sample_graph
from app.services.paper_parser import (
    detect_methodology_signals,
    extract_candidate_themes,
    stable_paper_id,
)

app = FastAPI(
    title="ScholarGraph AI API",
    description="Research intelligence API for literature review mapping and gap analysis.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root() -> dict[str, str]:
    """Health check endpoint."""

    return {
        "name": "ScholarGraph AI",
        "status": "research prototype",
        "message": "Turn scattered papers into structured research intelligence.",
    }


@app.post("/analyze/paper", response_model=PaperAnalysis)
def analyze_paper(paper: PaperInput) -> PaperAnalysis:
    """Analyze one paper and return structured research intelligence."""

    themes = extract_candidate_themes(paper.title, paper.abstract, paper.keywords)
    methodology_signals = detect_methodology_signals(f"{paper.title} {paper.abstract}")
    gaps = detect_gap_signals(paper.title, paper.abstract, paper.keywords)
    questions = generate_research_questions(themes, gaps)
    score = thesis_relevance_score(themes, gaps, methodology_signals)

    return PaperAnalysis(
        paper_id=stable_paper_id(paper.title),
        title=paper.title,
        themes=themes,
        methodology_signals=methodology_signals,
        possible_gaps=gaps,
        recommended_research_questions=questions,
        thesis_relevance_score=score,
    )


@app.get("/graph/sample")
def sample_graph():
    """Return a sample knowledge graph."""

    return build_sample_graph()


@app.get("/matrix/sample", response_model=list[LiteratureMatrixRow])
def sample_matrix() -> list[LiteratureMatrixRow]:
    """Return a sample literature review matrix."""

    return [
        LiteratureMatrixRow(
            paper="Explainable AI for Literature Review",
            problem="Researchers need transparent support for reviewing large paper collections.",
            method="Knowledge graph with NLP extraction pipeline",
            dataset="Research article abstracts and metadata",
            finding="Graph-based organization improves visibility of themes and limitations.",
            limitation="Human evaluation protocol remains underdeveloped.",
            possible_gap="Need for supervisor-centered validation of AI literature review tools.",
        ),
        LiteratureMatrixRow(
            paper="Graph Mining for Research Discovery",
            problem="Connections between papers and methods are difficult to inspect manually.",
            method="Network analysis and clustering",
            dataset="Citation and keyword network",
            finding="Topic clusters reveal emerging research directions.",
            limitation="Citation networks may overrepresent highly cited papers.",
            possible_gap="Need to combine citation signals with content-level evidence.",
        ),
    ]
