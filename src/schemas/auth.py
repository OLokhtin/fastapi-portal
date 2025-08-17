from pydantic import BaseModel

class AuthScheme(BaseModel):
    email: str
    password: str