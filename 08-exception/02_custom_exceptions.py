
class InvalidAmountError(Exception):
    pass

class Account:
    def __init__(self, balance:int):
        self.balance = balance

    def __updateBalance(self, amount:int):
        self.balance -= amount

    def withdraw(self, amount:int):
        if amount < 0 or amount > self.balance:
            raise InvalidAmountError("Invalid amount")
        self.__updateBalance(amount)
        return f"${amount}"

account = Account(1000)
try:
    amount_to_withdraw = int(input("Enter amount:"))
    print(account.withdraw(amount_to_withdraw))
except InvalidAmountError as ive:
    raise ValueError("Exception chaning example") from ive    
except ValueError:
    print("Invalid Amount")
except Exception:
    print("Some other error")
else:
    print("Transaction completed")
finally:
    print("Please take out your card")