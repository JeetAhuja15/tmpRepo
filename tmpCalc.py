# Basic Calculations
"""Calculator Program in Python demonstrating basic arithmetic operations."""

# Function to add three numbers
def add_numbers(a, b, c):
    """Function to add three numbers and return the sum."""
    return a + b + c

# Function to subtract two or three numbers
def subtract_numbers(n1, n2, n3=0):
    """Function to subtract two or three numbers and return the difference."""
    return n1 - n2 - n3

# Function to multiply two numbers
def multiply_numbers(n1, n2):
    """Function to multiply two numbers and return the product."""
    return n1 * n2

# Function to divide two numbers
def divide_numbers(n1, n2):
    """Function to divide two numbers and return the quotient. Handles division by zero."""
    if n2 == 0:
        return "Error! Division by zero."
    else:
        return n1 / n2

# Main program starts here
if __name__ == '__main__':
    # Input for addition
    print("Enter three numbers to add:")
    a = int(input("Enter first number (a): "))
    b = int(input("Enter second number (b): "))
    c = int(input("Enter third number (c): "))
    print("Result of addition: {} + {} + {} = {}".format(a, b, c, add_numbers(a, b, c)))

    # Input for subtraction
    print("\nEnter two numbers to subtract:")
    n1 = int(input("Enter first number (n1): "))
    n2 = int(input("Enter second number (n2): "))
    print("Result of subtraction: {} - {} = {}".format(n1, n2, subtract_numbers(n1, n2)))

    # Input for multiplication
    print("\nEnter two numbers to multiply:")
    n1 = int(input("Enter first number (n1): "))
    n2 = int(input("Enter second number (n2): "))
    print("Result of multiplication: {} * {} = {}".format(n1, n2, multiply_numbers(n1, n2)))

    # Input for division
    print("\nEnter two numbers to divide:")
    n1 = int(input("Enter first number (n1): "))
    n2 = int(input("Enter second number (n2): "))
    result = divide_numbers(n1, n2)
    if isinstance(result, str):
        print(result)
    else:
        print("Result of division: {} / {} = {}".format(n1, n2, result))