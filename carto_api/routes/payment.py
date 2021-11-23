from fastapi import APIRouter
from fastapi import HTTPException
from typing import Optional
from lib.payment import Payment
from typing import List
from datetime import date

router = APIRouter()
payment = Payment()

#Get total payment amount in date range (default data range is the total)
#Can select postal code to get payment
@router.get("/payment/total",)
async def get_total(date_init: Optional[date]='2015-01-01', date_final: Optional[date]='2015-12-01', postal_code: Optional[int]= None):

    return payment.get_total_payment(date_init, date_final, postal_code)


#Get total payment amount for each postal code in date range (default data range is the total)
@router.get("/payment/total/postal-codes",)
async def get_total_by_postal_code(date_init: Optional[date]='2015-01-01', date_final: Optional[date]='2015-12-01'):

    return payment.get_payment_by_postal_code(date_init, date_final)

#Get total payment amount for gender and age in date range (default data range is the total)
#Can select postal code to get payment
@router.get("/payment/{gender}/{age}",)
async def get_age_gender(gender:str, age:str, postal_code: Optional[int]= None ,date_init: Optional[date]='2015-01-01', date_final: Optional[date]='2015-12-01'):
    accepted_age = ["<=24", "25-34", "35-44", "45-54", "55-64", ">=65"]
    accepted_gender= ["F", "M"]
    if age not in accepted_age or gender not in accepted_gender:
        raise HTTPException(status_code=400, detail="Incorrect format of gender or age")
    return payment.get_age_gender_payment(date_init, date_final, gender, age, postal_code)



