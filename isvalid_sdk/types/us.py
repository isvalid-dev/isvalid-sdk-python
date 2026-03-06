from __future__ import annotations

from typing import Union

from typing_extensions import TypedDict

from isvalid_sdk.types.simple import InvalidResponse


class NpiValidResponse(TypedDict):
    valid: bool
    normalized: str


NpiResponse = Union[InvalidResponse, NpiValidResponse]
