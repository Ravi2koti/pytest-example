import pytest

from myapp.app import multiply_by_two, divide_by_two


@pytest.fixture
def numbers():
    a = 10
    b = 20
    return [a,b]


class TestApp:
    def test_division(self, numbers):
        res = divide_by_two(numbers[1])
        assert res == numbers[0]

    def test_area_student_id(self):
        from myapp.main import area_of_square  # use the correct import path
        side = 70  # last two digits of your student ID
        expected = side * side
        assert area_of_square(side) == expected


