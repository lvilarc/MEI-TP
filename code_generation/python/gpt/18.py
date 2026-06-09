def count_vowels(text: str) -> int:
    """Count the number of vowels in a string, case-insensitively."""
    vowels = {"a", "e", "i", "o", "u"}
    return sum(1 for char in text.lower() if char in vowels)


# Example usage
print(count_vowels("Hello, World!"))  # 3
print(count_vowels("PYTHON"))         # 1
print(count_vowels("AEIOU"))          # 5
