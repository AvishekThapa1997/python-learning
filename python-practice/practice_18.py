orders = [
    {"id": 101, "amount": 500},
    {"id": 102, "amount": 800},
    {"id": 103, "amount": 300},
    {"id": 104, "amount": 1200},
]

taxes = (order["amount"] * 0.18 for order in orders)