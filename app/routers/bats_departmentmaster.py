from fastapi import APIRouter,Depends
from .. import database,oauth2,userschema
from app.schemas import schema_departmentMaster as schema
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends
from app.datacode import departmentmaster as datacode
from typing import List

router=APIRouter(prefix="/departmentmaster",tags=["Department Master"])

@router.get('/',response_model=List[schema.show])
def get_all(db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):#current_user: userschema.User = Depends(oauth2.get_current_user)
    return datacode.get_all(db)

@router.get('/{DepartmentCode}',response_model=schema.show)
def get_id(DepartmentCode:int,db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.get_id(DepartmentCode,db)

@router.post('/', response_model=schema.postout)
def create(request: schema.add,db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.create(request,db,current_user)

@router.put('/{DepartmentCode}',response_model=schema.putout)
def update(DepartmentCode:int, request: schema.update, db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.update(DepartmentCode,request, db,current_user)