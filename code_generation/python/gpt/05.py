def is_palindrome(text: str) -> bool:
    """
    Check whether a string is a palindrome, ignoring case.

    Example:
        is_palindrome("Racecar") -> True
        is_palindrome("Hello") -> False
    """
    normalized = text.lower()
    return normalized == normalized[::-1]

print(is_palindrome("Racecar"))  # True
print(is_palindrome("hello"))    # False
print(is_palindrome("Madam"))    # True