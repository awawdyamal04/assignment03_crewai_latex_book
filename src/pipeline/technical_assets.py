"""Generate the table + formula technical asset (Phase 4).

Writes ``content/tables_formulas.md`` offline — no LLM, no fabricated
research. The file holds three course-aligned technical assets the later
LaTeX phase inserts into the document:

* a Markdown comparison table (RNN, LSTM, Transformer, CrewAI agents),
* one complex LaTeX formula — scaled dot-product attention,
* a short explanation plus a note that the content is course-aligned.

These are conceptual/definitional assets, not experimental results.
"""

from __future__ import annotations

from pathlib import Path

from src.config import ARTIFACTS, ensure_output_dirs, rel

ASSET_PATH: Path = ARTIFACTS["table_formula"]  # content/tables_formulas.md

# The complex formula, kept as a single token block so the validator and the
# LaTeX converter can locate it unambiguously.
ATTENTION_FORMULA = (
    r"\operatorname{Attention}(Q, K, V) = "
    r"\operatorname{softmax}\!\left(\frac{Q K^{T}}{\sqrt{d_k}}\right) V"
)

_TABLE = """\
| Model / System | Core mechanism | Sequence handling | Long-range dependencies | Parallelism |
|----------------|----------------|-------------------|-------------------------|-------------|
| **RNN** | Recurrent hidden state | Step-by-step (O(n) path) | Weak — vanishing/exploding gradients | Low (sequential) |
| **LSTM** | Gated cell state (input/forget/output) | Step-by-step (O(n) path) | Improved via gating + cell memory | Low (sequential) |
| **Transformer** | Scaled dot-product self-attention | All positions at once (O(1) path) | Strong — direct pairwise access | High (parallel) |
| **CrewAI agents** | Role-based agents + shared context | Sequential task hand-off | Carried by passed task context | Orchestrated (per process) |
"""


_HEADER = """\
<!-- file: tables_formulas.md — offline technical asset, no LLM, no real data -->

# Technical Assets — Table and Formula

> Course-aligned technical content for course **203.3763 — Orchestration of
> AI Agents**. These assets are conceptual/definitional (textbook-level), not
> experimental results, and are generated offline without calling any LLM.

## 1. Comparison Table

<!-- TABLE-ASSET -->
"""

_TABLE_CAPTION = """\

*Table: conceptual comparison of recurrent models, the Transformer, and
CrewAI agent orchestration.*

## 2. Complex Formula — Scaled Dot-Product Attention

<!-- FORMULA-ASSET -->

$$
"""

# Plain-text mirror + explanation + note. Not an f-string, so LaTeX braces
# such as {T} and {d_k} stay literal.
_EXPLANATION = """\
$$

Plain-text form: `Attention(Q,K,V) = softmax((Q K^T) / sqrt(d_k)) V`.

## 3. Explanation

The scaled dot-product attention is the core operation of the Transformer
(Vaswani et al., 2017). For each query in $Q$, the dot products $Q K^{T}$
score how relevant every key in $K$ is. Dividing by $\\sqrt{d_k}$ — the
square root of the key dimension — keeps those scores from growing too
large, which would otherwise push the `softmax` into regions with vanishing
gradients. The `softmax` turns the scaled scores into a probability
distribution (attention weights) that is then used to take a weighted sum of
the value vectors $V$. The result is a context-aware representation in which
every position can attend **directly** to every other position, removing the
long sequential dependency path that limits RNNs and LSTMs.

## 4. Note

<!-- COURSE-ALIGNED-NOTE -->
This table and formula are **course-aligned technical content**: they restate
established definitions from the course material and the cited literature and
contain no fabricated experimental data.
"""


def build_markdown() -> str:
    """Return the full Markdown for the table/formula asset file."""
    return (
        _HEADER
        + _TABLE
        + _TABLE_CAPTION
        + ATTENTION_FORMULA
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
    print("ASSETS — writing table + formula Markdown (no LLM)\n")
    path = build_assets()
    print(f"  written: {rel(path)}")
    print("\nContains: comparison table, scaled dot-product attention formula,")
    print("explanation, and a course-aligned note.")
    return 0


if __name__ == "__main__":  # pragma: no cover - convenience entry point
    raise SystemExit(generate_assets())
