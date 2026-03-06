from __future__ import annotations

from isvalid_sdk.client import HttpClient
from isvalid_sdk.types.es import NifResponse


class EsNamespace:
    def __init__(self, client: HttpClient) -> None:
        self._client = client

    def nif(self, value: str) -> NifResponse:
        return self._client.get("/v0/es/nif", {"value": value})
