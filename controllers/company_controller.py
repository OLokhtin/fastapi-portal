from main import app
from fastapi import HTTPException
from testDatabase import companies

@app.get("/companies/{company_id}",
         tags=["company-controller"],
         summary="get_company",)
def get_company(company_id: int):
    for company in companies:
        if company["company_id"] == company_id:
            return company
    raise HTTPException(status_code=404, detail="Company not found")

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