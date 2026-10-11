tea_prices_inr = {
    "Masala Chai":40,
    "Gree Tea" : 50,
    "Lemon Tea": 200
}

tea_prices_usd = {tea:price / 80 for tea,price in tea_prices_inr.items()}
print(tea_prices_usd)

