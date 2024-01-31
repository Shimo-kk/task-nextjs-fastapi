from fastapi import APIRouter, Request

from app.presentation.controllers.user_controller import UserController
from app.service.models.user_model import UserReadModel, UserCreateModel, UserUpdateModel

router = APIRouter()


@router.post("", response_model=UserReadModel)
async def create_user(request: Request, data: UserCreateModel):
    return UserController.create_user(request=request, data=data)


@router.get("/{work_space_id}", response_model=list[UserReadModel])
async def get_all_user(request: Request, work_space_id: int):
    return UserController.get_all_user(request=request, work_space_id=work_space_id)


@router.put("", response_model=UserReadModel)
async def update_user(request: Request, data: UserUpdateModel):
    return UserController.update_user(request=request, data=data)


@router.delete("/{id}")
async def delete_user(request: Request, id: int):
    return UserController.delete_user(request=request, id=id)
