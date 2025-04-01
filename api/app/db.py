from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base

from app.settings import settings

Base = declarative_base()

engine = create_async_engine(settings.POSTGRES_URL, future=True, echo=False)

AsyncSessionLocal = async_sessionmaker(
    engine, autoflush=False, expire_on_commit=False
)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
