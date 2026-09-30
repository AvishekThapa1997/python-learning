numbers = [10, 20, 30]

print(numbers)
print(type(numbers))

numbers.append(40)

print(numbers)

numbers = [10, 20, 30]

before = id(numbers)

numbers.append(40)

after = id(numbers)

print("before:", before)
print("after:", after)
print("same object:", before == after)
print("numbers:", numbers)

numbers = [10, 20, 30, 40, 50]

print(numbers[0])
print(numbers[2])

print(numbers[-1])
print(numbers[-2])
print(numbers[1:4])

numbers[:3]   # from beginning up to 3
numbers[2:]   # from index 2 to the end
numbers[:]    # entire list

print(numbers[::2]) # numbers[start:stop:step]

numbers = [10, 20, 30]

numbers[1] = 99

print(numbers)

numbers = [10, 20, 30]
other = numbers.copy()

other[1] = 99

print(numbers)
print(other)

numbers = [10, 20, 30, 40, 50, 60]
print(numbers[1::2])