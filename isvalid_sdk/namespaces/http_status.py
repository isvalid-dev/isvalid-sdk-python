from __future__ import annotations

from typing import List

from isvalid_sdk.client import HttpClient
from isvalid_sdk.types.http_status import HttpStatusListItem, HttpStatusResponse


class HttpStatusNamespace:
    def __init__(self, client: HttpClient) -> None:
        self._client = client

    def __call__(self, value: str) -> HttpStatusResponse:
        return self._client.get("/v0/http-status", {"value": value})

    def list(self) -> List[HttpStatusListItem]:
        return self._client.get("/v0/http-status/list")
