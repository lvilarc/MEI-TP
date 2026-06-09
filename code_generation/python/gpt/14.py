def decimal_to_binary(n: int) -> str:
    """
    Convert a non-negative decimal integer to its binary representation.

    Args:
        n: A non-negative integer.

    Returns:
        A string containing the binary representation of n.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")

    if n < 0:
        raise ValueError("Input must be non-negative")

    if n == 0:
        return "0"

    bits = []

    while n > 0:
        bits.append(str(n % 2))
        n //= 2

    return "".join(reversed(bits))


# Examples
print(decimal_to_binary(0))   # 0
print(decimal_to_binary(5))   # 101
print(decimal_to_binary(10))  # 1010
print(decimal_to_binary(42))  # 101010
