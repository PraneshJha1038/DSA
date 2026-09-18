"""LeetCode GraphQL API client.

Implements the mandatory two-stage resolution pipeline:
    frontend problem number -> problemsetQuestionList -> titleSlug
    titleSlug -> question(titleSlug) -> full metadata
"""
from __future__ import annotations
import time
import requests
from core.exceptions import NetworkError, ProblemNotFoundError, PremiumProblemError

GRAPHQL_URL = "https://leetcode.com/graphql"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; LCWorkspaceManager/1.0)",
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Origin": "https://leetcode.com",
    "Referer": "https://leetcode.com",
}

TIMEOUT = 10
MAX_RETRIES = 3

_LIST_QUERY = """
query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
  problemsetQuestionList: questionList(
    categorySlug: $categorySlug
    limit: $limit
    skip: $skip
    filters: $filters
  ) {
    total: totalNum
    questions: data {
      questionFrontendId
      titleSlug
      title
      difficulty
      paidOnly: isPaidOnly
    }
  }
}
"""

_QUESTION_QUERY = """
query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionId
    questionFrontendId
    title
    titleSlug
    difficulty
    content
    isPaidOnly
    exampleTestcases
    sampleTestCase
    topicTags { name }
    codeSnippets { lang langSlug code }
    hints
  }
}
"""


def _post(query: str, variables: dict) -> dict:
    """POST a GraphQL query with retries/backoff. Raises NetworkError on failure."""
    payload = {"query": query, "variables": variables}
    last_exc: Exception | None = None

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = requests.post(GRAPHQL_URL, json=payload, headers=HEADERS, timeout=TIMEOUT)
        except requests.RequestException as exc:
            last_exc = exc
            time.sleep(2 ** attempt)
            continue

        if resp.status_code == 429:
            raise NetworkError("Rate limited by LeetCode (HTTP 429). Try again shortly.")
        if resp.status_code == 403:
            raise NetworkError("Blocked by LeetCode (HTTP 403 / Cloudflare). Try again later.")
        if resp.status_code != 200:
            last_exc = NetworkError(f"Unexpected HTTP status: {resp.status_code}")
            time.sleep(2 ** attempt)
            continue

        try:
            data = resp.json()
        except ValueError as exc:
            raise NetworkError(f"Malformed GraphQL response (not JSON): {exc}") from exc

        if "errors" in data:
            raise NetworkError(f"GraphQL error: {data['errors']}")
        return data

    raise NetworkError(f"Network request failed after {MAX_RETRIES} attempts: {last_exc}")


def resolve_slug_by_number(problem_number: int) -> tuple[str, str]:
    """Resolve a frontend problem number to (titleSlug, difficulty) by
    paginating problemsetQuestionList until a match is found."""
    skip = 0
    limit = 100
    for _ in range(50):  # hard cap to avoid runaway pagination
        data = _post(_LIST_QUERY, {"categorySlug": "", "limit": limit, "skip": skip, "filters": {}})
        payload = data.get("data", {}).get("problemsetQuestionList")
        if not payload:
            raise NetworkError("Malformed problemsetQuestionList response.")
        questions = payload["questions"]
        if not questions:
            break
        for q in questions:
            if str(q["questionFrontendId"]) == str(problem_number):
                return q["titleSlug"], q["difficulty"]
        skip += limit
    raise ProblemNotFoundError(f"No problem found with number {problem_number}.")


def fetch_question(title_slug: str) -> dict:
    """Fetch full question detail by titleSlug. Raises PremiumProblemError if locked."""
    data = _post(_QUESTION_QUERY, {"titleSlug": title_slug})
    question = data.get("data", {}).get("question")
    if not question:
        raise ProblemNotFoundError(f"No question data returned for slug '{title_slug}'.")
    if question.get("isPaidOnly"):
        raise PremiumProblemError("This problem requires LeetCode Premium.")
    return question


def get_python_snippet(question: dict) -> str:
    """Select the python3 starter code snippet, or raise if unavailable."""
    for snippet in question.get("codeSnippets", []):
        if snippet.get("langSlug") == "python3":
            return snippet["code"]
    raise ProblemNotFoundError("No Python3 starter code available for this problem.")
