# Write a program in python that checks if a string starts with a given prefix 
# or ends with a given suffix.
prefix = input("Enter the prefix: ")
suffix = input("Enter the suffix: ")
user_string = input("Enter a string: ")

def check_starts_with(string, prefix):
    return string.startswith(prefix)

def check_ends_with(string, suffix):
    return string.endswith(suffix)

if check_starts_with(user_string, prefix):
    print("The string starts with the entered prefix.")
else:
    print(f"The string does not start with the entered prefix.")


if check_ends_with(user_string, suffix):
    print(f"The string ends with the entered suffix.")
else:
    print(f"The string does not end with the entered suffix")