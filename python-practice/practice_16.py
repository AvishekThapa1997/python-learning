reports = [
    {"id": 101, "duration": 250},
    {"id": 102, "duration": 800},
    {"id": 103, "duration": 900},
    {"id": 104, "duration": 200},
    {"id": 105, "duration": 1200},
]

def calculate_processing_cost(duration):
    # Assume this is an expensive calculation.
    return duration * 0.75

report_with_high_processing_cost = {
    report['id'] : processing_cost
    for report in reports
    if (processing_cost := calculate_processing_cost(report['duration'])) >= 600
}

print(report_with_high_processing_cost)
accounts = {
    "user_101": 2500.0,
    "user_102": 0.0,
    "user_103": 1750.0,
}

def get_account_balance(accounts, user_id):
    account_key = f"user_{user_id}"
    if account_key not in accounts:
        raise ValueError("User does not have any account")
    return accounts[account_key]
