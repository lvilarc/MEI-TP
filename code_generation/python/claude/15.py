def calculate_stats(numbers: list) -> dict:
    if not numbers:
        raise ValueError("The list must not be empty.")

    # Arithmetic Mean
    mean = sum(numbers) / len(numbers)

    # Median
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2

    if n % 2 == 1:
        median = sorted_nums[mid]           # Odd count: exact middle
    else:
        median = (sorted_nums[mid - 1] + sorted_nums[mid]) / 2  # Even count: average of two middle values

    return {"mean": mean, "median": median}

print(calculate_stats([3, 1, 4, 1, 5, 9, 2, 6]))
# {'mean': 3.875, 'median': 3.5}

print(calculate_stats([7, 2, 10, 9]))
# {'mean': 7.0, 'median': 8.0}