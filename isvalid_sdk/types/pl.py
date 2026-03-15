from __future__ import annotations

from typing import List, Optional, Union

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


class CeidgLookup(TypedDict, total=False):
    checked: bool
    found: bool
    reason: str
    status: Optional[str]
    firstName: Optional[str]
    lastName: Optional[str]
    businessName: Optional[str]
    regon: Optional[str]
    city: Optional[str]
    postalCode: Optional[str]
    street: Optional[str]
    houseNumber: Optional[str]
    flatNumber: Optional[str]
    startDate: Optional[str]
    pkd: List[str]
    primaryPkd: Optional[str]


class CeidgValidResponse(TypedDict, total=False):
    valid: bool  # True
    nip: str
    ceidg: CeidgLookup


CeidgResponse = Union[InvalidResponse, CeidgValidResponse]


class PkdValidResponse(TypedDict, total=False):
    valid: bool  # True
    code: str
    name: str
    section: str
    sectionName: str
    division: str
    divisionName: Optional[str]
    group: str
    groupName: Optional[str]
    className: Optional[str]
    # Note: JSON response also contains "class" key — accessible via result["class"]


PkdResponse = Union[InvalidResponse, PkdValidResponse]
