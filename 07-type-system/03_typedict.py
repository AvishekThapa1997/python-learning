from typing import TypedDict

class User(TypedDict):
    name: str
    email: str

def get_user(user_id:int) -> User:
    return {
        "name": "Avishek Thapa",
        "email": "abc@yopmail.com"
    }

user = get_user(1)
print(user)
print(type(user))