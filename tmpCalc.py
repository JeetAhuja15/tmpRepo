# Basic Calculations
# Calculator Program in Python demonstrating basic arithmetic operations

def cube(number):
    """Return the cube of the given number."""
    return number * number * number

def add(n1, n2):
    """Return the sum of two numbers."""
    return n1 + n2

def subtract(n1, n2, n3=0):
    """Return the difference between the first number and the sum of the subsequent numbers."""
    return n1 - n2 - n3

def multiply(n1, n2):
    """Return the product of two numbers."""
    return n1 * n2

def divide(n1, n2):
    """Return the division of the first number by the second."""
    return n1 / n2

# Prompting input from the user
# Assuming user input is going to be properly provided as numeric values
n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
n3 = float(input("Enter the third number (optional) for subtraction, skip if not required: ") or 0)

# Perform calculations
addition_result = add(n1, n2)
subtraction_result = subtract(n1, n2, n3)
multiplication_result = multiply(n1, n2)
division_result = divide(n1, n2)
cube_result = cube(n2)

# Display results
print("{} + {} = {}".format(n1, n2, addition_result))
print("{} - {} - {} = {}".format(n1, n2, n3, subtraction_result))
print("{} * {} = {}".format(n1, n2, multiplication_result))
print("{} / {} = {}".format(n1, n2, division_result))
print("Cube of {}: {}".format(n2, cube_result))