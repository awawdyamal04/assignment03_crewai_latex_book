# Cyberbullying Should Have Legal Consequences

### A Multi-Agent Academic Analysis Generated with CrewAI and LuaLaTeX

A multi-agent system built with **CrewAI** that autonomously researches, writes,
illustrates, reviews, and typesets a 15–18 page bilingual (Hebrew + English)
academic article into a **LuaLaTeX**-compiled PDF. The article argues a
balanced thesis: cyberbullying should carry **proportional, evidence-based
legal consequences** in serious cases, combined with education, school
intervention, reporting systems, and platform responsibility.

> This README is the **final report template** for Assignment 03. Sections
> marked _TBD_ are filled in as the project is implemented and verified. No
> result is recorded here unless it is real (see the No-Fake-Results rule in
> [`PROJECT_INSTRUCTIONS.md`](./PROJECT_INSTRUCTIONS.md)).

---

## 1. Course & Submission Details

| Field | Value |
|-------|-------|
| Course | 203.3763 — Orchestration of AI Agents |
| Assignment | 03 — CrewAI + LaTeX Book/Article |
| Lecturer | Dr. Yoram Reuven Segal |
| Student | Amal Awawdi |
| Date | _TBD_ |
| Repository | _TBD (public GitHub URL)_ |

---

## 2. Project Overview

The project orchestrates 9 cooperating CrewAI agents that behave like a small
publishing organization. Each agent owns one responsibility, and output flows
sequentially from one agent to the next (sequential context passing), ending in
a validated academic PDF.

See [`prd.md`](./prd.md) for WHAT the project must do and [`plan.md`](./plan.md)
for HOW it is built.

---

## 3. The Agents

| # | Agent | Responsibility |
|---|-------|----------------|
| 1 | Researcher | Web research and source gathering |
| 2 | Course Material Analyst | Align content with course concepts |
| 3 | Writer | Draft the article body (Markdown) |
| 4 | Bilingual Chapter | Hebrew + English BiDi chapter |
| 5 | Python Visualization | Write Python that generates the graph |
| 6 | Table & Formula | Produce the table and complex formula |
| 7 | Reviewer | Check accuracy, structure, coherence |
| 8 | LaTeX Converter | Convert Markdown → valid `.tex` |
| 9 | PDF Validation | Verify all required PDF features |

---

## 4. Tech Stack

Python · CrewAI · UV · LuaLaTeX · biblatex/biber · matplotlib · SerperDevTool

---

## 5. Setup (CLI / UV)

> Commands are finalized during implementation; this is the intended flow.

```bash
# 1. Install UV (if needed) — see https://docs.astral.sh/uv/
# 2. Sync the environment from the lockfile
uv sync

# 3. Configure secrets
cp .env.example .env   # then edit .env with your API keys

# 4. Run the crew (generates content artifacts)
uv run python -m src.main

# 5. Build the PDF (LuaLaTeX + biber)
#    (exact build command documented after Phase 9)
```

Prerequisites: a TeX distribution providing `lualatex` and `biber`
(e.g. TeX Live / MiKTeX), available on `PATH`.

---

## 6. How to Reproduce the PDF

1. Clone the repository.
2. `uv sync` to create the environment.
3. Provide API keys in `.env`.
4. Run the crew to regenerate `content/` and `figures/`.
5. Compile `latex/main.tex` with LuaLaTeX + biber.
6. Find the PDF and validation report in `results/`.

---

## 7. Document Feature Checklist (F1–F13)

Status reflects the most recent local LuaLaTeX + biber build of
`results/final_output.pdf` (19 pages, 0 undefined references, 0 missing
characters).

| # | Feature | Status |
|---|---------|--------|
| F1 | 15–18 pages of content | ☑ 19 pages total (~16 body) |
| F2 | Title page (course/lecturer/student/date) | ☑ built |
| F3 | Table of contents | ☑ built |
| F4 | Chapter division (13 chapters) | ☑ built |
| F5 | Headers and footers | ☑ built |
| F6 | At least one image | ☑ conceptual escalation figure |
| F7 | At least one table | ☑ responses + agents tables |
| F8 | One complex math formula | ☑ harm-risk score R = αF+βS+γD+δA |
| F9 | Python-generated graph | ☑ `escalation_model.png` |
| F10 | Bilingual Hebrew/English chapter | ☑ 0 missing glyphs |
| F11 | Citations + bibliography (biber, ≥6 sources) | ☑ 8 real sources |
| F12 | Working PDF hyperlinks | ☑ hyperref + `\href` |
| F13 | Abstract (English) precedes the body | ☑ built |

---

## 8. Project Structure

```
assignment03_crewai_latex_book/
├── prd.md · plan.md · todo.md · README.md · PROJECT_INSTRUCTIONS.md
├── pyproject.toml · requirements.txt · .gitignore · .env.example
├── src/        # Python (CrewAI agents, tasks, pipeline) — each file < 150 lines
├── content/    # Markdown artifacts produced by agents
├── latex/      # main.tex, preamble, references.bib, build output
├── figures/    # Python plotting script + generated images
├── results/    # compiled PDF, logs, validation report
└── prompts/    # reusable prompt fragments / backstories
```

---

## 9. Results & Reflection (filled in after Execute)

- **Final PDF:** _TBD (path in `results/`)_
- **Page count:** _TBD_
- **What worked:** _TBD_
- **What was hard (e.g. Hebrew BiDi):** _TBD_
- **What I'd improve:** _TBD_

---

## 10. Methodology & Rules

This project follows the Vibe Coding lifecycle (Idea → PRD → Plan → TODO →
Verify → Execute → Push) and the working rules in
[`PROJECT_INSTRUCTIONS.md`](./PROJECT_INSTRUCTIONS.md): CLI-only, UV-managed,
every Python file < 150 lines, meaningful incremental commits, and no fake
results.
