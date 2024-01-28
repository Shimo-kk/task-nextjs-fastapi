import alembic
import alembic.config
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.infrastructure.middlewares.http_request_middleware_test import TestHttpRequestMiddleware
from app.infrastructure.middlewares.auth_middleware import AuthMiddleware
from app.infrastructure.database.postgresql_test import SQLALCHEMY_DATABASE_URL, engine, get_db_session
from app.infrastructure.dtos import Base
from app.infrastructure.dtos.work_space_dto import WorkSpaceDTO
from app.domain.entitys.work_space_entity import WorkSpaceEntity

test_app = FastAPI()
test_app.add_middleware(AuthMiddleware)
test_app.add_middleware(TestHttpRequestMiddleware)


def create_test_data(session):
    # work_space
    test_work_spaces: list[WorkSpaceDTO] = [
        WorkSpaceDTO.from_entity(WorkSpaceEntity.create(name="test1.workspace")),
        WorkSpaceDTO.from_entity(WorkSpaceEntity.create(name="test2.workspace")),
        WorkSpaceDTO.from_entity(WorkSpaceEntity.create(name="test3.workspace")),
    ]
    session.add_all(test_work_spaces)

    session.commit()
    session.remove()


@pytest.fixture(scope="function")
def session():
    Base.metadata.create_all(bind=engine)

    alembic_cfg = alembic.config.Config("alembic.ini")
    alembic_cfg.set_main_option("sqlalchemy.url", SQLALCHEMY_DATABASE_URL)
    alembic.command.upgrade(alembic_cfg, "head")
    create_test_data(get_db_session())

    session = get_db_session()
    yield session
    session.remove()

    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def client():
    Base.metadata.create_all(bind=engine)

    alembic_cfg = alembic.config.Config("alembic.ini")
    alembic_cfg.set_main_option("sqlalchemy.url", SQLALCHEMY_DATABASE_URL)
    alembic.command.upgrade(alembic_cfg, "head")
    create_test_data(get_db_session())

    client = TestClient(test_app)
    yield client

    Base.metadata.drop_all(bind=engine)
