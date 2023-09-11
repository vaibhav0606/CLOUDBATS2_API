
from sqlalchemy.orm import Session
from app.models import models_User
from app.schemas import schema_User
from fastapi import HTTPException,status
from app.utils import encryption


def create_user(request:schema_User.addUser,db: Session):
    create=models_User.User(Email=request.Email,Password=encryption.encrypt.hash(request.Password))
    db.add(create)
    db.commit()
    db.refresh(create)
    return create 


def show(id:int,db:Session):
    user = db.query(models_User.User).filter(models_User.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")
    return user