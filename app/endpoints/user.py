from app import schemas
from app import crud
from app import models
from app.helpers.db import get_db
from typing import Any
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session


router = APIRouter()


@router.post("/")
def create_user(*,
                db: Session = Depends(get_db),
                user_in: schemas.UserCreateSchema):
    if user := crud.user.get_by_email(db=db, email=user_in.email):
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                             detail=f'Ya se encuentra registrado el correo {user_in.email}')
    try:
        return crud.user.create(db=db, obj_in=user_in)
    except Exception:
        # raise Exception(e) from e
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                             detail='Ha ocurrido un error al intentar creal el usuario.')
#
#
# @router.put('/{user_id}')
# def update_user(db: Session,
#                 user_id: int,
#                 user_in: schemas.UserUpdateSchema):
#     if user := crud.user.get(db=db, id=user_id):
#         user_updated = crud.user.update(db=db, obj_in=user_in, db_obj=user)
#
#
# @router.get('/')
# def get_users(db: Session = Depends(get_db)):
#     try:
#         return crud.user.get_multi(db=db)
#     except HTTPException as exception:
#         return exception


# @router.get('/{user_id}', response_model=None)
# def get_user(db: Session,
#              user_id: int) -> dict | Any:
#     if user := crud.user.get(db=db, id=user_id):
#         return user
#     return HTTPException(status_code=status.HTTP_403_FORBIDDEN,
#                          detail='Usuario no encontrado')


user_router = router
