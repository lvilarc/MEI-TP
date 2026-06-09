def remove_duplicates(arr: list[int]) -> list[int]:
    seen = set()
    result = []
    for x in arr:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result

# Example
print(remove_duplicates([4, 2, 7, 2, 4, 1, 7, 3]))
# Output: [4, 2, 7, 1, 3]