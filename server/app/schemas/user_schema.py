
from pydantic import BaseModel
from typing import Optional
from data_access.user.user_model import RoleEnum
class UserSchema(BaseModel):
    name: str
    email: str
    role: RoleEnum
    phone: str
    password: Optional[str]
    # verifed: bool

class InsertUser(UserSchema):
    pass

class RegisterUser(BaseModel):
    name: str
    email: str
    role: RoleEnum
    phone: str

class LoggedUser(UserSchema):
    token: str

class LoginUserModel(BaseModel):
    email: str
    password: str