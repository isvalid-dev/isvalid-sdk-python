from __future__ import annotations

from typing import Optional

from isvalid_sdk.client import HttpClient, IsValidConfig, RetryConfig
from isvalid_sdk.errors import IsValidAuthError, IsValidError, IsValidRateLimitError
from isvalid_sdk.namespaces.au import AuNamespace
from isvalid_sdk.namespaces.br import BrNamespace
from isvalid_sdk.namespaces.country import CountryNamespace
from isvalid_sdk.namespaces.currency import CurrencyNamespace
from isvalid_sdk.namespaces.es import EsNamespace
from isvalid_sdk.namespaces.gb import GbNamespace
from isvalid_sdk.namespaces.gs1_prefix import Gs1PrefixNamespace
from isvalid_sdk.namespaces.hs_code import HsCodeNamespace
from isvalid_sdk.namespaces.http_status import HttpStatusNamespace
from isvalid_sdk.namespaces.iata import IataNamespace
from isvalid_sdk.namespaces.india import InNamespace
from isvalid_sdk.namespaces.industry import IndustryNamespace
from isvalid_sdk.namespaces.language import LanguageNamespace
from isvalid_sdk.namespaces.lei import LeiNamespace
from isvalid_sdk.namespaces.locode import LocodeNamespace
from isvalid_sdk.namespaces.mime_type import MimeTypeNamespace
from isvalid_sdk.namespaces.net import NetNamespace
from isvalid_sdk.namespaces.pl import PlNamespace
from isvalid_sdk.namespaces.swift_mt import SwiftMtNamespace
from isvalid_sdk.namespaces.timezone import TimezoneNamespace
from isvalid_sdk.namespaces.us import UsNamespace
from isvalid_sdk.types.simple import (
    AbaResponse,
    BarcodeResponse,
    Base64Response,
    BicResponse,
    BooleanResponse,
    BtcAddressResponse,
    CasResponse,
    CfiResponse,
    ColorResponse,
    ContainerCodeResponse,
    CreditCardResponse,
    CronResponse,
    CusipResponse,
    DateResponse,
    DoiResponse,
    DomainResponse,
    DtiResponse,
    DunsResponse,
    EanResponse,
    EmailResponse,
    EoriResponse,
    EthAddressResponse,
    GlnResponse,
    GpsResponse,
    IbanResponse,
    ImeiResponse,
    IsbnResponse,
    IsinResponse,
    IssnResponse,
    JwtResponse,
    MicResponse,
    NutsResponse,
    OrcidResponse,
    PhoneResponse,
    PostalCodeResponse,
    QrResponse,
    RegexResponse,
    SemverResponse,
    SsccResponse,
    TimestampResponse,
    UrlResponse,
    UuidResponse,
    VatResponse,
    VinResponse,
)

__all__ = [
    "IsValid",
    "create_client",
    "IsValidConfig",
    "RetryConfig",
    "IsValidError",
    "IsValidAuthError",
    "IsValidRateLimitError",
]


