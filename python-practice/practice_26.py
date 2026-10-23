class User:
    def __init__(self, name):
        self.__name = name

    def test(self):
        print("TEST")    


class Admin(User):
    def display_name(self):
        super().test()
        return super().__name


admin = Admin("Alex")
print(admin.display_name())  # Alex