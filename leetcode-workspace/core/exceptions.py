"""Custom exceptions for the LeetCode workspace manager."""


class LCWorkspaceError(Exception):
    """Base exception for all workspace-related errors."""


class ConfigError(LCWorkspaceError):
    """Raised when config.json is missing, malformed, or invalid."""


class ProblemNotFoundError(LCWorkspaceError):
    """Raised when a problem number cannot be resolved."""


class PremiumProblemError(LCWorkspaceError):
    """Raised when the requested problem requires LeetCode Premium."""


class NetworkError(LCWorkspaceError):
    """Raised on network failures, timeouts, or rate limiting."""


class SessionError(LCWorkspaceError):
    """Raised on session file corruption or lifecycle violations."""


class ParsingError(LCWorkspaceError):
    """Raised when GraphQL response content cannot be parsed."""
