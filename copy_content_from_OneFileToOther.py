# Write a program that copies the contents of one text file to another. 
with open("data.txt", "r") as f:
    lines = f.readlines()
with open("empty.txt", "w") as g:
    for line in lines:
        g.write(line)

print("Contents copied successfully!")