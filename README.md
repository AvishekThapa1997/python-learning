## 1. \*args and \*\*kwargs — Quick Reference

- **Argument order:** Required positional parameters → `*args` → keyword-only parameters → `**kwargs` (when using all these forms).
- `*args` in a function definition collects extra positional arguments into a tuple.
- `**kwargs` in a function definition collects extra keyword arguments into a dictionary.
- `*items` in a function call unpacks an iterable into positional arguments.
- `**data` in a function call unpacks a dictionary into keyword arguments.
- Example: `func(*[10, 20])` passes two positional arguments.
- Example: `func(**{"name": "Ava"})` passes `name="Ava"`.
- Parameters after `*args` are keyword-only; a bare `*` also makes following parameters keyword-only.
- Positional arguments must come before keyword arguments in a function call.
- Default arguments are used when the caller omits those parameters.
- Unexpected keyword arguments raise `TypeError` unless accepted by `**kwargs`.
- Passing a value twice to the same function parameter raises `TypeError`.
- In dictionary literals, later duplicate keys overwrite earlier values.
- Avoid mutable defaults such as `items=[]`; use `None` and initialize inside the function.
- `result = items` creates another reference; `items[:]` creates a shallow list copy.

## 1. Compare the Tools: JavaScript vs Python

| Purpose                           | JavaScript Ecosystem  | Python Ecosystem      |
| --------------------------------- | --------------------- | --------------------- |
| Install packages                  | `npm install express` | `pip install fastapi` |
| Project metadata and dependencies | `package.json`        | `pyproject.toml`      |
| Lock resolved dependency versions | `package-lock.json`   | `uv.lock`             |
| Local dependency environment      | `node_modules/`       | `.venv/`              |
| Manage runtime versions           | `nvm`                 | `uv python`           |
| Initialize a project              | `npm init`            | `uv init`             |
| Synchronize dependencies          | `npm install`         | `uv sync`             |
| Run a project command             | `npm run dev`         | `uv run ...`          |

### Key Differences

- **`pip`**: Primarily installs Python packages.
- **`uv`**: Manages Python projects, dependencies, lockfiles, virtual environments, and Python versions.
- **`pyproject.toml`**: Defines project metadata and declared dependencies.
- **`uv.lock`**: Records resolved dependency versions for reproducible environments.
- **`.venv/`**: Contains the isolated Python environment and installed packages.

## 3. Generator

- **1. What Is a Generator?**

  A generator is an iterator that produces values one at a time instead of storing all the results upfront.

  Generators are useful when:
  - Processing large datasets.
  - Reading files line by line.
  - Processing streams of records.
  - Avoiding unnecessary intermediate lists.
  - Producing values on demand.

  A generator can be created using:
  - A generator function containing `yield`.
  - A generator expression.

  - **1.1. Using `return`**

    A `return` statement ends the function and returns its result.

    ```python
    def get_number():
        return 10

    result = get_number()
    print(result)
    ```

    Output:

    ```text
    10
    ```

    Once the function returns, its execution is finished.

  - **1.2. Using `yield`**

    A `yield` statement produces a value and pauses the generator. When execution resumes, it continues from where it paused.

    ```python
    def get_numbers():
        print("Starting")
        yield 10

        print("Resuming")
        yield 20

        print("Finished")

    numbers = get_numbers()

    print(next(numbers))
    print(next(numbers))
    ```

    Output:

    ```text
    Starting
    10
    Resuming
    20
    ```

    Notice that `Finished` is not printed because we haven't requested another value.

  - **1.3. Important Points**
    - Calling a generator function creates a generator object.
    - The function body does not execute immediately.
    - `next()` resumes the generator until it reaches the next `yield`.
    - The yielded value is returned to the caller.
    - Execution pauses at the `yield` statement and resumes from that exact point on the next request.

- **2. `next()` and Yielded Values**

  A yielded value is not automatically printed. The value is returned to the caller, and you decide what to do with it.
  - **2.1. Using `next()`**

    ```python
    def get_numbers():
        yield 10
        yield 20

    numbers = get_numbers()

    next(numbers)
    ```

    The value `10` is returned by `next()` but is not printed because we didn't use `print()`.

    To display the values:

    ```python
    print(next(numbers))
    print(next(numbers))
    ```

    Output:

    ```text
    10
    20
    ```

  - **2.2. `next()` After Exhaustion**

    ```python
    numbers = iter([10, 20])

    print(next(numbers))
    print(next(numbers))
    print(next(numbers))
    ```

    The third call raises `StopIteration` because there are no more values.

    A `for` loop handles normal iterator exhaustion automatically, but a direct `next()` call raises `StopIteration` when the iterator is exhausted.

- **3. Lazy Evaluation**

  Generators produce values only when requested.
  - **3.1. List Comprehension**

    ```python
    numbers = [x * 2 for x in range(5)]
    print(numbers)
    ```

    Output:

    ```text
    [0, 2, 4, 6, 8]
    ```

    A list comprehension evaluates all the expressions and stores the results in a list.

  - **3.2. Generator Expression**

    ```python
    numbers = (x * 2 for x in range(5))
    ```

    This creates a generator object. It does not immediately calculate and store all five results.

    ```python
    print(next(numbers))
    print(next(numbers))
    print(list(numbers))
    ```

    Output:

    ```text
    0
    2
    [4, 6, 8]
    ```

    The first two values have already been consumed, so `list()` collects only the remaining values.

  - **3.3. Important Distinction**
    - A generator expression does not store all generated results.
    - It produces values as they are requested.
    - A generator can reduce the memory needed for intermediate results.
    - A generator's memory usage also depends on its source. For example, iterating over an existing large list does not make that original list disappear.

