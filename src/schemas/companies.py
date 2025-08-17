from pydantic import BaseModel

class CompanyScheme(BaseModel):
    company_name: str
    inn: str
    status: int