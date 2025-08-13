from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base

class CompanyModel(Base):
    __tablename__ = "companies"
    company_id: Mapped[int] = mapped_column(primary_key=True)
    company_name: Mapped[str]
    inn: Mapped[str]
    status: Mapped[int]