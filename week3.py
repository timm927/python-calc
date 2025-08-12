def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price
    
price = float(input("Enter original price:"))
discount_percent = float(input("Enter percentage discount:"))

final_price = calculate_discount(price, discount_percent)
if discount_percent >= 20:
        print(f"Final price after {discount_percent}: {final_price}")
else:
        print(f"No discount applied. Price remains: {price}")
    