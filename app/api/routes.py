from fastapi import APIRouter, HTTPException  # type: ignore
from typing import List
from app.models.certificate import HostInfo
from app.services.certificate_service import CertificateService
from app.core.logging import logger

router: APIRouter = APIRouter()  # type: ignore

@router.get("/")  # type: ignore
async def root():
    return {"message": "Certificate Manager API"}

@router.post("/check-certificates", response_model=List[HostInfo])  # type: ignore
async def check_certificates(hosts: List[str]) -> List[HostInfo]:
    try:
        results: List[HostInfo] = []
        for host in hosts:
            host_info = CertificateService.check_host_certificates(host)
            results.append(host_info)
        return results
    except Exception as e:
        logger.error(f"Error checking certificates: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/update-certificate")  # type: ignore
async def update_certificate(host: str, url: str):
    try:
        # This is a stub - in real implementation, you would:
        # 1. SSH into the host
        # 2. Generate new certificate
        # 3. Update the certificate
        # 4. Restart the service if needed
        logger.info(f"Certificate update requested for {url} on {host}")
        return {"message": f"Certificate update requested for {url} on {host}"}
    except Exception as e:
        logger.error(f"Error updating certificate: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
