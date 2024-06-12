# Write a program that reads data from a CSV file and prints it to the 
# console. 
import csv
file = open('data.csv', 'r')
lines = csv.reader(file)
for line in lines:
    print(line)
file.close()
