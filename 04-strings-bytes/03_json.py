# import json

# user = {
#     "name": "Avishek",
#     "age": 29,
#     "is_active": True
# }

# json_data = json.dumps(user)

# print("JSON data",json_data)
# print(type(json_data))


# parsed_data = json.loads(json_data)
# print("Parsed Data", parsed_data)

import json

data = {
    "name": "Avishek",
    "skills": {"Python", "TypeScript"}
}

print(json.dumps(data))