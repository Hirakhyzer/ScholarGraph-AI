"""Knowledge graph construction helpers for ScholarGraph AI."""

from __future__ import annotations

from typing import List

from app.models import GraphEdge, GraphNode, KnowledgeGraph, PaperInput


def build_sample_graph() -> KnowledgeGraph:
    """Return a curated graph for frontend demos and documentation."""

    nodes = [
        GraphNode(id="p1", label="Paper: Literature AI", type="paper"),
        GraphNode(id="t1", label="Topic: Knowledge Graphs", type="topic"),
        GraphNode(id="m1", label="Method: NLP Pipeline", type="method"),
        GraphNode(id="d1", label="Dataset: Research PDFs", type="dataset"),
        GraphNode(id="g1", label="Gap: Explainability", type="gap"),
        GraphNode(id="q1", label="RQ: Transparent Review AI", type="question"),
    ]
    edges = [
        GraphEdge(source="p1", target="t1", relation="addresses"),
        GraphEdge(source="p1", target="m1", relation="uses"),
        GraphEdge(source="p1", target="d1", relation="evaluates_on"),
        GraphEdge(source="p1", target="g1", relation="reveals"),
        GraphEdge(source="g1", target="q1", relation="motivates"),
    ]
    return KnowledgeGraph(nodes=nodes, edges=edges)


def build_paper_graph(paper: PaperInput, themes: List[str], gaps: List[str]) -> KnowledgeGraph:
    """Create a lightweight paper-centered graph from analysis results."""

    paper_id = "paper"
    nodes = [GraphNode(id=paper_id, label=paper.title, type="paper")]
    edges: list[GraphEdge] = []

    for index, theme in enumerate(themes[:5], start=1):
        node_id = f"theme_{index}"
        nodes.append(GraphNode(id=node_id, label=theme.title(), type="topic"))
        edges.append(GraphEdge(source=paper_id, target=node_id, relation="has_theme"))

    for index, gap in enumerate(gaps[:3], start=1):
        node_id = f"gap_{index}"
        nodes.append(GraphNode(id=node_id, label=gap, type="gap"))
        edges.append(GraphEdge(source=paper_id, target=node_id, relation="suggests_gap"))

    return KnowledgeGraph(nodes=nodes, edges=edges)
