from app.domain.entitys.user_entity import UserEntity, IUserRepository
from app.domain.entitys.work_space_entity import WorkSpaceEntity, IWorkSpaceRepository
from app.infrastructure.repositorys.user_repository import UserRepository
from app.infrastructure.repositorys.work_space_repository import WorkSpaceRepository
from app.service.models.auth_model import SignInModel
from app.service.models.user_model import UserReadModel
from app.service.exceptions import (
    NotFoundError,
    BadRequestError,
)


class AuthUseCase:
    """
    認証のユースケースクラス

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

    def sign_in(self, data: SignInModel) -> UserReadModel:
        """
        サインイン

        Args:
            data: サインインモデル
        """
        try:
            # ワークスペース名でワークスペースを取得
            work_space_entity: WorkSpaceEntity = self.work_space_repository.find_by_name(name=data.work_space_name)
            if not work_space_entity:
                raise NotFoundError("ワークスペースが存在しません。")

            # E-mailでユーザーを取得
            user_entity: UserEntity = self.user_repository.find_by_email(
                work_space_id=work_space_entity.id, email=data.email
            )
            if not user_entity:
                raise NotFoundError("E-mailアドレスが存在しません。")

            # パスワードが正しくない場合は例外を投げる
            if not user_entity.verify_password(plain_pw=data.password):
                raise BadRequestError("パスワードに誤りがあります。")

            # ユーザー参照モデルへ変換
            result: UserReadModel = UserReadModel(
                id=user_entity.id,
                work_space_id=user_entity.work_space_id,
                name=user_entity.name,
                email=user_entity.email,
                is_admin=user_entity.is_admin,
            )

            return result

        except Exception:
            raise

    def get_current_signed_user(self, work_space_id: int, email: str) -> UserReadModel:
        """
        現在サインインしているユーザーを取得

        Args:
            work_space_name: ワークスペース名
            email: E-Mailアドレス
        """
        try:
            # E-mailでユーザーを取得
            user_entity: UserEntity = self.user_repository.find_by_email(work_space_id=work_space_id, email=email)

            # ユーザーが存在しない場合は例外を投げる
            if not user_entity:
                raise NotFoundError("ユーザーが存在しません。")

            # ユーザー参照モデルへ変換
            result: UserReadModel = UserReadModel(
                id=user_entity.id,
                work_space_id=user_entity.work_space_id,
                name=user_entity.name,
                email=user_entity.email,
                is_admin=user_entity.is_admin,
            )

            return result

        except Exception:
            raise
