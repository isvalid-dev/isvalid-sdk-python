from isvalid_sdk import IsValid, IsValidConfig, create_client
from isvalid_sdk.errors import IsValidAuthError, IsValidError, IsValidRateLimitError


def test_create_client():
    iv = create_client(IsValidConfig(api_key="test-key"))
    assert isinstance(iv, IsValid)


def test_default_config():
    config = IsValidConfig(api_key="test-key")
    assert config.base_url == "https://api.isvalid.dev"
    assert config.timeout == 10.0
    assert config.retry is not None
    assert config.retry.max_retries == 3


def test_disable_retry():
    config = IsValidConfig(api_key="test-key", retry=None)
    assert config.retry is None


def test_error_hierarchy():
    assert issubclass(IsValidAuthError, IsValidError)
    assert issubclass(IsValidRateLimitError, IsValidError)


def test_namespaces_exist():
    iv = create_client(IsValidConfig(api_key="test-key"))
    assert hasattr(iv, "lei")
    assert hasattr(iv, "country")
    assert hasattr(iv, "currency")
    assert hasattr(iv, "language")
    assert hasattr(iv, "iata")
    assert hasattr(iv, "net")
    assert hasattr(iv, "pl")
    assert hasattr(iv, "br")
    assert hasattr(iv, "au")
    assert hasattr(iv, "es")
    assert hasattr(iv, "in_")
    assert hasattr(iv, "us")
    assert hasattr(iv, "gb")
