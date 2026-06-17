"""Compile ``latex/main.tex`` into ``results/final_output.pdf`` (Phase 6).

Runs the LuaLaTeX + biber build sequence
``lualatex -> biber -> lualatex -> lualatex`` inside the ``latex/`` directory,
copies the resulting PDF to ``results/final_output.pdf`` and writes the combined
command output to ``results/compile_log.txt``. Offline only; no LLM is
contacted. If ``lualatex`` or ``biber`` is missing, a clear message is printed
instead of crashing, and no fake PDF is ever created.
"""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path
from typing import TextIO

from src.config import LATEX_DIR, RESULTS_DIR, ensure_output_dirs, rel
from src.pipeline.latex_builder import MAIN_TEX_PATH

FINAL_PDF_PATH: Path = RESULTS_DIR / "final_output.pdf"
COMPILE_LOG_PATH: Path = RESULTS_DIR / "compile_log.txt"
BUILT_PDF_PATH: Path = LATEX_DIR / "main.pdf"  # lualatex emits this from main.tex

# (label, argv) for each build step; all run with cwd=LATEX_DIR.
BUILD_STEPS: tuple[tuple[str, list[str]], ...] = (
    ("lualatex (pass 1)", ["lualatex", "-interaction=nonstopmode", "main.tex"]),
    ("biber", ["biber", "main"]),
    ("lualatex (pass 2)", ["lualatex", "-interaction=nonstopmode", "main.tex"]),
    ("lualatex (pass 3)", ["lualatex", "-interaction=nonstopmode", "main.tex"]),
)


def missing_tools() -> list[str]:
    """Return the names of required build tools that are not on PATH."""
    return [t for t in ("lualatex", "biber") if shutil.which(t) is None]


def _run_step(label: str, argv: list[str], log: TextIO) -> int:
    """Run one build step, appending its combined output to the open log."""
    log.write(f"\n===== {label}: {' '.join(argv)} =====\n")
    print(f"  running: {label} ...")
    try:
        proc = subprocess.run(
            argv,
            cwd=LATEX_DIR,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
    except OSError as exc:  # tool vanished between the check and the call
        log.write(f"[ERROR] could not launch {argv[0]}: {exc}\n")
        return 1
    log.write(proc.stdout or "")
    log.write(proc.stderr or "")
    log.write(f"\n[exit code: {proc.returncode}]\n")
    return proc.returncode


def compile_pdf() -> int:
    """CLI handler for ``--mode compile-pdf``. Returns an exit code."""
    print("COMPILE PDF — lualatex -> biber -> lualatex -> lualatex (no LLM)\n")
    if not MAIN_TEX_PATH.exists():
        print(f"  [FAIL] missing {rel(MAIN_TEX_PATH)} — run --mode build-latex first.")
        return 1

    missing = missing_tools()
    if missing:
        print("  [SKIP] required tool(s) not found on PATH: " + ", ".join(missing))
        print("         Install a TeX distribution (MiKTeX/TeX Live) providing")
        print("         lualatex and biber, then re-run --mode compile-pdf.")
        return 1

    ensure_output_dirs()
    worst = 0
    with COMPILE_LOG_PATH.open("w", encoding="utf-8") as log:
        log.write("Phase 6 compile log\n")
        log.write("build order: lualatex -> biber -> lualatex -> lualatex\n")
        for label, argv in BUILD_STEPS:
            worst = max(worst, _run_step(label, argv, log))
    print(f"  log written: {rel(COMPILE_LOG_PATH)}")

    if not BUILT_PDF_PATH.exists():
        print(f"  [FAIL] no PDF produced at {rel(BUILT_PDF_PATH)}; inspect the log.")
        return 1
    shutil.copyfile(BUILT_PDF_PATH, FINAL_PDF_PATH)
    size = FINAL_PDF_PATH.stat().st_size
    print(f"  PDF written: {rel(FINAL_PDF_PATH)} ({size} bytes)")
    if worst != 0:
        print("  [warn] a build step returned a non-zero exit code; check the log.")
    print("\nCompiled. Run --mode validate-pdf to verify the output.")
    return 0


if __name__ == "__main__":  # pragma: no cover - convenience entry point
    raise SystemExit(compile_pdf())
