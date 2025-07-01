from app.core.base import EnvConfig


class AppConfig(EnvConfig):
    app_debug: bool
    app_title: str
    app_description: str
    app_version: str
    app_host: str
    app_port: int
