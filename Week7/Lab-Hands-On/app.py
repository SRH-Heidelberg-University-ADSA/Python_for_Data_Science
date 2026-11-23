def calculate_total(prices):
    total = 0
    for price in prices:
        total += price
    return total

def apply_discount(total, discount_percent):
    discount = total * (discount_percent / 100)
    discounted_price = total - discount
    return discounted_price

items = [10.99, 25.50, 5.75, 42.00]

total = calculate_total(items)
final_price = apply_discount(total, 15)

print(f"Total: ${total:.2f}")
print(f"After 15% discount: ${final_price:.2f}")