from __future__ import annotations

from typing import List

from isvalid_sdk.client import HttpClient
from isvalid_sdk.types.net import (
    IpResponse,
    MacResponse,
    NetPortListItem,
    NetPortResponse,
)


class NetPortNamespace:
    def __init__(self, client: HttpClient) -> None:
        self._client = client

    def __call__(self, value: str) -> NetPortResponse:
        return self._client.get("/v0/net/port", {"value": value})

    def list(self) -> List[NetPortListItem]:
        return self._client.get("/v0/net/port/list")


class NetNamespace:
    def __init__(self, client: HttpClient) -> None:
        self._client = client
        self.port = NetPortNamespace(client)

    def ip(self, value: str) -> IpResponse:
        return self._client.get("/v0/net/ip", {"value": value})

    def mac(self, value: str) -> MacResponse:
        return self._client.get("/v0/net/mac", {"value": value})
