from datetime import datetime 
from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.orm import declarative_base
# from sqlalchemy.dialects.postgresql import UUID
# import uuid


Base = declarative_base()


class Building(Base):
    __tablename__= 'building'

    # id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.UUID)
    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False, default=datetime.utcnow)
    createdBy = Column(Integer, nullable=False, default=datetime.utcnow)
    name = Column(String, nullable=False)
    location= Column(String, nullable=False)
    capacity=Column(Integer,nullable=False)
    single_bed=Column(Integer,nullable=True)
    double_bed=Column(Integer,nullable=True)
    three_bed=Column(Integer,nullable=True)
    four_bed=Column(Integer,nullable=True)    

    def dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location,
            'capacity': self.capacity,
            'single_bed': self.single_bed,
            'double_bed': self.double_bed,
            'three_bed': self.three_bed,
            'four_bed': self.four_bed,
            'createdBy': self.createdBy
        }
    def update(self, name: str, location: str, capacity: int, single_bed: int,double_bed: int, three_bed:int, four_bed: int,  **kwargs):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.single_bed = single_bed
        self.double_bed = double_bed
        self.three_bed = three_bed
        self.four_bed = four_bed

