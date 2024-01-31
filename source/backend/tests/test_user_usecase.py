from app.service.usecases.user_usecase import UserUseCase
from app.service.models.user_model import UserCreateModel, UserReadModel, UserUpdateModel
from app.service.exceptions import NotFoundError, AlreadyExistsError


def test_create_ok(session):
    """
    作成 正常
    """
    try:
        data: UserCreateModel = UserCreateModel(
            work_space_id=1, name="test user", email="test@example.com", password="testtest", is_admin=False
        )
        usecase: UserUseCase = UserUseCase(session)
        user_read_model: UserReadModel = usecase.create_user(data)

    except Exception:
        assert False

    assert user_read_model.work_space_id == 1
    assert user_read_model.name == "test user"
    assert user_read_model.email == "test@example.com"
    assert user_read_model.is_admin is False


def test_create_ng_already_exists(session):
    """
    作成 異常 重複
    """
    try:
        data: UserCreateModel = UserCreateModel(
            work_space_id=1, name="test user", email="test1@example.com", password="testtest", is_admin=False
        )
        usecase: UserUseCase = UserUseCase(session)
        _ = usecase.create_user(data)

        assert False

    except AlreadyExistsError:
        assert True


def test_get_all_user_ok(session):
    """
    全件取得 正常
    """
    try:
        usecase: UserUseCase = UserUseCase(session)
        user_read_model_list: list[UserReadModel] = usecase.get_all_user(work_space_id=1)

    except Exception:
        assert False

    assert len(user_read_model_list) == 3
    assert user_read_model_list[0].id == 1
    assert user_read_model_list[1].id == 2
    assert user_read_model_list[2].id == 3


def test_update_ok(session):
    """
    更新 正常
    """
    try:
        data: UserUpdateModel = UserUpdateModel(id=1, name="test user updated", is_admin=False)

        usecase: UserUseCase = UserUseCase(session)
        user_read_model: UserReadModel = usecase.update_user(data=data)

    except Exception:
        assert False

    assert user_read_model.id == 1
    assert user_read_model.name == "test user updated"
    assert user_read_model.is_admin is False


def test_update_ng_not_found(session):
    """
    更新 異常 存在しない
    """
    try:
        data: UserUpdateModel = UserUpdateModel(id=4, name="test user updated", is_admin=False)

        usecase: UserUseCase = UserUseCase(session)
        _ = usecase.update_user(data=data)

        assert False

    except NotFoundError:
        assert True


def test_delete_ok(session):
    """
    削除 正常
    """
    try:
        usecase: UserUseCase = UserUseCase(session)
        usecase.delete_user(id=1)

    except Exception:
        assert False
