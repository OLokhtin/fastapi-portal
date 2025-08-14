from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

from src.database import get_session
from src.schemas.pagination import PaginationSchema

SessionDep = Annotated[AsyncSession, Depends(get_session)]
PaginationDep = Annotated[PaginationSchema, Depends(PaginationSchema)]