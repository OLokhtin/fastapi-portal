from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
from testDatabase import companies

app = FastAPI()

@app.get("/hello")
def read_root():
    return {"Hello": "World"}

#initiate with python main.py
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

@app.get("/companies",
         tags=["company-controller"],
         summary="get_companies",)
def get_companies():
    return companies

@app.get("/companies/{company_id}",
         tags=["company-controller"],
         summary="get_company",)
def get_company(company_id: int):
    for company in companies:
        if company["company_id"] == company_id:
            return company
    raise HTTPException(status_code=404, detail="Company not found")

class NewCompany(BaseModel):
    company_name: str
    inn: str
    status: int

@app.post("/companies",
          tags=["company-controller"],
          summary="create_company")
def create_company(new_company: NewCompany):
    companies.append({
        "id": len(companies) + 1,
        "company_name": new_company.company_name,
        "inn": new_company.inn,
        "status": new_company.status
    })
    return companies[-1]