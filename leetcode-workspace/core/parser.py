"""Parses raw GraphQL HTML content into structured, typed data.

Rendering modules (markdown_generator, python_generator) never touch
raw HTML directly -- they consume the typed output of this module.
"""
from __future__ import annotations
import re
from bs4 import BeautifulSoup, NavigableString, Tag
from core.models import Example, ParsedQuestion
from core.exceptions import ParsingError

_BLOCK_TAGS = {"p", "div", "pre", "ul", "ol"}

_TEX_REPLACEMENTS = [
    (r"\\left", ""), (r"\\right", ""),
    (r"\\leq", "<="), (r"\\le\b", "<="),
    (r"\\geq", ">="), (r"\\ge\b", ">="),
    (r"\\neq", "!="), (r"\\ne\b", "!="),
    (r"\\times", "*"), (r"\\cdot", "*"),
    (r"\\ldots", "..."), (r"\\dots", "..."),
    (r"\\text\{([^{}]*)\}", r"\1"),
]


def _tex_to_text(tex: str) -> str:
    """Convert a LaTeX snippet (as found in KaTeX's <annotation> tag) into
    plain text matching how these expressions are normally written out
    (l_i, 10^9, x <= 5, ...). LeetCode's own subscripts/superscripts and
    comparison operators are already nearly plain-text in TeX form --
    this just strips math-mode delimiters, unwraps a handful of common
    macros, and drops the grouping braces that TeX needs but plain text
    doesn't (l_{i} -> l_i)."""
    t = tex.strip()
    t = re.sub(r"^\${1,2}|\${1,2}$", "", t)
    t = re.sub(r"^\\\(|\\\)$", "", t)
    for pattern, repl in _TEX_REPLACEMENTS:
        t = re.sub(pattern, repl, t)
    t = t.replace("{", "").replace("}", "")
    return re.sub(r"\s+", " ", t).strip()


def _render(node) -> str:
    """Recursively turn a BeautifulSoup node into markdown-flavored text.

    Unlike soup.get_text(), this actually preserves the formatting LeetCode
    relies on to make problem statements readable: <code> spans become
    `backticks`, <strong>/<em> become **bold**/*italic*, and KaTeX-rendered
    math (LeetCode renders l_i, 10^9, etc. via KaTeX, not plain <sub>/<sup>)
    is pulled from KaTeX's hidden <annotation> tag rather than flattened
    from its visual layout spans -- naively flattening KaTeX's markup is
    what previously turned "l_i" into "l i" and "10^9" into "10 9", since
    KaTeX spells every glyph out in its own positioning <span>. Block-level
    tags (p, div, pre, ul, ol) get surrounding newlines; everything else
    stays inline so adjacent inline tags don't get spuriously split onto
    their own line.
    """
    if isinstance(node, NavigableString):
        return str(node)
    if not isinstance(node, Tag):
        return ""

    classes = node.get("class") or []
    if "katex" in classes:
        annotation = node.find("annotation")
        if annotation is not None:
            return f"`{_tex_to_text(annotation.get_text())}`"
        return node.get_text(strip=True)

    inner = "".join(_render(child) for child in node.children)

    if node.name == "code":
        return f"`{inner.strip()}`"
    if node.name == "sub":
        return f"_{inner.strip()}"
    if node.name == "sup":
        return f"^{inner.strip()}"
    if node.name in ("strong", "b"):
        return f"**{inner.strip()}**"
    if node.name in ("em", "i"):
        return f"*{inner.strip()}*"
    if node.name == "li":
        return f"\n- {inner.strip()}"
    if node.name == "br":
        return "\n"
    if node.name in _BLOCK_TAGS:
        return f"\n{inner}\n"
    return inner


def parse_content_html(html: str) -> ParsedQuestion:
    """Convert LeetCode's raw HTML question content into a ParsedQuestion."""
    if not html:
        raise ParsingError("Empty question content received.")

    soup = BeautifulSoup(html, "html.parser")
    full_text = _render(soup)
    full_text = re.sub(r"\n{3,}", "\n\n", full_text)

    examples = _extract_examples(full_text)
    constraints = _extract_constraints(full_text)
    description = _extract_description(full_text)

    return ParsedQuestion(description=description, examples=examples, constraints=constraints)


