class User:
    def __init__(self, name):
        self.name = name

    @property
    def display_name(self):
        return f"Name : {self.name}"


user = User("Avishek Thapa")
print(user.display_name)