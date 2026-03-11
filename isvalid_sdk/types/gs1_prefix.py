from __future__ import annotations

from typing import List, Optional, Union

from typing_extensions import TypedDict

from isvalid_sdk.types.simple import InvalidResponse


class Gs1PrefixValidResponse(TypedDict):
    valid: bool
    prefix: str
    organization: str
    countryCode: Optional[str]


Gs1PrefixResponse = Union[InvalidResponse, Gs1PrefixValidResponse]


class Gs1PrefixListItem(TypedDict):
    prefix: str
    organization: str
    countryCode: Optional[str]
