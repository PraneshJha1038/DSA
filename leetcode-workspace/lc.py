"""Entry point: creates a local workspace for a given LeetCode problem.

    python lc.py
"""
from __future__ import annotations
import datetime

from core.config import load_config
from core.exceptions import LCWorkspaceError
from core.api import resolve_slug_by_number, fetch_question, get_python_snippet
from core.parser import parse_content_html
from core.models import Problem
from core.markdown_generator import write_markdown
from core.python_generator import write_python_file
from core.session import load_session, start_new_session, delete_session
from core.editor import open_workspace
from core import console as ui


def main() -> None:
    ui.show_banner()

    try:
        config = load_config()
    except LCWorkspaceError as exc:
        ui.show_error(str(exc))
        return

    try:
        existing = load_session(config.session_file)
    except LCWorkspaceError as exc:
        ui.show_error(str(exc))
        ui.console.print("[yellow]Delete or fix session.json manually, then re-run.[/yellow]")
        return

    if existing is not None:
        choice = ui.show_session_conflict_table(existing)
        if choice == "cancel":
            return
        if choice == "discard":
            delete_session(config.session_file)
        # "resume" falls through -- a new workspace can still be generated below

    problem_number = ui.prompt_problem_number()

    try:
        with ui.console.status("[bold cyan]Resolving problem...[/]"):
            slug, difficulty = resolve_slug_by_number(problem_number)
        ui.step("Problem resolved")

        with ui.console.status("[bold cyan]Fetching problem details...[/]"):
            question = fetch_question(slug)
            starter_code = get_python_snippet(question)
            parsed = parse_content_html(question["content"])
        ui.step("Problem downloaded")
    except LCWorkspaceError as exc:
        ui.show_error(str(exc))
        return

    topics = [t["name"] for t in question.get("topicTags", [])]
    problem = Problem(
        id=problem_number,
        title=question["title"],
        slug=slug,
        difficulty=difficulty,
        topics=topics,
        starter_code=starter_code,
        parsed=parsed,
    )
    ui.show_problem_card(problem.id, problem.title, problem.difficulty, problem.topics)

    write_markdown(problem, config.markdown_file)
    ui.step("Markdown generated")

    started_at = datetime.datetime.now()
    try:
        py_path = write_python_file(
            problem, config.leetcode_folder, started_at,
            overwrite_check=ui.confirm_overwrite,
        )
    except FileExistsError as exc:
        ui.show_error(str(exc))
        return
    ui.step("Python template created")

    start_new_session(config.session_file, problem.id, problem.title, problem.difficulty)
    ui.step("Session started")

    editor_lines: list[str] = []
    if config.auto_open_vscode:
        editor_lines = open_workspace(
            config.vscode_project_folder, py_path, config.markdown_file,
            auto_split=config.auto_split_editor,
        )
        for line in editor_lines:
            ui.step(line, kind="info")

    ui.show_success_summary([
        "Problem downloaded",
        "Markdown generated",
        "Python template created",
        "Session started",
        *editor_lines,
    ])


if __name__ == "__main__":
    main()
