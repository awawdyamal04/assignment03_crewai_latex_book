"""Front-matter fragments for the assembled article (Phase 5).

Title page (course details, lecturer, student placeholder, date), the English
abstract (F13), and the table of contents (F3). Pure LaTeX strings — no LLM,
no PDF build.
"""

from __future__ import annotations

# ── Title page (F2) ─────────────────────────────────────────────────────────
TITLE_PAGE = r"""% ===== TITLE PAGE (F2) =====
\begin{titlepage}
  \centering
  \vspace*{2cm}
  {\Huge\bfseries From RNN and LSTM to\\[0.3em] Transformers and AI Agents\par}
  \vspace{0.6cm}
  {\Large\itshape How Modern AI Systems Generate Knowledge\par}
  \vspace{2cm}
  \begin{tabular}{rl}
    \textbf{Course}   & \coursenumber\ — \coursename \\[0.4em]
    \textbf{Lecturer} & \lecturername \\[0.4em]
    \textbf{Student}  & \studentname \\[0.4em]
    \textbf{Date}     & \today \\
  \end{tabular}
  \vfill
  {\small Assembled by a CrewAI multi-agent pipeline and typeset with LuaLaTeX.\par}
\end{titlepage}
\pagenumbering{roman}
"""

# ── Abstract (F13) ──────────────────────────────────────────────────────────
ABSTRACT = r"""% ===== ABSTRACT (F13) =====
\chapter*{Abstract}
\addcontentsline{toc}{chapter}{Abstract}
This article traces the evolution of sequence modelling in modern artificial
intelligence: from recurrent neural networks (RNNs) and their long
short-term memory (LSTM) refinement, through the attention mechanism and the
Transformer architecture, to the multi-agent systems that orchestrate them.
We explain why recurrent models were originally needed, how gating addressed
the vanishing-gradient problem, and why scaled dot-product attention enabled
parallel, long-range context modelling. We then connect attention and context
to agentic systems, using the CrewAI framework as an example of role-based
orchestration. The document itself was assembled by such a pipeline, and
serves as a worked example of how a team of cooperating agents can research,
write, illustrate, and typeset an academic PDF end to end.
"""

# ── Table of contents (F3) ──────────────────────────────────────────────────
TOC = r"""% ===== TABLE OF CONTENTS (F3) =====
\tableofcontents
\cleardoublepage
\pagenumbering{arabic}
"""
