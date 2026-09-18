"""Generates the formatted problem markdown file."""
from __future__ import annotations
from pathlib import Path
from core.models import Problem


def generate_markdown(problem: Problem) -> str:
    """Build the full Markdown document for a problem."""
    lines = [
        f"# {problem.id}. {problem.title}",
        "",
        f"**Difficulty:** {problem.difficulty}",
        f"**Topics:** {', '.join(problem.topics) if problem.topics else '-'}",
        "",
        "---",
        "",
        "## Description",
        "",
        problem.parsed.description,
        "",
        "---",
        "",
    ]

    for i, ex in enumerate(problem.parsed.examples, start=1):
        lines += [f"## Example {i}", ""]
        lines += ["**Input:**", "```", ex.input, "```"]
        lines += ["**Output:**", "```", ex.output, "```"]
        if ex.explanation:
            lines += ["**Explanation:**", ex.explanation]
        lines += ["", "---", ""]

    lines += ["## Constraints", ""]
    lines += [f"- {c}" for c in problem.parsed.constraints] or ["- (none listed)"]
    lines += [""]

    return "\n".join(lines)


def write_markdown(problem: Problem, path: str) -> None:
    """Always overwrite the markdown file -- no prompt, per spec."""
    Path(path).write_text(generate_markdown(problem), encoding="utf-8")
