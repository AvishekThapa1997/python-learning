from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id: Optional[int] = None


user = User(id=10)    

print(user.model_fields_set)