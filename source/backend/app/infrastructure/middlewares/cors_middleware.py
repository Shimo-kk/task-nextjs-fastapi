from starlette.middleware.cors import CORSMiddleware, ALL_METHODS
from starlette.types import ASGIApp

from app.core import ALLOW_ORIGINS, ALLOW_HEADERS


class CORSMiddleware(CORSMiddleware):
    """
    CROSを処理するミドルウェア
    """

    def __init__(self, app: ASGIApp) -> None:
        super().__init__(
            app,
            allow_origins=ALLOW_ORIGINS,
            allow_methods=ALL_METHODS,
            allow_headers=ALLOW_HEADERS,
            allow_credentials=True,
        )
