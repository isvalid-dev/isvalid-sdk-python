from __future__ import annotations

from typing import Union

from typing_extensions import TypedDict

from isvalid_sdk.types.simple import InvalidResponse


class NifValidResponse(TypedDict):
    valid: bool
    type: str
    normalized: str


NifResponse = Union[InvalidResponse, NifValidResponse]
