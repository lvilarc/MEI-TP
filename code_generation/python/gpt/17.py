from typing import List

def second_largest_unique(nums: List[int]) -> int:
    largest = None
    second_largest = None

    for num in nums:
        # Skip duplicates of values already tracked
        if num == largest or num == second_largest:
            continue

        if largest is None or num > largest:
            second_largest = largest
            largest = num
        elif second_largest is None or num > second_largest:
            second_largest = num

    return second_largest if second_largest is not None else -1

print(second_largest_unique([5, 1, 3, 5, 2]))   # 3
print(second_largest_unique([4, 4, 4]))         # -1
print(second_largest_unique([10]))              # -1
print(second_largest_unique([2, 1]))            # 1
print(second_largest_unique([-1, -2, -3]))      # -2