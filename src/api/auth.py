from fastapi import APIRouter, HTTPException
from sqlalchemy import select

from src.api.dependencies import SessionDep
from src.models.users import UserModel
from src.schemas.auth import AuthScheme
from src.security import verify_password, security

router = APIRouter()

@router.post("/api/login",
          tags=["auth-controller"],
          summary="login_user")
async def create_user(creds: AuthScheme,
                session: SessionDep):
    query = (select(UserModel)
             .filter(UserModel.user_email == creds.email))
    result = await session.execute(query)
    user = result.scalars().first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        if verify_password(creds.password, user.password):
            token = security.create_access_token(uid="123")
            return {"token": token}
        else:
            raise HTTPException(status_code=401, detail="Incorrect password")