from fastapi import APIRouter

from app.presentation.routers import csrf_router

api_router = APIRouter()
api_router.include_router(csrf_router.router, prefix="/csrf", tags=["csrf"])
