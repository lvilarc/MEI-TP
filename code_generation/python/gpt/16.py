from typing import List

def remove_duplicates(nums: List[int]) -> List[int]:
    seen = set()
    result = []

    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)

    return result

arr = [4, 2, 4, 3, 2, 1, 3]
print(remove_duplicates(arr))
