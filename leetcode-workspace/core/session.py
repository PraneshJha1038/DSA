"""Session lifecycle management (single active session, resume/discard/cancel)."""
from __future__ import annotations
import json
import datetime
from pathlib import Path
from core.models import Session
from core.exceptions import SessionError


def load_session(session_file: str) -> Session | None:
    """Return the active Session, or None if no session file exists.
    Raises SessionError if the file exists but is corrupted."""
    path = Path(session_file)
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return Session(**data)
    except (json.JSONDecodeError, TypeError, KeyError) as exc:
        raise SessionError(f"session.json is corrupted: {exc}") from exc


def save_session(session_file: str, session: Session) -> None:
    Path(session_file).write_text(json.dumps(session.__dict__, indent=4), encoding="utf-8")


def delete_session(session_file: str) -> None:
    path = Path(session_file)
    if path.exists():
        path.unlink()


def start_new_session(session_file: str, problem_id: int, title: str, difficulty: str) -> Session:
    """Create and persist a new session, using local time in ISO-8601."""
    session = Session(
        problem=problem_id,
        title=title,
        difficulty=difficulty,
        started_at=datetime.datetime.now().isoformat(timespec="seconds"),
    )
    save_session(session_file, session)
    return session


def compute_elapsed(session: Session) -> str:
    """Return elapsed time as HH:MM:SS since the session started (local time)."""
    started = datetime.datetime.fromisoformat(session.started_at)
    delta = datetime.datetime.now() - started
    total_seconds = max(int(delta.total_seconds()), 0)
    hours, rem = divmod(total_seconds, 3600)
    minutes, seconds = divmod(rem, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
