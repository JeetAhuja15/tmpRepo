# Basic Calculations
# Calculator Program in Python by using input() and format() functions

def add_numbers(a, b, c):
    """Function to add three numbers"""
    return a + b + c

def subtract_numbers(a, b, c):
    """Function to subtract numbers"""
    return a - b - c

def multiply_numbers(a, b):
    """Function to multiply two numbers"""
    return a * b

def divide_numbers(a, b):
    """Function to divide two numbers"""
    if b != 0:
        return a / b
    else:
        print("Error: Cannot divide by zero.")
        return None

# Adding three numbers and displaying the result
a, b, c = 2, 3, 6
print(f"{a} + {b} + {c} = {add_numbers(a, b, c)}")

# Subtraction with two numbers, hardcoded for demo purposes
n1, n2, n3 = 10, 5, 2
print(f"{n1} - {n2} - {n3} = {subtract_numbers(n1, n2, n3)}")

# Multiplication with two numbers, hardcoded for demo purposes
print(f"{n1} * {n2} = {multiply_numbers(n1, n2)}")

# Division with two numbers, hardcoded for demo purposes
division_result = divide_numbers(n1, n2)
if division_result is not None:
    print(f"{n1} / {n2} = {division_result}")

def tmp_func():
    """Temporary function to demonstrate print statement"""