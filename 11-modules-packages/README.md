# Day 11 — Modules and Packages

## Goal

Understand the essentials of organizing Python code into reusable files and packages before moving into FastAPI.

## 1. Modules

A **module** is a Python file (`.py`) containing reusable code, such as functions, classes, and constants.

Example structure:

```text
project/
├── main.py
└── calculator.py
```

`calculator.py`:

```python
def add(*args):
    return sum(args)
```

`main.py`:

```python
import calculator

print(calculator.add(1, 2, 3))
```

Output:

```text
6
```

### Common import styles

Import a module and access its names through the module:

```python
import calculator

calculator.add(1, 2)
```

Import a specific name:

```python
from calculator import add

add(1, 2)
```

Use an alias:

```python
import math as m
from math import prod as multiply

print(m.sqrt(16))
print(multiply([2, 3, 4]))
```

Output:

```text
4.0
24
```

Python has no `export` keyword like JavaScript. Names defined in a module can generally be imported by other modules.

JavaScript comparison:

- `from calculator import add` is similar in intent to `import { add } from "./calculator.js"`.
- `import calculator` is similar in intent to importing a module namespace and accessing `calculator.add`.

## 2. Packages

A **package** is a directory that groups related modules.

```text
project/
├── main.py
├── services/
│   ├── __init__.py
│   ├── user_service.py
│   └── product_service.py
└── repositories/
    ├── __init__.py
    └── user_repository.py
```

- `user_service.py` and `product_service.py` are modules.
- `services/` is a package.
- `repositories/` is another package.
- `__init__.py` is commonly used to mark a regular package and can expose package-level names. Modern Python also supports namespace packages without it, but using it explicitly is straightforward for learning and many applications.

## 3. Absolute imports

An absolute import starts from a package that Python can resolve on its import path.

If the project root is the current directory:

```python
from project.services.user_service import get_user
```

For example, from the directory containing `project/`, run:

```bash
python -m project.main
```

The command uses a dotted module path rather than a file path.

If you run `main.py` directly from inside `project/`, an import such as `from services.user_service import get_user` may work because Python's import path differs. Prefer a consistent package structure and launch command as your application grows.

## 4. Relative imports

Relative imports refer to modules in the current package.

Inside `project/services/user_service.py`:

```python
from .user_utils import format_user
```

- `.` means the current package.
- `..` means the parent package.
- `...` means the package one level above the parent.

Relative imports require package context. Running a package file directly can cause relative imports to fail; running the application as a module helps preserve that context.

## 5. `__init__.py` and package-level imports

Suppose the package looks like this:

```text
services/
├── __init__.py
├── user_service.py
└── product_service.py
```

`user_service.py`:

```python
def get_user():
    return "User found"
```

`product_service.py`:

```python
def get_products():
    return ["Keyboard", "Mouse"]
```

Expose selected functions in `services/__init__.py`:

```python
from .user_service import get_user
from .product_service import get_products
```

Then callers can import them from the package:

```python
from project.services import get_user, get_products
```

This creates a convenient package-level interface. Keep `__init__.py` simple; avoid placing substantial application logic there.

You can also expose modules:

```python
from . import user_service, product_service
```

Then code can use:

```python
from project.services import user_service

print(user_service.get_user())
```

You may expose both modules and selected functions if that makes the package easier to use.

## 6. `__all__`

`__all__` specifies which names are imported by a wildcard import (`from module import *`).

In `calculator.py`:

```python
__all__ = ["add", "subtract"]

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

With:

```python
from calculator import *
```

both `add` and `subtract` are brought into the importing namespace.

Important:

- `__all__` primarily controls wildcard imports.
- It is not an access-control or privacy mechanism.
- Explicit imports such as `from calculator import subtract` can still import a name even if it is not listed in `__all__`.
- Prefer explicit imports in application code; they are clearer than wildcard imports.

## 7. Import path and running modules

Python uses `sys.path` to find modules and packages. The exact paths depend on the Python environment and how code is launched.

For this structure:

```text
12-modules-packages/
└── project/
    ├── __init__.py
    ├── main.py
    └── services/
        ├── __init__.py
        └── user_service.py
```

If `main.py` imports:

```python
import project.services.user_service as user_service

print(user_service.get_user())
```

Run from `12-modules-packages/`:

```bash
python -m project.main
```

This lets Python resolve `project` from the parent directory and runs `main` in package context.

By contrast, when running a script by its file path, Python normally places the script's directory at the beginning of `sys.path`. This explains why an import that works with one launch command may fail with another.

## 8. `if __name__ == "__main__"` — brief note

- When a file is run directly, its `__name__` is `"__main__"`.
- When imported, its `__name__` is normally the module's name.
- This guard keeps entry-point code from running just because another module imports the file.

We are keeping this topic brief for now; the main focus is imports, packages, and `__init__.py`.

## Quick reference

| Need | Example |
|---|---|
| Import a module | `import calculator` |
| Import a specific function | `from calculator import add` |
| Alias a module | `import math as m` |
| Absolute import | `from project.services.user_service import get_user` |
| Relative import from a sibling module | `from .user_utils import format_user` |
| Expose functions from a package | `from .user_service import get_user` in `__init__.py` |
| Expose modules from a package | `from . import user_service` in `__init__.py` |
| Control wildcard imports | `__all__ = ["get_user"]` |
| Run a module in package context | `python -m project.main` |

## Key takeaways

1. A module is a `.py` file; a package groups modules.
2. Python has no JavaScript-style `export` keyword. Import names explicitly from modules or re-export them through `__init__.py`.
3. Absolute imports start from a resolvable top-level package; relative imports use dots to refer to modules within a package.
4. `__init__.py` can define a convenient public interface for a package.
5. `__all__` affects wildcard imports, not access control.
6. `sys.path` and the way you launch code affect import resolution.
7. These fundamentals are enough to start organizing a FastAPI application. We can learn more advanced import patterns when they become useful in the project.
