from app.endpoints import user_router
from fastapi import APIRouter


api_router = APIRouter()

api_router.include_router(
    router=user_router,
    prefix='/users',
    tags=['users'],
    responses={418: {'description': 'I"m a teapot =)'}}
)

