from pydantic_settings import BaseSettings
from .app import AppConfig
from .db import DbConfig


class Config(BaseSettings):
    db_config: DbConfig = DbConfig()
    app_config: AppConfig = AppConfig()


config = Config()
