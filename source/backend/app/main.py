from fastapi import FastAPI

from app.infrastructure.middlewares.cors_middleware import CORSMiddleware
from app.infrastructure.middlewares.http_request_middleware import HttpRequestMiddleware
from app.infrastructure.middlewares.auth_middleware import AuthMiddleware

from app.presentation.routers import api_router
from app.presentation.routers.v1 import api_v1_router

app = FastAPI()


# ミドルウェアの追加
app.add_middleware(AuthMiddleware)
app.add_middleware(HttpRequestMiddleware)
app.add_middleware(CORSMiddleware)

# ルーターの追加
app.include_router(api_router, prefix="/api")
app.include_router(api_v1_router, prefix="/api/v1")


@app.get("/")
async def root():
    return {"message": "Hello World"}
