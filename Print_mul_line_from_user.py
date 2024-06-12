# Write a program that reads multiple lines of input from the user until they 
# enter an empty line, then prints all the lines.
lines = []
while True:
    input_line = input("Enter a line: ")
    if not input_line:
        break
    lines.append(input_line)

for input_line in lines:
    print(input_line)