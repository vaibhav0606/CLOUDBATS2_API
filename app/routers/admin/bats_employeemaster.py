from fastapi import APIRouter,Depends
from app import database,oauth2,userschema
from app.schemas.admin import schema_employeemaster as schema
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status
from app.datacode.admin import employeemaster as datacode
from typing import List

router=APIRouter(prefix="/empmaster",tags=["Employee Master"])

@router.get('/',response_model=List[schema.show])
def get_all(db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):#current_user: userschema.User = Depends(oauth2.get_current_user)
    return datacode.get_all(db)

@router.get('/{EmployeeCode}',response_model=schema.show)
def get_id(EmployeeCode:int,db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.get_id(EmployeeCode,db)

@router.post('/', response_model=schema.postout)
def create(request: schema.add,db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.create(request,db,current_user)

@router.put('/{EmployeeCode}', response_model=schema.putout)
def update(EmployeeCode:int, request: schema.update, db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.update(EmployeeCode,request, db,current_user)