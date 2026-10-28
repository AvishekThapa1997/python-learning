class RecentOrder:
    __items:list[str]
    def __init__(self, items:list[str]):
        self.__items = items
       
    def __getitem__(self, s):
        return self.__items[s]

    def __len__(self):
        return len(self.__items)

    def __str__(self):
        return f"[{", ".join(self.__items)}]"
    


orders = RecentOrder(['ORD-1','ORD-2', 'ORD-3','ORD-4'])

print(orders)
print(orders[0])