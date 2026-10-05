items = [10,20,30]

list1 = items
list2 = items

list2[0] = 100

print("Before initializing to new list")
print("Original List", items)
print("List1", list1)
print('List2', list2)

list2 = [10,500,600]
list2[0] = 100
print("After initializing to new list")
print("Original List", items)
print("List1", list1)
print('List2', list2)



user = {
    "address" : {
        "state" : "Bengaluru"
    }
}
user2 = user

user2["address"]["state"] = "Odisha"
print("User2 :", user2)
print("User1:", user)