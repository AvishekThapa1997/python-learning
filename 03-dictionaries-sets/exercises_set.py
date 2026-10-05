# user_permissions = {"read", "write", "delete"}

# required_permissions = {"read", "write"}

# if(required_permissions.issubset(user_permissions)):
#     print("User has all permission")

# admin_permissions = {"read", "write", "delete"}
# restricted_permissions = {"delete", "suspend"}

# if(admin_permissions.isdisjoint(restricted_permissions)):
#     print("No common permission")

# all_features = {"search", "export", "analytics", "reports", "admin"}
# user_features = {"search", "reports"}

# print(all_features.difference(user_features))

# emails = [
#     "a@example.com",
#     "b@example.com",
#     "a@example.com",
#     "c@example.com",
#     "b@example.com",
# ]

# unique_email = set(emails)
# print(len(unique_email) != len(emails))

required = {"read", "write", "delete"}
user_permissions = {"read", "write"}
print(required.difference(user_permissions))