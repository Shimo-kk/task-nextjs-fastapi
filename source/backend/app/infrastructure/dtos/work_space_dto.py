from sqlalchemy import Column, VARCHAR
from typing import Union

from app.infrastructure.dtos import BaseDto
from app.domain.entitys.work_space_entity import WorkSpaceEntity


class WorkSpaceDTO(BaseDto):
    """
    ワークスペースのDTOクラス

    Attributes:
        name: 名称
    """

    __tablename__ = "work_space"

    name: Union[str, Column] = Column(VARCHAR(255), unique=True, nullable=False, comment="名称")

    @staticmethod
    def from_entity(entity: WorkSpaceEntity) -> "WorkSpaceDTO":
        return WorkSpaceDTO(
            id=entity.id,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
            name=entity.name,
        )

    def to_entity(self) -> WorkSpaceEntity:
        return WorkSpaceEntity(
            id=self.id,
            created_at=self.created_at,
            updated_at=self.updated_at,
            name=self.name,
        )
