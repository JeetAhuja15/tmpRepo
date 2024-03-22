# Basic Calculations
"""
Calculator Program in Python for performing basic arithmetic operations
such as addition, subtraction, multiplication, and division.
"""

# Adding three numbers and prompting input from the user
a = 2
b = 3
c = 6
print("Sum of a, b, and c is:", a+b+c)

# Perform addition
n1 = float(input("Enter first number for addition: "))
n2 = float(input("Enter second number for addition: "))
print("{} + {} = {}".format(n1, n2, n1 + n2))

# Perform subtraction
n1 = float(input("Enter first number for subtraction: "))
n2 = float(input("Enter second number for subtraction: "))
n3 = float(input("Enter third number for subtraction: "))
print("{} - {} - {} = {}".format(n1, n2, n3, n1 - n2 - n3))

# Perform multiplication
n1 = float(input("Enter first number for multiplication: "))
n2 = float(input("Enter second number for multiplication: "))
print("{} * {} = {}".format(n1, n2, n1 * n2))

# Perform division
n1 = float(input("Enter first number for division: "))
n2 = float(input("Enter second number for division: "))
# Ensure n2 is not zero to avoid ZeroDivisionError
if n2 == 0:
    print("Cannot divide by zero, please enter a non-zero number")
else:
    print("{} / {} = {}".format(n1, n2, n1 / n2))

# A temporary function (Assuming it is used for some internal checks)
def tmpFunc():
    # It is good practice to document what this function actually does.