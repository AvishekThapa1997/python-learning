# Day 10 — Lambda and Functional Tools

## Learning goals

- Write short functions with `lambda`.
- Transform data with `map()` and select data with `filter()`.
- Understand `reduce()` and when a built-in function is clearer.
- Use `any()`, `all()`, `sorted()`, `enumerate()`, and `zip()`.
- Distinguish lists, list comprehensions, generator expressions, and lazy iterators.
- Recognize equivalent patterns in TypeScript and Python.

## 1. Lambda expressions

A `lambda` creates a small anonymous function containing **one expression**.

```python
double = lambda n: n * 2
add = lambda a, b: a + b

print(double(5))  # 10
print(add(3, 4))  # 7
```

A lambda can contain a conditional expression:

```python
transform = lambda n: n * 2 if n > 0 else 0
```

The syntax is `value_if_true if condition else value_if_false`, similar to the TypeScript ternary expression `condition ? valueIfTrue : valueIfFalse`.

A lambda cannot contain multiple statements such as an assignment followed by `return`. Use `def` for multi-step logic:

```python
def transform(n):
    result = n * 2
    return result
```

**Rule of thumb:** use `lambda` for short expressions and `def` for more involved logic.

## 2. `map()` — transform items

`map(function, iterable)` applies a function to each item and returns a **lazy map iterator**.

```python
numbers = [1, 2, 3, 4]
result = map(lambda n: n * 2, numbers)
print(list(result))  # [2, 4, 6, 8]
```

The result is not a list until you materialize it with something like `list()`.

### Lazy and one-time behavior

```python
prices = [100, 200, 300]
result = map(lambda price: price + 10, prices)

print(next(result))  # 110
print(next(result))  # 210
print(list(result))  # [310]
```

The two `next()` calls consume two results. The final list contains only the unconsumed result.

### `map()` with multiple iterables

`map()` can accept multiple iterables. It passes one item from each iterable as a separate argument to the function.

```python
names = ["Avishek", "Ravi", "Maya"]
scores = [90, 75, 88]

result = list(map(lambda name, score: (name, score), names, scores))
print(result)
# [('Avishek', 90), ('Ravi', 75), ('Maya', 88)]
```

If the iterables have different lengths, `map()` stops when the **shortest** iterable is exhausted:

```python
names = ["Avishek", "Ravi", "Maya"]
scores = [90, 75]

result = list(map(lambda name, score: (name, score), names, scores))
print(result)
# [('Avishek', 90), ('Ravi', 75)]
```

### Common mistake: `map()` with `zip()`

This fails:

```python
map(lambda name, score: (name, score), zip(names, scores))
```

`zip(names, scores)` yields one tuple per iteration, and `map()` passes that tuple as **one argument**. The lambda expects two arguments, so this raises `TypeError`.

This works because the lambda accepts one tuple:

```python
result = list(
    map(lambda name_score: (name_score[0], name_score[1]), zip(names, scores))
)
```

But it is redundant: the tuples are already in the desired format. Prefer:

```python
result = list(zip(names, scores))
```

If you want the lambda to receive two arguments, pass two iterables directly:

```python
result = list(map(lambda name, score: (name, score), names, scores))
```

### `map()` versus list comprehension

```python
numbers = [1, 2, 3, 4]

mapped = list(map(lambda n: n * 2, numbers))
comprehension = [n * 2 for n in numbers]

print(mapped)         # [2, 4, 6, 8]
print(comprehension)  # [2, 4, 6, 8]
```

Both produce the same values. `map()` returns a lazy iterator; a list comprehension creates a list immediately. For simple transformations, comprehensions are often easier to read in Python.

**TypeScript comparison:** `array.map(fn)` eagerly returns a new array. Python's `map(fn, iterable)` returns a lazy iterator.

## 3. `filter()` — select items

`filter(predicate, iterable)` yields only items for which the predicate returns a truthy value. It returns a lazy iterator.

```python
numbers = [1, 2, 3, 4, 5, 6]
result = filter(lambda n: n > 3, numbers)
print(list(result))  # [4, 5, 6]
```

`next()` consumes a value:

