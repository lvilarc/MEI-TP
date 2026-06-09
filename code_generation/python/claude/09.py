def reverse_string_in_place(s: str) -> str:
    chars = list(s)          # Convert to mutable list
    start, end = 0, len(chars) - 1

    while start < end:
        chars[start], chars[end] = chars[end], chars[start]  # Swap
        start += 1
        end -= 1

    return "".join(chars)    # Convert back to string


# --- Examples ---
print(reverse_string_in_place("hello"))    # "olleh"
print(reverse_string_in_place("Python"))   # "nohtyP"
print(reverse_string_in_place("racecar"))  # "racecar"
print(reverse_string_in_place(""))         # ""
print(reverse_string_in_place("a"))        # "a"