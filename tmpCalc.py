# Basic Calculations
# Calculator Program in Python using input() and format() functions

import math

def perform_calculations():
    """
    Performs basic arithmetic calculations such as addition, subtraction,
    multiplication, and division, and calculates the square root of a number.
    """
    
    # Prompting input from the user for two numbers
    n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the second number: "))
    
    # Addition
    addition_result = n1 + n2
    print("{} + {} = {}".format(n1, n2, addition_result))

    # Square root
    # NOTE: The square root calculation previously was incorrect, as it used n1*0.5 to attempt to find a square root.
    # The correct method using the math.sqrt function is used now.
    square_root = math.sqrt(n1)
    print("Square root of {} is: {}".format(n1, square_root))

    # Subtraction
    # Assuming n3 needs to be taken as input as well, it was not present in the original code.
    n3 = float(input("Enter the third number (for subtraction): "))
    subtraction_result = n1 - n2 - n3
    print("{} - {} - {} = {}".format(n1, n2, n3, subtraction_result))

    # Multiplication
    multiplication_result = n1 * n2
    print("{} * {} = {}".format(n1, n2, multiplication_result))

    # Division
    # Added error handling for division by zero.
    if n2 == 0:
        print("Error: Cannot divide by zero.")
    else:
        division_result = n1 / n2
        print("{} / {} = {}".format(n1, n2, division_result))

# Run the function to perform calculations
if __name__ == "__main__":
    perform_calculations()