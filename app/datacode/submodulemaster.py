
from sqlalchemy.orm import Session
from app.models.models_master import SubModuleMaster as model
from app.schemas import schema_subModuleMaster as schema
from fastapi import HTTPException,status
from datetime import datetime


def create(request:schema.add,db: Session,current_user):
    Check=db.query(model).filter(model.SubModuleName == request.SubModuleName)
    if Check.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"SubModule is Already Exists")
    create=model(AddedBy=current_user.LoginCode,**request.model_dump())
    #create=model(SubModuleName=request.SubModuleName,ModuleCode=request.ModuleCode,IndexNum=request.IndexNum,SubModuleImage=request.SubModuleImage,IsActive=request.IsActive,AddedBy=request.AddedBy)
    db.add(create)
    db.commit()
    db.refresh(create)
    return create 

def update(SubModuleCode:int,request:schema.update,db: Session,current_user):
    update_query=db.query(model).filter(model.SubModuleCode == SubModuleCode)
    if not update_query.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"SubModule not found")
    Check=db.query(model).filter(model.SubModuleName == request.SubModuleName,
                                                       model.SubModuleCode != SubModuleCode)
    if Check.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"SubModule is Already Exists")
    update_data = request.model_dump()
    update_data["ModifiedBy"] = current_user.LoginCode 
    update_data["ModifiedOn"] = datetime.utcnow() 
    update_query.update(update_data, synchronize_session=False)
    db.commit()
    return update_query.first()

def get_id(SubModuleCode:int,db:Session):
    user = db.query(model).filter(model.SubModuleCode == SubModuleCode).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"SubModule not available")
    return user

def get_all(db:Session):
    get_all=db.query(model).all()
    if not get_all:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"data not found")
    return get_all



