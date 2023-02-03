import enum
from datetime import datetime 
from sqlalchemy import Column, DateTime, String, Enum, Integer, Boolean
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.dialects.postgresql import UUID

import uuid
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
    name = Column(String(16), nullable=False)
    email= Column(String(20), nullable=False, unique=True)
    phone= Column(String(10), nullable=False, unique=True)
    password=Column(String(255), nullable=False)
    role = Column(Enum(RoleEnum), nullable=False)
    verifed= Column(Boolean, default=False)
    token= Column(String(500), nullable=True)
    transaction= relationship('Transaction')
    building= relationship('Building',back_populates="user")
    tenant = relationship("Tenant", back_populates="user", uselist=False)

    def dict(self):
        return {
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'role': self.role,
            # 'verifed': self.verifed
        }
    def dict_with_password(self):
        return {
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'password': self.password,
            'role': self.role,
            # 'verfied': self.verifed
        }

