from functools import wraps

# def gen_square():
#     num = yield
#     while True:
#         num = yield num * num
        


# sq = gen_square()
# next(sq)
# for i in range(10):
#     print("I", i)
#     print("R",sq.send(i))


def my_decorator(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print("BEFORE")
        result = func(*args,**kwargs)
        print("AFTER")
        return result
    return wrapper

# @my_decorator
# def greet():
#     print("Hello!")

@my_decorator
def add(a, b):
    return a + b

def repeat(n):
    def decorator(func):
        def wrapper():
            result = []
            for _ in range(0, n):
               result.append(func())
            return result    
        return wrapper
    return decorator 
 
@repeat(5)
def greet():
    """Display a greeting."""
    print("Hello!")

greet()