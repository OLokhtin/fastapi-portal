from fastapi import APIRouter, HTTPException, status

from src.api.dependencies import SessionDep, PaginationDep, AuthDep
from src.repository.companies import CompaniesRepository
from src.schemas.companies import CompanyScheme

router = APIRouter()

@router.get("/api/companies",
            tags=["company-controller"],
            summary="get_companies",
            dependencies=[AuthDep]
            )
async def get_all(session: SessionDep,
                  pagination: PaginationDep
                  ):
    companies = await CompaniesRepository.get_companies(session, pagination)
    return companies

@router.get("/api/companies/{company_id}",
            tags=["company-controller"],
            summary="get_company",
            dependencies=[AuthDep]
            )
async def get_one(company_id:int,
                  session: SessionDep
                  ):
    company = await CompaniesRepository.get_company(company_id, session)
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
async def create_one(data: CompanyScheme,
                     session: SessionDep
                     ):
    created_company = await CompaniesRepository.create_company(data, session)
    return created_company

@router.put("/api/companies/{company_id}",
            tags=["company-controller"],
            summary="update_company",
            dependencies=[AuthDep]
            )
async def update_one(
        company_id: int,
        data: CompanyScheme,
        session: SessionDep
):
    updated_company = await CompaniesRepository.update_company(company_id, data, session)
    if updated_company is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Company not found"
                            )
    return updated_company

@router.delete("/api/companies/{company_id}",
               tags=["company-controller"],
               summary="delete_company",
               dependencies=[AuthDep]
               )
async def delete_one(company_id: int,
                     session: SessionDep
                     ):
    await CompaniesRepository.delete_company(company_id, session)
    return {"message": "No Content"}