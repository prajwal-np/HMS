from datetime import datetime 
from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.orm import declarative_base
# from sqlalchemy.dialects.postgresql import UUID
# import uuid


Base = declarative_base()


class Transaction(Base):
    __tablename__= 'transaction'

    # id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.UUID)
    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False, default=datetime.utcnow)
    user = Column(Integer, nullable=False)
    building = Column(Integer, nullable=False)
    type = Column(String, nullable=False)
    amount= Column(String, nullable=False)
    image=Column(String, nullable=False)
    remark=Column(String, nullable=False)
    month=Column(String, nullable=False)
    payment_method= Column(String, nullable=False)

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


