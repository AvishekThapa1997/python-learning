# Day 6 — Object-Oriented Programming (OOP)

## Goal

Understand the Python OOP concepts needed for backend development, with emphasis on composition, dependency injection, inheritance, properties, dunder methods, and Python's object model.

## 1. Classes and Instances

```python
class User:
    pass

user1 = User()
user2 = User()
```

Each `User()` call normally creates a separate instance.

## 2. `__init__` and `self`

`__init__` initializes an already-created instance.

```python
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
```

`self` refers to the current instance. `user.show()` conceptually binds the instance as the first argument.

## 3. Instance and Class Attributes

Instance attributes belong to individual objects:

```python
user1.name = "Avishek"
user2.name = "John"
```

Class attributes belong to the class:

```python
class User:
    role = "user"
```

An instance assignment such as `user.role = "admin"` shadows the class attribute for that instance.

## 4. Composition and Dependency Injection

Composition is a "has-a" relationship.

```python
class UserRepository:
    def find_user(self, user_id):
        return f"User {user_id}"

class UserService:
    def __init__(self, repository):
        self.repository = repository

    def get_user(self, user_id):
        return self.repository.find_user(user_id)
```

Dependency injection means providing the dependency from outside instead of constructing it internally.

This is very important for backend architecture.

## 5. Duck Typing

Python often cares about behavior rather than inheritance.

```python
class UserRepository:
    def find_user(self, user_id):
        return f"Real user: {user_id}"

class MockUserRepository:
    def find_user(self, user_id):
        return f"Mock user: {user_id}"
```

Both can be injected into `UserService` because both provide `find_user(user_id)`.

## 6. Inheritance and `super()`

Inheritance represents an "is-a" relationship.

```python
class User:
    def greet(self):
        print("Hello")

class Admin(User):
    pass
```

A child can override methods:

```python
class Admin(User):
    def greet(self):
        print("Welcome Admin")
```

Use `super()` to call parent behavior:

```python
class Admin(User):
    def __init__(self, name, permissions):
        super().__init__(name)
        self.permissions = permissions

    def greet(self):
        super().greet()
        print("Admin access enabled")
```

`super().__init__()` calls parent initialization; `super().method()` calls a parent method.

## 7. Inheritance vs Composition

Use inheritance for "is-a":

```text
Admin is a User
Dog is an Animal
```

Use composition for "has-a":

```text
UserService has a UserRepository
Car has an Engine
```

For backend development, composition and dependency injection are generally more important than inheritance.

## 8. `@property`

`@property` makes a method accessible like an attribute.

```python
class User:
    @property
    def display_name(self):
        return self.name.upper()
```

Then:

```python
user.display_name
```

This is conceptually similar to a JS/TS getter.

A setter allows controlled assignment:

```python
class User:
    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value
```

## 9. Dunder Methods and Protocols

Dunder methods have double underscores:

```python
__init__
__str__
__repr__
__eq__
__len__
```

Python calls them for corresponding operations:

```text
print(obj)    → __str__()
len(obj)      → __len__()
obj == other  → __eq__()
obj + other   → __add__()
```

You do not need to memorize every dunder method.

## 10. `__str__` vs `__repr__`

`__str__` is human-friendly:

```python
def __str__(self):
    return f"User: {self.name}"
```

`__repr__` is developer/debug-friendly:

```python
def __repr__(self):
    return f"User(name={self.name!r}, email={self.email!r})"
```

Mental model:

```text
__str__  → human-friendly
__repr__ → developer/debug-friendly
```

## 11. `__eq__`

By default, separate instances are not automatically equal just because their data is identical.

You can define equality:

```python
def __eq__(self, other):
    return self.email == other.email
```

Then users with the same email can be considered equal.

Remember:

```text
== → equality
is → identity
```

## 12. Instance, Class, and Static Methods

Instance methods receive `self`:

```python
def greet(self):
    ...
```

Class methods receive `cls`:

```python
@classmethod
def get_role(cls):
    return cls.role
```

Static methods receive neither automatically:

```python
@staticmethod
def is_valid_name(name):
    return len(name) >= 3
```

Mental model:

```text
Instance method → self → instance
Class method    → cls  → class
Static method   → nothing automatically
```

Calling a class method through an instance still provides `cls`, not `self`.

Calling a static method through an instance does not provide `self` or `cls`.

## 13. Internal and Name-Mangled Methods

Python does not have Java/TypeScript-style enforced private methods.

Single underscore:

```python
def _validate_name(self):
    ...
```

means internal/private-by-convention.

Double underscore:

```python
def __validate_name(self):
    ...
```

uses name mangling, roughly producing `_User__validate_name`.

This is not true access control.

## 14. `__new__` vs `__init__`

