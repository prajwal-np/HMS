from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://admin:password@localhost:3306/hms_dev"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
session_maker = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()