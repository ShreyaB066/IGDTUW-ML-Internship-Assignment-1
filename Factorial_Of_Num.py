# Write a python program that calculates the factorial of a given number. 
num = int(input("Enter number: "))
fact = 1
# Check if the number is negative, positive, or zero
if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1, num + 1):
        fact *= i
    print("The factorial is :",fact)