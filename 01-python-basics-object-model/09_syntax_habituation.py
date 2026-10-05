age = 25

if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")

for i in range(5):
    print(i)

count = 0
while count < 3:
    print(count)
    count += 1

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}"


print(greet("Avishek"))
print(greet("Avishek", "Hi"))    


def example(*args, **kwargs):
    for arg in args:
        print(arg)


example(10, 20, 30, name="Avishek", role="Backend Engineer")

numbers = [10,20,30]
squares = [number * number for number in numbers]
print(squares)