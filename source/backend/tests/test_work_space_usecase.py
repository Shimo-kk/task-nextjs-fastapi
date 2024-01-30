from app.service.usecases.work_space_usecase import WorkSpaceUseCase
from app.service.models.work_space_model import WorkSpaceCreateModel, WorkSpaceReadModel
from app.service.exceptions import (
    AlreadyExistsError,
    NotFoundError,
)


def test_create_ok(session):
    """
    ワークスペースの作成 正常
    """
    try:
        data: WorkSpaceCreateModel = WorkSpaceCreateModel(
            work_space_name="test.workspace",
            admin_name="test admin user",
            admin_email="test.admin@example.com",
            admin_password="testtest",
        )

        usecase: WorkSpaceUseCase = WorkSpaceUseCase(session)
        work_space_read_model: WorkSpaceReadModel = usecase.create_work_space(data=data)

    except Exception:
        assert False

    assert work_space_read_model.id is not None
    assert work_space_read_model.name == "test.workspace"


def test_create_ng_already_exists(session):
    """
    ワークスペースの作成 異常 重複
    """
    try:
        data: WorkSpaceCreateModel = WorkSpaceCreateModel(
            work_space_name="test1.workspace",
            admin_name="test admin user",
            admin_email="test.admin@example.com",
            admin_password="testtest",
        )

        usecase: WorkSpaceUseCase = WorkSpaceUseCase(session)
        _ = usecase.create_work_space(data=data)
        assert False

    except AlreadyExistsError:
        assert True


def test_get_ok(session):
    """
    ワークスペースの取得 正常
    """
    try:
        usecase: WorkSpaceUseCase = WorkSpaceUseCase(session)
        work_space_read_model: WorkSpaceReadModel = usecase.get_work_space(id=1)

    except Exception:
        assert False

    assert work_space_read_model.id == 1
    assert work_space_read_model.name == "test1.workspace"


def test_get_ng_not_found(session):
    """
    ワークスペースの取得 異常 存在しない
    """
    try:
        usecase: WorkSpaceUseCase = WorkSpaceUseCase(session)
        _ = usecase.get_work_space(id=4)
        assert False

    except NotFoundError:
        assert True
