"""Front-matter fragments for the assembled article (Phase 5).

Title page (course details, lecturer, student, date), the English abstract
(F13), and the table of contents (F3). Pure LaTeX strings - no LLM, no PDF
build.
"""

from __future__ import annotations

# -- Title page (F2) ---------------------------------------------------------
TITLE_PAGE = r"""% ===== TITLE PAGE (F2) =====
\begin{titlepage}
  \centering
  \vspace*{1.6cm}
  {\Huge\bfseries Cyberbullying Should Have\\[0.3em]
    Legal Consequences\par}
  \vspace{0.7cm}
  {\Large\itshape A Multi-Agent Academic Analysis Generated with\\[0.2em]
    CrewAI and LuaLaTeX\par}
  \vspace{2cm}
  \begin{tabular}{rl}
    \textbf{Course}   & \coursenumber\ - \coursename \\[0.4em]
    \textbf{Lecturer} & \lecturername \\[0.4em]
    \textbf{Student}  & \studentname \\[0.4em]
    \textbf{Date}     & \today \\
  \end{tabular}
  \vfill
  {\small Assembled by a CrewAI multi-agent pipeline and typeset with LuaLaTeX.\par}
\end{titlepage}
\pagenumbering{roman}
"""

# -- Abstract (F13) ----------------------------------------------------------
ABSTRACT = r"""% ===== ABSTRACT (F13) =====
\chapter*{Abstract}
\addcontentsline{toc}{chapter}{Abstract}
This article examines whether cyberbullying should carry legal consequences.
It argues that online harm is real harm, and that legal consequences may be
warranted when conduct is repeated, targeted, severe, threatening,
defamatory, exploitative, or causes serious harm. At the same time, any
response must remain proportional, age-aware, and evidence-based, and must be
combined with education, school intervention, clear reporting systems, and
genuine platform responsibility. The discussion stays balanced and general:
it describes psychological, social, and educational effects in broad terms,
avoids fabricated statistics, and makes no unsupported legal claims. The
document is also a worked example of agentic authorship: it was assembled by a
nine-agent CrewAI pipeline that researches, writes, illustrates, reviews, and
typesets the manuscript, and then compiles it to PDF with LuaLaTeX. A
conceptual escalation model, a conceptual harm-risk formula, comparison
tables, and a bilingual Hebrew-English chapter accompany the argument.
"""

# -- Table of contents (F3) --------------------------------------------------
TOC = r"""% ===== TABLE OF CONTENTS (F3) =====
\tableofcontents
\cleardoublepage
\pagenumbering{arabic}
"""
