# Day 4 — Strings, Bytes & JSON

## Goal

Build the Python knowledge needed to work with text, binary data, serialization, and eventually HTTP APIs/FastAPI.

For Day 4, the goal is **understanding the core concepts**, not memorizing every string/JSON method. More methods will be learned naturally while building APIs.

---

# 1. Strings

Python strings are:

- Ordered
- Indexable
- Sliceable
- Immutable

## Indexing

```python
name = "Avishek"

name[0]    # "A"
name[-1]   # "k"
```

First index:

```text
0
```

Last index:

```python
len(name) - 1
```

But negative indexing is usually cleaner:

```python
name[-1]
```

## Slicing

General syntax:

```python
sequence[start:stop:step]
```

- `start` → where to start
- `stop` → where to stop (excluded)
- `step` → how far to **jump** between indexes

Example:

```python
name = "Avishek"

name[::1]    # "Avishek"
name[::2]    # "Aihk"
name[::-1]   # "kehsivA"
```

Useful mental model:

> `step` is similar to the increment/decrement part of a traditional `for` loop.

For example:

```text
step = 1
0 → 1 → 2 → 3 → ...

step = 2
0 → 2 → 4 → 6 → ...

step = -1
6 → 5 → 4 → 3 → ...
```

## String immutability

Strings cannot be changed in place:

```python
name = "Avishek"

name[0] = "X"
```

This raises:

```text
TypeError: 'str' object does not support item assignment
```

To change a string, create a new string:

```python
name = "X" + name[1:]
```

---

# 2. Common String Operations

Core operations covered today:

```python
text.strip()
text.lower()
text.upper()
text.replace("old", "new")
text.find("value")
text.rfind("value")
text.split(",")
", ".join(values)
```

### JavaScript mental mapping

| JavaScript | Python |
|---|---|
| `trim()` | `strip()` |
| `indexOf()` | `find()` |
| `lastIndexOf()` | `rfind()` |
| `split()` | `split()` |
| `array.join()` | `separator.join(sequence)` |

### `find()` vs `index()`

```python
text.find("Python")
```

Returns `-1` if the value isn't found.

```python
text.index("Python")
```

Raises `ValueError` if the value isn't found.

For the JavaScript `indexOf()` mental model, use `find()`.

### `split()` and `join()`

```python
text = "python,fastapi,backend"

text.split(",")
```

Result:

```python
["python", "fastapi", "backend"]
```

Without a separator:

```python
"Python is great".split()
```

Result:

```python
["Python", "is", "great"]
```

`split()` without an argument splits on whitespace.

To get characters:

```python
list("Python")
```

Result:

```python
["P", "y", "t", "h", "o", "n"]
```

`join()` works in the opposite direction:

```python
words = ["python", "fastapi", "backend"]

", ".join(words)
```

Result:

```text
python, fastapi, backend
```

Important syntax:

```python
", ".join(words)
```

The **separator calls `join()`**.

---

# 3. F-Strings

F-strings are Python's convenient way to construct formatted strings.

```python
name = "Avishek"
age = 29

message = f"My name is {name} and I am {age} years old."
```

This is conceptually similar to JavaScript template literals:

```javascript
`My name is ${name} and I am ${age} years old.`
```

Expressions can also be used:

```python
a = 10
b = 20

print(f"Total: {a + b}")
```

Output:

```text
Total: 30
```

## Formatting values

```python
price = 1234.5678

print(f"Price: {price:.2f}")
```

Output:

```text
Price: 1234.57
```

Percentage formatting:

```python
percentage = 0.8567

print(f"Success rate: {percentage:.2%}")
```

Output:

```text
Success rate: 85.67%
```

Remember:

```text
:.2f → floating-point number with 2 decimal places
:.2% → percentage with 2 decimal places
```

---

# 4. Unicode

Unicode is **not the same thing as ASCII**.

ASCII is a subset of Unicode.

ASCII contains 128 characters with values from `0` to `127`.

Unicode covers a much larger set of characters, including characters such as:

```text
₹
é
中
😀
```

## `ord()` and `chr()`

`ord()` gives the Unicode code point of a character:

```python
ord("A")   # 65
ord("₹")   # 8377
ord("é")   # 233
```

`chr()` performs the reverse operation:

```python
chr(65)    # "A"
chr(8377)  # "₹"
```

Mental model:

```text
ord → character → number/code point
chr → number/code point → character
```

Important:

> For ASCII characters, the Unicode code point and ASCII value are the same.

---

# 5. Bytes

## `str` vs `bytes`

A Python string:

```python
text = "Hello"
```

is human-readable Unicode text.

A `bytes` object represents an immutable sequence of byte values.

```python
data = b"Hello"
```

Each element of `bytes` is an integer from `0` to `255`.

```python
data = b"Hello"

print(data[0])
```

Output:

```text
72
```

You can see all byte values:

```python
list(b"Hello")
```

Result:

```text
[72, 101, 108, 108, 111]
```

## Why does `H` become `72`?

For ASCII characters:

```text
H
↓
Unicode code point = 72
↓ UTF-8
byte value = 72
```

ASCII characters use the same numeric values in UTF-8 for this range.

---

## `bytes` vs `bytearray`

