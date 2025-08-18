import random

from fastapi import APIRouter
from sqlalchemy import select, update, delete

from src.api.dependencies import SessionDep, PaginationDep, AuthDep
from src.models.users import UserModel
from src.schemas.users import UserScheme
from src.security import hash_password

router = APIRouter()

@router.get("/api/users",
            tags=["user-controller"],
            summary="get_users",
            dependencies=[AuthDep]
            )
async def get_users(
        session: SessionDep,
        pagination: PaginationDep
):
    query = (select(UserModel)
             .limit(pagination.limit)
             .offset(pagination.offset)
     )
    result = await session.execute(query)
    return result.scalars().all()

@router.get("/api/users/{user_id}",
            tags=["user-controller"],
            summary="get_user",
            dependencies=[AuthDep]
            )
async def get_user(user_id:int, session: SessionDep):
    query = (select(UserModel)
             .filter(UserModel.user_id == user_id)
             )
    result = await session.execute(query)
    return result.scalars().first()

@router.post("/api/users",
             tags=["user-controller"],
             summary="create_user",
             dependencies=[AuthDep]
             )
async def create_user(
        data: UserScheme,
        session: SessionDep
):

    new_user = UserModel(
        company_id = data.company_id,
        user_full_name = data.user_full_name,
        user_email = data.user_email,
        password = hash_password(data.password)
    )
    session.add(new_user)
    await session.commit()
    return new_user

@router.put("/api/users/{user_id}",
            tags=["user-controller"],
            summary="update_user",
            dependencies=[AuthDep]
            )
async def update_user(
        user_id: int,
        data: UserScheme,
        session: SessionDep
):
    query = ((update(UserModel).
             where(UserModel.user_id == user_id)).
             values(company_id = data.company_id,
                    user_full_name = data.user_full_name,
                    user_email = data.user_email)
             )
    await session.execute(query)
    await session.commit()
    return {"message":"OK"}

@router.delete("/api/users/{user_id}",
               tags=["user-controller"],
               summary="delete_user",
               dependencies=[AuthDep]
               )
async def delete_user(user_id: int, session: SessionDep):
    query = (delete(UserModel).
             where(UserModel.user_id == user_id)
             )
    await session.execute(query)
    await session.commit()
    return {"message":"No Content"}

@router.delete("/api/users",
          tags=["user-controller"],
          summary="delete_random_user"
               )
async def delete_user(session: SessionDep):
    user_id = random.randint(1, 10)
    query = (delete(UserModel).
             where(UserModel.user_id == user_id)
             )
    await session.execute(query)
    await session.commit()
    return {"Deleted user": user_id}