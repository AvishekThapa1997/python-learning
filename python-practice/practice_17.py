orders = {
    101: {"amount": 1500.0, "status": "pending"},
    102: {"amount": 0.0, "status": "pending"},
    103: {"amount": 800.0, "status": "completed"},
}


def process_order(orders, order_id):
    if order_id not in orders:
        raise ValueError("Order is not available")
    order = orders[order_id]
    status = order['status']
    if status != 'pending':
        raise ValueError("Processed order cannot be reprocess")
    order['status'] = "completed"
    return order['amount']

try:
    print(process_order(orders,110))
except ValueError as err:
    print(f"Unable to process order: {err}")    
