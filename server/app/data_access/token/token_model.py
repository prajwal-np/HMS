
from datetime import datetime 
from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.orm import declarative_base
# from schemas.token_schema import UpdateToken
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID

import uuid



Base = declarative_base()


class Token(Base):
    __tablename__= 'token'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False, default=datetime.utcnow)
    name = Column(Integer, nullable=False,)
    email= Column(String(50), nullable=False)
    token=Column(String(255), nullable=False)
    type=Column(String(500), nullable=False)

    def dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'token': self.token,
            'type': self.type
        }
    # def update(self, data:UpdateToken):
    #         self.building= data.building,
    #         self.lunch_time= data.lunch_time
    #         self.break_fast_time= data.break_fast_time,
    #         self.snack_time= data.snack_time,
    #         self.dinner_time= data.dinner_time,

