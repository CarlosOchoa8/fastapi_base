"""
Generate an Object of CRUD
"""
from app import schemas
from app.models.user import User
from app.config.database.crud_base import CRUDBase
from sqlalchemy.orm import Session


class CRUDUser(CRUDBase[User, schemas.UserCreateSchema, schemas.UserUpdateSchema]):
    """Item CRUD class

    Args:
        CRUDBase ([Item, ItemCreate, ItemUpdate])
    """
    def get_by_email(self, email: str, db: Session):
        return db.query(self.model).filter(self.model.email == email).first()


user = CRUDUser(User)
