from pydantic.utils import path_type
from sqlalchemy import Integer, String, Float, Date
from sqlalchemy.sql.schema import Column
from database import Base


class Customer(Base):
    __tablename__ = "customers"
    Number = Column(Integer)
    customer_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    ssn = Column(Integer)
    credit_card = Column(Integer)
    credit_card_provider = Column(String)
    birth_date = Column(Date) 
    start_date= Column(Date)
    title= Column(String)
    office= Column(String)
    organization= Column(String)
    salary= Column(Float)
    bonus= Column(Float)
    accured_holidays= Column(Integer)
