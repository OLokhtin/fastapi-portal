from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base

class UserModel(Base):
    __tablename__ = "users"
    user_id: Mapped[int] = mapped_column(primary_key=True)
    company_id: Mapped[int]
    user_full_name: Mapped[str]
    user_email: Mapped[str]