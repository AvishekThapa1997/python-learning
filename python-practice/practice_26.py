class User:
    def __init__(self, name):
        self.__name = name

    def test(self):
        print("TEST")    


class Admin1(User):
    def test(self):
        print("Admin1")
        super().test()

class Admin2(User):
    def test(self):
        print("Admin2")
        super().test()

class Admin(Admin1, Admin2):
    def test(self):
        print("Admin")
        super().test()


admin = Admin("Alex")
admin.test()