def _extract_examples(full_text: str) -> list[Example]:
    """Extract Example N blocks (Input/Output/Explanation) from the page text."""
    blocks = re.split(r"\*{0,2}Example \d+:?\*{0,2}", full_text)[1:]
    examples: list[Example] = []
    for block in blocks:
        # Constraints usually trail the last example within the same
        # raw text stream -- cut it off so it doesn't leak into the
        # explanation of the final example.
        block = re.split(r"\*{0,2}Constraints:\*{0,2}", block)[0]

        inp = re.search(r"\*{0,2}Input:\*{0,2}\s*(.*?)(?=\*{0,2}Output:)", block, re.DOTALL)
        out = re.search(r"\*{0,2}Output:\*{0,2}\s*(.*?)(?=\*{0,2}Explanation:|$)", block, re.DOTALL)
        expl = re.search(r"\*{0,2}Explanation:\*{0,2}\s*(.*)", block, re.DOTALL)

        if inp and out:
            examples.append(Example(
                # Input/Output are spliced directly into generated Python
                # code later, so any stray `code` backticks that slipped
                # in from formatting must not survive here.
                input=inp.group(1).strip().replace("`", ""),
                output=out.group(1).strip().replace("`", ""),
                explanation=expl.group(1).strip() if expl else "",
            ))
    return examples


def _extract_constraints(full_text: str) -> list[str]:
    """Extract the bullet list under the 'Constraints:' heading, if present."""
    match = re.search(r"\*{0,2}Constraints:\*{0,2}\s*(.*)", full_text, re.DOTALL)
    if not match:
        return []
    lines = [ln.strip("- \t") for ln in match.group(1).splitlines() if ln.strip()]
    return [ln for ln in lines if ln and ln != "**"]


def _extract_description(full_text: str) -> str:
    """Everything before the first 'Example' heading is treated as the description."""
    parts = re.split(r"\*{0,2}Example \d+:?\*{0,2}", full_text)
    return parts[0].strip() if parts else full_text.strip()


def extract_function_name(starter_code: str) -> str:
    """Pull the method name out of a Python starter code template."""
    match = re.search(r"def (\w+)\(self", starter_code)
    if not match:
        raise ParsingError("Could not locate a method definition in starter code.")
    return match.group(1)


_JS_LITERAL = {"true": "True", "false": "False", "null": "None"}


def _normalize_literal(text: str) -> str:
    """Convert LeetCode's JS-style true/false/null tokens in raw example
    output text into valid Python literals, so the text can be embedded
    directly as executable source code."""
    return re.sub(r"\btrue\b|\bfalse\b|\bnull\b", lambda m: _JS_LITERAL[m.group(0)], text)


def generate_test_harness(func_name: str, examples: list[Example]) -> str:
    """Generate a small, dependency-free, immediately runnable test harness
    that calls the solution against every official example and prints
    PASS/FAIL -- no pytest, no manual uncommenting required.

    This relies on LeetCode's example input already being formatted as
    keyword arguments matching the signature (e.g. "n = 10203004",
    "nums = [2,7,11,15], target = 9"), so it can be spliced directly
    into a real call.
    """
    if not examples:
        return "    pass  # no official examples were available to test against"

    lines = ["    sol = Solution()", "    _cases = ["]
    for ex in examples:
        expected = _normalize_literal(ex.output)
        lines.append(f"        (sol.{func_name}({ex.input}), {expected}),")
    lines += [
        "    ]",
        "    _passed = 0",
        "    for _i, (_actual, _expected) in enumerate(_cases, start=1):",
        "        if _actual == _expected:",
        '            print(f"[PASS] Example {_i}: {_actual!r}")',
        "            _passed += 1",
        "        else:",
        '            print(f"[FAIL] Example {_i}: expected {_expected!r}, got {_actual!r}")',
        '    print(f"\\n{_passed}/{len(_cases)} example(s) passed.")',
    ]
    return "\n".join(lines)