- **4. Generator Function vs Generator Expression**

  Both approaches can produce values lazily, but their syntax and use cases differ.
  - **4.1. Generator Function**

    A generator function uses `yield`.

    ```python
    def get_squares():
        for number in range(4):
            yield number ** 2

    print(list(get_squares()))
    ```

    Output:

    ```text
    [0, 1, 4, 9]
    ```

  - **4.2. Generator Expression**

    A generator expression uses parentheses.

    ```python
    squares = (number ** 2 for number in range(4))

    print(list(squares))
    ```

    Output:

    ```text
    [0, 1, 4, 9]
    ```

  - **4.3. Comparing Comprehension Syntax**

    ```python
    # List comprehension
    [x * 2 for x in range(5)]

    # Generator expression
    (x * 2 for x in range(5))

    # Set comprehension
    {x * 2 for x in range(5)}
    ```

    - A list comprehension creates a list.
    - A generator expression creates a generator.
    - A set comprehension creates a set.

- **5. Generator Exhaustion**

  A generator is generally a one-time iterator. Once all its values have been consumed, it does not restart automatically.
  - **5.1. Consuming a Generator with `list()`**

    ```python
    def get_numbers():
        yield 10
        yield 20

    numbers = get_numbers()

    print(list(numbers))
    print(list(numbers))
    ```

    Output:

    ```text
    [10, 20]
    []
    ```

    Why?
    - The first `list(numbers)` consumes the generator completely.
    - The second `list(numbers)` finds no remaining values.

  - **5.2. Iterating Multiple Times**

    To iterate over the values again, create a new generator.

    ```python
    def get_numbers():
        yield 10
        yield 20

    numbers = get_numbers()
    print(list(numbers))

    numbers = get_numbers()
    print(list(numbers))
    ```

    Output:

    ```text
    [10, 20]
    [10, 20]
    ```

  - **5.3. Generators in Loops**

    ```python
    def get_users():
        yield "Alice"
        yield "Bob"
        yield "Charlie"

    users = get_users()

    for user in users:
        print(user)

    for user in users:
        print(user)
    ```

    Output:

    ```text
    Alice
    Bob
    Charlie
    ```

    The second loop prints nothing because the generator has already been exhausted.

  - **5.4. `list()` and `for` vs `next()`**
    - `next(iterator)` requests one value and raises `StopIteration` when exhausted.
    - `list(iterator)` consumes all remaining values and handles normal exhaustion internally.
    - A `for` loop also handles normal iterator exhaustion internally.
    - `list()` does not suppress arbitrary exceptions; it handles the normal `StopIteration` signal that indicates the iterator has finished.

- **6. Generator Expressions with `sum()`**

  Suppose we have transaction amounts:

  ```python
  amounts = [500, 1500, 800, 2200, 1200]
  ```

  We want to calculate the total of amounts greater than `1000`.
  - **6.1. Using a List Comprehension**

    ```python
    total = sum([amount for amount in amounts if amount > 1000])
    print(total)
    ```

    Output:

    ```text
    4900
    ```

    This creates an intermediate list containing the matching amounts: `[1500, 2200, 1200]`.

  - **6.2. Using a Generator Expression**

    ```python
    total = sum(amount for amount in amounts if amount > 1000)
    print(total)
    ```

    Output:

    ```text
    4900
    ```

    The generator expression produces matching amounts on demand, and `sum()` consumes them.

    ```python
    (amount for amount in amounts if amount > 1000)
    ```

    This expression creates a generator object. It does not directly return `4900` or a list.

  - **6.3. When Is a Generator Useful?**

    A generator is a good fit when you need to process values once, one at a time, without building an intermediate collection.

    A list is often more suitable when you need to:
    - Reuse the results.
    - Access values by index.
    - Iterate over the stored values multiple times.

- **7. `yield from`**

  `yield from` delegates iteration to another iterable or generator.
  - **7.1. Delegating to Another Generator**

    ```python
    def get_numbers():
        yield 1
        yield 2

    def get_all():
        yield from get_numbers()
        yield 3

    print(list(get_all()))
    ```

    Output:

    ```text
    [1, 2, 3]
    ```

    The statement:

    ```python
    yield from get_numbers()
    ```

    passes through the values yielded by `get_numbers()`.

  - **7.2. Equivalent Loop**

    For basic iteration, `yield from` is similar to writing:

    ```python
    def get_all():
        for number in get_numbers():
            yield number

        yield 3
    ```

  - **7.3. Delegating to Other Iterables**

    `yield from` also works with other iterables, such as lists and tuples.

    ```python
    def get_values():
        yield from [10, 20, 30]

    print(list(get_values()))
    ```

    Output:

    ```text
    [10, 20, 30]
    ```

    `yield from` also supports generator delegation behavior, including forwarding values sent into the delegating generator. For basic iteration, remember that it delegates producing values to another iterable or generator.

