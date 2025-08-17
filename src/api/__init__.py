from fastapi import APIRouter

from src.api.companies import router as companies_router
from src.api.services import router as services_router
from src.api.users import router as users_router
from src.api.auth import router as auth_router


main_router = APIRouter()

main_router.include_router(auth_router)
main_router.include_router(companies_router)
main_router.include_router(services_router)
main_router.include_router(users_router)