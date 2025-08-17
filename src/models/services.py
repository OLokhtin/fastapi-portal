from datetime import date

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base

class ServiceModel(Base):
    __tablename__ = "services"
    service_id: Mapped[int] = mapped_column(primary_key=True)
    company_id: Mapped[int] = mapped_column(ForeignKey("companies.company_id"))
    service_name: Mapped[str]
    service_start_date: Mapped[date]
    service_end_date: Mapped[date]
    service_type: Mapped[int]