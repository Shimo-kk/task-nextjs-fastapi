from app.core.environment import get_env

# CORS関連
ALLOW_ORIGINS: list = get_env().allow_origins
ALLOW_HEADERS: list = get_env().allow_headers

# DB関連
DATABASE_URL: str = get_env().database_url
TEST_DATABASE_URL: str = get_env().test_database_url

# 認証関連
CSRF_KEY: str = get_env().csrf_key
JWT_KEY: str = get_env().jwt_key
JWT_ALGORITHM = "HS256"

# デバッグモード
DEBUG: bool = get_env().debug
