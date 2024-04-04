# Basic Calculations
# Calculator Program in Python by using input() and format() functions

def perform_calculations(n1, n2, n3):
    """
    Perform basic arithmetic calculations such as addition, subtraction,
    multiplication, division, and exponentiation.
    Args:
    n1 (int/float): The first operand for calculations.
    n2 (int/float): The second operand for calculations.
    n3 (int/float): The third operand for subtraction.
    Returns:
    None
    """

    # Addition
    sum_result = n1 + n2
    print(f"{n1} + {n2} = {sum_result}")

    # Subtraction
    sub_result = n1 - n2 - n3
    print(f"{n1} - {n2} - {n3} = {sub_result}")

    # Multiplication
    mult_result = n1 * n2
    print(f"{n1} * {n2} = {mult_result}")

    # Division
    if n2 != 0:
        div_result = n1 / n2
        print(f"{n1} / {n2} = {div_result}")
    else:
        print("Error: Cannot divide by zero.")

    # Exponentiation
    a = 2
    b = 3
    exp_result = a ** b
    print(f"{a} raised to the power of {b} = {exp_result}")

# Example usage:
# Assuming some predefined values for n1, n2, and n3
n1 = 10
n2 = 5
n3 = 2

perform_calculations(n1, n2, n3)