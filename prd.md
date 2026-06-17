# PRD — Product Requirements Document

## Assignment 03 — Orchestration of AI Agents (203.3763)

**Project title:** *From RNN and LSTM to Transformers and AI Agents: How Modern AI Systems Generate Knowledge*

---

## 1. Purpose (The Idea)

Build a **multi-agent system** using the **CrewAI** framework that autonomously
researches, writes, illustrates, reviews, and typesets a **~15-page academic
article** as a compiled **PDF** produced from **LuaLaTeX**.

The agents act like a small publishing organization: each agent owns one
responsibility, and the output of one agent becomes the input/context of the
next (sequential context passing). The end product is a professional,
bilingual (Hebrew + English) academic document with figures, tables,
mathematical formulas, a Python-generated graph, citations, and a
bibliography.

This PRD describes **WHAT** must be built. `plan.md` describes **HOW**.

---

## 2. Scope

### 2.1 In scope
- A CrewAI crew of 9 cooperating agents (see §6).
- Automated research → Markdown drafting → LaTeX conversion → PDF compilation.
- A reproducible CLI-only workflow managed with **UV**.
- All mandatory documentation files (this PRD, plan, todo, README, instructions).

### 2.2 Out of scope
- Any GUI or web front-end.
- Manual hand-authoring of the article body (agents generate the content).
- Hosting / deployment of a running service.

---

## 3. The Document — Content Requirements

The article explains the evolution of sequence modeling and modern agentic AI:

1. Why sequential models such as **RNNs** were needed.
2. What problem **LSTM** solved (vanishing/exploding gradients, long-term memory).
3. Why **Transformers** replaced much of the sequential approach.
4. How **attention** and **context** relate to modern AI agents.
5. How **CrewAI** orchestrates agents like a small organization.
6. How a team of agents can produce an academic PDF end-to-end
   (research, writing, review, Python graph generation, LaTeX conversion, validation).

---

## 4. Mandatory Document Features (Acceptance Criteria)

The compiled PDF is **only accepted** when every item below is verifiably present.

| # | Requirement | Acceptance test |
|---|-------------|-----------------|
| F1 | ~15 pages of real content | PDF page count is 14–17 pages of body content |
| F2 | Title page | Shows course (203.3763), lecturer, student, date |
| F3 | Table of contents | Auto-generated TOC with correct page numbers |
| F4 | Chapter division | At least 6 chapters/sections matching §3 |
| F5 | Headers and footers | Running headers + page numbers on every body page |
| F6 | At least one image | A real embedded image renders in the PDF |
| F7 | At least one table | A formatted table renders correctly |
| F8 | One complex math formula | E.g. the scaled dot-product attention equation |
| F9 | Python-generated graph | A figure produced by agent-written Python code |
| F10 | Bilingual BiDi chapter | One chapter correctly mixes Hebrew + English |
| F11 | Citations + bibliography | BibTeX/biber, full reference list with **at least 6 real sources** |
| F12 | Working PDF hyperlinks | Internal + external links are clickable (hyperref) |
| F13 | Abstract | A short English abstract precedes the body (after title page, before/with TOC) |

---

## 5. Methodological Requirements

- Follow the **Vibe Coding lifecycle**: Idea → PRD → Plan → TODO → Verify → Execute → Push.
- Provide the five mandatory project files: `prd.md`, `plan.md`, `todo.md`,
  `README.md`, `PROJECT_INSTRUCTIONS.md`.
- `todo.md` contains **300–800** small, checkable tasks.
- Every Python file in the final project is **shorter than 150 lines**.
- Environment is managed exclusively with **UV**.
- All work is done through the **CLI** only.
- Submission is a **public GitHub repository** with a **meaningful commit history**
  (many small commits, not one large upload).

---

## 6. Required CrewAI Agents

Each agent has a **role**, **goal**, **backstory**, and **tools**. Output flows
sequentially from one agent to the next.

1. **Researcher Agent** — gathers sources/facts via a web search tool.
2. **Course Material Analyst Agent** — aligns content with course concepts/local notes.
3. **Writer Agent** — drafts the article body in Markdown.
4. **Bilingual Chapter Agent** — produces the Hebrew+English BiDi chapter.
5. **Python Visualization Agent** — writes Python that generates the graph figure.
6. **Table and Formula Agent** — produces the table + the complex math formula.
7. **Reviewer Agent** — checks accuracy, structure, completeness, and coherence.
8. **LaTeX Converter Agent** — converts approved Markdown into a valid `.tex` file.
9. **PDF Validation Agent** — verifies all F1–F13 features exist in the output.

---

## 7. Technical Requirements

- **Language:** Python (modular files, each < 150 lines).
- **Framework:** CrewAI (Agent / Task / Crew, sequential process).
- **Tools:** SerperDevTool (or equivalent search) + file-reading logic.
- **Typesetting:** **LuaLaTeX** (chosen for strong Hebrew/BiDi support).
- **Bibliography:** BibTeX/**biber** with `biblatex`.
- **Recommended pipeline:** agents produce Markdown → LaTeX Converter Agent
  emits `.tex` → project compiles `.tex` → PDF.

---

## 8. Constraints

- No code is written during the documentation phase.
- No existing files are deleted.
- No single huge monolithic source file.
- No fabricated results: every claimed feature must exist in a real compiled PDF.

---

## 9. Success Definition

The project succeeds when a reviewer can, from a clean checkout, run the
documented UV/CLI commands and obtain a ~15-page bilingual academic PDF that
satisfies every acceptance criterion F1–F13, backed by a GitHub repository with
an incremental, meaningful commit history.
