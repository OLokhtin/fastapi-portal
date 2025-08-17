from pydantic import BaseModel, Field, EmailStr

class UserScheme(BaseModel):
    company_id: int = Field(gt=0)
    user_full_name: str
    user_email: EmailStr
    password: str