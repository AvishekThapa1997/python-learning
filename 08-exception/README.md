# Day 8 — Exceptions & Context Managers

## Learning Goals

By the end of this module, you should be able to:
- Handle errors with `try`, `except`, `else`, and `finally`.
- Raise built-in and custom exceptions.
- Preserve the original cause when translating exceptions.
- Understand Python's exception hierarchy.
- Use context managers with `with` for reliable resource cleanup.
- Understand when `assert` is appropriate.

---

## 1. `try` and `except`

Use `try` for code that may raise an exception and `except` to handle a particular failure.

```python
try:
    number = int(input("Enter a number: "))
    result = 100 / number
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
```

- `ValueError` can occur when input cannot be converted to an integer.
- `ZeroDivisionError` occurs when dividing by zero.
- Prefer handling expected exceptions specifically instead of catching everything.

Python runs the first matching `except` block. Put specific exception types before broader ones. `ValueError` is a subclass of `Exception`, so a broad handler placed first would catch it before the specific handler.

Avoid a bare `except:` in ordinary application code because it also catches exceptions such as `KeyboardInterrupt` and `SystemExit`. `except Exception:` is generally the safer broad application-level handler.

---

## 2. `else` and `finally`

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Operation completed")
finally:
    print("Cleanup done")
```

- `else` runs only when the `try` block finishes without raising an exception.
- `finally` runs whether the operation succeeds or fails, including when the function returns.
- Keep success-only code in `else` when that makes the flow clearer.
- Use `finally` for cleanup that must happen regardless of success or failure.

### `return` and `finally`

A `return` inside `try` still allows `finally` to run before the function returns.

```python
def divide(a, b):
    try:
        return a / b
    finally:
        print("Cleanup done")
```

If `return` happens inside `try`, the `else` block does not run. Also, `return` can only be used inside a function.

### Scope note

Python does not create a separate local scope for `if`, `try`, `except`, `else`, `finally`, `for`, or `while` blocks. A variable assigned in a `try` block can be accessed later in the same function, provided execution actually assigned it.

---

## 3. Raising Exceptions

Use `raise` when code detects a condition it cannot or should not handle itself.

```python
def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")
    if amount > balance:
        raise ValueError("Insufficient balance")
    return balance - amount
```

`raise` is conceptually similar to `throw` in JavaScript/TypeScript.

---

## 4. Custom Exceptions

Create a custom exception when a specific failure deserves a clear name.

```python
class InsufficientBalanceError(Exception):
    pass
```

Then raise and handle it:

```python
def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError("Insufficient balance")
    return balance - amount

try:
    remaining = withdraw(1000, 1500)
except InsufficientBalanceError as error:
    print(error)
```

Conventions:
- Custom exception names usually end in `Error`.
- Inherit from `Exception` for normal application errors.
- `pass` is a no-op placeholder; it allows an otherwise empty class body.

---

## 5. Exception Chaining

When translating a low-level exception into a more meaningful application exception, preserve the original cause with `raise ... from ...`.

```python
class RepositoryError(Exception):
    pass

try:
    user_id = int("not-a-number")
except ValueError as error:
    raise RepositoryError("Failed to process user data") from error
```

This preserves the original exception as the cause, which helps debugging. JavaScript/TypeScript has a related concept using an error's `cause` property.

---

## 6. Exception Hierarchy

A simplified view:

```text
BaseException
├── Exception
│   ├── ValueError
│   ├── TypeError
│   ├── KeyError
│   ├── IndexError
│   ├── ZeroDivisionError
│   └── RuntimeError
├── KeyboardInterrupt
└── SystemExit
```

Most application exceptions inherit from `Exception`. `KeyboardInterrupt` and `SystemExit` are not ordinary application errors, which is another reason to avoid a bare `except:`.

---

## 7. Context Managers and `with`

A context manager manages setup and cleanup around a block of code. The `with` statement is commonly used for files, locks, database resources, and similar operations.

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

The file is closed when the `with` block exits, including when an exception occurs inside it.

A manual `try/finally` can achieve similar cleanup:

```python
file = open("notes.txt", "r", encoding="utf-8")
try:
    content = file.read()
finally:
    file.close()
```

### Context manager protocol

A context manager typically implements:
- `__enter__()` — runs when entering the `with` block and returns the value bound by `as`.
- `__exit__(exc_type, exc_value, traceback)` — runs when leaving the block, including when an exception occurs.

```python
class MyResource:
    def __enter__(self):
        print("Setup")
        return self

    def process(self):
        print("Processing")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Cleanup")
        # Returning False or None lets any exception propagate.
        return False

with MyResource() as resource:
    resource.process()
```

If the block succeeds, the three exception arguments passed to `__exit__` are `None`. If an exception occurs, they describe that exception.

Returning a truthy value from `__exit__` suppresses the exception; returning `False` or `None` allows it to propagate. Suppressing exceptions should be intentional.

---

## 8. `assert`

`assert` checks a condition that is expected to be true. If the condition is false, Python raises `AssertionError`.

```python
count = 3
assert count >= 0
```

Use assertions for tests and developer assumptions/invariants. **Do not use `assert` to validate untrusted input or enforce essential application rules**, because assertions can be disabled with optimized execution.

For tests, we will later learn `pytest`, which is a testing framework. `assert` is a Python statement, not a testing framework.

---

## 9. Practical Backend Connections

These concepts will appear again while building APIs:

- **Request validation:** handle or translate expected validation failures.
- **Service and repository layers:** raise meaningful exceptions and preserve causes.
- **API error handling:** convert application exceptions into appropriate HTTP responses.
- **Database transactions:** roll back or release resources when operations fail.
- **Files and connections:** use context managers to ensure cleanup.
- **Testing:** use assertions through a test framework such as `pytest`.

---

## 10. Practice Summary

### Practice 1 — Division

Write `divide(a, b)` that:
- attempts division;
- handles invalid numeric input separately from division by zero;
- returns the result on success;
- prints `Operation completed` only on success;
- always prints `Cleanup done`.

Expected success output:

```text
5.0
Operation completed
Cleanup done
```

Expected invalid-input output:

```text
Invalid input
Cleanup done
```

Expected zero-division output:

```text
Cannot divide by zero
Cleanup done
```

### Practice 2 — Account Withdrawal

Create a custom `InsufficientBalanceError` and an `Account` class with a balance and a withdrawal operation. Raise the custom exception when the requested amount exceeds the balance, and handle it in the caller.

Example successful output:

```text
Initial balance: 1000
Withdraw: 300
Remaining balance: 700
```

Example insufficient-balance output:

```text
Initial balance: 1000
Withdraw: 1500
Insufficient balance
```

### Practice 3 — Custom Context Manager

Create a `DatabaseConnection` context manager:
- print `Connecting to database` when entering;
- provide a `query()` method that prints `Executing query`;
- print `Closing database connection` when exiting;
- ensure the closing message appears even if an exception occurs inside the `with` block.

Expected successful output:

```text
Connecting to database
Executing query
Closing database connection
```

---

## Key Takeaways

- Catch expected exceptions specifically.
- `else` runs only after a successful `try`; `finally` runs during cleanup regardless of success or failure.
- `raise` signals an error; custom exceptions make application failures clearer.
- Use `raise NewError(...) from error` to preserve an underlying cause.
- Use `with` for reliable resource management.
- Use `assert` for assumptions and tests, not user-input validation.

## Next Module

**Day 9 — Iterables & Iterators**
