from fastapi import Request
from schemas.transaction_schema import TransactionSchema, InsertTransaction, UpdateTransaction
from sqlalchemy.orm import Session
from data_access.transaction.transaction_repository import TransactionRepo

def insert_transaction(request:Request, transaction:InsertTransaction)->TransactionSchema:
     with request.app.session_maker() as temp_session:
        session:Session = temp_session
        transaction_repo:TransactionRepo = request.app.repositories.transaction_repo(session)
        result = transaction_repo.add(transaction)
        return result

def get_transaction(request:Request, Transaction_id:int)->TransactionSchema:
    with request.app.session_maker() as temp_session:
        session:Session = temp_session
        transaction_repo:TransactionRepo = request.app.repositories.transaction_repo(session)
        return transaction_repo.get(Transaction_id)

def update_transaction(request:Request, data:UpdateTransaction)->TransactionSchema:
    with request.app.session_maker() as temp_session:
        session:Session = temp_session
        transaction_repo:TransactionRepo = request.app.repositories.transaction_repo(session)
        result = transaction_repo.update(data)
        return result

def delete_transaction(request:Request, id:int)->str:
    with request.app.session_maker() as temp_session:
        session:Session = temp_session
        transaction_repo:TransactionRepo = request.app.repositories.transaction_repo(session)
        return transaction_repo.delete(id)