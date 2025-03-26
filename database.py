from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.testing.schema import mapped_column

from config import settings

# # Синхронное подключение
# sync_engine = create_engine(
#     url=settings.DATABASE_URL_psycopg,
#     echo=True,                              # Запросы к БД будут выводиться в консоль
#     pool_size=5,                            # Лимит подключений
#     max_overflow=10                         # Количество дополнительных подключений
# )

# Асинхронное подключение
async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=True,                              # Запросы к БД будут выводиться в консоль
    pool_size=5,                            # Лимит подключений
    max_overflow=10                         # Количество дополнительных подключений
)

new_session = async_sessionmaker(async_engine, expire_on_commit=False)

class Model(DeclarativeBase):
    pass

class TaskOrm(Model):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str | None]


async def create_tables():
    async with async_engine.begin() as connection:
        await connection.run_sync(Model.metadata.create_all)

async def drop_tables():
    async with async_engine.begin() as connection:
        await connection.run_sync(Model.metadata.drop_all)