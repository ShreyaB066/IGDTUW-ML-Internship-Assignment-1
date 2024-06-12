# Write a python program that removes all punctuation from a given string.
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

input_str = input("Enter the string: ")
no_punc = ""
for char in input_str:
   if char not in punctuations:
       no_punc = no_punc + char

print(no_punc)