from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn
from app.api.errors import register_errors_handler
from app.core.base import Base
from app.config import config
from app.core.db import engine
from app.api.routes import register_main_router
from app.utils import configure_logging


@asynccontextmanager
async def lifespan(application: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield


def create_app() -> FastAPI:
    application = FastAPI(
        debug=config.app_config.app_debug,
        title=config.app_config.app_title,
        version=config.app_config.app_version,
        description=config.app_config.app_description,
        lifespan=lifespan,
    )
    register_main_router(application)
    register_errors_handler(application)
    configure_logging()
    return application


def run():
    uvicorn.run(
        app="app.main:app",
        host=config.app_config.app_host,
        port=config.app_config.app_port,
        reload=True
    )


app = create_app()
