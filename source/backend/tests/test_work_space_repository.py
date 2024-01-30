from app.domain.entitys.work_space_entity import WorkSpaceEntity, IWorkSpaceRepository
from app.infrastructure.repositorys.work_space_repository import WorkSpaceRepository


def test_insert_ok(session):
    """
    挿入 正常
    """
    try:
        repository: IWorkSpaceRepository = WorkSpaceRepository(session)

        new_entity: WorkSpaceEntity = WorkSpaceEntity.create(name="test.workspace")
        repository.insert(work_space_entity=new_entity)
        session.commit()

        entity: WorkSpaceEntity = repository.find_by_name(name=new_entity.name)
    except Exception:
        assert False

    assert entity.id is not None
    assert entity.created_at is not None
    assert entity.updated_at is not None
    assert entity.name == new_entity.name


def test_insert_ng_already_exists(session):
    """
    挿入 異常 重複
    """
    try:
        repository: IWorkSpaceRepository = WorkSpaceRepository(session)

        entity: WorkSpaceEntity = repository.find_by_id(id=1)
        new_entity: WorkSpaceEntity = WorkSpaceEntity.create(name=entity.name)
        repository.insert(user_entity=new_entity)
        session.commit()
    except Exception:
        assert True


def test_get_ok(session):
    """
    取得 正常
    """
    try:
        repository: IWorkSpaceRepository = WorkSpaceRepository(session)
        entity: WorkSpaceEntity = repository.find_by_name(name="test1.workspace")
    except Exception:
        assert False

    assert entity.id == 1
    assert entity.name == "test1.workspace"


def test_get_ng_not_found(session):
    """
    取得 異常 存在しない
    """
    try:
        repository: IWorkSpaceRepository = WorkSpaceRepository(session)
        entity: WorkSpaceEntity = repository.find_by_name(name="test.workspace")
    except Exception:
        assert False

    assert entity is None


def test_delete_ok(session):
    """
    削除 正常
    """
    try:
        repository: IWorkSpaceRepository = WorkSpaceRepository(session)

        repository.delete_by_id(id=1)
        session.commit()

        entity: WorkSpaceEntity = repository.find_by_id(id=1)
    except Exception:
        assert False

    assert entity is None
