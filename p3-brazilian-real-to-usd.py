user_cash = float(input("Enter the amount in Brazilian Real: "))
exchange_rate = 1 / 5.03
usd_amount = user_cash * exchange_rate
print(f"The equivalent amount in USD is: {usd_amount}")
