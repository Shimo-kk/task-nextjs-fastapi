import alembic
import alembic.config
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.infrastructure.database.postgresql_test import SQLALCHEMY_DATABASE_URL, engine, get_db_session
from app.infrastructure.dtos import Base

test_app = FastAPI()


def create_test_data(session):
    pass


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
