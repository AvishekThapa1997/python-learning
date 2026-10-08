# class User:
#     def __init__(self, name):
#         print("Object Initialization")
#         self.name = name

#     def __new__(cls, name):
#         print("Creating Object")
#         return super().__new__(cls)

#     def __str__(self):
#         return f"Username is ${self.name}"    

# user = User("Avishek")
# print(user)           


# # Sig

#Singleton Pattern

class User:
    user_instance = None

    def __new__(cls):
        if(cls.user_instance is None):
            cls.user_instance = super().__new__(cls)
        return cls.user_instance

        
            