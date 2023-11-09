from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DB_CONNECTION_STRING

Base = declarative_base()
engine = create_engine(DB_CONNECTION_STRING)
Session = sessionmaker(bind=engine)

class Validator(Base):
    __tablename__ = 'validators'

    id = Column(Integer, primary_key=True)
    chat_id = Column(Integer, nullable=False)
    validator_address = Column(String, nullable=False)
    alias = Column(String, nullable=False)
