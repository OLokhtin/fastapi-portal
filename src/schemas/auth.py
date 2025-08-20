from pydantic import BaseModel, EmailStr

class AuthScheme(BaseModel):
    email: EmailStr
    password: str

class ChangePassScheme(BaseModel):
    user_id: int
    old_password: str
    new_password: str