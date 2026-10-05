# # numbers = [10, 20, 30]

# # numbers.append(40)
# # print(numbers)

# # numbers.extend([50, 60])
# # print(numbers)

# # numbers.insert(1, 15)
# # print(numbers)

# # numbers.pop()
# # print(numbers)

# # numbers.pop(1)
# # print(numbers)

# # # append() vs extend()

# # numbers2 = [1, 2]

# # numbers2.append([3, 4])
# # print(numbers2)

# # numbers2.extend([5,6])
# # print(numbers2)

# # numbers = [40, 10, 30, 20]

# # result = numbers.sort()

# # print(numbers)
# # print(result)

# numbers = [1, 2, 3, 4, 5, 6]

# result = sorted(numbers)

# print(numbers)
# print(result)

# # squares = []
# # numbers.

# # for num in numbers:
# #     squares.append(num * num)
# # print(squares)    
# # [result for item in iterable if condition
# squares = [num * num for num in numbers]
# even_squares = [num * num for num in numbers if num % 2 == 0]
# print("Even squares:", even_squares)
# squares.remove(4)
# print(squares)

# numbers = (10, 20, 30, 40)

# numbers[1] = 200

user = ("Avishek", 28)

name, age = user

print(name)
print(age)
print(type(user))
# a = (10)
# a[0] = 20
# print(a)

numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

print(first)
middle.append(60)
print(middle)
print(last)

first, *rest = numbers
print(rest)