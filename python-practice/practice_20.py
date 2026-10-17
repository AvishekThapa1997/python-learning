def calculate_discount(price, discount_percent):
    return price * discount_percent / 100

# print(calculate_discount(2000, 10))
# print(calculate_discount(price=2000, discount_percent=10))
# print(calculate_discount(discount_percent=10, price=2000))

discount_config = {
    "price": 2000,
    "discount_percent": 10,
}
print(calculate_discount(**discount_config))
print(calculate_discount(**discount_config))
print(calculate_discount(**discount_config))
# price, discount_percent = discount_config.values()
# print(price, discount_percent)

# calculate_discount()


def calculate_shipping(weight, distance, express=False):
    base_cost = weight * distance * 0.1

    if express:
        return base_cost * 1.5

    return base_cost


print(calculate_shipping(2, 100)) 
print(calculate_shipping(2, 100, True))
print(calculate_shipping(2, 100, express=True))
