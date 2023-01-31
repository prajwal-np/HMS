import enum
from datetime import datetime 
from sqlalchemy import Column, Integer, DateTime, String, Enum
from sqlalchemy.orm import declarative_base

# from app.config.db import Base


# Usermetadata = Base.metadata
Base = declarative_base()

class RoleEnum(enum.Enum):
        SUPER_ADMIN='Super Admin'
        ADMIN='Admin'
        TENANT='Tenant'

class User(Base):
    __tablename__= 'users'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False, default=datetime.utcnow)
    name = Column(String, nullable=False)
    email= Column(String, nullable=False, unique=True)
    phone= Column(String, nullable=False, unique=True)
    password=Column(String, nullable=False)
    role = Column(Enum(RoleEnum), nullable=False)

    def dict(self):
        return {
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'role': self.role,
        }
    def dict_with_password(self):
        return {
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'password': self.password,
            'role': self.role
        }

