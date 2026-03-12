grocery_inventory = {
    "Milk" : ("Dairy", 3.50, 8),
    "Eggs" : ("Dairy", 5.50, 30),
    "Bread" : ("Bakery", 2.99, 15),
    "Apples" : ("Produce", 1.50, 50)
}
if grocery_inventory["Eggs"][1] > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    grocery_eggs = grocery_inventory["Eggs"]
    temp_list1 = list(grocery_eggs)
    temp_list1[1] -= 1
    grocery_eggs_upd = tuple(temp_list1)
    grocery_inventory["Eggs"] = grocery_eggs_upd
else:
    print("The price of Eggs is reasonable.")

grocery_inventory.update({"Tomatoes" : ("Produce", 1.20, 30)})
print("Inventory after adding Tomatoes: ", grocery_inventory)
if grocery_inventory["Milk"][2] < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    grocery_milk = grocery_inventory["Milk"]
    temp_list2 = list(grocery_milk)
    temp_list2[2] += 20
    grocery_milk_upd = tuple(temp_list2)
    grocery_inventory["Milk"] = grocery_milk_upd
else:
    print("Milk has sufficient stock.")

if grocery_inventory["Apples"][1] > 2:
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price.")

print("Updated inventory: ", grocery_inventory)