"""Assemble the sequential CrewAI crew from the agent and task specs.

This module imports CrewAI and is used only for a real run (Phase 5+). The
Phase 2 CLI modes (show-agents, show-tasks, dry-run) do not call it, so they
never require an LLM provider or API key.
"""

from __future__ import annotations

from src.config import get_api_key


def build_tools() -> dict[str, object]:
    """Resolve the toolset, degrading gracefully when keys are absent.

    Returns a mapping of tool name -> instance. A tool is only included when
    it can be constructed; missing keys simply omit that tool.
    """
    tools: dict[str, object] = {}
    try:
        from crewai_tools import FileReadTool

        tools["file_read"] = FileReadTool()
    except Exception:  # pragma: no cover - optional tool
        pass

    if get_api_key("SERPER_API_KEY"):
        try:
            from crewai_tools import SerperDevTool

            tools["search"] = SerperDevTool()
        except Exception:  # pragma: no cover - optional tool
            pass
    return tools


def build_crew(tools: dict[str, object] | None = None):
    """Build a sequential ``crewai.Crew`` wiring all agents and tasks.

    Output flows from one task to the next through each task's ``context``
    (see ``src/tasks/definitions.py``), under ``Process.sequential``.
    """
    from crewai import Crew, Process

    from src.agents.definitions import build_agents
    from src.tasks.definitions import build_tasks

    tools = build_tools() if tools is None else tools
    agents = build_agents(tools)
    tasks = build_tasks(agents)

    return Crew(
        agents=list(agents.values()),
        tasks=list(tasks.values()),
        process=Process.sequential,
        verbose=True,
    )
