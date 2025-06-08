from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class CertificateInfo(BaseModel):
    url: str
    valid_until: Optional[datetime] = None
    needs_update: bool = False
    error: Optional[str] = None

    class Config:
        orm_mode = True

class HostInfo(BaseModel):
    hostname: str
    certificates: List[CertificateInfo]

    class Config:
        orm_mode = True
