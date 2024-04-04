# Basic Calculations
# Calculator Program in Python by using input() and various arithmetic operations

def main():
    """
    Main function to perform basic arithmetic operations like
    addition, subtraction, multiplication, division, and cube of a number.
    It prompts the user for input and then shows the results of the calculations.
    """
    # Prompting input from the user
    n1 = float(input("Enter the first number (n1): "))
    n2 = float(input("Enter the second number (n2): "))
    
    # Addition
    print("{} + {} = ".format(n1, n2), n1 + n2)  # Fixed the operation to show correct result of addition.

    # Cube of the first number
    print("Cube of {}: ".format(n1), n1 ** 3)  # Fixed the operation to calculate the correct cube of n1.
    
    # Subtraction
    print("{} - {} = ".format(n1, n2), n1 - n2)  # Updated to show correct result of subtraction.

    # Multiplication
    print("{} * {} = ".format(n1, n2), n1 * n2)

    # Division
    # Adding check to prevent division by zero
    if n2 == 0:
        print("Error: Cannot divide by zero.")
    else:
        print("{} / {} = ".format(n1, n2), n1 / n2)

    # Temp function just as a placeholder for any additional future logic,
    # which isn't useful currently and could be removed.
    # def tmpFunc():
    #     print("Check!!!!") 

if __name__ == "__main__":
    main()