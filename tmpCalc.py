# Basic Calculations
# Calculator Program in Python by using input() and format() functions

def calculate_sum(a, b, c):
    """Calculate and print the sum of three numbers."""
    return a + b + c

# Adding three numbers using the calculate_sum function
a, b, c = 2, 3, 6
print("Sum of numbers: ", calculate_sum(a, b, c))

# Ask for user input for more operations
n1 = float(input("Enter first number (n1): "))
n2 = float(input("Enter second number (n2): "))
n3 = float(input("Enter third number (n3): "))

# Addition
result_add = n1 + n2
print("{} + {} = {}".format(n1, n2, result_add))

# Subtraction
result_sub = n1 - n2
print("{} - {} = {}".format(n1, n2, result_sub))

# Multiplication
result_mul = n1 * n2
print("{} * {} = {}".format(n1, n2, result_mul))

# Division
# Check for division by zero
if n2 == 0:
    print("Cannot divide by 0")
else:
    result_div = n1 / n2
    print("{} / {} = {}".format(n1, n2, result_div))

# Additional function to showcase functionality, if needed
def tmpFunc():
    """A temporary function to showcase the 'print' statement."""
    print("Check!!!!")