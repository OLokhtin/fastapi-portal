from datetime import date

from pydantic import BaseModel

class ServiceCreateScheme(BaseModel):
    company_id: int
    service_name: str
    service_start_date: date
    service_end_date: date
    service_type: int