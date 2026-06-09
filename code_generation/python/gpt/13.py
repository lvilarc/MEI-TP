from collections import Counter

def are_anagrams(str1: str, str2: str) -> bool:
    """
    Check whether two strings are anagrams of each other.

    This version is case-sensitive and includes spaces/punctuation.
    """
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Both inputs must be strings")

    return Counter(str1) == Counter(str2)

print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("hello", "world"))    # False
