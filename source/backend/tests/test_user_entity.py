from app.domain.entitys.user_entity import UserEntity
from app.domain.exceptions import ValueObjectValidError


def test_create_ok():
    """
    作成 正常
    """
    try:
        new_user_entity: UserEntity = UserEntity.create(
            work_space_id=1, name="test user", email="test@example.com", password="testtest", is_admin=False
        )
    except Exception:
        assert False

    assert new_user_entity.id is None
    assert new_user_entity.created_at is None
    assert new_user_entity.updated_at is None
    assert new_user_entity.work_space_id == 1
    assert new_user_entity.name == "test user"
    assert new_user_entity.email == "test@example.com"
    assert new_user_entity.verify_password("testtest")
    assert new_user_entity.is_admin is False


def test_create_ng_name_min_length():
    """
    作成 異常 ユーザー名が短い
    """
    try:
        _ = UserEntity.create(
            work_space_id=1,
            name="",
            email="test@example.com",
            password="testtest",
            is_admin=False,
        )
        assert False
    except ValueObjectValidError:
        assert True


def test_create_ng_name_max_length():
    """
    作成 異常 ユーザー名が長い
    """
    try:
        _ = UserEntity.create(
            work_space_id=1,
            name="testtesttesttesttesttesttesttesttesttesttesttesttest",
            email="test@example.com",
            password="testtest",
            is_admin=False,
        )
        assert False
    except ValueObjectValidError:
        assert True


def test_create_ng_email_not_valid():
    """
    作成 異常 メールアドレスが不正
    """
    try:
        _ = UserEntity.create(
            work_space_id=1,
            name="test user",
            email="test",
            password="testtest",
            is_admin=False,
        )
        assert False
    except ValueObjectValidError:
        assert True


def test_create_ng_password_min_length():
    """
    作成 異常 パスワードが短い
    """
    try:
        _ = UserEntity.create(
            work_space_id=1,
            name="test user",
            email="test@example.com",
            password="test",
            is_admin=False,
        )
        assert False
    except ValueObjectValidError:
        assert True
