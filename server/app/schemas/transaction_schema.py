from pydantic import BaseModel
from typing import Optional

class TransactionSchema(BaseModel):
    id: Optional[int]
    user: int
    building: int
    remark: str
    image: str
    amount:str
    month: str
    payment_method: str
    type: str

class InsertTransaction(TransactionSchema):
    pass

class UpdateTransaction(InsertTransaction):
    id: int