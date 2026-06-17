"""Problem-framing chapters (1-5) of the assembled article (Phase 5).

Introduction, definition, why online harm is real harm (with the conceptual
harm-risk formula, F8), the impact chapter, and why legal consequences may be
necessary (with the responses comparison table, F7). Conceptual, balanced,
course-aligned prose with real citations only - no fabricated statistics and
no unsupported legal claims. Pure LaTeX string; no LLM, no build.
"""

from __future__ import annotations

PROBLEM_CHAPTERS = r"""% ===== BODY CHAPTERS (F4) =====
\chapter{Introduction}
Much of social life now happens online, and so does some of its cruelty.
Cyberbullying - repeated, deliberate harm inflicted through digital means -
raises a sharp question: when, if ever, should it carry legal consequences?
This article defends a balanced thesis. Cyberbullying should have legal
consequences when it is repeated, targeted, severe, threatening, defamatory,
exploitative, or causes serious harm; but those consequences must be
proportional, age-aware, evidence-based, and combined with education, school
intervention, reporting systems, and platform responsibility. The argument is
developed through the conceptual harm-risk model in \autoref{eq:harmrisk},
the response options compared in \autoref{tab:responses}, and the conceptual
escalation model in \autoref{fig:escalation}. The article is also a worked
example of agentic authorship, as \autoref{tab:agents} documents.

\chapter{Definition of Cyberbullying}
Cyberbullying is commonly described as wilful and repeated harm inflicted
through computers, phones, and other digital devices~\cite{patchin2006}. Early
studies of secondary-school pupils identified several distinct forms,
including hurtful messages, exclusion from online groups, impersonation, and
the sharing of embarrassing material~\cite{smith2008}. Three features recur
across definitions: intent to harm, repetition (or content that is
persistently available), and an imbalance of power between those involved.
The digital setting changes the texture of the harm. Messages can reach a
large audience instantly, remain visible long after they are posted, and
follow a person from school into the home. Anonymity and distance can lower
inhibitions, and a single act of sharing can be repeated endlessly by others.
These properties matter for any later judgement about responsibility and
proportional response.

\chapter{Why Online Harm Is Real Harm}
A persistent misconception treats online conduct as less serious because it is
``only'' digital. The research literature does not support that view: reviews
of cyberbullying consistently associate victimisation with measurable
distress and with effects that overlap those of offline bullying~%
\cite{tokunaga2010,kowalski2014}. Harm that is mediated by a screen is still
harm to a real person. To reason about severity without inventing numbers, it
helps to name the factors that tend to make online harm worse. As an
educational conceptual model - not a legal test and not a measured formula -
one can express a harm-risk score as a weighted combination of such factors:
\begin{equation}
  R = \alpha F + \beta S + \gamma D + \delta A
  \label{eq:harmrisk}
\end{equation}
Here $R$ is a conceptual harm-risk score; $F$ is frequency (how often the
conduct recurs), $S$ is severity (how serious each act is), $D$ is duration
(how long the conduct or its content persists), and $A$ is audience or reach
(how widely it spreads). The weights $\alpha, \beta, \gamma, \delta$ simply
signal that these factors do not contribute equally. The model is purely
illustrative: it organises a discussion of why repeated, severe, persistent,
and widely-spread conduct is treated as more serious. It assigns no real
values and must never be used as an actual measurement or legal standard.

\chapter{Psychological, Social, and Educational Impact}
Discussed carefully and in general terms, the effects of cyberbullying span
several areas of a young person's life. On the psychological side, reviews
report associations with lowered well-being and emotional
distress~\cite{kowalski2014}. Socially, targeted online conduct can damage
friendships and reputation, and the persistence of digital content can make a
single incident feel ongoing~\cite{smith2008}. Educationally, students who
are preoccupied by online conflict may find it harder to concentrate or to
feel safe at school. These are described as general tendencies reported in the
literature, not as fixed outcomes for any individual, and this article
deliberately avoids citing specific figures it cannot verify. The point for
the argument is modest but important: because the harm is real and can be
serious, doing nothing is not a neutral choice.

\chapter{Why Legal Consequences May Be Necessary}
Education and support handle most situations, but not all. When conduct is
repeated, targeted, and severe - for example credible threats, sustained
harassment, defamation, or the non-consensual sharing of intimate images -
purely educational responses can be inadequate, and scholars of online abuse
have argued that the law has a legitimate role in the most serious
cases~\cite{citron2014}. Legal consequences can serve several purposes:
protecting victims, deterring the most harmful conduct, and signalling that
online harm is taken seriously. \autoref{tab:responses} compares the main
categories of response considered in this article, from prevention through to
legal action, without claiming that any particular statute applies.
\begin{table}[ht]
  \centering
  \small
  \caption{Conceptual comparison of responses to cyberbullying. Categories are
    general and illustrative; this is not legal advice and cites no specific
    statute.}
  \label{tab:responses}
  \begin{tabular}{@{}p{3.0cm}p{5.0cm}p{4.6cm}@{}}
    \toprule
    \textbf{Response} & \textbf{What it does} & \textbf{Best suited to} \\
    \midrule
    Education & Builds awareness, empathy, and digital-citizenship skills &
      Prevention and most everyday incidents \\
    School discipline & Applies school rules and restorative measures &
      Conduct involving students within a school's remit \\
    Platform moderation & Removes content, warns, or suspends accounts &
      Policy violations reported on a service \\
    Civil / legal liability & Allows claims such as defamation or harassment &
      Reputational or dignitary harm to identifiable victims \\
    Criminal / legal consequences & Reserved for the most serious conduct &
      Threats, severe harassment, or exploitative content \\
    \bottomrule
  \end{tabular}
\end{table}
"""
