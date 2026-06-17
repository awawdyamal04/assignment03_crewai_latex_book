"""Generate the conceptual escalation-model figure (Phase 4).

This writes ``figures/escalation_model.png`` using matplotlib with a headless
(Agg) backend - no GUI, no LLM, no real data. It is a *conceptual,
educational* illustration of how a proportional response to cyberbullying
intensifies as harm severity rises:

    prevention/education -> school intervention -> platform reporting/
    moderation -> civil/legal response -> severe legal action

Nothing here is a measurement, a benchmark, or a legal standard. The values
are fixed, ordinal step levels chosen only to draw the staircase.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # headless: never opens a window

import matplotlib.pyplot as plt  # noqa: E402  (must follow backend choice)
import numpy as np  # noqa: E402

from src.config import FIGURES_DIR, ensure_output_dirs, rel  # noqa: E402

FIGURE_PATH: Path = FIGURES_DIR / "escalation_model.png"

LEVELS = (
    "Prevention &\neducation",
    "School\nintervention",
    "Platform\nreporting/\nmoderation",
    "Civil /\nlegal\nresponse",
    "Severe\nlegal\naction",
)

CAPTION = (
    "Conceptual escalation model (not measured research, not a legal "
    "standard): as harm severity rises, a proportional response intensifies "
    "from prevention and education toward severe legal action. The step "
    "levels are ordinal and illustrative only."
)


def build_figure() -> Path:
    """Render and save the conceptual escalation staircase; return its path."""
    ensure_output_dirs()
    x = np.arange(1, len(LEVELS) + 1)  # ordinal harm-severity tiers 1..5
    y = np.arange(1, len(LEVELS) + 1)  # matching response-intensity tiers

    fig, ax = plt.subplots(figsize=(10, 5.2))
    fig.suptitle(
        "Conceptual Escalation Model of Cyberbullying Response",
        fontsize=14,
        fontweight="bold",
    )

    # Staircase: response intensity rises only as harm severity rises.
    ax.step(x, y, where="mid", color="#2471a3", linewidth=2.5, zorder=2)
    ax.scatter(x, y, color="#c0392b", s=90, zorder=3)

    for xi, yi, label in zip(x, y, LEVELS):
        ax.annotate(
            label,
            (xi, yi),
            textcoords="offset points",
            xytext=(0, 12),
            ha="center",
            va="bottom",
            fontsize=9,
        )

    ax.set_xlabel("Harm severity (low -> high, conceptual tiers)")
    ax.set_ylabel("Response intensity (conceptual tiers)")
    ax.set_xlim(0.5, len(LEVELS) + 0.7)
    ax.set_ylim(0.5, len(LEVELS) + 1.4)
    ax.set_xticks(x)
    ax.set_yticks(y)
    ax.grid(True, alpha=0.3)

    fig.text(
        0.5,
        -0.02,
        CAPTION,
        ha="center",
        va="top",
        fontsize=8,
        style="italic",
        wrap=True,
    )

    fig.tight_layout(rect=(0, 0, 1, 0.95))
    fig.savefig(FIGURE_PATH, dpi=200, bbox_inches="tight")
    plt.close(fig)
    return FIGURE_PATH


def generate_graph() -> int:
    """CLI helper: build the figure and report where it went."""
    print("GRAPH - rendering conceptual escalation model (no LLM)\n")
    path = build_figure()
    print(f"  written: {rel(path)}")
    print("\nCaption:")
    print(f"  {CAPTION}")
    return 0


if __name__ == "__main__":  # pragma: no cover - convenience entry point
    raise SystemExit(generate_graph())
