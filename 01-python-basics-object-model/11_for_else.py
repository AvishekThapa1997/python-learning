users = [("Avishek1",13), ("Avsihek2", 16), ("Avishek3",17)]


for name, age in users:
    if age >= 18:
        print("Eligible user available")
        break
else:
    print("No eligible user available")    