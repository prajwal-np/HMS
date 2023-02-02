from schemas.transaction_schema import TransactionSchema, InsertTransaction, UpdateTransaction
from fastapi import APIRouter, HTTPException, Depends
from starlette import status
from starlette.requests import Request
from utils.middleware import Middleware
from services.transaction import delete_transaction,get_transaction,insert_transaction,update_transaction

router = APIRouter(prefix='/transaction',tags=['Transaction'])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=TransactionSchema)
def create_transaction(request: Request, user: InsertTransaction):
    try:
        result = insert_transaction(request, user)
        return result
    except Exception as error:
        print(error)
        raise HTTPException(status_code=403,detail='Cannot register')

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=TransactionSchema)
def get_transaction_api(request: Request, id: int):
    try:
        result = get_transaction(request, id)
        return result
    except Exception as error:
        print(error)

@router.put("/", status_code=status.HTTP_200_OK, response_model=TransactionSchema)
def update_transaction_api(request: Request, transaction: UpdateTransaction):
    try:
        result = update_transaction(request, transaction)
        return result
    except Exception as error:
        print(error)

@router.delete("/{id}", status_code=status.HTTP_200_OK, response_model=str)
def delete_transaction_api(request: Request, id: str):
    try:
        result = delete_transaction(request, id)
        return result
    except Exception as error:
        print(error)
