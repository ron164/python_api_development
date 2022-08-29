# -*- coding: utf-8 -*-
# @Time : 27-08-2022 10:37
# @Author : rohan
# @File : database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings


SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency
# connection to the database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# For reference when Raw SQL is to be used
# while True:

#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres',
#                                 password='password123', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was succesfull!")
#         break
#     except Exception as error:
#         print("Connecting to database failed")
#         print("Error: ", error)
#         time.sleep(2)