class IsValid:
    def __init__(self, config: IsValidConfig) -> None:
        self._client = HttpClient(config)

        self.lei = LeiNamespace(self._client)
        self.country = CountryNamespace(self._client)
        self.currency = CurrencyNamespace(self._client)
        self.language = LanguageNamespace(self._client)
        self.iata = IataNamespace(self._client)
        self.net = NetNamespace(self._client)
        self.pl = PlNamespace(self._client)
        self.br = BrNamespace(self._client)
        self.au = AuNamespace(self._client)
        self.es = EsNamespace(self._client)
        self.in_ = InNamespace(self._client)
        self.us = UsNamespace(self._client)
        self.gb = GbNamespace(self._client)
        self.hs_code = HsCodeNamespace(self._client)
        self.gs1_prefix = Gs1PrefixNamespace(self._client)
        self.industry = IndustryNamespace(self._client)
        self.timezone = TimezoneNamespace(self._client)
        self.mime_type = MimeTypeNamespace(self._client)
        self.http_status = HttpStatusNamespace(self._client)
        self.swift_mt = SwiftMtNamespace(self._client)
        self.locode = LocodeNamespace(self._client)

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "IsValid":
        return self

    def __exit__(self, *args: object) -> None:
        self.close()

    # --- Simple endpoints ---

    def email(self, value: str, *, check_mx: bool = False) -> EmailResponse:
        return self._client.get(
            "/v0/email",
            {"value": value, "checkMx": str(check_mx).lower() if check_mx else None},
        )

    def iban(self, value: str, *, country_code: Optional[str] = None) -> IbanResponse:
        return self._client.get(
            "/v0/iban", {"value": value, "countryCode": country_code}
        )

    def isin(self, value: str) -> IsinResponse:
        return self._client.get("/v0/isin", {"value": value})

    def dti(self, value: str) -> DtiResponse:
        return self._client.get("/v0/dti", {"value": value})

    def vat(
        self,
        value: str,
        *,
        country_code: Optional[str] = None,
        check_vies: bool = False,
    ) -> VatResponse:
        return self._client.get(
            "/v0/vat",
            {
                "value": value,
                "countryCode": country_code,
                "checkVies": str(check_vies).lower() if check_vies else None,
            },
        )

    def gps(self, value: str) -> GpsResponse:
        return self._client.get("/v0/gps", {"value": value})

    def phone(self, value: str, *, country_code: Optional[str] = None) -> PhoneResponse:
        return self._client.get(
            "/v0/phone", {"value": value, "countryCode": country_code}
        )

    def url(self, value: str) -> UrlResponse:
        return self._client.get("/v0/url", {"value": value})

    def ean(self, value: str) -> EanResponse:
        return self._client.get("/v0/ean", {"value": value})

    def isbn(self, value: str) -> IsbnResponse:
        return self._client.get("/v0/isbn", {"value": value})

    def issn(self, value: str) -> IssnResponse:
        return self._client.get("/v0/issn", {"value": value})

    def bic(self, value: str) -> BicResponse:
        return self._client.get("/v0/bic", {"value": value})

    def cusip(self, value: str) -> CusipResponse:
        return self._client.get("/v0/cusip", {"value": value})

    def cfi(self, value: str) -> CfiResponse:
        return self._client.get("/v0/cfi", {"value": value})

    def mic(self, value: str) -> MicResponse:
        return self._client.get("/v0/mic", {"value": value})

    def nuts(self, value: str) -> NutsResponse:
        return self._client.get("/v0/nuts", {"value": value})

    def uuid(self, value: str, *, version: Optional[int] = None) -> UuidResponse:
        return self._client.get(
            "/v0/uuid",
            {"value": value, "version": str(version) if version is not None else None},
        )

    def jwt(self, value: str) -> JwtResponse:
        return self._client.get("/v0/jwt", {"value": value})

    def vin(self, value: str) -> VinResponse:
        return self._client.get("/v0/vin", {"value": value})

    def imei(self, value: str) -> ImeiResponse:
        return self._client.get("/v0/imei", {"value": value})

    def semver(self, value: str) -> SemverResponse:
        return self._client.get("/v0/semver", {"value": value})

    def color(self, value: str) -> ColorResponse:
        return self._client.get("/v0/color", {"value": value})

    def boolean(self, value: str) -> BooleanResponse:
        return self._client.get("/v0/boolean", {"value": value})

    def date(self, value: str, *, format: Optional[str] = None) -> DateResponse:
        return self._client.get("/v0/date", {"value": value, "format": format})

    def btc_address(self, value: str) -> BtcAddressResponse:
        return self._client.get("/v0/btc-address", {"value": value})

    def postal_code(
        self, value: str, *, country_code: Optional[str] = None
    ) -> PostalCodeResponse:
        return self._client.get(
            "/v0/postal-code", {"value": value, "countryCode": country_code}
        )

    def aba(self, value: str) -> AbaResponse:
        return self._client.get("/v0/aba", {"value": value})

    def container_code(self, value: str) -> ContainerCodeResponse:
        return self._client.get("/v0/container-code", {"value": value})

    def sscc(self, value: str) -> SsccResponse:
        return self._client.get("/v0/sscc", {"value": value})

    def gln(self, value: str) -> GlnResponse:
        return self._client.get("/v0/gln", {"value": value})

    def qr(self, value: str) -> QrResponse:
        return self._client.get("/v0/qr", {"value": value})

    def credit_card(self, number: str) -> CreditCardResponse:
        return self._client.post("/v0/credit-card", {"number": number})

    def cas(self, value: str) -> CasResponse:
        return self._client.get("/v0/cas", {"value": value})

    def eori(self, value: str, *, check: bool = False) -> EoriResponse:
        return self._client.get(
            "/v0/eori",
            {"value": value, "check": str(check).lower() if check else None},
        )

    def orcid(self, value: str, *, lookup: bool = False) -> OrcidResponse:
        return self._client.get(
            "/v0/orcid",
            {"value": value, "lookup": str(lookup).lower() if lookup else None},
        )

    def doi(self, value: str, *, lookup: bool = False) -> DoiResponse:
        return self._client.get(
            "/v0/doi",
            {"value": value, "lookup": str(lookup).lower() if lookup else None},
        )

    def barcode(self, value: str, *, type: Optional[str] = None) -> BarcodeResponse:
        return self._client.get(
            "/v0/barcode", {"value": value, "type": type}
        )

    def base64(self, value: str) -> Base64Response:
        return self._client.get("/v0/base64", {"value": value})

    def eth_address(self, value: str) -> EthAddressResponse:
        return self._client.get("/v0/eth-address", {"value": value})

    def cron(self, value: str) -> CronResponse:
        return self._client.get("/v0/cron", {"value": value})

    def domain(self, value: str) -> DomainResponse:
        return self._client.get("/v0/domain", {"value": value})

    def regex(self, pattern: str, *, flags: Optional[str] = None) -> RegexResponse:
        return self._client.post("/v0/regex", {"pattern": pattern, "flags": flags})

    def duns(self, value: str, *, lookup: bool = False) -> DunsResponse:
        return self._client.get(
            "/v0/duns",
            {"value": value, "lookup": str(lookup).lower() if lookup else None},
        )

    def timestamp(self, value: str) -> TimestampResponse:
        return self._client.get("/v0/timestamp", {"value": value})


def create_client(config: IsValidConfig) -> IsValid:
    return IsValid(config)
