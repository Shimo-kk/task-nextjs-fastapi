import os
from functools import lru_cache
from pydantic import BaseSettings

ENV_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Environment(BaseSettings):
    """
    環境変数クラス

    Attributes:
        allow_origins: 許可するオリジン
        allow_headers: 許可するヘッダー
        database_url: データベースのURL
        test_database_url: データベースのURL(テスト用)
        csrf_key: CSRFキー
        jwt_key: JWTキー
        debug: デバッグフラグ
    """

    allow_origins: list
    allow_headers: list

    database_url: str
    test_database_url: str

    csrf_key: str
    jwt_key: str

    debug: bool

    class Config:
        env_file = os.path.join(ENV_DIR, ".env")


@lru_cache
def get_env():
    """@lru_cacheで.envの結果をキャッシュする"""
    return Environment()
