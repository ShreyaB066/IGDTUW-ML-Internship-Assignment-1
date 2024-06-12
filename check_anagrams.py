# Write a python program that checks if two strings are anagrams of each 
# other.
input_str1 = input("Enter the first string: ")
input_str2 = input("Enter the second string: ")
sorted_str1 = sorted(input_str1)
sorted_str2 = sorted(input_str2)
if sorted_str1 == sorted_str2:
    print("Yes! The entered strings are anagrams.")
else:
    print("No! The entered strings are not anagrams.")