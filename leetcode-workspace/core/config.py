"""Config loading, validation, and first-run bootstrap.

Defaults below are pre-filled for this machine's DSA folder layout.
Edit config.json directly at any time to change paths.
"""
from __future__ import annotations
import json
from pathlib import Path
from rich.prompt import Prompt, Confirm
from core.models import Config
from core.exceptions import ConfigError

CONFIG_PATH = Path(__file__).resolve().parent.parent / "config.json"

REQUIRED_KEYS = [
    "leetcode_folder", "markdown_file", "csv_log",
    "vscode_project_folder", "session_file",
]

DEFAULTS = {
    "leetcode_folder": r"C:\Users\Pranesh\Downloads\VS CODE\DSA\Leetcode Problems",
    "markdown_file": r"C:\Users\Pranesh\Downloads\VS CODE\DSA\read.md",
    "csv_log": r"C:\Users\Pranesh\Downloads\VS CODE\DSA\leetcode_log.csv",
    "vscode_project_folder": r"C:\Users\Pranesh\Downloads\VS CODE\DSA",
    "session_file": r"C:\Users\Pranesh\Downloads\VS CODE\DSA\session.json",
    "auto_open_vscode": True,
    "auto_split_editor": True,
}


def _bootstrap() -> dict:
    """Interactively create config.json on first run."""
    print("No config.json found. Let's create one.")
    print("Press Enter to accept the shown default for this machine.\n")
    data: dict = {}
    for key, default in DEFAULTS.items():
        if isinstance(default, bool):
            data[key] = Confirm.ask(f"{key}", default=default)
        else:
            data[key] = Prompt.ask(f"{key}", default=str(default))
    CONFIG_PATH.write_text(json.dumps(data, indent=4), encoding="utf-8")
    return data


def _validate(data: dict) -> None:
    """Ensure required keys exist and referenced directories are creatable."""
    missing = [k for k in REQUIRED_KEYS if k not in data]
    if missing:
        raise ConfigError(f"config.json is missing required keys: {missing}")

    Path(data["leetcode_folder"]).mkdir(parents=True, exist_ok=True)
    Path(data["markdown_file"]).parent.mkdir(parents=True, exist_ok=True)
    Path(data["csv_log"]).parent.mkdir(parents=True, exist_ok=True)


def load_config() -> Config:
    """Load config.json, bootstrapping it interactively if absent, and
    validating/creating all referenced directories. Raises ConfigError
    on malformed JSON, missing keys, or filesystem failures."""
    if not CONFIG_PATH.exists():
        data = _bootstrap()
    else:
        try:
            data = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise ConfigError(f"config.json is corrupted: {exc}") from exc

    try:
        _validate(data)
    except OSError as exc:
        raise ConfigError(f"Filesystem error validating config paths: {exc}") from exc

    return Config(
        leetcode_folder=data["leetcode_folder"],
        markdown_file=data["markdown_file"],
        csv_log=data["csv_log"],
        vscode_project_folder=data["vscode_project_folder"],
        session_file=data["session_file"],
        auto_open_vscode=data.get("auto_open_vscode", True),
        auto_split_editor=data.get("auto_split_editor", True),
    )
