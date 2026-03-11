from __future__ import annotations

from typing import List, Optional, Union

from typing_extensions import TypedDict

from isvalid_sdk.types.simple import InvalidResponse


class SwiftMtValidResponse(TypedDict, total=False):
    valid: bool
    type: str
    category: int
    categoryName: str
    description: str


SwiftMtResponse = Union[InvalidResponse, SwiftMtValidResponse]


class SwiftMtListItem(TypedDict, total=False):
    type: str
    category: int
    categoryName: str
    description: str
