# Day 5 — Functions

## Goal

Build a practical understanding of Python functions for backend development and prepare for FastAPI.

---

## 1. Functions as Objects

Functions are objects in Python. They can be assigned to variables, passed as arguments, and returned from other functions.

```python
def add(a, b):
    return a + b

def calculate(operation, a, b):
    return operation(a, b)

print(calculate(add, 10, 20))
```

This is similar to JavaScript callbacks / higher-order functions.

---

## 2. `*args`

`*args` collects extra positional arguments into a tuple.

```python
def show(*args):
    print(args)

show(10, 20, 30)
```

Output:

```text
(10, 20, 30)
```

When calling a function, `*` can unpack a tuple into positional arguments.

---

## 3. `**kwargs`

`**kwargs` collects extra keyword arguments into a dictionary.

```python
def show(**kwargs):
    print(kwargs)

show(name="Avishek", role="developer")
```

Output:

```text
{'name': 'Avishek', 'role': 'developer'}
```

When calling a function, `**` can unpack a dictionary into keyword arguments.

---

## 4. `*args` + `**kwargs`

```python
def show_user(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)
```

Both are optional to define.

When nothing is passed:

```text
args   → ()
kwargs → {}
```

- `*args` collects extra positional arguments.
- `**kwargs` collects extra keyword arguments.

`*args` must come before `**kwargs` in function definitions and calls.

---

## 5. Positional-only and Keyword-only Parameters

```python
def func(a, b, /, c, d, *, e, f):
    ...
```

Rule:

```text
before `/`          → positional-only
between `/` and `*` → positional or keyword
after `*`           → keyword-only
```

If there is no `/`, there are no positional-only parameters.

Example:

```python
def create_request(method, *, timeout, retries):
    ...
```

`timeout` and `retries` must be passed by keyword.

---

## 6. Scope — LEGB

Python resolves names using:

```text
L → Local
E → Enclosing
G → Global
B → Built-in
```

Closures capture the enclosing variable binding, not an earlier snapshot of its value.

```python
def outer():
    x = 10

    def inner():
        print(x)

    x = 20
    return inner

fn = outer()
fn()
```

Output:

```text
20
```

### `nonlocal`

Use `nonlocal` when an inner function needs to modify a variable from its enclosing scope.

```python
def outer():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment
```

Detailed practice with `nonlocal` is intentionally deferred until needed.

---

## 7. Decorators

A decorator receives a function and commonly returns a replacement function, usually called a `wrapper`.

```python
def my_decorator(function):
    def wrapper():
        print("Before")
        function()
        print("After")

    return wrapper
```

Using:

```python
@my_decorator
def greet():
    print("Hello")
```

is effectively:

```python
greet = my_decorator(greet)
```

Flow:

```text
original function
      ↓
decorator(original function)
      ↓
wrapper returned
      ↓
function name points to wrapper
      ↓
caller calls wrapper
      ↓
wrapper calls original function
```

`wrapper` is a conventional name; it is not a special Python keyword.

---

## 8. Decorators with Arguments

A reusable decorator wrapper normally accepts arbitrary positional and keyword arguments:

```python
def my_decorator(function):
    def wrapper(*args, **kwargs):
        print("Before")
        function(*args, **kwargs)
        print("After")

    return wrapper
```

This allows:

```python
@my_decorator
def create_user(name):
    print(f"Creating {name}")
```

to work with both:

```python
create_user("Avishek")
```

and:

```python
create_user(name="Avishek")
```

The forwarding pattern is:

```python
wrapper(*args, **kwargs)
```

and:

```python
function(*args, **kwargs)
```

---

## 9. Preserving Return Values in Decorators

A wrapper does not automatically preserve the original function's return value.

This loses the value:

```python
def wrapper(*args, **kwargs):
    function(*args, **kwargs)
```

Correct:

```python
def wrapper(*args, **kwargs):
    result = function(*args, **kwargs)
    return result
```

Flow:

```text
caller
  ↓ arguments
wrapper
  ↓ arguments
original function
  ↓ return value
wrapper
  ↓ return value
caller
```

`result` is the value returned by the original function. It is not passed back into the original function.

---

## 10. Practical Decorator Example

Decorators can add reusable behavior without modifying the original function.

