from app.service.usecases.auth_usecase import AuthUseCase
from app.service.models.auth_model import SignInModel
from app.service.models.user_model import UserReadModel
from app.service.exceptions import (
    NotFoundError,
    BadRequestError,
)


def test_sign_in_ok(session):
    """
    サインイン 正常
    """
    try:
        data: SignInModel = SignInModel(
            work_space_name="test1.workspace", email="test1@example.com", password="testtest"
        )

        usecase: AuthUseCase = AuthUseCase(session)
        result: UserReadModel = usecase.sign_in(data)

    except Exception:
        assert False

    assert result.id is not None
    assert result.work_space_id == 1
    assert result.name == "test user1"
    assert result.email == "test1@example.com"
    assert result.is_admin


def test_sign_in_ng_not_found(session):
    """
    サインイン 異常 存在しない
    """
    try:
        data: SignInModel = SignInModel(
            work_space_name="test1.workspace", email="test@example.com", password="testtest"
        )

        usecase: AuthUseCase = AuthUseCase(session)
        _ = usecase.sign_in(data)
        assert False

    except NotFoundError:
        assert True
    except Exception:
        assert False


def test_sign_in_ng_bad_request(session):
    """
    サインイン 異常 パスワード不一致
    """
    try:
        data: SignInModel = SignInModel(
            work_space_name="test1.workspace", email="test1@example.com", password="testtesttest"
        )

        usecase: AuthUseCase = AuthUseCase(session)
        _ = usecase.sign_in(data)
        assert False

    except BadRequestError:
        assert True
    except Exception:
        assert False
