#name: Cassidy Ward
#date: 10/13/2021
#description: This program asks the user to enter how many numbers they'd like to input, then asks the user to enter each desired number. The program then gives the min and max values of the user input

num_1=int(input("How many integers would you like to enter?\n"))
print("Please enter "+str(num_1)+" integers.")
firstVal=0

minVal=int(input())
maxVal=0

x=int(input())
if x<minVal:
minVal=x;
if x>maxVal:
maxVal=x;


print("min: ",minVal)
print("max: ",maxVal)
