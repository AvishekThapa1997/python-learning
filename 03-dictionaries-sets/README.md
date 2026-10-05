# Day 3 — Dictionaries & Sets

## Dictionaries

Python `dict` stores **key → value** pairs.

```python
user = {"id": 101, "name": "Avishek", "role": "Senior Engineer"}
```

### Lookup

```python
user["name"]       # key must exist
user.get("email")  # None if missing
user.get("email", "Not provided")
```

Missing `user["email"]` raises `KeyError`.

`dict.get(key, default)` uses the default only when the key is missing, not when the value is `None`.

### `None` checks

Prefer:

```python
if value is None:
    ...
```

over `if not value` when you specifically mean `None`.

Python falsy values include:

```text
None, False, 0, "", [], {}, (), set()
```

Unlike JavaScript, empty arrays and objects are falsy in Python.

### Hashing and dictionary keys

Dictionary keys must be **hashable**.

```python
hash("name")       # works
hash(10)           # works
hash((1, 2, 3))    # works
hash([1, 2, 3])    # TypeError
hash((1, [2, 3]))  # TypeError
```

A tuple is hashable only when all of its contents are hashable.

Dictionary values can be mutable:

```python
data = {
    "skills": ["Python", "SQL"],
    "profile": {"experience": 5.5},
}
```

### Add, update, delete

```python
user["role"] = "Engineer"  # add/update
del user["role"]           # delete
```

Missing `del user["missing"]` raises `KeyError`.

```python
age = user.pop("age")
email = user.pop("email", None)
```

`pop()` removes and returns a value.

```python
user.clear()
```

removes everything.

### Iteration

```python
for key in user:
    ...

for key in user.keys():
    ...

for value in user.values():
    ...

for key, value in user.items():
    ...
```

`keys()`, `values()`, and `items()` return live **view objects**, not snapshots.

```python
keys = user.keys()
user["age"] = 28
# keys now reflects "age"
```

Use `list(user.keys())` when a snapshot/list is needed.

### Nested dictionaries

```python
user = {
    "id": 101,
    "profile": {
        "role": "Senior Engineer",
        "country": "India",
    },
}

user["profile"]["role"]
```

Nested dictionaries are common with JSON/API data.

## Dictionary comprehensions

Simple transformation:

```python
numbers = [1, 2, 3, 4]

squares = {
    x: x * x
    for x in numbers
}
```

General form:

```python
{key: value for item in iterable}
```

Filter with a condition:

```python
active_users = {
    user["id"]: user
    for user in users
    if user["active"]
}
```

Multiple conditions work:

```python
{
    user["id"]: user
    for user in users
    if user["active"] and user["id"] > 100
}
```

`if` after the `for` filters items.

`if/else` before the `for` transforms the value:

```python
status = {
    user["id"]: "active" if user["active"] else "inactive"
    for user in users
}
```

Use comprehensions for simple transformations; use a normal loop when the logic becomes complex.

# Sets

A set stores **unique, hashable elements**.

```python
numbers = {1, 2, 3, 2, 4}
```

Duplicates are removed.

Convert a list to a set:

```python
unique_numbers = set(numbers)
```

A set has no positional indexing:

```python
numbers[0]  # TypeError
```

### Membership

```python
20 in numbers
```

Set membership is typically **O(1) average**.

### Mutation

```python
numbers.add(40)
numbers.remove(20)
numbers.discard(50)
numbers.clear()
```

`remove(x)` raises `KeyError` when `x` is missing.

`discard(x)` does nothing when `x` is missing.

Set elements must be hashable:

```python
skills.add("Redis")            # works
skills.add(("Redis", "Docker")) # works
skills.add(["Redis", "Docker"]) # TypeError
```

## Set operations

### Intersection

Common elements:

```python
a & b
a.intersection(b)
```

### Union

All unique elements:

```python
a | b
a.union(b)
```

### Difference

Elements in the left set but not the right:

```python
a - b
a.difference(b)
```

Order matters.

### Symmetric difference

Elements unique to either set, excluding common elements:

```python
a ^ b
a.symmetric_difference(b)
```

Mental model:

```text
A - B → only A
A ^ B → unique to either A or B
```

### Subset

Checks whether all elements of one set exist in another:

```python
required.issubset(user_permissions)
```

Equivalent:

```python
required <= user_permissions
```

### Superset

Reverse perspective:

```python
user_permissions.issuperset(required)
```

Equivalent:

```python
user_permissions >= required
```

### Disjoint

Checks whether two sets have no elements in common:

```python
frontend.isdisjoint(backend)
```

## Performance

Typical average-case complexity:

| Operation | List | Set | Dict |
|---|---:|---:|---:|
| Membership / lookup | O(n) | O(1) | O(1) |
| Add | O(1) amortized | O(1) | O(1) |
| Remove | O(n) | O(1) | O(1) |

Converting a list to a set is O(n):

```python
unique = set(numbers)
```

But subsequent membership checks are typically O(1) average.

So converting once can be useful when many membership checks are needed.

`*_update()` set methods were intentionally skipped as they are mutating variants of the operations above.

## List vs Set vs Dict

```text
List
→ ordered
→ duplicates allowed
→ indexing
→ good when order matters

Set
→ unique elements
→ no positional indexing
→ fast membership
→ good for uniqueness/membership

Dict
→ key → value
→ hashable keys
→ fast key lookup
→ good for keyed data
```

## Backend use cases

### Index users by ID

```python
users_by_id = {
    user["id"]: user
    for user in users
}
```

### Detect duplicates

```python
has_duplicates = len(set(emails)) != len(emails)
```

### Check permissions

```python
required.issubset(user_permissions)
```

### Find missing permissions

```python
required - user_permissions
```

### Find overlap

```python
admin_permissions & restricted_permissions
```

## JavaScript / TypeScript mapping

| Python | JavaScript / TypeScript |
|---|---|
| `dict` | object / `Map` |
| `list` | array |
| `set` | `Set` |
| `None` | roughly `null` |
| `dict.items()` | `Object.entries()` |
| `dict.keys()` | `Object.keys()` |
| `dict.values()` | `Object.values()` |

Python dictionary keys can be hashable values such as integers and tuples. JavaScript objects generally use string/symbol property keys; `Map` is closer when arbitrary key types are needed.

## Key takeaways

```text
1. dict stores key → value pairs.
2. Dictionary keys must be hashable.
3. dict[key] raises KeyError when missing.
4. dict.get(key) safely handles missing keys.
5. keys(), values(), and items() return live views.
6. Dictionary iteration defaults to keys.
7. Dictionary comprehensions create dictionaries concisely.
8. Sets store unique hashable elements.
9. Sets do not support positional indexing.
10. Set membership is O(1) average.
11. Dictionary key lookup is O(1) average.
12. list → set conversion is O(n).
13. & = intersection.
14. | = union.
15. - = difference.
16. ^ = symmetric difference.
17. issubset() checks containment of all elements.
18. issuperset() is the reverse perspective.
19. isdisjoint() checks for zero overlap.
20. Choose list, set, or dict based on the operations your code needs.
```

## Day 3 Status

**Complete.**

Covered dictionaries, hashing, lookup and mutation, iteration, nested data, comprehensions, sets, set operations, subset/superset/disjoint checks, performance, backend use cases, and JavaScript/TypeScript comparisons.
