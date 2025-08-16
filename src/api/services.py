from fastapi import APIRouter
from sqlalchemy import select

from src.api.dependencies import SessionDep, PaginationDep
from src.models.services import ServiceModel
from src.schemas.services import ServiceCreateScheme

router = APIRouter()

@router.get("/services",
         tags=["service-controller"],
         summary="get_services")
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

@router.get("/services/{service_id}",
            tags=["service-controller"],
            summary="get_service")
async def get_service(service_id:int, session: SessionDep):
    query = (select(ServiceModel)
             .filter(ServiceModel.service_id == service_id))
    result = await session.execute(query)
    return result.scalars().first()

@router.post("/services",
          tags=["service-controller"],
          summary="create_service")
async def create_service(
        data: ServiceCreateScheme,
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