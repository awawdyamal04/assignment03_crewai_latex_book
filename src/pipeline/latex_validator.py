"""Validate the assembled LaTeX source (Phase 5, offline, no compile).

Confirms ``latex/main.tex`` and ``latex/references.bib`` exist and that the
source contains every required feature token (title page, TOC, image, table,
formula, Hebrew/English BiDi, biblatex/biber, hyperref), and asserts that no
final PDF has been produced yet. This never runs lualatex/biber.
"""

from __future__ import annotations

from src.config import LATEX_DIR, RESULTS_DIR, rel
from src.pipeline.latex_builder import MAIN_TEX_PATH
from src.pipeline.latex_references import REFERENCES_PATH

# Each feature maps to substrings; the feature passes if ANY substring is found.
FEATURE_TOKENS: dict[str, tuple[str, ...]] = {
    "title_page": (r"\begin{titlepage}", "Yoram Reuven Segal"),
    "table_of_contents": (r"\tableofcontents",),
    "image_graph": (r"\includegraphics", "complexity_comparison"),
    "table": (r"\begin{tabular}", r"\toprule"),
    "formula": (r"\operatorname{Attention}", r"\begin{equation}"),
    "hebrew_english_bidi": (r"\begin{hebrew}", r"\texthebrew"),
    "biblatex_biber": ("backend=biber", r"\printbibliography"),
    "hyperref": (r"{hyperref}", r"\href"),
}


def check_files_exist() -> list[str]:
    """main.tex and references.bib must both exist and be non-empty."""
    errors: list[str] = []
    for path in (MAIN_TEX_PATH, REFERENCES_PATH):
        if not path.exists():
            errors.append(f"missing: {rel(path)} (run --mode build-latex)")
        elif path.stat().st_size == 0:
            errors.append(f"empty: {rel(path)}")
    return errors


def check_features() -> dict[str, list[str]]:
    """Confirm each required feature token is present in main.tex."""
    if not MAIN_TEX_PATH.exists():
        return {f: [f"{rel(MAIN_TEX_PATH)} missing"] for f in FEATURE_TOKENS}
    text = MAIN_TEX_PATH.read_text(encoding="utf-8")
    results: dict[str, list[str]] = {}
    for feature, tokens in FEATURE_TOKENS.items():
        ok = any(tok in text for tok in tokens)
        results[feature] = [] if ok else [f"none of {tokens!r} found"]
    return results


def check_no_pdf() -> list[str]:
    """Phase 5 must not create a final PDF (only assembles the source)."""
    errors: list[str] = []
    for directory in (RESULTS_DIR, LATEX_DIR):
        if not directory.exists():
            continue
        for pdf in sorted(directory.rglob("*.pdf")):
            errors.append(f"unexpected PDF present: {rel(pdf)}")
    return errors


def run_latex_checks() -> dict[str, list[str]]:
    """Run every check; empty lists mean the check passed."""
    results: dict[str, list[str]] = {"files_exist": check_files_exist()}
    results.update(check_features())
    results["no_final_pdf"] = check_no_pdf()
    return results


def validate_latex() -> int:
    """CLI handler for ``--mode validate-latex``. Returns an exit code."""
    print("VALIDATE LATEX — checking assembled source (offline, no compile)\n")
    results = run_latex_checks()
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
    print("\nValidation passed: source complete, all features present, no PDF built.")
    return 0


if __name__ == "__main__":  # pragma: no cover - convenience entry point
    raise SystemExit(validate_latex())
