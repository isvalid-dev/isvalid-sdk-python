from __future__ import annotations

from typing import Optional, Union

from typing_extensions import TypedDict

from isvalid_sdk.types.simple import InvalidResponse


class CurrencyValidResponse(TypedDict):
    valid: bool
    format: str
    code: str
    numericCode: str
    name: str
    minorUnit: Optional[int]


CurrencyResponse = Union[InvalidResponse, CurrencyValidResponse]


class CurrencyListItem(TypedDict):
    code: str
    numericCode: str
    name: str
    minorUnit: Optional[int]
