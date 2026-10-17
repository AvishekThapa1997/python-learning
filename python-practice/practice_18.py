from functools import wraps
def create_order_validator(max_amount):
    @wraps(create_order_validator)
    def validate_order(amount):
        return amount <= max_amount
    return validate_order    

validate_standard = create_order_validator(1000)
validate_premium = create_order_validator(5000)

print(validate_standard(500))   # True
print(validate_standard(1500))  # False

print(validate_premium(3000))   # True
print(validate_premium(6000))   # False