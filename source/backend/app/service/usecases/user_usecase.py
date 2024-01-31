from app.domain.entitys.user_entity import UserEntity, IUserRepository
from app.domain.entitys.work_space_entity import WorkSpaceEntity, IWorkSpaceRepository
from app.domain.exceptions import ValueObjectValidError
from app.infrastructure.repositorys.user_repository import UserRepository
from app.infrastructure.repositorys.work_space_repository import WorkSpaceRepository
from app.service.models.user_model import UserCreateModel, UserReadModel, UserUpdateModel
from app.service.exceptions import NotFoundError, AlreadyExistsError, ValidError


class UserUseCase:
    """
    ユーザーのユースケースクラス

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

    def create_user(self, data: UserCreateModel) -> UserReadModel:
        """
        ユーザーの作成

        Args:
            data: ユーザー作成モデル
        Returns:
            UserReadModel: 作成したユーザーの参照モデル
        """
        try:
            # ワークスペースIDでワークスペースを取得
            work_space_entity: WorkSpaceEntity = self.work_space_repository.find_by_id(id=data.work_space_id)
            if not work_space_entity:
                raise NotFoundError("ワークスペースが存在しません。")

            # E-mailでユーザーを取得
            user_entity: UserEntity = self.user_repository.find_by_email(
                work_space_id=work_space_entity.id, email=data.email
            )
            if user_entity:
                raise AlreadyExistsError("E-mailアドレスがすでに存在しています。")

            # ユーザーエンティティを作成
            new_user_entity: UserEntity = UserEntity.create(
                work_space_id=work_space_entity.id,
                name=data.name,
                email=data.email,
                password=data.password,
                is_admin=data.is_admin,
            )

            # ユーザーの挿入
            inserted_user_entity: UserEntity = self.user_repository.insert(user_entity=new_user_entity)

            # ユーザー参照モデルへ変換
            result: UserReadModel = UserReadModel(
                id=inserted_user_entity.id,
                work_space_id=inserted_user_entity.work_space_id,
                name=inserted_user_entity.name,
                email=inserted_user_entity.email,
                is_admin=inserted_user_entity.is_admin,
            )

            return result

        except ValueObjectValidError as e:
            raise ValidError(e)
        except Exception:
            raise

    def get_all_user(self, work_space_id: int) -> list[UserReadModel]:
        """
        全てのユーザーを取得

        Args:
            work_space_id: ワークスペースID
        Returns:
            list[UserReadModel]: 取得したユーザーの参照モデルリスト
        """
        try:
            # ワークスペースIDでワークスペースを取得
            work_space_entity: WorkSpaceEntity = self.work_space_repository.find_by_id(id=work_space_id)
            if not work_space_entity:
                raise NotFoundError("ワークスペースが存在しません。")

            # ワークスペースIDでユーザーを全て取得
            user_entity_list: list[UserEntity] = self.user_repository.find_all(work_space_id=work_space_entity.id)

            # ユーザー参照モデルへ変換
            result: list[UserReadModel] = []
            for user_entity in user_entity_list:
                user_read_model: UserReadModel = UserReadModel(
                    id=user_entity.id,
                    work_space_id=user_entity.work_space_id,
                    name=user_entity.name,
                    email=user_entity.email,
                    is_admin=user_entity.is_admin,
                )
                result.append(user_read_model)

            return result

        except Exception:
            raise

    def update_user(self, data: UserUpdateModel) -> UserReadModel:
        """
        ユーザーの更新

        Args:
            data: ユーザー更新モデル
        Returns:
            UserReadModel: 更新したユーザーの参照モデル
        """
        try:
            # 対象のユーザーを取得
            user_entity: UserEntity = self.user_repository.find_by_id(id=data.id)
            if not user_entity:
                raise NotFoundError("ユーザーが存在しません。")

            # ユーザーを更新
            user_entity.name = data.name
            user_entity.is_admin = data.is_admin
            updated_user_entity: UserEntity = self.user_repository.update(user_entity=user_entity)

            # ユーザー参照モデルへ変換
            result: UserReadModel = UserReadModel(
                id=updated_user_entity.id,
                work_space_id=updated_user_entity.work_space_id,
                name=updated_user_entity.name,
                email=updated_user_entity.email,
                is_admin=updated_user_entity.is_admin,
            )

            return result

        except Exception:
            raise

    def delete_user(self, id: int):
        """
        ユーザーの削除

        Args:
            id: ユーザーID
        """
        try:
            # ユーザーの削除
            self.user_repository.delete_by_id(id=id)

        except Exception:
            raise
