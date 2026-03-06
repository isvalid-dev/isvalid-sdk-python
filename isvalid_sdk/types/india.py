from __future__ import annotations

from typing import Optional, Union

from typing_extensions import TypedDict

from isvalid_sdk.types.simple import InvalidResponse


class GstinValidResponse(TypedDict):
    valid: bool
    stateCode: str
    stateName: Optional[str]
    pan: str
    entityType: str
    checkDigit: str


GstinResponse = Union[InvalidResponse, GstinValidResponse]
