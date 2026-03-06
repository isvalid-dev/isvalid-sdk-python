from __future__ import annotations

from isvalid_sdk.client import HttpClient
from isvalid_sdk.types.india import GstinResponse


class InNamespace:
    def __init__(self, client: HttpClient) -> None:
        self._client = client

    def gstin(self, value: str) -> GstinResponse:
        return self._client.get("/v0/in/gstin", {"value": value})
