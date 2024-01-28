from fastapi import Request, Response, HTTPException, status
from starlette.middleware.base import BaseHTTPMiddleware

from app.core.auth import csrf_auth, jwt_auth


# CSRFトークン認証を行わないメソッド
CSRF_AUTH_EXCLUSION_METHOD = [
    "GET",
]

# JWTトークン認証を行わないパス
AWT_AUTH_EXCLUSION_PATH = ["/", "/favicon.ico", "/docs", "/openapi.json", "/api/csrf"]


class AuthMiddleware(BaseHTTPMiddleware):
    """
    認証処理を行うミドルウェア
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

        # CSRF認証
        if request.method not in CSRF_AUTH_EXCLUSION_METHOD:
            try:
                csrf_auth.validate_csrf(request)
            except Exception:
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="CSRFトークンの認証に失敗しました。")

        # JWT認証
        if request.url.path in AWT_AUTH_EXCLUSION_PATH:
            return await call_next(request)

        # CookieからJWTトークンを取得
        access_token: str = request.cookies.get("access_token")
        scheme, _, token = access_token.partition(" ")
        if not access_token or scheme != "Bearer":
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="JWTトークンが設定されていません。")

        # JWTトークンのデコード
        subject = jwt_auth.decode_jwt(token)
        if subject is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="JWTトークンが不正か、有効期限が切れています。")

        # 次の処理を実行
        response: Response = await call_next(request)

        # JWTトークンを更新
        jwt_token = jwt_auth.encode_jwt(subject)
        response.set_cookie(
            key="access_token", value=f"Bearer {jwt_token}", httponly=True, samesite="none", secure=True
        )

        return response
