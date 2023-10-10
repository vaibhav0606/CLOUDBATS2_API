from fastapi import APIRouter,Depends
from app import database,oauth2,userschema
from app.schemas.programing import schema_suppliermastertable as schema
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends
from app.datacode.programing import suppliermastertable as datacode
from typing import List

router=APIRouter(prefix="/suppliermastertable",tags=["Supplier Master"])

@router.get('/',response_model=List[schema.show])
def get_all(db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):#current_user: userschema.User = Depends(oauth2.get_current_user)
    return datacode.get_all(db)

@router.get('/{SupplierCode}',response_model=schema.show)
def get_id(SupplierCode:int,db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.get_id(SupplierCode,db)

@router.post('/', response_model=schema.postout)
def create(request: schema.add,db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.create(request,db,current_user)

@router.put('/{SupplierCode}',  response_model=schema.putout)
def update(SupplierCode:int, request: schema.update, db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.update(SupplierCode,request, db,current_user)


@router.get('/drop/',response_model=List[schema.loaddropdown])
def get_drop(db: Session = Depends(database.Connect_db),current_user: userschema.User = Depends(oauth2.get_current_user)):
    return datacode.get_drop(db)