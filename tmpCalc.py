# Basic Calculations
"""
Calculator Program in Python to perform basic arithmetic operations
by using input() and format() functions.
"""

# Function to add three numbers
def add_three_numbers(a, b, c):
    return a + b + c

# Function to subtract numbers
def subtract_numbers(n1, n2, n3=0):  # Added default value for n3 to ensure backward compatibility
    return n1 - n2 - n3

# Function to multiply two numbers
def multiply_two_numbers(n1, n2):
    return n1 * n2

# Function to divide two numbers
def divide_two_numbers(n1, n2):
    if n2 != 0:  # Added condition to prevent division by zero
        return n1 / n2
    else:
        return "Error: Division by zero"

# Prompting the user for input
n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
n3 = float(input("Enter the third number: "))

# Performing calculations
sum_result = add_three_numbers(n1, n2, n3)
sub_result = subtract_numbers(n1, n2, n3)
mul_result = multiply_two_numbers(n1, n2)
div_result = divide_two_numbers(n1, n2)

# Displaying the results
print("{} + {} + {} = {}".format(n1, n2, n3, sum_result))
print("{} - {} - {} = {}".format(n1, n2, n3, sub_result))
print("{} * {} = {}".format(n1, n2, mul_result))
print("{} / {} = {}".format(n1, n2, div_result))
```