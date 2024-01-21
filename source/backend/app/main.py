from fastapi import FastAPI

from app.infrastructure.middlewares.cors_middleware import CORSMiddleware
from app.infrastructure.middlewares.http_request_middleware import HttpRequestMiddleware
from app.infrastructure.middlewares.auth_middleware import AuthMiddleware

app = FastAPI()


# ミドルウェアの追加
app.add_middleware(AuthMiddleware)
app.add_middleware(HttpRequestMiddleware)
app.add_middleware(CORSMiddleware)


@app.get("/")
async def root():
    return {"message": "Hello World"}
