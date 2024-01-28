from sqlalchemy import Column, ForeignKey, INTEGER, VARCHAR, BOOLEAN
from typing import Union

from app.infrastructure.dtos import BaseDto
from app.domain.entitys.user_entity import UserEntity


class UserDto(BaseDto):
    """
    ユーザーのDTOクラス

    Attributes:
        work_space_id: ワークスペースID
        name: 名称
        email: E-mailアドレス
        password: パスワード（ハッシュ済み）
        is_admin: 管理者フラグ
    """

    __tablename__ = "user"

    work_space_id: Union[int, Column] = Column(
        INTEGER, ForeignKey("work_space.id", ondelete="CASCADE"), nullable=False, comment="ワークスペースID"
    )
    name: Union[str, Column] = Column(VARCHAR(50), nullable=False, comment="名称")
    email: Union[str, Column] = Column(VARCHAR(255), unique=True, nullable=False, comment="E-mailアドレス")
    password: Union[str, Column] = Column(VARCHAR(128), nullable=False, comment="パスワード")
    is_admin: Union[bool, Column] = Column(BOOLEAN, nullable=False, default=False, comment="管理者フラグ")

    @staticmethod
    def from_entity(entity: UserEntity) -> "UserDto":
        return UserDto(
            id=entity.id,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
            work_space_id=entity.work_space_id,
            name=entity.name,
            email=entity.email,
            password=entity.password,
            is_admin=entity.is_admin,
        )

    def to_entity(self) -> UserEntity:
        return UserEntity(
            id=self.id,
            created_at=self.created_at,
            updated_at=self.updated_at,
            work_space_id=self.work_space_id,
            name=self.name,
            email=self.email,
            password=self.password,
            is_admin=self.is_admin,
        )
