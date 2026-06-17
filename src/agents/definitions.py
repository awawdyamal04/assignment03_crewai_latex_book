"""Specifications for the nine CrewAI agents.

The specs are plain data (no CrewAI import), so ``show-agents`` and
``dry-run`` work without any LLM provider or API key. ``build_agents``
turns the specs into real ``crewai.Agent`` objects only when a run needs them.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class AgentSpec:
    """Declarative description of one agent (order matters for the pipeline)."""

    key: str
    role: str
    goal: str
    backstory: str
    tools: list[str] = field(default_factory=list)  # tool names, resolved later


# Ordered list — index reflects sequential execution order.
AGENT_SPECS: list[AgentSpec] = [
    AgentSpec(
        key="researcher",
        role="Researcher",
        goal="Gather accurate, citable facts and real, credible sources on "
        "cyberbullying, online harm, and proportional legal responses.",
        backstory="A meticulous academic researcher who only trusts verifiable, "
        "primary sources and records full citation details.",
        tools=["search"],
    ),
    AgentSpec(
        key="course_analyst",
        role="Course Material Analyst",
        goal="Align gathered research with course 203.3763 concepts and produce "
        "a chapter outline covering all required topics.",
        backstory="A teaching assistant who maps raw material onto the syllabus "
        "so nothing required by the course is missed.",
        tools=["file_read"],
    ),
    AgentSpec(
        key="writer",
        role="Writer",
        goal="Draft a clear, well-structured ~15-page academic article body in "
        "Markdown with at least six chapters.",
        backstory="An experienced academic author who writes in a precise, "
        "formal voice and structures arguments logically.",
    ),
    AgentSpec(
        key="bilingual",
        role="Bilingual Chapter Agent",
        goal="Produce one chapter that correctly mixes Hebrew and English with "
        "proper bidirectional (BiDi) text handling.",
        backstory="A bilingual editor fluent in Hebrew and English who knows how "
        "RTL and LTR text must be interleaved cleanly.",
    ),
    AgentSpec(
        key="visualization",
        role="Python Visualization Agent",
        goal="Write self-contained matplotlib code that generates one relevant, "
        "print-quality figure for the article.",
        backstory="A data-visualization engineer who writes small, runnable "
        "plotting scripts with labelled axes, titles, and legends.",
    ),
    AgentSpec(
        key="table_formula",
        role="Table and Formula Agent",
        goal="Specify one formatted table (responses to cyberbullying) and one "
        "conceptual math formula (a harm-risk score).",
        backstory="A technical typesetter who renders data as clean tables and "
        "transcribes mathematics faithfully.",
    ),
    AgentSpec(
        key="reviewer",
        role="Reviewer",
        goal="Check the manuscript for accuracy, structure, completeness, and "
        "coherence, then return an approved, corrected version.",
        backstory="A demanding peer reviewer who catches inconsistencies and "
        "insists every claim is supported.",
    ),
    AgentSpec(
        key="latex_converter",
        role="LaTeX Converter",
        goal="Convert the approved Markdown manuscript into one valid LuaLaTeX "
        "`.tex` document assembling figures, tables, formulas, and citations.",
        backstory="A LaTeX expert who produces compilable documents with correct "
        "preamble, BiDi support, and bibliography wiring.",
    ),
    AgentSpec(
        key="pdf_validation",
        role="PDF Validation Agent",
        goal="Verify that the compiled PDF satisfies every acceptance criterion "
        "F1–F13 and report honest pass/fail status.",
        backstory="A quality-assurance auditor who never fabricates a passing "
        "result and reports exactly what the artifact contains.",
    ),
]

AGENTS_BY_KEY: dict[str, AgentSpec] = {spec.key: spec for spec in AGENT_SPECS}


def build_agents(tools: dict[str, object] | None = None) -> dict[str, object]:
    """Construct real ``crewai.Agent`` objects from the specs.

    Imported lazily so the data-only CLI modes never require CrewAI.
    ``tools`` maps a tool name (e.g. ``"search"``) to a tool instance.
    """
    from crewai import Agent

    tools = tools or {}
    agents: dict[str, object] = {}
    for spec in AGENT_SPECS:
        resolved = [tools[name] for name in spec.tools if name in tools]
        agents[spec.key] = Agent(
            role=spec.role,
            goal=spec.goal,
            backstory=spec.backstory,
            tools=resolved,
            verbose=True,
            allow_delegation=False,
        )
    return agents
