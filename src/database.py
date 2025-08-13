from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from dotenv import load_dotenv
import os

# Create URL for async connection (asyncpg)
load_dotenv()
SQLALCHEMY_DATABASE_URL = (
    f"postgresql+asyncpg://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@"
    f"{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
)

# Create engine and session
engine = create_async_engine(SQLALCHEMY_DATABASE_URL)
new_session = async_sessionmaker(engine, expire_on_commit=False)

async def get_session():
    async with new_session() as session:
        yield session

# Create base class
class Base(DeclarativeBase):
    pass