import logging
from sqlalchemy.orm import Session
from app.models.models_master import loginmaster
from app.schemas.admin import schema_loginmaster
from fastapi import HTTPException,status
from app.utils import encryption

logging.basicConfig(filename='app.log', level=logging.ERROR)

def create(request:schema_loginmaster.addLogin,db: Session):
    try:
        create=loginmaster(LoginName=request.LoginName,Password=encryption.encrypt.hash(request.Password),EmployeeCode=request.EmployeeCode,DefaultLocChnlCode=request.DefaultLocChnlCode,RegisteredMobileNo=request.RegisteredMobileNo,MPIN=request.MPIN,TPIN=request.TPIN,IsFinalize=request.IsFinalize,IsActive=request.IsActive,IsAdmin=request.IsAdmin,SuperAdmin=request.SuperAdmin,AddedBy=request.AddedBy)
        db.add(create)
        db.commit()
        db.refresh(create)
        return create 
    except HTTPException as http_exception:
        raise http_exception
    except Exception as e:
        logging.error(f"loginmaster in create: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server Error")

def update(LoginCode:int,request:schema_loginmaster.updatelogin,db: Session):
    try:
        update=db.query(loginmaster).filter(loginmaster.LoginCode == LoginCode)
        if not update.first():
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Login with LoginCode {LoginCode} not found")
        update=update.update(request)
        db.commit()
        db.refresh(update)
        return update.first()
    except HTTPException as http_exception:
        raise http_exception
    except Exception as e:
            logging.error(f"loginmaster in update: {str(e)}")
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server Error")

def get_id(LoginCode:int,db:Session):
    try:
        user = db.query(loginmaster).filter(loginmaster.LoginCode == LoginCode).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Login with the LoginCode {LoginCode} is not available")
        return user
    except HTTPException as http_exception:
        raise http_exception
    except Exception as e:
            logging.error(f"loginmaster in get_id: {str(e)}")
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server Error")

  
def for_login(LoginName:str,token:str,db:Session):
    try:
        user = db.query(loginmaster).filter(loginmaster.LoginName == LoginName).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Login with the LoginCode {LoginName} is not available")
        return user
    except HTTPException as http_exception:
        raise http_exception
    except Exception as e:
        logging.error(f"loginmaster in for_login: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server Error")

def get_all(db:Session):
    try:
        get_all=db.query(loginmaster).all()
        if not get_all:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"data not found")
        return get_all
    except HTTPException as http_exception:
        raise http_exception
    except Exception as e:
        logging.error(f"loginmaster in get_all: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server Error")