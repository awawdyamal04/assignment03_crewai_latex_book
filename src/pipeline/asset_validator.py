"""Validate the Phase 4 technical assets (offline, no LLM, no PDF build).

Confirms that the conceptual figure and the table/formula Markdown exist
and contain the required course-aligned tokens, and asserts that no final
PDF has been produced yet (Phase 4 must not build the PDF).
"""

from __future__ import annotations

from pathlib import Path

from src.config import RESULTS_DIR, rel
from src.pipeline.graph_generator import FIGURE_PATH
from src.pipeline.technical_assets import ASSET_PATH

# Tokens the responses comparison table must mention.
TABLE_TOKENS = ("Education", "School", "Platform", "legal")
# Tokens the conceptual harm-risk formula / asset must contain.
FORMULA_TOKENS = ("R", "frequency", "severity", "duration", "audience")


def check_figure() -> list[str]:
    """The conceptual PNG must exist and be non-empty."""
    if not FIGURE_PATH.exists():
        return [f"figure not found: {rel(FIGURE_PATH)} (run generate-assets)"]
    if FIGURE_PATH.stat().st_size == 0:
        return [f"figure is empty: {rel(FIGURE_PATH)}"]
    return []


def check_assets_file() -> list[str]:
    """The table/formula Markdown must exist with all required tokens."""
    if not ASSET_PATH.exists():
        return [f"assets file not found: {rel(ASSET_PATH)} (run generate-assets)"]

    text = ASSET_PATH.read_text(encoding="utf-8")
    errors: list[str] = []

    for token in TABLE_TOKENS:
        if token not in text:
            errors.append(f"table missing required term {token!r}")

    # The formula is written in LaTeX (\sqrt, \operatorname{softmax}); accept
    # the plain-text mirror too so the check is robust to notation.
    lowered = text.lower()
    for token in FORMULA_TOKENS:
        if token.lower() not in lowered:
            errors.append(f"formula missing required token {token!r}")

    return errors


def check_no_pdf() -> list[str]:
    """Phase 4 must not create a final PDF anywhere in results/."""
    if not RESULTS_DIR.exists():
        return []
    pdfs = sorted(RESULTS_DIR.rglob("*.pdf"))
    return [f"unexpected PDF present in Phase 4: {rel(p)}" for p in pdfs]


def run_asset_checks() -> dict[str, list[str]]:
    """Run every asset check; empty lists mean the check passed."""
    return {
        "figure_exists": check_figure(),
        "assets_file": check_assets_file(),
        "no_final_pdf": check_no_pdf(),
    }


def validate_assets() -> int:
    """CLI helper for ``--mode validate-assets``. Returns an exit code."""
    print("VALIDATE ASSETS — checking Phase 4 technical assets (offline)\n")
    results = run_asset_checks()
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
        print(f"\nValidation found {failures} issue(s).")
        return 1
    print("\nValidation passed: assets present, complete, and no PDF built.")
    return 0


if __name__ == "__main__":  # pragma: no cover - convenience entry point
    raise SystemExit(validate_assets())
