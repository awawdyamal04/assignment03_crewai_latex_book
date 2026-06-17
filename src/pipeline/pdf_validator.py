"""Validate the compiled Phase 6 PDF (offline, no LLM, no fabrication).

Confirms ``results/final_output.pdf`` exists, is a real non-empty PDF, that
``results/compile_log.txt`` exists, that the log records no LaTeX fatal errors,
and that the bibliography (biber) step was attempted. Validation only passes
when a genuine PDF is present — this module never creates or fakes one.
"""

from __future__ import annotations

from src.config import rel
from src.pipeline.pdf_compiler import COMPILE_LOG_PATH, FINAL_PDF_PATH

# Substrings that indicate a genuine, build-aborting LaTeX/biber failure.
FATAL_MARKERS: tuple[str, ...] = (
    "Fatal error occurred",
    "! Emergency stop",
    "No pages of output",
)


def _log_text() -> str:
    if not COMPILE_LOG_PATH.exists():
        return ""
    return COMPILE_LOG_PATH.read_text(encoding="utf-8", errors="replace")


def check_pdf_exists() -> list[str]:
    """results/final_output.pdf must exist."""
    if not FINAL_PDF_PATH.exists():
        return [f"missing: {rel(FINAL_PDF_PATH)} (run --mode compile-pdf)"]
    return []


def check_pdf_real() -> list[str]:
    """The PDF must be non-empty and start with a real %PDF- header."""
    if not FINAL_PDF_PATH.exists():
        return [f"missing: {rel(FINAL_PDF_PATH)}"]
    errors: list[str] = []
    if FINAL_PDF_PATH.stat().st_size <= 0:
        errors.append(f"empty PDF (0 bytes): {rel(FINAL_PDF_PATH)}")
    with FINAL_PDF_PATH.open("rb") as fh:
        if fh.read(5) != b"%PDF-":
            errors.append(f"not a real PDF (bad header): {rel(FINAL_PDF_PATH)}")
    return errors


def check_log_exists() -> list[str]:
    """results/compile_log.txt must exist."""
    if not COMPILE_LOG_PATH.exists():
        return [f"missing: {rel(COMPILE_LOG_PATH)} (run --mode compile-pdf)"]
    return []


def check_no_fatal_errors() -> list[str]:
    """No fatal LaTeX/biber error markers may appear in the compile log."""
    if not COMPILE_LOG_PATH.exists():
        return [f"no log to inspect: {rel(COMPILE_LOG_PATH)}"]
    text = _log_text()
    return [f"fatal marker in log: {m!r}" for m in FATAL_MARKERS if m in text]


def check_bibliography_attempted() -> list[str]:
    """The compile log must show the bibliography (biber) step was run."""
    if not COMPILE_LOG_PATH.exists():
        return [f"no log to inspect: {rel(COMPILE_LOG_PATH)}"]
    if "biber" in _log_text().lower():
        return []
    return ["bibliography (biber) step not found in compile log"]


def run_pdf_checks() -> dict[str, list[str]]:
    """Run every PDF check; empty lists mean the check passed."""
    return {
        "pdf_exists": check_pdf_exists(),
        "pdf_is_real_nonempty": check_pdf_real(),
        "compile_log_exists": check_log_exists(),
        "no_fatal_errors": check_no_fatal_errors(),
        "bibliography_attempted": check_bibliography_attempted(),
    }


def validate_pdf() -> int:
    """CLI handler for ``--mode validate-pdf``. Returns an exit code."""
    print("VALIDATE PDF — checking the compiled output (offline, no LLM)\n")
    results = run_pdf_checks()
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
        print(f"\nValidation found {failures} issue(s). A real PDF was NOT confirmed.")
        return 1
    print("\nValidation passed: a real, non-empty PDF exists and the log is clean.")
    return 0


if __name__ == "__main__":  # pragma: no cover - convenience entry point
    raise SystemExit(validate_pdf())
