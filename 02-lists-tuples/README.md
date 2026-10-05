# Day 2 — Lists & Tuples

## Overview

Day 2 focuses on Python's two core sequence types:

- `list` — mutable, dynamic collection
- `tuple` — immutable, fixed collection

---

# 1. Lists

A list is an ordered, mutable collection.

```python
numbers = [10, 20, 30, 40, 50]
```

Lists support:

- Indexing
- Negative indexing
- Slicing
- Mutation
- Dynamic resizing
- Iteration
- Comprehensions

---

# 2. List Slicing

General syntax:

```python
sequence[start:stop:step]
```

The `stop` index is excluded.

```python
numbers = [10, 20, 30, 40, 50, 60]

numbers[1:4]
# [20, 30, 40]
```

### Common forms

```python
numbers[:3]     # first 3 elements
numbers[3:]     # from index 3 to the end
numbers[::2]    # every second element
numbers[::-1]   # reverse traversal
```

The two-colon form:

```python
sequence[start:stop:step]
```

The second `:` separates the optional `step`.

---

# 3. Slice Assignment

A slice can be assigned to:

```python
numbers = [10, 20, 30, 40, 50]

numbers[1:4] = [200, 300]

print(numbers)
# [10, 200, 300, 50]
```

The selected slice is replaced completely.

The replacement does not need to have the same number of elements.

```python
numbers = [10, 20, 30, 40, 50, 60]

numbers[1:3] = [100, 200, 300, 400]

print(numbers)
# [10, 100, 200, 300, 400, 40, 50, 60]
```

So:

```python
numbers[start:stop] = values
```

means:

> Select the slice using normal slicing rules and replace it with the supplied values.

---

# 4. List Mutation Methods

Common mutating methods:

```python
numbers.append(40)
numbers.extend([50, 60])
numbers.insert(1, 15)
numbers.pop()
numbers.pop(1)
numbers.remove(30)
numbers.clear()
```

## `append()`

Adds one element:

```python
numbers = [1, 2]

numbers.append(3)

# [1, 2, 3]
```

Even if the value is another list, it becomes one element:

```python
numbers.append([4, 5])

# [1, 2, 3, [4, 5]]
```

## `extend()`

Adds each element from an iterable:

```python
numbers = [1, 2]

numbers.extend([3, 4])

# [1, 2, 3, 4]
```

Rough JavaScript comparison:

```javascript
array.push(x)
array.push(...items)
```

---

# 5. Removing Elements

## `pop()`

Removes by index and returns the removed element.

```python
numbers = [10, 20, 30]

value = numbers.pop(1)

print(value)
# 20

print(numbers)
# [10, 30]
```

Without an index, it removes the last element:

```python
numbers.pop()
```

## `remove()`

Removes by value.

```python
numbers = [10, 20, 30, 20]

numbers.remove(20)

# [10, 30, 20]
```

Only the first matching value is removed.

## `del`

Deletes by index or slice:

```python
del numbers[1]
```

```python
del numbers[1:3]
```

## `clear()`

Removes everything:

```python
numbers.clear()

# []
```

### Summary

```text
pop(index)  → remove by index + return removed value
remove(x)   → remove first matching value
del         → delete index/slice
clear()     → remove everything
```

---

# 6. `sort()` vs `sorted()`

## `list.sort()`

Mutates the original list and returns `None`.

```python
numbers = [40, 10, 30, 20]

result = numbers.sort()

print(numbers)
# [10, 20, 30, 40]

print(result)
# None
```

## `sorted()`

Returns a new sorted list without modifying the original.

```python
numbers = [40, 10, 30, 20]

result = sorted(numbers)

print(numbers)
# [40, 10, 30, 20]

print(result)
# [10, 20, 30, 40]
```

Important distinction:

```text
.sort()  → mutates original
sorted() → creates/returns a new sorted result
```

`sorted()` works with any iterable, not only lists.

---

# 7. List Comprehensions

A list comprehension provides a compact way to create a list.

Normal approach:

```python
numbers = [1, 2, 3, 4, 5]

squares = []

for number in numbers:
    squares.append(number * number)
```

List comprehension:

```python
squares = [number * number for number in numbers]
```

