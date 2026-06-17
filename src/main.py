"""CLI entry point for the CrewAI pipeline (Phase 2 skeleton).

Safe, offline modes only — none of these contacts an LLM:

    python -m src.main --mode show-agents
    python -m src.main --mode show-tasks
    python -m src.main --mode dry-run
    python -m src.main --mode draft-markdown
    python -m src.main --mode validate-content
    python -m src.main --mode generate-assets
    python -m src.main --mode validate-assets

``dry-run`` prints the planned sequential pipeline and runs structural
checks. ``draft-markdown`` writes the offline Markdown template skeleton
(``content/draft.md`` + ``content/final_article.md``) and
``validate-content`` checks that skeleton. ``generate-assets`` renders the
conceptual graph (``figures/complexity_comparison.png``) and the
table/formula Markdown (``content/tables_formulas.md``); ``validate-assets``
checks those technical assets. The real ``crew.kickoff()`` run is wired in a
later phase.
"""

from __future__ import annotations

import argparse
import sys

try:  # Ensure Unicode (em-dash, Hebrew, F1–F13) prints cleanly on Windows.
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:  # pragma: no cover - older interpreters
    pass

from src.agents.definitions import AGENT_SPECS
from src.pipeline.asset_validator import validate_assets
from src.pipeline.markdown_pipeline import draft_markdown, validate_content
from src.tasks.definitions import TASK_SPECS, output_file
from src.validators import run_all_checks


def generate_assets() -> int:
    """Build the conceptual graph and the table/formula Markdown asset."""
    from src.pipeline.graph_generator import generate_graph
    from src.pipeline.technical_assets import generate_assets as write_assets

    rc = generate_graph()
    print()
    rc |= write_assets()
    return rc


def show_agents() -> None:
    print(f"Planned agents ({len(AGENT_SPECS)}):\n")
    for i, spec in enumerate(AGENT_SPECS, 1):
        tools = ", ".join(spec.tools) or "(none)"
        print(f"{i}. {spec.role}  [key={spec.key}]")
        print(f"   goal     : {spec.goal}")
        print(f"   backstory: {spec.backstory}")
        print(f"   tools    : {tools}\n")


def show_tasks() -> None:
    print(f"Planned tasks ({len(TASK_SPECS)}, sequential):\n")
    for i, spec in enumerate(TASK_SPECS, 1):
        ctx = ", ".join(spec.context_keys) or "(none)"
        print(f"{i}. {spec.key}  [agent={spec.agent_key}]")
        print(f"   description     : {spec.description}")
        print(f"   expected_output : {spec.expected_output}")
        print(f"   context (in)    : {ctx}")
        print(f"   artifact (out)  : {output_file(spec.key)}\n")


def dry_run() -> int:
    print("DRY RUN — planned sequential pipeline (no LLM calls)\n")
    print("Flow:")
    for i, spec in enumerate(TASK_SPECS, 1):
        ctx = " + ".join(spec.context_keys) or "start"
        print(f"  {i}. [{ctx}] -> {spec.key} -> {output_file(spec.key)}")

    print("\nStructural checks:")
    results = run_all_checks()
    failures = 0
    for name, errors in results.items():
        if errors:
            failures += len(errors)
            print(f"  [FAIL] {name}")
            for err in errors:
                print(f"         - {err}")
        else:
            print(f"  [ OK ] {name}")

    if failures:
        print(f"\nDry run found {failures} issue(s).")
        return 1
    print("\nDry run passed: structure is valid. No LLMs were called.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="src.main", description="CrewAI LaTeX-book pipeline (skeleton)."
    )
    parser.add_argument(
        "--mode",
        required=True,
        choices=[
            "show-agents",
            "show-tasks",
            "dry-run",
            "draft-markdown",
            "validate-content",
            "generate-assets",
            "validate-assets",
        ],
        help="Which safe, offline action to run.",
    )
    args = parser.parse_args()

    if args.mode == "show-agents":
        show_agents()
        return 0
    if args.mode == "show-tasks":
        show_tasks()
        return 0
    if args.mode == "draft-markdown":
        return draft_markdown()
    if args.mode == "validate-content":
        return validate_content()
    if args.mode == "generate-assets":
        return generate_assets()
    if args.mode == "validate-assets":
        return validate_assets()
    return dry_run()


if __name__ == "__main__":
    raise SystemExit(main())
