from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

from typing_extensions import TypedDict


class InvalidResponse(TypedDict):
    valid: bool  # False


class EmailValidResponse(TypedDict, total=False):
    valid: bool  # True
    local: str
    domain: str
    mxValid: bool


EmailResponse = Union[InvalidResponse, EmailValidResponse]


class IbanValidResponse(TypedDict):
    valid: bool
    countryCode: str
    countryName: str
    bban: str
    isEU: bool
    formatted: str
    bankCode: Optional[str]
    bankName: Optional[str]
    bankBic: Optional[str]


IbanResponse = Union[InvalidResponse, IbanValidResponse]


class IsinValidResponse(TypedDict, total=False):
    valid: bool
    countryCode: str
    countryName: Optional[str]
    nsin: str
    cusip: Optional[str]
    checkDigit: str
    found: Optional[bool]
    dataSource: Optional[str]
    name: Optional[str]
    fisn: Optional[str]
    cfiCode: Optional[str]
    currency: Optional[str]
    tradingVenue: Optional[str]
    issuerLei: Optional[str]
    maturityDate: Optional[str]
    status: Optional[str]
    ticker: Optional[str]
    exchCode: Optional[str]
    securityType: Optional[str]
    marketSector: Optional[str]
    figi: Optional[str]
    compositeFIGI: Optional[str]


IsinResponse = Union[InvalidResponse, IsinValidResponse]


class DtiValidResponse(TypedDict, total=False):
    valid: bool
    normalized: str
    payload: str
    checkChar: str
    found: Optional[bool]
    identifierType: str
    name: Optional[str]
    shortName: Optional[str]
    dtiType: Optional[int]


DtiResponse = Union[InvalidResponse, DtiValidResponse]


class ViesInfo(TypedDict, total=False):
    checked: bool
    valid: bool
    name: Optional[str]
    address: Optional[str]
    reason: str


class VatValidResponse(TypedDict, total=False):
    valid: bool
    normalized: str
    countryCode: str
    countryName: str
    isEU: bool
    vies: ViesInfo


VatResponse = Union[InvalidResponse, VatValidResponse]


class DmsCoords(TypedDict):
    lat: str
    lon: str


class GpsValidResponse(TypedDict):
    valid: bool
    format: str
    lat: float
    lon: float
    latDir: str
    lonDir: str
    dms: DmsCoords


GpsResponse = Union[InvalidResponse, GpsValidResponse]


class PhoneValidResponse(TypedDict):
    valid: bool
    countryCode: Optional[str]
    callingCode: str
    nationalNumber: str
    type: str
    e164: str
    national: str
    international: str


PhoneResponse = Union[InvalidResponse, PhoneValidResponse]


class UrlValidResponse(TypedDict):
    valid: bool
    protocol: str
    domain: str
    path: str
    query: Dict[str, Any]
    port: Optional[str]
    hash: Optional[str]


UrlResponse = Union[InvalidResponse, UrlValidResponse]


class EanValidResponse(TypedDict, total=False):
    valid: bool
    format: str
    prefix: str
    prefixCountry: str
    upcA: str
    indicator: str


EanResponse = Union[InvalidResponse, EanValidResponse]


class IsbnValidResponse(TypedDict):
    valid: bool
    format: str
    isbn10: Optional[str]
    isbn13: str


IsbnResponse = Union[InvalidResponse, IsbnValidResponse]


class IssnValidResponse(TypedDict):
    valid: bool
    issn: str


IssnResponse = Union[InvalidResponse, IssnValidResponse]


class BicValidResponse(TypedDict):
    valid: bool
    bankCode: str
    countryCode: str
    countryName: Optional[str]
    locationCode: str
    branchCode: Optional[str]
    bankName: Optional[str]
    city: Optional[str]
    branch: Optional[str]


BicResponse = Union[InvalidResponse, BicValidResponse]


class CusipValidResponse(TypedDict):
    valid: bool
    issuerNumber: str
    issueNumber: str
    checkDigit: str


CusipResponse = Union[InvalidResponse, CusipValidResponse]


class CfiAttribute(TypedDict):
    position: int
    code: str
    name: Optional[str]
    value: Optional[str]


class CfiValidResponse(TypedDict):
    valid: bool
    cfi: str
    category: str
    categoryName: str
    group: str
    groupName: Optional[str]
    attributes: List[CfiAttribute]


