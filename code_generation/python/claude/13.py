def are_anagrams(s1: str, s2: str) -> bool:
    return sorted(s1.lower()) == sorted(s2.lower())

# Examples
print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("Race", "Care"))      # True
print(are_anagrams("hello", "world"))    # False