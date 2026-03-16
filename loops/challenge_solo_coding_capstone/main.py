# Inventory dictionary with stock, price, and discount price
inventory = {
    "Bread": [42, 1.20, 0.99],  # "Item": [current stock, regular price, discounted price]
    "Eggs": [225, 2.12, 1.99],  # Eggs should be sold at a discount
    "Apples": [9, 1.50, 1.35]   # Apples need to be restocked
}

low_stock = 30
high_stock = 100

for item in inventory:
    if inventory[item][0] < low_stock:
        print(f"{item} need restocking.")
    elif inventory[item][0] > high_stock:
        discounted_price = inventory[item][2]
        print(f"{item} should be sold at the discounted price of {discounted_price}.")

    elif inventory[item][0] > low_stock and inventory[item][0] < high_stock:
        regular_price = inventory[item][1]
        print(f"{item} should be sold at the regular price of {regular_price}.")
        