CfiResponse = Union[InvalidResponse, CfiValidResponse]


class MicValidResponse(TypedDict, total=False):
    valid: bool
    found: bool
    mic: str
    operatingMic: str
    name: str
    type: str
    status: str
    countryCode: str
    countryName: Optional[str]
    city: str
    website: Optional[str]


MicResponse = Union[InvalidResponse, MicValidResponse]


class NutsValidResponse(TypedDict):
    valid: bool
    code: str
    level: int
    country: str
    countryName: Optional[str]
    regionName: Optional[str]


NutsResponse = Union[InvalidResponse, NutsValidResponse]


class UuidValidResponse(TypedDict):
    valid: bool
    version: int


UuidResponse = Union[InvalidResponse, UuidValidResponse]


class JwtValidResponse(TypedDict):
    valid: bool
    algorithm: str
    header: Dict[str, Any]
    payload: Dict[str, Any]
    issuedAt: Optional[str]
    expiresAt: Optional[str]
    expired: Optional[bool]


JwtResponse = Union[InvalidResponse, JwtValidResponse]


class VinValidResponse(TypedDict):
    valid: bool
    wmi: str
    vds: str
    checkDigit: str
    vin: str
    country: Optional[str]
    region: Optional[str]
    manufacturer: Optional[str]
    modelYearCandidates: List[int]
    serialNumber: str


VinResponse = Union[InvalidResponse, VinValidResponse]


class ImeiValidResponse(TypedDict):
    valid: bool
    tac: str
    snr: str
    checkDigit: str


ImeiResponse = Union[InvalidResponse, ImeiValidResponse]


class SemverValidResponse(TypedDict):
    valid: bool
    major: int
    minor: int
    patch: int
    prerelease: Optional[List[str]]
    build: Optional[List[str]]


SemverResponse = Union[InvalidResponse, SemverValidResponse]


class ColorValidResponse(TypedDict):
    valid: bool
    format: str
    r: int
    g: int
    b: int
    h: int
    s: int
    l: int
    alpha: int
    hex: str


ColorResponse = Union[InvalidResponse, ColorValidResponse]


class BooleanValidResponse(TypedDict):
    valid: bool
    normalized: bool


BooleanResponse = Union[InvalidResponse, BooleanValidResponse]


class DateValidResponse(TypedDict):
    valid: bool
    iso: str


DateResponse = Union[InvalidResponse, DateValidResponse]


class BtcAddressValidResponse(TypedDict):
    valid: bool
    type: str


BtcAddressResponse = Union[InvalidResponse, BtcAddressValidResponse]


class PostalCodeLocation(TypedDict):
    city: str
    region: Optional[str]
    subregion: Optional[str]
    lat: Optional[float]
    lon: Optional[float]


class PostalCodeMatchingCountry(TypedDict):
    country: str
    countryName: Optional[str]
    format: str


class PostalCodeValidResponse(TypedDict, total=False):
    valid: bool
    country: str
    countryName: Optional[str]
    format: str
    location: Optional[PostalCodeLocation]
    matchingCountries: List[PostalCodeMatchingCountry]


PostalCodeResponse = Union[InvalidResponse, PostalCodeValidResponse]


class AbaValidResponse(TypedDict):
    valid: bool
    routingNumber: str
    checkDigit: str


AbaResponse = Union[InvalidResponse, AbaValidResponse]


class ContainerCodeValidResponse(TypedDict):
    valid: bool
    ownerCode: str
    equipmentCategory: str
    serialNumber: str
    checkDigit: str


ContainerCodeResponse = Union[InvalidResponse, ContainerCodeValidResponse]


class SsccValidResponse(TypedDict):
    valid: bool
    extensionDigit: str
    gsPrefix: str
    serialRef: str
    checkDigit: str


SsccResponse = Union[InvalidResponse, SsccValidResponse]


class GlnValidResponse(TypedDict):
    valid: bool
    prefix: str
    locationRef: str
    checkDigit: str


GlnResponse = Union[InvalidResponse, GlnValidResponse]


class QrResponse(TypedDict, total=False):
    valid: bool
    format: str
    data: Dict[str, Any]
    error: str


class CreditCardValidResponse(TypedDict):
    valid: bool
    type: str


CreditCardResponse = Union[InvalidResponse, CreditCardValidResponse]
