from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

# Database credentials
POSTGRES_USER = "test_user"
POSTGRES_PASSWORD = "password"
POSTGRES_HOST = "localhost"
POSTGRES_PORT = "5432"
POSTGRES_DB = "test_db"

# Create URL for async connection (asyncpg)
SQLALCHEMY_DATABASE_URL = (
    f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@"
    f"{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)

# Create engine and session
engine = create_async_engine(SQLALCHEMY_DATABASE_URL)
new_session = async_sessionmaker(engine, expire_on_commit=False)