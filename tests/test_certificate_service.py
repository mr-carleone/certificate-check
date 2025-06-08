import pytest
from unittest.mock import patch, MagicMock
from datetime import datetime, timedelta
from app.services.certificate_service import CertificateService
from app.models.certificate import CertificateInfo, HostInfo


@pytest.fixture
def mock_ssl_context():
    with patch("ssl.create_default_context") as mock:
        context = MagicMock()
        mock.return_value = context
        yield context


@pytest.fixture
def mock_socket():
    with patch("socket.create_connection") as mock:
        sock = MagicMock()
        mock.return_value.__enter__.return_value = sock
        yield sock


def test_check_certificate_valid(mock_ssl_context, mock_socket):
    # Mock certificate data
    cert_data = {"notAfter": "Dec 31 23:59:59 2025 GMT"}

    # Setup mock SSL socket
    mock_ssl_socket = MagicMock()
    mock_ssl_socket.getpeercert.return_value = cert_data
    mock_ssl_context.wrap_socket.return_value.__enter__.return_value = mock_ssl_socket

    # Test valid certificate
    result = CertificateService.check_certificate("example.com")

    assert result.url == "example.com"
    assert isinstance(result.valid_until, datetime)
    assert result.needs_update is False
    assert result.error is None


def test_check_certificate_invalid(mock_ssl_context, mock_socket):
    # Mock connection error
    mock_socket.side_effect = Exception("Connection failed")

    # Test invalid certificate
    result = CertificateService.check_certificate("invalid.host")

    assert result.url == "invalid.host"
    assert result.valid_until is None
    assert result.needs_update is True
    assert result.error is not None


def test_check_host_certificates(mock_ssl_context, mock_socket):
    # Mock certificate data
    cert_data = {"notAfter": "Dec 31 23:59:59 2025 GMT"}

    # Setup mock SSL socket
    mock_ssl_socket = MagicMock()
    mock_ssl_socket.getpeercert.return_value = cert_data
    mock_ssl_context.wrap_socket.return_value.__enter__.return_value = mock_ssl_socket

    # Test host certificate check
    result = CertificateService.check_host_certificates("example.com")

    assert result.hostname == "example.com"
    assert len(result.certificates) == 1
    assert isinstance(result.certificates[0], CertificateInfo)
    assert result.certificates[0].url == "example.com"
