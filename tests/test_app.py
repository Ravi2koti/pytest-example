import sys
import os
import pytest

# --- Add project root directory to sys.path for GitHub Actions runner ---
# This works even when main.py is in the repository root
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

# --- Import functions ---
from myapp.app import multiply_by_two, divide_by_two

# Use importlib to dynamically import main.py safely
import importlib.util

main_path = os.path.join(ROOT_DIR, "main.py")
spec = importlib.util.spec_from_file_location("main", main_path)
main = importlib.util.module_from_spec(spec)
spec.loader.exec_module(main)


# --- Fixtures ---
@pytest.fixture
def numbers():
    a = 10
    b = 20
    return [a, b]


# --- Tests ---
class TestApp:

    def test_division(self, numbers):
        """Test divide_by_two() from myapp.app"""
        res = divide_by_two(numbers[1])
        assert res == numbers[0]

    def test_multiplication(self, numbers):
        """Test multiply_by_two()"""
        res = multiply_by_two(numbers[0])
        assert res == numbers[1]

    def test_area_student_id(self):
        """Test area_of_square() dynamically loaded from main.py"""
        side = 70  # last two digits of your student ID
        expected = side * side
        assert main.area_of_square(side) == expected
