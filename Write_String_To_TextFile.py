# Write a program that takes a string input from the user and writes it to a 
# text file.
data = input("Enter your data: ")
f=open('myfile.txt','w')
f.write(data)
f.close()