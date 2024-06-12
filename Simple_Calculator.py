# Write a program that acts as a simple calculator. It should take two 
# numbers and an operator (+, -, *, /) as input and print the result. 
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
operator = input("Enter the operator: ")
if operator == "+":
    print(a+b)
elif operator == "-":
    if a>b:
        print(a-b)
    else:
        print(b-a)
elif operator == "*":
    print(a*b)
elif operator == "/":
    print(a/b)
elif operator == "%":
    print(a%b)
else:
    print("Enter a valid operator.")