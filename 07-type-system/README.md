# Day 7 — Python Type System + Type Hints

## Goal

Understand Python's type system well enough to write typed backend code and understand how type hints connect to static checking, runtime validation, Pydantic, and FastAPI.

## Topics Covered

### 1. Type Annotations

```python
def add(a: int, b: int) -> int:
    return a + b
```

Python type annotations are **not runtime validation** by themselves.

```python
def add(a: int, b: int) -> int:
    return a + b

print(add("10", "20"))
```

Output:

```text
1020
```

Type annotations mainly provide information for developers, IDEs, and static type checkers.

### 2. Built-in Generic Types

```python
list[str]
dict[str, int]
tuple[int, str]
set[str]
```

Nested types are possible:

```python
def get_scores() -> dict[str, list[int]]:
    return {
        "Avishek": [80, 90, 95],
        "John": [70, 85, 88]
    }
```

Conceptually similar to TypeScript:

```typescript
string[]
Record<string, number[]>
```

### 3. Union Types

Python uses `|`:

```python
str | None
int | str | None
```

Example:

```python
def get_name(user_id: int) -> str | None:
    if user_id == 1:
        return "Avishek"
    return None
```

`None` is closest to TypeScript's `null`. Python has no direct equivalent of JavaScript's `undefined`.

### 4. Literal

`Literal` describes a specific set of allowed values:

```python
from typing import Literal

def set_method(method: Literal["GET", "POST", "PUT"]):
    print(method)
```

Conceptually similar to TypeScript:

```typescript
type Method = "GET" | "POST" | "PUT";
```

`Literal` is still a type hint and does not automatically perform runtime validation.

### 5. TypedDict

`TypedDict` describes the expected structure of a dictionary:

```python
from typing import TypedDict

class User(TypedDict):
    name: str
    email: str
```

A value is still a normal dictionary at runtime:

```python
user = {
    "name": "Avishek",
    "email": "abc@yopmail.com"
}

print(type(user))
# <class 'dict'>
```

Access is:

```python
user["name"]
user["email"]
```

rather than:

```python
user.name
```

### 6. Protocol

`Protocol` provides a structural typing contract:

```python
from typing import Protocol

class UserRepository(Protocol):
    def find_user(self, user_id: int) -> str:
        ...
```

Concrete classes do not need to inherit from the Protocol:

```python
class MySqlUserRepository:
    def find_user(self, user_id: int) -> str:
        return f"User from MYSQL: {user_id}"
```

The mental model is:

```text
Protocol
    ↓
Defines expected behavior
    ↓
Static type checker can verify compatibility
    ↓
Python runtime does not enforce the contract
```

This is essentially:

> Duck typing + static type checking

## Static Type Checking

Python type hints can be checked by external tools.

### Pyright

Pyright is a static type checker for Python. It can detect problems such as:

- Wrong argument types
- Incorrect return types
- Invalid `Literal` values
- Objects that don't satisfy a `Protocol`
- Incorrect `TypedDict` structures

### Pylance

Pylance provides Python language features in VS Code and uses Pyright's type analysis. It provides:

- Type checking
- Autocomplete
- Type information
- Diagnostics
- Navigation

### mypy

mypy is another widely used static type checker for Python. It checks annotations and reports type inconsistencies before runtime.

## Runtime Validation

Static type checking is different from runtime validation.

Runtime validation checks the **actual data while the application is running**.

This matters for:

- HTTP requests
- JSON payloads
- Database data
- External APIs
- Environment variables
- User input

Python type hints alone do not provide this validation.

## Runtime Validation Tools

There are several Python libraries for runtime validation.

Examples:

- **Pydantic** — our main choice
- `marshmallow`
- `voluptuous`
- `msgspec`
- `attrs` and validation-related integrations
- `dataclasses` combined with validation libraries

We will focus on **Pydantic** because it is directly relevant to our FastAPI backend path.

## Pydantic — What We Will Learn

Pydantic provides runtime data validation using Python type annotations.

Basic example:

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
```

We will learn Pydantic properly later, including:

- `BaseModel`
- Field validation
- Required vs optional fields
- Nested models
- Serialization
- Deserialization
- Validation errors
- Request models
- Response models

## FastAPI + Pydantic

FastAPI integrates heavily with Pydantic.

Our future flow will be:

```text
HTTP Request
     ↓
FastAPI
     ↓
Pydantic
     ↓
Runtime validation
     ↓
Valid data → endpoint
Invalid data → validation error
```

We are intentionally **not** doing a deep Pydantic study on Day 7. We will learn it when we reach FastAPI.

## Static Typing vs Runtime Validation

### Static typing

```text
Python code
    ↓
Pyright / Pylance / mypy
    ↓
Check type expectations
    ↓
Report problems
```

### Runtime validation

```text
Actual runtime data
    ↓
Pydantic
    ↓
Validate actual values
    ↓
Valid → continue
Invalid → validation error
```

## Day 7 Mental Model

```text
Type annotations
    ↓
Expected types

list[str]
dict[str, int]
    ↓
Generic collection types

str | None
    ↓
Union types

Literal["GET", "POST"]
    ↓
Specific allowed values

TypedDict
    ↓
Expected dictionary structure

Protocol
    ↓
Expected behavior / structural contract

Pyright / Pylance / mypy
    ↓
Static type checking

Pydantic
    ↓
Runtime data validation

FastAPI + Pydantic
    ↓
API request/response validation
```

## TypeScript Comparison

| Python | TypeScript |
|---|---|
| `list[str]` | `string[]` |
| `dict[str, int]` | `Record<string, number>` |
| `str \| None` | `string \| null` |
| `Literal["GET", "POST"]` | `"GET" \| "POST"` |
| `TypedDict` | Object type / interface |
| `Protocol` | Structural interface-like typing |
| Pyright / mypy | TypeScript compiler/type checker |
| Pydantic | Runtime validation libraries such as Zod provide a similar role |

## What We Will Learn Later

### Day 7 — Completed

- Type annotations
- Built-in generic types
- Union types
- `None`
- `Literal`
- `TypedDict`
- `Protocol`
- Static typing vs runtime behavior

### Later Backend Work

We will learn:

- Pydantic
- Request validation
- Response validation
- Configuration validation
- API error handling
- Production static type checking and tooling

## Key Takeaway

> **Python type hints describe what we expect. Static type checkers help catch violations before runtime. Runtime validation tools such as Pydantic validate actual data while the application is running.**

For our backend path:

```text
Python Type Hints
       ↓
Static Type Checking
       ↓
Pydantic
       ↓
FastAPI
       ↓
Runtime API Validation
```
