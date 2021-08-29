import random
random.randrange(0, 1)
def pizza_cart():
    item_purch = input(str("What do you want to buy? "))
    cost_pizza = float(4.95)
    if item_purch == "pizza":
        if random.random() <= 0.20:
            cost_pizza = cost_pizza * random.random()
            print("Congratulations! You are our lucky shopper!")
            print("You got a", random.random(), "discount on pizza")
        print("You got: pizza Cost: ",cost_pizza)
        numb_pizza.append(cost_pizza)
    else:
        print("Sorry we don't have", item_purch)
        return numb_pizza
numb_pizza = []
print("Welcome to Jack's Goody store!")
print("...make sure to check out our discount section")

user_name = input("What's your name? ")
print("Welcome ",user_name)
shopping_spree = input(str("Do you want to order any items? (yes/no) "))

if shopping_spree == "yes":
    pizza_cart()
    continue_shop = input(str("Do you want to continue shopping "))
    while continue_shop == "yes":
        pizza_cart()
        continue_shop = input(str("Do you want to continue shopping "))
        continue
    else:
        print("Total cost: ",sum(numb_pizza))
        print("Come again,", user_name)
else:
    print("Come again,", user_name)


