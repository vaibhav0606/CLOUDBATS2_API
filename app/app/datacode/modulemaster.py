from sqlalchemy.orm import Session
from app.models.models_master import moduleMaster as model 
from app.schemas import schema_moduleMaster as schema
from fastapi import HTTPException,status
from datetime import datetime

def create(request:schema.add,db: Session,current_user):
    Check=db.query(model).filter(model.ModuleName == request.ModuleName)
    if Check.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Module is Already Exists")
    create=model(AddedBy=current_user.LoginCode,**request.model_dump())
    #create=model(ModuleName=request.ModuleName,IndexNum=request.IndexNum,ModuleImage=request.ModuleImage,IsActive=request.IsActive,AddedBy=request.AddedBy)
    db.add(create)
    db.commit()
    db.refresh(create)
    return create 

def update(ModuleCode:int,request:schema.update,db: Session,current_user):
    update_query=db.query(model).filter(model.ModuleCode == ModuleCode)
    if not update_query.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Module  not found")
    Check=db.query(model).filter(model.ModuleName == request.ModuleName,
                                                       model.ModuleCode != ModuleCode)
    if Check.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Module is Already Exists")
    update_data = request.model_dump()
    update_data["ModifiedBy"] = current_user.LoginCode 
    update_data["ModifiedOn"] = datetime.utcnow() 
    update_query.update(update_data, synchronize_session=False)
    db.commit()
    return update_query.first()

def get_id(ModuleCode:int,db:Session):
    user = db.query(model).filter(model.ModuleCode == ModuleCode).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Module  not available")
    return user

def get_all(db:Session):
   
        get_all=db.query(model).all()
        if not get_all:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"data not found")
        return get_all
   
  


