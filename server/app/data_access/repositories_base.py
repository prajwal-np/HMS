from sqlalchemy.orm import Session
from typing import Union
from sqlalchemy import select

class BaseRepository:
    def __init__(self, session: Session):
        self.session = session
    
    def add(self,data):
        self.session.add(data)
        self.session.commit()
        return data.dict()
    
    def get(self,model, id: Union[str, int]):
            stmt = select(model).where(model.id.__eq__(id))
            result = self.session.scalar(stmt)
            return result.dict()
    
    def delete(self,model, id: Union[str, int]):
        self.session.query(model).where(model.id.__eq__(id)).delete()
        self.session.commit()
        return 'deleted'