from fastapi import Request, Response, HTTPException
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from app.core import logger
from app.infrastructure.database.postgresql import get_db_session


class HttpRequestMiddleware(BaseHTTPMiddleware):
    """
    HTTPリクエストを処理するミドルウェア
    """

    async def dispatch(self, request: Request, call_next) -> Response:
        """
        ミドルウェアの処理

        Args:
            request (Request): リクエスト情報
            call_next (method): 次の処理

        Returns:
            Response: レスポンス
        """
        try:
            logger.info(f"{request.method} {request.url.path} HTTP/{request.scope['http_version']}")
            request.state.db_session = get_db_session()
            response: Response = await call_next(request)
            request.state.db_session.commit()
            return response
        except HTTPException as e:
            request.state.db_session.rollback()

            detail = {
                "detail": e.detail,
            }
            return JSONResponse(detail, status_code=e.status_code)
        except Exception as e:
            request.state.db_session.rollback()

            detail = {
                "detail": str(e),
            }
            return JSONResponse(detail, status_code=500)
        finally:
            request.state.db_session.remove()
