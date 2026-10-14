import threading

product_stock = 0

def restock():
    global product_stock
    for _ in range(10000):
        product_stock += 1

threads = [threading.Thread(target=restock) for _ in range(2)]
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()   


print(f"Product stock is {product_stock}")