```python
numbers = [1, 2, 3, 4, 5, 6]
result = filter(lambda n: n % 2 == 0, numbers)

print(next(result))  # 2
print(list(result))  # [4, 6]
```

The first even number is consumed by `next()`, so it does not appear again in the remaining list.

### Filtering dictionaries

```python
users = [
    {"name": "Ravi", "active": True},
    {"name": "Anu", "active": False},
    {"name": "Maya", "active": True},
]

active_users = filter(lambda user: user["active"], users)
print(list(active_users))
# [{'name': 'Ravi', 'active': True}, {'name': 'Maya', 'active': True}]
```

A comprehension is often clearer when filtering and extracting values together:

```python
active_user_names = [
    user["name"] for user in users if user["active"]
]
print(active_user_names)  # ['Ravi', 'Maya']
```

## 4. List comprehensions versus generator expressions

Both can express transformations and filtering, and both can be passed to functions such as `sum()`, `any()`, and `all()`. The key difference is how results are produced and stored.

### List comprehension: creates a list

```python
numbers = [1, 2, 3, 4, 5]
squares_list = [n * n for n in numbers]
print(squares_list)  # [1, 4, 9, 16, 25]
```

The resulting list can be iterated over repeatedly.

### Generator expression: produces values lazily

```python
numbers = [1, 2, 3, 4, 5]
squares_generator = (n * n for n in numbers)

print(squares_generator)  # <generator object ...>
print(list(squares_generator))  # [1, 4, 9, 16, 25]
```

Values are produced as requested. A generator is a one-time iterator: once consumed, it does not restart.

### Both can be passed to the same function

```python
numbers = [1, 2, 3, 4, 5]

print(sum([n * 2 for n in numbers]))  # 30
print(sum(n * 2 for n in numbers))    # 30
```

The first creates an intermediate list. The second supplies values lazily to `sum()`.

### `any()` and `all()` consume iterators

- `any(iterable)` returns `True` when it finds a truthy item, then stops.
- `all(iterable)` returns `False` when it finds a falsy item, then stops.
- Both consume values from the iterable they receive.
- `any()` on an empty iterable returns `False`.
- `all()` on an empty iterable returns `True`.

**Generator gotcha:** reusing the same generator for multiple checks means the later check sees only the values that remain.

```python
users = [
    {"active": False},
    {"active": True},
]

active_values = (user["active"] for user in users)

print(any(active_values))  # True
print(all(active_values))  # True
```

`any()` has to consume both values (`False`, then `True`) to find a truthy value. The generator is now exhausted. `all()` receives an empty iterator, and `all()` of an empty iterable is `True`.

Create a fresh generator for each check:

```python
any_active = any(user["active"] for user in users)
all_active = all(user["active"] for user in users)
```

### Which should you choose?

| Situation | Often a good choice |
|---|---|
| Need a list of results or repeated iteration | List comprehension |
| Process values once without storing an intermediate list | Generator expression |
| Transform/filter simple data | Comprehension |
| Feed values directly to `sum()`, `any()`, or `all()` | Generator expression |
| Need a reusable snapshot of results | Materialize a list |

`map()`, `filter()`, generator expressions, and `enumerate()` produce iterators. List comprehensions produce lists.

## 5. `reduce()` — cumulative operations

`reduce()` is in the `functools` module:

```python
from functools import reduce

numbers = [1, 2, 3, 4]
result = reduce(lambda acc, n: acc + n, numbers)
print(result)  # 10
```

The accumulator (`acc`) carries the result from one iteration to the next. Without an initial value, `reduce()` uses the first item as the initial accumulator.

```python
from functools import reduce

numbers = [10, 3, 2]
result = reduce(lambda acc, n: acc - n, numbers)
print(result)  # 5
```

Steps: start with `10`, then `10 - 3 = 7`, then `7 - 2 = 5`.

### Supplying an initial value

```python
from functools import reduce

result = reduce(lambda acc, n: acc - n, [1, 2, 3], 10)
print(result)  # 4
```

The accumulator starts at `10`: `10 - 1 = 9`, `9 - 2 = 7`, `7 - 3 = 4`.

