# numbers = [10, 20, 30]

# first = iter(numbers)
# second = iter(numbers)

# print(next(first))
# print(next(first))
# print(next(second))


# numbers = [10, 20, 30]

# print(hasattr(numbers, "__iter__"))
# print(hasattr(numbers, "__next__"))

# iterator = iter(numbers)

# print(hasattr(iterator, "__iter__"))
# print(hasattr(iterator, "__next__"))

# items = list({1,2,3})
# print(items)

# numbers = [10, 20, 30]

# iterator = iter(numbers)
# same_iterator = iter(iterator)

# print(iterator is same_iterator)
# print(next(iterator))
# print(next(same_iterator))

numbers = [10, 20, 30]
iterator = iter(numbers)

for number in iterator:
    print(number)

print("Loop finished")

# print(next(iterator))

items = {1,2,3}
for item in items:
    print(item)

