from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class Repository[T]:
    def __init__(self, session: AsyncSession, table: type[T]):
        self.session = session
        self.table = table

    async def get_all(self):
        res = await self.session.execute(select(self.table))
        return res.scalars().all()

    async def commit(self) -> None:
        await self.session.commit()
