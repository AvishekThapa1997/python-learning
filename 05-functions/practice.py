


from functools import wraps
def decorator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print("Calling function")
        result = function(*args, **kwargs)
        print("Function completed")
        return result
    return wrapper

@decorator
def multiply(a, b):
    return a * b

print(multiply(5, 6))
