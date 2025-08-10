from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel, Field
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

class companyScheme(BaseModel):
    company_name: str
    inn: str = Field(max_length=12)
    status: int = Field(ge=1, le=4)
    description: str | None = Field(max_length=255)

@app.post("/companies",
          tags=["company-controller"],
          summary="create_company")
def create_company(company: companyScheme):
    companies.append({
        "id": len(companies) + 1,
        "company_name": company.company_name,
        "inn": company.inn,
        "status": company.status
    })
    return companies[-1]