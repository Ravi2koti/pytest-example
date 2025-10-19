import pytest
from myapp.app import divide_by_two
import importlib.util
import sys
import os


class TestApp:
    def test_division(self, numbers=[10, 20]):
        """Test divide_by_two function."""
        res = divide_by_two(numbers[1])
        assert res == numbers[0]

    def test_area_student_id(self):
        """Test area_of_square using last two digits of student ID (70)."""
        # Dynamically import main.py from the root directory
        root_path = os.path.dirname(os.path.dirname(__file__))
        main_path = os.path.join(root_path, "main.py")

        spec = importlib.util.spec_from_file_location("main", main_path)
        main = importlib.util.module_from_spec(spec)
        sys.modules["main"] = main
        spec.loader.exec_module(main)

        side = 70  # last two digits of your student ID
        expected = side * side
        assert main.area_of_square(side) == expected 
