# Write a program that takes a number from the user and prints whether the number is even or odd.

# Function to check if the number is even or odd
def CheckOddOrEven(inputNumber):
    if inputNumber % 2 == 0:
        return "EVEN"
    else:
        return "ODD"


# Take a number from the user
inputString = input("Please enter a integer value: ")

# Convert the input string to integer
input1 = int(inputString)

# Check if the number is even or odd
numberType = ""

# Check if the number is even or odd
if input1 % 2 == 0:
	numberType = "EVEN" 
else:
    numberType = "ODD"

# Print the result
print("The Number is ", numberType)