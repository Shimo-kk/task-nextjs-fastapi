from fastapi import Request, HTTPException, status

from app.service.models.work_space_model import WorkSpaceCreateModel, WorkSpaceReadModel
from app.service.usecases.work_space_usecase import WorkSpaceUseCase
from app.service.exceptions import (
    ValidError,
    AlreadyExistsError,
    NotFoundError,
)


class WorkSpaceController:
    """
    ワークスペースのコントローラークラス
    """

    @staticmethod
    def create_work_space(request: Request, data: WorkSpaceCreateModel) -> WorkSpaceReadModel:
        """
        ワークスペースの作成

        Args:
            request: リクエスト
            data: ワークスペース作成モデル
        Returns:
            WorkSpaceReadModel: 作成したワークスペースの参照モデル
        """
        try:
            usecase: WorkSpaceUseCase = WorkSpaceUseCase(db_session=request.state.db_session)
            result: WorkSpaceReadModel = usecase.create_work_space(data=data)
            return result
        except AlreadyExistsError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        except ValidError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        except Exception:
            raise

    @staticmethod
    def get_work_space(request: Request, id: int) -> WorkSpaceReadModel:
        """
        ワークスペースの取得

        Args:
            request: リクエスト
            id: 主キー
        Returns:
            WorkSpaceReadModel: 取得したワークスペースの参照モデル
        """
        try:
            usecase: WorkSpaceUseCase = WorkSpaceUseCase(db_session=request.state.db_session)
            result: WorkSpaceReadModel = usecase.get_work_space(id=id)
            return result
        except NotFoundError as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
        except Exception:
            raise
