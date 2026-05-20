def calculate_usd(real_amount):
    exchange_rate = 1 / 5.03
    return real_amount * exchange_rate


user_real = float(input("Enter the amount in Brazilian Real: "))
print(f"The equivalent amount in USD is: {calculate_usd(user_real)}")
