from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

DB_URL_ASYNC = "postgresql+asyncpg://postgres:1234@localhost:5432/mydatabase"
engine_async = create_async_engine(DB_URL_ASYNC, echo=False, pool_size=50, max_overflow=50)
session = async_sessionmaker(engine_async, class_=AsyncSession, expire_on_commit=False)

DB_URL_SYNC = "postgresql+psycopg://postgres:1234@localhost:5432/mydatabase"
engine = create_engine(DB_URL_SYNC, echo=False, pool_size=50, max_overflow=50)
session_sync = Session(engine)
