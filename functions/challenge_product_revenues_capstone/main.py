# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold
def calculate_revenue(prices, quantities_sold):
    revenue = []
    for item in range(len(prices)):
        item_revenue = prices[item]* quantities_sold[item]
        revenue.append(item_revenue)
    return revenue
list_of_revenues = calculate_revenue(prices, quantities_sold)
revenue_per_product1 = tuple(zip(products, list_of_revenues))
#revenue_per_product = list(revenue_per_product)
print(revenue_per_product1)
revenue_per_product = sorted(revenue_per_product1)
def formatted_output(revenue_per_product1):
    for item in range(len(revenue_per_product)):
        print(f"{revenue_per_product[item][0]} has total revenue of ${revenue_per_product[item][1]}")
    return revenue_per_product

formatted_output(revenue_per_product)
    



# Example of expected output line (do not remove):
#print(f"{revenue[0]} has total revenue of ${revenue[1]}")