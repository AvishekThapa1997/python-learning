numbers = [10, 20, 30]

a = numbers
b = [10, 20, 30]

print(id(numbers))
print(id(a))
print(id(b))

print(numbers is a)
print(numbers is b)