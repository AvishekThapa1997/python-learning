def get_welcome_message(user_name, user_roles):
    if not user_roles: # same as if len(user_roles) == 0 , empty sequences (`[]`, `{}`, `""`, `0`, `None`) evaluate directly to `False` in boolean contexts
        return f"Welcome, {user_name}! You have no assigned roles"
    else:
        return f"Welcome, {user_name}! Your primary role is {user_roles[0]}"


get_welcome_message("Avishek Thapa",[])
get_welcome_message("Avishek Thapa",["admin", "editor"])