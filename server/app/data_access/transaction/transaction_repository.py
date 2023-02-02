from ..repositories_base import BaseRepository
from .transaction_model import Transaction
from typing import Union
from schemas.transaction_schema import InsertTransaction, TransactionSchema, UpdateTransaction

class TransactionRepo(BaseRepository):

    def add(self, data: InsertTransaction)->TransactionSchema:
        try:
            transaction = Transaction(
                 user= data.user,
                 building= data.building,
                 type= data.type,
                 amount= data.amount,
                 payment_method= data.payment_method,
                 image= data.image,
                 remark = data.remark,
                 month = data.month
            )
            return super().add(transaction)
        except Exception as e:
            print(e)
            raise e
    
    def get(self, id: Union[str, int]):
        return super().get(Transaction,id)
    
    def update(self, data: UpdateTransaction)->TransactionSchema:
        transaction:Transaction = self.session.query(Transaction).get(data.id)
        transaction.update(data)
        result = super().add(transaction)
        return result

    def delete(self, id: Union[str, int]):
        return super().delete(Transaction, id)