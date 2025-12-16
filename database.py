from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

DB_URL = "postgresql+asyncpg://postgres:1234@localhost:5432/mydatabase"

engine = create_async_engine(DB_URL, echo=False)
session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
