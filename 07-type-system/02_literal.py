from typing import Literal

Role = Literal["admin", "user", "moderator"]

def create_user(role: Role):
    print(role)

def get_status(status:Literal["active", "pending", "processing"]):
    print(status)

def get_user(user_id:Literal[2]):
    print(user_id)        

get_status("pending")
get_status("asasda")

get_user(user_id=3)