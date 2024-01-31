from app.service.exceptions import NotFoundError, AlreadyExistsError, ValidError
from fastapi import Request, HTTPException, status

from app.service.usecases.user_usecase import UserUseCase
from app.service.models.user_model import UserCreateModel, UserReadModel, UserUpdateModel


class UserController:
    """
    ユーザーのコントローラークラス
    """

    @staticmethod
    def create_user(request: Request, data: UserCreateModel) -> UserReadModel:
        """
        ユーザーの作成

        Args:
            request: リクエスト
            data: ユーザー作成モデル

        Returns:
            UserReadModel: ユーザー参照モデル
        """
        try:
            usecase: UserUseCase = UserUseCase(db_session=request.state.db_session)
            result: UserReadModel = usecase.create_user(data=data)

            return result

        except NotFoundError as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
        except AlreadyExistsError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        except ValidError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        except Exception:
            raise

    @staticmethod
    def get_all_user(request: Request, work_space_id: int) -> list[UserReadModel]:
        """
        全てのユーザーを取得

        Args:
            request: リクエスト
            work_space_id: ワークスペースID
        Returns:
            list[UserReadModel]: 取得したユーザーの参照モデルリスト
        """
        try:
            usecase: UserUseCase = UserUseCase(db_session=request.state.db_session)
            result: list[UserReadModel] = usecase.get_all_user(work_space_id=work_space_id)

            return result

        except NotFoundError as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
        except Exception:
            raise

    @staticmethod
    def update_user(request: Request, data: UserUpdateModel) -> UserReadModel:
        """
        ユーザーの更新

        Args:
            request: リクエスト
            data: ユーザー更新モデル
        Returns:
            UserReadModel: 更新したユーザーの参照モデル
        """
        try:
            usecase: UserUseCase = UserUseCase(db_session=request.state.db_session)
            result: UserReadModel = usecase.update_user(data=data)

            return result

        except NotFoundError as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
        except Exception:
            raise

    @staticmethod
    def delete_user(request: Request, id: int):
        """
        ユーザーの削除

        Args:
            id: ユーザーID
        """
        try:
            usecase: UserUseCase = UserUseCase(db_session=request.state.db_session)
            usecase.delete_user(id=id)

        except Exception:
            raise
