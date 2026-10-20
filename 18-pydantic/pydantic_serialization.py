from pydantic import BaseModel,ConfigDict
from typing import List,Optional
from datetime import datetime


class Address(BaseModel):
    street: str
    city: str
    zip_code: str


class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    created_at : datetime
    address : Address
    tags: Optional[List[str]] = []

    model_config = ConfigDict(
        json_encoders = {
            datetime: lambda value : value.strftime('%d-%m-%Y %H:%M:$S'),
            bool : lambda value : 1 if value else 0
        }
    )


user = User(
    id=101,
    email="abc@gmail.com",
    name="Avishek Thapa",
    created_at= datetime(2026, 3, 15, 14, 30),
    address=Address(
        city="Jharsuguda",
        street="OMP Line",
        zip_code="768204"
    ),
    is_active = False,
    tags=["premium", "subscriber"]
 )

user_dict = user.model_dump()
user_json = user.model_dump_json()

print("DICT", user_dict)
print("==================")

print("JSON", user_json)