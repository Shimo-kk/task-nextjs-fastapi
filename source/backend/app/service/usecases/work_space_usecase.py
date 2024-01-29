from app.domain.exceptions import ValueObjectValidError
from app.domain.entitys.user_entity import UserEntity, IUserRepository
from app.domain.entitys.work_space_entity import WorkSpaceEntity, IWorkSpaceRepository
from app.infrastructure.repositorys.user_repository import UserRepository
from app.infrastructure.repositorys.work_space_repository import WorkSpaceRepository
from app.service.models.work_space_model import WorkSpaceCreateModel, WorkSpaceReadModel
from app.service.exceptions import (
    ValidError,
    AlreadyExistsError,
    NotFoundError,
)


class WorkSpaceUseCase:
    """
    ワークスペースのユースケースクラス

    Attributes:
        db_session: DBセッション
    """

    def __init__(self, db_session):
        """
        Args:
            db_session: DBセッション
        """
        self.db_session = db_session

        self.work_space_repository: IWorkSpaceRepository = WorkSpaceRepository(db_session=self.db_session)
        self.user_repository: IUserRepository = UserRepository(db_session=self.db_session)

    def create_work_space(self, data: WorkSpaceCreateModel) -> WorkSpaceReadModel:
        """
        ワークスペースの作成

        Args:
            data: ワークスペース作成モデル
        Returns:
            WorkSpaceReadModel: 作成したワークスペースの参照モデル
        """
        try:
            # 名称でワークスペースを取得
            work_space_entity: WorkSpaceEntity = self.work_space_repository.find_by_name(name=data.work_space_name)
            if work_space_entity:
                raise AlreadyExistsError("同名のワークスペースが既に存在しています。")

            # ワークスペースエンティティを作成
            new_work_space_entity: WorkSpaceEntity = WorkSpaceEntity.create(name=data.work_space_name)

            # ワークスペースの挿入
            inserted_work_space_entity: WorkSpaceEntity = self.work_space_repository.insert(
                work_space_entity=new_work_space_entity
            )

            # 管理者ユーザーのエンティティを作成
            new_user_entity: UserEntity = UserEntity.create(
                work_space_id=inserted_work_space_entity.id,
                name=data.admin_name,
                email=data.admin_email,
                password=data.admin_password,
                is_admin=True,
            )

            # 管理者ユーザーの挿入
            self.user_repository.insert(user_entity=new_user_entity)

            # 参照モデルへ変換
            result: WorkSpaceReadModel = WorkSpaceReadModel(
                id=inserted_work_space_entity.id, name=inserted_work_space_entity.name
            )

            return result

        except ValueObjectValidError as e:
            raise ValidError(e)
        except Exception:
            raise

    def get_work_space(self, name: str) -> WorkSpaceReadModel:
        """
        ワークスペースの取得

        Args:
            name: ワークスペース名
        Returns:
            WorkSpaceReadModel: 取得したワークスペースの参照モデル
        """
        try:
            # 名称でワークスペースを取得
            work_space_entity: WorkSpaceEntity = self.work_space_repository.find_by_name(name=name)
            if not work_space_entity:
                raise NotFoundError("ワークスペースが存在しません。")

            # 参照モデルへ変換
            result: WorkSpaceReadModel = WorkSpaceReadModel(id=work_space_entity.id, name=work_space_entity.name)

            return result

        except Exception:
            raise
