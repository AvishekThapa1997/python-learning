# # # # class BankAccount:
# # # #     def __init__(self, owner, balance):
# # # #         self.owner = owner
# # # #         self.balance = balance

# # # #     @property
# # # #     def available_balance(self):
# # # #         return self.balance   


# # # # class AccountService:
# # # #     def __init__(self, bank_account):
# # # #         self.bank_account = bank_account

# # # #     def show_balance(self):
# # # #         return self.bank_account.available_balance



# # # # bank_account = BankAccount("Avishek", 1000)
# # # # account_service = AccountService(bank_account)
# # # # balance = account_service.show_balance()
# # # # print(balance)


# # # class User:
# # #     def __init__(self, name, email):
# # #         self.name = name
# # #         self.email = email

# # #     def greet(self):
# # #         print(f"Hello {self.name}")


# # # class AdminUser(User):
# # #     def __init__(self, name, email, permissions):
# # #         super().__init__(name, email)
# # #         self.permissions = permissions

# # #     def greet(self):
# # #         super().greet()
# # #         print("Admin access enabled")
# # #         print(f"Permissions : {self.permissions}")

# # #     def show_permissions(self):
# # #         return self.permissions

# # #     def __str__(self):
# # #         return f"User(name={self.name}, email={self.email}, permissions={self.permissions})"     

# # # admin = AdminUser(
# # #     "Avishek",
# # #     "avishek@example.com",
# # #     ["read", "write", "delete"]
# # # )

# # # admin.greet()
# # # print(admin.show_permissions())
# # # print(admin)          
# # # 
# # #   

# # # class UserRepository:
# # #     def find_user(self, user_id):
# # #         return f"UserRepository: User {user_id}"

# # # class MockUserRepository:
# # #     def find_user(self, user_id):
# # #         return f"MockUserRepository:Mock User {user_id}"        


# # # class UserService:
# # #     def __init__(self, user_repository):
# # #         self.user_repository  = user_repository

# # #     def get_user(self, user_id):
# # #         return self.user_repository.find_user(user_id)


# # # service = UserService(UserRepository())
# # # print(service.get_user(10))

# # # service = UserService(MockUserRepository())
# # # print(service.get_user(10))


# # class User:

# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age

# #     @property
# #     def age(self):
# #        return self._age

# #     @age.setter
# #     def age(self, age):
# #         if age < 0:
# #             raise ValueError("Age cannot be negative")
# #         self._age = age    



# # user = User("Avishek", -29)

# # print(user.age)

# # user.age = 30
# # print(user.age)

# # user.age = -5

# class User:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email

#     def __str__(self):
#         return f"User: {self.email}"    

#     def __eq__(self,other):
#         return self.email == other.email

# user1 = User("Avishek", "avishek@example.com")
# user2 = User("John", "avishek@example.com")
# user3 = User("John", "john@example.com")

# print(user1 == user2)
# print(user1 == user3)
# print(user1)            


class User:
    def __init__(self,name, email):
        self.name = name
        self.email = email

    def greet(self):
        print(f"Hello {self.name}")

    def __str__(self):
        return f"User:{self.name} {self.email}"   

    def __eq__(self, other):
        return self.email == other.email     

class AdminUser(User):
    def __init__(self, name , email, permissions):
        super().__init__(name, email)
        self.permissions = permissions

    def greet(self):
        super().greet()
        print(f"Admin Access enabled")    

class UserRepository:
    def find_user(self,user_id):
        return User(name="Avishek Thapa", email="abc@yopmail.com")

class  UserService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def get_user(self, user_id):
        return self.user_repository.find_user(user_id)          

repository = UserRepository()
service = UserService(repository)

user = service.get_user(1)

print(user)
print(user == User("Another Name", "avishek@example.com"))

admin = AdminUser(
    "Admin Avishek",
    "admin@example.com",
    ["read", "write", "delete"]
)

admin.greet()