# # def greet():
# #     print("Hello")


# # def my_decorator(function):
# #     def wrapper(*args, **kwargs):
# #         print("Before")
# #         function(*args, **kwargs)
# #         print("After")

# #     return wrapper

# # @my_decorator
# # def create_user(name):
# #     print(f"Creating {name}")

# # @my_decorator
# # def delete_user():
# #     print("Deleting user")

# # create_user("Avishek Thapa")

# # def test(a,b):
# #     return a + b

# # print(test(**{"a":10,"b":20}))    



# import time


# def log_time(function):
#     def wrapper(*args, **kwargs):
#         print("Wrapper Start")
#         start = time.time()

#         result = function(*args, **kwargs)

#         end = time.time()

#         print(f"{function.__name__} took {end - start:.4f} seconds")
#         print("Wrapper End")
#         return result

#     return wrapper


# @log_time
# def calculate():
#     print("Callback Started")
#     time.sleep(1)
#     print("Calback Ended")
#     return 100


# result = calculate()
# print(result)

# print(calculate.__name__)
from functools import wraps

def my_decorator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return result

    return wrapper
def my_decorator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)

    return wrapper


@my_decorator
def add(a, b):
    return a + b


# print(add.__name__) #wrapper as function out name depends on the wrapper function name created inside decorator"

# def get_user(user_id:str) -> dict[str,int]:
#     return {
#         "a":"dddd"
#     }

# print(get_user("1"))

from typing import Callable

def add(*args) -> int:
    sum = 0
    for num in args:
        sum += num
    return sum


def calculate(
    operation: Callable[[()], int],
    *args
) -> int:
    return operation(*args)


print(calculate(add, 10, 20, 30, 40))
