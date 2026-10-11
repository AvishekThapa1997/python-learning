# value = 13
# remainder = value % 5

# if remainder:
#     print(f"No divisble, remainder is {remainder}")



value = 13

if (remainder := value % 5):
    print(f"No divisble, remainder is {remainder}")


available_sizes = ('small', 'medium', 'large')
if(requested_size := input("Enter your chai cup size: ")) in available_sizes:
    print(f"Serving {requested_size} chai")    
else:
    print(f"Size unavailable {available_sizes}")

flavours = ("masala", "ginger", "lemon", "mint")
print(f"Available flavours: {flavours}")

while((flavor := input("Choose your flavour: ")) not in flavours):
    print(f"Sorry, {flavor} is not available")

print(f"You choose {flavor}")
