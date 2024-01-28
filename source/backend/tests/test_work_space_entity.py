from app.domain.entitys.work_space_entity import WorkSpaceEntity
from app.domain.exceptions import ValueObjectValidError


def test_create_ok():
    """
    作成 正常
    """
    try:
        new_work_space_entity: WorkSpaceEntity = WorkSpaceEntity.create(name="test.workspace")
    except Exception:
        assert False

    assert new_work_space_entity.id is None
    assert new_work_space_entity.created_at is None
    assert new_work_space_entity.updated_at is None
    assert new_work_space_entity.name == "test.workspace"


def test_create_ng_name_max_length():
    """
    作成 異常 名称が長すぎる
    """
    try:
        _ = WorkSpaceEntity.create(
            name="test.workspacetest.workspacetest.workspacetest.workspacetest.workspacetest.workspacetest.workspacetest.workspacetest.workspacetest.workspacetest.workspacetest.workspacetest.workspacetest.workspacetest.workspacetest.workspacetest.workspacetest.workspacetest.workspacetest.workspacetest.workspacetest.workspacetest.workspacetest.workspacetest.workspacetest.workspacetest.workspace"
        )
        assert False
    except ValueObjectValidError:
        assert True


def test_create_ng_not_match_the_pattern():
    """
    作成 異常 正規表現にマッチしない
    """
    try:
        _ = WorkSpaceEntity.create(name="テストワークスペース")
        assert False
    except ValueObjectValidError:
        assert True
