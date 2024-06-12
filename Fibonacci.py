# Write a python program that generates the first n numbers in the 
# Fibonacci sequence.
def fibo(n):
    num_1 = 0
    num_2 = 1
    no_of_terms = 0
    while no_of_terms < n:
        print(num_1, end=" ")
        nth_term = num_1 + num_2
        num_1 = num_2
        num_2 = nth_term
        no_of_terms += 1

t = int(input("Enter the number of terms: "))
fibo(t) 