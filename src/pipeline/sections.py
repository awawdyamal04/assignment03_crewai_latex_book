"""Template Markdown sections for the article skeleton (Phase 3).

Every string here is an explicit DRAFT/TEMPLATE placeholder, not real
research. The later CrewAI agents (Writer, Bilingual, Table/Formula,
Visualization) replace each ``TODO`` block with sourced content. Embedded
HTML-comment markers are what ``content_validator`` checks for, so the
two modules stay in sync.
"""

from __future__ import annotations

from src.pipeline.content_validator import CHAPTER_MARKER, REQUIRED_MARKERS

BANNER = (
    "<!-- DRAFT / TEMPLATE — NOT FINAL RESEARCH -->\n"
    "> **DRAFT TEMPLATE.** This file is a structural placeholder generated\n"
    "> offline by the content pipeline. No LLM was called and no sources were\n"
    "> consulted. Every section below is filled with `TODO` markers that the\n"
    "> CrewAI agents replace with real, cited content in a later phase.\n"
)

FRONT_MATTER = (
    "<!-- TITLE-PAGE-PLACEHOLDER -->\n"
    "# From RNN and LSTM to Transformers and AI Agents\n"
    "## *How Modern AI Systems Generate Knowledge*\n\n"
    "| Field | Value |\n"
    "|-------|-------|\n"
    "| Course | 203.3763 — Orchestration of AI Agents |\n"
    "| Lecturer | TODO: lecturer name |\n"
    "| Student | TODO: student name |\n"
    "| Date | TODO: submission date |\n"
)

ABSTRACT = (
    f"{REQUIRED_MARKERS['abstract']}\n\n"
    "TODO: A short English abstract (~150 words) summarising the article's\n"
    "argument — the path from recurrent models to attention-based\n"
    "Transformers and multi-agent systems. Placeholder only; written by the\n"
    "Writer agent.\n"
)


def _chapter(number: int, title: str, body: str) -> str:
    """Render a chapter heading + the marker the validator counts."""
    return f"## {number}. {title}\n{CHAPTER_MARKER}\n\n{body}\n"


CHAPTERS: list[str] = [
    _chapter(1, "Introduction",
        "TODO: Motivate sequence modelling and outline the article."),
    _chapter(2, "Recurrent Neural Networks (RNNs)",
        "TODO: Why sequential models were needed; the RNN recurrence and its\n"
        "limits (vanishing / exploding gradients)."),
    _chapter(3, "Long Short-Term Memory (LSTM)",
        "TODO: How gating and the cell state address long-term dependencies."),
    _chapter(4, "Transformers and Attention",
        "TODO: Why attention replaced much of the recurrent approach; the\n"
        "notion of context. See the formula in the integration section."),
    _chapter(5, "AI Agents and CrewAI",
        "TODO: From attention/context to agentic systems; how CrewAI\n"
        "orchestrates cooperating agents like a small organisation."),
    _chapter(6, "Bilingual Chapter — Hebrew and English (BiDi)",
        f"{REQUIRED_MARKERS['bilingual section placeholder']}\n"
        "TODO: One chapter mixing Hebrew (RTL) and English (LTR) with correct\n"
        "bidirectional handling. Placeholder; produced by the Bilingual agent."),
    _chapter(7, "Tables, Formulas and Generated Graphs",
        "Integration points the typesetting phase wires into LuaLaTeX.\n\n"
        f"{REQUIRED_MARKERS['table placeholder']}\n"
        "TODO: one formatted table (Table & Formula agent).\n\n"
        f"{REQUIRED_MARKERS['formula placeholder']}\n"
        "TODO: one complex formula — scaled dot-product attention.\n\n"
        f"{REQUIRED_MARKERS['graph placeholder']}\n"
        "TODO: one Python-generated figure (Visualization agent)."),
    _chapter(8, "Conclusion",
        "TODO: Recap the evolution and the role of agent orchestration."),
]

REFERENCES = (
    "## References\n"
    f"{REQUIRED_MARKERS['references placeholder']}\n\n"
    "TODO: At least six real, citable sources are added during the research\n"
    "and LaTeX phases (BibTeX / biber). No citations are invented here.\n"
)
