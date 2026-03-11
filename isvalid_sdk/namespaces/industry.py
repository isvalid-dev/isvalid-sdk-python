from __future__ import annotations

from typing import List, Optional

from isvalid_sdk.client import HttpClient
from isvalid_sdk.types.industry import IndustryListItem, IndustryResponse


class IndustryNamespace:
    def __init__(self, client: HttpClient) -> None:
        self._client = client

    def __call__(self, value: str, *, system: Optional[str] = None) -> IndustryResponse:
        return self._client.get(
            "/v0/industry", {"value": value, "system": system}
        )

    def list(
        self,
        system: str,
        *,
        level: Optional[str] = None,
        parent: Optional[str] = None,
    ) -> List[IndustryListItem]:
        return self._client.get(
            "/v0/industry/list",
            {"system": system, "level": level, "parent": parent},
        )
