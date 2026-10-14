from pydantic import BaseModel
from typing import Optional


class Item(BaseModel):
    id:int
    name:str

class Cart(BaseModel):
    user_id:int
    items: list[Item] # List[Item]
    quantities: dict[str, int] # Dict[str, int]

class Blog(BaseModel):
    id: int
    title : str
    content:str
    image_url: Optional[str] = None

