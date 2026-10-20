from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    postal_code: str


class User(BaseModel):
    id: int
    name:str
    address: Address


user = User(id=101, name="Avishek Thapa", address=Address(street="OMP Line",city="JSG", postal_code="768204"))

print("User", user)

