# Write a program that reads the content of a text file and prints it to the 
# console.
f = open('myfile.txt', 'r')
data = f.read()
print(data)
f.close()