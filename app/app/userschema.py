from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
    name:str
    email:str
    password:str
    
class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    LoginCode: Optional[int] = None
    
