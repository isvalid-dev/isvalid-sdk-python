from __future__ import annotations

from isvalid_sdk.client import HttpClient
from isvalid_sdk.types.pl import KrsResponse, PeselResponse, RegonResponse


class PlNamespace:
    def __init__(self, client: HttpClient) -> None:
        self._client = client

    def pesel(self, value: str) -> PeselResponse:
        return self._client.get("/v0/pl/pesel", {"value": value})

    def regon(self, value: str, *, lookup: bool = False) -> RegonResponse:
        return self._client.get(
            "/v0/pl/regon",
            {"value": value, "lookup": str(lookup).lower() if lookup else None},
        )

    def krs(self, value: str, *, lookup: bool = False) -> KrsResponse:
        return self._client.get(
            "/v0/pl/krs",
            {"value": value, "lookup": str(lookup).lower() if lookup else None},
        )
