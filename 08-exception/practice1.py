# def main():
#     try:
#         a = int(input("Enter first number"))
#         b = int(input("Enter second number"))
#         result = a / b
#     except ZeroDivisionError:
#         print("Cannot divide by zero")    
#     except ValueError:
#         print("Invalid input")    
#     except Exception:
#         print("Something went wrong")
#     else:
#         print("Operation completed")
#         return result
#     finally:
#         print("Cleanup done")         
# 
#    


class InvalidAmountError(Exception):
    pass

class Account:
    def __init__(self, balance):
        self.balance = balance

    def update_balance(self, amount):
        self.balance -= amount     

    def withdraw(self, amount):
        if amount < 0 or amount > self.balance:
            raise InvalidAmountError("Cannot proceed with the amount")
        self.update_balance(amount)    
        return amount

def main():
    try:
        account = Account(5000)
        amount_to_withdraw = int(input("Enter amount"))
        print(f"Initial balance: {account.balance}")
        amount = account.withdraw(amount_to_withdraw)
    except InvalidAmountError:
        print("Cannot proceed")
    except ValueError:
        print('Invalid')
    except Exception:
        print("Something went wrong")
    else:
        print(f"Withdraw: {amount}")
        print(f"Remaining Balance: {account.balance}")  
          


main()
