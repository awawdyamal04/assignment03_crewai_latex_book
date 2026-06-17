# PROJECT_INSTRUCTIONS.md — Working Rules

These are the **binding rules** for how this project is built. They apply to the
human author and to any AI coding agent assisting on the project. Read this file
before making any change.

---

## 1. Vibe Coding Lifecycle (mandatory order)

```
Idea → PRD → Plan → TODO → Verify → Execute → Push
```

- **Idea:** the chosen topic and goal (locked in `prd.md`).
- **PRD:** `prd.md` defines WHAT must be built. Do not start code until it exists.
- **Plan:** `plan.md` defines HOW. Architecture/decisions live here.
- **TODO:** `todo.md` holds 300–800 small, checkable tasks.
- **Verify:** before executing a task, confirm it matches the plan and PRD.
- **Execute:** implement in small steps, checking off TODO items.
- **Push:** commit incrementally and push to the public GitHub repo.

Documentation comes first. **No Python code is written during the documentation phase.**

---

## 2. CLI-Only Rule

- All work is performed through the **command line**. No GUI/IDE-specific steps.
- Environment, runs, builds, and git are all driven by documented CLI commands.
- Any contributor must be able to reproduce results from a terminal alone.

---

## 3. File-Size Rule

- **Every Python file must be shorter than 150 lines.**
- Prefer many small, single-responsibility modules over one large file.
- If a file approaches the limit, split it by responsibility (e.g. one agent or
  one task per module).
- No single "huge file" containing the whole system.

---

## 4. UV Environment Rule

- The virtual environment and dependencies are managed **only with UV**.
- Use `uv init`, `uv add`, `uv run`, `uv sync` — not bare `pip`/`venv`.
- Dependencies are declared in `pyproject.toml`; keep `requirements.txt` in sync.
- The lockfile is committed so the environment is reproducible.

---

## 5. Commit Rule (Meaningful History)

- Commit **incrementally**: one logical change per commit.
- **No single big upload at the end.** History must show the work progressing.
- Write clear, present-tense commit messages (e.g. `Add Researcher agent factory`).
- Commit at natural boundaries: each doc, each agent, each task, each build step.
- Push regularly to the **public GitHub repository**.

---

## 6. No-Fake-Results Rule

- Never fabricate output, screenshots, page counts, or "passing" checks.
- Every claimed document feature (F1–F12 in `prd.md`) must exist in a **real
  compiled PDF** and be verifiable.
- If something does not work, **say so** and record it; do not pretend it passed.
- The PDF Validation Agent's report must reflect the actual compiled artifact.

---

## 7. No-Destruction Rule

- Do not delete existing files unless explicitly instructed.
- Additive changes preferred; when editing, preserve prior intent and history.

---

## 8. Modularity & Structure Rule

- Follow the directory layout in `plan.md` (`src/`, `content/`, `latex/`,
  `figures/`, `results/`, `prompts/`).
- Keep agents in `src/agents/`, tasks in `src/tasks/`, build helpers in
  `src/pipeline/` — one concern per module.

---

## 9. Secrets Rule

- No API keys or secrets in source control. Use `.env` (git-ignored).
- Document required variables in `.env.example` with placeholder values only.

---

## 10. Definition of Done

A task is done only when it is implemented, verified against `prd.md`/`plan.md`,
its TODO item is checked off, and the change is committed with a meaningful
message. The project is done when all F1–F12 criteria pass on a real PDF built
from a clean checkout via UV/CLI.
