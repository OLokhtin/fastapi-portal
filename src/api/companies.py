from fastapi import APIRouter
from sqlalchemy import select

from src.api.dependencies import SessionDep
from src.models.companies import CompanyModel
from src.schemas.companies import CompanyCreateScheme

router = APIRouter()

@router.get("/companies",
         tags=["company-controller"],
         summary="get_company")
async def get_companies(session: SessionDep):
    query = select(CompanyModel)
    result = await session.execute(query)
    return result.scalars().all()

@router.post("/companies",
          tags=["company-controller"],
          summary="create_company")
async def create_company(data: CompanyCreateScheme, session: SessionDep):
    new_company = CompanyModel(
        company_name = data.company_name,
        inn = data.inn,
        status = data.status
        )
    session.add(new_company)
    await session.commit()
    return new_company

# def get_company(company_id: int):
#     for company in companies:
#         if company["company_id"] == company_id:
#             return company
#     raise HTTPException(status_code=404, detail="Company not found")