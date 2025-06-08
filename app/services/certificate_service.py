import ssl
import socket
from datetime import datetime
from app.models.certificate import CertificateInfo, HostInfo
from app.core.logging import logger
from app.config.settings import settings

class CertificateService:
    @staticmethod
    def check_certificate(url: str) -> CertificateInfo:
        try:
            hostname = url.replace("https://", "").replace("http://", "")
            logger.info(f"Checking certificate for {hostname}")

            context = ssl.create_default_context()
            with socket.create_connection((hostname, 443)) as sock:
                with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                    cert = ssock.getpeercert()
                    if cert is None:
                        raise ValueError("No certificate found")

                    not_after = cert.get('notAfter')
                    if not isinstance(not_after, str):
                        raise ValueError("Invalid certificate expiration date format")

                    exp_date = datetime.strptime(not_after, '%b %d %H:%M:%S %Y %Z')
                    needs_update = (exp_date - datetime.now()).days < settings.CERTIFICATE_EXPIRY_DAYS

                    return CertificateInfo(
                        url=url,
                        valid_until=exp_date,
                        needs_update=needs_update,
                        error=None
                    )
        except Exception as e:
            logger.error(f"Error checking certificate for {url}: {str(e)}")
            return CertificateInfo(
                url=url,
                valid_until=None,
                needs_update=True,
                error=str(e)
            )

    @staticmethod
    def check_host_certificates(host: str) -> HostInfo:
        logger.info(f"Checking certificates for host: {host}")
        cert_info = CertificateService.check_certificate(host)
        return HostInfo(
            hostname=host,
            certificates=[cert_info]
        )
