from __future__ import annotations


class IsValidError(Exception):
    def __init__(self, status: int, body: dict[str, str]) -> None:
        super().__init__(body.get("error", "Unknown error"))
        self.status = status
        self.body = body


class IsValidAuthError(IsValidError):
    def __init__(self, body: dict[str, str]) -> None:
        super().__init__(401, body)


class IsValidRateLimitError(IsValidError):
    def __init__(self, body: dict[str, str], retry_after: int | None = None) -> None:
        super().__init__(429, body)
        self.retry_after = retry_after
