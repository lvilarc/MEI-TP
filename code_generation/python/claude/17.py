def second_largest(arr: list[int]) -> int:
    first = second = float('-inf')
    for num in arr:
        if num > first:
            second, first = first, num
        elif first > num > second:
            second = num
    return second if second != float('-inf') else -1

second_largest([4, 1, 7, 3, 7, 4])  # → 4  (unique: {1,3,4,7}, remove 7 → max is 4)
second_largest([9, 9, 9])            # → -1 (only one unique value)
second_largest([10, 20, 30])         # → 20 (unique: {10,20,30}, remove 30 → max is 20)
second_largest([5])                  # → -1 (only one element)
second_largest([])                   # → -1 (empty array)