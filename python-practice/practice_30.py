from collections.abc import Sequence


class RecentOrders(Sequence):
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]

    def __len__(self):
       return len(self.items)


recent_orders = RecentOrders(["ORD-1","ORD-2", "ORD-3", "ORD-2"])  

# print(recent_orders[0])
# print(len(recent_orders))

print(recent_orders.count("ORD-2"))