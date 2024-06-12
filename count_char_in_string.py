# Write a program in python that counts the frequency of each character in 
# a string.
input_str = input("Enter the string: ")
freq = {}

for char in input_str:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print("Frequency of the character:", freq)