
from sqlalchemy.orm import Session
from app.models.models_master import GenreMaster as model
from app.schemas import schema_genremaster as schema
from fastapi import HTTPException,status
from datetime import datetime

def create(request:schema.add,db: Session,current_user):
    Check=db.query(model).filter(model.GenreName == request.GenreName)
    if Check.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"GenreName is Already Exists")
    create=model(AddedBy=current_user.LoginCode,**request.model_dump())

    db.add(create)
    db.commit()
    db.refresh(create)
    return create 

def update(GenreCode:int,request:schema.update,db: Session,current_user):
    update_query=db.query(model).filter(model.GenreCode == GenreCode)
    if not update_query.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"GenreName  not found")
    Check=db.query(model).filter(model.GenreName == request.GenreName,
                                                       model.GenreCode != GenreCode)
    if Check.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"GenreName is Already Exists")
    update_data = request.model_dump()
    update_data["ModifiedBy"] = current_user.LoginCode 
    update_data["ModifiedOn"] = datetime.utcnow() 
    update_query.update(update_data, synchronize_session=False)
    db.commit()
    return update_query.first()

def get_id(GenreCode:int,db:Session):
    user = db.query(model).filter(model.GenreCode == GenreCode).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"GenreName not available")
    return user

def get_all(db:Session):
    get_all=db.query(model).all()
    if not get_all:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"data not found")
    return get_all

