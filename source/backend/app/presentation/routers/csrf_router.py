from fastapi import APIRouter, Request, Response

from app.core.auth import csrf_auth


router = APIRouter()


@router.get("")
async def get_csrf(request: Request, response: Response):
    token: str = csrf_auth.generate_csrf()
    return {"csrf_token": token}
