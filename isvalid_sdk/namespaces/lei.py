from __future__ import annotations

from typing import Optional

from isvalid_sdk.client import HttpClient
from isvalid_sdk.types.lei import LeiLousResponse, LeiResponse, LeiSearchResponse


class LeiNamespace:
    def __init__(self, client: HttpClient) -> None:
        self._client = client

    def __call__(self, value: str) -> LeiResponse:
        return self._client.get("/v0/lei", {"value": value})

    def search(
        self,
        query: str,
        *,
        country: Optional[str] = None,
        entity_status: Optional[str] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> LeiSearchResponse:
        return self._client.get(
            "/v0/lei/search",
            {
                "q": query,
                "country": country,
                "entityStatus": entity_status,
                "page": str(page) if page is not None else None,
                "limit": str(limit) if limit is not None else None,
            },
        )

    def lous(self) -> LeiLousResponse:
        return self._client.get("/v0/lei/lous")
