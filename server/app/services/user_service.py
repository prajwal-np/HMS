from starlette.requests import Request
from schemas.user_schema import UserSchema, InsertUser, RegisterUser
from utils.crypt import verify_password
from utils.jwt import generate_token
from data_access.user.user_repository import UserRepository, RoleEnum
from sqlalchemy.orm import Session
from utils.jwt import decode_token

def register_user(request:Request, user: InsertUser)-> UserSchema:
    with request.app.session_maker() as temp_session:
        session:Session = temp_session
        user_repo: UserRepository = request.app.repositories.user_repo(session)
        user = user_repo.add(
           user
        )
        session.commit()
        return user

def authenticate_user(request:Request, email: str, password:str):
    with request.app.session_maker() as temp_session:
        session:Session = temp_session
        user_repo:UserRepository = request.app.repositories.user_repo(session)
        user:UserSchema = user_repo.find_one_by_email(email).dict_with_password()
        if not user:
            return False
        if not verify_password(password, user['password']):
            return False
        token = generate_token({'email': user['email'], 'role': RoleEnum(user['role']).value})
        del user['password']
        tempUser = user.copy()
        tempUser.update({"token": token})
        return tempUser

def get_user_by_email(request:Request, email: str)->UserSchema:
    with request.app.session_maker() as temp_session:
        session:Session = temp_session
        user_repo = request.app.repositories.user_repo(session)
        user:UserSchema = user_repo.find_one_by_email(email).dict()
        return user

def on_board(request:Request, user:RegisterUser):
    decoded = decode_token(request.headers['x-token'])
    if decoded['role'] =='Super Admin':
        print('Super admin')
    if decoded['role'] =='Admin':
        print('admin')
    return