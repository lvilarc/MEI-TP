def reverse_string_in_place(chars: list[str]) -> None:
    """
    Reverses a list of characters in-place.

    Example:
        chars = ["h", "e", "l", "l", "o"]
        reverse_string_in_place(chars)
        print(chars)  # ["o", "l", "l", "e", "h"]
    """
    left = 0
    right = len(chars) - 1

    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
text = "hello"

chars = list(text)
reverse_string_in_place(chars)

reversed_text = "".join(chars)

print(reversed_text)  # "olleh"