### Prefer built-ins for common operations

```python
numbers = [1, 2, 3, 4]

print(sum(numbers))        # 10
print(max(numbers))        # 4
print(min(numbers))        # 1
print(any([False, True]))  # True
print(all([True, True]))   # True
```

Use `reduce()` when a custom cumulative operation is genuinely needed. For ordinary sums, `sum()` is clearer.

## 6. `any()` and `all()` in backend logic

```python
permissions = ["read", "write", "delete"]
required_permissions = ["read", "write"]

has_all_permissions = all(
    permission in permissions
    for permission in required_permissions
)
print(has_all_permissions)  # True
```

If a required permission is missing:

```python
permissions = ["read", "write", "delete"]
required_permissions = ["read", "admin"]

print(all(permission in permissions for permission in required_permissions))
# False
```

- `any(...)`: at least one condition must be true.
- `all(...)`: every condition must be true.

Example: check whether any user is both active and verified, and whether all users are active:

```python
users = [
    {"name": "A", "active": True, "verified": True},
    {"name": "B", "active": True, "verified": False},
    {"name": "C", "active": False, "verified": True},
]

any_active_and_verified = any(
    user["active"] and user["verified"] for user in users
)
all_users_active = all(user["active"] for user in users)

print(any_active_and_verified)  # True
print(all_users_active)         # False
```

## 7. `sorted()` with `key=`

`sorted()` returns a **new list** and does not modify the original iterable.

```python
scores = [45, 90, 72, 60, 85]

result = sorted(scores, reverse=True)

print(result)  # [90, 85, 72, 60, 45]
print(scores)  # [45, 90, 72, 60, 85]
```

Use `key=` to tell Python which value to sort by:

```python
users = [
    {"name": "Ravi", "age": 32},
    {"name": "Anu", "age": 24},
    {"name": "Maya", "age": 28},
]

sorted_users = sorted(users, key=lambda user: user["age"])
print(sorted_users)
# [
#   {'name': 'Anu', 'age': 24},
#   {'name': 'Maya', 'age': 28},
#   {'name': 'Ravi', 'age': 32}
# ]
```

Sort by name instead:

```python
sorted_users = sorted(users, key=lambda user: user["name"])
```

Sort active users by age:

```python
users = [
    {"name": "Ravi", "age": 32, "active": True},
    {"name": "Anu", "age": 24, "active": False},
    {"name": "Maya", "age": 28, "active": True},
    {"name": "Raj", "age": 22, "active": True},
]

active_users = (user for user in users if user["active"])
sorted_users = sorted(active_users, key=lambda user: user["age"])
print(sorted_users)
# [
#   {'name': 'Raj', 'age': 22, 'active': True},
#   {'name': 'Maya', 'age': 28, 'active': True},
#   {'name': 'Ravi', 'age': 32, 'active': True}
# ]
```

The generator filters lazily, but `sorted()` must consume all selected items before it can return a sorted list.

## 8. `enumerate()` — index and value

`enumerate(iterable, start=0)` yields `(index, value)` tuples. It returns an iterator, not a list of tuples.

```python
tasks = ["Build API", "Write tests", "Deploy"]

result = enumerate(tasks, start=1)
print(type(result))  # <class 'enumerate'>

print(list(result))
# [(1, 'Build API'), (2, 'Write tests'), (3, 'Deploy')]
```

Usually, use it directly in a loop:

```python
for index, task in enumerate(tasks, start=1):
    print(f"{index}. {task}")
```

Output:

```text
1. Build API
2. Write tests
3. Deploy
```

**TypeScript comparison:**
- Python `enumerate(list)` is similar in purpose to JavaScript/TypeScript `array.entries()`.
- `list(enumerate(items))` materializes the iterator, similar to `Array.from(array.entries())`.
- Python `dict.items()` is closer to `Object.entries(object)` for dictionary key-value pairs.

## 9. `zip()` — pair items from iterables

`zip()` yields tuples containing corresponding items from each iterable.

```python
names = ["Avishek", "Ravi", "Maya"]
scores = [90, 75, 88]

print(list(zip(names, scores)))
# [('Avishek', 90), ('Ravi', 75), ('Maya', 88)]
```

