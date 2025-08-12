from fastapi import FastAPI, Depends, HTTPException
import uvicorn
from pydantic import BaseModel, Field
from database import new_session, CompanyModel
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated

app = FastAPI()

# Dependency for session
async def get_session():
    async with new_session() as session:
        yield session

SessionDep = Annotated[AsyncSession, Depends(get_session)]

@app.get("/hello")
def read_root():
    return {"Hello": "World"}

# Initiate app: python main.py
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

class CompanyCreateScheme(BaseModel):
    company_name: str
    inn: str
    status: int

@app.post("/companies")
async def create_company(data: CompanyCreateScheme, session: SessionDep):
    new_company = CompanyModel(
        company_name = data.company_name,
        inn = data.inn,
        status = data.status
        )
    session.add(new_company)
    await session.commit()
    await session.refresh(new_company)
    return new_company

# @app.get("/companies/{company_id}",
#          tags=["company-controller"],
#          summary="get_company",)
# def get_company(company_id: int):
#     for company in companies:
#         if company["company_id"] == company_id:
#             return company
#     raise HTTPException(status_code=404, detail="Company not found")

# @app.post("/companies",
#           tags=["company-controller"],
#           summary="create_company")
# def create_company(company: companyScheme):
#     companies.append({
#         "id": len(companies) + 1,
#         "company_name": company.company_name,
#         "inn": company.inn,
#         "status": company.status
#     })
#     return companies[-1]