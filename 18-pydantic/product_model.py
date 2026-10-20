from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True



product_one = Product(id=101, name="Shoe", price=222.99,in_stock=False)
product_two = Product(id= 102, name="Mouse", price=333.99)

print(product_one)
print(product_two)