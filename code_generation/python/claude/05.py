def is_palindrome(s: str) -> bool:
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]

print(is_palindrome("Racecar"))   # True
print(is_palindrome("Madam"))     # True
print(is_palindrome("Python"))    # False
print(is_palindrome("Level"))     # True