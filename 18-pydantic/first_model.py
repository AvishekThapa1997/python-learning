from pydantic import BaseModel


class User(BaseModel):
    id:int
    name:str
    is_active:bool


input_data = {
    "id":101,
    "name":"Avishek Thapa",
    "is_active" : 0
}

user = User(**input_data)

print(user)