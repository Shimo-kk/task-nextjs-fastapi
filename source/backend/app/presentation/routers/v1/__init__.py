from fastapi import APIRouter

from app.presentation.routers.v1 import work_space_router
from app.presentation.routers.v1 import auth_router
from app.presentation.routers.v1 import user_router

api_v1_router = APIRouter()
api_v1_router.include_router(work_space_router.router, prefix="/work-space", tags=["work-space"])
api_v1_router.include_router(auth_router.router, prefix="/auth", tags=["auth"])
api_v1_router.include_router(user_router.router, prefix="/user", tags=["user"])
