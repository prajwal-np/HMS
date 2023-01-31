from starlette.requests import Request
from app.schemas.user_schema import UserSchema, InsertUser
from app.utils.crypt import verify_password
from app.utils.jwt import generate_token

def register_user(request:Request, user: InsertUser)-> UserSchema:
      with request.app.session_maker() as session:
        user_repo = request.app.repositories.user_repo(session)
        user = user_repo.add(
           user
        )
        session.commit()
        return user

def authenticate_user(request:Request, email: str, password:str):
    with request.app.session_maker() as session:
        user_repo = request.app.repositories.user_repo(session)
        user:UserSchema = user_repo.find_one_by_email(email).dict_with_password()
        if not user:
            return False
        if not verify_password(password, user['password']):
            return False
        token = generate_token({email: user['email']})
        del user['password']
        tempUser = user.copy()
        tempUser.update({"token": token})
        return tempUser