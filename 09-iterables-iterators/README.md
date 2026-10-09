# Day 9 — Iterables, Iterators, and Generators

## Learning goals

- Understand iterables and iterators.
- Use `iter()` and `next()`.
- Understand iterator exhaustion and `StopIteration`.
- Understand how `for` loops consume iterators.
- Understand generators, `yield`, and lazy evaluation.
- Build a generator that yields batches from a list.

## 1. Iterable vs. iterator

An **iterable** is an object Python can obtain an iterator from. Examples include lists, tuples, strings, dictionaries, and sets.

An **iterator** supplies values one at a time and remembers its current position.

```python
numbers = [10, 20, 30]
iterator = iter(numbers)

print(next(iterator))  # 10
print(next(iterator))  # 20
print(next(iterator))  # 30
```

Calling `iter(numbers)` creates an iterator for the list. Calling `iter()` on an existing iterator returns that same iterator:

```python
iterator = iter([10, 20, 30])
same_iterator = iter(iterator)

print(iterator is same_iterator)  # True
```

Each new iterator created from the list has its own independent position.

## 2. Iterator exhaustion

When an iterator has no more values, calling `next()` raises `StopIteration`. A `for` loop handles this automatically and stops normally.

```python
numbers = [10, 20]
iterator = iter(numbers)

print(next(iterator))  # 10
print(next(iterator))  # 20
print(next(iterator))  # Raises StopIteration
```

Once an iterator is exhausted, it does not automatically reset. Lists can be iterated over again by creating a new iterator; an exhausted iterator or generator does not restart.

## 3. How `for` loops consume iterators

A `for` loop obtains an iterator and repeatedly requests values until the iterator is exhausted.

```python
numbers = [10, 20, 30]
iterator = iter(numbers)

print(next(iterator))  # 10

for number in iterator:
    print(number)  # 20, then 30
```

The loop continues from the iterator's current position; it does not rewind it.

## 4. Eager vs. lazy evaluation

A list comprehension computes and stores its values immediately:

```python
numbers = [x * 2 for x in range(5)]
print(numbers)  # [0, 2, 4, 6, 8]
```

A generator expression produces values as they are requested:

```python
numbers = (x * 2 for x in range(5))

print(next(numbers))  # 0
print(next(numbers))  # 2
print(next(numbers))  # 4
```

Lazy iteration can help process large sequences incrementally without creating a complete list first.

## 5. Generator functions and `yield`

A function containing `yield` is a **generator function**. Calling it creates a generator object; the function body does not start executing at that point.

```python
def generate_numbers():
    print("Step 1")
    yield 10

    print("Step 2")
    yield 20

    print("Step 3")
    yield 30

numbers = generate_numbers()

print("Created")
print(next(numbers))
print(next(numbers))
```

Output:

```text
Created
Step 1
10
Step 2
20
```

### What happens on each `next()` call?

1. Calling `generate_numbers()` creates the generator object without executing the function body.
2. The first `next()` starts execution and runs the code up to the first `yield`.
3. The yielded value is returned, and execution pauses at that `yield`.
4. The next `next()` resumes execution immediately after the previous `yield`, runs the next section of code, and pauses at the next `yield`.
5. When the function finishes without yielding another value, the generator becomes exhausted and a subsequent `next()` raises `StopIteration`.

In short: **each `next()` starts or resumes the generator and executes until the next `yield` or until the function finishes.** Code after a `yield` does not execute until the generator is resumed.

## 6. Generators are one-time iterators

```python
def generate_numbers():
    yield 1
    yield 2

numbers = generate_numbers()

for number in numbers:
    print(number)

print(list(numbers))  # []
```

The first loop consumes the generator. The later `list(numbers)` is empty because there are no values left.

To iterate over those values again, call the generator function again to create a new generator object.

## 7. Practice: yield list batches

File: `03_iterator_practice.py`

```python
def read_batches(items, batch_size):
    pos = 0

    while pos < len(items):
        start = pos
        end = pos + batch_size
        pos = end

        yield items[start:end]


items = [1, 2, 3, 4, 5, 6, 7]

for batch in read_batches(items, 3):
    print(batch)
```

Output:

```text
[1, 2, 3]
[4, 5, 6]
[7]
```

For this learning exercise, the focus is on how the generator yields each batch. In production code, validate that `batch_size` is greater than zero so the loop always advances.

## Key takeaways

- An iterable can provide an iterator; an iterator produces values one at a time.
- `iter(iterable)` obtains an iterator, while `iter(iterator)` returns the same iterator.
- `next()` advances an iterator; exhaustion raises `StopIteration`.
- A `for` loop consumes an iterator and handles exhaustion.
- A generator function uses `yield` to produce values incrementally.
- Calling a generator function creates the generator; its body starts when iteration begins.
- Each `next()` resumes execution until the next `yield` or function completion.
- Generators are iterators and are consumed as their values are requested.
