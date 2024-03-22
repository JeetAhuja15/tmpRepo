# Basic Calculations
"""
Calculator Program in Python by using print and arithmetic operations.
This program calculates addition, cube, subtraction, multiplication, and division.
"""

# Add two numbers and print the result
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
print("{} + {} = {}".format(n1, n2, n1 + n2))

# Find and print the cube of a given number
a = 2
print("The cube of {} is {}".format(a, a**3))

# Subtract three numbers and print the result
n3 = int(input("Enter the third number: "))
print("{} - {} - {} = {}".format(n1, n2, n3, n1 - n2 - n3))

# Multiply two numbers and print the result
print("{} * {} = {}".format(n1, n2, n1 * n2))

# Divide two numbers and print the result
print("{} / {} = {}".format(n1, n2, n1 / n2))

# Temporary function just for demonstration (Potentially to be removed)
def tmpFunc():
    print("Check!!!!") 

# Note: This code assumes that n1, n2, and n3 are integers and n2 is not zero for division. 
# It's generally a good practice to include error handling for division by zero and invalid inputs.