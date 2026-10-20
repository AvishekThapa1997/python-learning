def get_pending_orders():
    yield "ORD-101"
    yield "ORD-102"

def get_shipped_orders():
    yield "ORD-201"
    yield "ORD-202"

def get_all_orders():
    yield from get_pending_orders()
    yield from get_shipped_orders()

orders = get_all_orders()
# while (value:= next(orders,None)) is not None:
#     print(value)  

for order in orders:
    print(order)
def generate_sum(*numbers):
    return sum(numbers)


numbers = range(10)
print(generate_sum(*numbers))
