#You have a log of user API requests represented as tuples: `(user_id, timestamp, endpoint, status_code, response_time_ms)
logs = [
    ("user_101", "2026-10-14 10:00", "/api/v1/checkout", 200, 450),
    ("user_102", "2026-10-14 10:01", "/api/v1/login", 500, 120),
    ("user_101", "2026-10-14 10:02", "/api/v1/pay", 200, 890),
    ("user_103", "2026-10-14 10:03", "/api/v1/cart", 404, 50),
    ("user_102", "2026-10-14 10:04", "/api/v1/checkout", 500, 1500),
]

error_logs = [(*rest,status_code,response_time) for *rest,status_code,response_time in logs if status_code >= 500]

error_logs.sort(key=lambda log:(-log[-1], log[0]))
print(error_logs)