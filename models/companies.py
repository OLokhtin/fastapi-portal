from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class BaseModel(DeclarativeBase):
    pass

class CompanyModel(BaseModel):
    __tablename__ = "companies"
    company_id: Mapped[int] = mapped_column(primary_key=True)
    company_name: Mapped[str]
    inn: Mapped[str]
    status: Mapped[int]