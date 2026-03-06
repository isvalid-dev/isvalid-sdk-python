from __future__ import annotations

from typing import Union

from typing_extensions import TypedDict

from isvalid_sdk.types.simple import InvalidResponse


class SortCodeValidResponse(TypedDict):
    valid: bool
    normalized: str
    formatted: str


SortCodeResponse = Union[InvalidResponse, SortCodeValidResponse]
