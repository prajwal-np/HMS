
from pydantic import BaseModel

class UserSchema(BaseModel):
    name: str
    email: str
    # role: str
    phone: str

class InsertUser(BaseModel):
    name: str
    email: str
    role: str
    phone: str
    password: str

class LoginUserModel(BaseModel):
    email: str
    password: str