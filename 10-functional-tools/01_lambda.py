# double = lambda number: number * 2

# print(double(5))
# print(double(10))


# numbers = [1, 2, 3, 4]

# result = map(lambda number: number * 2, numbers)
# print(list(result))

# prices = [100, 200, 300]

# result = map(lambda price: price + 10, prices)

# print(next(result))
# print(next(result))
# print(list(result))

# numbers = [1, 2, 3]

# result = map(lambda number: number, "abccd")

# print(type(result))
# print(iter(result) is result)
# print(next(iter(result)))

# prices = [100, 200, 300]

# result = map(lambda price: price + 10, prices)

# print(next(result))
# print(next(result))
# print(list(result))

# users = [
#     {"name": "Amit", "active": True},
#     {"name": "Priya", "active": False},
#     {"name": "Rahul", "active": True},
# ]

# active_users = list(filter(lambda user: user["active"], users))
# #active_users = [user for user in users if user["active"]]

# print(active_users)

from functools import reduce

numbers = [1, 2, 3, 4]

result = reduce(lambda accumulator, number: accumulator + number, numbers)


result = reduce(lambda acc, n: acc - n, numbers, 10)

print(result)