import re
from datetime import datetime
from typing import ClassVar
from dataclasses import dataclass
from abc import ABC, abstractmethod

from app.domain.entitys import BaseEntity
from app.domain.exceptions import ValueObjectValidError


class WorkSpaceEntity(BaseEntity):
    """
    ワークスペースのエンティティクラス

    Attributes:
        name: 名称
    """

    @dataclass(frozen=True)
    class Name:
        """
        名称のValueObject
        """

        value: str

        MAX_LENGTH: ClassVar[int] = 255
        PATTERN: ClassVar[str] = "[ -~]+"

        def __init__(self, value: str):
            """
            Args:
                value: 値
            """
            length: int = len(value)
            if length > self.MAX_LENGTH:
                raise ValueObjectValidError("ワークスペース名が長すぎます。")

            if re.fullmatch(self.PATTERN, value) is None:
                raise ValueObjectValidError("ワークスペース名には半角英数字記号のみ使用可能です。")

            object.__setattr__(self, "value", value)

    def __init__(
        self,
        id: int = None,
        created_at: datetime = None,
        updated_at: datetime = None,
        name: str = "",
    ):
        """
        Args:
            id: 主キー
            created_at: 作成日時
            updated_at: 更新日時
            name: 名称
        """
        BaseEntity.__init__(self, id, created_at, updated_at)
        self.name: str = name

    def __eq__(self, o: object) -> bool:
        return BaseEntity.__eq__(o)

    @staticmethod
    def create(name: str) -> "WorkSpaceEntity":
        """
        ワークスペースエンティティの作成

        Args:
            name: 名称
        """
        return WorkSpaceEntity(
            name=WorkSpaceEntity.Name(name).value,
        )


class IWorkSpaceRepository(ABC):
    """
    ユーザーのリポジトリインターフェース
    """

    @abstractmethod
    def insert(self, work_space_entity: WorkSpaceEntity) -> WorkSpaceEntity:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, id: int) -> WorkSpaceEntity:
        raise NotImplementedError

    @abstractmethod
    def find_by_name(self, name: str) -> WorkSpaceEntity:
        raise NotImplementedError

    @abstractmethod
    def delete_by_id(self, id: int) -> None:
        raise NotImplementedError
