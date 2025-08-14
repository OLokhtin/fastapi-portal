from pydantic import BaseModel, Field

class PaginationSchema(BaseModel):
    limit: int = Field(10, ge= 10, le=100)
    offset: int = Field(0, ge= 0)