# Write a program that converts temperature from Celsius to Fahrenheit 
# and vice versa based on user input. 
temp = int(input("Enter the temperature: "))
unit = input("Enter the unit of temperature(C/F): ")
if unit == "C":
    f = (temp * 9/5) + 32
    print("The temperature in Fahrenheit is: ",f)
elif unit == "F":
    c = (temp - 32) * 5/9
    print("The temperature in Celsius is: ",c)
else:
    print("Invalid input! please enter either C or F")
