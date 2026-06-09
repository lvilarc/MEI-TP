from typing import List

def bubble_sort(numbers: List[int]) -> List[int]:
    """
    Sorts a list of integers in ascending order using Bubble Sort.

    Returns a new sorted list and does not modify the original list.
    """
    arr = numbers.copy()
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no elements were swapped, the list is already sorted
        if not swapped:
            break

    return arr


# Example usage
values = [64, 34, 25, 12, 22, 11, 90]
sorted_values = bubble_sort(values)

print(sorted_values)