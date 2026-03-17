# List of product prices
product_prices = [1.50, 2.50, 3.00, 0.99, 2.30]

def apply_discount(product_prices):
    prices_copy = product_prices.copy()
    for item in range(len(prices_copy)):
        if prices_copy[item] > 2.00:
            prices_copy[item] -= prices_copy[item]*0.1
            print(range(len(prices_copy)))

    return prices_copy

# Call the function and store the updated prices
updated_prices = apply_discount(product_prices)
print(f"Updated product prices: ${updated_prices}")