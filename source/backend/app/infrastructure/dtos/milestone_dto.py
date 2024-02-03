from datetime import datetime
from sqlalchemy import Column, ForeignKey, INTEGER, VARCHAR, TIMESTAMP
from typing import Union

from app.infrastructure.dtos import BaseDto


class MilestoneDTO(BaseDto):
    """
    マイルストーンのDTOクラス

    Attributes:
        project_id: プロジェクトID
        name: 名称
        start_date: 開始日
        end_date: 終了日
    """

    __tablename__ = "milestone"

    project_id: Union[int, Column] = Column(
        INTEGER, ForeignKey("project.id", ondelete="CASCADE"), nullable=False, comment="プロジェクトID"
    )
    name: Union[str, Column] = Column(VARCHAR(50), nullable=False, comment="名称")
    start_date: Union[datetime, Column] = Column(TIMESTAMP(timezone=True), nullable=True, comment="開始日")
    end_date: Union[datetime, Column] = Column(TIMESTAMP(timezone=True), nullable=True, comment="終了日")
