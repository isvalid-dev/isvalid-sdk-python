from __future__ import annotations

from typing import List, Optional, Union

from typing_extensions import TypedDict

from isvalid_sdk.types.simple import InvalidResponse


class TimezoneValidResponse(TypedDict, total=False):
    valid: bool
    timezone: str
    utcOffset: str
    region: str
    abbreviation: Optional[str]
    currentTime: str


TimezoneResponse = Union[InvalidResponse, TimezoneValidResponse]


class TimezoneListItem(TypedDict, total=False):
    timezone: str
    utcOffset: str
    region: str
    abbreviation: Optional[str]
