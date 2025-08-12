from fastapi import FastAPI, Depends, HTTPException
import uvicorn
from pydantic import BaseModel, Field
from database import new_session
from models.companies import CompanyModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import Annotated
from controllers.company_controller import *

app = FastAPI()

# Initiate app: python main.py
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

# Dependency for session
async def get_session():
    async with new_session() as session:
        yield session

SessionDep = Annotated[AsyncSession, Depends(get_session)]

class CompanyCreateScheme(BaseModel):
    company_name: str
    inn: str
    status: int

@app.get("/company")
async def get_companies(session: SessionDep):
    query = select(CompanyModel)
    result = await session.execute(query)
    return result.scalars().all()

@app.post("/companies")
async def create_company(data: CompanyCreateScheme, session: SessionDep):
    new_company = CompanyModel(
        company_name = data.company_name,
        inn = data.inn,
        status = data.status
        )
    session.add(new_company)
    await session.commit()
    return new_company