customer_ids = [104, 101, 104, 102, 101, 103, 102]
amounts = [250.0, 800.0, 150.0, 0.0, 200.0, 450.0, 300.0]

customer_details = {
    101: {"name": "Amit", "tier": "gold"},
    102: {"name": "Neha", "tier": "silver"},
    103: {"name": "Ravi", "tier": "gold"},
}

def generate_order_summary(customer_ids,customer_details,amounts):
    result = {}
    for customer_id, amount in zip(customer_ids,amounts,strict=True):
        customer = customer_details.get(customer_id)
        name = customer_id
        tier = "unknown"
        if customer is not None:
            name = customer['name']
            tier = customer['tier']
        summary = result.setdefault(customer_id, {
            "customer_id":customer_id,
            "name":name,
            "tier":tier,
            "order_count":0,
            "total_amount":0
        })
        summary["order_count"] += 1
        summary["total_amount"] += amount
    report = list(result.values())
    report.sort(key=lambda report : report['total_amount'],reverse=True)
    return report

        

order_summary = generate_order_summary(customer_ids=customer_ids,customer_details=customer_details,amounts=amounts)

print(order_summary)

