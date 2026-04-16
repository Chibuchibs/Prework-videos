print(42)
print("42")
print(42.0)




print(42 + 6)

print("42" + "6")

value1 = 42

value2 = "42"

print(f"value1 is {type(value1)}")

print(f"value2 is {type(value2)}")


product_name = "wireless mouse"
price_text = "29.99"
quantity_text = "3"
tax_rate_text = "0.08"

price = float(price_text)
quantity = int(quantity_text)
tax_rate = float(tax_rate_text)

subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

print(f"product: {product_name}")
print(f"price: ${price} * {quantity}")
print(f"subtotal: ${subtotal:.2f}")
print(f"tax: $({tax_rate * 100}%): ${tax:.2f}")
print(f"total: ${total:.2f}): ${total:.2f}")
