import os
from pydantic_settings import BaseSettings
from typing import List
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    APP_NAME: str = "Certificate Manager"
    DEBUG: bool = False
    ALLOWED_HOSTS: List[str] = ["*"]
    LOG_LEVEL: str = "INFO"
    CERTIFICATE_EXPIRY_DAYS: int = 30

    class Config:
        env = os.getenv("ENV", "prod")
        if env == "dev":
            env_file = ".env.dev"
        elif env == "test":
            env_file = ".env.test"
        else:
            env_file = ".env"
        case_sensitive = True


settings = Settings()
