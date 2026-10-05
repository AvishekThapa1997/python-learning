# numbers = [10, 20, 30, 40, 50, 60]

# numbers[1:4] = [200,300,400,500]
# print(numbers)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# even_squares = [num * num for num in numbers if num % 2 == 0]
# print("Even squares:", even_squares)

# numbers = [10, 20, 10, 30, 20, 40, 30]
# unique = []
# for num in numbers:
#     if(num not in unique):
#         unique.append(num)

# print(unique)

# data = ("Avishek", 5.5, "Senior Engineer", "India")
# name,*middle, country = data
# print(name)
# print(country)
# print(middle)
users = [
    ("Avishek", 28, True),
    ("Rahul", 31, False),
    ("Priya", 25, True),
    ("Amit", 35, False),
]

active_user_age_below_30 = [name for (name,age,active) in users if(age < 30 and active)]
print(active_user_age_below_30)