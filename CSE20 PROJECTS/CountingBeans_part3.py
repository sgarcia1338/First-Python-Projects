num_of_jars = int(input("Enter number of jars: "))
if num_of_jars <= 0:
    exit()
elif num_of_jars > 0:
    number_of_jar = []
    mason_jar_list = []
    for count in range(0,num_of_jars):
        print("Adding another jar to calculate for...")
        number_of_jar.append(num_of_jars)
        mason_jar_type = str(input("Type in brackets [cup], [half], [quart], [pint]: "))
        mason_jar_list.append(mason_jar_type)

for mason_jar_type in mason_jar_list:
    beans_total = 0
    bean_per_cubic = 0.06545
    beans_current_volume = 0
    if (mason_jar_type == "cup"):
        print("Working with a cup size")
        print("Let's try to estimate number of beans in the",mason_jar_type,"jar")
        mason_jar_volume = 14.4375
        while (beans_current_volume < mason_jar_volume):
            beans_total = beans_total + 1
            beans_current_volume = beans_current_volume + 0.06545
        print("Rough estimate of number of beans in",mason_jar_type,"is",beans_total,"")
    elif (mason_jar_type == "half"):
        print("Working with a half gallon size")
        print("Let's try to estimate number of beans in the",mason_jar_type,"jar")
        mason_jar_volume = 14.4375 * 8
        while (beans_current_volume < mason_jar_volume):
            beans_total = beans_total + 1
            beans_current_volume = beans_current_volume + 0.06545
        print("Rough estimate of number of beans in",mason_jar_type,"is",beans_total,"")
    elif (mason_jar_type == "quart"):
        print("Working with a quart size")
        print("Let's try to estimate number of beans in the",mason_jar_type,"jar")
        mason_jar_volume = 14.4375 * 4
        while (beans_current_volume < mason_jar_volume):
            beans_total = beans_total + 1
            beans_current_volume = beans_current_volume + 0.06545
        print("Rough estimate of number of beans in",mason_jar_type,"is",beans_total,"")
    else:
        print("Working with a pint size")
        print("Let's try to estimate number of beans in the",mason_jar_type,"jar")
        mason_jar_volume = 14.4375 * 2
        while (beans_current_volume < mason_jar_volume):
            beans_total = beans_total + 1
            beans_current_volume = beans_current_volume + 0.06545
        print("Rough estimate of number of beans in",mason_jar_type,"is",beans_total,"")





