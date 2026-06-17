"""Specifications for the nine CrewAI tasks and their context wiring.

Specs are plain data (no CrewAI import). Each task names its predecessor
task(s) via ``context_keys``, implementing sequential context passing.
``build_tasks`` turns the specs into real ``crewai.Task`` objects.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from src.config import ARTIFACTS, rel


@dataclass(frozen=True)
class TaskSpec:
    """Declarative description of one task in the sequential pipeline."""

    key: str
    agent_key: str
    description: str
    expected_output: str
    context_keys: list[str] = field(default_factory=list)


# Ordered to match the sequential process. ``context_keys`` may only point to
# tasks that appear earlier in this list (verified by the validators).
TASK_SPECS: list[TaskSpec] = [
    TaskSpec(
        key="research",
        agent_key="researcher",
        description="Research cyberbullying, online harm, and proportional "
        "legal responses. Collect at least six real, credible sources.",
        expected_output="Markdown notes with key facts and a list of reference "
        "candidates including authors, titles, and years.",
    ),
    TaskSpec(
        key="course",
        agent_key="course_analyst",
        description="Align the research with course 203.3763 concepts and draft "
        "a chapter outline covering all six required topics.",
        expected_output="A concept-alignment note plus an ordered chapter outline.",
        context_keys=["research"],
    ),
    TaskSpec(
        key="writing",
        agent_key="writer",
        description="Write the full English article body in Markdown following "
        "the outline, with at least six chapters.",
        expected_output="A complete Markdown draft long enough for ~15 pages.",
        context_keys=["research", "course"],
    ),
    TaskSpec(
        key="bilingual",
        agent_key="bilingual",
        description="Produce one chapter that correctly mixes Hebrew and English "
        "with proper BiDi handling.",
        expected_output="A Markdown chapter with meaningful Hebrew and English text.",
        context_keys=["writing"],
    ),
    TaskSpec(
        key="visualization",
        agent_key="visualization",
        description="Write a matplotlib script that generates one relevant figure "
        "for the article (labelled axes, title, legend).",
        expected_output="A runnable Python script that saves a print-quality PNG.",
        context_keys=["writing"],
    ),
    TaskSpec(
        key="table_formula",
        agent_key="table_formula",
        description="Specify one formatted table (responses to cyberbullying) "
        "and one conceptual harm-risk formula for inclusion in the article.",
        expected_output="Markdown with one table and one conceptual LaTeX formula.",
        context_keys=["writing"],
    ),
    TaskSpec(
        key="review",
        agent_key="reviewer",
        description="Review the draft, bilingual chapter, and table/formula for "
        "accuracy, structure, and coherence; return a corrected manuscript.",
        expected_output="An approved Markdown manuscript plus review notes.",
        context_keys=["writing", "bilingual", "table_formula"],
    ),
    TaskSpec(
        key="latex",
        agent_key="latex_converter",
        description="Convert the approved manuscript into one valid LuaLaTeX "
        "document that assembles figure, table, formula, and citations.",
        expected_output="A compilable main.tex with preamble, body, and bibliography.",
        context_keys=["review", "bilingual", "visualization", "table_formula"],
    ),
    TaskSpec(
        key="validation",
        agent_key="pdf_validation",
        description="Check the assembled document against acceptance criteria "
        "F1–F13 and report honest pass/fail status.",
        expected_output="A Markdown report listing each F1–F13 item and its status.",
        context_keys=["latex"],
    ),
]

TASKS_BY_KEY: dict[str, TaskSpec] = {spec.key: spec for spec in TASK_SPECS}


def output_file(key: str) -> str:
    """Relative artifact path a task writes to (for display and wiring)."""
    return rel(ARTIFACTS[key])


def build_tasks(agents: dict[str, object]) -> dict[str, object]:
    """Construct real ``crewai.Task`` objects with context passing.

    Imported lazily so the data-only CLI modes never require CrewAI.
    """
    from crewai import Task

    tasks: dict[str, object] = {}
    for spec in TASK_SPECS:
        tasks[spec.key] = Task(
            description=spec.description,
            expected_output=spec.expected_output,
            agent=agents[spec.agent_key],
            context=[tasks[k] for k in spec.context_keys],
            output_file=str(ARTIFACTS[spec.key]),
        )
    return tasks
