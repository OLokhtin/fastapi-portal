from pydantic import BaseModel

class CompanyCreateScheme(BaseModel):
    company_name: str
    inn: str
    status: int