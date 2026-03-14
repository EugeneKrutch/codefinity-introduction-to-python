# List of products on promotion for each weekday
daily_promotions = ["Milk", "Eggs", "Bread", "Apples", "Oranges"]

# List of weekdays corresponding to the promotions
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

for promotion in range(5):
    product = daily_promotions[promotion]
    weekday = weekdays[promotion]
    print(f"{weekday}: Promotion on {product}")