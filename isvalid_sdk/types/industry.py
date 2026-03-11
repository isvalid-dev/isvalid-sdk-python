from __future__ import annotations

from typing import List, Optional, Union

from typing_extensions import TypedDict

from isvalid_sdk.types.simple import InvalidResponse


class IndustryValidResponse(TypedDict, total=False):
    valid: bool
    system: str
    code: str
    description: str
    level: int
    parent: Optional[str]
    parentDescription: Optional[str]


IndustryResponse = Union[InvalidResponse, IndustryValidResponse]


class IndustryListItem(TypedDict, total=False):
    code: str
    description: str
    level: int
    parent: Optional[str]
