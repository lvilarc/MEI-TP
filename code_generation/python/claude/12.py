def find_min_max(arr):
    if not arr:
        raise ValueError("Array must not be empty")
    return min(arr), max(arr)

# Example usage
arr = [23, 45, 12, 56, 78, 34]
minimum, maximum = find_min_max(arr)
print(f"Min: {minimum}, Max: {maximum}")  # Min: 12, Max: 78