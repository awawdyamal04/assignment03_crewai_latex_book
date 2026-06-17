"""Closing chapters (12-13) of the assembled article (Phase 5).

The bilingual Hebrew-English BiDi chapter (F10), rendered with polyglossia
under LuaLaTeX so the Hebrew is readable and correctly spaced, and the
conclusion. Pure LaTeX string; no LLM, no build.
"""

from __future__ import annotations

CLOSING_CHAPTERS = r"""\chapter{Bilingual Chapter - Hebrew and English (BiDi)}
This chapter demonstrates bidirectional (BiDi) typesetting: left-to-right
English mixed with right-to-left Hebrew, handled by \texttt{polyglossia} under
LuaLaTeX. The Hebrew term for ``cyberbullying'' is
\texthebrew{בריונות רשת}, and ``legal consequences'' is
\texthebrew{השלכות משפטיות}. The Hebrew title of this chapter is
\texthebrew{בריונות רשת והשלכות משפטיות}. A short Hebrew paragraph follows,
stating the same balanced thesis the article defends in English:
\begin{hebrew}
בריונות רשת היא פגיעה חוזרת ונשנית באמצעים דיגיטליים, כגון הודעות מאיימות,
הפצת שמועות או חשיפת מידע פרטי. הפגיעה המקוונת היא פגיעה אמיתית, והיא עלולה
לגרום נזק נפשי וחברתי ממשי. כאשר ההתנהגות חמורה, חוזרת וממוקדת, ייתכן שיש
מקום להשלכות משפטיות. עם זאת, התגובה חייבת להיות מידתית, מותאמת לגיל ומבוססת
על ראיות, ולצד ענישה יש לשלב חינוך, מניעה ואחריות של הפלטפורמות.
\end{hebrew}
In English: cyberbullying is repeated harm carried out through digital means,
such as threatening messages, spreading rumours, or exposing private
information. Online harm is real harm and can cause genuine psychological and
social damage. When the conduct is severe, repeated, and targeted, legal
consequences may have a place; but the response must be proportional,
age-aware, and evidence-based, and combined with education, prevention, and
platform responsibility. The two scripts coexist in one chapter with correct
directionality, each word spaced normally within its own writing direction.

\chapter{Conclusion}
Cyberbullying poses a genuine problem because online harm is real harm. This
article has argued that legal consequences should be available when conduct is
repeated, targeted, severe, threatening, defamatory, exploitative, or causes
serious harm - and that they should be applied proportionally, with due
process, and with attention to age. Equally, the law is a backstop rather than
a first resort: prevention, education, school intervention, clear reporting and
documentation, and real platform responsibility do most of the work and reduce
how often legal consequences are ever needed. The references below ground the
discussion in credible sources, and the production-pipeline chapter shows how a
cooperating team of CrewAI agents assembled the document itself.
"""
