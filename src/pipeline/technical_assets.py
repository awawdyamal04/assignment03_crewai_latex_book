"""Generate the table + formula technical asset (Phase 4).

Writes ``content/tables_formulas.md`` offline - no LLM, no fabricated
research. The file holds three course-aligned technical assets the later
LaTeX phase reflects in the document:

* a Markdown comparison table of responses to cyberbullying,
* one conceptual formula - a harm-risk score,
* a short explanation plus a note that the content is conceptual/educational.

These are conceptual/illustrative assets, not experimental results, and no
unsupported legal claim is attached to them.
"""

from __future__ import annotations

from pathlib import Path

from src.config import ARTIFACTS, ensure_output_dirs, rel

ASSET_PATH: Path = ARTIFACTS["table_formula"]  # content/tables_formulas.md

# The conceptual formula, kept as a single token block so the validator and the
# LaTeX phase can locate it unambiguously.
HARM_RISK_FORMULA = r"R = \alpha F + \beta S + \gamma D + \delta A"

_TABLE = """\
| Response | What it does | Best suited to |
|----------|--------------|----------------|
| **Education** | Builds awareness, empathy, and digital-citizenship skills | Prevention and most everyday incidents |
| **School discipline** | Applies school rules and restorative measures | Conduct involving students within a school's remit |
| **Platform moderation** | Removes content, warns, or suspends accounts | Policy violations reported on a service |
| **Civil / legal liability** | Allows claims such as defamation or harassment | Reputational or dignitary harm to identifiable victims |
| **Criminal / legal consequences** | Reserved for the most serious conduct | Threats, severe harassment, or exploitative content |
"""


_HEADER = """\
<!-- file: tables_formulas.md - offline technical asset, no LLM, no real data -->

# Technical Assets - Table and Formula

> Course-aligned technical content for course **203.3763 - Orchestration of
> AI Agents**. These assets are conceptual/illustrative, not experimental
> results, and are generated offline without calling any LLM. They contain no
> fabricated statistics and no unsupported legal claims.

## 1. Comparison Table - Responses to Cyberbullying

<!-- TABLE-ASSET -->
"""

_TABLE_CAPTION = """\

*Table: conceptual comparison of responses to cyberbullying, from prevention
through to legal consequences. Categories are general and illustrative; this is
not legal advice.*

## 2. Conceptual Formula - Harm-Risk Score

<!-- FORMULA-ASSET -->

$$
"""

# Plain-text mirror + explanation + note. Not an f-string, so LaTeX braces stay
# literal.
_EXPLANATION = """\
$$

Plain-text form: `R = alpha*F + beta*S + gamma*D + delta*A`.

## 3. Explanation

This is an **educational conceptual model, not a real legal formula and not a
measurement**. It organises a discussion of why some online conduct is treated
as more serious than other conduct. `R` is a conceptual harm-risk score and the
factors are: `F` = frequency (how often the conduct recurs), `S` = severity
(how serious each act is), `D` = duration (how long the conduct or its content
persists), and `A` = audience/reach (how widely it spreads). The weights
`alpha, beta, gamma, delta` simply indicate that these factors do not
contribute equally. No real values are assigned, and the model must never be
used as an actual measurement or legal standard.

## 4. Note

<!-- COURSE-ALIGNED-NOTE -->
This table and formula are **course-aligned, conceptual technical content**:
they organise general, balanced points and contain no fabricated experimental
data and no unsupported legal claims.
"""


def build_markdown() -> str:
    """Return the full Markdown for the table/formula asset file."""
    return (
        _HEADER
        + _TABLE
        + _TABLE_CAPTION
        + HARM_RISK_FORMULA
        + "\n"
        + _EXPLANATION
    )


def build_assets() -> Path:
    """Write the table/formula Markdown file; return its path."""
    ensure_output_dirs()
    ASSET_PATH.write_text(build_markdown(), encoding="utf-8")
    return ASSET_PATH


def generate_assets() -> int:
    """CLI helper: write the table/formula asset and report the path."""
    print("ASSETS - writing table + formula Markdown (no LLM)\n")
    path = build_assets()
    print(f"  written: {rel(path)}")
    print("\nContains: responses comparison table, conceptual harm-risk")
    print("formula, explanation, and a course-aligned note.")
    return 0


if __name__ == "__main__":  # pragma: no cover - convenience entry point
    raise SystemExit(generate_assets())
