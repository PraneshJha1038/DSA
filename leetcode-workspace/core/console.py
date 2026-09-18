"""Rich-based console UI helpers -- all user-facing output goes through here.

This module owns the visual identity of the CLI: the banner, step-by-step
progress reporting, panels, and prompts. No other module should print
directly to the terminal.
"""
from __future__ import annotations
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.prompt import Prompt, Confirm
from rich.align import Align
from rich import box

console = Console()

_BANNER = r"""
 _        _______  _______ _________ _______  _______  ______   _______
( \      (  ____ \(  ____ \\__   __/(  ____ \(  ___  )(  __  \ (  ____ \
| (      | (    \/| (    \/   ) (   | (    \/| (   ) || (  \  )| (    \/
| |      | (__    | (__       | |   | |      | |   | || |   ) || (__
| |      |  __)   |  __)      | |   | |      | |   | || |   | ||  __)
| |      | (      | (         | |   | |      | |   | || |   ) || (
| (____/\| (____/\| (____/\   | |   | (____/\| (___) || (__/  )| (____/\
(_______/(_______/(_______/   )_(   (_______/(_______)(______/ (_______/
"""

_DIFFICULTY_COLOR = {
    "Easy": "green",
    "Medium": "yellow",
    "Hard": "red",
}
_DIFFICULTY_EMOJI = {
    "Easy": "🟢",
    "Medium": "🟡",
    "Hard": "🔴",
}

STATUS_COLOR = {
    "Solved": "green",
    "Partially Solved": "yellow",
    "Editorial": "blue",
    "Couldn't Solve": "red",
}
STATUS_REACTION = {
    "Solved": "🎉 Nailed it!",
    "Partially Solved": "🙂 Solid progress!",
    "Editorial": "📖 Good learning rep!",
    "Couldn't Solve": "💪 Next one's yours!",
}

STEP_ICONS = {
    "done": "[bold green]✓[/bold green]",
    "info": "[bold cyan]➜[/bold cyan]",
    "warn": "[bold yellow]![/bold yellow]",
}


def show_banner() -> None:
    """Print the ASCII LeetCode wordmark banner once at startup."""
    console.print(Text(_BANNER, style="bold yellow"), justify="center")
    console.rule(style="yellow")


def prompt_problem_number() -> int:
    """Prompt until a valid positive integer problem number is entered."""
    while True:
        raw = Prompt.ask("[bold cyan]📋 Enter LeetCode Problem Number[/]")
        if raw.isdigit() and int(raw) > 0:
            return int(raw)
        console.print("[red]✗ Please enter a valid positive integer.[/red]")


def show_error(message: str) -> None:
    console.print(
        Panel(
            f"[bold red]{message}[/bold red]",
            title="[bold red]✗ Error[/bold red]",
            border_style="red",
            box=box.ROUNDED,
        )
    )


def show_problem_card(problem_id: int, title: str, difficulty: str, topics: list[str]) -> None:
    """Show a compact card confirming what was fetched, before the step list."""
    color = _DIFFICULTY_COLOR.get(difficulty, "white")
    emoji = _DIFFICULTY_EMOJI.get(difficulty, "⚪")
    body = Text()
    body.append(f"{problem_id}. {title}\n", style="bold white")
    body.append("Difficulty: ", style="dim")
    body.append(f"{emoji} {difficulty}\n", style=f"bold {color}")
    body.append("Topics: ", style="dim")
    body.append(", ".join(topics) if topics else "-", style="cyan")
    console.print(Panel(body, title="🧩 Problem", border_style="blue", box=box.ROUNDED))


def step(message: str, kind: str = "done") -> None:
    """Print a single live progress line as work happens, e.g.
    '✓ Markdown generated'. kind: 'done' | 'info' | 'warn'."""
    icon = STEP_ICONS.get(kind, STEP_ICONS["done"])
    console.print(f"  {icon} {message}")


def show_success_summary(steps: list[str]) -> None:
    body = "\n".join(f"[bold green]✓[/bold green] {s}" for s in steps)
    console.print(
        Panel(
            body,
            title="[bold green]🚀 Ready to code[/bold green]",
            border_style="green",
            box=box.ROUNDED,
        )
    )


def confirm_overwrite(path) -> bool:
    return Confirm.ask(f"[yellow]⚠ {path} already exists. Overwrite?[/yellow]", default=False)


def show_session_conflict_table(session) -> str:
    """Display the conflicting active session and ask resume/discard/cancel."""
    table = Table(title="⏳ Active Session Detected", box=box.ROUNDED, border_style="yellow")
    table.add_column("Field", style="dim")
    table.add_column("Value", style="bold white")
    table.add_row("Problem", str(session.problem))
    table.add_row("Title", session.title)
    table.add_row("Started", session.started_at)
    console.print(table)
    return Prompt.ask(
        "[bold]Resume, Discard, or Cancel?[/bold]",
        choices=["resume", "discard", "cancel"],
        default="cancel",
    )


def prompt_finish_status() -> str:
    console.print(
        "[dim]✅ Solved   🌓 Partially Solved   📖 Editorial   ❌ Couldn't Solve[/dim]"
    )
    return Prompt.ask(
        "[bold cyan]📝 Status[/]",
        choices=["Solved", "Partially Solved", "Editorial", "Couldn't Solve"],
    )


def prompt_multiline_notes() -> str:
    console.print("[dim]Enter notes. Type END on its own line to finish.[/dim]")
    lines: list[str] = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        lines.append(line)
    return "\n".join(lines)


def show_finish_summary(title: str, status: str, elapsed: str) -> None:
    status_color = STATUS_COLOR.get(status, "white")
    reaction = STATUS_REACTION.get(status, "")

    body = Text()
    body.append(f"{title}\n\n", style="bold white")
    body.append("Status: ", style="dim")
    body.append(f"{status}", style=f"bold {status_color}")
    if reaction:
        body.append(f"   {reaction}", style=f"bold {status_color}")
    body.append("\n")
    body.append("Time taken: ", style="dim")
    body.append(f"{elapsed}\n", style="bold cyan")
    body.append("Logged to CSV. Session closed.", style="dim")

    console.print(Panel(body, title="🏁 Session Complete", border_style=status_color, box=box.ROUNDED))
