from datetime import date
from pydantic import BaseModel


class CreateCustomer(BaseModel):
    Number:int
    customer_id:int
    first_name:str
    last_name:str
    gender:str
    ssn :int
    credit_card:int 
    credit_card_provider:str
    birth_date :date
    start_date:date
    title:str
    office:str
    organization:str 
    salary:float
    bonus:float
    accured_holidays:int 