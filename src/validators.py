"""Structural validators used by the dry-run mode.

These checks verify the pipeline's shape without contacting any LLM:
agent/task references resolve, context only points backward (sequential
safety), every task has an artifact path, and every Python file obeys the
150-line limit.
"""

from __future__ import annotations

from pathlib import Path

from src.agents.definitions import AGENTS_BY_KEY
from src.config import ARTIFACTS, ROOT
from src.tasks.definitions import TASK_SPECS

MAX_LINES = 150


def check_agent_references() -> list[str]:
    """Every task must point at a defined agent."""
    errors = []
    for spec in TASK_SPECS:
        if spec.agent_key not in AGENTS_BY_KEY:
            errors.append(f"task {spec.key!r} -> unknown agent {spec.agent_key!r}")
    return errors


def check_sequential_context() -> list[str]:
    """Context may only reference tasks defined earlier (no forward/cyclic deps)."""
    errors = []
    seen: set[str] = set()
    for spec in TASK_SPECS:
        for ctx in spec.context_keys:
            if ctx not in seen:
                errors.append(
                    f"task {spec.key!r} depends on {ctx!r} which is not an "
                    f"earlier task"
                )
        seen.add(spec.key)
    return errors


def check_artifacts() -> list[str]:
    """Every task must map to a known output artifact path."""
    return [
        f"task {spec.key!r} has no artifact path"
        for spec in TASK_SPECS
        if spec.key not in ARTIFACTS
    ]


def check_line_limits(root: Path | None = None) -> list[str]:
    """Report any Python file in ``src/`` at or above the line limit."""
    base = (root or ROOT) / "src"
    errors = []
    for path in sorted(base.rglob("*.py")):
        lines = path.read_text(encoding="utf-8").splitlines()
        if len(lines) >= MAX_LINES:
            errors.append(f"{path.relative_to(ROOT)} has {len(lines)} lines (>= {MAX_LINES})")
    return errors


def run_all_checks() -> dict[str, list[str]]:
    """Run every structural check; empty lists mean the check passed."""
    return {
        "agent_references": check_agent_references(),
        "sequential_context": check_sequential_context(),
        "artifacts": check_artifacts(),
        "line_limits": check_line_limits(),
    }
