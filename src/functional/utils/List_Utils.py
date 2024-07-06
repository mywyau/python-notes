from functools import reduce
from typing import List, Callable, TypeVar, Generic

T = TypeVar('T')
U = TypeVar('U')


class FluentList(Generic[T]):
    def __init__(self, iterable: List[T]):
        self._list = iterable

    def map(self, func: Callable[[T], U]) -> 'FluentList[U]':
        return FluentList(list(map(func, self._list)))

    def filter(self, func: Callable[[T], bool]) -> 'FluentList[T]':
        return FluentList(list(filter(func, self._list)))

    def reduce(self, func: Callable[[T, T], T], initial: T) -> T:
        return reduce(func, self._list, initial)

    def fold(self, if_empty: Callable[[], U], if_non_empty: Callable[[List[T]], U]) -> U:
        if not self._list:
            return if_empty()
        else:
            return if_non_empty(self._list)

    def foldLeft(self, initial: U) -> Callable[[Callable[[U, T], U]], U]:
        def inner_fold(func: Callable[[U, T], U]) -> U:
            res = initial
            for item in self._list:
                res = func(res, item)
            return res

        return inner_fold

    def to_list(self) -> List[T]:
        return self._list


# Example usage
def increment(x: int) -> int:
    return x + 1


def is_even(x: int) -> bool:
    return x % 2 == 0


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]

    # Fluent list operations
    result: FluentList[int] = (
        FluentList(data)
        .map(increment)
        .filter(is_even)
    )

    def add(x: int, y: int) -> int:
        return x + y

    foldLeft_with_initial = FluentList(data).foldLeft(0)(add)
    foldLeft_with_initial_2 = foldLeft_with_initial

    print(foldLeft_with_initial)  # Output: [2, 4, 6]

    print(result)  # Output: [2, 4, 6]

    # Using reduce
    sum_result = FluentList(data) \
        .reduce(lambda x, y: x + y, 0)

    print(sum_result)  # Output: 15

    # Using fold
    fold_result = FluentList(data) \
        .fold(lambda: "List is empty", lambda lst: f"List has {len(lst)} elements")

    print(fold_result)  # Output: List has 5 elements
