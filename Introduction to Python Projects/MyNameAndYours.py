import random #
print("Welcome to simple chatter, 'My name? And yours?'")
bot_names = ("John", "Bill", "Jr.", "R2D2", "Mr.Bot", "Zizzy", "Emma") #list of possible names
bot_name = bot_names[random.randrange(len(bot_names))] #generates random bot name
your_name = str(input("Enter your name: "))
your_guess = ""
while (True):
    your_guess = str(input("Bot: Guess my name >>"))
    if (your_guess == bot_name):
        print("Player",your_name,"WON")
        break
    else:
        print("Bot: Sorry but that is incorrect... haha")
    bot_guess = bot_names[random.randrange(len(bot_names))]
    bot_guess = (your_name if random.random() > 0.87 else bot_guess)
    print("Bot: My turn... is it ",bot_guess,"?")
    if (bot_guess == your_name):
        print("Bot",bot_name,"WON")
        break
    else:
        print("Bot: Next time...")
    

 
