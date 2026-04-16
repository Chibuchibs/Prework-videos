item1_name = "notebook"
item1_price = "4.99"
item1_qty = "2"

item2_name = "pen pack"
item2_price = "7.50"
item2_qty = "1"

item3_name = "backpack"
item3_price = "34.99"
item3_qty = "1"

tax_rate = "0.075" # 7.5% sales tax

price1 = float(item1_price)
qty1 = int(item1_qty)
price2 = float(item2_price)
qty2 = int(item2_qty)
price3 = float(item3_price)
qty3 = int(item3_qty)
tax_rate = float(tax_rate)

subtotal = (price1 * qty1) + (price2 * qty2) + (price3 * qty3)
tax = subtotal * tax_rate
total = subtotal + tax

print("=" * 40)
print("Store Receipt".center(40))
print("=" * 40)
print(f"{item1_name}: ${price1:.2f} * {qty1} = ${price1 * qty1:.2f}")
print(f"{item2_name}: ${price2:.2f} * {qty2} = ${price2 * qty2:.2f}")
print(f"{item3_name}: ${price3:.2f} * {qty3} = ${price3 * qty3:.2f}")
print("-" * 40)
print(f"Subtotal:   ${subtotal:.2f}")
print(f"Tax: ({tax_rate * 100}%) ${tax:.2f}")
print(f"Total:      ${total:.2f}")