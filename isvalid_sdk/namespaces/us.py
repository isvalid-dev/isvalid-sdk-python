from __future__ import annotations

from isvalid_sdk.client import HttpClient
from isvalid_sdk.types.us import NpiResponse


class UsNamespace:
    def __init__(self, client: HttpClient) -> None:
        self._client = client

    def npi(self, value: str) -> NpiResponse:
        return self._client.get("/v0/us/npi", {"value": value})
