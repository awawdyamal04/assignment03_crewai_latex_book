"""Response and safeguards chapters (6-10) of the article (Phase 5).

Proportionality and due process (with the conceptual escalation figure,
F6/F9), minors/schools/parents, platform responsibility, evidence and
reporting, and prevention and education. Balanced, course-aligned prose with
real citations only; no fabricated statistics and no unsupported legal claims.
Pure LaTeX string; no LLM, no build.
"""

from __future__ import annotations

RESPONSE_CHAPTERS = r"""\chapter{Proportionality and Due Process}
If legal consequences are sometimes justified, they must still be fair. Two
principles do most of the work. Proportionality requires that the response
match the seriousness of the conduct: a one-off rude comment is not a crime,
while sustained, severe abuse may warrant a stronger answer. Due process
requires that accusations be tested on evidence, that the accused can respond,
and that intent and context are weighed before any penalty. \autoref{fig:escalation}
sketches a conceptual escalation model in which the response intensifies only
as the harm does, beginning with prevention and education and reserving severe
legal action for the most serious cases. It is conceptual and educational - a
way of organising options - not a measured finding or a rule that any
authority is bound to follow.
\begin{figure}[ht]
  \centering
  \includegraphics[width=0.85\textwidth]{escalation_model.png}
  \caption{Conceptual escalation model of cyberbullying response: as harm
    severity rises, the appropriate response intensifies from prevention and
    education toward severe legal action. Conceptual and educational only -
    not measured research and not a legal standard.}
  \label{fig:escalation}
\end{figure}

\chapter{Minors, Schools, and Parents}
Much cyberbullying involves young people, which changes how consequences
should be applied. An age-aware approach recognises that minors are still
developing judgement, and that the goal is usually to change behaviour rather
than to punish for its own sake~\cite{hinduja2015}. Schools sit at the centre
of this work: they can teach digital citizenship, intervene early, and apply
proportionate, often restorative, discipline within their remit. Parents
reinforce the same norms at home, model respectful communication, and help
children document and report incidents. None of this removes a role for the
law in the most serious cases, but it means that for minors, education and
school intervention should usually come first and that legal consequences,
where they exist, are calibrated to age and circumstance.

\chapter{Platform Responsibility}
Online services shape the conditions in which cyberbullying spreads, so they
share responsibility for reducing it. Practical measures include clear conduct
policies, easy and visible reporting tools, timely review of complaints,
options to block or mute, and design choices that slow the viral spread of
harmful content. Scholars of online abuse have argued that platforms can do
considerably more to protect targets of harassment~\cite{citron2014}, and
child-focused organisations publish practical guidance on staying safe and
reporting abuse online~\cite{unicef2019}. Platform action is not a substitute
for education or, in serious cases, the law; rather, it is a necessary layer
that operates faster and at larger scale than either, and that preserves the
evidence later steps may need.

\chapter{Evidence, Reporting, and Documentation}
Any fair response depends on a reliable record of what happened. Because
digital conduct leaves traces, victims and bystanders can preserve evidence -
screenshots with visible dates, message threads, and URLs - before content is
deleted~\cite{hinduja2015}. Clear reporting systems matter just as much:
people need to know where to report, what will happen next, and that reports
will be handled seriously and confidentially~\cite{unicef2019}. Good
documentation supports proportionality and due process directly: it lets a
school, platform, or court distinguish a single lapse from a sustained
campaign, and it protects the wrongly accused as much as the genuine victim.
Reporting and documentation are therefore the connective tissue between the
educational and the legal ends of the response spectrum.

\chapter{Prevention and Education}
The best response to cyberbullying is to prevent it. Prevention is primarily
educational: teaching empathy, digital citizenship, and bystander
responsibility, and building school cultures in which targets feel safe to
speak up~\cite{hinduja2015}. Practical digital-safety habits - protecting
personal information, knowing how to block and report, and keeping records -
reduce both the incidence and the impact of online harm~\cite{unicef2019}.
Prevention and legal consequences are complementary, not competing: a credible
backstop for the most serious cases reinforces everyday norms, while strong
education reduces how often that backstop is ever needed. This is exactly the
balance the thesis of this article defends.
"""
