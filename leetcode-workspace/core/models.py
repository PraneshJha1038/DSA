"""Typed data models used throughout the workspace manager."""
from __future__ import annotations
from dataclasses import dataclass, field


@dataclass
class Example:
    input: str
    output: str
    explanation: str = ""


@dataclass
class ParsedQuestion:
    description: str
    examples: list[Example]
    constraints: list[str]
    notes: list[str] = field(default_factory=list)


@dataclass
class Problem:
    id: int
    title: str
    slug: str
    difficulty: str
    topics: list[str]
    starter_code: str
    parsed: ParsedQuestion
    raw_testcases: str = ""


@dataclass
class Session:
    problem: int
    title: str
    difficulty: str
    started_at: str  # ISO-8601, local time


@dataclass
class Config:
    leetcode_folder: str
    markdown_file: str
    csv_log: str
    vscode_project_folder: str
    session_file: str
    auto_open_vscode: bool = True
    auto_split_editor: bool = True
