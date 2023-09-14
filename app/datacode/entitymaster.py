
from sqlalchemy.orm import Session
from app.models import models_master
from app.schemas import schema_entitymaster
from fastapi import HTTPException,status
from app.utils import encryption


def create(request:schema_entitymaster.addentity,db: Session):
    create=models_master.EntityMaster(EntityId=request.EntityId,EntityName=request.EntityName,PermAddress=request.PermAddress,CorpAddress=request.CorpAddress,ContactPerson=request.ContactPerson,Contact=request.Contact,IsActive=request.IsActive,AddedBy=request.AddedBy,PANNO=request.PANNO,CINNumber=request.CINNumber)
    db.add(create)
    db.commit()
    db.refresh(create)
    return create 

def update(EntityCode:int,request:schema_entitymaster.updateentity,db: Session):
    update=db.query(models_master.EntityMaster).filter(models_master.EntityMaster.EntityCode == EntityCode)
    if not update.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Entity with EntityCode {EntityCode} not found")
    update=update.update(request)
    db.commit()
    db.refresh(update)
    return 'updated'

def get_id(EntityCode:int,db:Session):
    data = db.query(models_master.EntityMaster).filter(models_master.EntityMaster.EntityCode == EntityCode).first()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Entity with the EntityCode {EntityCode} is not available")
    return data

def get_all(db:Session):
    get_all=db.query(models_master.EntityMaster).all()
    if not get_all:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"data not found")
    return get_all


