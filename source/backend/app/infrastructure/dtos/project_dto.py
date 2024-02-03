from datetime import datetime
from sqlalchemy import Column, ForeignKey, INTEGER, VARCHAR, TEXT, TIMESTAMP
from typing import Union

from app.infrastructure.dtos import BaseDto


class ProjectDTO(BaseDto):
    """
    プロジェクトのDTOクラス

    Attributes:
        work_space_id: ワークスペースID
        name: 名称
        summary: 概要
        start_date: 開始日
        end_date: 終了日
    """

    __tablename__ = "project"

    work_space_id: Union[int, Column] = Column(
        INTEGER, ForeignKey("work_space.id", ondelete="CASCADE"), nullable=False, comment="ワークスペースID"
    )
    name: Union[str, Column] = Column(VARCHAR(50), nullable=False, comment="名称")
    summary: Union[str, Column] = Column(TEXT, nullable=True, comment="概要")
    start_date: Union[datetime, Column] = Column(TIMESTAMP(timezone=True), nullable=True, comment="開始日")
    end_date: Union[datetime, Column] = Column(TIMESTAMP(timezone=True), nullable=True, comment="終了日")
