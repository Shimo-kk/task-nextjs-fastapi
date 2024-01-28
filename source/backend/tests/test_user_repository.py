from app.domain.entitys.user_entity import UserEntity, IUserRepository
from app.infrastructure.repositorys.user_repository import UserRepository


def test_insert_ok(session):
    """
    挿入 正常
    """
    try:
        repository: IUserRepository = UserRepository(session)

        new_user_entity: UserEntity = UserEntity.create(
            work_space_id=1, name="test user", email="test@example.com", password="testtest", is_admin=False
        )
        repository.insert(user_entity=new_user_entity)
        session.commit()

        user_entity: UserEntity = repository.find_by_email(work_space_id=1, email=new_user_entity.email)
    except Exception:
        assert False

    assert user_entity.id is not None
    assert user_entity.created_at is not None
    assert user_entity.updated_at is not None
    assert user_entity.work_space_id == 1
    assert user_entity.name == new_user_entity.name
    assert user_entity.email == new_user_entity.email
    assert user_entity.password == new_user_entity.password
    assert user_entity.is_admin is False


def test_find_all_ok(session):
    """
    全件取得 正常
    """
    try:
        repository: IUserRepository = UserRepository(session)
        user_entity_list: list[UserEntity] = repository.find_all(work_space_id=1)
    except Exception:
        assert False

    assert len(user_entity_list) == 3
    assert user_entity_list[0].id == 1
    assert user_entity_list[1].id == 2
    assert user_entity_list[2].id == 3


def test_update_ok(session):
    """
    更新 正常
    """
    try:
        repository: IUserRepository = UserRepository(session)

        user_entity: UserEntity = repository.find_by_id(id=1)
        user_entity.name = "test user updated"
        repository.update(user_entity=user_entity)
        session.commit()

        updated_user_entity: UserEntity = repository.find_by_id(id=1)
    except Exception:
        assert False

    assert updated_user_entity.updated_at > user_entity.updated_at
    assert updated_user_entity.name == "test user updated"
    assert updated_user_entity.email == user_entity.email
    assert updated_user_entity.password == user_entity.password


def test_delete_ok(session):
    """
    削除 正常
    """
    try:
        repository: IUserRepository = UserRepository(session)

        repository.delete_by_id(id=1)
        session.commit()

        user_entity: UserEntity = repository.find_by_id(id=1)
    except Exception:
        assert False

    assert user_entity is None
