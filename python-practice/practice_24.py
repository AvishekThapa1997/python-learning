class ToDictMixin:

    def to_dict(self):
        return self.__dict__



class Employee(ToDictMixin):
    name :str
    department: str
    def __init__(self, name:str, department:str):
        self.name = name
        self.department = department


class Project(ToDictMixin):
    name: str
    status: str

    def __init__(self, name:str, status:str):
       self.name = name
       self.status = status


employee = Employee("Alex", "Engineering")
project = Project("API Migration", "In Progress")
print(Employee.name)
print(employee.to_dict())
print(project.to_dict())

assert employee.to_dict() == {
    "name": "Alex",
    "department": "Engineering",
}

assert project.to_dict() == {
    "name": "API Migration",
    "status": "In Progress",
}