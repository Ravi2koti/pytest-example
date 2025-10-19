# main.py
import sys
from myapp.app import multiply_by_two, divide_by_two

def area_of_square(side: int) -> int:
    """Return the area of a square given one side."""
    return side * side


def main():
    """Main program that performs simple math operations."""
    num = int(input("Insert a number: "))
    print(f"The double of {num} is {multiply_by_two(num)}")
    print(f"The half of {num} is {divide_by_two(num)}")
    print(f"The area of a square with side {num} is {area_of_square(num)}")
    sys.exit(0)


if __name__ == "__main__":
    main()
