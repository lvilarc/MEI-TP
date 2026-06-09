def sum_digits(n: int) -> int:
    """Return the sum of the digits of an integer."""
    return sum(int(digit) for digit in str(abs(n)))

print(sum_digits(12345))   # 15
print(sum_digits(-908))    # 17