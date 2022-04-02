from email.quoprimime import header_check
from fastapi import FastAPI
from app.settings import settings

from starlette.middleware.cors import CORSMiddleware

from app.routes import hello_check

app = FastAPI(
    title= settings.PROJECT_NAME,
    version= settings.PROJECT_VERSION
)

if settings.BACKEND_CORS_ORIGIN:
    app.add_middleware(
        CORSMiddleware,
        allow_origins = [str(origin) for origin in settings.BACKEND_CORS_ORIGIN],
        allow_methods = ["*"],
        allow_headers = ["*"]
    )


app.include_router(hello_check.router)
# app.include_router(prefix= settings.API_v1_STR)