from __future__ import annotations

from typing import List, Optional

from isvalid_sdk.client import HttpClient
from isvalid_sdk.types.swift_mt import SwiftMtListItem, SwiftMtResponse


class SwiftMtNamespace:
    def __init__(self, client: HttpClient) -> None:
        self._client = client

    def __call__(self, value: str) -> SwiftMtResponse:
        return self._client.get("/v0/swift-mt", {"value": value})

    def list(self, *, category: Optional[str] = None) -> List[SwiftMtListItem]:
        return self._client.get(
            "/v0/swift-mt/list", {"category": category}
        )