- **8. A `yield` Expression Can Receive a Value**

  So far, we've used `yield` to produce values. But a `yield` expression can also receive a value sent by the caller using `.send()`.
  - **8.1. Example**

    ```python
    def get_value():
        received = yield 10
        print("Received:", received)

    gen = get_value()

    value = next(gen)
    print("Yielded:", value)

    gen.send(50)
    ```

    Output:

    ```text
    Yielded: 10
    Received: 50
    ```

  - **8.2. First: Produce a Value**

    When the generator reaches:

    ```python
    received = yield 10
    ```

    it:
    - Produces `10` for the caller.
    - Pauses execution.

    The caller receives `10`.

  - **8.3. Second: Receive a Value**

    When the caller resumes the generator with:

    ```python
    gen.send(50)
    ```

    the suspended `yield` expression evaluates to `50`.

    Therefore, the statement:

    ```python
    received = yield 10
    ```

    assigns `50` to `received` after the generator resumes.

  - **8.4. Important Rule**

    You must start a generator before sending a non-`None` value into it.

    Valid:

    ```python
    gen = get_value()
    next(gen)
    gen.send(50)
    ```

    Invalid:

    ```python
    gen = get_value()
    gen.send(50)
    ```

    The second example raises `TypeError` because the generator has not started.

- **9. Understanding `num = yield`**

  Consider this generator:

  ```python
  def example():
      num = yield 5
      yield num

  gen = example()

  print(next(gen))
  print(gen.send(100))
  ```

  Output:

  ```text
  5
  100
  ```

  - **9.1. Producing a Value**

    The first call:

    ```python
    next(gen)
    ```

    starts the generator and reaches:

    ```python
    num = yield 5
    ```

    The generator produces `5` and pauses.

  - **9.2. Receiving a Value**

    The next call:

    ```python
    gen.send(100)
    ```

    resumes execution. The suspended `yield` expression evaluates to `100`.

  - **9.3. Assigning the Received Value**

    The assignment:

    ```python
    num = yield 5
    ```

    assigns `100` to `num`.

    The next statement:

    ```python
    yield num
    ```

    produces `100`.

    Remember that `num = yield 5` means:
    - Yield `5` now.
    - When resumed, receive a value.
    - Assign that received value to `num`.

- **10. Using a Generator as a Coroutine**

  A generator can be used as a simple coroutine: the caller sends values into it, and it produces results back.

  Consider the square generator we explored.
  - **10.1. The Example**

    ```python
    def gen_square():
        while True:
            num = yield
            result = num * num
            num = yield result

    sq = gen_square()
    next(sq)

    for i in range(4):
        print("I", i)
        print("R", sq.send(i))
    ```

    Output:

    ```text
    I 0
    R 0
    I 1
    R None
    I 2
    R 4
    I 3
    R None
    ```

  - **10.2. Understanding the Two `yield` Statements**

    ```python
    num = yield
    result = num * num
    num = yield result
    ```

    There are two separate pause points inside the loop.
    - The first `yield` receives a value but produces `None`.
    - The second `yield` produces the calculated square and can receive a value when resumed.

  - **10.3. First Call: `sq.send(0)`**
    - The generator is paused at `num = yield`.
    - The value `0` is assigned to `num`.
    - `result = num * num` calculates `0`.
    - `num = yield result` produces `0` and pauses.

    The call returns `0`.

  - **10.4. Second Call: `sq.send(1)`**
    - The generator resumes at `num = yield result`.
    - The sent value `1` becomes the result of that `yield` expression.
    - It is assigned to `num`, but then the loop reaches its end.
    - The loop repeats and reaches `num = yield`.
    - This `yield` has no expression, so the call returns `None`.

    The sent value `1` is not used to calculate a square because the generator is resuming at the second `yield`, not the first.

  - **10.5. Third Call: `sq.send(2)`**
    - The generator resumes at `num = yield`.
    - It assigns `2` to `num`.
    - It calculates `2 * 2`.
    - It yields `4`.

    The result is `4`.

  - **10.6. Key Lesson**

    A loop does not restart immediately when a generator yields a value. The generator resumes from the exact point where it paused.

    A `.send(value)` call:
    - Resumes the currently suspended `yield`.
    - Makes the sent value the result of that `yield` expression.
    - Continues executing until the next `yield` or until the generator finishes.
    - Returns the value produced by the next `yield`.

    If the next `yield` has no expression, the call returns `None`.

- **11. A Cleaner Square Coroutine**

  For a coroutine that receives the next number while yielding the previous number's square:

  ```python
  def gen_square():
      num = yield

      while True:
          num = yield num * num

  sq = gen_square()
  next(sq)

  print(sq.send(5))
  print(sq.send(10))
  print(sq.send(20))
  ```

  Output:

  ```text
  25
  100
  400
  ```

  - **11.1. Starting the Generator**

    The initial `next(sq)` starts the generator and pauses at the first `yield`, ready to receive a value.

  - **11.2. Sending Values**
    - `sq.send(5)` assigns `5` to `num`, then yields `25`.
    - `sq.send(10)` resumes the suspended `yield`, assigns `10` to `num`, then yields `100`.
    - `sq.send(20)` resumes again, assigns `20` to `num`, then yields `400`.

  - **11.3. Understanding the Pipelined Behavior**

    The expression:

    ```python
    num = yield num * num
    ```

    both produces the current square and receives the next value when execution resumes.

    This pattern is pipelined:
    - The first `.send(5)` yields the square of `5`.
    - The next `.send(10)` yields the square of `10`.
    - Each subsequent call yields the square of the number supplied to that call.

    For a simple calculation like squaring a number, an ordinary function is more straightforward. This coroutine pattern is useful for learning how generators communicate with their callers and preserve state across suspension points.

