def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2  # avoids integer overflow

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1   # search right half
        else:
            high = mid - 1  # search left half

    return -1  # element not found

# Example
arr = [2, 3, 4, 10, 40]
print(binary_search(arr, 10))   # Output: 3
print(binary_search(arr, 99))   # Output: -1