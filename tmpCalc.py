# Basic Calculations
# Calculator Program in Python by using input() and format() functions


def add_numbers(a, b, c):
    """
    Adds three numbers and prints the result.

    Parameters:
    a (int): First number.
    b (int): Second number.
    c (int): Third number.
    """
    print(f"{a} + {b} + {c} = {a + b + c}")


def subtract_numbers(n1, n2, n3=0):
    """
    Subtracts two or three numbers and prints the result.

    Parameters:
    n1 (int): First number.
    n2 (int): Second number.
    n3 (int): Third number (optional).
    """
    if n3:
        print(f"{n1} - {n2} - {n3} = {n1 - n2 - n3}")
    else:
        print(f"{n1} - {n2} = {n1 - n2}")


def multiply_numbers(n1, n2):
    """
    Multiplies two numbers and prints the result.

    Parameters:
    n1 (int): First number.
    n2 (int): Second number.
    """
    print(f"{n1} * {n2} = {n1 * n2}")


def divide_numbers(n1, n2):
    """
    Divides the first number by the second and prints the result.

    Parameters:
    n1 (int): First number.
    n2 (int): Second number.
    """
    if n2 != 0:
        print(f"{n1} / {n2} = {n1 / n2}")
    else:
        print("Cannot divide by zero.")


# Example usage
if __name__ == "__main__":
    # Adding three numbers
    a, b, c = 2, 3, 6
    add_numbers(a, b, c)

    # Replace this with user input or another mechanism to set values
    n1, n2, n3 = 10, 5, 2

    # Perform basic calculations
    subtract_numbers(n1, n2)
    subtract_numbers(n1, n2, n3)
    multiply_numbers(n1, n2)
    divide_numbers(n1, n2)