- **12. Generator Mental Model**

  Keep these rules in mind:
  - **12.1. Generator Creation and Execution**
    - Calling a generator function creates a generator object.
    - The function body does not execute immediately.

  - **12.2. Pausing and Resuming**
    - `next()` starts or resumes the generator.
    - `yield value` produces a value and pauses execution.
    - A generator resumes from the exact `yield` where it paused.

  - **12.3. Sending Values**
    - `send(value)` resumes the generator and supplies a value to the suspended `yield` expression.
    - The sent value becomes the result of that `yield` expression.
    - If a `yield` has no expression, it produces `None`.

  - **12.4. Generator Exhaustion**
    - `list()` and `for` loops consume values until exhaustion.
    - An exhausted generator does not restart automatically.
    - Create a new generator object to iterate over the sequence again.

  - **12.5. Lazy Evaluation**
    - Generator expressions produce values on demand.
    - They can reduce memory usage by avoiding intermediate lists.
    - `yield from` delegates iteration to another iterable or generator.

  - **12.6. Multiple `yield` Statements**
    - Multiple `yield` statements in a loop create multiple pause points.
    - Each call resumes whichever `yield` is currently active.
    - To understand the output, trace the generator from its exact suspended position.

- **13. Practice Questions**

  Try these without looking up the answers.
  - **13.1. Question 1: Basic Generator**

    Predict the exact output.

    ```python
    def get_numbers():
        yield 10
        yield 20

    numbers = get_numbers()

    print(next(numbers))
    print(next(numbers))
    ```

  - **13.2. Question 2: Lazy Evaluation**

    Predict the exact output.

    ```python
    def generate():
        print("A")
        yield 1
        print("B")
        yield 2

    gen = generate()

    print("Ready")
    print(next(gen))
    print("Done")
    ```

  - **13.3. Question 3: Exhaustion**

    Predict the exact output.

    ```python
    def get_values():
        yield 1
        yield 2

    values = get_values()

    print(list(values))
    print(list(values))
    ```

  - **13.4. Question 4: Generator Expression**

    Write a single expression using `sum()` and a generator expression to calculate the sum of numbers greater than `10`.

    ```python
    numbers = [5, 15, 8, 25, 12]
    ```

    Expected result:

    ```text
    52
    ```

  - **13.5. Question 5: Sending Values**

    Predict the exact output.

    ```python
    def example():
        value = yield 10
        yield value

    gen = example()

    print(next(gen))
    print(gen.send(50))
    ```

  - **13.6. Question 6: Multiple `yield` Statements**

    Predict the exact output and explain why the second call returns `None`.

    ```python
    def gen_square():
        while True:
            num = yield
            yield num * num

    sq = gen_square()
    next(sq)

    print(sq.send(3))
    print(sq.send(4))
    print(sq.send(5))
    ```

- **14. Summary**

  Generators let you produce values lazily, pause execution, and resume later. They retain their execution state between calls.

  The `yield` expression can also receive values through `.send()`, which allows generators to act as simple coroutines.

  The most important concept is to understand exactly where execution pauses and where it resumes, especially when a generator contains multiple `yield` statements.
  - **14.1. Key Takeaways**
    - `yield` produces a value and pauses execution.
    - `next()` resumes the generator.
    - `.send(value)` resumes the generator and supplies a value to the suspended `yield` expression.
    - Generator expressions are lazy and generally consume values only once.
    - `yield from` delegates iteration.
    - Multiple `yield` statements create multiple suspension points.

# Python Decorators

## 1. What Is a Decorator?

A decorator is a function that takes another function as input, adds or changes its behavior, and returns a function.

Decorators are useful when we want to add behavior without modifying the original function's implementation.

Common use cases include:

- Logging
- Measuring execution time
- Authentication and authorization
- Caching
- Validation
- Registering API routes in FastAPI

### Example

```python
def my_decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")

    return wrapper


def greet():
    print("Hello!")


greet = my_decorator(greet)
greet()
```

Output:

```text
Before function execution
Hello!
After function execution
```

---

## 2. Functions Are First-Class Objects

Python functions are objects. This means we can:

- Assign a function to a variable.
- Pass a function as an argument.
- Return a function from another function.

### 2.1 Assign a Function to a Variable

```python
def greet():
    print("Hello!")


say_hello = greet

say_hello()
```

Output:

```text
Hello!
```

Notice the difference:

```python
say_hello = greet
```

This assigns the function object to `say_hello`.

```python
say_hello = greet()
```

This executes `greet()` immediately and assigns its return value to `say_hello`.

### 2.2 Pass a Function as an Argument

```python
def greet():
    print("Hello!")


def execute(func):
    func()


execute(greet)
```

Output:

```text
Hello!
```

