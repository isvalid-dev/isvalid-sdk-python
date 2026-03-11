from __future__ import annotations

from typing import List, Optional, Union

from typing_extensions import TypedDict

from isvalid_sdk.types.simple import InvalidResponse


class HttpStatusValidResponse(TypedDict, total=False):
    valid: bool
    code: int
    message: str
    category: str
    description: str


HttpStatusResponse = Union[InvalidResponse, HttpStatusValidResponse]


class HttpStatusListItem(TypedDict, total=False):
    code: int
    message: str
    category: str
