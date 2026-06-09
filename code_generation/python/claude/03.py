def bubble_sort_optimized(arr):
    n = len(arr)
    for i in range(n):
        swapped = False                      # Early-exit flag
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:                      # No swaps = already sorted
            break
    return arr

# Example
arr = [5, 1, 4, 2, 8]
print(bubble_sort_optimized(arr))
# Output: [1, 2, 4, 5, 8]