from __future__ import annotations

from typing import Optional, Union

from typing_extensions import TypedDict

from isvalid_sdk.types.simple import InvalidResponse


class IpValidResponse(TypedDict, total=False):
    valid: bool
    version: int
    type: str
    expanded: str


IpResponse = Union[InvalidResponse, IpValidResponse]


class MacValidResponse(TypedDict):
    valid: bool
    normalized: str
    type: str
    isLocal: bool
    isBroadcast: bool


MacResponse = Union[InvalidResponse, MacValidResponse]


class NetPortValidResponse(TypedDict, total=False):
    valid: bool
    port: int
    protocol: str
    serviceName: str
    description: str


NetPortResponse = Union[InvalidResponse, NetPortValidResponse]


class NetPortListItem(TypedDict, total=False):
    port: int
    protocol: str
    serviceName: str
    description: str
