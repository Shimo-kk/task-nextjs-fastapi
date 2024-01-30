from fastapi import Request, Response, HTTPException, status

from app.core.auth import jwt_auth
from app.service.usecases.auth_usecase import AuthUseCase
from app.service.models.auth_model import SignInModel
from app.service.models.user_model import UserReadModel
from app.service.exceptions import (
    NotFoundError,
    BadRequestError,
)


class AuthController:
    """
    認証のコントローラークラス
    """

    @staticmethod
    def sign_in(request: Request, response: Response, data: SignInModel):
        """
        サインイン

        Args:
            request: リクエスト
            response: レスポンス
            data: サインインモデル

        Returns:
            UserReadModel: ユーザー参照モデル
        """
        try:
            usecase: AuthUseCase = AuthUseCase(db_session=request.state.db_session)
            result: UserReadModel = usecase.sign_in(data=data)

            subject: str = f"{result.work_space_id} {result.email}"
            token = jwt_auth.encode_jwt(subject=subject)

            response.set_cookie(
                key="access_token", value=f"Bearer {token}", httponly=True, samesite="none", secure=True
            )

        except NotFoundError as e:
            raise HTTPException(status_code=404, detail=str(e))
        except BadRequestError as e:
            raise HTTPException(status_code=400, detail=str(e))
        except Exception:
            raise

        return result

    @staticmethod
    def sign_out(request: Request, response: Response):
        """
        サインアウト

        Args:
            request: リクエスト
            response: レスポンス
        """
        response.set_cookie(key="access_token", value="", httponly=True, samesite="none", secure=True)
        return {"message": "サインアウトが完了しました。"}

    @staticmethod
    def get_current_signed_user(request: Request, response: Response):
        """
        現在サインインしているユーザーを取得

        Args:
            request: リクエスト
            response: レスポンス
        """
        try:
            # トークン取得
            access_token: str = request.cookies.get("access_token")
            scheme, _, token = access_token.partition(" ")
            if not access_token or scheme != "Bearer":
                raise HTTPException(status_code=401, detail="トークンが設定されていません。")

            # トークンのデコード
            subject = jwt_auth.decode_jwt(token)
            if subject is None:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="JWTトークンが不正か、有効期限が切れています。")

            # サブジェクトを使用して、ユーザー情報を取得
            work_space_id: int = int(subject.split(" ")[0])
            email: str = subject.split(" ")[1]
            usecase: AuthUseCase = AuthUseCase(db_session=request.state.db_session)
            result: UserReadModel = usecase.get_current_signed_user(work_space_id=work_space_id, email=email)

            return result

        except NotFoundError as e:
            raise HTTPException(status_code=404, detail=str(e))
