from fastapi import APIRouter, Request, Response

from app.presentation.controllers.auth_controller import AuthController
from app.service.models.auth_model import SignInModel
from app.service.models.user_model import UserReadModel

router = APIRouter()


@router.post("/signin", response_model=UserReadModel)
async def sign_in(request: Request, response: Response, data: SignInModel):
    return AuthController.sign_in(request=request, response=response, data=data)


@router.get("/signout")
async def sign_out(request: Request, response: Response):
    return AuthController.sign_out(request=request, response=response)


@router.get("/get-current-signed-user", response_model=UserReadModel)
async def get_current_signed_user(request: Request, response: Response):
    return AuthController.get_current_signed_user(request=request, response=response)
