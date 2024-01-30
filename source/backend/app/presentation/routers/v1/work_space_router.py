from fastapi import APIRouter, Request

from app.presentation.controllers.work_space_controller import WorkSpaceController
from app.service.models.work_space_model import WorkSpaceCreateModel, WorkSpaceReadModel

router = APIRouter()


@router.post("", response_model=WorkSpaceReadModel)
async def create_work_space(request: Request, data: WorkSpaceCreateModel):
    return WorkSpaceController.create_work_space(request=request, data=data)


@router.get("/{id}", response_model=WorkSpaceReadModel)
async def get_work_space(request: Request, id: int):
    return WorkSpaceController.get_work_space(request=request, id=id)