When:

```python
user = User("Avishek")
```

the rough sequence is:

```text
User(...)
  ↓
__new__()
  ↓
object is created
  ↓
__init__()
  ↓
object is initialized
```

Therefore:

```text
__new__  → creates/returns the instance
__init__ → initializes the returned instance
```

Important: `__new__` itself does **not** call `__init__`. The object creation mechanism coordinates the two calls.

If `__new__` does not return an instance of the class, `__init__` is not called for that returned object.

## 15. Arguments to `__new__`

If:

```python
user = User("Avishek")
```

the argument is available to both `__new__` and `__init__`:

```python
class User:
    def __new__(cls, name):
        print("NEW:", name)
        return super().__new__(cls)

    def __init__(self, name):
        print("INIT:", name)
```

Output:

```text
NEW: Avishek
INIT: Avishek
```

Arguments do not automatically need to be forwarded to `super().__new__()`.

For ordinary classes:

```python
super().__new__(cls)
```

is normally correct because `object.__new__()` normally needs the class, not your custom constructor arguments.

Only forward additional arguments when the parent `__new__` actually expects them.

## 16. Parent `__new__` vs Parent `__init__`

They are separate operations.

```python
class Child(Parent):
    def __new__(cls, value):
        return super().__new__(cls, value)

    def __init__(self, value):
        super().__init__(value)
```

The exact arguments depend on what the parent implementations expect.

Mental model:

```text
Child.__new__()
    ↓
if needed → super().__new__(...)

Child.__init__()
    ↓
if needed → super().__init__(...)
```

Neither automatically calls the other.

## 17. Singleton

Python does not have a truly private constructor like Java/TypeScript.

A Singleton is a pattern intended to ensure one instance:

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

Then:

```python
a = Singleton()
b = Singleton()

print(a is b)
```

outputs:

```text
True
```

For normal backend development, prefer clean dependency injection or module-level state where appropriate rather than automatically using Singleton.

# Practice Exercises

## Practice 1 — Composition + Property

Create `BankAccount` and `AccountService`.

Requirements:
1. `BankAccount` receives `owner` and `balance`.
2. Store the balance internally.
3. Expose balance using a property.
4. `AccountService` receives a `BankAccount`.
5. `show_balance()` returns the balance.
6. Do not use inheritance.

Expected:

```text
Owner: Avishek
Balance: 5000
```

## Practice 2 — Inheritance + `super()`

Create `User` and `AdminUser`.

Requirements:
1. `User` accepts `name` and `email`.
2. `User` has `greet()`.
3. `AdminUser` inherits from `User`.
4. `AdminUser` accepts `permissions`.
5. Use `super()` to initialize parent state.
6. Override `greet()`.
7. Call the parent `greet()` from the override.
8. Add `show_permissions()`.

Expected:

```text
Hello Avishek
Admin access enabled
Permissions: ['read', 'write', 'delete']
```

## Practice 3 — Duck Typing + Composition

Create `UserRepository`, `MockUserRepository`, and `UserService`.

Both repositories must implement:

```python
find_user(user_id)
```

`UserService` receives a repository and delegates to it.

Expected:

```text
UserRepository: User 10
MockUserRepository: Mock User 10
```

Do not use inheritance between the repositories.

## Practice 4 — Property + Validation

Create a `User` with `name` and `age`.

Negative ages must raise:

```text
Age cannot be negative
```

Valid assignment must work.

## Practice 5 — `__eq__` + `__str__`

Create a `User` with `name` and `email`.

Equality must be based only on email.

Expected:

```text
True
False
User: Avishek <avishek@example.com>
```

## Practice 6 — Combined OOP

Create:

- `User`
- `UserRepository`
- `UserService`
- `AdminUser`

Combine:
- composition
- dependency injection
- inheritance
- `super()`
- `__eq__`
- `__str__`

Expected:

```text
User: Avishek avishek@example.com
True
Hello Admin Avishek
Admin access enabled
```

# Key Mental Models

```text
self → current instance
cls  → current class

is → same object
== → equality

is-a  → inheritance
has-a → composition

__new__  → create/return object
__init__ → initialize object

@property → method accessed like an attribute

super().__init__() → parent initialization
super().method()    → parent method

_method()  → internal convention
__method() → name mangling

@classmethod  → automatic cls
@staticmethod → no automatic self/cls
```

# Day 6 Completion

Day 6 OOP is complete.

Next:

**Day 7 — Python Type System + Type Hints**

Topics:
- Type annotations
- Built-in generic types
- `Optional` / `Union`
- `|`
- `Literal`
- `TypedDict`
- `Protocol`
- Static typing vs runtime behavior
- Pydantic/FastAPI connection
