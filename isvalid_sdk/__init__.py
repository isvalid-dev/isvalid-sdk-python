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
from isvalid_sdk.namespaces.iata import IataNamespace
from isvalid_sdk.namespaces.india import InNamespace
from isvalid_sdk.namespaces.language import LanguageNamespace
from isvalid_sdk.namespaces.lei import LeiNamespace
from isvalid_sdk.namespaces.net import NetNamespace
from isvalid_sdk.namespaces.pl import PlNamespace
from isvalid_sdk.namespaces.us import UsNamespace
from isvalid_sdk.types.simple import (
    AbaResponse,
    BicResponse,
    BooleanResponse,
    BtcAddressResponse,
    CfiResponse,
    ColorResponse,
    ContainerCodeResponse,
    CreditCardResponse,
    CusipResponse,
    DateResponse,
    DtiResponse,
    EanResponse,
    EmailResponse,
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
    PhoneResponse,
    PostalCodeResponse,
    QrResponse,
    SemverResponse,
    SsccResponse,
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


def create_client(config: IsValidConfig) -> IsValid:
    return IsValid(config)