We pass `greet`, not `greet()`, because we want to pass the function itself rather than execute it immediately.

### 2.3 Return a Function

```python
def greet():
    print("Hello!")


def get_function():
    return greet


result = get_function()
result()
```

Output:

```text
Hello!
```

The call to `get_function()` returns the function object. The function executes when we subsequently call `result()`.

---

## 3. Basic Decorator Structure

A basic decorator accepts a function, defines a wrapper, and returns the wrapper.

```python
def my_decorator(func):
    def wrapper():
        print("BEFORE")
        func()
        print("AFTER")

    return wrapper


@my_decorator
def greet():
    print("Hello!")


greet()
```

Output:

```text
BEFORE
Hello!
AFTER
```

### 3.1 What Does `@my_decorator` Mean?

This:

```python
@my_decorator
def greet():
    print("Hello!")
```

Is conceptually equivalent to:

```python
def greet():
    print("Hello!")


greet = my_decorator(greet)
```

Python passes the original function to the decorator and assigns the returned function to the name `greet`.

After decoration, calling `greet()` invokes the returned wrapper.

### 3.2 Why Return the Wrapper?

Correct:

```python
def my_decorator(func):
    def wrapper():
        func()

    return wrapper
```

Incorrect for this pattern:

```python
def my_decorator(func):
    def wrapper():
        func()

    return wrapper()
```

The second version calls `wrapper()` immediately and returns its result. If `wrapper()` has no explicit return statement, its result is `None`.

As a result, the decorated function name may become bound to `None` rather than to a callable function.

**Remember:** `return wrapper` returns the function object. `return wrapper()` executes the function immediately.

---

## 4. Supporting Arguments with `*args` and `**kwargs`

A wrapper that accepts no arguments only works with functions that also need no arguments.

Consider this decorator:

```python
def my_decorator(func):
    def wrapper():
        func()

    return wrapper


@my_decorator
def add(a, b):
    return a + b


print(add(10, 20))
```

This raises a `TypeError` because the wrapper cannot accept the two arguments passed to `add()`.

### Correct Implementation

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result

    return wrapper


@my_decorator
def add(a, b):
    return a + b


print(add(10, 20))
```

Output:

```text
30
```

### What Do `*args` and `**kwargs` Do?

- `*args` collects positional arguments into a tuple.
- `**kwargs` collects keyword arguments into a dictionary.
- Passing `*args` and `**kwargs` to `func()` forwards the collected arguments to the original function.

For example:

```python
def wrapper(*args, **kwargs):
    return func(*args, **kwargs)
```

This makes the wrapper flexible enough to support many different function signatures.

### Preserve the Return Value

Always consider whether the original function returns a value.

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result

    return wrapper
```

Without `return result`, the wrapper would return `None`, even if the original function returned a value.

---

## 5. Using `functools.wraps`

A decorator replaces the original function name with the returned wrapper function. Without additional handling, metadata such as the function's name and docstring may refer to the wrapper.

### Without `wraps`

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@my_decorator
def greet():
    """Display a greeting."""
    print("Hello!")


print(greet.__name__)
print(greet.__doc__)
```

Output:

```text
wrapper
None
```

### With `wraps`

```python
from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@my_decorator
def greet():
    """Display a greeting."""
    print("Hello!")


print(greet.__name__)
print(greet.__doc__)
```

Output:

```text
greet
Display a greeting.
```

### Why Use `@wraps(func)`?

`functools.wraps` preserves important metadata from the original function, including its name and docstring. It also sets the wrapper's `__wrapped__` attribute to the original function.

Use `@wraps(func)` in custom decorators as a good default practice.

---

## 6. Parameterized Decorators

A parameterized decorator accepts configuration, such as a repetition count, before receiving the function to decorate.

Example:

```python
@repeat(3)
def greet():
    print("Hello!")
```

Calling `greet()` should print `Hello!` three times.

A normal decorator receives the function directly. A parameterized decorator introduces another function level to receive its configuration first.

### 6.1 Implementation

```python
from functools import wraps


def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(3)
def greet():
    print("Hello!")


greet()
```

Output:

```text
Hello!
Hello!
Hello!
```

### 6.2 Understand the Three Function Levels

```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)

        return wrapper

    return decorator
```

- `repeat(n)` receives the decorator configuration.
- `decorator(func)` receives the original function.
- `wrapper(*args, **kwargs)` executes the original function when the decorated function is called.

Each function has a different responsibility.

### 6.3 How Python Applies `@repeat(3)`

Consider:

```python
@repeat(3)
def greet():
    print("Hello!")
```

This is conceptually equivalent to:

```python
def greet():
    print("Hello!")


