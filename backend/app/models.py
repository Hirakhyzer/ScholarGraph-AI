"""Pydantic models for ScholarGraph AI."""

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class PaperInput(BaseModel):
    """Input format for a paper-level analysis request."""

    title: str = Field(..., min_length=3, description="Paper title")
    abstract: str = Field(..., min_length=20, description="Paper abstract or summary")
    keywords: List[str] = Field(default_factory=list, description="User-provided keywords")
    authors: List[str] = Field(default_factory=list, description="Optional author names")
    year: Optional[int] = Field(default=None, description="Publication year")
    venue: Optional[str] = Field(default=None, description="Journal, conference, or workshop")


class PaperAnalysis(BaseModel):
    """Structured analysis returned by the research intelligence pipeline."""

    paper_id: str
    title: str
    themes: List[str]
    methodology_signals: List[str]
    possible_gaps: List[str]
    recommended_research_questions: List[str]
    thesis_relevance_score: float = Field(..., ge=0, le=1)


class GraphNode(BaseModel):
    id: str
    label: str
    type: str


class GraphEdge(BaseModel):
    source: str
    target: str
    relation: str


class KnowledgeGraph(BaseModel):
    nodes: List[GraphNode]
    edges: List[GraphEdge]


class LiteratureMatrixRow(BaseModel):
    paper: str
    problem: str
    method: str
    dataset: str
    finding: str
    limitation: str
    possible_gap: str
