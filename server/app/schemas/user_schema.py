
from pydantic import BaseModel
from data_access.user.user_model import RoleEnum
class UserSchema(BaseModel):
    name: str
    email: str
    role: RoleEnum
    phone: str

class InsertUser(BaseModel):
    name: str
    email: str
    role: RoleEnum
    phone: str
    password: str

class LoggedUser(UserSchema):
    token: str

class LoginUserModel(BaseModel):
    email: str
    password: str