greet = repeat(3)(greet)
```

The process is:

1. `repeat(3)` executes and returns `decorator`.
2. `decorator(greet)` receives the original function and returns `wrapper`.
3. Python binds the name `greet` to the returned wrapper.
4. When `greet()` is called, the wrapper executes the original function three times.

The repetition does not happen merely because the decorator is applied. It happens when the decorated function is called.

### 6.4 Why Do We Need `wrapper`?

Suppose the decorator called `func()` three times directly inside `decorator(func)`.

Those calls would happen when the decorator is applied, rather than every time the decorated function is called.

The wrapper delays execution until the decorated function is invoked.

This distinction is especially important when writing decorators that control execution timing.

### 6.5 A Note About Return Values

The previous `repeat` implementation intentionally ignores the return value of `func()` and returns `None`.

That is suitable for a simple example where `greet()` only prints text. However, a decorator intended for general-purpose functions must decide what return-value behavior it should provide.

For example, if the wrapped function returns a value, repeatedly calling it raises a design question: which result should the wrapper return?

There is no universal answer; it depends on the decorator's intended behavior.

---

## 7. Decorator Execution Timeline

Consider:

```python
def my_decorator(func):
    print("Applying decorator")

    def wrapper():
        print("Calling function")
        func()

    return wrapper


@my_decorator
def greet():
    print("Hello!")


print("Starting")
greet()
```

Output:

```text
Applying decorator
Starting
Calling function
Hello!
```

Why?

- `Applying decorator` prints when Python applies the decorator during function definition.
- `Starting` prints afterward, when normal top-level execution reaches that statement.
- `Calling function` and `Hello!` print when `greet()` invokes the wrapper.

**Key distinction:** Applying a decorator and calling a decorated function are separate events.

---

## 8. Common Mistakes

### Mistake 1: Passing a Function Call Instead of the Function

Incorrect:

```python
decorated = repeat(3)(greet())
```

Correct:

```python
decorated = repeat(3)(greet)
```

The incorrect version executes `greet()` first and passes its return value to the decorator. The correct version passes the function object itself.

### Mistake 2: Returning `wrapper()` Instead of `wrapper`

Incorrect:

```python
return wrapper()
```

Correct:

```python
return wrapper
```

The first executes the wrapper immediately. The second returns the callable function.

### Mistake 3: Forgetting Wrapper Arguments

If the original function accepts arguments, a zero-argument wrapper will not work when those arguments are passed through the decorated function.

For a flexible wrapper, use:

```python
def wrapper(*args, **kwargs):
    return func(*args, **kwargs)
```

### Mistake 4: Forgetting to Return the Original Result

If the original function returns a value, the wrapper should usually return that value too:

```python
def wrapper(*args, **kwargs):
    result = func(*args, **kwargs)
    return result
```

### Mistake 5: Forgetting `functools.wraps`

Without `@wraps(func)`, introspection may show the wrapper's metadata instead of the original function's metadata.

---

## 9. Decorators in FastAPI

Decorators are not just a Python language exercise. They are used extensively in frameworks.

For example:

```python
@app.get("/users")
def get_users():
    return [{"id": 1, "name": "Alex"}]
```

Here, `@app.get("/users")` is a decorator expression used by FastAPI to register the function as a handler for the specified route.

The exact behavior is implemented by FastAPI; it is not the same as the custom `repeat` decorator. But the function-passing and decoration concepts are directly relevant.

Other examples you may encounter include:

- `@app.post("/users")`
- `@classmethod`
- `@staticmethod`
- `@property`
- `@field_validator(...)` in Pydantic

You do not need to implement all these decorators yourself to use them effectively.

---

## 10. Quick Revision Checklist

Before moving on, make sure you can explain:

- [ ] The difference between `func` and `func()`.
- [ ] How a function can be passed as an argument and returned from another function.
- [ ] Why a basic decorator returns a wrapper function.
- [ ] Why `return wrapper` differs from `return wrapper()`.
- [ ] Why `*args` and `**kwargs` are useful in wrappers.
- [ ] Why decorators should preserve return values when appropriate.
- [ ] What `functools.wraps` does.
- [ ] Why `@repeat(3)` needs an additional function level.
- [ ] When the decorator is applied versus when the wrapped function executes.

## Summary

A decorator lets you add behavior around a function without rewriting the function itself.

For a basic decorator:

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper
```

For a parameterized decorator:

```python
def decorator_factory(option):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    return decorator
```

Remember the mental model:

- **Decorator factory:** receives configuration.
- **Decorator:** receives the original function.
- **Wrapper:** controls execution when the decorated function is called.

# Decorators in Python

## 1. What Is a Decorator?

- A decorator is a function that takes another function, adds or modifies its behavior, and returns a function.
- Decorators allow us to add functionality without modifying the original function's implementation.
- Common use cases:
  - Logging
  - Measuring execution time
  - Authentication and authorization
  - Caching
  - Validation
  - Registering API routes in FastAPI

### Example

```python
def my_decorator(func):
    def wrapper():
        print("Before execution")
        func()
        print("After execution")

    return wrapper


def greet():
    print("Hello!")


greet = my_decorator(greet)
greet()
```

Output:

```text
Before execution
Hello!
After execution
```

- `my_decorator` receives `greet` as an argument.
- It returns `wrapper`, which adds behavior before and after calling `greet`.
- The name `greet` now refers to the returned wrapper.

---

## 2. Functions Are First-Class Objects

- Python functions are objects.
- This means we can:
  - Assign functions to variables.
  - Pass functions as arguments.
  - Return functions from other functions.

### 2.1 Assigning a Function to a Variable

```python
def greet():
    print("Hello!")


say_hello = greet
say_hello()
```

Output:

```text
Hello!
```

- `say_hello = greet`
  - Assigns the function object to another variable.
  - Does not execute the function.
- `say_hello()`
  - Executes the function.

