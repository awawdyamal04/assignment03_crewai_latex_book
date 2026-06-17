"""Generate the conceptual complexity-comparison figure (Phase 4).

This writes ``figures/complexity_comparison.png`` using matplotlib with a
headless (Agg) backend — no GUI, no LLM, no real experimental data. The
curves are *deterministic, theoretical* illustrations of well-known
complexity ideas from "Attention Is All You Need" (Vaswani et al., 2017,
Table 1), clearly labelled as conceptual:

* RNN / LSTM read a sequence step by step, so the maximum dependency path
  between two positions grows linearly, O(n).
* Transformer self-attention connects every pair directly, giving an O(1)
  path length but O(n^2) pairwise interactions per layer.

Nothing here is a benchmark or a measured result.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # headless: never opens a window

import matplotlib.pyplot as plt  # noqa: E402  (must follow backend choice)
import numpy as np  # noqa: E402

from src.config import FIGURES_DIR, ensure_output_dirs, rel  # noqa: E402

FIGURE_PATH: Path = FIGURES_DIR / "complexity_comparison.png"

CAPTION = (
    "Conceptual comparison (not a benchmark): recurrent models (RNN/LSTM) "
    "relate two positions through O(n) sequential steps, while Transformer "
    "self-attention uses an O(1) path at the cost of O(n^2) pairwise "
    "interactions per layer. Theoretical curves only."
)


def _data() -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Return deterministic conceptual curves over sequence length n."""
    n = np.arange(1, 65)  # sequence lengths 1..64, fully deterministic
    rnn_path = n.astype(float)  # O(n) sequential dependency path
    transformer_path = np.ones_like(n, dtype=float)  # O(1) direct access
    rnn_ops = n.astype(float)  # O(n) sequential interactions
    transformer_ops = n.astype(float) ** 2  # O(n^2) pairwise interactions
    return n, rnn_path, transformer_path, rnn_ops, transformer_ops


def build_figure() -> Path:
    """Render and save the two-panel conceptual figure; return its path."""
    ensure_output_dirs()
    n, rnn_path, tr_path, rnn_ops, tr_ops = _data()

    fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(11, 4.5))
    fig.suptitle(
        "RNN/LSTM vs. Transformer — Conceptual Sequence-Processing Cost",
        fontsize=13,
        fontweight="bold",
    )

    # Left panel: maximum dependency path length between two positions.
    ax_left.plot(n, rnn_path, label="RNN / LSTM (sequential, O(n))", color="#c0392b")
    ax_left.plot(
        n, tr_path, label="Transformer attention (direct, O(1))", color="#2471a3"
    )
    ax_left.set_title("Maximum dependency path length")
    ax_left.set_xlabel("Sequence length n (tokens)")
    ax_left.set_ylabel("Steps to relate two positions")
    ax_left.legend(loc="upper left", fontsize=9)
    ax_left.grid(True, alpha=0.3)

    # Right panel: interactions per layer (note the log scale for clarity).
    ax_right.plot(
        n, rnn_ops, label="RNN / LSTM (sequential, O(n))", color="#c0392b"
    )
    ax_right.plot(
        n, tr_ops, label="Transformer attention (pairwise, O(n^2))", color="#2471a3"
    )
    ax_right.set_title("Interactions per layer")
    ax_right.set_xlabel("Sequence length n (tokens)")
    ax_right.set_ylabel("Relative operation count (log scale)")
    ax_right.set_yscale("log")
    ax_right.legend(loc="upper left", fontsize=9)
    ax_right.grid(True, which="both", alpha=0.3)

    # Caption beneath both panels.
    fig.text(
        0.5,
        -0.04,
        CAPTION,
        ha="center",
        va="top",
        fontsize=8,
        style="italic",
        wrap=True,
    )

    fig.tight_layout(rect=(0, 0, 1, 0.96))
    fig.savefig(FIGURE_PATH, dpi=200, bbox_inches="tight")
    plt.close(fig)
    return FIGURE_PATH


def generate_graph() -> int:
    """CLI helper: build the figure and report where it went."""
    print("GRAPH — rendering conceptual complexity comparison (no LLM)\n")
    path = build_figure()
    print(f"  written: {rel(path)}")
    print("\nCaption:")
    print(f"  {CAPTION}")
    return 0


if __name__ == "__main__":  # pragma: no cover - convenience entry point
    raise SystemExit(generate_graph())
