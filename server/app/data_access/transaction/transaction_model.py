from datetime import datetime 
from sqlalchemy import Column, Integer, DateTime, String, ForeignKey
from sqlalchemy.orm import declarative_base
from ..user.user_model import User
from ..building.building_model import Building

# from sqlalchemy.dialects.postgresql import UUID
# import uuid


Base = declarative_base()


class Transaction(Base):
    __tablename__= 'transaction'

    # id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.UUID)
    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False, default=datetime.utcnow)
    user = Column(Integer, ForeignKey(User.id), nullable=False)
    building = Column(Integer,ForeignKey(Building.id), nullable=False)
    type = Column(String(50), nullable=False)
    amount= Column(String(50), nullable=False)
    image=Column(String(50), nullable=False)
    remark=Column(String(50), nullable=False)
    month=Column(String(50), nullable=False)
    payment_method= Column(String(50), nullable=False)

    def dict(self):
        return {
            'id': self.id,
            'user': self.user,
            'building': self.building,
            'type': self.type,
            'amount': self.amount,
            'image': self.image,
            'remark': self.remark,
            'month': self.month,
            'payment_method': self.payment_method
        }
    def update(self,data):
        self.user = data.user
        self.building = data.building
        self.type = data.type
        self.amount = data.amount
        self.image = data.image
        self.remark = data.remark
        self.month = data.month
        self.payment_method = data.payment_method


