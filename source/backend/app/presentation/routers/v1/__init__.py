from fastapi import APIRouter

from app.presentation.routers.v1 import work_space_router

api_v1_router = APIRouter()
api_v1_router.include_router(work_space_router.router, prefix="/work-space", tags=["work-space"])
