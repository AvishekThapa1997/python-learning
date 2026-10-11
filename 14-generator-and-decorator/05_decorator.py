from datetime import datetime
from time import time
from functools import wraps
def measure_time(fn):
    @wraps(fn)
    def wrapper():
        start_time = datetime.now()
        fn()
        end_time = datetime.now()
        execution_time = end_time - start_time
        print(f"Execution Time is {execution_time}")
    return wrapper

@measure_time
def gen_square():
    for num in range(100):
        print(f"Square num is {num * num}")

print(f"Function name :{gen_square.__name__}")

        
