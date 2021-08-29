mason_jar_type = str(input("Type in brackets [cup], [half], [quart], [pint]: "))

if (mason_jar_type == "cup"):
    print("Working with a cup size")
    mason_jar_volume = 14.4375
elif (mason_jar_type == "half"):
    print("Working with a half gallon size")
    mason_jar_volume = 14.4375 * 8
elif (mason_jar_type == "quart"):
    print("Working with a quart size")
    mason_jar_volume = 14.4375 * 4
else:
    print("Working with a pint size")
    mason_jar_volume = 14.4375 * 2

print("Let's try to estimate number of beans in the",mason_jar_type,"jar")

beans_total = 0
bean_per_cubic = 0.06545
beans_current_volume = 0

while (beans_current_volume < mason_jar_volume):
    beans_total = beans_total + 1
    beans_current_volume = beans_current_volume + 0.06545
    continue
else:
    print("Rough estimate of number of beans in",mason_jar_type,"is",beans_total,"")
    
    
    
    



