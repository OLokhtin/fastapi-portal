from fastapi import APIRouter, HTTPException
from sqlalchemy import select
from authx import AuthX, AuthXConfig
from dotenv import load_dotenv
import os

from src.api.dependencies import SessionDep
from src.models.users import UserModel
from src.schemas.auth import AuthScheme

router = APIRouter()

config = AuthXConfig()
load_dotenv()
config.JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
config.JWT_ACCESS_COOKIE_NAME = "X-Access-Token"
config.JWT_TOKEN_LOCATION = ["cookies"]

security = AuthX(config=config)

@router.post("/login",
          tags=["auth-controller"],
          summary="login_user")
async def create_user(creds: AuthScheme,
                session: SessionDep):
    query = (select(UserModel)
             .filter(UserModel.user_email == creds.email))
    result = await session.execute(query)
    if result.scalars().first() is None:
        raise HTTPException(status_code=401, detail="User not found")
    else:
        token = security.create_access_token(uid="123")
        return {"token": token}