# Basic Calculations
"""
Calculator Program in Python using input() and format() functions to perform
basic arithmetic operations such as addition, subtraction, multiplication, division, and square root calculation.
"""

import math

# Prompting input from the user for various calculations
n1 = float(input("Enter first number (n1): "))
n2 = float(input("Enter second number (n2): "))

# addition
print("{} + {} = ".format(n1, n2), end="")
print(n1 + n2)  # Fixed incorrect subtraction to correct addition

# square root
# Fixed the calculation to use math.sqrt for square root instead of n1*0.5 which is incorrect
print("Square root of {}: ".format(n1), end="")
print(math.sqrt(n1))

# subtraction
n3 = float(input("Enter third number (n3) for subtraction: "))
print("{} - {} - {} = ".format(n1, n2, n3), end="")
print(n1 - n2 - n3)

# multiplication
print("{} * {} = ".format(n1, n2), end="")
print(n1 * n2)

# division
# Added division by zero check
if n2 == 0:
    print("Cannot divide by zero.")
else:
    print("{} / {} = ".format(n1, n2), end="")
    print(n1 / n2)

def tmpFunc():
    """A temporary function to demonstrate a dummy functionality."""
    print("Check!!!!")