```text
bytes     → immutable sequence of bytes
bytearray → mutable sequence of bytes
```

Example:

```python
data = bytearray(b"Hello")

data[0] = 74

print(data)
```

Output:

```text
bytearray(b'Jello')
```

Java mental mapping:

```text
Java byte[]        → Python bytes (closest conceptual match)
mutable byte array → Python bytearray
```

The important distinction is that Python `bytes` is immutable.

---

# 6. Unicode vs UTF-8

This is one of the most important concepts from Day 4.

### Unicode

Unicode identifies **which character** we are dealing with.

Example:

```text
₹ → Unicode code point 8377
```

### UTF-8

UTF-8 defines **how that character is represented as bytes**.

Example:

```python
"₹".encode("utf-8")
```

The resulting bytes are:

```text
[226, 130, 185]
```

So:

```text
Unicode
   ↓
"Which character is this?"
   ↓
₹ = code point 8377

UTF-8
   ↓
"How do I represent this character as bytes?"
   ↓
₹ = [226, 130, 185]
```

The key distinction:

> **Unicode identifies the character; UTF-8 represents the character as bytes.**

---

# 7. Encoding and Decoding

## Encode

Convert Python text into bytes:

```python
text = "Hello"

data = text.encode("utf-8")
```

```text
str
 ↓ encode("utf-8")
bytes
```

Example:

```python
text = "₹"

data = text.encode("utf-8")

print(data)
```

Result:

```text
b'\xe2\x82\xb9'
```

## Decode

Convert bytes back into Python text:

```python
decoded = data.decode("utf-8")
```

```text
bytes
 ↓ decode("utf-8")
str
```

Overall flow:

```text
str
 ↓ encode("utf-8")
bytes
 ↓ decode("utf-8")
str
```

### Why bytes matter in backend development

Bytes are encountered when working with things such as:

- HTTP data
- Files
- Sockets
- Encryption
- Other external systems

We will explore the practical uses when we start building APIs.

---

# 8. JSON

JSON is a data interchange format commonly used by HTTP APIs.

Python provides the built-in `json` module.

```python
import json
```

## `json.dumps()`

Converts a Python object into a JSON string.

```python
user = {
    "name": "Avishek",
    "age": 29,
    "is_active": True
}

json_data = json.dumps(user)

print(json_data)
print(type(json_data))
```

Output:

```text
{"name": "Avishek", "age": 29, "is_active": true}
<class 'str'>
```

Important:

> `json.dumps()` produces a **Python string containing JSON**.

It does not produce a Python dictionary.

This process is called **serialization**.

---

## `json.loads()`

Converts a JSON string back into a Python object.

```python
parsed_user = json.loads(json_data)

print(parsed_user)
print(type(parsed_user))
```

Output:

```text
{'name': 'Avishek', 'age': 29, 'is_active': True}
<class 'dict'>
```

This is **deserialization**.

Mental model:

```text
Python dict
    ↓ json.dumps()
JSON string
    ↓ json.loads()
Python dict
```

---

# 9. `dump()` and `load()` — Files

The difference between the `s` and non-`s` versions is mainly the source/destination.

```text
dumps → Python object → JSON string
loads → JSON string → Python object

dump  → Python object → JSON file
load  → JSON file → Python object
```

Example:

```python
with open("user.json", "w") as file:
    json.dump(user, file)
```

Read it:

```python
with open("user.json", "r") as file:
    user = json.load(file)
```

Easy mental model:

> **`s` = string**

---

# 10. JSON Data Types and Python Limitations

JSON supports a smaller data model than Python.

Common mapping:

| Python | JSON |
|---|---|
| `dict` | object |
| `list` | array |
| `str` | string |
| `int` / `float` | number |
| `True` / `False` | `true` / `false` |
| `None` | `null` |

Not every Python object is directly JSON serializable.

For example:

```python
data = {
    "skills": {"Python", "TypeScript"}
}

json.dumps(data)
```

raises:

```text
TypeError: Object of type set is not JSON serializable
```

A Python `set` has no direct JSON representation.

You would typically convert it into a JSON-compatible structure such as a list:

```python
data = {
    "skills": list({"Python", "TypeScript"})
}
```

Important mental model:

> **A Python dictionary is not automatically a JSON object.**

Rather:

> A Python dictionary can be serialized into a JSON object when its contents are JSON-compatible.

---

# 11. Day 4 Backend Mental Model

## Text

```text
str
 ↓ encode("utf-8")
bytes
 ↓ decode("utf-8")
str
```

## JSON

```text
Python object
 ↓ json.dumps()
JSON string
 ↓ json.loads()
Python object
```

## JSON file

```text
Python object
 ↓ json.dump()
JSON file
 ↓ json.load()
Python object
```

## Character vs encoding

```text
Unicode → identifies the character
UTF-8   → represents the character as bytes
```

---

# What We Are NOT Memorizing Yet

We have intentionally covered the **core concepts**, not every available method.

You do not need to memorize every string method or every JSON option now.

As we move into:

- FastAPI
- HTTP requests/responses
- Pydantic
- API validation
- Authentication
- Database work
- File handling

we will learn the relevant methods naturally in their real context.

The goal is to understand the **Python model first**, then learn the APIs/methods while building real backend systems.
