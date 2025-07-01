from fastapi import APIRouter, FastAPI
from .health import router as health_router

router = APIRouter()
router.include_router(health_router)


def register_main_router(app: FastAPI) -> None:
    app.include_router(router)


__all__ = ["register_main_router"]
