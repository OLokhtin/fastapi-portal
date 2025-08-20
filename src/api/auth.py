from fastapi import APIRouter, HTTPException, status, Response
from sqlalchemy import select, update

from src.api.dependencies import SessionDep, AuthDep
from src.models.users import CreateUserModel
from src.schemas.auth import AuthScheme, ChangePassScheme
from src.security import verify_password, security, config, hash_password

router = APIRouter()

@router.post("/api/login",
             tags=["auth-controller"],
             summary="login_user"
             )
async def login_user(creds: AuthScheme,
                     session: SessionDep,
                     response: Response
                     ):
    query = (select(CreateUserModel)
             .filter(CreateUserModel.user_email == creds.email)
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
            return {"message": "Successfully logged in"}
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

@router.post("/api/change_password",
             tags=["auth-controller"],
             summary="change_password",
             dependencies=[AuthDep]
             )
async def change_password(data: ChangePassScheme,
                          session: SessionDep
                          ):
    query = (select(CreateUserModel)
             .filter(CreateUserModel.user_id == data.user_id)
             )
    result = await session.execute(query)
    user = result.scalars().first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not found"
                            )
    else:
        if user.password is None or verify_password(data.old_password, user.password):
            query = ((update(CreateUserModel).
                      where(CreateUserModel.user_id == data.user_id)).
                     values(password=hash_password(data.new_password))
                     )
            await session.execute(query)
            await session.commit()
            return {"message": "Password changed successfully"}
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Incorrect old password"
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