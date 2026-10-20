orders = [
    {"id": 101, "amount": 1500, "status": "completed"},
    {"id": 102, "amount": 800, "status": "pending"},
    {"id": 103, "amount": 2200, "status": "completed"},
    {"id": 104, "amount": 400, "status": "cancelled"},
    {"id": 105, "amount": 1200, "status": "completed"},
]

completed_order_ids = [
    order["id"]
    for order in orders
    if order['status'] == 'completed'
]

high_value_orders = [
    order
    for order in orders
    if (isinstance(amount := order.get("amount"),(int,float)))
    and amount >= 1000
]

completed_order_summaries = [
    f"Order {order['id']} : {order['amount']}"
    for order in orders
    if order['status'] == 'completed'
]