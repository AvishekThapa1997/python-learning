from typing import Protocol

class UserRepository(Protocol):
    def find_user(self, user_id: int) -> str:
        pass # or ... (Ellipsis type)



class MySqlUserRepository:
    def find_user(self, user_id:int):
        return f"User from MYSQL: {user_id}"

class MongoDBUserRepository:
    def find_user(self, user_id:int):
        return f"User from MongoDB: {user_id}"

class UserService:
    def __init__(self, user_repository:UserRepository):
        self.user_repository = user_repository

    def find_user(self, user_id:int):
        return self.user_repository.find_user(user_id)            

mysql_user_repository = MySqlUserRepository()
mongodb_user_repository = MongoDBUserRepository()
user_service_1 = UserService(mysql_user_repository)
user_service_2 = UserService(mongodb_user_repository)

print(user_service_1.find_user(1))
print(user_service_2.find_user(2))
