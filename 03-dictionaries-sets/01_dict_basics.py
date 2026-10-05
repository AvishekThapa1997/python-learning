# # user = {
# #     "id": 101,
# #     "name": "Avishek",
# #     "role": "Senior Engineer"
# # }

# # print(user["name"])
# # print(user.get("name"))


# # print(hash("hello"))
# user = {
#     "name": "Avishek",
#     "age": 28
# }

# user["role"] = "Senior Engineer"
# print(user)

# user["age"] = 29
# print(user)

# print(user.pop("age"))
# print(user)

# # for key, value in user.items():
# #     print(key, value)

# # for item in user:
# #     print("Item:", item)


# # print(user.keys())
# # print(user.values())
# # print(user.items())

# user = {"name": "Avishek"}

# keys = user.keys()

# user["age"] = 28

# print(keys)
# print(list(user.keys()))

# request_data = {
#     "name": "Avishek",
#     "email": "avishek@example.com"
# }
# phone = request_data.get("phone")
# if(phone is None):
#     print("No phone number available")


# user = {
#     "id": 101,
#     "name": "Avishek",
#     "profile": {
#         "role": "Senior Engineer",
#         "country": "India"
#     }
# }

# print(user["profile"]["role"])
# print(user["profile"]["country"])


numbers = [1, 2, 3, 4]

# dict comprehension
# {
#     key: value
#     for item in iterable
#     if condition
# }
squares = {
    x: x * x
    for x in numbers
}

print(squares)

