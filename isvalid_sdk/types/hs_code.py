from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

from typing_extensions import TypedDict

from isvalid_sdk.types.simple import InvalidResponse


class HsCodeValidResponse(TypedDict, total=False):
    valid: bool
    code: str
    level: str
    description: str
    parent: Optional[str]
    chapter: str
    chapterDescription: str


HsCodeResponse = Union[InvalidResponse, HsCodeValidResponse]


class HsCodeListItem(TypedDict, total=False):
    code: str
    level: str
    description: str
    parent: Optional[str]
