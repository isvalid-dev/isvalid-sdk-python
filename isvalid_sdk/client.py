from __future__ import annotations

import random
import time
from dataclasses import dataclass, field
from typing import Any

import httpx

from isvalid_sdk.errors import IsValidAuthError, IsValidError, IsValidRateLimitError

DEFAULT_BASE_URL = "https://api.isvalid.dev"
DEFAULT_TIMEOUT = 10.0

_DEFAULT_RETRY_ON = (429, 500, 502, 503)


@dataclass
class RetryConfig:
    max_retries: int = 3
    initial_delay: float = 0.5
    max_delay: float = 10.0
    retry_on: tuple[int, ...] = _DEFAULT_RETRY_ON


@dataclass
class IsValidConfig:
    api_key: str
    base_url: str = DEFAULT_BASE_URL
    timeout: float = DEFAULT_TIMEOUT
    retry: RetryConfig | None = field(default_factory=RetryConfig)


def _backoff_delay(attempt: int, initial: float, max_delay: float) -> float:
    base = initial * (2 ** attempt)
    jitter = random.random() * initial
    return min(base + jitter, max_delay)


class HttpClient:
    def __init__(self, config: IsValidConfig) -> None:
        self._base_url = config.base_url.rstrip("/")
        self._api_key = config.api_key
        self._retry = config.retry
        self._timeout = config.timeout
        self._client = httpx.Client(
            base_url=self._base_url,
            timeout=self._timeout,
            headers={
                "Authorization": f"Bearer {self._api_key}",
                "Accept": "application/json",
            },
        )

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> HttpClient:
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()

    def get(self, path: str, params: dict[str, str | None] | None = None) -> Any:
        filtered = {k: v for k, v in (params or {}).items() if v is not None}
        return self._request("GET", path, params=filtered)

    def post(self, path: str, json: Any) -> Any:
        return self._request("POST", path, json=json)

    def _request(self, method: str, path: str, **kwargs: Any) -> Any:
        max_attempts = (self._retry.max_retries + 1) if self._retry else 1

        for attempt in range(max_attempts):
            response = self._client.request(method, path, **kwargs)

            if response.is_success:
                return response.json()

            if (
                self._retry
                and attempt < self._retry.max_retries
                and response.status_code in self._retry.retry_on
            ):
                retry_after = response.headers.get("Retry-After")
                if retry_after:
                    delay = int(retry_after)
                else:
                    delay = _backoff_delay(
                        attempt, self._retry.initial_delay, self._retry.max_delay
                    )
                time.sleep(delay)
                continue

            try:
                body = response.json()
            except Exception:
                body = {"error": response.reason_phrase or "Unknown error"}

            if response.status_code == 401:
                raise IsValidAuthError(body)
            if response.status_code == 429:
                ra = response.headers.get("Retry-After")
                raise IsValidRateLimitError(body, int(ra) if ra else None)
            raise IsValidError(response.status_code, body)

        raise IsValidError(0, {"error": "Max retries exceeded"})