### 2.2 Passing a Function as an Argument

```python
def greet():
    print("Hello!")


def execute(func):
    func()


execute(greet)
```

Output:

```text
Hello!
```

- `execute(greet)`
  - Passes the function object to `execute`.
- `func()`
  - Executes the function received as an argument.

### 2.3 Returning a Function

```python
def greet():
    print("Hello!")


def get_function():
    return greet


result = get_function()
result()
```

Output:

```text
Hello!
```

- `return greet`
  - Returns the function object.
- `return greet()`
  - Executes the function and returns its result.
- This distinction is fundamental to understanding decorators.

---

## 3. Basic Decorator Structure

- A basic decorator:
  - Receives a function.
  - Defines a wrapper function.
  - Returns the wrapper function.

### Example

```python
def my_decorator(func):
    def wrapper():
        print("BEFORE")
        func()
        print("AFTER")

    return wrapper


@my_decorator
def greet():
    print("Hello!")


greet()
```

Output:

```text
BEFORE
Hello!
AFTER
```

### 3.1 Understanding `@my_decorator`

- This syntax:

```python
@my_decorator
def greet():
    print("Hello!")
```

- Is conceptually equivalent to:

```python
def greet():
    print("Hello!")


greet = my_decorator(greet)
```

- Python applies the decorator when it executes the function definition.
- The decorator receives the original function.
- The returned function is assigned to the name `greet`.
- Calling `greet()` subsequently invokes the wrapper.

### 3.2 Why Return `wrapper`?

- Correct:

```python
return wrapper
```

- Returns the function object.
- Does not execute the wrapper immediately.

- Incorrect for this pattern:

```python
return wrapper()
```

- Executes the wrapper immediately.
- Returns its result instead of returning the wrapper itself.
- If the wrapper has no explicit return statement, the result is `None`.

**Key point:** `wrapper` is a function reference; `wrapper()` is a function call.

---

## 4. Supporting Arguments with `*args` and `**kwargs`

- A wrapper without parameters only supports functions that can be called without arguments.

### Incorrect Example

```python
def my_decorator(func):
    def wrapper():
        func()

    return wrapper


@my_decorator
def add(a, b):
    return a + b


print(add(10, 20))
```

- This raises a `TypeError` because the wrapper does not accept the arguments passed to `add`.

### Correct Example

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result

    return wrapper


@my_decorator
def add(a, b):
    return a + b


print(add(10, 20))
```

Output:

```text
30
```

### Understanding the Arguments

- `*args`
  - Collects positional arguments into a tuple.
- `**kwargs`
  - Collects keyword arguments into a dictionary.
- `func(*args, **kwargs)`
  - Passes the collected arguments to the original function.
- `return result`
  - Preserves the original function's return value.

### Why Preserve the Return Value?

- A decorator should usually preserve the behavior of the original function unless changing it is intentional.
- If the wrapper calls `func()` but does not return its result, the decorated function may return `None`.

---

## 5. Preserving Metadata with `functools.wraps`

- Without `functools.wraps`, the decorated function can expose the wrapper's metadata instead of the original function's metadata.

### 5.1 Without `wraps`

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@my_decorator
def greet():
    """Display a greeting."""
    print("Hello!")


print(greet.__name__)
print(greet.__doc__)
```

Output:

```text
wrapper
None
```

- `greet.__name__` reports `wrapper`.
- `greet.__doc__` reports `None`.

### 5.2 With `wraps`

```python
from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@my_decorator
def greet():
    """Display a greeting."""
    print("Hello!")


print(greet.__name__)
print(greet.__doc__)
```

Output:

```text
greet
Display a greeting.
```

- `@wraps(func)` preserves important metadata from the original function.
- It also sets the wrapper's `__wrapped__` attribute to the original function.
- Using `@wraps(func)` is a good default practice when implementing custom decorators.

---

## 6. Parameterized Decorators

- A parameterized decorator accepts configuration before receiving the function.
- For example:

```python
@repeat(3)
def greet():
    print("Hello!")
```

- Calling `greet()` should print `Hello!` three times.
- A regular decorator receives the function directly.
- A parameterized decorator needs an additional function level to receive its configuration.

### 6.1 Implementation

```python
from functools import wraps


def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(3)
def greet():
    print("Hello!")


greet()
```

Output:

```text
Hello!
Hello!
Hello!
```

### 6.2 Understanding the Three Function Levels

- `repeat(n)`
  - Receives the configuration, such as the repetition count.
  - Returns the decorator function.
- `decorator(func)`
  - Receives the original function.
  - Returns the wrapper function.
- `wrapper(*args, **kwargs)`
  - Executes when the decorated function is called.
  - Calls the original function `n` times.

### 6.3 How `@repeat(3)` Works

- This:

```python
@repeat(3)
def greet():
    print("Hello!")
```

- Is conceptually equivalent to:

```python
def greet():
    print("Hello!")


greet = repeat(3)(greet)
```

- Execution sequence:
  1. `repeat(3)` executes and returns `decorator`.
  2. `decorator(greet)` receives the original function and returns `wrapper`.
  3. The name `greet` is bound to the returned wrapper.
  4. Calling `greet()` executes the wrapper.
  5. The wrapper calls the original function three times.

