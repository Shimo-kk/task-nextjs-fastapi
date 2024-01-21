from datetime import datetime
from typing import Union
from sqlalchemy import Column, func
from sqlalchemy.dialects.postgresql import INTEGER, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseDto(Base):
    """
    DTOクラスのベース

    Attributes:
        id: 主キー
        created_at: 作成日時
        updated_at: 更新日時
    """

    __abstract__ = True

    id: Union[int, Column] = Column(
        INTEGER,
        primary_key=True,
        autoincrement=True,
    )

    created_at: Union[datetime, Column] = Column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
        nullable=False,
        comment="登録日時",
    )

    updated_at: Union[datetime, Column] = Column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
        comment="更新日時",
    )
