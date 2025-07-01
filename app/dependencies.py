from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from app.core.db import get_async_session
from app.models import Url
from app.repositories import UrlRepository
from app.services import UrlService

AsyncSessionDep = Annotated[AsyncSession, Depends(get_async_session)]


def get_url_repository(db: AsyncSessionDep) -> UrlRepository:
    return UrlRepository(db, Url)


def get_url_service(repository: UrlRepository = Depends(get_url_repository)) -> UrlService:
    return UrlService(repository)


UrlServiceDep = Annotated[UrlService, Depends(get_url_service)]
