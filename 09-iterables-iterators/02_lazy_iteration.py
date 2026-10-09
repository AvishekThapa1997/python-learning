numbers = [x * 2 for x in range(5)]
print(numbers)

numbers = (x * 2 for x in range(5))
print(next(numbers))
print(next(numbers))
print(next(numbers))


def generate_numbers():
    print("Generating 0")
    yield 0

    print("Generating 1")
    yield 1

numbers = generate_numbers()

print("Generator created")
print(next(numbers))
print(next(numbers))
