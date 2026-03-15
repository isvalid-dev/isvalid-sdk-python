# isvalid-sdk

Python SDK for the [isvalid.dev](https://isvalid.dev) validation API.

## Features

- **Single dependency** — only `httpx`
- **Full type hints** with `TypedDict` for every endpoint response
- **Context manager** support for proper resource cleanup
- **Automatic retry** with exponential backoff for 429/5xx
- **Custom exception classes** for auth and rate limit errors
- **Python 3.9+**

## Installation

```bash
pip install isvalid-sdk
```

## Quick Start

Get your free API key at [isvalid.dev/getting-started-python](https://isvalid.dev/getting-started-python).

```python
from isvalid_sdk import IsValidConfig, create_client

iv = create_client(IsValidConfig(api_key="your-api-key"))

# Simple validation
email = iv.email("user@example.com", check_mx=True)
# => {"valid": True, "local": "user", "domain": "example.com", "mxValid": True}

iban = iv.iban("DE89370400440532013000")
# => {"valid": True, "countryCode": "DE", "bankName": "Commerzbank", ...}

vat = iv.vat("DE123456789", check_vies=True)
# => {"valid": True, "countryCode": "DE", "isEU": True, "vies": {"checked": True, ...}}
```

## Context Manager

```python
with create_client(IsValidConfig(api_key="your-api-key")) as iv:
    result = iv.email("user@example.com")
```

## Namespaced Methods

Some endpoints support callable + property access pattern:

```python
# LEI
lei = iv.lei("5493001KJTIIGC8Y1R12")
search = iv.lei.search("Apple", country="US", limit=5)
lous = iv.lei.lous()

# Country / Currency / Language
country = iv.country("PL")
countries = iv.country.list()

currency = iv.currency("USD")
currencies = iv.currency.list()

language = iv.language("en")
languages = iv.language.list()

# IATA
flight = iv.iata.flight("LH1234")
airline = iv.iata.airline("LH")
airlines = iv.iata.airline.list()
airport = iv.iata.airport("WAW")

# Timezone
tz = iv.timezone("Europe/Warsaw")
# => {"valid": True, "timezone": "Europe/Warsaw", "utcOffset": "+01:00", "abbreviation": "CET", "isDST": False}
timezones = iv.timezone.list(region="Europe")

# MIME Type
mime = iv.mime_type("application/json")
# => {"valid": True, "mime": "application/json", "type": "application", "subtype": "json", "extensions": ["json"], ...}
by_ext = iv.mime_type.ext("pdf")
mimes = iv.mime_type.list(type="image")

# HTTP Status
status = iv.http_status("404")
# => {"valid": True, "code": 404, "reasonPhrase": "Not Found", "category": "client-error"}
statuses = iv.http_status.list()

# SWIFT MT
mt = iv.swift_mt("MT103")
# => {"valid": True, "type": "MT103", "category": 1, "group": "Customer Payments & Cheques", ...}
mt_list = iv.swift_mt.list(category=1)

# UN/LOCODE
locode = iv.locode("PLWAW")
# => {"valid": True, "locode": "PLWAW", "country": "PL", "name": "Warszawa", "found": True, ...}
locodes = iv.locode.list(country="PL")

# HS Code (Harmonized System)
hs = iv.hs_code("8471")
# => {"valid": True, "code": "8471", "level": "heading", "description": "...", ...}
hs_list = iv.hs_code.list(chapter="84", level="heading")

# GS1 Prefix
gs1 = iv.gs1_prefix("590")
# => {"valid": True, "prefix": "590", "country": "Poland"}
gs1_list = iv.gs1_prefix.list()

# Industry (NAICS / NACE)
ind = iv.industry("5112", system="naics")
# => {"valid": True, "system": "NAICS", "code": "5112", "description": "...", ...}
ind_list = iv.industry.list(system="naics", level="sector")
```

## Country-Specific Endpoints

```python
# Poland
iv.pl.pesel("44051401358")
iv.pl.regon("012345678", lookup=True)
iv.pl.krs("0000123456", lookup=True)
iv.pl.ceidg("5252344078", lookup=True)
iv.pl.pkd("62.01.Z")

# Brazil
iv.br.cnpj("11.222.333/0001-81")
iv.br.cpf("123.456.789-09")

# Other
iv.au.abn("51824753556")
iv.es.nif("12345678Z")
iv.in_.gstin("27AAPFU0939F1ZV")  # note: in_ (reserved word)
iv.us.npi("1234567893")
iv.gb.sort_code("12-34-56")
```

## Network & Financial

```python
# Network
iv.net.ip("192.168.1.1")
iv.net.mac("00:1B:44:11:3A:B7")
iv.net.port("443")
# => {"valid": True, "port": 443, "range": "well-known", "serviceName": "HTTPS", ...}
ports = iv.net.port.list()

# Financial
iv.isin("US0378331005")
iv.dti("B1234567Z")
iv.bic("DEUTDEFF")
iv.cusip("037833100")
iv.credit_card("4111111111111111")  # POST endpoint
```

## All Simple Endpoints

```python
iv.email(value, check_mx=)     iv.iban(value, country_code=)
iv.isin(value)                  iv.dti(value)
iv.vat(value, country_code=, check_vies=)
iv.gps(value)                   iv.phone(value, country_code=)
iv.url(value)                   iv.ean(value)
iv.isbn(value)                  iv.issn(value)
iv.bic(value)                   iv.cusip(value)
iv.cfi(value)                   iv.mic(value)
iv.nuts(value)                  iv.uuid(value, version=)
iv.jwt(value)                   iv.vin(value)
iv.imei(value)                  iv.semver(value)
iv.color(value)                 iv.boolean(value)
iv.date(value, format=)         iv.btc_address(value)
iv.postal_code(value, country_code=)
iv.aba(value)                   iv.container_code(value)
iv.sscc(value)                  iv.gln(value)
iv.qr(value)                    iv.credit_card(number)
iv.cas(value)                   iv.eori(value, check=)
iv.orcid(value, lookup=)        iv.doi(value, lookup=)
iv.barcode(value, type=)        iv.base64(value)
iv.eth_address(value)           iv.cron(value)
iv.domain(value)                iv.regex(pattern, flags=)
iv.duns(value, lookup=)         iv.timestamp(value)
```

## Configuration

```python
from isvalid_sdk import IsValidConfig, RetryConfig, create_client

iv = create_client(IsValidConfig(
    api_key="your-api-key",
    base_url="https://api.isvalid.dev",  # default
    timeout=15.0,                         # default: 10.0 (seconds)
    retry=RetryConfig(
        max_retries=5,                   # default: 3
        initial_delay=1.0,               # default: 0.5
        max_delay=30.0,                  # default: 10.0
        retry_on=(429, 500, 502, 503),   # default
    ),
))

# Disable retry
iv = create_client(IsValidConfig(api_key="...", retry=None))
```

## Error Handling

```python
from isvalid_sdk import (
    IsValidError, IsValidAuthError, IsValidRateLimitError, create_client
)

try:
    iv.email("test@example.com")
except IsValidRateLimitError as e:
    print("Rate limited, retry after:", e.retry_after, "seconds")
except IsValidAuthError as e:
    print("Invalid API key")
except IsValidError as e:
    print("API error:", e.status, e.body["error"])
```

## API Reference

Full endpoint documentation: [isvalid.dev/docs](https://isvalid.dev/docs)

## License

MIT
