from sqlalchemy import create_engine, Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Session

DATABASE= 'mysql+mysqlconnector://root:@localhost/python_orm'

# tao engine
engine= create_engine(DATABASE, echo=True)

# khoi tao base cho cac orm
Base = declarative_base()

# tao session de tuong tac voi data
session= sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()