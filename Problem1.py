restaurant_menu = {
"Starters": {"Soup": 5.99, "Bruschetta": 6.50},
"Main Course": {"Steak": 15.99, "Salmon": 13.99},
"Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

restaurant_menu["Beverages"] = {"Coke":1.99, "Latte": 3.50}
restaurant_menu["Main Course"]["Steak"] = 18.99
del restaurant_menu["Starters"]["Bruschetta"]

print(restaurant_menu)

