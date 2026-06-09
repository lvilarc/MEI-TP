from typing import Sequence, TypeVar

T = TypeVar("T")


def binary_search(array: Sequence[T], target: T) -> int:
    """
    Return the index of target in a sorted array.

    If target is not found, return -1.

    Assumes array is sorted in ascending order.
    """
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

numbers = [1, 3, 5, 7, 9, 11]

print(binary_search(numbers, 7))   # 3
print(binary_search(numbers, 2))   # -1