from pydantic import BaseModel,computed_field, Field


class Product(BaseModel):
    price:float
    quantity:int

    @computed_field
    @property
    def total_price(self) -> float:
        return round(self.price * self.quantity, 2)


product = Product(price=100, quantity=2)
print(product)


class Booking(BaseModel):
    user_id:int
    room_id:int
    nights: int = Field(
        ...,
        ge = 1
    )
    rate_per_night: float

    @computed_field
    @property
    def total_amount(self) -> float:
        return round(self.nights * self.rate_per_night ,2)


booking = Booking(
    user_id=123,
    room_id=456,
    nights=2,
    rate_per_night=125.50
)

print(booking.model_dump())