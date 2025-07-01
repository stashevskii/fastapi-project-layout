from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from app.config import config

engine = create_async_engine(
    f"postgresql+asyncpg://{config.db_config.db_username}:{config.db_config.db_password}@{config.db_config.db_host}/{config.db_config.db_name}",
)

async_session_maker = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)


async def get_async_session() -> AsyncSession:
    async with async_session_maker() as session:
        yield session
