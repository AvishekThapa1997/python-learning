# # # def multiply(a, b):
# # #     return a * b

# # # operation = multiply
# # # print("Multiply: ", operation(2, 3))    


# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# # def calculate(operation, a, b):
# #     return operation(a, b)


# # print(calculate(add, 10, 20))
# # print(calculate(substract, 10 , 5))
# # print(calculate(multiply, 2 , 5))

# # def get_operation(operation):
# #     if operation == "add":
# #         return add
# #     elif operation == "substract":
# #         return subtract
# #     else:
# #         return multiply        


# # operation = get_operation("add")
# # print(operation(10,30))

# # def show_arguments(*args):
# #     print(args)
# #     print(type(args))


# # show_arguments(10, 20, 30, 40)

# # numbers = (10, 20, 30, 40)
# # show_arguments(*numbers)


# def show_arguments(**kwargs):
#     print(kwargs)
#     print(type(kwargs))

# show_arguments(name = "Avishek",age = 10)

# user = {
#     "name" : "Avishek",
#     "age" : 10
# }

# show_arguments(**user)


def show_user(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

show_user(10, 20, 30, name="Avishek", active=True)

def create_user(name, *, age, active):
    print(name, age, active)
create_user("Avishek", age=29, active=True)

# def create_request(method, *, timeout, retries):
#     print(f"Method:{method},Timeout:{timeout},Retries:{retries}")

# create_request("GET", timeout=5, retries=3) 

def create_request(*, method, timeout, retries):
    print(f"Method: {method}")
    print(f"Timeout: {timeout}")
    print(f"Retries: {retries}")

create_request(method="GET", timeout=5, retries=3)     