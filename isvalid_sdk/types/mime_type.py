from __future__ import annotations

from typing import List, Optional, Union

from typing_extensions import TypedDict

from isvalid_sdk.types.simple import InvalidResponse


class MimeTypeValidResponse(TypedDict, total=False):
    valid: bool
    mimeType: str
    type: str
    subtype: str
    extensions: List[str]


MimeTypeResponse = Union[InvalidResponse, MimeTypeValidResponse]


class MimeTypeExtResponse(TypedDict, total=False):
    valid: bool
    extension: str
    mimeType: str


class MimeTypeListItem(TypedDict, total=False):
    mimeType: str
    type: str
    subtype: str
    extensions: List[str]
