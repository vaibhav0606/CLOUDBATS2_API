
from sqlalchemy.orm import Session
from app.models.models_master import EntityMaster as model 
from app.schemas import schema_entitymaster as schema
from fastapi import HTTPException,status
from datetime import datetime


def create(request:schema.add,db: Session,current_user):
    Check=db.query(model).filter(model.EntityName == request.EntityName)
    if Check.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Entity is Already Exists")
    create=model(AddedBy=current_user.LoginCode,**request.model_dump())
    db.add(create)
    db.commit()
    db.refresh(create)
    return create 

def update(EntityCode:int,request:schema.update,db: Session,current_user):
    update_query=db.query(model).filter(model.EntityCode == EntityCode)
    if not update_query.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Entity not found")
    Check=db.query(model).filter(model.EntityName == request.EntityName,
                                                       model.EntityCode != EntityCode)
    if Check.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Entity is Already Exists")
    update_data = request.model_dump()
    update_data["ModifiedBy"] = current_user.LoginCode 
    update_data["ModifiedOn"] = datetime.utcnow() 
    update_query.update(update_data, synchronize_session=False)
    db.commit()
    return update_query.first()

def get_id(EntityCode:int,db:Session):
    data = db.query(model).filter(model.EntityCode == EntityCode).first()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Entity  is not available")
    return data

def get_all(db:Session):
    get_all=db.query(model).all()
    if not get_all:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"data not found")
    return get_all


