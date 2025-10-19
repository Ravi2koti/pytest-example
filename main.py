import sys
from myapp.app import multiply_by_two, divide_by_two


def area_of_square(side):
    """
    Calculate and return the area of a square.
    This is used in test_app.py to verify student ID–based area calculation.
    """
    return side * side


def main():
    """
    Entry point of the program.
    Asks the user for a number, doubles it, halves it, and prints the results.
    """
    try:
        num = int(input("Insert a number: "))
        print("The double of %d is %d" % (num, multiply_by_two(num)))
        print("The half of %d is %d" % (num, divide_by_two(num)))
        sys.exit(0)
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        sys.exit(1)


if __name__ == "__main__":
    main()
