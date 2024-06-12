# Write a program in python that converts a string into a list of its characters.
def string_to_list_of_char(s):
    return list(s)

input_string = input("Enter a string: ")
char_list = string_to_list_of_char(input_string)
print("List of characters:", char_list)