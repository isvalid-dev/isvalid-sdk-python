from __future__ import annotations

from typing import List

from isvalid_sdk.client import HttpClient
from isvalid_sdk.types.gs1_prefix import Gs1PrefixListItem, Gs1PrefixResponse


class Gs1PrefixNamespace:
    def __init__(self, client: HttpClient) -> None:
        self._client = client

    def __call__(self, value: str) -> Gs1PrefixResponse:
        return self._client.get("/v0/gs1-prefix", {"value": value})

    def list(self) -> List[Gs1PrefixListItem]:
        return self._client.get("/v0/gs1-prefix/list")
