"""Body chapters for the assembled article (Phase 5).

Thirteen chapters (F4) on whether cyberbullying should have legal
consequences, assembled from four small modules so each Python file stays
under the 150-line limit:

* ``latex_ch_problem``   - intro, definition, real harm (formula F8), impact,
  why legal consequences (responses table F7).
* ``latex_ch_response``  - proportionality (figure F6/F9), minors/schools,
  platform responsibility, evidence/reporting, prevention.
* ``latex_ch_pipeline``  - the CrewAI production-pipeline chapter (agents
  table F7) that keeps the project methodology visible.
* ``latex_ch_closing``   - bilingual Hebrew/English BiDi chapter (F10) and
  the conclusion.

Conceptual, balanced, course-aligned prose with real citations only (F11),
internal + external hyperlinks (F12) - no fabricated statistics and no
unsupported legal claims. Pure LaTeX string; no LLM, no build.
"""

from __future__ import annotations

from src.pipeline.latex_ch_closing import CLOSING_CHAPTERS
from src.pipeline.latex_ch_pipeline import PIPELINE_CHAPTER
from src.pipeline.latex_ch_problem import PROBLEM_CHAPTERS
from src.pipeline.latex_ch_response import RESPONSE_CHAPTERS

CHAPTERS = "\n".join(
    [
        PROBLEM_CHAPTERS,
        RESPONSE_CHAPTERS,
        PIPELINE_CHAPTER,
        CLOSING_CHAPTERS,
    ]
)