General syntax:

```python
[result for item in iterable]
```

It is conceptually similar to `map()` for simple transformations.

JavaScript:

```javascript
numbers.map(number => number * number)
```

Python:

```python
[number * number for number in numbers]
```

---

# 8. Conditions in List Comprehensions

A condition can be added:

```python
numbers = [1, 2, 3, 4, 5, 6]

even_squares = [
    number * number
    for number in numbers
    if number % 2 == 0
]

# [4, 16, 36]
```

General syntax:

```python
[result for item in iterable if condition]
```

Multiple conditions are allowed:

```python
[
    number * number
    for number in numbers
    if number % 2 == 0 and number > 2
]
```

Normal boolean operators work:

```python
and
or
not
```

Python also has built-in `map()` and `filter()`, but list comprehensions are often more idiomatic for straightforward list creation.

---

# 9. Tuple Unpacking in Comprehensions

Tuples can be unpacked directly inside a comprehension.

```python
users = [
    ("Avishek", 28, True),
    ("Rahul", 31, False),
    ("Priya", 25, True),
    ("Amit", 35, False),
]

active_users = [
    name
    for name, age, active in users
    if age < 30 and active
]

print(active_users)
# ["Avishek", "Priya"]
```

The tuple:

```python
("Avishek", 28, True)
```

is unpacked into:

```text
name   → "Avishek"
age    → 28
active → True
```

---

# 10. List Copying

Assignment does not create a new list:

```python
numbers = [1, 2, 3]

a = numbers

a.append(4)

print(numbers)
# [1, 2, 3, 4]
```

Both names reference the same list.

A shallow copy creates a new outer list:

```python
b = numbers.copy()
```

Slicing can also create a shallow copy:

```python
c = numbers[:]
```

For a flat list:

```python
numbers.copy()
numbers[:]
list(numbers)
```

all create a new list.

Nested objects are still shared in a shallow copy.

Deep-copy behavior was covered on:

**Day 1 — Shallow vs Deep Copy**

---

# 11. List Performance

Python lists are implemented as dynamic arrays.

Typical complexity:

| Operation | Complexity |
|---|---:|
| `numbers[index]` | O(1) |
| `numbers.append(x)` | O(1) amortized |
| `numbers.pop()` | O(1) |
| `numbers.insert(0, x)` | O(n) |
| `numbers.pop(0)` | O(n) |
| `x in numbers` | O(n) |

### Why is the beginning expensive?

For:

```python
numbers.insert(0, 100)
```

existing elements may need to be shifted:

```text
Before:
[10, 20, 30, 40]

After:
[100, 10, 20, 30, 40]
```

Therefore front insertion/removal is O(n).

For efficient queue operations, Python provides:

```python
from collections import deque
```

This will be covered later in the curriculum.

---

# 12. Tuples

A tuple is an ordered, immutable collection.

```python
numbers = (10, 20, 30, 40)
```

Indexing and slicing work similarly to lists:

```python
numbers[1]
numbers[1:3]
```

But mutation is not allowed:

```python
numbers[1] = 200
```

Results in:

```text
TypeError: 'tuple' object does not support item assignment
```

---

# 13. Tuple vs Rebinding

Immutable means the tuple object cannot be modified.

It does not mean the variable cannot be rebound.

```python
numbers = (10, 20, 30)

numbers = (10, 200, 30)
```

This is valid because a new tuple is being assigned to the name.

Similarly:

```python
a = (10,)

a = 20
```

is valid.

This is the same distinction from Day 1:

```text
Mutation  → changing the object
Rebinding → making a name reference another object
```

---

# 14. Tuple Creation and the Comma

Parentheses alone do not create a tuple.

```python
a = (10)

print(type(a))
# <class 'int'>
```

A comma creates the tuple:

```python
a = (10,)

print(type(a))
# <class 'tuple'>
```

This also works:

```python
a = 10,
```

The comma is what matters.

---

# 15. Tuple Packing

Multiple values can be packed into a tuple without parentheses:

```python
user = "Avishek", 28
```

Equivalent to:

```python
user = ("Avishek", 28)
```

---

# 16. Tuple Unpacking

A tuple can be unpacked into multiple variables:

