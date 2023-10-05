from pydantic import BaseModel



class showUser(BaseModel):
    Email : str
    class Config:
        orm_mode=True
     
class addUser(BaseModel):
    Email:str
    Password:str
    #Object_Status:str
    #Person_Id:str
    #RememberMe:str
    #Role_Id:str
    #System:int
    #status:int
    