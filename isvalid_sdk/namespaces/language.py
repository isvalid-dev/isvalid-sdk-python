from __future__ import annotations

from typing import List

from isvalid_sdk.client import HttpClient
from isvalid_sdk.types.language import LanguageListItem, LanguageResponse


class LanguageNamespace:
    def __init__(self, client: HttpClient) -> None:
        self._client = client

    def __call__(self, value: str) -> LanguageResponse:
        return self._client.get("/v0/language", {"value": value})

    def list(self) -> List[LanguageListItem]:
        return self._client.get("/v0/language/list")
