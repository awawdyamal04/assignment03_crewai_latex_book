"""CrewAI production-pipeline chapter (11) of the article (Phase 5).

Explains how this document was produced by a nine-agent CrewAI pipeline and
lists each agent's name, role, input context, and output artifact (F7 table).
Keeps the project methodology visible. Pure LaTeX string; no LLM, no build.
"""

from __future__ import annotations

PIPELINE_CHAPTER = r"""\chapter{The CrewAI Production Pipeline Used in This Project}
This article was not written by a single author in one pass. It was produced
by a multi-agent pipeline built with the CrewAI framework, which organises
large-language-model agents into roles with explicit goals and shared
context~\cite{crewai2024}. The agents run as a sequential process: each one
owns a single responsibility, and the output of one agent becomes the context
of the next, much like a small academic publishing team. Nine agents
cooperate. The \emph{Researcher} gathers credible sources; the \emph{Course
Material Analyst} aligns them with the course concepts and drafts an outline;
the \emph{Writer} produces the English body; the \emph{Bilingual Chapter}
agent writes the Hebrew-English chapter; the \emph{Python Visualization} agent
writes the matplotlib code for the figure; the \emph{Table and Formula} agent
specifies the table and the conceptual formula; the \emph{Reviewer} checks
accuracy, balance, and structure; the \emph{LaTeX Converter} assembles a valid
LuaLaTeX document; and the \emph{PDF Validation} agent verifies that the
required features are present. \autoref{tab:agents} summarises the nine agents,
their roles, the context each consumes, and the artifact each produces.
\begin{table}[ht]
  \centering
  \small
  \caption{The nine-agent CrewAI production pipeline used to generate this
    document, with each agent's role, input context, and output artifact.}
  \label{tab:agents}
  \begin{tabular}{@{}p{2.7cm}p{3.6cm}p{3.3cm}p{3.1cm}@{}}
    \toprule
    \textbf{Agent} & \textbf{Role} & \textbf{Input context} &
      \textbf{Output artifact} \\
    \midrule
    Researcher & Gather credible sources & Topic brief &
      content/research.md \\
    Course Material Analyst & Align with course concepts & Research notes &
      content/course\_alignment.md \\
    Writer & Draft the English body & Research + outline &
      content/draft.md \\
    Bilingual Chapter & Write Hebrew-English chapter & Draft &
      content/bilingual.md \\
    Python Visualization & Code the figure & Draft &
      figures/plot.py + PNG \\
    Table and Formula & Specify table + formula & Draft &
      content/tables\_formulas.md \\
    Reviewer & Check accuracy and balance & Draft + chapters &
      content/reviewed.md \\
    LaTeX Converter & Assemble valid .tex & Reviewed manuscript &
      latex/main.tex \\
    PDF Validation & Verify required features & Assembled document &
      results/validation.md \\
    \bottomrule
  \end{tabular}
\end{table}
This chapter keeps the project methodology visible inside the document itself:
the article both argues a thesis about cyberbullying and demonstrates how a
cooperating team of agents can research, write, illustrate, review, and typeset
an academic PDF end to end. See the
\href{https://docs.crewai.com}{CrewAI documentation} for the framework's API.
"""
