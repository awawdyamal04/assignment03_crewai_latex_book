# todo.md — Detailed Task List

Granular, checkable tasks for Assignment 03, ordered by the phases in
[`plan.md`](./plan.md). Check off `[x]` as each is completed. Follow the rules in
[`PROJECT_INSTRUCTIONS.md`](./PROJECT_INSTRUCTIONS.md). Tasks are intentionally
small so the commit history stays meaningful.

**Legend:** `[ ]` todo · `[x]` done · _(verify)_ = run a check before moving on.

---

## Phase 0 — Documentation (Idea → PRD → Plan → TODO)

- [ ] 0.1 Confirm the chosen topic with the assignment brief
- [ ] 0.2 Confirm course number 203.3763 is recorded everywhere
- [ ] 0.3 Create `prd.md` describing WHAT the project must do
- [ ] 0.4 List all 13 mandatory PDF features (F1–F13) in `prd.md`
- [ ] 0.5 Define acceptance criteria for each feature in `prd.md`
- [ ] 0.6 List the 9 required agents in `prd.md`
- [ ] 0.7 Record methodological requirements in `prd.md`
- [ ] 0.8 Record technical requirements in `prd.md`
- [ ] 0.9 Create `plan.md` describing HOW the project is built
- [ ] 0.10 Add architecture diagram to `plan.md`
- [ ] 0.11 Add technology-stack table to `plan.md`
- [ ] 0.12 Add project-structure tree to `plan.md`
- [ ] 0.13 Add agent/task design table to `plan.md`
- [ ] 0.14 Add LaTeX/build strategy to `plan.md`
- [ ] 0.15 Add phased build order to `plan.md`
- [ ] 0.16 Add risks & mitigations to `plan.md`
- [ ] 0.17 Create `todo.md` with 300–800 tasks (this file)
- [ ] 0.18 Create `README.md` as the final report template
- [ ] 0.19 Add F1–F13 status checklist to `README.md`
- [ ] 0.20 Create `PROJECT_INSTRUCTIONS.md` with all working rules
- [ ] 0.21 Document the Vibe Coding lifecycle in `PROJECT_INSTRUCTIONS.md`
- [ ] 0.22 Document the CLI-only rule
- [ ] 0.23 Document the < 150-line file-size rule
- [ ] 0.24 Document the UV environment rule
- [ ] 0.25 Document the meaningful-commit rule
- [ ] 0.26 Document the no-fake-results rule
- [ ] 0.27 Review all five docs for consistency
- [ ] 0.28 Commit the documentation set with a meaningful message
- [ ] 0.29 Print the final file tree to confirm structure

---

## Phase 1 — Repository Scaffolding & UV Setup

