from app.infrastructure.dtos.work_space_dto import WorkSpaceDTO
from app.domain.entitys.work_space_entity import WorkSpaceEntity, IWorkSpaceRepository


class WorkSpaceRepository(IWorkSpaceRepository):
    """
    ワークスペースのリポジトリクラス

    Attributes:
        db_session: DBセッション
    """

    def __init__(self, db_session):
        """
        Args:
            db_session: DBセッション
        """
        self.db_session = db_session

    def insert(self, work_space_entity: WorkSpaceEntity) -> WorkSpaceEntity:
        """
        ユーザーの挿入

        Args:
            work_space_entity: 挿入するワークスペースのエンティティ
        Returns:
            WorkSpaceEntity: 挿入したワークスペースのエンティティ
        """
        work_space_dto: WorkSpaceDTO = WorkSpaceDTO.from_entity(work_space_entity)
        self.db_session.add(work_space_dto)
        self.db_session.flush()
        self.db_session.refresh(work_space_dto)

        result: WorkSpaceEntity = work_space_dto.to_entity()
        return result

    def find_by_id(self, id: int) -> WorkSpaceEntity:
        """
        主キーでの取得

        Args:
            id: 主キー
        Returns:
            WorkSpaceEntity: 取得したワークスペースのエンティティ
        """
        work_space_dto: WorkSpaceDTO = self.db_session.query(WorkSpaceDTO).filter_by(id=id).first()
        if not work_space_dto:
            return None

        result: WorkSpaceEntity = work_space_dto.to_entity()
        return result

    def find_by_name(self, name: str) -> WorkSpaceEntity:
        """
        名称での取得

        Args:
            name: 名称
        Returns:
            WorkSpaceEntity: 取得したワークスペースのエンティティ
        """
        work_space_dto: WorkSpaceDTO = self.db_session.query(WorkSpaceDTO).filter_by(name=name).first()
        if not work_space_dto:
            return None

        result: WorkSpaceEntity = work_space_dto.to_entity()
        return result

    def delete_by_id(self, id: int) -> None:
        """
        主キーでの削除

        Args:
            id: 主キー
        """
        self.db_session.query(WorkSpaceDTO).filter_by(id=id).delete()

        return None
