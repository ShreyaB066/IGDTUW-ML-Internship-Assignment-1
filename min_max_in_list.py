# Write a python program that returns the minimum and maximum values in a list of numbers. 
input_list = [38, 1, 75, 10, 5]
min_element = input_list[0]
max_element = input_list[1]
for num in input_list:
    if num < min_element:
        min_element = num
    elif num > max_element:
        max_element = num

print("Minimum Element from the list:", min_element)
print("Maximum Element from the list:", max_element)