- [ ] 1.1 Verify UV is installed (`uv --version`)
- [ ] 1.2 Initialize the project with `uv init` (preserve existing docs)
- [ ] 1.3 Confirm `pyproject.toml` was created
- [ ] 1.4 Set project name in `pyproject.toml`
- [ ] 1.5 Set Python version requirement (>=3.11) in `pyproject.toml`
- [ ] 1.6 Add project description/metadata to `pyproject.toml`
- [ ] 1.7 Create `.gitignore`
- [ ] 1.8 Ignore `.venv/` in `.gitignore`
- [ ] 1.9 Ignore `.env` in `.gitignore`
- [ ] 1.10 Ignore `__pycache__/` and `*.pyc` in `.gitignore`
- [ ] 1.11 Ignore LaTeX aux files (`*.aux *.log *.toc *.out *.bbl *.bcf *.blg *.run.xml`)
- [ ] 1.12 Ignore `results/*.pdf`? (decide: keep final PDF tracked) — document choice
- [ ] 1.13 Create `src/` directory
- [ ] 1.14 Create `src/__init__.py`
- [ ] 1.15 Create `src/agents/` directory with `__init__.py`
- [ ] 1.16 Create `src/tasks/` directory with `__init__.py`
- [ ] 1.17 Create `src/pipeline/` directory with `__init__.py`
- [ ] 1.18 Create `content/` directory (with `.gitkeep`)
- [ ] 1.19 Create `latex/` directory (with `.gitkeep`)
- [ ] 1.20 Create `figures/` directory (with `.gitkeep`)
- [ ] 1.21 Create `results/` directory (with `.gitkeep`)
- [ ] 1.22 Create `prompts/` directory (with `.gitkeep`)
- [ ] 1.23 Add `crewai` dependency via `uv add crewai`
- [ ] 1.24 Add `crewai-tools` dependency via `uv add crewai-tools`
- [ ] 1.25 Add `matplotlib` dependency via `uv add matplotlib`
- [ ] 1.26 Add `python-dotenv` dependency via `uv add python-dotenv`
- [ ] 1.27 Add any plotting/data deps (numpy) via `uv add numpy`
- [ ] 1.28 Run `uv sync` and confirm the lockfile is created
- [ ] 1.29 Generate/refresh `requirements.txt` to mirror locked deps
- [ ] 1.30 Create `.env.example` with placeholder keys (no secrets)
- [ ] 1.31 Document `OPENAI_API_KEY` (or chosen LLM key) in `.env.example`
- [ ] 1.32 Document `SERPER_API_KEY` in `.env.example`
- [ ] 1.33 Verify `.env` is git-ignored (not staged)
- [ ] 1.34 Confirm `uv run python -c "import crewai"` works
- [ ] 1.35 Commit: project scaffolding + UV setup
- [ ] 1.36 Commit: directory skeleton with `.gitkeep` files
- [ ] 1.37 Commit: dependency manifest + lockfile

---

## Phase 2 — Config & Tools

- [ ] 2.1 Create `src/config.py`
- [ ] 2.2 Load environment variables via `python-dotenv` in `config.py`
- [ ] 2.3 Define base project paths (root, content, latex, figures, results, prompts)
- [ ] 2.4 Define the LLM model name/config in `config.py`
- [ ] 2.5 Add a helper to ensure output directories exist
- [ ] 2.6 Add a helper to read API keys safely (clear error if missing)
- [ ] 2.7 Keep `config.py` under 150 lines _(verify)_
- [ ] 2.8 Create `src/tools.py`
- [ ] 2.9 Wire up the web search tool (SerperDevTool)
- [ ] 2.10 Add a guard so search tool degrades gracefully without a key
- [ ] 2.11 Wire up a file-reading tool/logic for local course notes
- [ ] 2.12 Expose a function returning the toolset for agents
- [ ] 2.13 Keep `tools.py` under 150 lines _(verify)_
- [ ] 2.14 Add reusable prompt fragments under `prompts/`
- [ ] 2.15 Write the Researcher backstory fragment in `prompts/`
- [ ] 2.16 Write the Writer style-guide fragment in `prompts/`
- [ ] 2.17 Write the Bilingual BiDi guidance fragment in `prompts/`
- [ ] 2.18 Write the LaTeX conventions fragment in `prompts/`
- [ ] 2.19 Commit: config module
- [ ] 2.20 Commit: tools module
- [ ] 2.21 Commit: prompt fragments

---

## Phase 3 — Agents (one small module each)

### Researcher Agent
- [ ] 3.1 Create `src/agents/researcher.py`
- [ ] 3.2 Define role, goal, backstory
- [ ] 3.3 Attach the search tool
- [ ] 3.4 Expose a factory function `build_researcher()`
- [ ] 3.5 Keep file under 150 lines _(verify)_

### Course Material Analyst Agent
- [ ] 3.6 Create `src/agents/course_analyst.py`
- [ ] 3.7 Define role, goal, backstory
- [ ] 3.8 Attach file-read tool for local notes
- [ ] 3.9 Expose `build_course_analyst()`
- [ ] 3.10 Keep file under 150 lines _(verify)_

### Writer Agent
- [ ] 3.11 Create `src/agents/writer.py`
- [ ] 3.12 Define role, goal, backstory (academic tone)
- [ ] 3.13 Expose `build_writer()`
- [ ] 3.14 Keep file under 150 lines _(verify)_

