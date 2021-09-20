from datetime import date
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from schemas import CreateCustomer
from database import get_db
from models import Customer
import uvicorn
from fastapi.responses import JSONResponse


app = FastAPI()

@app.post("/")
def create(details: CreateCustomer, db: Session = Depends(get_db)):
    to_create = Customer(
        Number = details.Number,
        customer_id = details.customer_id,
        first_name=details.first_name,
        last_name=details.last_name,
        gender = details.gender,
        ssn = details.ssn,
        credit_card = details.credit_card,
        credit_card_provider = details.credit_card_provider,
        birth_date = details.birth_date,
        start_date= details.start_date,
        title= details.title,
        office= details.office,
        organization= details.organization,
        salary= details.salary,
        bonus= details.bonus,
        accured_holidays= details.accured_holidays
        
    )
    db.add(to_create)
    db.commit()
    return { 
        "success": "uspesno"
    }



@app.put("/")
def update(id: int,details: CreateCustomer ,db:Session = Depends(get_db)):
    item_to_update = db.query(Customer).filter(Customer.customer_id == id).first()
    item_to_update.first_name = details.first_name
    item_to_update.last_name=details.last_name
    item_to_update.gender = details.gender
    item_to_update.ssn=details.ssn
    item_to_update.credit_card = details.credit_card
    item_to_update.credit_card_provider=details.credit_card_provider
    item_to_update.birth_date = details.birth_date
    item_to_update.start_date=details.start_date
    item_to_update.title = details.title
    item_to_update.office=details.office
    item_to_update.organization = details.organization
    item_to_update.salary=details.salary
    item_to_update.bonus = details.bonus
    item_to_update.accured_holidays=details.accured_holidays

    db.commit()

    return item_to_update


@app.get("/")
def get_by_id(id: int, db: Session = Depends(get_db)):
    return db.query(Customer).filter(Customer.customer_id == id).first()

@app.delete("/")
def delete(id: int, db: Session = Depends(get_db)):
    db.query(Customer).filter(Customer.customer_id == id).delete()
    db.commit()
    return { "success": True }

if __name__ == "__main__":
    uvicorn.run(app, port=8080, log_level="info")