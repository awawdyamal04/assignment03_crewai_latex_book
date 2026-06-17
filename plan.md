# plan.md — Implementation Plan

How we will build the system described in [`prd.md`](./prd.md). This document is
the **HOW**: architecture, technology choices, agent/task design, data flow,
file layout, and the phased build order.

---

## 1. High-Level Architecture

```
                 ┌──────────────────────── CrewAI Crew (sequential) ────────────────────────┐
                 │                                                                            │
 web/search ──▶ Researcher ─▶ Course Analyst ─▶ Writer ─▶ Bilingual ─▶ Visualization ─▶ ...  │
                 │                 │              │           │             │                 │
                 ▼                 ▼              ▼           ▼             ▼                 │
            content/research   content/course  content/   content/      figures/*.png       │
              .md               .md            draft.md   bilingual.md   + python script     │
                 │                                                                            │
   ... ─▶ Table&Formula ─▶ Reviewer ─▶ LaTeX Converter ─▶ PDF Validation                     │
              │                │              │                  │                            │
              ▼                ▼              ▼                  ▼                            │
        content/tables.md  content/      latex/main.tex     results/validation.md            │
                            reviewed.md   + build → PDF                                       │
                 └──────────────────────────────────────────────────────────────────────────┘
```

Each agent writes its artifact to disk; the next agent receives the previous
output as **task context** (CrewAI `context=[...]`), implementing sequential
context passing.

> Filenames in the diagram above are abbreviated for layout. The **canonical
> artifact paths** are the ones listed in the §4 table (e.g.
> `content/course_alignment.md`, `content/tables_formulas.md`) and in `todo.md`.

---

## 2. Technology Stack

| Concern | Choice | Reason |
|---------|--------|--------|
| Orchestration | CrewAI | Required; Agent/Task/Crew abstractions |
| Language | Python 3.11+ | Required; modular files < 150 lines |
| Env / packaging | **UV** | Required; fast, reproducible venv + lockfile |
| Web research | SerperDevTool | Course-recommended search tool |
| Local reading | FileReadTool / custom | Read course notes if present |
| Typesetting | **LuaLaTeX** | Best Hebrew/BiDi + fontspec support |
| Bibliography | biblatex + **biber** | Modern, robust citation handling |
| Plotting | matplotlib | Agent-written Python generates the graph |
| LLM | Configurable via env (`.env`) | Keep keys out of source control |

---

## 3. Project Structure

```
assignment03_crewai_latex_book/
├── prd.md
├── plan.md
├── todo.md
├── README.md
├── PROJECT_INSTRUCTIONS.md
├── pyproject.toml            # UV-managed project + deps
├── requirements.txt          # mirror of locked deps
├── .gitignore
├── .env.example              # documents required keys (no secrets)
├── src/                      # all Python, each file < 150 lines
│   ├── __init__.py
│   ├── main.py               # CLI entrypoint: builds + runs the crew
│   ├── config.py             # env, paths, model settings
│   ├── tools.py              # search + file-read tool wiring
│   ├── agents/               # one small module per agent factory
│   ├── tasks/                # one small module per task definition
│   └── pipeline/             # build helpers: markdown, latex, compile, validate
├── content/                  # Markdown artifacts produced by agents
├── latex/                    # main.tex, preamble, references.bib, build output
├── figures/                  # Python-generated images + the plotting script
├── results/                  # compiled PDF, logs, validation report
└── prompts/                  # reusable prompt fragments / backstories
```

**File-size rule:** if any `src/` module approaches 150 lines, split it (e.g.
`agents/researcher.py`, `agents/writer.py`, …) rather than growing one file.

---

## 4. Agent & Task Design

Sequential `Process.sequential`. Each task lists its predecessor(s) in
`context=[...]`.

| Order | Agent | Task expected output | Artifact |
|-------|-------|----------------------|----------|
| 1 | Researcher | Sourced notes + reference candidates | `content/research.md` |
| 2 | Course Analyst | Concept alignment + outline | `content/course_alignment.md` |
| 3 | Writer | Full English draft (chapters) | `content/draft.md` |
| 4 | Bilingual Chapter | Hebrew+English BiDi chapter | `content/bilingual.md` |
| 5 | Python Visualization | Plot script + PNG + caption | `figures/plot.py`, `figures/*.png` |
| 6 | Table & Formula | Table (md) + LaTeX math formula | `content/tables_formulas.md` |
| 7 | Reviewer | Reviewed/approved manuscript + notes | `content/reviewed.md` |
| 8 | LaTeX Converter | Valid `.tex` assembling everything | `latex/main.tex` |
| 9 | PDF Validation | Pass/fail report on F1–F13 | `results/validation.md` |

Each agent factory lives in its own module under `src/agents/`; each task
definition under `src/tasks/`. `src/main.py` wires them into a `Crew` and runs it.

---

## 5. LaTeX / Build Strategy

- **Engine:** `lualatex` with `fontspec` + `polyglossia` (or `babel` + `bidi`)
  for Hebrew/English BiDi.
- **Headers/footers:** `fancyhdr`.
- **Hyperlinks:** `hyperref` (internal TOC links + external URLs/DOIs).
- **Bibliography:** `biblatex` backend `biber`, `references.bib`.
- **Math:** `amsmath`/`amssymb`; complex formula = scaled dot-product attention.
- **Figure/table:** `graphicx` for the PNG, `booktabs` for the table.
- **Build sequence:** `lualatex → biber → lualatex → lualatex` (resolve refs/TOC),
  driven by a small Python helper or `latexmk` invoked from the CLI.

---

## 6. Phased Build Order (after documentation is approved)

1. **Phase 0 — Docs (current):** prd, plan, todo, README, instructions. *No code.*
2. **Phase 1 — Scaffolding:** UV init, `pyproject.toml`, `.gitignore`, empty dirs.
3. **Phase 2 — Config & tools:** `config.py`, `tools.py`, `.env.example`.
4. **Phase 3 — Agents:** implement the 9 agent factories.
5. **Phase 4 — Tasks:** implement the 9 task definitions with context passing.
6. **Phase 5 — Crew runner:** `main.py` CLI to execute the crew.
7. **Phase 6 — Content generation:** run crew → Markdown artifacts.
8. **Phase 7 — Visualization:** verify Python graph renders to PNG.
9. **Phase 8 — LaTeX assembly:** `main.tex`, preamble, `references.bib`.
10. **Phase 9 — Compilation:** LuaLaTeX + biber build to PDF.
11. **Phase 10 — Validation:** check F1–F13; iterate until all pass.
12. **Phase 11 — Polish & submit:** README report, final commits, push.

Each phase ends with a **meaningful commit** (and ideally a verify step).

---

## 7. Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| Hebrew BiDi rendering breaks | Use LuaLaTeX + polyglossia; isolate in one chapter; test early |
| Agent output not valid LaTeX | Dedicated LaTeX Converter Agent + compile check + Reviewer pass |
| Missing API keys block run | `.env.example`; document fallbacks; cache intermediate Markdown |
| File exceeds 150 lines | Split modules by responsibility from the start |
| Single giant commit | Commit per phase/artifact; enforce in PROJECT_INSTRUCTIONS |
| Fabricated "results" | PDF Validation Agent + manual page-count/feature check |

---

## 8. Definition of Done

All F1–F13 acceptance criteria pass against a real compiled PDF, the repo builds
from a clean checkout using only the documented UV/CLI commands, every Python
file is < 150 lines, and the commit history is incremental and meaningful.
