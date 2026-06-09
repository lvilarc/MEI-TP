from typing import List, Tuple

def find_min_max(numbers: List[int]) -> Tuple[int, int]:
    """
    Returns the minimum and maximum elements in an integer array.

    Raises:
        ValueError: If the array is empty.
    """
    if not numbers:
        raise ValueError("Array cannot be empty")

    minimum = numbers[0]
    maximum = numbers[0]

    for num in numbers[1:]:
        if num < minimum:
            minimum = num
        elif num > maximum:
            maximum = num

    return minimum, maximum

arr = [12, 4, 9, -3, 25, 0]

minimum, maximum = find_min_max(arr)

print("Minimum:", minimum)
print("Maximum:", maximum)