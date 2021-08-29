my_file = open("lab07_out.txt", "w+")
my_file.write("Start of Lab07_out text file... \n")
my_file.write("-------------------------------\n")
while True:
    if (input("Continue adding to file? (yes/no) ") == "yes"):
        text = input("Enter text: ")
        my_file.write(text + "\n")
    else:
        break
my_file.close()
with open("lab07_out.txt") as fh:
    for line in fh:
        print(line, end="")
        
