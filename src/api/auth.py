from fastapi import APIRouter, HTTPException, status, Response
from sqlalchemy import select

from src.api.dependencies import SessionDep, AuthDep
from src.models.users import UserModel
from src.schemas.auth import AuthScheme
from src.security import verify_password, security, config

router = APIRouter()

@router.post("/api/login",
          tags=["auth-controller"],
          summary="login_user"
             )
async def login_user(creds: AuthScheme,
                     session: SessionDep,
                     response: Response
                     ):
    query = (select(UserModel)
             .filter(UserModel.user_email == creds.email)
             )
    result = await session.execute(query)
    user = result.scalars().first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not found"
                            )
    else:
        if verify_password(creds.password, user.password):
            token = security.create_access_token(uid=str(user.user_id))
            response.set_cookie(key=config.JWT_ACCESS_COOKIE_NAME,
                                value=token
                                )
            return {"message": "Successfully logged in", "token": token}
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Incorrect password"
                                )

@router.post("/api/logout",
             tags=["auth-controller"],
             summary="logout_user"
             )
async def logout_user(response: Response):
    response.delete_cookie(key=config.JWT_ACCESS_COOKIE_NAME)
    return {"message": "Successfully logged out"}

@router.get("/api/secret_data",
            tags=["auth-controller"],
            summary="get_secret_data",
            dependencies=[AuthDep]
            )
def get_secret_data():
    return {"message": "secret data"}