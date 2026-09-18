"""Entry point: closes the active solve session and logs it to CSV.

    python finish.py
"""
from __future__ import annotations
from core.config import load_config
from core.exceptions import LCWorkspaceError
from core.session import load_session, compute_elapsed, delete_session
from core.csv_logger import log_entry
from core import console as ui


def main() -> None:
    ui.show_banner()

    try:
        config = load_config()
    except LCWorkspaceError as exc:
        ui.show_error(str(exc))
        return

    try:
        session = load_session(config.session_file)
    except LCWorkspaceError as exc:
        ui.show_error(str(exc))
        return

    if session is None:
        ui.console.print("[yellow]No active solve session.[/yellow]")
        return

    elapsed = compute_elapsed(session)
    status = ui.prompt_finish_status()
    notes = ui.prompt_multiline_notes()

    try:
        log_entry(
            config.csv_log, session.problem, session.title,
            session.difficulty, status, elapsed, notes,
        )
    except OSError as exc:
        ui.show_error(f"Could not write to CSV log: {exc}")
        return

    delete_session(config.session_file)
    ui.step("Logged to CSV")
    ui.step("Session closed")
    ui.show_finish_summary(session.title, status, elapsed)


if __name__ == "__main__":
    main()
