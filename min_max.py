#name: Cassidy Ward
#date: 10/12/2021
#description: This program asks the user to enter how many numbers they'd like to input, then asks the user to enter
# each desired number. The program then gives the min and max values of the user input

num_1 = int(input("How many integers would you like to enter?"))
print("Please enter", num_1, "integers.")
_min = int(input())
_max = int(input())
for i in range(1, num_1):
    number = int(input())  
    if number > _max:
        _max = number
    if number < _min:
        _min = number

print("min: ", _min)
print("max: ", _max)
