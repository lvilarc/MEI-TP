def count_vowels(s: str) -> int:
    return sum(1 for char in s.lower() if char in "aeiou")

print(count_vowels("Hello World"))   # 3
print(count_vowels("PYTHON"))        # 1
print(count_vowels("aeiou"))         # 5
print(count_vowels("bcdfg"))         # 0