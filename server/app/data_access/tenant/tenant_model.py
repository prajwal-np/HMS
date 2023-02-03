from datetime import datetime 
from sqlalchemy import Column, Integer, DateTime, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from schemas.tenant_schema import UpdateTenant
from ..user.user_model import User

# from sqlalchemy.dialects.postgresql import UUID
# import uuid


Base = declarative_base()


class Tenant(Base):
    __tablename__= 'tenant'

    # id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.UUID)
    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False, default=datetime.utcnow)
    building = Column(Integer, nullable=False)
    room_type = Column(String(50), nullable=False)
    current_status = Column(String(50), nullable=False)
    user_id = Column(Integer,ForeignKey(User.id), nullable=False)
    user = relationship("User", back_populates="tenant")

    def dict(self):
        return {
            'id': self.id,
            'building': self.building,
            'room_type': self.room_type,
            'current_status': self.current_status,
            'user': self.user,
        }
    
    def update(self, data: UpdateTenant):
        self.building= data.building
        self.room_type= data.room_type
        self.current_status= data.current_status
        self.user= data.user


    

