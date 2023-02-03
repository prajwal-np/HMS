from datetime import datetime 
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base
from schemas.food_routine_schema import UpdateFoodRoutine
from datetime import datetime
from ..building.building_model import Building

# from sqlalchemy.dialects.postgresql import UUID

# import uuid



Base = declarative_base()


class FoodRoutine(Base):
    __tablename__= 'food_routine'

    # id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.UUID)
    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False, default=datetime.utcnow)
    building = Column(Integer,ForeignKey(Building.id), nullable=False, default=datetime.utcnow)
    lunch_time= Column(DateTime, nullable=True)
    break_fast_time= Column(DateTime, nullable=True) 
    snack_time= Column(DateTime, nullable=True) 
    dinner_time= Column(DateTime, nullable=True)

    def dict(self):
        return {
            'id': self.id,
            'building': self.building,
            'lunch_time': self.lunch_time,
            'break_fast_time': self.break_fast_time,
            'snack_time': self.snack_time,
            'dinner_time': self.dinner_time,
        }
    def update(self, data:UpdateFoodRoutine):
            self.building= data.building,
            self.lunch_time= data.lunch_time
            self.break_fast_time= data.break_fast_time,
            self.snack_time= data.snack_time,
            self.dinner_time= data.dinner_time,

