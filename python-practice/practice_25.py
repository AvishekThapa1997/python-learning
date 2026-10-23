class ToDictMixin:
    def to_dict(self):
        return {
            key:self._convert(value)
            for key, value in self.__dict__.items()
        }
    
    def _convert(self,obj):
        if (is_dict:=isinstance(obj,dict)) or hasattr(obj, "__dict__"):
            items = obj.items() if is_dict else obj.__dict__.items()
            return {
                key : self._convert(value)
                for key,value in items
            }
        elif isinstance(obj,(list,tuple)):
            return [
                self._convert(value)
                for value in obj
            ]
        else:
            return obj 

class Address:
    def __init__(self, city: str, country: str):
        self.city = city
        self.country = country



class Employee(ToDictMixin):
    def __init__(self, name: str, addresses: list[Address],metadata:dict):
        self.name = name
        self.address = addresses
        self.metadata = metadata


employee = Employee(
    "Alex",
   [ Address("Bhubaneswar", "India")],
   {
       "metadata": {
            "team": "Engineering",
            "home_address":[
                Address(city="Ranchi",country="India"),
                Address(city="New Delhi",country="India")
            ]
        }
   }
)

print(employee.to_dict())