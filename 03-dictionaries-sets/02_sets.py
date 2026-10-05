# # numbers = [1, 2, 3, 2, 4, 1, 5, 3]

# # unique_numbers = set(numbers)

# # print(unique_numbers)

# numbers = {10, 20, 30}

# print(numbers)

# numbers = set()

# numbers.add(10)
# numbers.add(10)
# print(numbers)

# numbers = {10, 20, 30}

# numbers.add(40)
# print(numbers)

# numbers.remove(20)
# print(numbers)

# numbers.discard(50)
# print(numbers)

# numbers.remove(50)

# backend_skills = {"Python", "Node.js", "SQL", "Redis"}
# frontend_skills = {"JavaScript", "TypeScript", "React", "SQL"}

# print(backend_skills.intersection(frontend_skills))
# print(backend_skills.union(frontend_skills))
# print(backend_skills.difference(frontend_skills)) #means "in a, but not in b."
# print(backend_skills.symmetric_difference(frontend_skills))

required = {"read", "write"}
user_permissions = {"read", "write", "delete"}

print("ISSUBSET",required.issubset(user_permissions)) # Are all elements of A present in B?
print("ISSUPERSET",user_permissions.issuperset(required)) # Does A contain every element of B?

frontend = {"React", "TypeScript"}
backend = {"Python", "SQL"}

print("ISDISJOINT",frontend.isdisjoint(backend)) # Do these two sets have zero elements in common?"