### Bilingual Chapter Agent
- [ ] 3.15 Create `src/agents/bilingual.py`
- [ ] 3.16 Define role, goal, backstory (Hebrew+English BiDi)
- [ ] 3.17 Add guidance on correct RTL/LTR mixing
- [ ] 3.18 Expose `build_bilingual()`
- [ ] 3.19 Keep file under 150 lines _(verify)_

### Python Visualization Agent
- [ ] 3.20 Create `src/agents/visualization.py`
- [ ] 3.21 Define role, goal, backstory (writes matplotlib code)
- [ ] 3.22 Expose `build_visualization()`
- [ ] 3.23 Keep file under 150 lines _(verify)_

### Table & Formula Agent
- [ ] 3.24 Create `src/agents/table_formula.py`
- [ ] 3.25 Define role, goal, backstory
- [ ] 3.26 Expose `build_table_formula()`
- [ ] 3.27 Keep file under 150 lines _(verify)_

### Reviewer Agent
- [ ] 3.28 Create `src/agents/reviewer.py`
- [ ] 3.29 Define role, goal, backstory (accuracy/coherence checks)
- [ ] 3.30 Expose `build_reviewer()`
- [ ] 3.31 Keep file under 150 lines _(verify)_

### LaTeX Converter Agent
- [ ] 3.32 Create `src/agents/latex_converter.py`
- [ ] 3.33 Define role, goal, backstory (Markdown → valid .tex)
- [ ] 3.34 Add LaTeX conventions to backstory/goal
- [ ] 3.35 Expose `build_latex_converter()`
- [ ] 3.36 Keep file under 150 lines _(verify)_

### PDF Validation Agent
- [ ] 3.37 Create `src/agents/pdf_validation.py`
- [ ] 3.38 Define role, goal, backstory (checks F1–F13)
- [ ] 3.39 Expose `build_pdf_validation()`
- [ ] 3.40 Keep file under 150 lines _(verify)_

### Agents wiring
- [ ] 3.41 Export all agent factories from `src/agents/__init__.py`
- [ ] 3.42 Smoke-test importing every agent factory
- [ ] 3.43 Commit: Researcher + Course Analyst agents
- [ ] 3.44 Commit: Writer + Bilingual agents
- [ ] 3.45 Commit: Visualization + Table/Formula agents
- [ ] 3.46 Commit: Reviewer + LaTeX Converter + Validation agents

---

## Phase 4 — Tasks (with sequential context passing)

### Research task
- [ ] 4.1 Create `src/tasks/research_task.py`
- [ ] 4.2 Write description (gather sources on RNN→Transformers→agents)
- [ ] 4.3 Write expected_output (sourced notes + reference candidates)
- [ ] 4.4 Set output file `content/research.md`
- [ ] 4.5 Keep file under 150 lines _(verify)_

### Course alignment task
- [ ] 4.6 Create `src/tasks/course_task.py`
- [ ] 4.7 Write description (align with course concepts + outline)
- [ ] 4.8 Set `context=[research_task]`
- [ ] 4.9 Set output file `content/course_alignment.md`
- [ ] 4.10 Keep file under 150 lines _(verify)_

### Writing task
- [ ] 4.11 Create `src/tasks/writing_task.py`
- [ ] 4.12 Write description (full English draft, 6 chapters)
- [ ] 4.13 Set `context=[research_task, course_task]`
- [ ] 4.14 Set output file `content/draft.md`
- [ ] 4.15 Keep file under 150 lines _(verify)_

### Bilingual task
- [ ] 4.16 Create `src/tasks/bilingual_task.py`
- [ ] 4.17 Write description (one chapter mixing Hebrew+English)
- [ ] 4.18 Set `context=[writing_task]`
- [ ] 4.19 Set output file `content/bilingual.md`
- [ ] 4.20 Keep file under 150 lines _(verify)_

### Visualization task
- [ ] 4.21 Create `src/tasks/visualization_task.py`
- [ ] 4.22 Write description (generate matplotlib script + PNG)
- [ ] 4.23 Set `context=[writing_task]`
- [ ] 4.24 Set output `figures/plot.py` (+ produced PNG)
- [ ] 4.25 Keep file under 150 lines _(verify)_

