
from sqlalchemy.orm import Session
from app.models.models_master import loginmaster
from app.schemas import schema_loginmaster
from fastapi import HTTPException,status
from app.utils import encryption


def create(request:schema_loginmaster.addLogin,db: Session):
    create=loginmaster(LoginName=request.LoginName,Password=encryption.encrypt.hash(request.Password),EmployeeCode=request.EmployeeCode,DefaultLocChnlCode=request.DefaultLocChnlCode,RegisteredMobileNo=request.RegisteredMobileNo,MPIN=request.MPIN,TPIN=request.TPIN,IsFinalize=request.IsFinalize,IsActive=request.IsActive,IsAdmin=request.IsAdmin,SuperAdmin=request.SuperAdmin,AddedBy=request.AddedBy)
    db.add(create)
    db.commit()
    db.refresh(create)
    return create 

def update(LoginCode:int,request:schema_loginmaster.updatelogin,db: Session):
    update=db.query(loginmaster).filter(loginmaster.LoginCode == LoginCode)
    if not update.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Login with LoginCode {LoginCode} not found")
    update=update.update(request)
    db.commit()
    db.refresh(update)
    return 'updated'

def get_id(LoginCode:int,db:Session):
    user = db.query(loginmaster).filter(loginmaster.LoginCode == LoginCode).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Login with the LoginCode {LoginCode} is not available")
    return user

  
def for_login(LoginName:str,token:str,db:Session):
    user = db.query(loginmaster).filter(loginmaster.LoginName == LoginName).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Login with the LoginCode {LoginName} is not available")
    return user

def get_all(db:Session):
    get_all=db.query(loginmaster).all()
    if not get_all:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"data not found")
    return get_all