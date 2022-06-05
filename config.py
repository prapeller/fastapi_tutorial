import logging
import os

from pydantic import BaseSettings

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    database_url: str = os.getenv(
        'DATABASE_URL', 'postgresql://postgres:4189@127.0.0.1:5432/fastapitutorial_db')
    http_proxy: str = os.getenv('http_proxy', '')
    https_proxy: str = os.getenv('https_proxy', '')


def get_settings() -> Settings:
    log.info("Loading Settings for prod...")
    return Settings()
