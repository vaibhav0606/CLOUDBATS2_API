
from sqlalchemy.orm import Session
from app.models.models_master import DepartmentMaster as model 
from app.schemas import schema_departmentMaster as schema
from fastapi import HTTPException,status
from datetime import datetime

def create(request:schema.add,db: Session,current_user):
    Check=db.query(model).filter(model.DepartmentName == request.DepartmentName)
    if Check.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Department Name is Already Exists")
    create=model(AddedBy=current_user.LoginCode,**request.dict())
    db.add(create)
    db.commit()
    db.refresh(create)
    return create 

def update(DepartmentCode:int,request:schema.update,db: Session,current_user):
    update_query=db.query(model).filter(model.DepartmentCode == DepartmentCode)
    if not update_query.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Department not found")
    Check=db.query(model).filter(model.DepartmentName == request.DepartmentName,
                                                       model.DepartmentCode != DepartmentCode)
    if Check.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Department is Already Exists")
    update_data = request.dict()
    update_data["ModifiedBy"] = current_user.LoginCode 
    update_data["ModifiedOn"] = datetime.utcnow() 
    update_query.update(update_data, synchronize_session=False)
    db.commit()
    return update_query.first()

def get_id(DepartmentCode:int,db:Session):
    user = db.query(model).filter(model.DepartmentCode == DepartmentCode).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Department not available")
    return user

def get_all(db:Session):

    # Code to create a show instance
        get_all=db.query(model).all()
        if not get_all:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"data not found")
        return get_all

  