### Table & formula task
- [ ] 4.26 Create `src/tasks/table_formula_task.py`
- [ ] 4.27 Write description (one table + one complex formula)
- [ ] 4.28 Set `context=[writing_task]`
- [ ] 4.29 Set output file `content/tables_formulas.md`
- [ ] 4.30 Keep file under 150 lines _(verify)_

### Review task
- [ ] 4.31 Create `src/tasks/review_task.py`
- [ ] 4.32 Write description (verify accuracy/structure/coherence)
- [ ] 4.33 Set `context=[writing_task, bilingual_task, table_formula_task]`
- [ ] 4.34 Set output file `content/reviewed.md`
- [ ] 4.35 Keep file under 150 lines _(verify)_

### LaTeX conversion task
- [ ] 4.36 Create `src/tasks/latex_task.py`
- [ ] 4.37 Write description (assemble valid `main.tex`)
- [ ] 4.38 Set `context=[reviewed, bilingual, visualization, table_formula]`
- [ ] 4.39 Set output file `latex/main.tex`
- [ ] 4.40 Keep file under 150 lines _(verify)_

### Validation task
- [ ] 4.41 Create `src/tasks/validation_task.py`
- [ ] 4.42 Write description (check F1–F13 in compiled PDF)
- [ ] 4.43 Set `context=[latex_task]`
- [ ] 4.44 Set output file `results/validation.md`
- [ ] 4.45 Keep file under 150 lines _(verify)_

### Tasks wiring
- [ ] 4.46 Export task builders from `src/tasks/__init__.py`
- [ ] 4.47 Verify each task references the correct predecessor context
- [ ] 4.48 Commit: research + course tasks
- [ ] 4.49 Commit: writing + bilingual tasks
- [ ] 4.50 Commit: visualization + table/formula tasks
- [ ] 4.51 Commit: review + latex + validation tasks

---

## Phase 5 — Crew Runner (CLI entrypoint)

- [ ] 5.1 Create `src/main.py`
- [ ] 5.2 Build all 9 agents via their factories
- [ ] 5.3 Build all 9 tasks with context wiring
- [ ] 5.4 Assemble a `Crew` with `Process.sequential`
- [ ] 5.5 Add CLI argument parsing (e.g. `--dry-run`, `--only research`)
- [ ] 5.6 Ensure output directories exist before running
- [ ] 5.7 Add basic logging of each step
- [ ] 5.8 Add graceful error handling for missing keys
- [ ] 5.9 Write `crew.kickoff()` invocation
- [ ] 5.10 Persist each task output to its target file
- [ ] 5.11 Keep `main.py` under 150 lines _(verify; split into pipeline/ if needed)_
- [ ] 5.12 Create `src/pipeline/build_crew.py` if `main.py` grows too large
- [ ] 5.13 Smoke-test `uv run python -m src.main --dry-run`
- [ ] 5.14 Commit: crew runner / CLI entrypoint

---

## Phase 6 — Content Generation (run the crew)

- [ ] 6.1 Provide real API keys in local `.env`
- [ ] 6.2 Run the Researcher step and inspect `content/research.md`
- [ ] 6.3 Verify research includes citable, real sources
- [ ] 6.4 Run Course Analyst and inspect `content/course_alignment.md`
- [ ] 6.5 Confirm outline covers all 6 required topics
- [ ] 6.6 Run Writer and inspect `content/draft.md`
- [ ] 6.7 Confirm draft has ≥6 chapters
- [ ] 6.8 Confirm draft length is sufficient for ~15 pages
- [ ] 6.9 Run Bilingual agent and inspect `content/bilingual.md`
- [ ] 6.10 Confirm Hebrew + English are both present and meaningful
- [ ] 6.11 Run Table & Formula agent and inspect output
- [ ] 6.12 Confirm a real table and a complex formula are specified
- [ ] 6.13 Run Reviewer and inspect `content/reviewed.md`
- [ ] 6.14 Address any issues the Reviewer raised
- [ ] 6.15 Re-run affected steps if the Reviewer requested changes
- [ ] 6.16 Commit: generated research + alignment artifacts
- [ ] 6.17 Commit: generated draft + bilingual chapter
- [ ] 6.18 Commit: generated tables/formulas + review notes

---

