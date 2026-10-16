from pydantic import BaseModel, field_validator, model_validator
from datetime import datetime

class Person(BaseModel):
    first_name:str
    last_name:str

    @field_validator('first_name','last_name')
    def names_must_be_capitalize(cls, value:str):
        if not value.istitle():
            return ValueError("Name must be capitalized")
        return value


class User(BaseModel):

    email :str

    @field_validator('email')
    def normalize_email(cls, value:str):
        return value.lower().strip()



class Product(BaseModel):
    price:str # $4.44

    @field_validator("price", mode="before")
    def parse_price(cls, value):
        if isinstance(value, str):
            return float(value.replace('$','').replace(",",''))
        return value    


class DateRange(BaseModel):

    start_date : datetime
    end_date:datetime

    @model_validator(mode='after')
    def validate_date_range(cls, value):
        if value.start_date >= value.end_date:
            raise ValueError("end_date must be after start_date")
        return value

    


