orders = [
    {
        "order_id": 101,
        "category": "electronics",
        "price": 299.99,
        "vip": True,
    },
    {
        "order_id": 102,
        "category": "books",
        "price": 15.50,
        "vip": False,
    },
    {
        "order_id": 103,
        "category": "electronics",
        "price": 89.00,
        "vip": False,
    },
    {
        "order_id": 104,
        "category": "books",
        "price": 42.00,
        "vip": True,
    },
    {
        "order_id": 105,
        "category": "electronics",
        "price": 1200.00,
        "vip": True,
    },
]


def generate_result_by_category(orders):
    result = dict()
    for order in orders:
        category = order['category']
        is_vip = order.get("vip", False)
        price = order.get("price", False)
        entry = result.setdefault(category, {
            "category":category,
            "total_spend": 0,
            "vip_spend" : 0
        })
        entry["total_spend"] += price
        if is_vip:
            entry["vip_spend"] += price
    summary = list(result.values())
    summary.sort(key=lambda x: (x["vip_spend"], x["total_spend"]))
    return summary

print(list(generate_result_by_category(orders=orders)))






