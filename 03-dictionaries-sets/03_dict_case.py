users = [
    {id:"1","total":100, "coupon": "P50"},
    {id:"2","total":500, "coupon": "P25"},
    {id:"3","total":800, "coupon": "P45"}
]
print(users)

discounts = {
    "P50": (0, 10),
    "P25": (0.25, 0),
    "P45": (0.45, 0)
}

for user in users:
    coupon = user.get("coupon")
    if coupon is None:
        continue
    (percent, fixed) = discounts.get(coupon, (0,0))
    total = user.get("total")
    discount =  fixed if fixed > 0 else (percent * total)
    final_amount = user.get("total") - discount
    print("Final amount:",final_amount)




