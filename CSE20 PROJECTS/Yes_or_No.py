your_height_in_feet = float(input("Enter your height in feet: "))

current_temperature_in_farenheit = float(input("Enter current temperature in Fahrenheit: "))

your_height_in_meters = ( your_height_in_feet * 0.3048 )

current_temperature_in_celsius = ( current_temperature_in_farenheit - 32 )*(9.0/5.0)

if ( your_height_in_meters > current_temperature_in_celsius ):
    print("Wow, your height is larger than the temperature!")
else:
    print("Wow, the temperature is so hot!")

if ( your_height_in_feet > your_height_in_meters ):
    print("Good, we did the conversion correct for feet to meters!")
elif ( your_height_in_feet == 0 ):
    print("Interesting... should only happen if height is zero???")
else:
    print("Oh no, our math is wrong :(")

