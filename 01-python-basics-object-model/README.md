# Day 1 — Python Basics & Object Model

## 1. Python Data Types

| Python | Example | JS/TS rough equivalent |
|---|---|---|
| `int` | `42` | `number` |
| `float` | `42.5` | `number` |
| `complex` | `2 + 3j` | No common equivalent |
| `bool` | `True` | `boolean` |
| `str` | `"hello"` | `string` |
| `NoneType` | `None` | `null` |
| `list` | `[1, 2, 3]` | `Array` |
| `tuple` | `(1, 2, 3)` | No direct equivalent |
| `dict` | `{"name": "Avishek"}` | `Object` / `Map` |
| `set` | `{1, 2, 3}` | `Set` |
| `bytes` | `b"hello"` | `Uint8Array` / binary data |
| `bytearray` | `bytearray(...)` | Mutable binary buffer |

### Important differences

- Python `int` supports arbitrarily large integers natively.
- Python has `None`, but no separate `undefined`.
- `None` is a singleton and is conventionally checked with `is None`.

```python
if value is None:
    ...
```

---

## 2. Names, Objects & References

A Python variable is a **name bound to an object**.

```python
numbers = [10, 20, 30]
a = numbers
b = numbers
```

All three names refer to the same list object.

```text
numbers ──┐
a ────────┼──> [10, 20, 30]
b ────────┘
```

Assignment does not automatically create a copy.

---

## 3. `is` vs `==`

- `is` → object identity: are these the same object?
- `==` → equality: are these objects equal in value?

```python
a = [1, 2]
b = a
c = [1, 2]

a is b   # True
a is c   # False
a == c   # True
```

Common identity check:

```python
if value is None:
    ...
```

---

## 4. `id()`

`id()` exposes an identity value for an object during its lifetime.

```python
numbers = [1, 2, 3]
a = numbers

id(numbers) == id(a)  # True
numbers is a          # True
```

Normally use `is` for identity checks rather than comparing `id()` values directly.

JavaScript has no direct built-in equivalent of Python's `id()`.

---

## 5. Mutation vs Rebinding

### Mutation

Changes the existing object.

```python
numbers = [10, 20, 30]
numbers[0] = 100
```

### Rebinding

Makes a name refer to another object.

```python
numbers = [10, 20, 30]
numbers = [100, 200, 300]
```

For example:

```python
items = [10, 20, 30]
a = items
b = items

b[0] = 100
# items and a also see the change

b = [500, 600, 700]
# items and a remain unchanged
```

---

## 6. Mutable vs Immutable

### Mutable

The object can be modified after creation.

Common examples:

- `list`
- `dict`
- `set`
- `bytearray`

### Immutable

The object itself cannot be modified after creation.

Common examples:

- `int`
- `float`
- `bool`
- `str`
- `tuple`
- `None`

Important:

> Immutable does not mean the name cannot change.

```python
x = 10
x = 100
```

This rebinds `x`; it does not modify the integer object `10`.

---

## 7. Shallow vs Deep Copy

### Shallow copy

Creates a new outer object but keeps references to nested objects.

```python
import copy

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
```

Nested lists are shared.

### Deep copy

Recursively copies nested objects.

```python
deep = copy.deepcopy(original)
```

Nested objects are independent.

Rough JS/TS comparison:

```text
Python                    JavaScript
copy.copy()        ≈      {...obj} / [...array]
copy.deepcopy()    ≈      structuredClone()
```

The comparison is conceptual; cloning semantics are not identical for every type.

---

## 8. Function Arguments & Object References

Python uses **pass-by-object-reference / call-by-sharing** semantics.

A parameter is a local name referring to the passed object.

### Mutation is visible to the caller

```python
def change(numbers):
    numbers[0] = 100

values = [10, 20, 30]
change(values)

# values -> [100, 20, 30]
```

### Rebinding is not visible to the caller

```python
def change(numbers):
    numbers = [100, 200, 300]

values = [10, 20, 30]
change(values)

# values -> [10, 20, 30]
```

This is essentially the same reference/mutation behavior encountered in JavaScript/TypeScript.

---

## 9. Basic Python Syntax

### Conditional blocks

Python uses indentation instead of `{}`.

```python
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")
```

### `for` and `range`

```python
for i in range(5):
    print(i)
```

Produces:

```text
0
1
2
3
4
```

The upper bound is exclusive.

### `while`

```python
count = 0

while count < 3:
    print(count)
    count += 1
```

---

## 10. Functions

Basic syntax:

```python
def add(a, b):
    return a + b
```

Default arguments:

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}"
```

Keyword arguments:

```python
greet(name="Avishek", greeting="Hi")
```

### `*args` and `**kwargs`

```python
def example(*args, **kwargs):
    print(args)
    print(kwargs)
```

- `*args` collects positional arguments into a tuple.
- `**kwargs` collects keyword arguments into a dictionary.

---

## 11. f-Strings

Python f-strings are similar to JavaScript template literals.

```python
name = "Avishek"
message = f"Hello, {name}"
```

JS/TS equivalent:

```javascript
const message = `Hello, ${name}`;
```

---

## 12. List Comprehension — Introduction Only

List comprehensions were introduced but are covered in detail on **Day 2 — Lists & Tuples**.

```python
squares = [number * number for number in numbers]
```

Day 2 covers conditions, nesting, readability, and performance considerations.

---

## 13. Imports — Introduction Only

Python code is organized into modules.

```python
import math

math.sqrt(25)
math.floor(4.8)
math.ceil(4.2)
```

The full module/package/import system is covered on **Day 16 — Modules & Packages**.

---

## Deferred Topics

Some Day 1 topics intentionally depend on later modules:

- Detailed function argument behavior → reinforced on **Day 5 — Functions**
- List comprehensions → **Day 2 — Lists & Tuples**
- Module/package/import system → **Day 16 — Modules & Packages**
- Runtime details and memory model → **Day 11 — Python Runtime & OS**
- Concurrency and shared-state implications → **Days 11–15**
