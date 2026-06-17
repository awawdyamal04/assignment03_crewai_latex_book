"""Validate a Markdown draft for the required structural placeholders.

This check is purely offline: it reads a Markdown file (or string) and
confirms the template skeleton is present. It never contacts an LLM and
never inspects a PDF — it only verifies that the *draft* contains every
section/placeholder the later phases will fill in with real content.
"""

from __future__ import annotations

from pathlib import Path

# Minimum number of chapter-level sections required by F4 (>= 6 chapters).
MIN_CHAPTERS = 6

# Marker emitted directly under every chapter heading by the pipeline.
CHAPTER_MARKER = "<!-- CHAPTER -->"

# Human-readable requirement name -> literal token that must appear in the
# draft. The markdown pipeline embeds exactly these tokens, so the two modules
# stay in lock-step.
REQUIRED_MARKERS: dict[str, str] = {
    "abstract": "## Abstract",
    "bilingual section placeholder": "<!-- BILINGUAL-PLACEHOLDER -->",
    "table placeholder": "<!-- TABLE-PLACEHOLDER -->",
    "formula placeholder": "<!-- FORMULA-PLACEHOLDER -->",
    "graph placeholder": "<!-- GRAPH-PLACEHOLDER -->",
    "references placeholder": "<!-- REFERENCES-PLACEHOLDER -->",
}


def count_chapters(text: str) -> int:
    """Count chapter-level sections via the embedded chapter marker."""
    return text.count(CHAPTER_MARKER)


def validate_text(text: str) -> list[str]:
    """Return a list of human-readable problems; empty means valid."""
    errors: list[str] = []
    for name, token in REQUIRED_MARKERS.items():
        if token not in text:
            errors.append(f"missing {name} (expected token {token!r})")

    chapters = count_chapters(text)
    if chapters < MIN_CHAPTERS:
        errors.append(
            f"only {chapters} chapter(s) found; need at least {MIN_CHAPTERS} "
            f"(expected {CHAPTER_MARKER!r} under each chapter heading)"
        )
    return errors


def validate_file(path: Path) -> list[str]:
    """Validate a Markdown file on disk, reporting if it is missing."""
    if not path.exists():
        return [f"file not found: {path}"]
    return validate_text(path.read_text(encoding="utf-8"))
