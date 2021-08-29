import random
cust_bag = []
response_gift = []
def purchaseitems():
    items_purch = input(str("What do you want to buy? "))
    cust_bag.append(items_purch)
def giftcard():
    buy_gift = input(str("Do you want to buy a giftcard? (yes/no) "))
    if buy_gift == "yes":
        cust_bag.append("GIFT CARD")
    response_gift.append(buy_gift)

print("Hello shopper!")
buy_items = input(str("Do you want to order any items? (yes/no) "))

if buy_items == "yes":
    print("Wohoo! Let's shop :)")
    cust_name = input(str("Welcome customer: "))
    purchaseitems()
    giftcard()
    continue_shop = input(str("Do you want to continue shopping "))
    while continue_shop == "yes":
        purchaseitems()
        giftcard()
        continue_shop = input(str("Do you want to continue shopping "))
        continue
    else:
        if "yes" in response_gift:
            print("Yay, you bought our GIFT CARD! You get a 10% discount on all of your items!")
        for item in cust_bag:
            print("You have: ",str(item))
        print("Come again ", cust_name)
else:
    print("Ok, bye :(")


