from __future__ import annotations

from typing import Optional, Union

from typing_extensions import TypedDict

from isvalid_sdk.types.simple import InvalidResponse


class IataFlightValidResponse(TypedDict):
    valid: bool
    airlineCode: str
    flightNumber: str
    suffix: Optional[str]


IataFlightResponse = Union[InvalidResponse, IataFlightValidResponse]


class IataAirlineValidResponse(TypedDict, total=False):
    valid: bool
    found: bool
    iataCode: str
    icaoCode: Optional[str]
    name: str
    country: Optional[str]


IataAirlineResponse = Union[InvalidResponse, IataAirlineValidResponse]


class IataAirlineListItem(TypedDict):
    iataCode: str
    icaoCode: Optional[str]
    name: str
    country: Optional[str]


class IataAirportValidResponse(TypedDict, total=False):
    valid: bool
    found: bool
    iataCode: str
    name: str
    city: Optional[str]
    country: Optional[str]


IataAirportResponse = Union[InvalidResponse, IataAirportValidResponse]
