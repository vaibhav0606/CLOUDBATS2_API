from fastapi import Depends
from datetime import datetime, timedelta
from jose import JWTError, jwt
from . import userschema


SECRET_KEY = "09d25e094faa6ca97689768486b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 120


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    return encoded_jwt



def verify_token(token:str,credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        LoginCode: str = payload.get("LoginCode")
        if LoginCode is None:
            raise credentials_exception
        token_data = userschema.TokenData(LoginCode=LoginCode)
    except JWTError:
        raise credentials_exception
    
    return token_data

"""
def verify_tokencheck(token:str,credentials_exception,db:Session):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        LoginName: str = payload.get("sub")
        if LoginName is None:
            raise credentials_exception
        db_token = check_token_in_database(token)
        if not db_token:
            raise credentials_exception
        if token != db_token:
            raise credentials_exception
        token_data = userschema.TokenData(LoginName=LoginName)
    except JWTError:
        raise credentials_exception
    


def check_token_in_database(LoginCode:1,db: Session = Depends(database.Connect_db)):
    return loginmaster.get_id(LoginCode,db)
    
    """