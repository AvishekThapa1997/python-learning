### \*args and \*\*kwargs — Quick Reference

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
