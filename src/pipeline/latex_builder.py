"""Assemble ``latex/main.tex`` + ``latex/references.bib`` (Phase 5).

Composes the LuaLaTeX document from the preamble, front-matter, body, and
bibliography fragments and writes it to ``latex/main.tex``. This stage does
NOT compile a PDF — it only emits the source the LaTeX/biber phase later
builds. Offline only; no LLM is contacted.
"""

from __future__ import annotations

from pathlib import Path

from src.config import ARTIFACTS, ensure_output_dirs, rel
from src.pipeline.latex_body import CHAPTERS
from src.pipeline.latex_frontmatter import ABSTRACT, TITLE_PAGE, TOC
from src.pipeline.latex_preamble import PREAMBLE
from src.pipeline.latex_references import build_references

MAIN_TEX_PATH: Path = ARTIFACTS["latex"]  # latex/main.tex


def build_main_tex() -> str:
    """Return the full ``main.tex`` source as a single string."""
    return "\n".join(
        [
            PREAMBLE,
            r"\begin{document}",
            TITLE_PAGE,
            ABSTRACT,
            TOC,
            CHAPTERS,
            r"% ===== BIBLIOGRAPHY (F11) =====",
            r"\printbibliography[heading=bibintoc,title={References}]",
            r"\end{document}",
            "",
        ]
    )


def build_latex() -> int:
    """CLI handler for ``--mode build-latex``. Returns an exit code."""
    print("BUILD LATEX — assembling LuaLaTeX source (no compile, no LLM)\n")
    ensure_output_dirs()

    MAIN_TEX_PATH.write_text(build_main_tex(), encoding="utf-8")
    print(f"  written: {rel(MAIN_TEX_PATH)}")

    bib_path = build_references()
    print(f"  written: {rel(bib_path)}")

    print(
        "\nAssembled the document source only. No PDF was built — run the\n"
        "LaTeX/biber phase (lualatex -> biber -> lualatex -> lualatex) to\n"
        "compile, then `--mode validate-latex` to check the source."
    )
    return 0


if __name__ == "__main__":  # pragma: no cover - convenience entry point
    raise SystemExit(build_latex())
