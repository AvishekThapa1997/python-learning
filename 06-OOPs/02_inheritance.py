class User:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello {self.name}")


class Admin(User):
    def __init__(self, name, prop):
        super(self,name)
        self.prop = prop


admin = Admin("Avishek",True)

admin.greet()