from pydantic import BaseModel, Field

from datetime import date

class ServiceScheme(BaseModel):
    company_id: int = Field(gt=0)
    service_name: str
    service_start_date: date
    service_end_date: date = None
    service_type: int = Field(gt=0)