For pairing values, `list(zip(names, scores))` is simpler than a comprehension that rebuilds each tuple:

```python
# Valid but unnecessary:
name_and_score = [(name, score) for name, score in zip(names, scores)]
```

By default, `zip()` stops when the shortest iterable runs out.

```python
names = ["Avishek", "Ravi", "Maya"]
scores = [90, 75]

print(list(zip(names, scores)))
# [('Avishek', 90), ('Ravi', 75)]
```

## 10. Chaining transformations: TypeScript vs Python

In TypeScript:

```typescript
const result = numbers
  .filter(n => n > 2)
  .map(n => n * 10)
  .reduce((acc, n) => acc + n, 0);
```

Python's built-in `filter()` and `map()` don't use the same array-method chaining syntax. You can nest calls:

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

result = reduce(
    lambda acc, n: acc + n,
    map(lambda n: n * 10, filter(lambda n: n > 2, numbers)),
    0,
)
print(result)  # 120
```

Or use intermediate variables:

```python
filtered = filter(lambda n: n > 2, numbers)
mapped = map(lambda n: n * 10, filtered)
result = sum(mapped)

print(result)  # 120
```

For this simple case, idiomatic Python is often clearer:

```python
numbers = [1, 2, 3, 4, 5]

result = sum(n * 10 for n in numbers if n > 2)
print(result)  # 120
```

The final example uses a generator expression, so it does not build an intermediate list.

## 11. Practice examples covered

### Filter and increase prices by 10%

```python
prices = [100, 250, 80, 400, 150]

filtered_prices = (price for price in prices if price >= 150)
transformed_prices = [price + price * 0.10 for price in filtered_prices]

print(transformed_prices)  # [275.0, 440.0, 165.0]
```

### Extract active user names

```python
users = [
    {"name": "Ravi", "active": True},
    {"name": "Anu", "active": False},
    {"name": "Maya", "active": True},
]

active_user_names = [
    user["name"] for user in users if user["active"]
]
print(active_user_names)  # ['Ravi', 'Maya']
```

### Filter, transform, and sum

```python
numbers = [1, 2, 3, 4, 5]

result = sum(num * 10 for num in numbers if num > 2)
print(result)  # 120
```

## 12. Quick reference

| Tool | Purpose | Result type / behavior |
|---|---|---|
| `lambda` | Define a short anonymous function | Function object; one expression |
| `map()` | Transform each item | Lazy iterator; supports multiple iterables |
| `filter()` | Select items by predicate | Lazy iterator |
| List comprehension | Transform/filter into a list | List, eager |
| Generator expression | Transform/filter lazily | One-time iterator |
| `reduce()` | Accumulate a custom operation | Final accumulated value |
| `sum()` | Sum values | Final numeric value |
| `any()` | Check whether at least one item is truthy | Boolean; short-circuits |
| `all()` | Check whether every item is truthy | Boolean; short-circuits |
| `sorted()` | Return sorted values | New list |
| `enumerate()` | Yield index-value pairs | Iterator of tuples |
| `zip()` | Pair corresponding values | Iterator of tuples |

## Practical rules to remember

1. Prefer `def` over `lambda` for multi-step logic.
2. Prefer comprehensions for simple filtering and transformation when they are clearer.
3. Use generator expressions to process values lazily without building an intermediate list.
4. Treat generators and other iterators as consumable; don't expect the same iterator to start over.
5. `map()` accepts multiple iterables and passes one value from each to the function on each iteration.
6. `map()` and `zip()` stop at the shortest iterable.
7. Use `sum()`, `any()`, and `all()` for common operations instead of forcing everything into `reduce()`.
8. Use `sorted(..., key=...)` to sort records by a selected field.
9. Use `enumerate()` when you need both an index and a value.
10. In straightforward Python code, readability matters more than using a functional tool just because it exists.

## Connection to FastAPI

These tools are useful when processing collections of records, filtering results, transforming values for response payloads, sorting records, checking permissions, and preparing data for API responses. In FastAPI, these concepts will be revisited in context rather than trying to master every functional-programming pattern in advance.
