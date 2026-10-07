# # class User:
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age

# #     def show(self):
# #         print(self)
# #         print(self.name)    


# # user = User("Avishek Thapa", 25)
# # print(User.show)

# class UserRepository:
#     def find_user(self, user_id):
#         print(f"Finding user {user_id}")


# class UserService:
#     def __init__(self, repository):
#         self.repository = repository

#     def get_user(self, user_id):
#         return self.repository.find_user(user_id)


# repository = UserRepository()
# service = UserService(repository)

# service.get_user(10)

class MyRepository:
    def find_user(self, user_id):
        return f"My repo: {user_id}"


class AnotherRepository:
    def find_user(self, user_id):
        return f"Another repo: {user_id}"


class UserService:
    def __init__(self, repository):
        self.repository = repository

    def get_user(self, user_id):
        return self.repository.find_user(user_id)


service1 = UserService(MyRepository())
service2 = UserService(AnotherRepository())

print(service1.get_user(10))
print(service2.get_user(10))