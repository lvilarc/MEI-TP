from typing import Iterable


def mean_and_median(values: Iterable[float]) -> tuple[float, float]:
    """
    Calculate the arithmetic mean and median of a list of numbers.

    Args:
        values: An iterable of numeric values.

    Returns:
        A tuple containing:
        - arithmetic mean
        - median

    Raises:
        ValueError: If the input is empty.
        TypeError: If the input contains non-numeric values.
    """
    numbers = list(values)

    if not numbers:
        raise ValueError("The list of numbers cannot be empty.")

    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("All values must be numbers.")

    mean = sum(numbers) / len(numbers)

    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    middle = n // 2

    if n % 2 == 1:
        median = sorted_numbers[middle]
    else:
        median = (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2

    return mean, median

numbers = [10, 2, 5, 8, 3]

mean, median = mean_and_median(numbers)

print("Mean:", mean)
print("Median:", median)