from fastapi import APIRouter
from app.settings import settings

router = APIRouter()

@router.get("/")
def hello_check():
    return {
        "project":settings.PROJECT_NAME,
        "version": settings.PROJECT_VERSION
    }