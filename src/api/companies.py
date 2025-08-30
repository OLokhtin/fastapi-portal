from fastapi import APIRouter, HTTPException, status
from sqlalchemy import select, delete, update

from src.api.dependencies import SessionDep, PaginationDep, AuthDep
from src.models.companies import CompanyModel
from src.schemas.companies import CompanyScheme

router = APIRouter()

@router.get("/api/companies",
            tags=["company-controller"],
            summary="get_companies",
            dependencies=[AuthDep]
            )
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

@router.get("/api/companies/{company_id}",
            tags=["company-controller"],
            summary="get_company",
            dependencies=[AuthDep]
            )
async def get_company(company_id:int, session: SessionDep):
    query = (select(CompanyModel)
             .filter(CompanyModel.company_id == company_id)
             )
    result = await session.execute(query)
    company = result.scalars().first()
    if company is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Company not found"
                            )
    return company

@router.post("/api/companies",
             tags=["company-controller"],
             summary="create_company",
             dependencies=[AuthDep]
             )
async def create_company(
        data: CompanyScheme,
        session: SessionDep
):
    new_company = CompanyModel(
        company_name = data.company_name,
        inn = data.inn,
        status = data.status
    )
    session.add(new_company)
    await session.flush()
    await session.commit()
    return new_company

@router.put("/api/companies/{company_id}",
            tags=["company-controller"],
            summary="update_company",
            dependencies=[AuthDep]
            )
async def update_company(
        company_id: int,
        data: CompanyScheme,
        session: SessionDep
):
    query = ((update(CompanyModel).
             where(CompanyModel.company_id == company_id)).
             values(company_name=data.company_name,
                    inn=data.inn,
                    status=data.status).
             returning(CompanyModel)
             )
    result = await session.execute(query)
    updated_company = result.scalars().first()
    if updated_company is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Company not found"
                            )
    await session.commit()
    return updated_company

@router.delete("/api/companies/{company_id}",
               tags=["company-controller"],
               summary="delete_company",
               dependencies=[AuthDep]
               )
async def delete_company(company_id: int, session: SessionDep):
    query = (delete(CompanyModel).
             where(CompanyModel.company_id == company_id)
             )
    await session.execute(query)
    await session.commit()
    return {"message":"No Content"}