# from functools import reduce
# numbers = [1, 2, 3, 4, 5]

# filter_numbers = filter(lambda n: n > 2, numbers)
# result = reduce(lambda acc, curr: acc + (curr * 10), filter_numbers, 0)
# print(result)


# # Another approach
# filter_numbers = (num for num in numbers if num > 2)
# result = sum(filter_numbers)

# prices = [100, 250, 80, 400, 150]
# filtered_price = (price for price in prices if price >= 150)
# transformed_price = [price + (price * 0.10) for price in filtered_price]
# print(transformed_price)

# users = [
#     {"name": "A", "active": True, "verified": True},
#     {"name": "B", "active": True, "verified": False},
#     {"name": "C", "active": False, "verified": True},
# ]


# active_user_generator = (user["active"] for user in users)

# any_user_active = any(active_user_generator)
# all_user_active = all(active_user_generator)
# print(any_user_active)
# print(all_user_active)

# users = [
#     {"name": "Ravi", "age": 32},
#     {"name": "Anu", "age": 24},
#     {"name": "Maya", "age": 28},
# ]

# sorted_users = sorted(users, key=lambda user: user['age'])
# print(sorted_users)


# entries = enumerate(sorted_users)
# for entry in entries:
#     print(entry)


# users = [
#     {"name": "Ravi", "age": 32, "active": True},
#     {"name": "Anu", "age": 24, "active": False},
#     {"name": "Maya", "age": 28, "active": True},
#     {"name": "Raj", "age": 22, "active": True},
# ]


# active_users = (user for user in users if user["active"])
# active_user_names = [
#     user["name"] for user in users if user["active"]
# ]
# sorted_users = sorted(active_users, key=lambda user : user['age'])

# print(active_user_names)

names = ["Avishek", "Ravi", "Maya"]
scores = [90, 75, 88]


# map_name_and_score = list(map(lambda name, score: (name, score), zip(names, scores)))
# print(map_name_and_score)

print( "LIST",list(zip(names, scores)))