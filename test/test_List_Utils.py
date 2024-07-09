from typing import List

import pytest

from functional.utils.List_Utils import FluentList


def add_one(x: int):
    return x + 1


# Test cases for the FluentList class
def test_map():
    numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    fluentList: FluentList[int] = FluentList(numbers)

    assert fluentList.map(add_one).to_list() == [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


def test_flat_map():
    def add_one_list(x: int) -> List[int]:
        return [x + 1]

    numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    fluentList: FluentList[int] = FluentList(numbers)

    assert fluentList.flat_map(add_one_list).to_list() == [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


def test_fold_left():

    def add_one_list(x: int, y: int) -> int:
        return x + y

    numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    fluentList: FluentList[int] = FluentList(numbers)

    assert fluentList.fold_left(0)(add_one_list) == 55


# If you want to run tests from the command line using pytest
if __name__ == "__main__":
    pytest.main()