## Phase 7 — Python-Generated Visualization

- [ ] 7.1 Inspect agent-written `figures/plot.py`
- [ ] 7.2 Confirm the script is < 150 lines
- [ ] 7.3 Confirm the script uses matplotlib (no GUI backend)
- [ ] 7.4 Run `uv run python figures/plot.py`
- [ ] 7.5 Confirm a PNG is produced in `figures/`
- [ ] 7.6 Verify the figure is relevant (e.g. attention/scaling/perf chart)
- [ ] 7.7 Verify axis labels, title, and legend are present
- [ ] 7.8 Confirm the figure resolution is print-quality (dpi)
- [ ] 7.9 Fix the script if it errors and re-run
- [ ] 7.10 Confirm the figure filename matches what `main.tex` expects
- [ ] 7.11 Commit: Python plotting script
- [ ] 7.12 Commit: generated figure PNG

---

## Phase 8 — LaTeX Assembly

- [ ] 8.1 Inspect agent-produced `latex/main.tex`
- [ ] 8.2 Set document class (e.g. `report` or `article`)
- [ ] 8.3 Add LuaLaTeX preamble (`fontspec`)
- [ ] 8.4 Configure Hebrew + English via `polyglossia` (or `babel`+`bidi`)
- [ ] 8.5 Select fonts that support Hebrew glyphs
- [ ] 8.6 Add `amsmath`/`amssymb` for math
- [ ] 8.7 Add `graphicx` for the figure
- [ ] 8.8 Add `booktabs` for the table
- [ ] 8.9 Add `fancyhdr` and configure headers/footers
- [ ] 8.10 Add `hyperref` for clickable links
- [ ] 8.11 Add `biblatex` with backend `biber`
- [ ] 8.12 Create `latex/references.bib` with real entries
- [ ] 8.13 Add ≥6 real references (RNN, LSTM, Attention, CrewAI, etc.)
- [ ] 8.14 Build the title page (course 203.3763, lecturer, student, date)
- [ ] 8.14a Add a short English abstract after the title page (F13)
- [ ] 8.15 Add `\tableofcontents`
- [ ] 8.16 Add chapter/section structure for all 6 topics
- [ ] 8.17 Insert the figure with `\includegraphics` + caption + label
- [ ] 8.18 Insert the table with `booktabs` + caption + label
- [ ] 8.19 Insert the complex formula (scaled dot-product attention)
- [ ] 8.20 Insert the bilingual Hebrew/English chapter content
- [ ] 8.21 Add `\cite{...}` calls throughout the body
- [ ] 8.22 Add `\printbibliography`
- [ ] 8.23 Add internal cross-references (`\ref`, `\autoref`)
- [ ] 8.24 Add at least one external hyperlink (`\href`)
- [ ] 8.25 Split preamble into `latex/preamble.tex` if `main.tex` is too large
- [ ] 8.26 Verify no single `.tex` becomes unwieldy (modularize)
- [ ] 8.27 Commit: LaTeX preamble + document skeleton
- [ ] 8.28 Commit: references.bib
- [ ] 8.29 Commit: assembled main.tex with all content

---

## Phase 9 — Compilation (LuaLaTeX + biber)

- [ ] 9.1 Confirm `lualatex` is on PATH (`lualatex --version`)
- [ ] 9.2 Confirm `biber` is on PATH (`biber --version`)
- [ ] 9.3 First pass: `lualatex main.tex`
- [ ] 9.4 Resolve any preamble/package errors
- [ ] 9.5 Run `biber main`
- [ ] 9.6 Resolve any bibliography errors
- [ ] 9.7 Second pass: `lualatex main.tex`
- [ ] 9.8 Third pass: `lualatex main.tex` (finalize TOC/refs)
- [ ] 9.9 Confirm zero fatal errors in the log
- [ ] 9.10 Review warnings (overfull boxes, undefined refs)
- [ ] 9.11 Fix undefined references / citations
- [ ] 9.12 Confirm the output PDF is generated
- [ ] 9.13 Move/copy final PDF to `results/`
- [ ] 9.14 Optionally add a `src/pipeline/compile.py` helper (< 150 lines)
- [ ] 9.15 Optionally add a `latexmk` config for one-command builds
- [ ] 9.16 Document the exact build command in `README.md`
- [ ] 9.17 Commit: build helper / compile script
- [ ] 9.18 Commit: compiled PDF in results/

