"""Central configuration: paths, model settings, and safe env access.

No secrets live here. API keys are read from the environment (loaded from a
git-ignored `.env`). Importing this module never contacts an external service.
"""

from __future__ import annotations

import os
from pathlib import Path

try:  # python-dotenv is optional at import time; degrade gracefully.
    from dotenv import load_dotenv

    load_dotenv()
except Exception:  # pragma: no cover - dotenv missing is non-fatal
    pass

# ── Project paths ───────────────────────────────────────────────────────────
ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT / "content"
LATEX_DIR = ROOT / "latex"
FIGURES_DIR = ROOT / "figures"
RESULTS_DIR = ROOT / "results"
PROMPTS_DIR = ROOT / "prompts"

OUTPUT_DIRS = (CONTENT_DIR, LATEX_DIR, FIGURES_DIR, RESULTS_DIR, PROMPTS_DIR)

# Canonical artifact paths produced by each task (relative to ROOT).
ARTIFACTS = {
    "research": CONTENT_DIR / "research.md",
    "course": CONTENT_DIR / "course_alignment.md",
    "writing": CONTENT_DIR / "draft.md",
    "bilingual": CONTENT_DIR / "bilingual.md",
    "visualization": FIGURES_DIR / "plot.py",
    "table_formula": CONTENT_DIR / "tables_formulas.md",
    "review": CONTENT_DIR / "reviewed.md",
    "latex": LATEX_DIR / "main.tex",
    "validation": RESULTS_DIR / "validation.md",
}

# ── Model configuration ─────────────────────────────────────────────────────
# CrewAI reads provider keys from the environment. The model name is
# configurable so no provider-specific value is hard-coded.
DEFAULT_MODEL = os.getenv("OPENAI_MODEL_NAME", "gpt-4o-mini")


def ensure_output_dirs() -> None:
    """Create every output directory if it does not already exist."""
    for directory in OUTPUT_DIRS:
        directory.mkdir(parents=True, exist_ok=True)


def get_api_key(name: str, *, required: bool = False) -> str | None:
    """Return an API key from the environment.

    With ``required=True`` a clear error is raised when the key is absent,
    so failures surface early instead of midway through an LLM call.
    """
    value = os.getenv(name)
    if required and not value:
        raise RuntimeError(
            f"Missing required environment variable {name!r}. "
            f"Copy .env.example to .env and fill it in."
        )
    return value


def rel(path: Path) -> str:
    """Render a path relative to the project root for tidy printing."""
    try:
        return str(path.relative_to(ROOT))
    except ValueError:  # pragma: no cover - path outside root
        return str(path)
