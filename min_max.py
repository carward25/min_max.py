# Cassidy Ward

# 10/12/2021

# Description: This program asks the user to enter how many numbers they'd like to input, then asks the user to enter
# each desired number. The program then gives the min and max values of the user input

num_1 = int(input("How many integers would you like to enter?"))
print("Please enter", num_1, "integers.")
min = int(input())
max = min
for i in range(1, num_1):
    number = int(input())  
    if number > max:
        max = number
    if number < min:
        min = number

print("min: ", min)
print("max: ", max)
