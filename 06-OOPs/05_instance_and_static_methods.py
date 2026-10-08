class User:
    def __init__(self, name):
        self.name = name

    @classmethod
    def create_user(cls,name):
        print(cls)
        return cls(name)

    def __str__(self):
        return f"Username is {self.name}"

    def __repr__(self):
        return f"User(name={self.name})"        

user1 = User('Avishek')
user2 = User('Avishek')
user3 = User.create_user("Avishek")
user4 = user1.create_user("Avishek")

print(user1)
print(user2)
print(user3)

print(repr(user1))
print(repr(user2))
print(repr(user3))




