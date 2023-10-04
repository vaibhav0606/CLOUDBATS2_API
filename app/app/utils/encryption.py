from passlib.context import CryptContext


password_cxt=CryptContext(schemes=['bcrypt'],deprecated='auto')

class encrypt():
    def hash(password:str):
        return password_cxt.hash(password)
    
    def verify(hashed_password,plain_password):
        return password_cxt.verify(plain_password,hashed_password)