from __future__ import annotations

from typing import Union

from typing_extensions import TypedDict

from isvalid_sdk.types.simple import InvalidResponse


class CountryValidResponse(TypedDict):
    valid: bool
    value: str
    format: str
    alpha2: str
    alpha3: str
    numeric: str
    name: str


CountryResponse = Union[InvalidResponse, CountryValidResponse]


class CountryListItem(TypedDict):
    alpha2: str
    alpha3: str
    numeric: str
    name: str
