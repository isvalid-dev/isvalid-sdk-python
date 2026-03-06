from __future__ import annotations

from typing import Union

from typing_extensions import TypedDict

from isvalid_sdk.types.simple import InvalidResponse


class AbnValidResponse(TypedDict):
    valid: bool
    normalized: str


AbnResponse = Union[InvalidResponse, AbnValidResponse]
