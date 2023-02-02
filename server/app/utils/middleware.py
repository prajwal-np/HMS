from fastapi import HTTPException, Header, Request
from utils.jwt import decode_token
from datetime import datetime

async def Middleware(x_token: str = Header()):
    decoded_token = decode_token(token= x_token)
    if not decoded_token:
        raise HTTPException(status_code=403, detail="X-Token header invalid")
    if datetime.now().timestamp() > decoded_token['exp']:
        raise HTTPException(status_code=403, detail="X-Token header invalid")