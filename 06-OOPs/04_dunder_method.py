class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"User(name={self.name!r})"

    def __str__(self):
        return f"User name is {self.name}" 

    def __eq__(self, other):
        return self.name == other.name    


user1 = User("Avishek")
user2 = User("Avishek")
print(user1 is user2)
print(user1)
print(repr(user1))