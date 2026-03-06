from __future__ import annotations

from isvalid_sdk.client import HttpClient
from isvalid_sdk.types.net import IpResponse, MacResponse


class NetNamespace:
    def __init__(self, client: HttpClient) -> None:
        self._client = client

    def ip(self, value: str) -> IpResponse:
        return self._client.get("/v0/net/ip", {"value": value})

    def mac(self, value: str) -> MacResponse:
        return self._client.get("/v0/net/mac", {"value": value})
