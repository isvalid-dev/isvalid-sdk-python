from __future__ import annotations

from typing import Union

from typing_extensions import TypedDict

from isvalid_sdk.types.simple import InvalidResponse


class CnpjValidResponse(TypedDict):
    valid: bool
    normalized: str
    type: str


CnpjResponse = Union[InvalidResponse, CnpjValidResponse]


class CpfValidResponse(TypedDict):
    valid: bool
    normalized: str


CpfResponse = Union[InvalidResponse, CpfValidResponse]
