from fastapi import Request, Response, HTTPException
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from app.core import logger
from app.infrastructure.database.postgresql_test import get_db_session


class TestHttpRequestMiddleware(BaseHTTPMiddleware):
    """
    HTTPリクエストを処理するミドルウェア（テスト用）
    """

    __test__ = False

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
            logger.error(str(e))
            request.state.db_session.rollback()

            detail = {
                "detail": str(e),
            }
            return JSONResponse(detail, status_code=500)
        finally:
            request.state.db_session.remove()
