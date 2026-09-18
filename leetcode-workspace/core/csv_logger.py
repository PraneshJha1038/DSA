"""Append-only CSV solve-history logger."""
from __future__ import annotations
import csv
import datetime
from pathlib import Path

FIELDNAMES = ["Date", "Problem", "Title", "Difficulty", "Status", "Time Taken", "Notes"]


def log_entry(
    csv_path: str,
    problem: int,
    title: str,
    difficulty: str,
    status: str,
    time_taken: str,
    notes: str,
) -> None:
    """Append one row to the CSV log, creating the file with headers if absent.
    Uses csv.DictWriter so commas, quotes, and multiline notes are handled
    correctly -- never hand-build CSV rows via string concatenation."""
    path = Path(csv_path)
    is_new = not path.exists()
    with path.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        if is_new:
            writer.writeheader()
        writer.writerow({
            "Date": datetime.datetime.now().strftime("%Y-%m-%d"),
            "Problem": problem,
            "Title": title,
            "Difficulty": difficulty,
            "Status": status,
            "Time Taken": time_taken,
            "Notes": notes,
        })
