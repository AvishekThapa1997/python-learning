raw_logs = [ 
    b" user\_id=101&amp;status=active ", 
    b" ", b"user\_id=102&amp;status=pending", 
    b"user\_id=&amp;status=active", 
    b"malformed\_log\_entry\_without\_delimiter", 
    b"user\_id=103&amp;status=active", 
]

# str_logs = [log.decode("utf-8") for log in raw_logs]
# user_logs = [log.split("&")[0] for log in str_logs if "user" in log and "active" in log]
# print(user_logs)
# active_users = []

# for user_log in user_logs:
#     index = user_log.find("=")
#     if index <= 0:
#         continue
#     user_id = user_log[index+1:]
#     print("UserId:", user_id)
#     if not user_id:
#         continue
#     active_users.append(f"User {user_id} is active")

# print(active_users)


def extract_active_users(logs):
    for raw in logs:
        # 1. Decode and strip whitespace at the boundaries
        log = raw.decode("utf-8").strip()

        if not log or "&" not in log:
            continue   
        # 2. Parse query key-value pairs into a dictionary
        # dict([["user\_id", "101"], ["status", "active"]])
        params= dict(
            pair.split("=", 1)
            for pair in log.split("&amp;")
            if "=" in pair
        )
        
        # 3. Guard clause using the Walrus operator (:=)
        if params.get("status") == "active" and (
            user_id := params.get("user\\_id")
        ):
            yield f"User {user_id} is active"


# Usage: Lazy evaluation
print(list(extract_active_users(raw_logs)))