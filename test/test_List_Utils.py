import pytest

from functional.utils.List_Utils import FluentList


# Test cases for the FluentList class
def test_map():
    def add_one(x: int):
        return x + 1

    numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    fluentList: FluentList[int] = FluentList(numbers)

    assert fluentList.map(add_one).to_list() == [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


# If you want to run tests from the command line using pytest
if __name__ == "__main__":
    pytest.main()
