from datetime import date

from pydantic import BaseModel, Field

class ServiceScheme(BaseModel):
    company_id: int = Field(gt=0)
    service_name: str
    service_start_date: date
    service_end_date: date
    service_type: int = Field(gt=0)