from fastapi import APIRouter

from src.api.companies import router as companies_router

main_router = APIRouter()

main_router.include_router(companies_router)