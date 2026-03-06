from __future__ import annotations

from typing import List

from isvalid_sdk.client import HttpClient
from isvalid_sdk.types.country import CountryListItem, CountryResponse


class CountryNamespace:
    def __init__(self, client: HttpClient) -> None:
        self._client = client

    def __call__(self, value: str) -> CountryResponse:
        return self._client.get("/v0/country", {"value": value})

    def list(self) -> List[CountryListItem]:
        return self._client.get("/v0/country/list")
