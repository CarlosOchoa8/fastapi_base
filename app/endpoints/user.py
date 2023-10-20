from app import schemas
from app import crud
from app import models
from app.helpers.db import get_db
from typing import Any
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session


router = APIRouter()


@router.post("/")
async def create_user(user_in: schemas.UserCreateSchema,
                      db: Session = Depends(get_db)):
    if user := crud.user.get_by_email(db=db, email=user_in.email):
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                             detail=f'Already exists a user with email {user.email}')
    try:
        user_created = (crud.user.create(db=db, obj_in=user_in))
        return schemas.UserResponseSchema(**user_created.__dict__)
    except HTTPException:
        # raise Exception(e) from e
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                             detail='Has been occurred a problem trying create the user.')


@router.put('/{user_id}',
            response_model=schemas.UserResponseSchema)
def update_user(user_id: int,
                user_in: schemas.UserUpdateSchema,
                db: Session = Depends(get_db)):
    if user_obj := crud.user.get(db=db, id=user_id):
        try:
            user_updated = crud.user.update(db=db, obj_in=user_in, db_obj=user_obj)
            return schemas.UserResponseSchema(**user_updated.__dict__)
        except HTTPException:
            return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                 detail='Has been occurred a problem trying create the user.')
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                         detail=f'User {user_id} does not exist.')


@router.get('/',
            response_model=schemas.UserResponseSchema)
def get_users(db: Session = Depends(get_db)):
    try:
        user_objs = crud.user.get_multi(db=db)
        return schemas.UserResponseSchema(**user_objs.__dict__)
    except HTTPException:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail='Has been occurred a problem getting users.')


@router.get('/{user_id}',
            response_model=schemas.UserResponseSchema)
def get_user(user_id: int,
             db: Session = Depends(get_db)) -> dict | Any:
    try:
        user_obj = crud.user.get(db=db, id=user_id)
        return schemas.UserResponseSchema(**user_obj.__dict__)
    except HTTPException:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail='Has been occurred a problem getting user.')


user_router = router
