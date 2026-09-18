"""Generates the runnable Python solution template file."""
from __future__ import annotations
import datetime
import re
from pathlib import Path
from typing import Callable
from core.models import Problem
from core.parser import extract_function_name, generate_test_harness

_DEF_PATTERN = re.compile(r"^(\s*)def\s+\w+\(.*\)\s*(?:->\s*(?P<ret>.+?))?\s*:\s*$")


def _default_return_expr(ret_type: str | None) -> str:
    """Pick a type-appropriate placeholder return so the stub runs cleanly
    and doesn't silently return None where the signature promises a real
    value (e.g. an empty list instead of None for a List[int] return)."""
    if not ret_type:
        return "pass"

    t = ret_type.strip()
    simple = {
        "int": "return 0",
        "float": "return 0.0",
        "bool": "return False",
        "str": 'return ""',
    }
    if t in simple:
        return simple[t]

    if t.startswith(("List[", "list[")) or t in ("List", "list"):
        return "return []"
    if t.startswith(("Dict[", "dict[")) or t in ("Dict", "dict"):
        return "return {}"
    if t.startswith(("Set[", "set[")) or t in ("Set", "set"):
        return "return set()"
    if t.startswith(("Tuple[", "tuple[")) or t in ("Tuple", "tuple"):
        return "return ()"
    if "Optional" in t or t == "None":
        return "return None"

    # Custom/complex types (TreeNode, ListNode, Union[...], etc.) -- None
    # is always valid at runtime even where it doesn't match the annotation.
    return "return None"


def ensure_runnable_body(starter_code: str) -> str:
    """Insert a type-appropriate placeholder body into any method whose
    body is empty.

    LeetCode's raw starter code often ends right after the signature (no
    statement follows), which is valid on their site but is an
    IndentationError the moment the file is saved and run standalone. A
    bare `pass` would also silently return None even where the signature
    promises an int/str/list/etc., so the placeholder is chosen based on
    the declared return type instead.
    """
    lines = starter_code.split("\n")
    result: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        result.append(line)
        match = _DEF_PATTERN.match(line)
        if match:
            indent = match.group(1)
            has_body = False
            j = i + 1
            while j < len(lines):
                nxt = lines[j]
                if nxt.strip() == "":
                    j += 1
                    continue
                has_body = (len(nxt) - len(nxt.lstrip())) > len(indent)
                break
            if not has_body:
                placeholder = _default_return_expr(match.group("ret"))
                result.append(f"{indent}    {placeholder}")
        i += 1
    return "\n".join(result)


def generate_python_file(problem: Problem, started_at: datetime.datetime) -> str:
    """Render the full contents of <id>.py.

    The main block is a real, immediately runnable test harness -- no
    pytest, no manual uncommenting. `python <id>.py` runs every official
    example against your solution and prints PASS/FAIL as-is.
    """
    starter_code = ensure_runnable_body(problem.starter_code)
    func_name = extract_function_name(starter_code)
    test_harness = generate_test_harness(func_name, problem.parsed.examples)

    header = f'''"""
Problem : {problem.id}
Title   : {problem.title}

Started : {started_at.strftime("%H:%M:%S")}
Date    : {started_at.strftime("%A, %d %B %Y")}
"""

'''
    body = starter_code.strip() + "\n\n\n"

    runner = f'''if __name__ == "__main__":
{test_harness}
'''
    return header + body + runner


def write_python_file(
    problem: Problem,
    folder: str,
    started_at: datetime.datetime,
    overwrite_check: Callable[[Path], bool],
) -> Path:
    """Write <id>.py into folder. If it already exists, overwrite_check(path)
    decides whether to overwrite; raises FileExistsError if declined."""
    target = Path(folder) / f"{problem.id}.py"
    if target.exists() and not overwrite_check(target):
        raise FileExistsError(f"{target} already exists and overwrite was declined.")
    target.write_text(generate_python_file(problem, started_at), encoding="utf-8")
    return target
