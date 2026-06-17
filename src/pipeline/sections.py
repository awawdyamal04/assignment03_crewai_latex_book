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
    "# Cyberbullying Should Have Legal Consequences\n"
    "## *A Multi-Agent Academic Analysis Generated with CrewAI and LuaLaTeX*\n\n"
    "| Field | Value |\n"
    "|-------|-------|\n"
    "| Course | 203.3763 — Orchestration of AI Agents |\n"
    "| Lecturer | Dr. Yoram Reuven Segal |\n"
    "| Student | Amal Awawdi |\n"
    "| Date | TODO: submission date |\n"
)

ABSTRACT = (
    f"{REQUIRED_MARKERS['abstract']}\n\n"
    "TODO: A short English abstract (~150 words) summarising the balanced\n"
    "argument — that cyberbullying should carry proportional, evidence-based\n"
    "legal consequences in serious cases, combined with education, school\n"
    "intervention, reporting, and platform responsibility. Placeholder only.\n"
)


def _chapter(number: int, title: str, body: str) -> str:
    """Render a chapter heading + the marker the validator counts."""
    return f"## {number}. {title}\n{CHAPTER_MARKER}\n\n{body}\n"


CHAPTERS: list[str] = [
    _chapter(1, "Introduction",
        "TODO: Motivate the question and state the balanced thesis."),
    _chapter(2, "Definition of Cyberbullying",
        "TODO: Define cyberbullying — intent, repetition, power imbalance,\n"
        "and the digital features that change the harm."),
    _chapter(3, "Why Online Harm Is Real Harm",
        "TODO: Argue that online harm is real harm; introduce the conceptual\n"
        "harm-risk score (frequency, severity, duration, audience)."),
    _chapter(4, "Psychological, Social, and Educational Impact",
        "TODO: Discuss effects carefully and generally; no fabricated stats."),
    _chapter(5, "Why Legal Consequences May Be Necessary",
        "TODO: When repeated, targeted, severe conduct warrants the law."),
    _chapter(6, "Proportionality and Due Process",
        "TODO: Proportionality, due process, and the escalation model."),
    _chapter(7, "Minors, Schools, and Parents",
        "TODO: Age-aware response; the role of schools and parents."),
    _chapter(8, "Platform Responsibility",
        "TODO: Reporting tools, moderation, and design responsibility."),
    _chapter(9, "Evidence, Reporting, and Documentation",
        "TODO: Preserving evidence and clear reporting systems."),
    _chapter(10, "Prevention and Education",
        "TODO: Prevention-first; education and digital-safety habits."),
    _chapter(11, "The CrewAI Production Pipeline Used in This Project",
        "TODO: Explain the nine-agent CrewAI pipeline that produced this\n"
        "document; keep the project methodology visible."),
    _chapter(12, "Bilingual Chapter — Hebrew and English (BiDi)",
        f"{REQUIRED_MARKERS['bilingual section placeholder']}\n"
        "TODO: One chapter mixing Hebrew (RTL) and English (LTR) with correct\n"
        "bidirectional handling. Placeholder; produced by the Bilingual agent."),
    _chapter(13, "Tables, Formulas and Generated Graphs",
        "Integration points the typesetting phase wires into LuaLaTeX.\n\n"
        f"{REQUIRED_MARKERS['table placeholder']}\n"
        "TODO: one formatted table (responses to cyberbullying).\n\n"
        f"{REQUIRED_MARKERS['formula placeholder']}\n"
        "TODO: one conceptual formula — the harm-risk score.\n\n"
        f"{REQUIRED_MARKERS['graph placeholder']}\n"
        "TODO: one Python-generated figure (conceptual escalation model)."),
    _chapter(14, "Conclusion",
        "TODO: Recap the balanced thesis and the role of agent orchestration."),
]

REFERENCES = (
    "## References\n"
    f"{REQUIRED_MARKERS['references placeholder']}\n\n"
    "TODO: At least six real, credible sources are added during the research\n"
    "and LaTeX phases (BibTeX / biber). No citations are invented here.\n"
)
