from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from pydantic import BaseModel

class Base(DeclarativeBase):
    pass

class CompanyModel(Base):
    __tablename__ = "companies"
    company_id: Mapped[int] = mapped_column(primary_key=True)
    company_name: Mapped[str]
    inn: Mapped[str]
    status: Mapped[int]

class CompanyCreateScheme(BaseModel):
    company_name: str
    inn: str
    status: int