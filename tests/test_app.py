import pytest
from myapp.app import divide_by_two


class TestApp:

    def test_division(self, numbers=[10, 20]):
        """Test divide_by_two function."""
        res = divide_by_two(numbers[1])
        assert res == numbers[0]

    def test_area_student_id(self):
        """Test area_of_square using last two digits of student ID (70)."""
        # Import function dynamically from main.py
        from myapp.main import area_of_square
        
        side = 70  # last two digits of your student ID
        expected = side * side
        assert area_of_square(side) == expected
