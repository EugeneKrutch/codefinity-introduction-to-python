prices = [29.99, 45.50, 12.75, 38.20]

for price in range(len(prices)):
    if price == 0:
        prices[price] -= prices[price] * 0.1
        print(f"Updated price for item {price}: ${prices[price]:.2f}")
    elif price == 1:
        prices[price] -= prices[price] * 0.2
        print(f"Updated price for item {price}: ${prices[price]:.2f}")
    elif price == 2:
        prices[price] -= prices[price] * 0.15
        print(f"Updated price for item {price}: ${prices[price]:.2f}")
    elif price == 3:
        prices[price] -= prices[price] * 0.05
        print(f"Updated price for item {price}: ${prices[price]:.2f}")
    
