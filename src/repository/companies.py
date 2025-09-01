from sqlalchemy import select, delete, update

from src.api.dependencies import SessionDep, PaginationDep
from src.models.companies import CompanyModel
from src.schemas.companies import CompanyScheme

class CompaniesRepository:
    @classmethod
    async def get_companies(cls,
                            session: SessionDep,
                            pagination: PaginationDep
                            ):
        query = (select(CompanyModel)
                 .limit(pagination.limit)
                 .offset(pagination.offset)
         )
        result = await session.execute(query)
        companies = result.scalars().all()
        return companies

    @classmethod
    async def get_company(cls,
                          company_id: int,
                          session: SessionDep
                          ):
        query = (select(CompanyModel)
                 .filter(CompanyModel.company_id == company_id)
                 )
        result = await session.execute(query)
        company = result.scalars().first()
        return company

    @classmethod
    async def create_company(cls,
                             data: CompanyScheme,
                             session: SessionDep
                             ):
        new_company = CompanyModel(
            company_name=data.company_name,
            inn=data.inn,
            status=data.status
        )
        session.add(new_company)
        await session.flush()
        await session.commit()
        return new_company

    @classmethod
    async def update_company(cls,
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
        await session.commit()
        updated_company = result.scalars().first()
        return updated_company

    @classmethod
    async def delete_company(cls,
                             company_id: int,
                             session: SessionDep
                             ):
        query = (delete(CompanyModel).
                 where(CompanyModel.company_id == company_id)
                 )
        await session.execute(query)
        await session.commit()