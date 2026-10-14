inventory = [("apple", 15), ("banana", 8), ("cherry", 42)]

for i,(fruit, quantity) in enumerate(inventory,1):
    print(f"{i}: {fruit.capitalize()} -> {quantity} units")