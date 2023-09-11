from fastapi import APIRouter,HTTPException,Response,status,Depends
from .. import database 
from app.schemas import schema_User
from app.models import models_User
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status
from app.datacode import user
from app.utils import encryption
from typing import List
router=APIRouter(prefix="/user",tags=["User"])

@router.get('/',response_model=List[schema_User.showUser],status_code=status.HTTP_200_OK)
def get_all_user(db:Session=Depends(database.Connect_db)):
    get_all=db.query(models_User.User).all()
    if not get_all:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"data not found")
    return get_all


@router.post('/', response_model=schema_User.addUser)
def create_user(request: schema_User.addUser,db: Session = Depends(database.Connect_db)):
    return user.create_user(request,db)


@router.get('/{id}',response_model=schema_User.showUser)
def get_user_by_id(id:int,db: Session = Depends(database.Connect_db)):
    return user.show(id,db)
