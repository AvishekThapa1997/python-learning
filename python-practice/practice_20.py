from enum import Enum

user_data = {
    "name": "Avishek",
    "address": {
        "city": "Bhubaneswar",
        "country": "India"
    },
    "orders": [
        {"order_id": "ORD-101", "status": "shipped"},
        {"order_id": "ORD-102", "status": "pending"}
    ]
}


OrderStatus = Enum('OrderStatus',[('SHIPPED','shipped'), ('PENDING', 'pending')])
 
class Order:
    order_id:str
    status: OrderStatus
    def __init__(self, order_id:str, status:OrderStatus):
        self.order_id = order_id
        self.status = status

    def __str__(self):
        return f"Order(user_id={self.order_id}, status={self.status.value})"    


class Address:
    city: str
    country: str
    def __init__(self, city:str, country: str):
        self.city = city
        self.country = country

    def __str__(self):
        return f"Address(city={self.city}, country={self.country})" 
    


class User:
    name: str
    address: Address
    orders : list[Order]
    def __init__(self, name: str, address:Address, orders:list[Order]):
        self.name = name
        self.address = address
        self.orders = orders

    def __str__(self):
        return f"User(name={self.name}, address={self.address}, orders={self.orders})"

    @classmethod
    def from_dict(cls,user_data):
        address = user_data['address']
        orders = user_data['orders']
        return cls(
            name=user_data['name'],
            address=Address(city=address['city'], country=address['country']),
            orders= [
                Order(order_id=order['order_id'],status=OrderStatus[order['status'].upper()])
                for order in orders
            ]
        )


orders_list : list[Order] = [
    Order(order_id="ORD-101", status=OrderStatus.SHIPPED),
    Order(order_id="ORD-102", status=OrderStatus.PENDING)
]

address = Address(city="Bhubaneswar", country="India")

user = User.from_dict(user_data=user_data)
print(user)