from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from app.core import DEBUG, DATABASE_URL

SQLALCHEMY_DATABASE_URL: str = DATABASE_URL

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=DEBUG,
    encoding="utf-8",
    # pool_size=,
    # max_overflow=
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db_session() -> scoped_session:
    """DBのセッション取得

    Returns:
            scoped_session: DBセッション
    """
    return scoped_session(SessionLocal)
