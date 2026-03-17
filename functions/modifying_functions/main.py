def apply_discount(price, discount = 0.05):
    return price * (1 - discount)
def apply_tax(price, tax=0.07):
    return price * (1 + tax)

def calculate_total(price, discount = 0.05, tax= 0.07):
    discounted = apply_discount(price, discount)
    total_price_default = apply_tax(discounted, tax)
    #total_price_default = price - apply_discount(price) + apply_tax(price)
    return total_price_default

print("Total cost with default discount and tax: $",calculate_total(120))
print("Total cost with custom discount and tax: $",calculate_total(price=100, tax=0.08, discount=0.10))
