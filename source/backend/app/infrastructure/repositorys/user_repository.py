from app.infrastructure.dtos.user_dto import UserDto
from app.domain.entitys.user_entity import UserEntity, IUserRepository


class UserRepository(IUserRepository):
    """
    ユーザーのリポジトリクラス

    Attributes:
        db_session: DBセッション
    """

    def __init__(self, db_session):
        """
        Args:
            db_session: DBセッション
        """
        self.db_session = db_session

    def insert(self, user_entity: UserEntity) -> UserEntity:
        """
        ユーザーの挿入

        Args:
            user_entity: 挿入するユーザーのエンティティ
        Returns:
            UserEntity: 挿入したユーザーのエンティティ
        """
        user_dto: UserDto = UserDto.from_entity(user_entity)
        self.db_session.add(user_dto)
        self.db_session.flush()
        self.db_session.refresh(user_dto)

        result: UserEntity = user_dto.to_entity()
        return result

    def find_all(self, work_space_id: int) -> list[UserEntity]:
        """
        ワークスペースIDでの全件取得

        Args:
            work_space_id: ワークスペースID
        Returns:
            list[UserEntity]: 取得したユーザーのエンティティのリスト
        """
        user_dto_list: list[UserDto] = (
            self.db_session.query(UserDto).filter_by(work_space_id=work_space_id).order_by(UserDto.id)
        )

        result: list[UserEntity] = []
        for user_dto in user_dto_list:
            result.append(user_dto.to_entity())

        return result

    def find_by_id(self, id: int) -> UserEntity:
        """
        主キーでの取得

        Args:
            id: 主キー
        Returns:
            UserEntity: 取得したユーザーのエンティティ
        """
        user_dto: UserDto = self.db_session.query(UserDto).filter_by(id=id).first()
        if not user_dto:
            return None

        result: UserEntity = user_dto.to_entity()
        return result

    def find_by_email(self, work_space_id: int, email: str) -> UserEntity:
        """
        E-mailアドレスでの取得

        Args:
            email: E-mailアドレス
        Returns:
            UserEntity: 挿入したユーザーのエンティティ
        """
        user_dto: UserDto = self.db_session.query(UserDto).filter_by(work_space_id=work_space_id, email=email).first()
        if not user_dto:
            return None

        result: UserEntity = user_dto.to_entity()
        return result

    def update(self, user_entity: UserEntity) -> UserEntity:
        """
        ユーザーの更新

        Args:
            user_entity: 更新するユーザーのエンティティ
        Returns:
            UserEntity: 更新したユーザーのエンティティ
        """
        user_dto: UserDto = UserDto.from_entity(user_entity)
        _user: UserDto = self.db_session.query(UserDto).filter_by(id=user_dto.id).first()
        _user.name = user_dto.name
        _user.email = user_dto.email
        _user.password = user_dto.password
        self.db_session.flush()

        result: UserEntity = _user.to_entity()
        return result

    def delete_by_id(self, id: int) -> None:
        """
        主キーでの削除

        Args:
            id: 主キー
        """
        self.db_session.query(UserDto).filter_by(id=id).delete()

        return None