```python
user = ("Avishek", 28)

name, age = user

print(name)
# Avishek

print(age)
# 28
```

Direct unpacking also works:

```python
name, age = ("Avishek", 28)
```

---

# 17. `*` Unpacking

`*` can collect remaining values:

```python
numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers
```

Result:

```text
first  → 10
middle → [20, 30, 40]
last   → 50
```

Notice that the collected values become a **list**.

Other examples:

```python
first, *rest = numbers
```

```text
first → 10
rest  → [20, 30, 40, 50]
```

And:

```python
*start, last = numbers
```

```text
start → [10, 20, 30, 40]
last  → 50
```

---

# 18. Tuple vs List

Use a list when the collection is expected to change:

```python
users = ["A", "B", "C"]
```

Use a tuple when the values form a fixed collection:

```python
coordinates = (20.29, 85.82)
```

However, if values have meaningful field names, a dictionary can be clearer:

```python
coordinates = {
    "x": 20.29,
    "y": 85.82
}
```

Tuple:

```python
coordinates[0]
coordinates[1]
```

Dictionary:

```python
coordinates["x"]
coordinates["y"]
```

Use a tuple when positional meaning is clear and the structure is small/fixed.

Use a dictionary when named fields make the data clearer.

---

# 19. Dunder Methods

Dunder means **double underscore**.

Examples:

```python
__init__
__str__
__len__
__eq__
__contains__
__getitem__
```

Python's normal syntax often invokes these methods internally.

For example:

```python
len(numbers)
```

uses the object's length protocol.

Similarly:

```python
numbers[0]
```

uses the object's item-access protocol.

Generally, application code should use normal Python syntax instead of calling dunder methods directly.

Prefer:

```python
num in numbers
```

over:

```python
numbers.__contains__(num)
```

Dunder methods will be covered properly in:

**Day 6 — Classes & OOP**

---

# 20. JavaScript / TypeScript Mapping

| Python | JavaScript / TypeScript |
|---|---|
| `list` | `Array` |
| `tuple` | No direct equivalent |
| `append()` | `push()` |
| `extend()` | `push(...items)` |
| `pop()` | `pop()` |
| `remove(x)` | Usually `findIndex()` + `splice()` |
| `sort()` | `sort()` |
| `sorted()` | `[...array].sort()` |
| List comprehension | `map()` / `filter()` combination |
| `x in list` | `array.includes(x)` |
| `list.copy()` | `[...array]` |
| Tuple unpacking | Array destructuring |
| `*rest` | `...rest` |

---

# Key Takeaways

1. Lists are mutable; tuples are immutable.
2. Slicing uses:
   ```python
   [start:stop:step]
   ```
3. `stop` is excluded.
4. Slice assignment can change the size of a list.
5. `append()` adds one element; `extend()` adds multiple elements.
6. `sort()` mutates; `sorted()` returns a new sorted result.
7. List comprehensions are a concise way to create lists.
8. Comprehensions can contain conditions.
9. Assignment creates another reference; `.copy()` creates a new outer list.
10. List random access and end operations are generally fast; front operations are O(n).
11. Tuples are immutable sequences.
12. Tuple packing/unpacking is heavily used in Python.
13. `*` can collect remaining unpacked values into a list.
14. Tuple vs dictionary depends on whether positional or named fields communicate the data better.
15. Dunder methods implement Python's object protocols and will be covered deeply on Day 6.

---

# Topics Deferred

Some topics were intentionally not covered deeply yet:

- `map()` / `filter()` internals → Day 10: Iterators & Generators
- Dunder methods and implementing them → Day 6: OOP
- `deque` → Day 9: Collections & Data Structures
- Deep copy → Day 1: Object Model
- Modules and imports → Day 16: Modules & Packages
- Lambda → Day 5: Functions

---

# Day 2 Status

**Completed**

Core understanding:

- Lists ✅
- Slicing ✅
- Slice assignment ✅
- Mutation methods ✅
- Sorting ✅
- List comprehensions ✅
- List copying ✅
- List performance ✅
- Tuples ✅
- Tuple unpacking ✅
- `*` unpacking ✅
- Practical list/tuple usage ✅
