import sys
import os
import pytest

# --- Ensure GitHub Actions can find the root module (main.py) ---
# Adds the project root folder to Python's import search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# --- Import application functions ---
from myapp.app import multiply_by_two, divide_by_two
from main import area_of_square


# --- Fixtures ---
@pytest.fixture
def numbers():
    a = 10
    b = 20
    return [a, b]


# --- Test Class ---
class TestApp:

    def test_division(self, numbers):
        """Test divide_by_two() from myapp.app"""
        res = divide_by_two(numbers[1])
        assert res == numbers[0]

    def test_multiplication(self, numbers):
        """Extra test for multiply_by_two()"""
        res = multiply_by_two(numbers[0])
        assert res == numbers[1]

    def test_area_student_id(self):
        """Test area_of_square() from main.py using student ID digits"""
        side = 70  # last two digits of your student ID (101002870 → 70)
        expecte
