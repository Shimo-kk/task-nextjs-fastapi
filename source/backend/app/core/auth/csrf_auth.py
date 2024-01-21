from fastapi import Request
from fastapi_csrf_protect import CsrfProtect
from pydantic import BaseModel

from app.core import CSRF_KEY


class CsrfSettings(BaseModel):
    secret_key: str = CSRF_KEY


@CsrfProtect.load_config
def get_csrf_config():
    return CsrfSettings()


def generate_csrf():
    csrf_protect: CsrfProtect = CsrfProtect()
    return csrf_protect.generate_csrf()


def validate_csrf(request: Request):
    csrf_protect: CsrfProtect = CsrfProtect()
    csrf_token = csrf_protect.get_csrf_from_headers(request.headers)
    csrf_protect.validate_csrf(csrf_token)