```python
import time

def log_time(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()

        print(f"{function.__name__} took {end - start:.4f} seconds")
        return result

    return wrapper

@log_time
def calculate():
    time.sleep(1)
    return 100

result = calculate()
print(result)
```

---

## 11. `functools.wraps`

Without `wraps`, a decorated function can expose the wrapper's metadata:

```python
def my_decorator(function):
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)

    return wrapper
```

Then:

```python
@my_decorator
def add(a, b):
    return a + b

print(add.__name__)
```

can output:

```text
wrapper
```

Use:

```python
from functools import wraps

def my_decorator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)

    return wrapper
```

Now:

```text
add
```

is preserved as the function name.

`wraps` preserves important metadata from the original function on the wrapper.

---

## 12. Function Type Hints

```python
def add(a: int, b: int) -> int:
    return a + b
```

- `a: int` → expected integer parameter
- `b: int` → expected integer parameter
- `-> int` → expected integer return value

Python type hints are not general runtime validation.

For example:

```python
def get_user(user_id: str) -> dict[str, int]:
    return {
        "a": "dddd"
    }
```

Python does not automatically raise an error because the returned dictionary contains a string.

Runtime validation will be covered later with Pydantic and FastAPI.

---

## 13. Generic Container Type Hints

```python
dict[str, str]
```

means:

```text
key   → str
value → str
```

Union types can use `|`:

```python
dict[str, int | str | bool]
```

The value may be an `int`, `str`, or `bool`.

`Any` is also available:

```python
from typing import Any

dict[str, Any]
```

Prefer precise types when the expected shape is known.

---

## 14. `Callable`

A function that receives another function can be type-hinted using `Callable`:

```python
from typing import Callable

def add(a: int, b: int) -> int:
    return a + b

def calculate(
    operation: Callable[[int, int], int],
    a: int,
    b: int,
) -> int:
    return operation(a, b)
```

```python
print(calculate(add, 10, 20))
```

Output:

```text
30
```

`Callable[[int, int], int]` means the callable accepts two integers and returns an integer.

Advanced callable typing is deferred until needed.

---

## 15. `async` / `await` Basics

Calling an `async def` function creates a coroutine object.

```python
async def fetch_data():
    return "data"
```

This:

```python
result = fetch_data()
```

does not directly produce `"data"`.

Use `await`:

```python
import asyncio

async def fetch_data():
    return "data"

async def main():
    result = await fetch_data()
    print(result)

asyncio.run(main())
```

Output:

```text
data
```

Mental model:

```text
async def
   ↓
coroutine function

fetch_data()
   ↓
coroutine object

await fetch_data()
   ↓
result
```

Deeper `asyncio`, event-loop, task, and concurrency concepts are covered later.

---

## 16. Default Arguments

Default arguments are evaluated when the function is defined, not every time it is called.

This differs from JavaScript's default parameter evaluation behavior.

### Mutable Default Argument Pitfall

Avoid mutable objects such as lists as defaults when a fresh object is expected per call:

```python
def add_tag(tag, tags=[]):
    tags.append(tag)
    return tags
```

The same default list is reused:

```python
print(add_tag("python"))
print(add_tag("fastapi"))
```

Output:

```text
["python"]
["python", "fastapi"]
```

Safe pattern:

```python
def add_tag(tag, tags=None):
    if tags is None:
        tags = []

    tags.append(tag)
    return tags
```

Important distinction:

```text
No argument → shared default object
Explicit []  → new list object
```

---

## 17. Key Day 5 Takeaways

```text
Functions are objects
        ↓
Can be passed / returned
        ↓
*args / **kwargs
        ↓
Flexible signatures
        ↓
Scope / closures
        ↓
Decorators
        ↓
Wrapper + argument forwarding
        ↓
Preserve return values
        ↓
functools.wraps
        ↓
Function type hints
        ↓
async / await basics
        ↓
Default argument behavior
```

### FastAPI Connection

These concepts will directly support later FastAPI learning:

- Decorators → route declarations such as `@app.get(...)`
- Function parameters → path/query/request handling
- Type hints → API definitions
- `Callable` → dependencies and higher-order functions
- `async` / `await` → async endpoints and I/O
- Return annotations → response typing
- Pydantic → runtime validation of structured API data

Deeper FastAPI/Pydantic behavior will be learned during the FastAPI phase.
