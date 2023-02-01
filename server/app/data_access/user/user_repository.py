from data_access.user.user_model import User, RoleEnum
from schemas.user_schema import InsertUser
from sqlalchemy import select, exc
from sqlalchemy.orm import Session
from utils.crypt import get_password_hash

class UserRepository:
    def __init__(self, session: Session):
        self.session = session
    
    def add(self, user:InsertUser):
        try:
            user_res = User(
                email = user.email,
                name = user.name,
                phone= user.phone,
                role= RoleEnum(user.role).name,
                password= get_password_hash(user.password)
            )
            self.session.add(user_res)
            self.session.commit()
            return user_res.dict()
        except exc.SQLAlchemyError:
            raise exc.SQLAlchemyError

    def find_one_by_email(self, email: str):
        stmt = select(User).where(User.email.__eq__(email))
        result = self.session.scalars(stmt).one()
        return result