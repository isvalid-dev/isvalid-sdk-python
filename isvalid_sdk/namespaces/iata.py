from __future__ import annotations

from typing import List

from isvalid_sdk.client import HttpClient
from isvalid_sdk.types.iata import (
    IataAirlineListItem,
    IataAirlineResponse,
    IataAirportResponse,
    IataFlightResponse,
)


class IataAirlineNamespace:
    def __init__(self, client: HttpClient) -> None:
        self._client = client

    def __call__(self, value: str) -> IataAirlineResponse:
        return self._client.get("/v0/iata/airline", {"value": value})

    def list(self) -> List[IataAirlineListItem]:
        return self._client.get("/v0/iata/airline/list")


class IataNamespace:
    def __init__(self, client: HttpClient) -> None:
        self._client = client
        self.airline = IataAirlineNamespace(client)

    def flight(self, value: str) -> IataFlightResponse:
        return self._client.get("/v0/iata/flight", {"value": value})

    def airport(self, value: str) -> IataAirportResponse:
        return self._client.get("/v0/iata/airport", {"value": value})
