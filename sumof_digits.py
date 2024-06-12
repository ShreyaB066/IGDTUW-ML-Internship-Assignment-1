# Write a python program that calculates the sum of the digits of a given 
# number.
n = int(input("Enter the number: "))
def Sum_of_digits(n): 
    
    sum = 0
    while (n != 0): 
       
        sum = sum + (n % 10)
        n = n//10
       
    return sum


print(Sum_of_digits(n))