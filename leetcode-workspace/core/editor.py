"""VS Code integration: opens the DSA folder plus the problem/markdown files.

The `code` launcher is started as a fire-and-forget background process
(subprocess.Popen, never waited on) rather than subprocess.run.

Why this matters: on Windows, if no VS Code instance is already running,
`code` becomes the *master* process and stays attached to this console
until every VS Code window is closed. subprocess.run() waits for the
child to exit, so it would block this entire terminal -- and even
swallow Ctrl+C -- until VS Code itself was closed. Popen (with no
.wait()/.communicate() call) sidesteps that: this script hands off the
launch and returns control to the terminal immediately, so `finish.py`
can be run right after in the same window.

Honest limitation: the `code` CLI has no flag to force a true split-editor
layout. Both files are opened as tabs in the same group. Pressing
Ctrl+\\ (Cmd+\\ on macOS) once splits them side by side, and VS Code
remembers that layout for this workspace on future launches.
"""
from __future__ import annotations
import os
import shutil
import subprocess
from pathlib import Path


def _code_available() -> bool:
    return shutil.which("code") is not None


def _detached_kwargs() -> dict:
    """Platform-specific kwargs that fully decouple the child process
    from this script's console, so it can never re-attach Ctrl+C or
    keep the terminal busy."""
    if os.name == "nt":
        return {
            "creationflags": subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP
        }
    return {"start_new_session": True}


def open_workspace(
    project_folder: str,
    problem_file: Path,
    markdown_file: str,
    auto_split: bool = True,
) -> list[str]:
    """Launch VS Code in the background (folder + both files, reusing the
    current window via -r) and return immediately without waiting for it.
    Returns human-readable status lines for console output."""
    status: list[str] = []

    if not _code_available():
        status.append("VS Code 'code' CLI not found on PATH -- skipped auto-open.")
        return status

    try:
        subprocess.Popen(
            ["code", "-r", project_folder, markdown_file, str(problem_file)],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            stdin=subprocess.DEVNULL,
            **_detached_kwargs(),
        )
        status.append(f"Opened folder in VS Code: {project_folder}")
        status.append(f"Opened markdown file: {markdown_file}")
        status.append(f"Opened problem file: {problem_file}")

        if auto_split:
            status.append(
                "Tip: press Ctrl+\\ (Cmd+\\ on Mac) once to split these two "
                "tabs side by side -- VS Code remembers the layout after that."
            )
    except OSError as exc:
        status.append(f"Failed to open VS Code: {exc}")

    return status
