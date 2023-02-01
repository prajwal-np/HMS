from ..repositories_base import BaseRepository
from typing import Union
from schemas.building_schema import BuildingSchema, InsertBuilding, UpdateBuilding
from .building_model import Building
from sqlalchemy import select

class BuildingRepo(BaseRepository):
    
    def add(self, data: InsertBuilding)->BuildingSchema:
        try:
            building = Building(
                createdBy=data.createdBy,
                capacity=data.capacity,
                name=data.name,
                location = data.location,
                single_bed = data.single_bed,
                double_bed = data.double_bed,
                three_bed = data.three_bed,
                four_bed= data.four_bed
                )
            print(self.session)
            self.session.add(building)
            self.session.commit()
            return building.dict()
        except Exception as e:
            print(e)
            raise e
    
    def get(self, id: Union[str, int]):
        stmt = select(Building).where(Building.id.__eq__(id))
        result = self.session.scalar(stmt)
        return result.dict()
    
    def update(self, data: UpdateBuilding):
        build:Building = self.session.query(Building).get(data.id)
        build.update(
            name = data.name,
            location = data.location,
            capacity = data.capacity,
            single_bed = data.single_bed,
            double_bed = data.double_bed,
            three_bed = data.three_bed,
            four_bed = data.four_bed
        )
        self.session.add(build)
        self.session.commit()
        return build.dict()

    def delete(self, id: Union[str, int]):
        self.session.query(Building).where(Building.id.__eq__(id)).delete()
        self.session.commit()
        return 'deleted'