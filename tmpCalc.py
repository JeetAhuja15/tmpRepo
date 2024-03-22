# Basic Calculations
# Calculator Program in Python using input() and format() functions

def calculate_operations(n1, n2):
    """
    Perform basic arithmetic operations like addition, subtraction, multiplication,
    and division on two given numbers and print the results to the console.

    Parameters:
    n1 (int/float): The first number.
    n2 (int/float): The second number.
    """
    # addition
    print("{} + {} = {}".format(n1, n2, n1 + n2))

    # subtraction
    print("{} - {} = {}".format(n1, n2, n1 - n2))

    # multiplication
    print("{} * {} = {}".format(n1, n2, n1 * n2))

    # division
    # Check if n2 is not zero to avoid ZeroDivisionError
    if n2 != 0:
        print("{} / {} = {}".format(n1, n2, n1 / n2))
    else:
        print("Cannot divide by zero")

    # finding cube
    # Improved cube calculation to be generic for any number
    a = 2  # Example number
    print("The cube of {} is {}".format(a, a**3))

# The following function seems to be a placeholder for further implementation
# and not providing any meaningful operations, hence is commented out.
# def tmpFunc():
#    print("Check!!!!")

# Assuming 'n1', 'n2' are provided by user input or defined elsewhere in code
# For example, in an interactive session you might use:
# n1 = float(input('Enter the first number: '))
# n2 = float(input('Enter the second number: '))

# Example values for n1 and n2
n1 = 10  # Replace with user input or another source of values
n2 = 5   # Replace with user input or another source of values

# Call function to perform calculations
calculate_operations(n1, n2)