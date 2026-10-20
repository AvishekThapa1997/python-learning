orders = [
    {"order_id": "ORD-101", "status": "shipped"},
    {"order_id": "ORD-102", "status": "pending"},
]

def generate_report(orders, formatter):
    return [
        formatter(order)
        for order in orders
    ]

def format_order_id(order):
    return order["order_id"]

def format_order_status(order):
    return order["status"].upper()

print(generate_report(orders, format_order_id))
# ['ORD-101', 'ORD-102']

print(generate_report(orders, format_order_status))
# ['SHIPPED', 'PENDING']