from __future__ import annotations

from isvalid_sdk.client import HttpClient
from isvalid_sdk.types.gb import SortCodeResponse


class GbNamespace:
    def __init__(self, client: HttpClient) -> None:
        self._client = client

    def sort_code(self, value: str) -> SortCodeResponse:
        return self._client.get("/v0/gb/sort-code", {"value": value})
