"""Assemble the structured Markdown skeleton for the article (Phase 3).

This is the safe, offline content stage: it writes ``content/draft.md`` and
``content/final_article.md`` as clearly-marked DRAFT/TEMPLATE files. It does
NOT call any LLM, fabricate research, invent citations, or build a PDF — it
only lays out the section structure the CrewAI agents later fill in.
"""

from __future__ import annotations

from pathlib import Path

from src.config import ARTIFACTS, CONTENT_DIR, ensure_output_dirs, rel
from src.pipeline import sections as S
from src.pipeline.content_validator import validate_file

# Target files this stage produces (draft.md is also the Writer's artifact).
DRAFT_PATH: Path = ARTIFACTS["writing"]
FINAL_PATH: Path = CONTENT_DIR / "final_article.md"


def build_document(target_name: str) -> str:
    """Return the full Markdown skeleton as a single string.

    ``target_name`` only labels the file in its header note; the structure
    is identical for the draft and the assembled-template file.
    """
    note = (
        f"<!-- file: {target_name} — offline template, no LLM, no real data -->"
    )
    parts = [
        note,
        S.BANNER,
        S.FRONT_MATTER,
        S.ABSTRACT,
        *S.CHAPTERS,
        S.REFERENCES,
    ]
    return "\n\n".join(part.strip("\n") for part in parts) + "\n"


def write_markdown(*, overwrite: bool = True) -> list[Path]:
    """Write the draft and final-article templates to ``content/``.

    Returns the list of paths written. Existing files are only replaced when
    ``overwrite`` is true, so a real generated draft is never clobbered by
    accident.
    """
    ensure_output_dirs()
    written: list[Path] = []
    for path in (DRAFT_PATH, FINAL_PATH):
        if path.exists() and not overwrite:
            continue
        path.write_text(build_document(path.name), encoding="utf-8")
        written.append(path)
    return written


def draft_markdown() -> int:
    """CLI handler for ``--mode draft-markdown``. Returns an exit code."""
    print("DRAFT MARKDOWN — writing offline template skeleton (no LLM)\n")
    written = write_markdown(overwrite=True)
    for path in (DRAFT_PATH, FINAL_PATH):
        status = "written" if path in written else "skipped (exists)"
        print(f"  {status}: {rel(path)}")
    print(
        "\nThese are DRAFT/TEMPLATE files with TODO placeholders — not final\n"
        "research. Run `--mode validate-content` to check their structure."
    )
    return 0


def validate_content() -> int:
    """CLI handler for ``--mode validate-content``. Returns an exit code."""
    print("VALIDATE CONTENT — checking Markdown draft structure (offline)\n")
    total = 0
    for path in (DRAFT_PATH, FINAL_PATH):
        errors = validate_file(path)
        total += len(errors)
        if errors:
            print(f"  [FAIL] {rel(path)}")
            for err in errors:
                print(f"         - {err}")
        else:
            print(f"  [ OK ] {rel(path)}")

    if total:
        print(
            f"\nFound {total} issue(s). Run `--mode draft-markdown` first, or "
            "ensure each required section/placeholder is present."
        )
        return 1
    print("\nValidation passed: all required sections and placeholders present.")
    return 0
