from __future__ import annotations

from typing import List, Optional

from isvalid_sdk.client import HttpClient
from isvalid_sdk.types.hs_code import HsCodeListItem, HsCodeResponse


class HsCodeNamespace:
    def __init__(self, client: HttpClient) -> None:
        self._client = client

    def __call__(self, value: str) -> HsCodeResponse:
        return self._client.get("/v0/hs-code", {"value": value})

    def list(
        self,
        *,
        chapter: Optional[str] = None,
        level: Optional[str] = None,
    ) -> List[HsCodeListItem]:
        return self._client.get(
            "/v0/hs-code/list",
            {"chapter": chapter, "level": level},
        )
