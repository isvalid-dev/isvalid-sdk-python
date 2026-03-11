from __future__ import annotations

from typing import List

from isvalid_sdk.client import HttpClient
from isvalid_sdk.types.locode import LocodeListItem, LocodeResponse


class LocodeNamespace:
    def __init__(self, client: HttpClient) -> None:
        self._client = client

    def __call__(self, value: str) -> LocodeResponse:
        return self._client.get("/v0/locode", {"value": value})

    def list(self, country: str) -> List[LocodeListItem]:
        return self._client.get("/v0/locode/list", {"country": country})
