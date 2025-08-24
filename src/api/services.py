from fastapi import APIRouter
from sqlalchemy import select, update, delete, func

from src.api.dependencies import SessionDep, PaginationDep, AuthDep
from src.models.services import ServiceModel
from src.schemas.services import ServiceScheme

router = APIRouter()

@router.get("/api/services",
            tags=["service-controller"],
            summary="get_services",
            dependencies=[AuthDep]
            )
async def get_services(
        session: SessionDep,
        pagination: PaginationDep
):
    query = (select(ServiceModel)
             .limit(pagination.limit)
             .offset(pagination.offset)
     )
    result = await session.execute(query)
    return result.scalars().all()

@router.get("/api/services/{service_id}",
            tags=["service-controller"],
            summary="get_service",
            dependencies=[AuthDep]
            )
async def get_service(service_id:int, session: SessionDep):
    query = (select(ServiceModel)
             .filter(ServiceModel.service_id == service_id)
             )
    result = await session.execute(query)
    return result.scalars().first()

@router.post("/api/services",
             tags=["service-controller"],
             summary="create_service",
             dependencies=[AuthDep]
             )
async def create_service(
        data: ServiceScheme,
        session: SessionDep
):
    new_service = ServiceModel(
        company_id = data.company_id,
        service_name = data.service_name,
        service_start_date = data.service_start_date,
        service_end_date = data.service_end_date,
        service_type = data.service_type
    )
    session.add(new_service)
    await session.commit()
    return new_service

@router.put("/api/services/{service_id}",
            tags=["service-controller"],
            summary="update_service",
            dependencies=[AuthDep]
            )
async def update_service(
        service_id: int,
        data: ServiceScheme,
        session: SessionDep
):
    query = ((update(ServiceModel).
             where(ServiceModel.service_id == service_id)).
             values(company_id = data.company_id,
                    service_name = data.service_name,
                    service_start_date = data.service_start_date,
                    service_end_date = data.service_end_date,
                    service_type = data.service_type)
             )
    await session.execute(query)
    await session.commit()
    return {"message":"OK"}

@router.delete("/api/services/{service_id}",
               tags=["service-controller"],
               summary="delete_service",
               dependencies=[AuthDep]
               )
async def delete_service(service_id: int, session: SessionDep):
    query = (delete(ServiceModel).
             where(ServiceModel.service_id == service_id)
             )
    await session.execute(query)
    await session.commit()
    return {"message":"No Content"}

@router.delete("/api/delete_last_service",
               tags=["service-controller"],
               summary="delete_last_service",
               dependencies=[AuthDep]
               )
async def delete_last_service(session: SessionDep):
    query = select(func.max(ServiceModel.service_id))
    result = await session.execute(query)
    service_id = result.scalar()
    query = (delete(ServiceModel).
             where(ServiceModel.service_id == service_id)
             )
    await session.execute(query)
    await session.commit()
    return {"Deleted service": service_id}