---

## Phase 10 — Validation (F1–F13 against the real PDF)

- [ ] 10.1 Open the compiled PDF
- [ ] 10.2 F1: Count pages — confirm ~15 (14–17) of content
- [ ] 10.3 F2: Confirm title page shows course 203.3763
- [ ] 10.4 F2: Confirm lecturer name present
- [ ] 10.5 F2: Confirm student name present
- [ ] 10.6 F2: Confirm date present
- [ ] 10.7 F3: Confirm TOC exists with correct page numbers
- [ ] 10.8 F4: Confirm ≥6 chapters/sections
- [ ] 10.9 F5: Confirm headers appear on body pages
- [ ] 10.10 F5: Confirm footers/page numbers appear
- [ ] 10.11 F6: Confirm the image renders correctly
- [ ] 10.12 F7: Confirm the table renders correctly
- [ ] 10.13 F8: Confirm the complex formula renders correctly
- [ ] 10.14 F9: Confirm the Python-generated graph appears
- [ ] 10.15 F10: Confirm Hebrew text renders (no missing glyphs)
- [ ] 10.16 F10: Confirm English+Hebrew mix in one chapter is correct (BiDi)
- [ ] 10.17 F11: Confirm citations render as `[n]`/author-year
- [ ] 10.18 F11: Confirm bibliography lists all references (≥6 real sources)
- [ ] 10.18a F13: Confirm a short English abstract appears before the body
- [ ] 10.19 F12: Click an internal TOC link — confirm it jumps
- [ ] 10.20 F12: Click an external URL/DOI — confirm it opens
- [ ] 10.21 Run the PDF Validation Agent and read `results/validation.md`
- [ ] 10.22 Reconcile agent report with manual checks (no fake passes)
- [ ] 10.23 Fix any failing feature and recompile
- [ ] 10.24 Re-validate until all F1–F13 pass
- [ ] 10.25 Update the F1–F13 checklist in `README.md` with real status
- [ ] 10.26 Commit: validation report
- [ ] 10.27 Commit: fixes from validation round

---

## Phase 11 — Polish, Report & Submit (Push)

- [ ] 11.1 Fill in lecturer/student/date in `README.md`
- [ ] 11.2 Fill in the public repo URL in `README.md`
- [ ] 11.3 Complete the Results & Reflection section in `README.md`
- [ ] 11.4 Proofread the compiled PDF end-to-end
- [ ] 11.5 Verify every Python file is < 150 lines (final sweep)
- [ ] 11.6 Verify no secrets are committed
- [ ] 11.7 Verify `.env.example` is complete and accurate
- [ ] 11.8 Run `uv sync` from a clean clone to confirm reproducibility
- [ ] 11.9 Confirm the documented build reproduces the PDF
- [ ] 11.10 Review the full commit history for meaningfulness
- [ ] 11.11 Squash nothing essential; keep incremental history
- [ ] 11.12 Create the public GitHub repository
- [ ] 11.13 Add the remote and push `main`
- [ ] 11.14 Confirm the repo is public and renders the README
- [ ] 11.15 Final commit: README report completed
- [ ] 11.16 Tag/release the submission (optional)
- [ ] 11.17 Submit the repository URL per course instructions

---

## Cross-Cutting / Continuous Checks

- [ ] C.1 After every new Python file, confirm it is < 150 lines
- [ ] C.2 After every phase, make at least one meaningful commit
- [ ] C.3 Never commit `.env` or API keys
- [ ] C.4 Keep all work reproducible from the CLI with UV
- [ ] C.5 Do not delete existing files without explicit instruction
- [ ] C.6 Do not fabricate any result or feature status
- [ ] C.7 Keep agents/tasks one-concern-per-module
- [ ] C.8 Keep documentation in sync with implementation
- [ ] C.9 Re-run the crew end-to-end after major changes
- [ ] C.10 Back up intermediate Markdown artifacts before re-runs
