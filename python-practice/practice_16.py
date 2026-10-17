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