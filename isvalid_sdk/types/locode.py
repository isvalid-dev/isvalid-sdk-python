from __future__ import annotations

from typing import List, Optional, Union

from typing_extensions import TypedDict

from isvalid_sdk.types.simple import InvalidResponse


class LocodeValidResponse(TypedDict, total=False):
    valid: bool
    locode: str
    country: str
    countryName: str
    city: str
    subdivision: Optional[str]
    functions: List[str]


LocodeResponse = Union[InvalidResponse, LocodeValidResponse]


class LocodeListItem(TypedDict, total=False):
    locode: str
    city: str
    subdivision: Optional[str]
    functions: List[str]
