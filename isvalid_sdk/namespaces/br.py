from __future__ import annotations

from isvalid_sdk.client import HttpClient
from isvalid_sdk.types.br import CnpjResponse, CpfResponse


class BrNamespace:
    def __init__(self, client: HttpClient) -> None:
        self._client = client

    def cnpj(self, value: str) -> CnpjResponse:
        return self._client.get("/v0/br/cnpj", {"value": value})

    def cpf(self, value: str) -> CpfResponse:
        return self._client.get("/v0/br/cpf", {"value": value})
