from __future__ import annotations

from isvalid_sdk.client import HttpClient
from isvalid_sdk.types.au import AbnResponse


class AuNamespace:
    def __init__(self, client: HttpClient) -> None:
        self._client = client

    def abn(self, value: str) -> AbnResponse:
        return self._client.get("/v0/au/abn", {"value": value})
