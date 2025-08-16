from fastapi import APIRouter
from sqlalchemy import select

from src.api.dependencies import SessionDep, PaginationDep
from src.models.companies import CompanyModel
from src.schemas.companies import CompanyCreateScheme

router = APIRouter()

@router.get("/companies",
         tags=["company-controller"],
         summary="get_companies")
async def get_companies(
        session: SessionDep,
        pagination: PaginationDep
):
    query = (select(CompanyModel)
             .limit(pagination.limit)
             .offset(pagination.offset)
     )
    result = await session.execute(query)
    return result.scalars().all()

@router.get("/companies/{company_id}",
            tags=["company-controller"],
            summary="get_company")
async def get_company(company_id:int, session: SessionDep):
    query = (select(CompanyModel)
             .filter(CompanyModel.company_id == company_id))
    result = await session.execute(query)
    return result.scalars().first()

@router.post("/companies",
          tags=["company-controller"],
          summary="create_company")
async def create_company(
        data: CompanyCreateScheme,
        session: SessionDep
):
    new_company = CompanyModel(
        company_name = data.company_name,
        inn = data.inn,
        status = data.status
    )
    session.add(new_company)
    await session.commit()
    return new_company