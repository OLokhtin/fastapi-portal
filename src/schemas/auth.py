from pydantic import BaseModel

class AuthScheme(BaseModel):
    email: str
    password: str

class ChangePassScheme(BaseModel):
    user_id: int
    old_password: str
    new_password: str