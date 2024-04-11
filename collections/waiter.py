# Waiter program

menu = {
    "starters": ["Spaghetti", "Gnocchi", "Breadsticks", "Soup of the day"],
    "starters_prices": [5, 4.50, 1, 3],
    "mains": ["Steak", "Salmon", "Lamb"],
    "mains_prices": [8, 9, 8],
    "desserts": ["Gelato", "Tiramisu", "Panettone"],
    "desserts_prices": [3, 3, 3]
}

print("Hello and welcome to La Nonna. We hope you're having a good time. Are you ready to order?")

print("The starters we offer today include: Spaghetti, Gnocchi, Breadsticks, Soup of the Day")
starter = input("I'd like: ")
starter_price = menu["starters_prices"][menu["starters"].index(starter)]
customer_order_list = [starter]

print("Ok great choice. The mains we have today are: Steak, Salmon, Lamb. All come with our complimentary salad")
main = input("I'd like: ")
main_price = menu["mains_prices"][menu["mains"].index(main)]
customer_order_list.append(main)

print("Ok. Finally for dessert we have: Gelato, Tiramisu, Panettone")
dessert = input("I'd like: ")
dessert_price = menu["desserts_prices"][menu["desserts"].index(dessert)]
customer_order_list.append(dessert)

print(f"Ok so we have {starter} for the starter, {main} as the main and {dessert} as the dessert")

# add index of food to bill
print(f"So that's £{starter_price:.2f} for the {starter}, £{main_price:.2f} for the {main} and £{dessert_price:.2f} for the {dessert}.")
print(f"And your total comes to £{starter_price+main_price+dessert_price:.2f}")
