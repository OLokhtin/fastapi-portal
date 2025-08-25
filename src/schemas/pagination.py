from typing import Optional

from pydantic import BaseModel

class PaginationSchema(BaseModel):
    limit: Optional[int] = None
    offset: Optional[int] = None