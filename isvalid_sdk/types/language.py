from __future__ import annotations

from typing import Optional, Union

from typing_extensions import TypedDict

from isvalid_sdk.types.simple import InvalidResponse


class LanguageValidResponse(TypedDict):
    valid: bool
    format: str
    alpha2: Optional[str]
    alpha3: str
    name: str


LanguageResponse = Union[InvalidResponse, LanguageValidResponse]


class LanguageListItem(TypedDict):
    alpha2: Optional[str]
    alpha3: str
    name: str
