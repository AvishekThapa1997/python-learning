from functools import wraps

def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
       print(f"{func.__name__} Started 🚀")
       result = func(*args, **kwargs)
       print(f"{func.__name__} Ended")
       return result
    return wrapper

       
       
@log_activity
def gen_square(num):
    return num * num

print(gen_square(2))

