from pydantic import BaseModel, Field

class CompanyScheme(BaseModel):
    company_name: str
    inn: str = Field(min_length=9, max_length=12)
    status: int = Field(gt=0)