from fastapi import APIRouter,HTTPException,Response,status,Depends
from .. import database,oauth2,userschema
from app.schemas import schema_subgenreMaster
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status
from app.datacode import subgenremaster
from typing import List

router=APIRouter(prefix="/subgenremaster",tags=["Sub Genre Master"])

@router.get('/',response_model=List[schema_subgenreMaster.show])
def get_all(db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):#current_user: userschema.User = Depends(oauth2.get_current_user)
    return subgenremaster.get_all(db)

@router.get('/{SubGenreCode}',response_model=schema_subgenreMaster.show)
def get_id(SubGenreCode:int,db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return subgenremaster.get_id(SubGenreCode,db)

@router.post('/', response_model=schema_subgenreMaster.postout)
def create(request: schema_subgenreMaster.add,db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return subgenremaster.create(request,db,current_user)

@router.put('/{SubGenreCode}', response_model=schema_subgenreMaster.putout)
def update(SubGenreCode:int, request: schema_subgenreMaster.update, db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return subgenremaster.update(SubGenreCode,request, db,current_user)