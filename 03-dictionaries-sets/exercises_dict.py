# users = [
#     {"id": 101, "name": "Avishek", "active": True},
#     {"id": 102, "name": "Rahul", "active": False},
#     {"id": 103, "name": "Priya", "active": True},
#     {"id": 104, "name": "Amit", "active": False},
# ]

# users.append({
#     "id":105,
#     "name":"test",
#     "active" : True
# })

# user_id_with_name = {
#     user["id"]:user["name"]
#     for user in users
#     if user["active"]
# }
# print(user_id_with_name)

# products = [
#     {"id": 1, "name": "Laptop", "price": 80000},
#     {"id": 2, "name": "Mouse", "price": 1500},
#     {"id": 3, "name": "Keyboard", "price": 3000},
#     {"id": 4, "name": "Monitor", "price": 12000},
# ]

# product_name_by_id = {
#     product["id"]:product["name"]
#     for product in products
#     if product['price'] > 5000
# }
# print(product_name_by_id)

orders = [
    {"id": 1, "amount": 5000, "status": "completed"},
    {"id": 2, "amount": 2500, "status": "pending"},
    {"id": 3, "amount": 8000, "status": "completed"},
    {"id": 4, "amount": 1500, "status": "cancelled"},
]

updated_order_amount_by_id = {
    order["id"] : order["amount"] * 0.9
    for order in orders
    if order["status"] == "completed"
}
print(updated_order_amount_by_id)