from __future__ import annotations

from typing import Optional, Union

from typing_extensions import TypedDict

from isvalid_sdk.types.simple import InvalidResponse


class PeselValidResponse(TypedDict):
    valid: bool
    birthDate: str
    gender: str
    isOver15: bool
    isOver18: bool
    isOver21: bool


PeselResponse = Union[InvalidResponse, PeselValidResponse]


class RegonLookup(TypedDict, total=False):
    checked: bool
    found: bool
    reason: str
    name: Optional[str]
    nip: Optional[str]
    voivodeship: Optional[str]
    district: Optional[str]
    community: Optional[str]
    city: Optional[str]
    postalCode: Optional[str]
    street: Optional[str]
    houseNumber: Optional[str]
    flatNumber: Optional[str]
    activityEndDate: Optional[str]


class RegonValidResponse(TypedDict, total=False):
    valid: bool
    type: str
    regon: RegonLookup


RegonResponse = Union[InvalidResponse, RegonValidResponse]


class KrsAddress(TypedDict):
    city: Optional[str]
    voivodeship: Optional[str]
    street: Optional[str]
    houseNumber: Optional[str]
    flatNumber: Optional[str]
    postalCode: Optional[str]
    country: Optional[str]
    website: Optional[str]


class KrsLookup(TypedDict, total=False):
    checked: bool
    found: bool
    reason: str
    krs: Optional[str]
    registry: str
    name: Optional[str]
    legalForm: Optional[str]
    nip: Optional[str]
    regon: Optional[str]
    hasOppStatus: Optional[bool]
    registeredAt: Optional[str]
    dataAsOf: Optional[str]
    lastEntryAt: Optional[str]
    address: Optional[KrsAddress]


class KrsValidResponse(TypedDict, total=False):
    valid: bool
    number: str
    krs: KrsLookup


KrsResponse = Union[InvalidResponse, KrsValidResponse]
