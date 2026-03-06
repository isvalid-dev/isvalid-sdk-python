from __future__ import annotations

from typing import List, Optional, Union

from typing_extensions import TypedDict

from isvalid_sdk.types.simple import InvalidResponse


class LeiEntity(TypedDict):
    legalName: str
    country: Optional[str]
    entityStatus: Optional[str]
    registrationStatus: Optional[str]
    category: Optional[str]
    initialRegistrationDate: Optional[str]
    lastUpdate: Optional[str]
    nextRenewal: Optional[str]
    managingLou: Optional[str]


class LeiLou(TypedDict):
    lei: str
    name: str
    country: Optional[str]
    status: Optional[str]


class LeiValidResponse(TypedDict):
    valid: bool
    lei: str
    louCode: str
    checkDigits: str
    found: Optional[bool]
    dataSource: Optional[str]
    entity: Optional[LeiEntity]
    lou: Optional[LeiLou]


LeiResponse = Union[InvalidResponse, LeiValidResponse]


class LeiSearchResult(TypedDict):
    lei: str
    legalName: str
    country: Optional[str]
    entityStatus: Optional[str]
    registrationStatus: Optional[str]
    category: Optional[str]


class LeiSearchResponse(TypedDict):
    results: List[LeiSearchResult]
    page: int
    limit: int
    total: int


class LeiLouItem(TypedDict):
    louCode: str
    lei: str
    name: str
    country: Optional[str]
    status: Optional[str]


class LeiLousResponse(TypedDict):
    lous: List[LeiLouItem]
    total: int
