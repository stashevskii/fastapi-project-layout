from app.core.base import EnvConfig


class DbConfig(EnvConfig):
    db_username: str
    db_password: str
    db_host: str
    db_name: str