### 6.4 Why Do We Need `wrapper`?

- Without the wrapper, repeated calls could happen while the decorator is being applied.
- The wrapper delays execution until the decorated function is actually called.
- This allows every call to `greet()` to trigger the repeated behavior.

### 6.5 Parameterized Decorator Mental Model

```text
repeat(3)
    |
    v
decorator(func)
    |
    v
wrapper(*args, **kwargs)
    |
    v
Execute the original function 3 times
```

- The outer function handles configuration.
- The middle function receives the original function.
- The inner function controls execution.

### 6.6 Return-Value Consideration

- The example above calls the original function repeatedly but does not return its result.
- This is fine for a simple printing example.
- For a general-purpose decorator, decide what the wrapper should return.
- If the original function returns a value, repeating it raises a design question: should the wrapper return the first result, the last result, or all results?
- The correct choice depends on the decorator's intended behavior.

---

## 7. Decorator Application vs Function Execution

Consider:

```python
def my_decorator(func):
    print("Applying decorator")

    def wrapper():
        print("Calling function")
        func()

    return wrapper


@my_decorator
def greet():
    print("Hello!")


print("Starting")
greet()
```

Output:

```text
Applying decorator
Starting
Calling function
Hello!
```

- `Applying decorator`
  - Prints when Python applies the decorator during function definition.
- `Starting`
  - Prints during normal top-level execution.
- `Calling function`
  - Prints when `greet()` invokes the wrapper.
- `Hello!`
  - Prints when the wrapper calls the original function.

**Key distinction:** Applying a decorator and calling a decorated function are two separate events.

---

## 8. Common Mistakes

### 8.1 Passing a Function Call Instead of the Function

- Incorrect:

```python
decorated = repeat(3)(greet())
```

- Correct:

```python
decorated = repeat(3)(greet)
```

- `greet()` executes the function immediately and passes its return value.
- `greet` passes the function object itself.

### 8.2 Returning `wrapper()` Instead of `wrapper`

- Incorrect:

```python
return wrapper()
```

- Correct:

```python
return wrapper
```

- The first executes the wrapper immediately.
- The second returns a callable function.

### 8.3 Forgetting Wrapper Arguments

- If the original function accepts arguments, a zero-argument wrapper may raise a `TypeError`.
- Use `*args` and `**kwargs` when the wrapper needs to support different function signatures.

### 8.4 Forgetting to Return the Original Result

- Incorrect when preserving the result is required:

```python
def wrapper(*args, **kwargs):
    func(*args, **kwargs)
```

- Correct:

```python
def wrapper(*args, **kwargs):
    return func(*args, **kwargs)
```

### 8.5 Forgetting `functools.wraps`

- Without `@wraps(func)`, function metadata may refer to the wrapper.
- Use `@wraps(func)` to preserve important metadata.

---

## 9. Decorators in FastAPI

- Decorators are used extensively in Python frameworks.
- Example:

```python
@app.get("/users")
def get_users():
    return [{"id": 1, "name": "Alex"}]
```

- `@app.get("/users")` registers the function as a handler for the specified route.
- FastAPI implements the actual registration behavior.
- The Python concepts involved are still relevant:
  - Functions are objects.
  - Functions can be passed to other functions.
  - Decorators can configure or register behavior.
- Other decorators you may encounter:
  - `@app.post("/users")`
  - `@classmethod`
  - `@staticmethod`
  - `@property`
  - `@field_validator(...)` in Pydantic

---

## 10. Practice Questions

### Question 1: Basic Decorator

- Create a decorator that prints `Before`, executes the original function, and prints `After`.
- Apply it to a function that prints `Hello`.

Expected output:

```text
Before
Hello
After
```

### Question 2: Function Arguments

- Create a decorator that works with a function accepting two positional arguments.
- Apply it to an `add(a, b)` function that returns their sum.
- Ensure the result is preserved.

Expected output:

```text
30
```

### Question 3: Metadata

- Create a decorator using `functools.wraps`.
- Apply it to a function with a docstring.
- Print the decorated function's name and docstring.

Expected output:

```text
greet
Display a greeting.
```

### Question 4: Parameterized Decorator

- Implement `repeat(n)`.
- Apply it to a function that prints `Python`.
- Call the decorated function with a repetition count of four.

Expected output:

```text
Python
Python
Python
Python
```

### Question 5: Execution Order

- Create a decorator that prints `Decorating` when applied.
- Its wrapper should print `Executing` when called.
- Print `Starting` between the function definition and the function call.

Expected output:

```text
Decorating
Starting
Executing
```

---

## 11. Summary

- A decorator receives a function and returns a function that adds or changes behavior.
- `@my_decorator` is conceptually equivalent to `my_function = my_decorator(my_function)`.
- `return wrapper` returns the function; `return wrapper()` executes it immediately.
- `*args` and `**kwargs` allow wrappers to forward positional and keyword arguments.
- `functools.wraps` preserves important function metadata.
- A parameterized decorator uses three levels:
  - Outer function: receives configuration.
  - Decorator function: receives the original function.
  - Wrapper function: controls execution.
- Decorators are used in FastAPI for route registration and throughout the Python ecosystem.
- You do not need to master every decorator pattern before learning FastAPI. Revisit these concepts when you encounter them in practical code.
