from main import app
from database import SessionDep
from models.companies_model import CompanyModel, CompanyCreateScheme
from sqlalchemy import select

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

# @app.get("/companies/{company_id}",
#          tags=["company-controller"],
#          summary="get_company")
# def get_company(company_id: int):
#     for company in companies:
#         if company["company_id"] == company_id:
#             return company
#     raise HTTPException(status_code=404, detail="Company not found")
#
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