from __future__ import annotations

from typing import List, Optional

from isvalid_sdk.client import HttpClient
from isvalid_sdk.types.timezone import TimezoneListItem, TimezoneResponse


class TimezoneNamespace:
    def __init__(self, client: HttpClient) -> None:
        self._client = client

    def __call__(self, value: str) -> TimezoneResponse:
        return self._client.get("/v0/timezone", {"value": value})

    def list(self, *, region: Optional[str] = None) -> List[TimezoneListItem]:
        return self._client.get("/v0/timezone/list", {"region": region})
