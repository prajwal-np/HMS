from app.data_access.user.user_model import User
from app.schemas.user_schema import InsertUser
from sqlalchemy import select
from app.utils.crypt import get_password_hash

class UserRepository:
    def __init__(self, session):
        self.session = session
    
    def add(self, user:InsertUser):
        user_res = User(
            email = user.email,
            name = user.name,
            phone= user.phone,
            password= get_password_hash(user.password)
        )
        self.session.add(user_res)
        return user_res.dict()
    def find_one_by_email(self, email: str):
        stmt = select(User).where(User.email.__eq__(email))
        result = self.session.scalars(stmt).one()
        return result