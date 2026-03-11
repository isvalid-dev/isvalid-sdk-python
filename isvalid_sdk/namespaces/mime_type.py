from __future__ import annotations

from typing import Any, List, Optional

from isvalid_sdk.client import HttpClient
from isvalid_sdk.types.mime_type import (
    MimeTypeExtResponse,
    MimeTypeListItem,
    MimeTypeResponse,
)


class MimeTypeNamespace:
    def __init__(self, client: HttpClient) -> None:
        self._client = client

    def __call__(self, value: str) -> MimeTypeResponse:
        return self._client.get("/v0/mime-type", {"value": value})

    def ext(self, value: str) -> MimeTypeExtResponse:
        return self._client.get("/v0/mime-type/ext", {"value": value})

    def list(self, *, type: Optional[str] = None) -> List[MimeTypeListItem]:
        return self._client.get("/v0/mime-type/list", {"type": type})
