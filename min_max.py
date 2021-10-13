#name: Cassidy Ward
#date: 10/13/2021
#description: This program asks the user to enter how many numbers they'd like to input, then asks the user to enter each desired number. The program then gives the min and max values of the user input

N=int(input("How many integers would you like to enter?\n"))
print("Please enter "+str(N)+" integers.")
firstVal=0
#Get first value from user and assign to minVal
minVal=int(input())
maxVal=0
#Loop through rest of the user inputs
for i in range(0,N-1):
    x=int(input())
if x<minVal:
    minVal=x;
if x>maxVal:
    maxVal=x;

#Print min and max values
print("min:",minVal)
print("max:",maxVal)
