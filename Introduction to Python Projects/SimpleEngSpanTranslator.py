eng_to_spa_dict = {"hello":"hola", "bye":"adios", "big":"grande", "small":"pequeno", "student":"estudiante", "teacher":"profesor"}
print(eng_to_spa_dict)
print(eng_to_spa_dict.keys())
print(eng_to_spa_dict.values())

add_word = input("Add another word? (yes/no): ")
while True:
    if add_word == "yes":
        print(eng_to_spa_dict)
        eng_word = input("Enter English word: ")
        spa_word = input("Enter Spanish translation: ")
        eng_to_spa_dict[eng_word] = spa_word
        add_word = input("Add another word? (yes/no)")
    else:
        break
print(eng_to_spa_dict)
transsent = input(str("Enter an English sentence: "))
translist = transsent.split()
for elem in translist:
    if elem in eng_to_spa_dict.keys():
        print("Found:", "<", elem ,">", "translated to: ", "<", eng_to_spa_dict[elem] ,">")
    
