

def main():
    try:
        number = int(input("Enter a number: "))
        print(100 / number)
    except ValueError:
        print("Please enter a valid number")
    except ZeroDivisionError:
        print("Number cannot be zero")
    except:
        print("Something went wrong")
    else:
        print("Success")
        return None
        # executes when try block is success
    finally:
        print("Finally")

class Account:
    def __init__(self, balance:int):
        self.balance = balance

    def __updateBalance(self, amount:int):
        self.balance -= amount

    def withdraw(self, amount:int):
        if amount < 0 or amount > self.balance:
            raise ValueError("Invalid amount")
        self.__updateBalance(amount)
        return f"${amount}"

account = Account(1000)
try:
    amount_to_withdraw = int(input("Enter amount:"))
    print(account.withdraw(amount_to_withdraw))
except ValueError:
    print("Invalid Amount")
except Exception:
    print("Some other error")
else:
    print("Transaction completed")
finally:
    print("Please take out your card")                       


