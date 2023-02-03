from jose import JWTError, jwt
from datetime import datetime, timedelta
SECRET_KEY = "deff1952d59f883ece260e8683fed21ab0ad9a53323eca4f"
ALGORITHM = "HS256"
EXPIRY_MINUTES= 60

def decode_token(token: str):
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

def generate_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=EXPIRY_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode,SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt